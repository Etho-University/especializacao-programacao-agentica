# ETHAGT07 — Knowledge Graphs & Vector Databases para Agentes

> **Apostila do curso** · Especialização em Programação Agêntica · Universidade Etho
> Fase B — Razão, Memória e Conhecimento · Carga 30 h · Versão 1.0 · Julho 2026
> *Material de referência duradouro (nível pós-graduação lato sensu). Os slides são auxiliares.*

---

## Sumário

- **Capítulo 1** — Vector databases: o modelo mental
- **Capítulo 2** — Comparativo de vector DBs
- **Capítulo 3** — Knowledge graphs
- **Capítulo 4** — GraphRAG
- **Capítulo 5** — Pipelines híbridos (vector + grafo)
- **Capítulo 6** — Operação em escala
- **Capítulo 7** — Casos de estudo
- **Capítulo 8** — Referências e leituras

---

## Capítulo 1 — Vector databases: o modelo mental

### 1.1 Infraestrutura cognitiva do agente

ETHAGT06 tratou a *recuperação agêntica* — as estratégias de RAG que decidem quando e o que recuperar. Este módulo desce um nível: a **infraestrutura** que sustenta essa recuperação. Um agente precisa de duas formas complementares de armazenar conhecimento: **vetorial** (para similaridade semântica) e **estrutural** (knowledge graphs, para relações e raciocínio multi-hop). Saber escolher, modelar e operar ambas é o que torna o conhecimento do agente *escalável e confiável*.

### 1.2 O problema da busca por similaridade

A recuperação vetorial resolve um problema: dado um vetor de consulta (o embedding da pergunta), encontrar os vetores *mais próximos* num conjunto grande. O desafio computacional é que a busca exata (comparar com todos) é O(N) — inviável em milhões de vetores. A solução é a **Approximate Nearest Neighbor (ANN)**: algoritmos que *aproximam* o resultado exato, trocando um pouco de recall por velocidade enorme.

### 1.3 HNSW: o algoritmo dominante

O **HNSW** (Hierarchical Navigable Small World, Malkov & Yashunin) é o algoritmo ANN dominante nos vector DBs modernos. A ideia: construir um grafo *hierárquico* onde a busca navega de nó em nó, descendo as camadas da hierarquia até o vizinho mais próximo — como encontrar um amigo numa multidão indo de grupo em grupo. O HNSW oferece excelente equilíbrio entre recall, latência e memória.

Outra família é o **IVF** (Inverted File Index): particiona o espaço em células (via clustering), e a busca examina só as células mais próximas da consulta. HNSW e IVF podem combinar-se (IVF-HNSW). Você não precisa implementá-los, mas precisa saber que *existem* e que seus parâmetros (ex.: `ef_construction`, `ef_search` e `M` para HNSW; `nlist` para IVF) afetam o trade-off recall/latência.

### 1.4 Métricas de similaridade

| Métrica | Quando usar |
|---|---|
| **Cosine** | Quando a *direção* importa, não a magnitude (mais comum em texto) |
| **Dot product** | Embeddings já normalizados; eficiente |
| **Euclidean (L2)** | Quando a distância geométrica é significativa (pouco comum em texto) |

A escolha da métrica deve casar com o embedding: se o modelo de embedding foi treinado para cosine, use cosine. Misturar métrica e embedding treinado para outra degrada o recall.

### 1.5 Metadata filtering (payloads)

Raramente você busca "no universo todo": quase sempre há um filtro ("documentos deste usuário", "deste período", "deste tipo"). Os vector DBs modernos suportam **metadata filtering** — filtrar por atributos *antes* ou *durante* a busca vetorial. Isso é crítico para multi-tenancy (cada usuário só vê seus dados) e para precisão (restringir o espaço de busca melhora relevância). A qualidade e eficiência do filtering é um diferencial competitivo entre vector DBs (Qdrant destaca-se aqui).

### 1.6 Busca híbrida: sparse + dense

Como vimos em ETHAGT06 §6.4, combinar busca *densa* (vetorial) com *esparsa* (BM25/keyword) captura casos que cada uma perde. Operacionalmente, muitos vector DBs agora suportam *ambas* nativamente (Weaviate, Qdrant com sparse vectors), permitindo buscar híbrido num único sistema. A fusão dos scores (ex.: Reciprocal Rank Fusion) combina os rankings.

---

## Capítulo 2 — Comparativo de vector DBs

### 2.1 Não há "melhor vector DB"

