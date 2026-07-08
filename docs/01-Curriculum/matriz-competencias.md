# Matriz de Competências — Programação Agêntica

> **Proposta de adição** ao Framework de Competências da Universidade Etho, área **Inteligência Artificial**.
> Cada competência é medida em 3 níveis: **B**ásico · **I**ntermediário · **A**vançado.

Estas competências complementam as já existentes (Machine Learning, Deep Learning, NLP, LLMs & Prompt Engineering, MLOps, IA Generativa Aplicada, RAG Systems) e cobrem o espectro específico da **Programação Agêntica**.

---

## Competência 1 — Programação Agêntica

A capacidade de **arquitetar, implementar e operar agentes LLM** — desde o bloco fundamental (Augmented LLM em loop) até sistemas de produção.

| Nível | Descrição |
|---|---|
| **B** | Compreende o agent loop (perceive → think → act); implementa um agente ReAct simples em 1 framework; diferencia workflow de agente. |
| **I** | Compõe os 5 workflows (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer); modela ACI eficaz; usa observabilidade básica (traces). |
| **A** | **Arquiteta** sistemas de agentes de produção: trade-offs de custo/latência, padrões de recuperação de falhas, design de toolsets complexos, escolha fundamentada entre workflows e agentes autônomos. |

**Módulos que desenvolvem**: `ETHAGT01`, `ETHAGT02`, `ETHAGT03`, `ETHAGT12`, `ETHAGT14`.

## Competência 2 — Multi-Agent Systems

A capacidade de projetar **sistemas compostos por múltiplos agentes** que colaboram, coordenam e dividem trabalho.

| Nível | Descrição |
|---|---|
| **B** | Conhece topologias básicas (supervisor, sequential); implementa 2 agentes coordenados; entende protocolos de mensagem simples. |
| **I** | Implementa topologias hierarchical, orchestrator-workers e swarm; lida com negociação e resolução de conflitos; usa filas/eventos para coordenação. |
| **A** | **Projeta** sociedades de agentes distribuídas: escolhe topologia com base em requisitos (consistência, latência, custo); implementa blackboard / actor model / agent mesh; avalia emergência e_convergência. |

**Módulos que desenvolvem**: `ETHAGT09`, `ETHAGT10`, `ETHAGT11`, `ETHAGT15`, `ETHAGT16`, `ETHAGT90`.

## Competência 3 — MCP & Tool Use

A capacidade de **modelar, construir e governar** a interface entre agentes e sistemas externos.

| Nível | Descrição |
|---|---|
| **B** | Usa MCP servers existentes; define tools com schemas claros; entende o custo de tool calls. |
| **I** | Constrói MCP servers customizados; modela ACI seguindo os princípios de Anthropic (poka-yoke, exemplos, absolute paths); versiona tools. |
| **A** | **Define governança** de ecossistema de ferramentas: catálogo, permissões, auditoria, supply chain security, estratégia multi-host. |

**Módulos que desenvolvem**: `ETHAGT02`, `ETHAGT08`, `ETHAGT13`.

## Competência 4 — Agent Memory

A capacidade de arquitetar **sistemas de memória** que dão a agentes persistência, contexto e aprendizado acumulado.

| Nível | Descrição |
|---|---|
| **B** | Entende context window e limites; usa memória de curta duração (sessão). |
| **I** | Implementa memória persistente via checkpointer (Postgres/Redis); diferencia memória episódica/semântica/procedural; gerencia janela deslizante. |
| **A** | **Arquiteta** estratégia de memória multi-camada: vector store + graph + relacional + cache; lida com consistência, evicção, privacidade e custo. |

**Módulos que desenvolvem**: `ETHAGT05`, `ETHAGT07`, `ETHAGT14`.

## Competência 5 — AgentOps & Avaliação

A capacidade de **observar, medir, avaliar e melhorar** sistemas de agentes com rigor experimental.

| Nível | Descrição |
|---|---|
| **B** | Roda traces básicos; avalia outputs manualmente; entende métricas de LLM (precision/recall para tasks). |
| **I** | Monta evals automatizados com LLM-as-judge; usa tooling (LangSmith, Phoenix, Langfuse); implementa testes de regressão para prompts/tools. |
| **A** | **Define benchmarks** (SWE-bench, GAIA, τ-bench, AgentBench, WebArena), calcula custos, implementa observabilidade end-to-end, conduz estudos comparativos. |

**Módulos que desenvolvem**: `ETHAGT12`, `ETHAGT06` (RAG eval), `ETHAGT90`.

## Competência 6 — Agent Security & Governance

A capacidade de **proteger agentes e governar** seu comportamento em ambientes adversariais e regulados.

| Nível | Descrição |
|---|---|
| **B** | Conhece prompt injection e riscos básicos; aplica filtros de entrada/saída; entende o princípio do menor privilégio. |
| **I** | Aplica guardrails (constitutions, structured outputs, tool allowlists); implementa Human-in-the-Loop em checkpoints críticos; roda DAST em tools. |
| **A** | **Lidera red team** de agentes, define policy-as-code, arquiteta governança para agentes autônomos (auditoria, explicabilidade, conformidade regulatória). |

**Módulos que desenvolvem**: `ETHAGT13`, `ETHAGT15`, `ETHAGT90`.

---

## Resumo visual

| Competência | Foco | Diferencia Etho? |
|---|---|---|
| Programação Agêntica | Bloco fundamental + agent loop | Base |
| Multi-Agent Systems | **Ênfase** — sociedades, pesquisa autônoma | **Sim — diferenciação forte** |
| MCP & Tool Use | Interface agente ↔ mundo | Sim — alinhado ao ecossistema MCP |
| Agent Memory | Persistência e aprendizado | Sim — pouco coberto no mercado |
| AgentOps & Avaliação | Rigor de produção | Sim — gap claro no mercado |
| Agent Security | Confiança e governança | Sim — crítico para enterprise |

---

*Relacionado: [`grade-curricular.md`](grade-curricular.md) · [`mapa-competencias-modulos.md`](mapa-competencias-modulos.md) · Framework de Competências Etho (Confluence `UE`)*
