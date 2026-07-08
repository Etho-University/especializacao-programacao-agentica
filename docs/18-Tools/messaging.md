# Mensageria / Orquestração / Estado / Observabilidade / Infra

## Mensageria (`messaging.md`)

| Tool | Força | Quando |
|---|---|---|
| **Kafka** | log partitioned, escala, durável | alto volume, ordering, event sourcing |
| **RabbitMQ** | routing rico, flexível | complex routing, tradicional |
| **NATS** | leve, baixa latência, JetStream | simplicidade, performance |
| **SQS/SNS** (cloud) | managed | sem ops |
| **Redis Streams** | simples, em memória | volume médio |

## Orquestração (`orchestration.md`)

| Tool | Força | Quando |
|---|---|---|
| **Temporal** | durable, código-first, escalável | workflows longos, HITL |
| **Prefect** | Python-first, simples | data pipelines |
| **Airflow** | maduro, DAGs | batch tradicional |
| **Restate** | durable RPC, moderno | microservices duráveis |

## Estado / Memory (`state.md`)

| Tool | Uso | Quando |
|---|---|---|
| **Postgres** | checkpointer, memória semântica relacional | produção |
| **Redis** | baixa latência, cache, sessões | cache + state efêmero |
| **SQLite** | dev, protótipo | local |

## Observabilidade (`observability.md`)

| Tool | Força | Quando |
|---|---|---|
| **LangSmith** | tight LangChain | ecossistema LangChain |
| **Phoenix** (Arize) | open source, poderoso | agnóstico, self-host |
| **Langfuse** | open source, self-host | privacidade |
| **OpenLLMetry** | OTel-native | padronização |
| **Honeycomb / Datadog** | enterprise | já tem stack |

## Infra / CI (`infra.md`)

- **Docker / Docker Compose**: reprodutibilidade local.
- **Kubernetes**: produção distribuída.
- **GitHub**: versionamento + colaboração.
- **GitHub Actions**: CI/CD (incluindo eval de agentes).

## Referências

- Documentação oficial de cada ferramenta.
