---
password: Etho-Prof-2026
---
# ETHAGT07 — Avaliação do Módulo

> Curso: Knowledge Graphs & Vector Databases para Agentes · Nota mínima de aprovação: 3,0

## Composição da nota (4 pilares)

| Pilar | Peso | Instrumento |
|---|---|---|
| Técnico | 40% | Projeto (pipeline híbrido vector + grafo) + benchmark |
| Consultivo | 30% | Defesa do ADR |
| Comportamental | 20% | Code review |
| Prático | 10% | Demo: query multi-hop |

**Nota final** = Σ(pilar × peso).

---

## Rubrica — Pilar Técnico (40%)

O projeto exige construir um pipeline híbrido (vector + knowledge graph) para um corpus técnico, com agente que escolhe estratégia de retrieval e justifica. Meta: híbrido melhora success rate em casos multi-hop sem explodir custo.

| Critério | Peso | 1 (muito abaixo) | 3 (esperado) | 5 (referência) |
|---|---|---|---|---|
| Correção técnica | 25% | Pipeline não funciona; sem KG ou sem vector DB | Pipeline híbrido funcional; agente escolhe vector vs grafo; benchmark em ≥20 casos | GraphRAG (local + global) + casos de borda (entidade ausente, query ambígua, manutenção incremental) com success rate superior |
| Qualidade arquitetural | 25% | Sem separação de camadas; vector DB e KG acoplados | Separação razoável entre vector store, KG e retrieval agent | Padrões claros (retrieval agent abstrai estratégia), modelagem de KG justificada (entidades/relações), ADR documenta escolha |
| Profundidade | 20% | Superficial; não entende ANN vs grafo | Compara vector vs grafo vs híbrido em success rate e custo | Discute trade-offs (HNSW vs IVF, quando GraphRAG supera vector RAG, custo de construção do KG), justifica quando *não* usar híbrido |
| Produção-ready | 15% | Só roda em notebook | Docker (vector DB + Neo4j); benchmark reproduzível | Docker compose + reindexação + drift de embeddings tratado + observabilidade de retrieval |
| Avaliação/observabilidade | 15% | Sem benchmark | Benchmark vector vs grafo vs híbrido em ≥20 casos | Benchmark automatizado com latência/recall por estratégia, análise de erros por tipo de query, custo de manutenção do KG medido |

**Benchmark** (parte do Pilar Técnico): comparação sistemática de vector-only, graph-only e híbrido em casos single-hop e multi-hop, com métricas de accuracy, latência e custo. Peso: 50% do pilar técnico.

---

## Critérios dos demais pilares

- **Consultivo (30%):** Defesa do ADR para banca, justificando a escolha de vector DB, modelagem de KG e estratégia híbrida.
  - *1:* ADR ausente ou não justifica escolhas.
  - *3:* ADR coerente justificando quando usar vector vs grafo vs híbrido com dados.
  - *5:* Articula custo de manutenção do KG, identifica cenários onde híbrido é overkill, recomendação acionável.

- **Comportamental (20%):** Code review do pipeline de um colega.
  - *1:* Comentários ausentes ou genéricos.
  - *3:* ≥5 observações sobre modelagem de KG, queries Cypher e estratégia de retrieval.
  - *5:* Sugere otimização de queries, identifica problemas de drift de embeddings, propõe melhoria de modelagem.

- **Prático (10%):** Demo: query multi-hop respondida pelo pipeline híbrido.
  - *1:* Pipeline falha ou não resolve multi-hop.
  - *3:* Resolve query multi-hop corretamente, mostrando o raciocínio no grafo.
  - *5:* Mostra agente escolhendo estratégia, visualiza o caminho no grafo, lida com entidade ambígua.

---

## Regras

- Entrega: repositório Git com código, benchmark, ADR (`./docs/adr-001-hybrid.md`) e dados do corpus.
- **Integridade acadêmica:** benchmarks devem ser reais e reproduzíveis. Assistência de IA é permitida e deve ser declarada. Plágio resulta em nota 1,0.
- Atraso: -0,5 ponto por dia útil, até 3 dias.
