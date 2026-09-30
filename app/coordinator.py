from agents import Agent
from app.agents import strategy_agent, people_agent, process_agent, data_agent, governance_agent

coordinator = Agent(
    name="Amabile AI Coordinator",
    instructions="""
Você coordena o diagnóstico Amabile AI de maturidade em Inteligência Artificial.
Use os especialistas quando necessário e consolide apenas evidências disponíveis.

Entregue:
1. Sumário executivo
2. Diagnóstico por dimensão
3. Pontos fortes
4. Lacunas e dados ausentes
5. Oportunidades priorizadas
6. Riscos e controles
7. Nível preliminar de maturidade (1 a 5), justificando pelas evidências
8. Recomendações
9. Roadmap de 12 meses dividido em 0-90 dias, 3-6 meses e 6-12 meses

Níveis: 1 Experimental; 2 Operacional; 3 Integrado; 4 Data-driven; 5 Transformacional.
Não invente informações. Quando a evidência for insuficiente, declare que o nível é preliminar e solicite os dados necessários.
""",
    tools=[
        strategy_agent.as_tool(tool_name="strategy_analysis", tool_description="Analisa estratégia e valor de negócio."),
        people_agent.as_tool(tool_name="people_analysis", tool_description="Analisa pessoas, liderança, competências e cultura."),
        process_agent.as_tool(tool_name="process_analysis", tool_description="Analisa processos e automação."),
        data_agent.as_tool(tool_name="data_analysis", tool_description="Analisa dados e prontidão informacional."),
        governance_agent.as_tool(tool_name="governance_analysis", tool_description="Analisa governança, riscos e controles de IA."),
    ],
)
