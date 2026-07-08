# ETHAGT90 — Starter Code (estrutura inicial)

> Estrutura **sugerida** para o repositório do Capstone. Você pode adaptar — desde que atenda ao enunciado.

```
capstone-autoresearch/
├── README.md                      # como rodar, testar, avaliar
├── docker-compose.yml             # sobe toda a stack
├── .env.example                   # variáveis (sem segredos)
├── pyproject.toml                 # dependências Python
│
├── src/
│   ├── agents/
│   │   ├── supervisor.py          # supervisor geral (planner + router)
│   │   ├── orchestrator.py        # orchestrator-workers
│   │   ├── researchers/
│   │   │   ├── arxiv.py           # usa arxiv-mcp
│   │   │   ├── github.py          # usa github-mcp
│   │   │   └── kb.py              # usa confluence-mcp + RAG
│   │   ├── synthesizer.py
│   │   ├── evaluator.py           # evaluator-optimizer
│   │   ├── writer.py
│   │   └── publisher.py
│   │
│   ├── mcp_servers/
│   │   ├── arxiv_server.py        # FastMCP server p/ arXiv
│   │   ├── github_server.py       # FastMCP server p/ GitHub
│   │   └── confluence_server.py   # FastMCP server p/ Confluence
│   │
│   ├── memory/
│   │   ├── checkpointer.py        # Postgres checkpointer
│   │   ├── episodic.py            # Qdrant
│   │   ├── semantic.py            # Postgres relacional
│   │   └── procedural.py          # skills JSON
│   │
│   ├── rag/
│   │   ├── adaptive.py            # adaptive RAG
│   │   ├── reranker.py
│   │   └── hybrid.py              # vector + graph
│   │
│   ├── security/
│   │   ├── input_filter.py
│   │   ├── output_filter.py
│   │   ├── guardrails.py
│   │   └── policies/              # OPA rego files
│   │
│   ├── observability/
│   │   ├── tracer.py              # Phoenix/OTel
│   │   └── cost_meter.py
│   │
│   ├── events/
│   │   ├── bus.py                 # NATS publisher/consumer
│   │   └── saga.py                # saga compensatória
│   │
│   └── workflow/
│       └── temporal.py            # durable execution
│
├── eval/
│   ├── benchmark/                 # ≥30 perguntas curadas
│   │   ├── questions.json
│   │   └── ideal_answers.json
│   ├── golden_cases/              # casos com resposta ideal
│   ├── llm_judge.py               # evaluator automatizado
│   └── run_eval.py                # script de rerun
│
├── red_team/
│   ├── cases/                     # ≥10 casos de ataque
│   └── run_redteam.py
│
├── docs/
│   ├── adr/                       # ≥3 ADRs
│   │   ├── 001-topology.md
│   │   ├── 002-event-bus.md
│   │   └── 003-durable-execution.md
│   ├── architecture/              # diagramas C4 (mermaid)
│   ├── threat-model.md
│   ├── privacy-policy.md
│   └── eval-report.md             # relatório de avaliação final
│
└── tests/
    ├── unit/
    ├── integration/
    └── chaos/                     # testes de resiliência
```

## Como começar (semana 1)

```bash
mkdir capstone-autoresearch && cd capstone-autoresearch
git init
# Copie esta estrutura
# Comece pelo docker-compose.yml com Postgres + Qdrant + Neo4j
# Depois pelo supervisor.py mínimo
```

## Princípio

> Esta estrutura é **ponto de partida**, não camisa de força. Adapte ao seu design — mas mantenha separação clara (agents, mcp_servers, memory, rag, security, observability, eval).