A pergunta "qual o melhor vector DB?" é mal formulada: depende do cenário. Este capítulo compara as opções principais por *eixo de adequação*, não por ranking absoluto.

| Vector DB | Forte em | Quando escolher |
|---|---|---|
| **Qdrant** | Filtering robusto, performance (Rust), API limpa | Filtros complexos, multi-tenancy, production-ready |
| **Milvus** | Escala massiva, arquitetura distribuída | Bilhões de vetores, clusters grandes |
| **Weaviate** | Modules (embeddings, reranking built-in), híbrido | DX alto, quer tudo num sistema |
| **Chroma** | Simplicidade, setup zero | Protótipos, desenvolvimento, volumes pequenos |
| **pgvector** | Já está no Postgres | Operacional: não quer adicionar um sistema novo; volumes médios |

> **Diagrama de referência:** [`12-Diagrams/ETHAGT07/vector-vs-graph.mmd`](../../12-Diagrams/ETHAGT07/vector-vs-graph.mmd).

### 2.2 Quando *não* usar vector DB

Nem todo problema de busca pede um vector DB. Casos onde uma alternativa é melhor:

- **Consulta exata por chave estruturada:** um banco relacional (SQL) é mais barato, preciso e consistente. ("Qual o saldo da conta X?")
- **Poucos documentos (< alguns milhares):** uma busca linear in-memory é instantânea e trivial — não adicione infraestrutura.
- **Relações entre entidades:** um knowledge graph (Capítulo 3) raciocina melhor que vetores.

O anti-pattern: adicionar um vector DB quando um `LIKE` ou um join SQL resolveria, criando complexidade operacional desnecessária.

### 2.3 pgvector: a opção operacional

O **pgvector** merece destaque porque resolve um dilema comum: você *já* tem Postgres, e quer adicionar busca vetorial sem introduzir um novo sistema. O pgvector é uma extensão que adiciona tipos e índices vetoriais ao Postgres, permitindo combinar busca vetorial com consultas relacionais *na mesma query*. Para volumes médios e operações que valorizam simplicidade de stack, é frequentemente a escolha certa.

---

## Capítulo 3 — Knowledge graphs

### 3.1 Conhecimento estruturado vs similaridade

Um vector DB responde "o que é *parecido* com isto?". Um **knowledge graph (KG)** responde "o que está *relacionado* com isto, e *como*?". Essa diferença é fundamental: para raciocínio sobre *relações* (quem trabalha com quem, qual drug interage com qual, qual documento referencia qual), a estrutura de grafo é intrinsecamente superior à similaridade vetorial.

### 3.2 O modelo: triplas, propriedades, labels

Um KG modela o conhecimento como **triplas** `(sujeito, predicado, objeto)` — ex.: `(Ana, trabalha_com, Bob)`. Em grafos de propriedades (o modelo do Neo4j), nós e arestas têm *propriedades* (atributos chave-valor) e *labels* (tipos):

```
(:Pessoa {nome:"Ana"}) -[:TRABALHA_COM {desde:2022}]-> (:Pessoa {nome:"Bob"})
```

### 3.3 Neo4j e Cypher

O **Neo4j** é o banco de grafos dominante, com a linguagem de consulta **Cypher** (declarativa, pattern-matching). Uma query típica:

```cypher
MATCH (a:Pessoa {nome:"Ana"})-[:COAUTORA*1..3]-(coautor)
RETURN DISTINCT coautor.nome
```

Esta query encontra co-autores de Ana em até 3 "saltos" de coautoria — algo que um vector DB não consegue expressar, mas que num grafo é uma travessia natural.

### 3.4 Modelagem para raciocínio

Modelar um KG para agentes requer pensar em *quais entidades e relações importam para o raciocínio*. Ex.: num domínio farmacêutico, entidades como `Drug`, `Disease`, `Gene`, `Protein` e relações como `TREATS`, `INTERACTS_WITH`, `TARGETS`. A qualidade do schema determina a utilidade — um KG mal modelado é tão inútil quanto um vector DB mal chunkado.

### 3.5 Extração de entidades/relações com LLM

Como popular um KG a partir de texto não-estruturado? Com LLM: dê ao modelo o texto e peça para extrair entidades e relações como triplas. Esse pipeline (*LLM-based knowledge extraction*) é escalável, mas ruidoso — requer desduplicação de entidades (sinônimos), validação e cura. O GraphRAG (Capítulo 4) automatiza parte disso.

---

## Capítulo 4 — GraphRAG

