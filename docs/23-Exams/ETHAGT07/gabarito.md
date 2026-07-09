---
password: Etho-Prof-2026
---
# ETHAGT07 — Gabarito da Prova

> Restrito a mentores. Respostas esperadas e critérios de correção para [`prova.md`](prova.md).

## Parte 1 — Conceitos

**1. (b) A busca exata O(N) é inviável em milhões de vetores; ANN aproxima o resultado trocando recall por velocidade.** ANN (Approximate Nearest Neighbor) é a solução computacional para busca vetorial em escala — algoritmos como HNSW e IVF aproximam o vizinho mais próximo sem comparar com todos. Ref.: Capítulo 1 — Vector databases, §1.2.

**2. VERDADEIRO.** Essa é a distinção fundamental: vector DB = similaridade semântica ("parecido com isto"); knowledge graph = relações estruturadas ("relacionado com isto e como?"). Para raciocínio sobre relações, a estrutura de grafo é intrinsecamente superior. Ref.: Capítulo 3 — Knowledge graphs, §3.1.

**3. (c) Cosine.** Cosine similarity é a métrica mais comum para embeddings de texto, pois mede a *direção* (semântica), não a magnitude. A escolha deve casar com o embedding: se o modelo foi treinado para cosine, use cosine. Ref.: Capítulo 1, §1.4.

**4. FALSO.** Híbrido adiciona complexidade operacional (dois sistemas para manter). Para aplicações simples, um vector DB basta. A regra: **adicione complexidade só com evidência** de que melhora o resultado. Meça: se o híbrido melhora success rate em casos multi-hop sem explodir custo, justifica-se; senão, é overhead. Ref.: Capítulo 5 — Pipelines híbridos, §5.4.

## Parte 2 — Aplicação e trade-off

**5.** GraphRAG é caro porque **extrair entidades e relações de um corpus grande exige muitas chamadas LLM** (LLM-based knowledge extraction). A construção pode custar ordens de magnitude mais que um vector DB. O custo é *amortizado* se o KG for consultado muitas vezes — mas para corpora voláteis, a reconstrução frequente é proibitiva. Mitigação: atualização incremental (adicionar novas entidades sem reconstruir tudo). Ref.: Capítulo 4 — GraphRAG, §4.4.

**6.** (a) **Knowledge graph (GraphRAG global search):** perguntas globais/sintetizadoras não têm chunk individual que as responda — GraphRAG agrega sumários de comunidade. (b) **Vector DB:** busca por similaridade semântica direta — "documentos sobre reembolso". (c) **Knowledge graph:** travessia de relações em até 3 saltos (drug → gene → interaction) é uma query Cypher natural, impossível em vector DB. Ref.: Capítulo 4, §4.3 e Capítulo 5.

**7.** Os parâmetros do HNSW (ex.: `M`, `ef_construction`, `ef_search`) e do IVF (ex.: `nlist`) foram calibrados para 1M vetores e **degradam em 10M**. Solução: **reindexação** com parâmetros recalibrados para o novo volume. Planeje a reindexação como operação de manutenção esperada, não surpresa. Outro cenário que exige reindexação: troca do modelo de embedding (drift). Ref.: Capítulo 6 — Operação em escala, §6.2.

**8. VERDADEIRO.** pgvector resolve o dilema comum: você já tem Postgres e quer busca vetorial sem novo sistema. É uma extensão que adiciona tipos e índices vetoriais ao Postgres, permitindo combinar busca vetorial com consultas relacionais na mesma query. Ideal para volumes médios e operações que valorizam simplicidade de stack. Ref.: Capítulo 2 — Comparativo, §2.3.

## Parte 3 — Projeto curto

**9.**
```cypher
MATCH (a:Pessoa {nome:"Ana"})-[:COAUTORA*1..3]-(coautor)
RETURN DISTINCT coautor.nome
```
Avaliar: pattern matching com `COAUTORA*1..3` (1 a 3 saltos), `DISTINCT` para evitar duplicatas. Ref.: Capítulo 3, §3.3.

**10.** As 4 etapas: (1) **Extração:** LLM extrai entidades e relações do corpus, formando um grafo. (2) **Comunidades:** algoritmo de detecção (ex.: Leiden) agrupa nós relacionados. (3) **Sumarização hierárquica:** cada comunidade é sumarizada pelo LLM em múltiplos níveis. (4) **Consulta:**
- **Local search:** para perguntas sobre entidades específicas — traversa o grafo local.
- **Global search:** para perguntas globais/sintetizadoras — agrega sumários de comunidade (map-reduce).

Ref.: Capítulo 4 — GraphRAG, §4.2.

---

## Nota esperada por perfil

- **5,0**: domina vector DBs e KGs, justifica GraphRAG com custo/benefício, escreve Cypher.
- **4,0**: diferencia tecnologias corretamente, com pequenas imprecisões em escala.
- **3,0**: conhece conceitos mas não articula quando usar vector vs grafo.
- **<3,0**: precisa revisar infraestrutura cognitiva.
