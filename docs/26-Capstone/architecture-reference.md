---
password: Etho-Prof-2026
---
# ETHAGT90 — Arquitetura de Referência

> Esta é uma **sugestão** de arquitetura. O aluno pode propor alternativa **justificada em ADR**. O importante é atender aos requisitos do [`enunciado.md`](enunciado.md).

## Visão C4 — Context (nível 1)

```
                           ┌─────────────────────────┐
                           │   Usuário (pesquisador)  │
                           └────────────┬─────────────┘
                                        │ pergunta de pesquisa
                                        ▼
┌──────────────────────────────────────────────────────────────────┐
│            PLATAFORMA DE PESQUISA AUTÔNOMA (AutoResearch)         │
│                                                                    │
│  [supervisor geral] ──► [orchestrator de busca]                   │
│                          ├── [researcher (arXiv)]                 │
│                          ├── [researcher (GitHub)]                │
│                          └── [researcher (Confluence)]            │
│  [synthesizer] ◄── resultados                                    │
│  [evaluator-optimizer loop]                                       │
│  [writer] ──► rascunho                                            │
│  [HITL] ──► humano aprova                                         │
│  [publisher] ──► relatório final                                  │
└──────────────────────────────────────────────────────────────────┘
        │           │             │            │
        ▼           ▼             ▼            ▼
   [arXiv API]  [GitHub API]  [Confluence]  [Vector DB / KG]
```

## Visão C4 — Container (nível 2)

```
┌─────────────────────────────────────────────────────────────────┐
│                        Docker Compose                            │
│                                                                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  │ Agent Runtime│  │ Event Bus    │  │ Workflow Engine       │  │
│  │ (LangGraph)  │  │ (NATS)       │  │ (Temporal)            │  │
│  └──────┬───────┘  └──────┬───────┘  └──────────┬─────────────┘  │
│         │                 │                     │                │
│  ┌──────┴─────────────────┴─────────────────────┴──────────┐    │
│  │                MCP Servers (3+)                          │    │
│  │  [arxiv-mcp]  [github-mcp]  [confluence-mcp]            │    │
│  └──────┬─────────────────┬─────────────────┬──────────────┘    │
│         │                 │                 │                  │
│  ┌──────┴──────┐  ┌───────┴──────┐  ┌──────┴──────────────┐    │
│  │ Postgres    │  │ Vector DB    │  │ Knowledge Graph     │    │
│  │ (checkpt+   │  │ (Qdrant:     │  │ (Neo4j: entidades   │    │
│  │  semântica) │  │  episódica)  │  │  + relações)        │    │
│  └─────────────┘  └──────────────┘  └─────────────────────┘    │
│                                                                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  │ Observability│  │ Guardrails   │  │ OPA (policy-as-code) │  │
│  │ (Phoenix)    │  │ (NeMo/custom)│  │                      │  │
│  └──────────────┘  └──────────────┘  └──────────────────────┘  │
└──────────────────────────────────────────────────────────────────┘
```

## Visão C4 — Component (nível 3, do Agent Runtime)

```
Agent Runtime (LangGraph)
├── supervisor/           (nó supervisor geral)
│   ├── planner           (decompõe pergunta em plano)
│   └── router            (decide próximos workers)
├── workers/
│   ├── researcher_arxiv  (usa arxiv-mcp)
│   ├── researcher_github (usa github-mcp)
│   ├── researcher_kb     (usa confluence-mcp + RAG)
│   ├── synthesizer       (integra achados)
│   ├── evaluator         (critica completude/qualidade)
│   └── writer            (produz rascunho)
├── hitl/                 (interrupt + resume via checkpointer)
├── memory/
│   ├── working           (state do grafo)
│   ├── episodic          (vector store)
│   ├── semantic          (Postgres + Neo4j)
│   └── procedural        (skills JSON)
├── security/
│   ├── input_filter
│   ├── output_filter
│   └── tool_allowlist
└── observability/
    ├── tracer            (Phoenix/OTel)
    └── cost_meter        (FinOps)
```

## Fluxo de execução (sequência)

```
1. Usuário submete pergunta
2. Supervisor: planner decompõe em plano (quais fontes, que ordem)
3. Orchestrator-Workers:
   - Paralelamente (via NATS): researcher_arxiv, researcher_github, researcher_kb
   - Cada um usa seu MCP server + RAG agêntico
4. Synthesizer: integra achados numa estrutura
5. Evaluator-Optimizer loop:
   - Evaluator: "faltou fonte? há contradição? completa?"
   - Se insuficiente: volta para workers específicos
6. Writer: produz rascunho de relatório
7. HITL: humano revisa (interrupt via Temporal/Postgres checkpointer)
8. Publisher: publica relatório final com fontes
9. Tudo traceado; custo medido; logs auditados
```

## Decisões arquiteturais (ADRs esperados)

- **ADR-001**: Por que Hierarchical + Orchestrator-Workers + Evaluator-Optimizer?
- **ADR-002**: Por que NATS em vez de Kafka?
- **ADR-003**: Por que Temporal para durable (em vez de só Postgres checkpointer)?
- **ADR-004**: Por que Qdrant para episódica + Neo4j para semântica?
- **ADR-005**: Política de HITL — onde e como.

Cada ADR justifica com requisitos + alternativas + trade-offs.

## Stack sugerida (não obrigatória)

| Camada | Sugestão | Alternativas |
|---|---|---|
| Agent runtime | LangGraph | OpenAI Agents SDK, CrewAI |
| Event bus | NATS | Kafka, RabbitMQ |
| Workflow engine | Temporal | Prefect, custom |
| Vector DB | Qdrant | Milvus, Weaviate, pgvector |
| Graph DB | Neo4j | memgraph, ArangoDB |
| State/Checkpointer | Postgres | Redis |
| MCP SDK | Python (FastMCP) | TypeScript |
| Observability | Phoenix | LangSmith, Langfuse |
| Guardrails | custom + NeMo | Lakera |
| Policy | OPA | custom |

## Princípio

> Esta arquitetura é **referência**, não **prescrição**. O aluno pode propor alternativas — desde que justifique em ADR e atenda aos requisitos do enunciado.
