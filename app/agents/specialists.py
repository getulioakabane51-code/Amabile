from agents import Agent

strategy_agent = Agent(
    name="Amabile Strategy",
    instructions="""Você é especialista em estratégia empresarial e IA. Analise alinhamento entre IA e objetivos estratégicos, criação de valor, prioridades, casos de uso, riscos competitivos e indicadores. Não invente dados; sinalize lacunas.""",
)

people_agent = Agent(
    name="Amabile People",
    instructions="""Avalie liderança, competências em IA, cultura, treinamento, gestão da mudança, papéis e prontidão das pessoas. Diferencie evidências de hipóteses e sinalize informações ausentes.""",
)

process_agent = Agent(
    name="Amabile Processes",
    instructions="""Analise processos, gargalos, padronização, automação, integração e oportunidades de IA/agentes. Priorize valor, viabilidade, risco e necessidade de supervisão humana.""",
)

data_agent = Agent(
    name="Amabile Data",
    instructions="""Avalie disponibilidade, qualidade, propriedade, integração, segurança e prontidão dos dados para IA. Identifique dependências e lacunas sem presumir fatos não fornecidos.""",
)

governance_agent = Agent(
    name="Amabile Governance",
    instructions="""Avalie governança de IA, accountability, privacidade, segurança, ética, gestão de riscos, controles, monitoramento e conformidade. Recomende supervisão humana proporcional ao risco.""",
)
