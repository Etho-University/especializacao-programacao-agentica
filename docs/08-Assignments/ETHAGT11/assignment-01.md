# ETHAGT11 — Avaliação do Módulo

> Curso: Event-Driven Agents & Workflow Orchestration · Nota mínima de aprovação: 3,0

## Composição da nota (4 pilares)

| Pilar | Peso | Instrumento |
|---|---|---|
| Técnico | 40% | Projeto (pipeline event-driven) + chaos test |
| Consultivo | 30% | Defesa da arquitetura |
| Comportamental | 20% | Code review |
| Prático | 10% | Demo: recuperação após crash |

**Nota final** = Σ(pilar × peso).

---

## Rubrica — Pilar Técnico (40%)

O projeto exige projetar um pipeline event-driven para um cenário (ex.: processamento de tickets em massa), com durable execution, retries e compensação. Meta: pipeline sobrevive a ≥2 falhas injetadas sem perda de dados.

| Critério | Peso | 1 (muito abaixo) | 3 (esperado) | 5 (referência) |
|---|---|---|---|---|
| Correção técnica | 25% | Pipeline quebra ao primeiro erro; sem retries | Pipeline funcional com durable execution; sobrevive a ≥2 falhas injetadas sem perda de dados | ≥2 falhas + casos de borda (ordering por partição, idempotência, compensação saga) tratados e verificados |
| Qualidade arquitetural | 25% | Orquestração síncrona acoplada; sem filas | Separação razoável (filas + workflow engine); retries e circuit breakers presentes | Padrões claros (saga, CQRS, durable execution), idempotência por chave, ADR justifica Temporal vs Kafka puro |
| Profundidade | 20% | Superficial; não entende event-driven | Diferencia síncrono de assíncrono; justifica escolha de fila (Kafka/RabbitMQ/NATS) | Discute trade-offs (exactly-once vs at-least-once, Temporal vs Prefect), analisa compensação e ordering |
| Produção-ready | 15% | Só roda em memória | Docker compose (fila + workflow engine); pipeline reproduzível | Docker compose + OpenTelemetry (distributed tracing) + chaos test automatizado + análise de falhas injetadas |
| Avaliação/observabilidade | 15% | Sem chaos test nem observabilidade | Chaos test com ≥2 falhas injetadas; análise de recuperação documentada | Distributed tracing completo, medição de recovery time, análise de dead-letter queue, retry budget documentado |

**Chaos test** (parte do Pilar Técnico): injeção de ≥2 falhas (kill de consumer, timeout de tool, partição indisponível) com verificação de que o pipeline recupera sem perda de dados. Peso: 40% do pilar técnico.

---

## Critérios dos demais pilares

- **Consultivo (30%):** Defesa da arquitetura event-driven para banca.
  - *1:* Não justifica as escolhas de mensageria e orquestração.
  - *3:* Justifica fila e workflow engine com ≥3 critérios (escalabilidade, resiliência, complexidade).
  - *5:* Usa dados do chaos test, articula trade-offs de ordering/durabilidade, recomendação acionável.

- **Comportamental (20%):** Code review do pipeline de um colega.
  - *1:* Comentários ausentes ou genéricos.
  - *3:* ≥5 observações sobre retries, idempotência e tratamento de falhas.
  - *5:* Identifica problemas de ordering, sugere compensação saga, avalia estratégia de dead-letter queue.

- **Prático (10%):** Demo: recuperação após crash ao vivo.
  - *1:* Pipeline não recupera após crash.
  - *3:* Pipeline recupera após kill do processo, sem perda de dados.
  - *5:* Mostra durable execution (replay), mede recovery time, lida com falha em tool externa.

---

## Regras

- Entrega: repositório Git com código, ADR (`./docs/adr-001-event-driven.md`), chaos test e análise de falhas.
- **Integridade acadêmica:** chaos tests devem ser reais (não simulados só no relatório). Assistência de IA é permitida e deve ser declarada. Plágio resulta em nota 1,0.
- Atraso: -0,5 ponto por dia útil, até 3 dias.
