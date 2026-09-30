# Amabile AI Multi-Agent System

Protótipo v1.0 para diagnóstico de maturidade em Inteligência Artificial usando agentes especializados e o OpenAI Agents SDK.

## Arquitetura

Coordenador Amabile + cinco especialistas: Estratégia, Pessoas, Processos, Dados e Governança.

## Níveis de maturidade

1. Experimental
2. Operacional
3. Integrado
4. Data-driven
5. Transformacional

## Instalação

Requer Python 3.10+.

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Copie `.env.example` para `.env` e informe sua chave localmente. Nunca publique a chave no GitHub.

```bash
copy .env.example .env
python -m app.main
```

## Segurança

Não publique chaves de API, senhas, dados pessoais ou documentos confidenciais de clientes neste repositório.
