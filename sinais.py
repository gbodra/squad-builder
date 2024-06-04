import os
import time
import threading
from nicegui import app, ui
from crewai import Crew, Process
from multiprocessing import Value
from squad.tasks import SignalTasks
from squad.agents import SignalAgents
from dotenv import load_dotenv

load_dotenv()

class Logger:
    def __init__(self, log):
        self.log = log

    def write(self, message):
        self.log.push(message)

    def flush(self):
        pass

    def isatty(self):
        return False

agents = SignalAgents()
tasks = SignalTasks()
spinner_visible = Value('b', False)

def setup_crew():
    print(app.storage.general.get('context'))
    
    # Research new techs
    tech_researcher = agents.ResearcherTech()

    # New techs can create new businesses, research new busienss
    business_researcher = agents.ResearcherBusiness()

    # New businessses need new management, research new management
    management_researcher = agents.ResearcherManagement()

    # All of this has to be summarized in a knowledge graph
    knowledge_agent = agents.ResearchKnowledgeAgent()

    # Then we need to find non obivous insights
    insights_agent = agents.ResearchInsightsAgent()

    # Create tasks
    task_tech = tasks.ResearchTech(tech_researcher, app.storage.general.get('context'))
    task_business = tasks.ResearchBusiness(business_researcher, app.storage.general.get('context'), [task_tech])
    task_management = tasks.ResearchManagement(management_researcher, app.storage.general.get('context'), [task_tech, task_business])
    task_knowledge = tasks.BuildKnowledgeGraph(knowledge_agent, app.storage.general.get('context'), [task_tech, task_business, task_management])
    task_insights = tasks.FindNonObviousInsights(insights_agent, app.storage.general.get('context'), [task_knowledge])

    research_crew = Crew(
        agents=[tech_researcher, business_researcher, management_researcher, knowledge_agent, insights_agent],
        tasks=[task_tech, task_business, task_management, task_knowledge, task_insights],
        verbose=True,
        process=Process.sequential,
        memory=True,
        cache=True,
        max_rpm=100,
        language='pt-br',
        output_log_file='sinais.log'
        )

    research_crew.kickoff()

    # Signal that the crew is done
    spinner_visible.value = False

def kickoff_crew():
    # Clear the done signal and start the crew in a new thread
    spinner_visible.value = True
    threading.Thread(target=setup_crew, daemon=True).start()


if __name__ in {"__main__", "__mp_main__"}:
    @ui.page('/')
    def index():
        app.storage.general['context'] = 'bodra'
        ui.page_title('Squad Builder AI')

        with ui.header(elevated=True).style('background-color: #3874c8'):
            ui.label('Squad Builder')

        with ui.footer().style('background-color: #3874c8'):
            ui.label('FOOTER')

        ui.input(label='Contexto', 
                        placeholder='Digite o contexto da análise de sinais').bind_value_to(app.storage.general, 'context').classes('w-full')

        ui.button('Iniciar análise de sinais', icon='radar', on_click=kickoff_crew).classes('w-full')

        # Create a spinner and bind its visibility to the crew_done event
        spinner = ui.spinner('dots', size='lg', color='red').bind_visibility(spinner_visible, 'value').classes('w-full')

        log = ui.log(max_lines=10000).classes('w-full h-100')

        def update_log():
            while True:
                if os.path.exists('sinais.log'):
                    with open('sinais.log', 'r') as file:
                        content = file.read()
                    log.clear()
                    log.push(f'{content}\n\n')
                time.sleep(5)

        threading.Thread(target=update_log, daemon=True).start()

    ui.run(storage_secret='private key to secure the browser session cookie')