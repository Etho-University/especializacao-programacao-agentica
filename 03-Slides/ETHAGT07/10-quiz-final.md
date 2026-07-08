# ETHAGT07 — Quiz Final

> Quiz individual, sem consulta, 5 perguntas de múltipla escolha.
> Tempo estimado: 5 min
**Critério**: ≥3 acertos = compreensão básica atingida.

---

## Pergunta 1

Qual métrica de similaridade é equivalente a dot product quando os embeddings estão normalizados?

- A) Euclidean (L2)
- B) Cosine
- C) Manhattan
- D) Jaccard

<details>
<summary>Resposta</summary>

**B) Cosine**

Quando os embeddings são normalizados (norma = 1), cosine e dot product dão o mesmo ranking. O cosine mede o ângulo entre vetores; o dot product é cosine × magnitudes. Com magnitude = 1, são idênticos. Por isso muita gente normaliza e usa dot (uma multiplicação a menos por dimensão). Euclidean mede distância, não ângulo. Manhattan é outra métrica. Jaccard é para conjuntos.
</details>

---

## Pergunta 2

Quando GraphRAG supera vector RAG de forma mais clara?

- A) Quando a pergunta é sobre um fato específico em um documento
- B) Quando a pergunta exige raciocínio multi-hop entre entidades
- C) Quando a latência é o requisito mais importante
- D) Quando o corpus é pequeno (< 100 documentos)

<details>
<summary>Resposta</summary>

**B) Quando a pergunta exige raciocínio multi-hop entre entidades**

GraphRAG brilha em perguntas que exigem encadear relacionamentos (A → B → C) ou visão global do corpus. Fato específico (A) é melhor com vector RAG. Latência baixa (C) é melhor com vector RAG (GraphRAG global é mais lento por map-reduce). Corpus pequeno (D) não justifica o custo de construção do GraphRAG.
</details>

---

## Pergunta 3

Em um pipeline híbrido, o que o RetrievalAgent faz?

- A) Sempre faz busca vetorial e grafo em paralelo
- B) Classifica a pergunta para escolher vector, graph ou híbrido
- C) Substitui o vector DB por um grafo
- D) Gera embeddings para o grafo

<details>
<summary>Resposta</summary>

**B) Classifica a pergunta para escolher vector, graph ou híbrido**

O RetrievalAgent é um router: classifica a intenção da pergunta e despacha para a estratégia certa. Nem toda pergunta precisa de híbrido — o router economiza retrieval desnecessário. "Sempre híbrido" (A) é mais caro e adiciona latência. O agente não substitui vector DB (C) nem gera embeddings para o grafo (D).
</details>

---

## Pergunta 4

Qual vector DB é mais indicado quando você JÁ USA PostgreSQL e não quer adicionar infraestrutura?

- A) Milvus
- B) Qdrant
- C) pgvector
- D) Chroma

<details>
<summary>Resposta</summary>

**C) pgvector**

pgvector é uma extensão do PostgreSQL — você adiciona vector DB dentro do Postgres que já tem, com ACID, transações e JOINs. Milvus (A) é para escala massiva (bilhões). Qdrant (B) é para filtering complexo. Chroma (D) é para prototipagem. Se já tem Postgres e o volume é até ~1M, pgvector resolve sem nova infra.
</details>

---

## Pergunta 5

Qual é o PRINCIPAL risco de confiar cegamente em triplas extraídas por LLM?

- A) O grafo fica muito grande
- B) Alucinação — o LLM inventa relações inexistentes
- C) A query Cypher fica lenta
- D) O vector DB fica desatualizado

<details>
<summary>Resposta</summary>

**B) Alucinação — o LLM inventa relações inexistentes**

LLMs podem alucinar relações que não estão no texto de origem. Sem validação (schema restrito + verificação + score de confiança), o grafo fica contaminado com triplas falsas — e o agente raciocina sobre elas com confiança. O tamanho do grafo (A) não é o problema principal. Cypher lenta (C) é problema de query, não de extração. Vector DB (D) é independente da extração de triplas.

Mitigação: schema restrito (só permita predicados pré-definidos), validação (a relação está no texto?), e score de confiança na aresta (mantém, mas com flag de "baixa confiança").
</details>

---

## Pergunta Bônus (não conta para nota)

Qual algoritmo é usado pelo GraphRAG da Microsoft para detecção de comunidades?

- A) K-means
- B) Leiden
- C) HNSW
- D) PageRank

<details>
<summary>Resposta</summary>

**B) Leiden**

O GraphRAG da Microsoft usa o algoritmo Leiden para detecção de comunidades — grupos de entidades densamente conectadas entre si. K-means (A) é para clustering de vetores (usado em IVF). HNSW (C) é para ANN (busca de vizinhos). PageRank (D) é para ranquear nós por centralidade. Leiden detecta a estrutura comunitária que permite a sumarização hierárquica do GraphRAG.
</details>

---

## Resultado

| Acertos | Avaliação |
|---|---|
| 5/5 | Excelente — compreensão completa de vector, grafo e GraphRAG |
| 4/5 | Bom — compreensão sólida, revisar 1 ponto |
| 3/5 | Suficiente — revisar 2 pontos |
| 2/5 | Insuficiente — reler Edge et al. GraphRAG + revisar slides de vector DB |
| 0-1/5 | Crítico — agendar horário com professor |
