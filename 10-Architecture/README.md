# 10 — Architecture

Biblioteca de **arquiteturas** (topologias de sistema multi-agente) + ADRs de implementação.

## Estrutura

- [`architectures/`](architectures) — 12 topologias de referência (v1 em [`catalog.md`](architectures/catalog.md))
- [`adr/`](adr) — ADRs de implementação (use `24-Templates/template-adr.md`)

## As 12 topologias

Single Agent · Supervisor · Hierarchical · Blackboard · Actor Model · Pipeline · Event-Driven · Swarm · Tree of Agents · Recursive · Agent Mesh · Hybrid.

Cada uma documentada em [`architectures/catalog.md`](architectures/catalog.md) com: Estrutura · Quando usar · Quando evitar · Trade-offs · Referências.

## Diferença vs `11-AgentPatterns/` e `13-Workflows/`

- **Aqui (`10-Architecture`)**: topologias de **sistema inteiro** (como agentes se organizam).
- **`11-AgentPatterns`**: papéis **individuais** de agentes (supervisor, planner, critic…).
- **`13-Workflows`**: composições controladas (LLMs em caminhos predefinidos).

**Hierarquia**: padrões **compõem** arquiteturas; workflows são **casos simples** de arquiteturas.

## Profundidade

Aprofundamento das 6 topologias mais usadas (Supervisor, Hierarchical, Swarm, Pipeline, Event-Driven, Mesh) no curso `ETHAGT10`.
