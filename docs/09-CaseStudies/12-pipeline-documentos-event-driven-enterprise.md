# Caso de Estudo — Pipelines de processamento de documentos em enterprise

> ETHAGT11 · Event-driven + durable em produção.

## Contexto

Empresas que processam **milhares de documentos** (contratos, faturas, papers científicos) para extração de entidades, classificação e indexação usam pipelines event-driven com durable execution. Padrão observado em several vendors (Hebbia, Glean, legais como Casetext).

## Arquitetura típica

```
[upload] ─► Kafka "raw" ─► [OCR + extract] ─► Kafka "extracted"
                                                          │
                                                          ▼
                                              [validate + HITL]
                                                          │
                                              ┌───────────┴───────────┐
                                              ▼                       ▼
                                      Kafka "validated"         Kafka "needs_review"
                                              │                       │
                                              ▼                       ▼
                                      [index → vector DB]      [HITL queue]
                                              │                       │
                                              ▼                       ▼
                                      [available for search]    [reprocess]
```

## Componentes

- **Mensageria**: Kafka (ordering por `doc_id` via partition key).
- **Durable execution**: Temporal para workflows com HITL.
- **DLQ**: documentos problemáticos (OCR falhou, formato estranho).
- **Observabilidade**: distributed tracing (OpenTelemetry), métricas por estágio.
- **Saga**: se indexação falha após validação, compensar (remover da fila de disponíveis).

## Lições

1. **Cada estágio é um consumer** independente — escala horizontalmente.
2. **HITL como cidadão de primeira classe** — fila dedicada, UI para humanos.
3. **DLQ é obrigatório** — sempre há documentos patológicos.
4. **Idempotência no index** — redelivery não duplica.
5. **Ordering por chave** — preserva ordem por documento/usuário relevante.
6. **Observabilidade é metade da batalha** — sem traces, debug é impossível.

## Referências

- Temporal case studies (Hebbia, etc.).
- Confluent (Kafka) reference architectures.
