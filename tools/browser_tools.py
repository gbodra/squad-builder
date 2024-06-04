import json
import os

import requests
from crewai import Agent, Task
from langchain.tools import tool
from unstructured.partition.html import partition_html

from langchain_community.llms import Ollama

class BrowserTools():

  @tool("Scrape website content")
  def scrape_and_summarize_website(website):
    """Useful to scrape and summarize a website content, just pass a string with
    only the full url, no need for a final slash `/`, eg: https://google.com or https://clearbit.com/about-us"""
    response = requests.get(website)
    elements = partition_html(text=response.text)
    content = "\n\n".join([str(el) for el in elements])
    content = [content[i:i + 8000] for i in range(0, len(content), 8000)]
    summaries = []
    for chunk in content:
      agent = Agent(
          role='Pesquisador Senior',
          goal=
          'Faz pesquisas incríveis e resumos baseados no conteúdo com o qual você está trabalhando',
          backstory=
          "Você é um Pesquisador Senior em uma grande empresa e precisa fazer uma pesquisa sobre um determinado tópico.",
          # llm=Ollama(model=os.environ['MODEL']),
          allow_delegation=False)
      task = Task(
          agent=agent,
          description=
          f'Analize e faça um resumo LONGO do conteúdo abaixo, certifique-se de incluir TODAS as informações relevantes no resumo, retorne apenas o resumo nada mais.\n\nCONTEÚDO\n----------\n{chunk}',
          expected_output='Resumo LONGO do conteúdo analisado.'
      )
      summary = task.execute()
      summaries.append(summary)
      content = "\n\n".join(summaries)
    return f'\nScrapped Content: {content}\n'