### 4.1 Do local ao global

O **GraphRAG** (Edge et al., Microsoft, 2024; arXiv:2404.16130) é a ponte entre KG e RAG. A motivação: o RAG vetorial responde bem a perguntas *locais* ("o que diz este chunk?"), mas falha em perguntas *globais* ("quais os temas principais deste corpus?", "como estes documentos se conectam?"), porque nenhuma parte individual contém a resposta. O GraphRAG constrói um KG a partir do corpus e usa sua estrutura para responder perguntas globais.

> **Diagrama de referência:** [`12-Diagrams/ETHAGT07/graphrag-pipeline.mmd`](../../12-Diagrams/ETHAGT07/graphrag-pipeline.mmd).

### 4.2 O pipeline GraphRAG

1. **Extração:** o LLM extrai entidades e relações do corpus, formando um grafo.
2. **Comunidades:** um algoritmo de detecção de comunidades (ex.: Leiden) agrupa nós relacionados.
3. **Sumarização hierárquica:** cada comunidade é sumarizada pelo LLM, gerando descrições em múltiplos níveis.
4. **Consulta:**
   - *Local search:* para perguntas sobre entidades específicas — atravessa o grafo local.
   - *Global search:* para perguntas globais — agrega os sumários de comunidade (map-reduce sobre as comunidades).

### 4.3 Quando GraphRAG supera o vector RAG

GraphRAG brilha em:
- **Perguntas globais/sintetizadoras** ("quais os temas principais?").
- **Raciocínio multi-hop** explícito (travessia de relações).
- **Corpus onde as conexões são o conhecimento** (jurídico, científico).

Vector RAG ainda vence em:
- **Perguntas factuais locais** diretas.
- **Latência/custo sensíveis** (GraphRAG é caro de construir).

### 4.4 O custo do GraphRAG

GraphRAG é **caro de construir**: extrair entidades/relações de um corpus grande exige muitas chamadas LLM. A construção pode custar ordens de magnitude mais que um vector DB. Esse custo é *amortizado* se o KG for consultado muitas vezes — mas para corpora voláteis, a reconstrução frequente é proibitiva. Mitigação: atualização *incremental* (adicionar novas entidades/relações sem reconstruir tudo).

---

## Capítulo 5 — Pipelines híbridos (vector + grafo)

### 5.1 O melhor dos dois mundos

A conclusão natural dos capítulos anteriores: **não é vector *ou* grafo — é vector *e* grafo.** Um pipeline híbrido usa o vector DB para recall por similaridade e o KG para raciocínio sobre relações, combinando os resultados.

> **Diagrama de referência:** [`12-Diagrams/ETHAGT07/hybrid-retrieval.mmd`](../../12-Diagrams/ETHAGT07/hybrid-retrieval.mmd).

### 5.2 O RetrievalAgent que escolhe estratégia

A forma mais agêntica do híbrido: um agente que *decide* qual estratégia usar por pergunta. Pergunta factual local → vector. Pergunta sobre relações → grafo. Pergunta global → GraphRAG global. Cada fonte é uma ferramenta (ETHAGT02), e o agente escolhe — exatamente o Agentic RAG do ETHAGT05 §5, agora com mais fontes.

```python
tools = [search_vector, query_graph, graphrag_global]
agente = Agent(tools=tools, system=HYBRID_RETRIEVAL_PROMPT)
```

### 5.3 Manutenção: incremental update e lineage

Corpora mudam: novos documentos, atualizações, remoções. Manter vector DB e KG sincronizados e atualizados requer:

- **Incremental update:** adicionar/marcar removidos sem reconstrução total.
- **Lineage:** rastrear de qual documento cada fato/entidade veio (para invalidação).
- **Drift de embeddings:** ao retreinar o modelo de embedding, os vetores antigos ficam inconsistentes — reindexação necessária (Capítulo 6).

### 5.4 "Sempre preferir híbrido"?

Não. Híbrido adiciona complexidade operacional (dois sistemas para manter). Para aplicações simples, um vector DB basta. A regra de projeto (recorrente no curso): **adicione complexidade só com evidência de que ela melhora o resultado.** Meça: se o híbrido melhora o success rate em casos multi-hop sem explodir custo, justifica-se; senão, é overhead.

---

## Capítulo 6 — Operação em escala

### 6.1 Sharding e replicação

