# Catálogo de Ferramentas — Agentic AI

> v1: comparativo das principais ferramentas do ecossistema. Cada categoria tem ficha com: licença · maturidade · quando escolher · quando evitar · alternativas.

## Categorias

| Categoria | Foco | Módulos |
|---|---|---|
| [Agentic IDEs](agentic-ides.md) | OpenCode, Claude Code, Cursor, VSCode+MCP | ETHAGT08 |
| [Agent SDKs](agent-sdks.md) | OpenAI Agents SDK, LangGraph, CrewAI, AutoGen, Agno, PydanticAI, Semantic Kernel, Google ADK | ETHAGT01, 10 |
| [Coding Agents](coding-agents.md) | OpenHands, OpenDevin, Devin, OpenCode | ETHAGT-E2 |
| [Protocolo](protocol.md) | MCP (servers/clients/hosts) | ETHAGT08 |
| [Vector DBs](vector-dbs.md) | Qdrant, Milvus, Weaviate, Chroma, pgvector | ETHAGT07 |
| [Graph DBs](graph-dbs.md) | Neo4j, memgraph | ETHAGT07 |
| [State / Memory](state.md) | Postgres, Redis, SQLite (checkpointers) | ETHAGT05, 11 |
| [Mensageria](messaging.md) | Kafka, RabbitMQ, NATS | ETHAGT11 |
| [Orquestração](orchestration.md) | Temporal, Prefect, Airflow | ETHAGT11 |
| [Observabilidade](observability.md) | LangSmith, Phoenix, Langfuse, OpenTelemetry | ETHAGT12 |
| [Infra / CI](infra.md) | Docker, Kubernetes, GitHub, GitHub Actions | todos |

## Critério de comparação

Para cada ferramenta:
- **Licença** (MIT, Apache, comercial).
- **Maturidade** (estável, beta, experimental).
- **Modelo mental** (como pensa).
- **Controle** (preto vs caixa branca).
- **Prod-readiness** (pronto para produção?).
- **Comunidade** (adoção, suporte).
- **Custo** (open source, SaaS, self-host).
- **Quando escolher** / **Quando evitar**.
- **Alternativas**.

## Princípio

> **A ferramenta é consequência do princípio arquitetural** — não o inverso. Este catálogo ajuda a escolher, mas o curso ETHAGT01-16 ensina a decidir **por que**.
