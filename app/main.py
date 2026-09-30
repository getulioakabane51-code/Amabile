import os
from dotenv import load_dotenv
from agents import Runner
from app.coordinator import coordinator


def main() -> None:
    load_dotenv()
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("Defina OPENAI_API_KEY no arquivo .env antes de executar.")

    print("Amabile AI Multi-Agent System v1.0")
    print("Descreva a organização, contexto, iniciativas atuais de IA, pessoas, processos, dados e governança.")
    context = input("\nContexto da organização:\n> ").strip()
    if not context:
        raise ValueError("Forneça algum contexto para realizar o diagnóstico.")

    prompt = f"""Realize um diagnóstico preliminar Amabile AI com base exclusivamente no contexto abaixo.\n\nCONTEXTO:\n{context}"""
    result = Runner.run_sync(coordinator, prompt)
    print("\n=== DIAGNÓSTICO AMABILE AI ===\n")
    print(result.final_output)


if __name__ == "__main__":
    main()
