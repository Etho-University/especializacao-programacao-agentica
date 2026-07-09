---
password: Etho-Prof-2026
---
# ETHAGT14 — Avaliação do Módulo

> Curso: Escalabilidade & Sistemas Distribuídos de Agentes · Nota mínima de aprovação: 3,0

## Composição da nota (4 pilares)

| Pilar | Peso | Instrumento |
|---|---|---|
| Técnico | 40% | Projeto (otimização custo/latência) + FinOps report |
| Consultivo | 30% | Defesa do ADR para "CTO" |
| Comportamental | 20% | Code review |
| Prático | 10% | Demo: antes/depois |

**Nota final** = Σ(pilar × peso).

---

## Rubrica — Pilar Técnico (40%)

O projeto exige otimizar custo/latência de um sistema agêntico existente (de módulos anteriores) em ≥40% sem perder qualidade mensurável (success rate mantido em ±2%). Entrega: antes/depois + ADR de otimizações + FinOps dashboard.

| Critério | Peso | 1 (muito abaixo) | 3 (esperado) | 5 (referência) |
|---|---|---|---|---|
| Correção técnica | 25% | Otimização não funciona ou degrada qualidade >2% | Redução ≥40% em custo ou latência com success rate mantido (±2%) | ≥40% + casos de borda (cache invalidation, rate limit, cold start, sharding skew) tratados |
| Qualidade arquitetural | 25% | Otimizações pontuais; sem separação de caching/routing | Separação razoável (cache + model routing + sharding); FinOps observável | Padrões claros (cache semântico, stateless workers, circuit breaker), ADR justifica otimizações com dados |
| Profundidade | 20% | Superficial; não entende gargalos | Identifica gargalos (LLM vs tools vs memória vs rede); justifica otimizações | Discute trade-offs (cache semântico falha quando?, streaming vs batching, serverless vs dedicado), compara abordagens |
| Produção-ready | 15% | Só roda em notebook | Docker + infra configurável; FinOps dashboard | Docker/Kubernetes + FinOps dashboard (custo por step/tool/tenant) + orçamento com circuit breaker |
| Avaliação/observabilidade | 15% | Sem medição de custo/latência | Métricas antes/depois (custo, latência p50/p95, success rate) | FinOps dashboard granular, benchmark de cache hit rate, análise de gargalos, A/B de model routing |

**FinOps report** (parte do Pilar Técnico): relatório com medição granular de custo/latência antes/depois, orçamento por execução/tenant, análise de gargalos e justificativa de cada otimização. Peso: 40% do pilar técnico.

---

## Critérios dos demais pilares

- **Consultivo (30%):** Defesa do ADR para "CTO" (banca simulada como liderança técnica executiva).
  - *1:* Não justifica as otimizações nem o impacto financeiro.
  - *3:* Apresenta redução de custo/latência com dados, justifica as escolhas.
  - *5:* Quantifica impacto financeiro, articula trade-offs custo-latência-qualidade, propõe roadmap de FinOps.

- **Comportamental (20%):** Code review das otimizações de um colega.
  - *1:* Comentários ausentes ou genéricos.
  - *3:* ≥5 observações sobre cache invalidation, sharding e tratamento de rate limits.
  - *5:* Identifica problemas de consistência de cache, sugere model routing, avalia custo de infra.

- **Prático (10%):** Demo: antes/depois ao vivo (mesma query, com e sem otimização).
  - *1:* Não demonstra diferença ou a otimização quebra.
  - *3:* Mostra redução visível de custo/latência mantendo qualidade.
  - *5:* Dashboard FinOps ao vivo, mostra cache hit, model routing, circuit breaker em ação.

---

## Regras

- Entrega: repositório Git com código, ADR (`./docs/adr-001-scalability.md`), FinOps report e dashboard.
- **Integridade acadêmica:** medições de custo/latência devem ser reais e reproduzíveis. Fabricação de números resulta em nota 1,0.
- Atraso: -0,5 ponto por dia útil, até 3 dias.
