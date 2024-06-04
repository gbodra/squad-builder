import os
from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama

class Simulation:
    def __init__(self):
        self.n_agents = 3
        self.agents = []
        self.tasks = []
        self.crew = None
        self.llm = Ollama(model=os.environ['MODEL'])

    def setup_crew(self):
        self.crew = Crew(
            agents=self.agents,
            tasks=self.tasks,
            memory=True,
            cache=True,
            max_rpm=100,
            share_crew=True,
            # manager_llm=ChatOpenAI(temperature=0, model="gpt-4"),
            manager_llm=Ollama(model=os.environ['MODEL']),
            process=Process.hierarchical
        )

    def run(self):
        print(self.tasks)
        self.crew.kickoff()