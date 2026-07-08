# ETHAGT14 — Projeto do Módulo: Otimização de Custo/Latência de Sistema Agêntico

> Curso: Escalabilidade & Sistemas Distribuídos de Agentes · Pilar: Técnico 40% + Prático 10% · Equipe: individual ou dupla

## Contexto / Cenário

Uma startup de SaaS oferece um agente de análise de dados que atende ≥50 tenants empresariais. Com o crescimento, a faturação de LLM saltou de US$8K/mês para US$45K/mês em um trimestre, e a latência p95 passou de 4s para 12s — a margem de lucro está sendo consumida pela inference. O CTO exige um plano de otimização que reduza custo e/ou latência em ≥40% *sem* degradar a qualidade mensurável do agente (success rate). As alavancas disponíveis incluem: cache semântico, model routing (Haiku para tarefas simples, Sonnet para complexas), batching, streaming, sharding por tenant, e FinOps (orçamento por execução com circuit breaker). Você deve diagnosticar os gargalos, aplicar otimizações e provar o ganho com dados antes/depois.

## Objetivo

Otimizar custo e/ou latência de um sistema agêntico existente (construído em módulos anteriores, ou fornecido) em ≥40% sem perder qualidade mensurável (success rate mantido dentro de ±2%). Diagnosticar gargalos, aplicar ≥3 técnicas de otimização (cache semântico, model routing, batching, streaming, sharding), e entregar um relatório FinOps com dashboard de custo granular.

## Requisitos

### Funcionais

1. Sistema base mensurado (baseline): custo por execução, latência p95/p99, success rate, distribuição de tokens por etapa.
2. ≥3 técnicas de otimização aplicadas e isoladas (medir o ganho de cada uma):
   - Cache semântico (similaridade de embedding para respostas reutilizáveis).
   - Model routing (classificador de complexidade roteia para Haiku/Sonnet).
   - Batching, streaming, ou sharding por tenant.
3. FinOps: orçamento por execução/tenant com circuit breaker (aborta se excede limite).
4. Medição granular de custo: por step, por tool, por tenant, por modelo.
5. Dashboard (Grafana ou equivalente) com custo, latência, cache hit rate, success rate em tempo real.

### Não-funcionais

- Otimizações não degradam success rate além de ±2% (validado em ≥30 casos).
- Cache semântico com política de invalidação documentada (TTL, consistência).
- Model routing com classificador calibrado (precisão ≥80% na rota correta).
- Circuit breaker respeita orçamento em 100% das execuções.
- Reprodutível: baseline e otimizado executam sobre o mesmo conjunto de casos.

## Entregáveis

- Código (repositório com baseline + versão otimizada + configuração de cache/routing/sharding).
- Relatório antes/depois (custo, latência, success rate, cache hit rate) com ≥30 casos.
- ADR de otimizações (técnicas escolhidas, trade-offs, ordem de aplicação).
- FinOps dashboard (Grafana ou equivalente) com custo granular em tempo real.

## Critérios de sucesso (mensuráveis)

- Redução ≥40% em custo ou latência (p95) mantendo success rate dentro de ±2%.
- Cada uma das ≥3 técnicas tem ganho isolado medido e reportado.
- Model routing classifica corretamente a complexidade em ≥80% dos casos.
- Circuit breaker aborta execuções que excedem orçamento em 100% dos testes de limite.
- FinOps dashboard mostra custo por step/tool/tenant/modelo em tempo real.

## Competências avaliadas

- C1 Programação Agêntica — nível **A** (otimização de sistema agêntico em produção).
- C2 Multi-Agent Systems — nível **A** (sharding, distribuição, coordenação).
- C3 MCP & Tool Use — nível **B** (cache de tool results, otimização de chamadas).
- C4 Agent Memory — nível **A** (cache semântico, invalidação, consistência distribuída).
- C5 AgentOps & Avaliação — nível **A** (medição granular, FinOps, circuit breaker, dashboard).

## Referências

- Apostila: `04-Apostilas/ETHAGT14/apostila.md`
- Rubrica técnica: `08-Assignments/ETHAGT14/assignment-01.md`
