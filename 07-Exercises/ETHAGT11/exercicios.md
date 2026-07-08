# ETHAGT11 — Lista de Exercícios

> Curso: Event-Driven Agents & Workflow Orchestration. Fixação de conceitos. Use a apostila `04-Apostilas/ETHAGT11/apostila.md` como referência.

## Múltipla escolha

**1. "Durable execution" (ex.: Temporal) significa que:**

a) O workflow usa modelos duráveis
b) O estado do workflow persiste entre crashes, permitindo retomar do ponto exato de falha
c) Os logs são permanentes
d) O agente nunca falha

**2. No padrão Saga, a "compensação" serve para:**

a) Acelerar o workflow
b) Desfazer ações já executadas quando uma etapa posterior falha (rollback semântico)
c) Cachear resultados
d) Fazer re-ranking

**3. A diferença entre at-least-once e exactly-once delivery é:**

a) Exactly-once garante que cada mensagem é entregue exatamente uma vez; at-least-once pode entregar duplicatas
b) At-least-once é mais caro
c) Exactly-once não existe
d) Não há diferença

**4. Quando Kafka é preferível a RabbitMQ?**

a) Sempre
b) Quando se precisa de ordering por partição, alto throughput e log persistente (event sourcing)
c) Quando se precisa de routing complexo
d) Nunca

## Verdadeiro ou Falso (justificado)

**1.** "Event-driven é sempre mais escalável que orquestração síncrona." — Justifique.

**2.** "Idempotência (chaves de idempotência) é necessária mesmo com exactly-once delivery." — Justifique.

**3.** "Retries com backoff exponencial evitam tempestades de chamadas quando um serviço cai." — Justifique.

**4.** "Temporal permite replays e debug temporal de workflows, o que é valioso para investigar falhas." — Justifique.

## Código curto

**1.** Escreva o pseudocódigo de uma saga compensatória para "transferência entre contas": debitar A → creditar B, com compensação se creditar falhar.

**2.** Escreva o pseudocódigo de um retry com backoff exponencial (máximo 3 tentativas, base 1s).

**3.** Escreva o pseudocódigo de um circuit breaker: se >5 falhas consecutivas, abrir circuito por 60s.

## Análise de trade-off

**1.** Compare Temporal vs. Kafka puro para orquestração de agentes de longa duração. Quando Temporal vale a pena?

**2.** Compare at-least-once vs. exactly-once. Quando at-least-once com idempotência é suficiente?

**3.** Compare orquestração via código (Temporal/Prefect) vs. via agente supervisor. Quando cada?

## Debug / diagnóstico

**1.** Um workflow event-driven processa eventos duplicados, causando efeito colateral duplo (ex.: dois emails enviados). Diagnóstico e correção.

**2.** Um agente de longa duração em Temporal trava após um crash e não retoma. Diagnóstico e 2 possíveis causas.
