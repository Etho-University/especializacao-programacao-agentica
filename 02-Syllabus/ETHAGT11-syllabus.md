# `ETHAGT11` — Event-Driven Agents & Workflow Orchestration

> Fase C · Carga 25 h · Versão 1.0 · Julho 2026

## 1. Identificação

| Campo | Valor |
|---|---|
| Código | `ETHAGT11` |
| Título | Event-Driven Agents & Workflow Orchestration |
| Fase interna | C |
| Carga horária | 25 h |
| Pré-requisitos | `ETHAGT10` |
| Módulos que dependem deste | `ETHAGT12`, `ETHAGT14`, `ETHAGT90` |

## 2. Objetivos

**Objetivo geral**: Capacitar o aluno a construir sistemas de agentes **orientados a eventos** com orquestração robusta (durable execution, filas, workflows de longa duração).

**Objetivos específicos**:
1. Diferenciar orquestração síncrona de event-driven assíncrona.
2. Aplicar filas (Kafka, RabbitMQ, NATS) para coordenação de agentes.
3. Implementar durable execution (Temporal, Prefect) para workflows longos.
4. Lidar com falhas, retries, idempotência, compensação.
5. Avaliar escala, ordering, exactly-once vs at-least-once.

## 3. Competências desenvolvidas

| Competência | Nível ao final |
|---|---|
| C1 Programação Agêntica | **A** |
| C2 Multi-Agent Systems | **A** |
| C3 MCP & Tool Use | B |
| C4 Agent Memory | B |
| C5 AgentOps & Avaliação | **I** |

## 4. Conteúdo programático

### Unidade 1 — Por que event-driven (3 h)
- Limites da orquestração síncrona
- Event-driven: desacoplamento, escala, resiliência
- Trade-off: complexidade, debugging

### Unidade 2 — Mensageria (5 h)
- Kafka (particionamento, log, ordering por partição)
- RabbitMQ (filas, routing, exchanges)
- NATS (jetstream, leveza, performance)
- Quando cada; patterns (CQRS, saga)

### Unidade 3 — Orquestração de workflows (5 h)
- Workflow engine vs agentes que decidem
- Temporal: durable execution, activity, workflow
- Prefect, Airflow (comparativo)
- Quando orquestrar via código vs via agente supervisor

### Unidade 4 — Durable execution para agentes (5 h)
- Sobreviver a crashes (estado persistente)
- Long-running agents (horas, dias)
- Human-in-the-loop via timers/signals
- Replays e debug temporal

### Unidade 5 — Patterns de resiliência (4 h)
- Retries com backoff
- Idempotência (chaves de idempotência)
- Compensação (saga pattern)
- Circuit breakers

### Unidade 6 — Produção: ordering, escala, observabilidade (3 h)
- Exactly-once vs at-least-once (mitos e realidade)
- Sharding de consumidores
- Distributed tracing em pipelines de agentes
- Custo

## 5. Bibliografia

### Fundamental
- Temporal.io documentation e *Durable Execution* primer.
- Kafka: *Kafka: The Definitive Guide* (Narkhede et al.).
- Richards, M. *Fundamentals of Software Architecture* (cap. event-driven).

### Complementar
- NATS docs; RabbitMQ docs.
- Microsoft *Cloud Design Patterns* (saga, CQRS).

## 6. Papers / docs canônicos

- Temporal *Durable Execution* whitepapers
- *CloudEvents* spec (CNCF)
- *The Log* (Kreps, LinkedIn)

## 7. Laboratórios

- **Lab 1** (4 h): "Agente com Kafka". Dois agentes coordenados via tópicos; ordering por chave.
- **Lab 2** (5 h): "Workflow durável em Temporal". Agente de longa duração (simulado) sobrevivendo a kill do processo.

## 8. Projeto do módulo

**Descrição**: projetar pipeline event-driven para um cenário (ex.: processamento de tickets em massa), com durable execution, retries e compensação.
**Entrega**: código + ADR + análise de falhas injetadas (chaos).
**Critério de sucesso**: pipeline sobrevive a ≥2 falhas injetadas sem perda de dados.

## 9. Exercícios

1. Quando Temporal é preferível a Kafka puro?
2. Escreva uma saga compensatória para "transferência entre contas".
3. Como garantir idempotência em tool de "enviar email"?
4. Diferencie exactly-once de at-least-once.
5. Verdadeiro/falso: "Event-driven é sempre mais escalável."

## 10. Avaliação

| Pilar | Peso | Instrumento |
|---|---|---|
| Técnico | 40% | Projeto + chaos test |
| Consultivo | 30% | Defesa da arquitetura |
| Comportamental | 20% | Code review |
| Prático | 10% | Demo: recuperação após crash |

**Nota mínima**: 3,0.

## 11. Slides

- Slides: `03-Slides/ETHAGT11-slides.md` (~70 slides).

## 12. Leitura complementar

- Temporal docs; Kreps *The Log*.

## 13. Ferramentas

- Kafka, NATS, RabbitMQ, Temporal, Prefect, Docker Compose, OpenTelemetry.

## 14. Diagramas

- Diagramas: `12-Diagrams/ETHAGT11/` — event-driven.mmd, saga.mmd, durable-execution.mmd.

## 15. Estudo de caso

- pipelines de processamento de documentos em enterprise.

## 16. Ficha de pesquisa

- Ficha: `20-Research/ETHAGT11-pesquisa.md`.

---

*Mantido por: Universidade Etho · Versão 1.0 · Julho 2026*
