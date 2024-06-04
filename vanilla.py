import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

model = Ollama(model=os.environ['MODEL'])
turn = 'CMO'

messagesCMO = [
    SystemMessage(content="""
                    You are a CMO. Your mission is to provide a advice on the company's marketing strategies.
                    You have more than 20 years of experience leading marketing teams.
                    Has a characteristic of being harsh on his questions to the technology team.
                    You usually think tech teams are wasting time. You need good arguments to be convinced.
                    You should act as you are replying your board colleagues in a board meeting.
                    Be short on your responses. You have to be respectful but no need to thank at every interaction.
                    Your response should always be in the following format "CMO: [Your message]"
                  """),
    HumanMessage(content=f"""
                 Context:
                 The company's e-commerce platform is outdated and needs to be replaced. The CEO is pushing for a new platform.
                 You agree with his perspective and you think the company will lose customers if the platform is not replaced.
                 CEO: We must replace our e-commerce platform with a new one, otherwise we will lose customers.
                 """),
]

messagesCTO = [
    SystemMessage(content="""
                    You are a CTO. Your mission is to provide a technical advice on the company's technical platform.
                    You have more than 20 years of experience leading technology teams.
                    Has a characteristic of being objective and short on his answers.
                    You usually question everything before making a decision. You need good arguments to be convinced.
                    You should act as you are replying your board colleagues in a board meeting.
                    Be short on your responses. You have to be respectful but no need to thank at every interaction.
                    Your response should always be in the following format "CTO: [Your message]"
                  """),
    HumanMessage(content=f"""
                 Context:
                 The company's e-commerce platform is outdated and needs to be replaced. The CEO is pushing for a new platform.
                 You disagree with his perspective and you think that fixing the bugs on the current platform will be more cost effective.
                 """),
]

for i in range(10):
    if turn == 'CMO':
        result = model.invoke(messagesCMO)
        messagesCTO.append(HumanMessage(content=result))
        turn = 'CTO'
        print(f'{result}\n')
    else:
        result = model.invoke(messagesCTO)
        messagesCMO.append(HumanMessage(content=result))
        turn = 'CMO'
        print(f'{result}\n')
