# ETHAGT07 — Roteiro da Apresentação

> Universidade Etho · Especialização em Programação Agêntica
> Fase B — Infraestrutura Cognitiva · 30 h

---

## Metadados

| Campo | Valor |
|---|---|
| Código | ETHAGT07 |
| Título | Knowledge Graphs & Vector Databases para Agentes |
| Duração | 90 min (2 blocos de 45 min) |
| Total de slides | 80 |
| Competências | C1 (A), C3 (B), C4 (A), C5 (I) |
| Pré-requisitos | ETHAGT06 (RAG & Retrieval Agêntico) |
| Fontes canônicas | Edge et al. *GraphRAG* (arXiv:2404.16130); Lewis et al. *RAG* (arXiv:2005.11401); Pan et al. *Unifying LLMs and KGs* (arXiv:2306.08302) |

---

## Fluxo da Aula

### BLOCO 1 — 45 min

| Seção | Slides | Tempo | Objetivo |
|---|---|---|---|
| A — Abertura | 1-6 | 8 min | Engajar, estabelecer objetivos e contextualizar a evolução do RAG |
| B — Vector DBs | 7-16 | 12 min | ANN (HNSW/IVF), métricas, filtering, sparse+dense |
| C — Comparativo | 17-25 | 10 min | Qdrant, Milvus, Weaviate, Chroma, pgvector; quando NÃO usar vector DB |
| D — Knowledge Graphs | 26-36 | 15 min | Triplas, Neo4j, Cypher, extração com LLM, inferência |
| Intervalo | — | 5 min | — |

### BLOCO 2 — 45 min

| Seção | Slides | Tempo | Objetivo |
|---|---|---|---|
| E — GraphRAG | 37-51 | 15 min | Microsoft GraphRAG, local vs global, DEMO, custos |
| F — Híbridos | 52-62 | 12 min | Vector + grafo, RetrievalAgent, manutenção, benchmark |
| G — Escala | 63-68 | 8 min | Sharding, reindexação, quantização, observabilidade |
| H — Fechamento | 69-80 | 10 min | Boas práticas, anti-patterns, caso, quiz, referências, Q&A |

---

## Pontos de Engajamento

| Slide | Tipo | Interação |
|---|---|---|
| 5 | Reflexão | "Quando uma busca por similaridade não é suficiente?" |
| 14 | Pergunta técnica | "Cosine vs dot — quando a diferença importa?" |
| 24 | Discussão | "Para um MVP, qual vector DB? E para 1M de usuários?" |
| 36 | Duplas (2 min) | "Qual a cardinalidade típica de um KG empresarial?" |
| 46 | DEMO ao vivo | GraphRAG em Neo4j (Lab 2) |
| 47 | Duplas (2 min) | "O GraphRAG errou algo? Qual o custo em tokens?" |
| 50 | Discussão | "Para qual domínio GraphRAG vale? E qual é overkill?" |
| 60 | Grupo | 5 cenários: vector, graph, ou híbrido? |
| 61 | Verdadeiro/falso | "Sempre preferir híbrido." |
| 75-77 | Quiz individual | 3 perguntas de verificação |

---

## Materiais Necessários

- [ ] Projetor / tela de compartilhamento
- [ ] VS Code aberto com `05-Labs/ETHAGT07/Lab2-GraphRAG-Neo4j`
- [ ] Terminal com Python 3.11+, Qdrant/Neo4j Docker e `OPENAI_API_KEY` configurada
- [ ] Neo4j Browser aberto para DEMO (Slide 46)
- [ ] Acesso ao repositório da especialização
- [ ] Quadro branco (para diagramas improvisados)
- [ ] Handout: storyboard impresso (opcional)

---

## Riscos e Planos B

| Risco | Plano B |
|---|---|
| Neo4j/LLM indisponível na DEMO (Slide 46) | Mostrar screenshots pré-gravados do Neo4j Browser + trace |
| Alunos sem pré-requisito de RAG (ETHAGT06) | Direcionar para ETHAGT06; oferecer recap rápido de embeddings no Slide 9 |
| Tempo estourado no Bloco 1 | Cortar exercício do Slide 36 (cardinalidade); mover para homework |
| Tempo estourado no Bloco 2 | Reduzir quiz para 2 perguntas (Slides 75-76); referências como leitura |
| Nenhuma pergunta no Q&A | Fazer pergunta inversa: "Qual parte foi menos clara — vector, grafo ou híbrido?" |
| Demora na extração de entidades na DEMO | Usar corpus menor pré-carregado; mostrar apenas a query multi-hop |

---

## Avaliação da Aula

- Quiz ao final (Slides 75-77): ≥2 acertos = compreensão básica
- Exercício de decisão (Slide 60): 5 cenários em grupos
- Perguntas de discussão (Slide 50): profundidade sobre ROI de GraphRAG
- Feedback informal: "Uma infraestrutura que você escolheria diferente após esta aula"
