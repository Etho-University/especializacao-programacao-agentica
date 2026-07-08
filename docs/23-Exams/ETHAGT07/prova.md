# ETHAGT07 — Prova do Módulo: Knowledge Graphs & Vector Databases para Agentes

> Universidade Etho · Versão 1.0 · Julho 2026
> Duração: ~60 min · 10 questões · closed book · Pilar Técnico (40%)

Esta prova avalia vector databases, knowledge graphs, GraphRAG e pipelines híbridos como infraestrutura cognitiva de agentes.

---

## Parte 1 — Conceitos (Q1-4)

**1. (Múltipla escolha)** O que a técnica ANN (Approximate Nearest Neighbor) resolve?
- (a) Embedding de textos
- (b) A busca exata O(N) é inviável em milhões de vetores; ANN aproxima o resultado trocando recall por velocidade
- (c) Reordenação de resultados por relevância
- (d) Compressão de vetores

**2. (V/F justificado)** "Um knowledge graph responde 'o que está relacionado com isto e como?', enquanto um vector DB responde 'o que é parecido com isto?'."

**3. (Múltipla escolha)** Qual métrica de similaridade é mais comum para embeddings de texto?
- (a) Euclidean (L2)
- (b) Manhattan
- (c) Cosine
- (d) Hamming

**4. (V/F justificado)** "Sempre preferir pipeline híbrido (vector + grafo) é a melhor estratégia."

---

## Parte 2 — Aplicação e trade-off (Q5-8)

**5. (Trade-off)** Por que GraphRAG é caro de construir? Justifique o custo e diga quando ele é amortizado.

**6. (Análise comparativa)** Para estes 3 cenários, vector DB ou knowledge graph?
- (a) "Quais os temas principais deste corpus de 10.000 artigos científicos?"
- (b) "Quais documentos falam sobre reembolso?"
- (c) "Quais drugs interagem com o gene X em até 3 saltos?"

**7. (Debug de escala)** Um vector DB com índice HNSW calibrado para 1M vetores está degradando em latência após chegar a 10M. O que aconteceu e qual é a solução?

**8. (V/F justificado)** "pgvector é uma opção operacional viável quando você já tem Postgres e quer adicionar busca vetorial sem introduzir um sistema novo."

---

## Parte 3 — Projeto curto (Q9-10)

**9. (Projeto curto)** Escreva uma query Cypher (Neo4j) para encontrar "co-autores de Ana em até 3 saltos de coautoria", retornando nomes distintos.

**10. (Projeto curto)** Descreva o pipeline GraphRAG em 4 etapas (extração → comunidades → sumarização → consulta) e diferencie Local search de Global search.

---

## Critérios de correção (resumo)

| Conceito | Questões | Peso |
|---|---|---|
| Vector DBs & ANN | 1, 3, 8 | 20% |
| Knowledge graphs | 2, 9 | 20% |
| GraphRAG & custo | 5, 10 | 25% |
| Escolha de tecnologia | 4, 6 | 20% |
| Operação em escala | 7 | 15% |

**Conversão**: cada questão vale 10 pts; total 100 pts. Nota 1-5.
- 90+ pts: 5,0
- 75-89: 4,0
- 60-74: 3,0 (mínimo aprovação)
- <60: reprovação.

Gabarito comentado em [`gabarito.md`](gabarito.md).
