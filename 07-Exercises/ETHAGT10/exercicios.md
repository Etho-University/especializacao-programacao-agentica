# ETHAGT10 — Lista de Exercícios

> Curso: Padrões de Arquitetura Multi-Agente. Fixação de conceitos. Use a apostila `04-Apostilas/ETHAGT10/apostila.md` como referência.

## Múltipla escolha

**1. Na topologia Supervisor (LangGraph), o supervisor é essencialmente:**

a) Um vector database
b) Um roteador com tool calls que decide qual worker acionar
c) Um modelo de embeddings
d) Um log de auditoria

**2. Qual topologia é mais adequada quando as subtarefas são dinâmicas e não podem ser pré-determinadas?**

a) Pipeline fixo
b) Orchestrator-Workers / Hierarchical
c) Single Agent
d) Round-robin

**3. Na topologia Swarm (OpenAI), a coordenação é:**

a) Centralizada em um supervisor fixo
b) Descentralizada via handoffs entre agentes leves que transferem controle
c) Baseada em voting
d) Baseada em blackboard

**4. Quando a topologia Hierarchical é melhor que flat (supervisor simples)?**

a) Sempre
b) Quando há múltiplos níveis de especialização (supervisor → workers → sub-workers) que justificam a árvore
c) Quando há poucos agentes
d) Nunca

## Verdadeiro ou Falso (justificado)

**1.** "Mesh é sempre a topologia mais escalável." — Justifique.

**2.** "Recursive (meta-agents) é anti-pattern quando não há necessidade de agentes que criam agentes." — Justifique.

**3.** "O supervisor pode se tornar um gargalo se todas as decisões passarem por ele." — Justifique.

**4.** "A escolha de topologia deve ser documentada em um ADR (Architecture Decision Record)." — Justifique.

## Código curto

**1.** Escreva o esqueleto de um ADR de topologia: Contexto, Decisão, Justificativa, Trade-offs.

**2.** Escreva o pseudocódigo de uma topologia Supervisor com 2 workers (worker_a, worker_b), onde o supervisor roteia por tipo de tarefa.

**3.** Escreva o pseudocódigo de um swarm com handoff: agent_general decide se transfere para agent_specialist.

## Análise de trade-off

**1.** Compare Hierarchical vs. Swarm para revisão de PR com especialistas (frontend, backend, security). Qual escolher?

**2.** Compare Supervisor vs. Blackboard para um sistema dinâmico com especialistas contribuindo incrementalmente. Quando cada?

**3.** Para 3 cenários (atendimento ao cliente com 5 departamentos, pesquisa científica colaborativa, pipeline ETL fixo), qual topologia?

## Debug / diagnóstico

**1.** Em uma topologia hierarchical com supervisor + 3 workers, um worker consistentemente não é acionado. Diagnóstico e correção.

**2.** Um swarm com 5 agentes gera respostas incoerentes — cada agente "refaz" o trabalho do anterior sem continuidade. Diagnóstico do problema de handoff.