Em volumes grandes, um único nó não basta. Vector DBs distribuem dados por *sharding* (partição horizontal) e garantem disponibilidade por *replicação*. O trade-off clássico (CAP): consistência vs disponibilidade vs tolerância a partição. Para RAG, *consistência eventual* costuma ser aceitável (um documento indexado com leve atraso não quebra a aplicação).

### 6.2 Reindexação e drift de embeddings

Dois cenários exigem reindexação:

1. **Drift de modelo:** você troca o modelo de embedding (ex.: para um melhor). Vetores antigos e novos são *incompatíveis* — precisa re-embedar e reindexar tudo.
2. **Crescimento além do índice:** parâmetros do HNSW/IVF calibrados para N vetores degradam em 10N.

Planeje a reindexação como uma operação de manutenção *esperada*, não uma surpresa.

### 6.3 Custo de armazenamento e query

Vetores são *grandes* (ex.: 1536 dimensões × 4 bytes = ~6 KB por vetor; milhões de vetores = GB). Armazenamento, memória RAM (para índices rápidos) e custo de query escalam com o volume. Quantização (reduzir precisão dos vetores, ex.: int8 em vez de float32) reduz memória com leve perda de recall — uma otimização comum em escala.

### 6.4 Observabilidade

Em produção, meça: latência de query (p50/p95/p99), recall@K (em amostras rotuladas), taxa de cache hit, tamanho do índice. Sem essas métricas, a degradação é invisível até virar incidente.

---

## Capítulo 7 — Casos de estudo

### 7.1 Farmacêutico e jurídico

Domínios ricos em relações (farmacêutico: drug-gene-disease; jurídico: lei-jurisprudência-artigo) são os casos canônicos de GraphRAG e híbrido. A lição: nesses domínios, o raciocínio multi-hop é *intrínseco* à tarefa, e a estrutura de grafo não é opcional — é o que torna as respostas corretas possíveis.

> **Leitura.** Detalhes em [`09-CaseStudies/`](../../09-CaseStudies/).

### 7.2 Lições transversais

1. **Vector para similaridade, grafo para relações, relacional para fatos estruturados** — frequentemente os três coexistem.
2. **A construção é o custo escondido.** GraphRAG e KG caros de construir; planeje amortização.
3. **Escolha por evidência, não por hype.** "Vector DB resolve tudo" é o anti-pattern que este módulo desmonta.

---

## Capítulo 8 — Referências e leituras

### 8.1 Bibliografia fundamental

- **Edge, D. et al.** *GraphRAG: From Local to Global.* Microsoft, 2024. arXiv:2404.16130. 🏛
- **Pan, S. et al.** *Unifying Large Language Models and Knowledge Graphs.* arXiv:2306.08302. 🏛
- **Lewis, P. et al.** *RAG original.* NeurIPS 2020. arXiv:2005.11401. 🏛

### 8.2 Bibliografia complementar

- **Malkov, Y. & Yashunin, D.** *HNSW.* — algoritmo ANN dominante.
- **Microsoft GraphRAG** — implementação de referência (GitHub).
- **Documentação:** Qdrant, Milvus, Weaviate, Chroma, pgvector, Neo4j.

### 8.3 Recursos práticos

- **Cypher** — linguagem de query do Neo4j.
- **LangGraph examples:** `tutorials/tnt-llm/` (graph + LLM).
- **Padrões RAG:** [`15-RAG/graph-rag.md`](../../15-RAG/graph-rag.md).

### 8.4 Ficha de pesquisa

Fontes em [`20-Research/ETHAGT07-pesquisa.md`](../../20-Research/ETHAGT07-pesquisa.md). Última consulta: Julho 2026.

---

## Síntese do módulo

Ao concluir ETHAGT07, você deve ser capaz de:

1. **Comparar** vector DBs por cenário e escolher conscientemente (incluindo *não* usar um).
2. **Modelar** knowledge graphs para raciocínio estruturado e extraí-los com LLM.
3. **Implementar** GraphRAG (local + global) e justificar seu custo.
4. **Construir** pipelines híbridos com um RetrievalAgent que escolhe estratégia.
5. **Operar** em escala (sharding, reindexação, drift, custo).

Próximos passos: ETHAGT14 aprofunda escalabilidade distribuída; ETHAGT90 integra vector + grafo no Capstone. Com ETHAGT07, encerra-se a Fase B — o agente agora raciocina (ETHAGT04), lembra (ETHAGT05) e conhece (ETHAGT06/07).

---

*Mantido por: Escola de Tecnologia — Universidade Etho · Área de Inteligência Artificial · Versão 1.0 · Julho 2026*
