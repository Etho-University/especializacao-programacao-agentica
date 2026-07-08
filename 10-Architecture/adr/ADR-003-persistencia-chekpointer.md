# ADR-003: Checkpointer PostgreSQL para Memória de Longo Prazo

> **Status**: Aceito · **Data**: Julho 2026 · **Autor**: [Nome]

## Contexto
Agentes precisam persistir estado entre execuções (sessões duram horas/dias). Requer consistência, recuperação e concorrência.

## Decisão
Usar **PostgreSQL** como checkpointer (via LangGraph `CheckpointerPostgres`) + **vector store** (pgvector) para recall semântico.

## Alternativas consideradas
- **SQLite**: rejeitado porque não escala para múltiplos workers concorrentes.
- **Redis**: rejeitado porque sem queries semânticas; sem persistência forte.
- **MongoDB**: rejeitado porque sem integração nativa com checkpointer de graph.

## Consequências
- **Positivas**: consistência ACID; integração nativa LangGraph; pgvector para recall semântico no mesmo banco.
- **Negativas**: custo operacional (PostgreSQL gerenciado); latência de conexão vs Redis.
- **Mitigação**: pool de conexões (PgBouncer) e cache de checkpoint recente em Redis.

## Referências
- ETHAGT05 — Memória de Agentes
- `16-Memory/01-checkpointer-pattern.md`
