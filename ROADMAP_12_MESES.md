# Roadmap Amabile AI — 12 meses

## Objetivo
Transformar o protótipo Amabile AI em uma solução empresarial de diagnóstico, priorização e acompanhamento da maturidade em IA, mantendo supervisão humana nas decisões relevantes.

## Visão do produto
O sistema combina um Coordenador Amabile com especialistas em Estratégia, Pessoas, Processos, Dados e Governança. O roadmap evolui da validação metodológica para pilotos, integração de conhecimento empresarial, governança e preparação para escala.

## Fase 1 — Fundação e validação (Meses 1–3)

### Mês 1 — Metodologia e arquitetura
- Revisar as cinco dimensões e os cinco níveis de maturidade.
- Definir critérios objetivos de pontuação e evidências mínimas.
- Definir papéis do Coordenador e dos agentes especialistas.
- Criar catálogo inicial de riscos e controles.
- Definir indicadores de sucesso do produto.

**Entregáveis:** metodologia v1.1, matriz de maturidade, arquitetura e KPIs.

### Mês 2 — Questionário e diagnóstico
- Expandir o questionário empresarial.
- Criar respostas estruturadas e validação de dados de entrada.
- Separar fatos, hipóteses e informações ausentes.
- Produzir diagnóstico por dimensão.
- Gerar recomendações vinculadas às evidências.

**Entregáveis:** questionário v2, diagnóstico estruturado e relatório executivo inicial.

### Mês 3 — MVP executável
- Criar fluxo completo: entrada → especialistas → coordenador → relatório.
- Adicionar testes automatizados.
- Registrar consumo e erros das execuções.
- Criar conjunto de casos fictícios para avaliação.
- Documentar instalação e operação.

**Entregáveis:** MVP v1, suíte de testes e documentação técnica.

## Fase 2 — Produto e conhecimento empresarial (Meses 4–6)

### Mês 4 — Interface de usuário
- Criar interface web para preenchimento do diagnóstico.
- Exibir pontuação e nível por dimensão.
- Criar gráfico de maturidade.
- Permitir revisão humana antes do relatório final.

**Entregáveis:** interface web v1 e painel de diagnóstico.

### Mês 5 — RAG e documentos autorizados
- Implementar recuperação de conhecimento sobre documentos empresariais autorizados.
- Definir separação segura por cliente/projeto.
- Exigir indicação das evidências utilizadas no diagnóstico.
- Testar respostas com e sem documentação suficiente.

**Entregáveis:** RAG v1, política de documentos e testes de grounding.

### Mês 6 — Relatório executivo e roadmap automático
- Gerar sumário executivo, gaps, oportunidades, riscos e prioridades.
- Produzir roadmap específico de 12 meses para cada organização.
- Criar exportação estruturada dos resultados.
- Validar relatórios com especialistas humanos.

**Entregáveis:** relatório executivo v2 e gerador de roadmap empresarial.

## Fase 3 — Governança, qualidade e pilotos (Meses 7–9)

### Mês 7 — Guardrails e governança
- Adicionar validações de entrada e saída.
- Definir ações que sempre exigem aprovação humana.
- Criar política de privacidade, retenção e acesso.
- Implementar trilha de auditoria e critérios de revisão.

**Entregáveis:** framework de governança, guardrails e checklist de aprovação.

### Mês 8 — Observabilidade e avaliação
- Implantar tracing das execuções dos agentes.
- Medir qualidade, consistência, latência e custo.
- Criar testes de regressão para prompts e agentes.
- Definir processo de tratamento de falhas e incidentes.

**Entregáveis:** painel de qualidade, conjunto de avaliações e processo de incidentes.

### Mês 9 — Pilotos controlados
- Selecionar organizações-piloto.
- Aplicar diagnóstico com acompanhamento humano.
- Comparar resultado dos agentes com avaliação de especialistas.
- Coletar feedback de executivos e usuários.
- Ajustar metodologia e experiência de uso.

**Entregáveis:** relatório dos pilotos, metodologia v2 e backlog priorizado.

## Fase 4 — Escala e oferta comercial (Meses 10–12)

### Mês 10 — Segurança e preparação para produção
- Revisar autenticação, autorização e segregação de dados.
- Definir ambientes de desenvolvimento, teste e produção.
- Criar procedimentos de backup, continuidade e atualização.
- Realizar revisão técnica e de segurança antes da expansão.

**Entregáveis:** checklist de produção e plano de segurança operacional.

### Mês 11 — Modelo de serviço Amabile AI
- Estruturar pacotes de diagnóstico, roadmap e acompanhamento.
- Integrar trilhas de capacitação para líderes e equipes.
- Criar modelo de acompanhamento trimestral da maturidade.
- Definir indicadores de valor para o cliente.

**Entregáveis:** catálogo de serviços, jornada do cliente e modelo de acompanhamento.

### Mês 12 — Lançamento controlado e ciclo de melhoria
- Consolidar versão 2.0.
- Publicar documentação operacional e metodologia aprovada.
- Estabelecer revisão periódica de agentes, prompts, avaliações e controles.
- Criar plano do segundo ano baseado nos resultados dos pilotos e clientes.

**Entregáveis:** Amabile AI v2.0, documentação final e roadmap do ano 2.

## KPIs sugeridos
- Percentual de diagnósticos revisados/aprovados por especialista humano.
- Consistência entre diagnóstico automatizado e avaliação humana.
- Percentual de afirmações relevantes sustentadas por evidências disponíveis.
- Tempo médio para produzir diagnóstico e roadmap.
- Custo médio por diagnóstico.
- Satisfação do usuário executivo.
- Percentual de recomendações aceitas para análise/implantação pelo cliente.
- Número e gravidade de incidentes de segurança, privacidade ou qualidade.

## Marcos
- **90 dias:** MVP validado.
- **6 meses:** produto com interface, RAG e roadmap automático.
- **9 meses:** pilotos concluídos e metodologia revisada.
- **12 meses:** Amabile AI v2.0 pronta para oferta comercial controlada.

## Princípio de governança
A Amabile AI deve apoiar decisões humanas, não substituir automaticamente decisões executivas de alto impacto. Recomendações devem distinguir evidência, inferência e informação ausente, com revisão humana proporcional ao risco.
