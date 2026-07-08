# Event-Driven

> Topologia 7/12 · ETHAGT11

## Descrição
Agentes reagem a eventos publicados em um message broker (Kafka, NATS, RabbitMQ). Agentes são desacoplados — produtores e consumidores não se conhecem.

## Estrutura
```
[Event Bus: Kafka / NATS]
    ▲        │        ▲
    │        ▼        │
[Produtor] [Worker A] [Worker B]
```

## Quando usar
- Desacoplamento entre agentes
- Escala horizontal (mais consumidores)
- Workflows longos com HITL assíncrono
- Tolerância a falhas (eventos persistem)

## Quando evitar
- Tarefas síncronas simples
- Baixa latência crítica (< 100ms)
- Poucos agentes (overhead do broker)

## Trade-offs
| Prós | Contras |
|------|---------|
| Escala horizontal | Complexidade de infra |
| Desacoplamento total | Debug distribuído caro |
| Resiliência (replay) | Garantias de entrega (exactly-once é caro) |

## Referências
- ETHAGT11 — Event-Driven & Orquestração
- Kafka, NATS, Temporal

## Diagramas relacionados
- `12-Diagrams/ETHAGT11/01-event-driven.mmd`
