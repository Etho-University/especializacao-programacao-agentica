# 11 — Agent Patterns

Biblioteca de **23 padrões de projeto** para agentes (papéis individuais). Inspirada no espírito de *Design Patterns* (GoF), adaptada para Agentic AI.

## Status: v1 (catálogo consolidado)

A v1 está em [`catalog.md`](catalog.md) — todos os 23 padrões documentados em um arquivo, cada um com: **Intenção** · **Estrutura** · **Quando usar** · **Anti-patterns** · **Custo** · **Referências**.

Sprint futuro: dividir cada padrão em arquivo próprio (`<nome>.md`) com exemplos de código runnable.

## Catálogo (23 padrões)

### A — Orquestração
1. **Supervisor** — orquestra workers via tool calls
2. **Orchestrator** — delegação dinâmica + síntese
3. **Coordinator** — media comunicação, mantém state
4. **Router** — classifica e direciona

### B — Planejamento e Execução
5. **Planner** — decompõe objetivo em passos
6. **Executor** — opera passos do plano
7. **Scheduler** — agenda e prioriza
8. **Recovery Agent** — recupera de falhas

### C — Avaliação e Melhoria
9. **Critic** — avalia em loop
10. **Evaluator** — mede contra critérios
11. **Reviewer** — revisão iterativa
12. **Reflection Agent** — auto-crítica + aprendizado

### D — Informação e Memória
13. **Researcher** — busca e recupera
14. **Retrieval Agent** — RAG agêntico especializado
15. **Memory Manager** — gerencia memória do sistema
16. **Observer** — observa e emite métricas

### E — Governança e Segurança
17. **Guardian** — guardrails e veto
18. **Meta-Governor** — define/revisa políticas

### F — Meta-Agência e Evolução
19. **Strategy Evolver** — evolui estratégias/prompts
20. **Learning Agent** — aprende com experiência
21. **Simulation Agent** — simula cenários
22. **Negotiation Agent** — negocia entre partes
23. **Tool Agent** — encapsula domínio de tools

## Mapa rápido "preciso de…"

| Situação | Padrão |
|---|---|
| Orquestrar workers | Supervisor / Orchestrator / Coordinator |
| Rotear | Router |
| Planejar/executar | Planner + Executor + Scheduler |
| Avaliar/melhorar | Critic / Evaluator / Reviewer / Reflection |
| Recuperar info | Researcher / Retrieval Agent |
| Memória | Memory Manager / Observer |
| Segurança | Guardian / Meta-Governor |
| Evoluir sistema | Strategy Evolver / Learning Agent |
| Recuperar falhas | Recovery Agent |

## Diferença vs `10-Architecture/` e `13-Workflows/`

- **Aqui (`11-AgentPatterns`)**: papéis **individuais** de agentes.
- **`10-Architecture/`**: topologias de **sistema inteiro** (como os agentes se organizam).
- **`13-Workflows/`**: composições controladas (LLMs em caminhos predefinidos).

Padrões **compõem** arquiteturas e workflows.
