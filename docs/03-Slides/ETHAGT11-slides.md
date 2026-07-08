# ETHAGT11 — Event-Driven Agents & Workflow Orchestration — Slides

> Apresentação para aula síncrona · ~50 min · 13 slides

## Estrutura da aula
- Abertura (5 min): gancho/motivação
- Teoria (25 min): conceitos principais com diagramas de referência
- Demonstração (10 min): código ao vivo ou walkthrough de lab
- Exercício (5 min): questão rápida ou discussão
- Fechamento (5 min): conexão com próximo módulo, leitura recomendada

## Slides

### Slide 1 — Título
- ETHAGT11 — Event-Driven Agents & Workflow Orchestration
- Professor, data, Universität Etho
- Pré-requisito: ETHAGT10
- ~1 min

### Slide 2 — Agenda
1. Por que event-driven (limites da orquestração síncrona)
2. Mensageria (Kafka, RabbitMQ, NATS)
3. Orquestração de workflows (Temporal, Prefect)
4. Durable execution para agentes
5. Patterns de resiliência (retries, idempotência, saga)
6. Produção: ordering, escala, observabilidade
- ~1 min

### Slide 3 — Gancho / Motivação
- Problema: agente síncrono morre no meio de uma tarefa longa e perde todo o progresso
- Exemplo: processamento de 10.000 tickets — se o processo cai no ticket 5.000, recomeça do zero
- A solução: event-driven + durable execution
- Pergunta: *Qual o pior crash que você já viu em produção?*
- ~3 min

### Slide 4 — Por que Event-Driven
- Limites da orquestração síncrona: acoplamento, falta de resiliência, difícil escalar
- Event-driven: desacoplamento, escala horizontal, resiliência
- Trade-off: complexidade (eventual consistency, debugging)
- Diagrama: `12-Diagrams/ETHAGT11/event-driven.mmd`
- ~4 min

### Slide 5 — Mensageria
- Kafka: particionamento, log imutável, ordering por partição
- RabbitMQ: filas, routing, exchanges, mais simples
- NATS: JetStream, leveza, baixa latência
- Quando cada: Kafka para volume alto e replay; RabbitMQ para routing complexo; NATS para edge
- Padrões: CQRS, saga
- Pergunta: *Ordering por partição — como garantir que mensagens do mesmo agente vão pra mesma partição?*
- ~5 min

### Slide 6 — Orquestração de Workflows
- Workflow engine vs agentes que decidem (são complementares)
- Temporal: durable execution, activity, workflow (código como workflow)
- Prefect: python puro, mais simples, menos durável
- Airflow: agendamento, não orquestração em tempo real
- Quando orquestrar via código vs via agente supervisor
- ~4 min

### Slide 7 — Durable Execution para Agentes
- Sobreviver a crashes: estado persistente (Temporal replay)
- Long-running agents: horas ou dias de execução
- Human-in-the-loop via timers/signals
- Replays e debug temporal (re-executar do início com mesmo histórico)
- Diagrama: `12-Diagrams/ETHAGT11/durable-execution.mmd`
- Pergunta: *Replay: se uma tool externa mudou de comportamento, o replay quebra?*
- ~4 min

### Slide 8 — DEMO: Agente com Kafka
- Código ao vivo: dois agentes coordenados via tópicos Kafka
- Agente A publica "tarefa: pesquisar X" → Agente B consome, processa, publica resultado
- Mostrar ordering por chave (mesmo agent_id = mesma partição)
- Simular falha de consumer e mostrar reprocessamento
- Referência: `05-Labs/ETHAGT11/Lab1-Agente-Kafka`
- ~5 min

### Slide 9 — Patterns de Resiliência
- Retries com backoff (exponential, jitter)
- Idempotência (chaves de idempotência em tools)
- Compensação (saga pattern: se passo 3 falha, desfaz passo 1 e 2)
- Circuit breakers (parar de chamar tool que está falhando)
- Diagrama: `12-Diagrams/ETHAGT11/saga.mmd`
- ~4 min

### Slide 10 — Produção: Ordering, Escala, Observabilidade
- Exactly-once vs at-least-once: mitos e realidade (na prática, at-least-once + idempotência)
- Sharding de consumidores (grupos de consumo paralelos)
- Distributed tracing em pipelines de agentes (OpenTelemetry)
- Custo: mensageria não é grátis
- Pergunta: *Exactly-once existe de verdade ou é mito?*
- ~3 min

### Slide 11 — Exercício: Saga Compensatória
- Cenário: sistema de transferência entre contas (debita conta A → credita conta B → notifica)
- Em duplas: escrever a lógica de compensação para cada passo falhar
- 3 min, apresentar 2 exemplos
- ~4 min

### Slide 12 — Conexão com Próximo Módulo
- ETHAGT12 — AgentOps: observabilidade + avaliação
- ETHAGT14 — Escalabilidade: event-driven em produção
- Leitura: Temporal.io *Durable Execution* primer
- Kreps *The Log* (LinkedIn)
- Microsoft *Cloud Design Patterns* (saga, CQRS)
- ~2 min

### Slide 13 — Referências
- Temporal.io documentation e *Durable Execution* primer
- Kafka: *Kafka: The Definitive Guide* (Narkhede et al.)
- Richards, M. *Fundamentals of Software Architecture* (cap. event-driven)
- NATS docs; RabbitMQ docs
- CloudEvents spec (CNCF)
- ~1 min
