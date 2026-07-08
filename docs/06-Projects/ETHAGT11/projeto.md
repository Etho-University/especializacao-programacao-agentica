# ETHAGT11 — Projeto do Módulo: Pipeline Event-Driven com Durable Execution

> Curso: Event-Driven Agents & Workflow Orchestration · Pilar: Técnico 40% + Prático 10% · Equipe: individual ou dupla

## Contexto / Cenário

Uma operadora de processamento de documentos fiscais (notas fiscais eletrônicas) precisa processar ≥10.000 documentos por hora: cada documento passa por extração de dados (OCR/LLM), validação fiscal, enriquecimento (consulta a APIs de cadastro), classificação contábil, e escrituração no ERP. O pipeline atual é síncrono e frágil — uma queda do banco de dados ou timeout de API perde documentos e exige reprocessamento manual. A diretoria de engenharia quer um pipeline *event-driven* com durable execution que sobreviva a crashes, retries automaticamente, compense transações parciais em caso de falha, e seja observável de ponta a ponta. O sistema deve tolerar falhas injetadas (chaos engineering) sem perda de dados.

## Objetivo

Projetar um pipeline event-driven para processamento de documentos em massa (notas fiscais ou equivalente), com durable execution (Temporal), retries com backoff, idempotência, e compensação (saga). Demonstrar resiliência injetando falhas (crash de worker, timeout de API, partition rebalance) e mostrando que o pipeline recupera sem perda de dados. Entregar um ADR justificando a arquitetura e uma análise de chaos testing.

## Requisitos

### Funcionais

1. Pipeline com ≥5 etapas: ingestão (fila) → extração (LLM/OCR) → validação → enriquecimento → escrituração.
2. Mensageria: Kafka ou NATS para desacoplamento entre etapas (ordering por chave = documento).
3. Durable execution via Temporal: estado de cada workflow persistido, sobrevive a crash do worker.
4. Retries com backoff exponencial em etapas que chamam APIs externas (validação, enriquecimento).
5. Idempotência: chave de idempotência por documento (NF-e ID) evita processamento duplicado.
6. Compensação (saga): se a escrituração falha, etapas anteriores são compensadas (ex.: marca documento como pendente, não como processado).

### Não-funcionais

- Pipeline tolera ≥2 tipos de falha injetada (crash de worker, timeout de API, kill do processo) sem perda de dados.
- Throughput ≥100 documentos/minuto em ambiente de teste.
- Observabilidade: distributed tracing (OpenTelemetry) correlacionando spans entre etapas.
- At-least-once delivery garantido; idempotência elimina duplicação de efeito.
- Latência p99 por documento ≤ 30 segundos (em condições normais).

## Entregáveis

- Código (repositório com pipeline, workers, configuração de mensageria e Temporal).
- ADR de arquitetura event-driven (escolha de broker, Temporal vs Prefect, padrões de resiliência).
- Análise de chaos testing (≥2 falhas injetadas, comportamento observado, recuperação demonstrada).
- Dashboard de observabilidade (traces, métricas de throughput, taxa de erro, latência).

## Critérios de sucesso (mensuráveis)

- Pipeline sobrevive a ≥2 falhas injetadas (crash, timeout) sem perda de dados — 100% dos documentos processados ou compensados.
- Idempotência verificada: reenvio do mesmo documento N vezes produz o mesmo resultado (1 escrituração, não N).
- Saga de compensação funciona: falha na etapa final reverte/marca etapas anteriores corretamente em 100% dos casos de teste.
- Distributed tracing correlaciona spans de ponta a ponta para qualquer documento.
- Throughput documentado e latência p99 medida em condições normais e sob falha.

## Competências avaliadas

- C1 Programação Agêntica — nível **A** (orquestração de agentes em pipeline assíncrono).
- C2 Multi-Agent Systems — nível **A** (coordenação via eventos, workers distribuídos).
- C3 MCP & Tool Use — nível **B** (tools como atividades do workflow).
- C4 Agent Memory — nível **B** (estado persistido via durable execution).
- C5 AgentOps & Avaliação — nível **I** (chaos testing, distributed tracing, observabilidade).

## Referências

- Apostila: `04-Apostilas/ETHAGT11/apostila.md`
- Rubrica técnica: `08-Assignments/ETHAGT11/assignment-01.md`
