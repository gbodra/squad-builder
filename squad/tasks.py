from crewai import Task
from datetime import datetime

current_year = datetime.now().year

class SignalTasks:
    def ResearchTech(self, agent, context):
        return Task(description=f"""
                    Faça uma pesquisa abrangente sobre notícias relacionadas ao mercado de tecnologia,
                    novas tecnologias, novos softwares e serviços.
                    Você pode usar a internet para encontrar informações relevantes e deve buscar notícias
                    de fontes confiáveis e respeitadas.
                    Reporte somente os fatos, não faça suposições ou especulações.
                    Estamos no ano {current_year}.
                    Adapte a sua pesquisa ao contexto a seguir: {context}""",
                    expected_output=f"""
                    Uma lista com as principais notícias e um resumo de 1 parágrafo para cada notícia.
                    """,
			        agent=agent)
    
    def ResearchBusiness(self, agent, context, previous_tasks):
        return Task(description=f"""
                    Faça uma pesquisa abrangente sobre notícias relacionadas ao mercado de negócios,
                    novos modelos de negócio, novos produtos e serviços.
                    Você pode usar a internet para encontrar informações relevantes e deve buscar notícias
                    de fontes confiáveis e respeitadas.
                    Reporte somente os fatos, não faça suposições ou especulações.
                    Estamos no ano {current_year}.
                    Adapte a sua pesquisa ao contexto a seguir: {context}""",
                    expected_output=f"""
                    Uma lista com as principais notícias e um resumo de 1 parágrafo para cada notícia.
                    """,
                    context=previous_tasks,
			        agent=agent)

    def ResearchManagement(self, agent, context, previous_tasks):
        return Task(description=f"""
                    Faça uma pesquisa abrangente sobre notícias relacionadas a gestão de negócios,
                    novas técnicas de gestão, novos frameworks e modelos.
                    Você pode usar a internet para encontrar informações relevantes e deve buscar notícias
                    de fontes confiáveis e respeitadas.
                    Reporte somente os fatos, não faça suposições ou especulações.
                    Estamos no ano {current_year}.
                    Adapte a sua pesquisa ao contexto a seguir: {context}""",
                    expected_output=f"""
                    Uma lista com as principais notícias e um resumo de 1 parágrafo para cada notícia.
                    """,
                    context=previous_tasks,
			        agent=agent)

    def BuildKnowledgeGraph(self, agent, context, previous_tasks):
        return Task(description=f"""
                    Ler e analisar os conteúdos preparados pelos agentes de pesquisa de mercado, 
                    pesquisa de tecnologia e pesquisa de gestão. A principal responsabilidade é 
                    identificar conexões não óbvias entre esses diferentes conteúdos e gerar um 
                    grafo de conhecimento que explore até três níveis de profundidade nas conexões.

                    Tarefa:
                    Receber e revisar as pesquisas realizadas pelos agentes de pesquisa de mercado, tecnologia e gestão.
                    Identificar e mapear conexões não óbvias entre os diferentes estudos.
                    Organizar essas conexões em um grafo de conhecimento, explorando até três níveis de profundidade nas implicações.
                    Estamos no ano {current_year}.
                    Adapte sua análise ao contexto a seguir: {context}""",
                    expected_output=f"""
                    A saída deve ser somente o grafo no formato Mermaid, sem nenhuma outra informação adicional.
                    """,
                    context=previous_tasks,
                    output_file='graph.md',
			        agent=agent)

    def FindNonObviousInsights(self, agent, context, previous_tasks):
        return Task(description=f"""
                    Ler o grafo de conhecimento gerado pelo Analista de Conexões de Pesquisa e, 
                    a partir dele, identificar e gerar insights de negócio acionáveis. 
                    Esses insights devem ser objetivos, claros e relevantes, permitindo que 
                    executivos possam discutir e adaptar suas estratégias de negócio de maneira prática e eficiente.

                    Tarefa:
                    - Receber e revisar o grafo de conhecimento gerado pelo Analista de Conexões de Pesquisa.
                    - Interpretar as conexões e padrões identificados no grafo, extraindo informações relevantes.
                    - Gerar insights de negócio acionáveis e objetivos, focados em estratégias práticas e 
                    adaptações necessárias para preparar a organização para mudanças emergentes.
                    - Garantir que os insights sejam apresentados de forma clara e sem futurismo, focando em ações 
                    concretas que os executivos possam discutir e implementar.
                    Estamos no ano {current_year}.
                    Adapte sua análise ao contexto a seguir: {context}""",
                    expected_output=f"""
                    Lista de insights de negócio acionáveis, apresentada em formato de texto claro e objetivo, 
                    estruturada para fácil compreensão e discussão pelos executivos.
                    Exemplo:
                    1. **Insight 1:** Aumento na demanda por soluções de tecnologia sustentável
                        - **Ação:** Investir em pesquisa e desenvolvimento de produtos eco-friendly
                        - **Impacto:** Posicionamento de mercado como líder em sustentabilidade
                        - **Prazo:** 6-12 meses

                    2. **Insight 2:** Necessidade crescente de capacitação em inteligência artificial nas equipes de TI
                        - **Ação:** Implementar programas de treinamento em IA para colaboradores de TI
                        - **Impacto:** Melhoria na eficiência operacional e inovação tecnológica
                        - **Prazo:** 3-6 meses
                    """,
                    context=previous_tasks,
                    output_file='insights.md',
			        agent=agent)