import sys
from nicegui import ui
from io import StringIO
from dotenv import load_dotenv
from simulation import Simulation
from crewai import Agent, Task, Crew

load_dotenv()

# output = StringIO()
# sys.stdout = output

sim = Simulation()

# N_AGENTS = 3
STEPPER_VISIBLE = True
# AGENTS = []
# TASKS = []

@ui.refreshable
def agents_info_ui():
    for i in range(sim.n_agents):
        agent = Agent(
            role='',
            goal='',
            backstory='',
            max_iter=10,
            verbose=True,
            allow_delegation=True,
            cache=True
        )

        with ui.expansion(f'Agent {i+1}', icon='smart_toy').classes('w-full'):
            ui.input('Role').classes('w-full').bind_value_to(agent, 'role')
            ui.input('Goal').classes('w-full').bind_value_to(agent, 'goal')
            ui.textarea('Backstory').classes('w-full').bind_value_to(agent, 'backstory')

        sim.agents.append(agent)

@ui.refreshable
def agents_tasks_ui():
    for i in range(sim.n_agents):
        task = Task(
            description=(''),
            expected_output='',
            agent=None
        )
        
        with ui.expansion(f'Agent {i+1} Task', icon='task').classes('w-full'):
            ui.textarea('Description').classes('w-full').bind_value_to(task, 'description')
            ui.input('Expected Output').classes('w-full').bind_value_to(task, 'expected_output')

        task.agent = sim.agents[i]
        sim.tasks.append(task)

def next_step_refresh_ui(stepper):
    agents_tasks_ui.refresh()
    stepper.next()

def finish_agents_setup(stepper):
    sim.setup_crew()
    stepper.next()

@ui.refreshable
def simulation_ui():
    for i in range(10):
        isSent = i % 2 == 0
        ui.chat_message(f'Hello NiceGUI {i}!', sent=isSent, name='Robot', stamp='now', avatar=f'https://robohash.org/{i}')

with ui.header(elevated=True).style('background-color: #3874c8'):
    ui.label('Squad Builder')

with ui.footer().style('background-color: #3874c8'):
    ui.label('FOOTER')

ui.label('Welcome to Squad Builder. Here you can create your own team of agents.')

with ui.expansion('1. Build your squad', icon='build').classes('w-full shaddow-lg'):
    with ui.stepper().props('vertical').classes('w-full') as stepper:
        stepper.bind_visibility(globals(), 'STEPPER_VISIBLE')
        
        with ui.step('Size of your squad', icon='123'):
            ui.label('How many agents you need?')
            slider = ui.slider(min=0, max=10, value=sim.n_agents).props('label-always')
            slider.bind_value(sim, 'n_agents')
            slider.on_value_change(lambda value: agents_info_ui.refresh())
            
            with ui.stepper_navigation():
                ui.button(icon='done', on_click=stepper.next).props('round').classes('shadow-lg')
        
        with ui.step('Goal of your squad', icon='flag'):
            ui.label('What does this squad need to achieve?')
            ui.textarea('Enter your goal here').classes('w-full')
            
            with ui.stepper_navigation():
                with ui.button(color='green', icon='auto_awesome').props('round').classes('shadow-lg'):
                    ui.tooltip('Improve with AI')
                ui.button(icon='done', on_click=stepper.next).props('round').classes('shadow-lg')
                ui.button(icon='arrow_back', on_click=stepper.previous).props('round flat')

        with ui.step('Define your agents', icon='smart_toy'):
            ui.label('Explain the role of each agent')

            agents_info_ui()
                
            with ui.stepper_navigation():
                ui.button(icon='done', on_click=lambda: next_step_refresh_ui(stepper)).props('round').classes('shadow-lg')
                ui.button(icon='arrow_back', on_click=stepper.previous).props('round flat')

        with ui.step('Define your agent\'s tasks', icon='task'):
            ui.label('What tasks each agent needs to do?')

            agents_tasks_ui()

            with ui.stepper_navigation():
                ui.button(icon='done', on_click=lambda: finish_agents_setup(stepper)).props('round').classes('shadow-lg')
                ui.button(icon='arrow_back', on_click=stepper.previous).props('round flat')

        with ui.step('You are all set', icon='verified'):
            ui.label('You can now start the simulation.')
            with ui.stepper_navigation():
                ui.button(icon='arrow_back', on_click=stepper.previous).props('round flat')

ui.button('Start Simulation', on_click=lambda: sim.run()).props('raised').classes('w-full shadow-lg')

with ui.scroll_area().classes('w-full border shadow-lg'):
    with ui.grid().classes('w-full'):
        simulation_ui()

# output_str = output.getvalue()

ui.run()