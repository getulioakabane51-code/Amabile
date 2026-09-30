QUESTIONS = {
    "strategy": [
        "A organização possui objetivos de IA ligados à estratégia de negócio?",
        "Existem casos de uso priorizados por valor e viabilidade?",
        "Há indicadores para medir valor gerado pela IA?",
    ],
    "people": [
        "A liderança compreende oportunidades e riscos da IA?",
        "Há programa de capacitação por perfil profissional?",
        "Existem papéis e responsabilidades claros para iniciativas de IA?",
    ],
    "processes": [
        "Os processos prioritários estão documentados e mensurados?",
        "A IA está integrada a processos ou é usada apenas de forma individual?",
        "Existem mecanismos de supervisão humana nas automações relevantes?",
    ],
    "data": [
        "Os dados necessários aos casos de uso estão identificados e acessíveis?",
        "Há controles de qualidade, propriedade e segurança dos dados?",
        "As fontes de dados estão suficientemente integradas?",
    ],
    "governance": [
        "Existe política ou estrutura de governança de IA?",
        "Riscos, privacidade, segurança e ética são avaliados antes da implantação?",
        "Modelos e agentes são monitorados após entrarem em produção?",
    ],
}


def render_questionnaire() -> str:
    lines = ["QUESTIONÁRIO AMABILE AI — MATURIDADE EM IA", ""]
    for dimension, questions in QUESTIONS.items():
        lines.append(dimension.upper())
        for index, question in enumerate(questions, 1):
            lines.append(f"{index}. {question}")
        lines.append("")
    return "\n".join(lines)
