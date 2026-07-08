# ETHAGT11 — Prova do Módulo: Event-Driven Agents & Workflow Orchestration

> Universidade Etho · Versão 1.0 · Julho 2026
> Duração: ~60 min · 10 questões · closed book · Pilar Técnico (40%)

Esta prova avalia a construção de sistemas de agentes **orientados a eventos** com orquestração robusta — mensageria, durable execution, resiliência (retries, idempotência, compensação) e ordering em escala.

---

## Parte 1 — Conceitos (Q1-4)

**1. (Múltipla escolha)** A principal vantagem da orquestração *event-driven* sobre a síncrona é:
- (a) Menor latência ponta-a-ponta garantida.
- (b) Desacoplamento, escala e resiliência entre produtores e consumidores.
- (c) Debug mais simples, pois tudo é assíncrono.

**2. (V/F justificado)** "Em Kafka, o ordering das mensagens é garantido globalmente em todo o tópico."

**3. (Múltipla escolha)** *Durable execution* (Temporal) significa:
- (a) Mensagens persistem no Kafka por retenção configurável.
- (b) O estado do workflow é checkpointado e sobrevive a crashes; execução pode ser replayada.
- (c) Resultados são cacheados em Redis.

**4. (V/F justificado)** "Event-driven é sempre mais escalável que orquestração síncrona."

---

## Parte 2 — Aplicação e trade-off (Q5-8)

**5. (Trade-off)** Dê 2 cenários em que **Temporal** é preferível a **Kafka puro** e justifique.

**6. (Debug)** Um agente enviou o mesmo email 3 vezes após retries. Diagnóstico: falta de idempotência. Proponha 2 formas de garantir idempotência numa tool `send_email`.

**7. (Análise)** Por que o *partition key* importa num pipeline de agentes? Dê um exemplo onde a escolha errada causa bug.

**8. (Trade-off)** Diferencie *exactly-once* de *at-least-once*. Por que o primeiro é em grande parte um mito e como se projeta contra isso?

---

## Parte 3 — Projeto curto (Q9-10)

**9. (Projeto)** Esquematize uma **saga compensatória** para "transferência entre contas A→B": liste passos e a compensação de cada um em caso de falha.

**10. (Projeto)** Escreva o esqueleto de um *workflow* em estilo Temporal (pseudo-código) que aguarda HITL por até 24 h antes de uma ação destrutiva.

---

## Critérios de correção (resumo)

| Parte | Questões | Peso |
|---|---|---|
| Conceitos | 1, 2, 3, 4 | 40% |
| Aplicação/trade-off | 5, 6, 7, 8 | 40% |
| Projeto curto | 9, 10 | 20% |

**Conversão**: cada questão vale 10 pts; total 100 pts → nota 1-5.
- 90+: 5,0 · 80-89: 4,5 · 70-79: 4,0 · 60-69: 3,5 · 50-59: 3,0 (mínimo) · <50: reprovação.

Gabarito comentado em [`gabarito.md`](gabarito.md).
