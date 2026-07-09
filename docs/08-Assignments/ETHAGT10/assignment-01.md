---
password: Etho-Prof-2026
---
# ETHAGT10 — Avaliação do Módulo

> Curso: Padrões de Arquitetura Multi-Agente (topologias) · Nota mínima de aprovação: 3,0

## Composição da nota (4 pilares)

| Pilar | Peso | Instrumento |
|---|---|---|
| Técnico | 40% | Projeto (topologia + benchmark) + ADR |
| Consultivo | 30% | Defesa do ADR para painel |
| Comportamental | 20% | Code review |
| Prático | 10% | Demo: topologia rodando |

**Nota final** = Σ(pilar × peso).

---

## Rubrica — Pilar Técnico (40%)

O projeto exige, dada uma tarefa complexa (ex.: revisão de PR com especialistas), projetar e implementar a topologia mais adequada, justificada em ADR, com benchmark comparando a topologia escolhida com ≥1 alternativa.

| Critério | Peso | 1 (muito abaixo) | 3 (esperado) | 5 (referência) |
|---|---|---|---|---|
| Correção técnica | 25% | Topologia não funciona; agentes não colaboram | Topologia funcional (≥1 implementada); tarefa resolvida; benchmark comparável | ≥2 topologias + casos de borda (worker falha, supervisor gargalo, handoff ambíguo) tratados |
| Qualidade arquitetural | 25% | Sem topologia clara; agentes acoplados | Topologia clara (supervisor/swarm/hierarchical); responsabilidades separadas | Topologia modularizável, ADR justifica escolha via matriz de decisão (consistência × latência × custo × flexibilidade) |
| Profundidade | 20% | Superficial; não diferencia as 12 topologias | Compara ≥2 topologias em custo, latência e qualidade; justifica escolha | Discute trade-offs (quando hierarchical supera swarm, quando recursive é anti-pattern), identifica sinais de evolução |
| Produção-ready | 15% | Só roda em notebook | Docker; benchmark em casos reais | Docker compose + benchmark reproduzível + identificação de gargalos + ADR completo |
| Avaliação/observabilidade | 15% | Sem benchmark | Benchmark comparando topologias em ≥10 casos | Benchmark automatizado com custo/latência/quality por topologia, análise de gargalos, traces de handoff/orquestração |

**ADR** (parte do Pilar Técnico): documento de decisão arquitetural justificando a topologia via matriz de decisão, comparando com ≥1 alternativa, com medições reais. Peso: 40% do pilar técnico.

---

## Critérios dos demais pilares

- **Consultivo (30%):** Defesa do ADR para painel (banca simulada como arquitetos).
  - *1:* ADR ausente ou não justifica a topologia.
  - *3:* ADR coerente com matriz de decisão e ≥1 comparação.
  - *5:* Usa dados do benchmark, articula sinais de evolução, identifica quando a topologia precisa mudar.

- **Comportamental (20%):** Code review da topologia de um colega.
  - *1:* Comentários ausentes ou genéricos.
  - *3:* ≥5 observações sobre orquestração, handoffs e tratamento de falhas de worker.
  - *5:* Sugere topologia alternativa, identifica complexidade desnecessária, avalia escalabilidade.

- **Prático (10%):** Demo: topologia escolhida rodando ao vivo.
  - *1:* Topologia não roda ou falha na demo.
  - *3:* Topologia resolve a tarefa, mostrando coordenação entre agentes.
  - *5:* Mostra handoffs/orquestração em tempo real, mede custo/latência, lida com falha de worker.

---

## Regras

- Entrega: repositório Git com código, ADR (`./docs/adr-001-topology.md`), benchmark e dados comparativos.
- **Integridade acadêmica:** benchmarks devem ser reais e reproduzíveis. Assistência de IA é permitida e deve ser declarada. Plágio resulta em nota 1,0.
- Atraso: -0,5 ponto por dia útil, até 3 dias.
