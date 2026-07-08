# ETHAGT07 — Knowledge Graphs & Vector Databases para Agentes
## Storyboard da Apresentação

> **Universidade Etho · Especialização em Programação Agêntica**
> Fase B — Infraestrutura Cognitiva · 30 h
> Storyboard v1.0 · Julho 2026

---

## Metadados da Apresentação

| Campo | Valor |
|---|---|
| Código | ETHAGT07 |
| Título | Knowledge Graphs & Vector Databases para Agentes |
| Duração estimada | 90 min (2 blocos de 45 min) |
| Total de slides | 80 |
| Público | Arquitetos, Engenheiros de Software, Engenheiros de IA, Cientistas de Dados, Tech Leads |
| Pré-requisitos | ETHAGT06 (RAG & Retrieval Agêntico) |
| Competências | C1 (A), C3 (B), C4 (A), C5 (I) |

---

## Mapa Visual da Apresentação

```
BLOCO 1 (45 min)                              BLOCO 2 (45 min)
┌──────────────────────────────┐              ┌──────────────────────────────┐
│ SEÇÃO A — Abertura (8 min)   │              │ SEÇÃO E — GraphRAG (15 min) │
│  Capa · Objetivos · Agenda   │              │  Microsoft GraphRAG · Local │
│  Motivação · Contexto        │              │  vs Global · DEMO · Custos  │
├──────────────────────────────┤              ├──────────────────────────────┤
│ SEÇÃO B — Vector DBs (12 min)│              │ SEÇÃO F — Híbridos (12 min) │
│  ANN · HNSW · IVF · Métricas │              │  Vector + Grafo · Router ·  │
│  Filtering · Sparse + Dense  │              │  Manutenção · Benchmark     │
├──────────────────────────────┤              ├──────────────────────────────┤
│ SEÇÃO C — Comparativo (10 m) │              │ SEÇÃO G — Escala (8 min)    │
│  Qdrant · Milvus · Weaviate  │              │  Sharding · Reindexação ·   │
│  Chroma · pgvector · Decisão │              │  Custo · Observabilidade    │
├──────────────────────────────┤              ├──────────────────────────────┤
│ SEÇÃO D — Knowledge Graphs   │              │ SEÇÃO H — Fechamento (10 m) │
│  (15 min)                    │              │  Boas práticas · Caso ·     │
│  Triplas · Neo4j · Cypher ·  │              │  Resumo · Quiz · Referências│
│  Extração · Inferência       │              │  · Next · Q&A               │
└──────────────────────────────┘              └──────────────────────────────┘
```

---

## Storyboard Detalhado

### SEÇÃO A — Abertura (Slides 1-6 · 8 min)

---

#### Slide 1 — Capa
- **Tipo**: Capa
- **Objetivo**: Identificar a aula, professor e contexto
- **Conteúdo**:
  - ETHAGT07 — Knowledge Graphs & Vector Databases para Agentes
  - Universidade Etho · Especialização em Programação Agêntica
  - Fase B — Infraestrutura Cognitiva
  - Professor · Data
- **Diagrama**: Logo Etho + imagem de fundo abstrata (rede de nós + vetores)
- **Animação**: Fade in do título
- **Tempo**: 1 min

---

#### Slide 2 — Objetivos do Módulo
- **Tipo**: Conteúdo
- **Objetivo**: Deixar claro o que o aluno deve conseguir fazer ao final
- **Conteúdo**:
  - Objetivo geral: Escolher, modelar e operar vector databases e knowledge graphs como infraestrutura cognitiva de agentes — incluindo GraphRAG
  - 5 objetivos específicos (1 linha cada):
    1. Comparar vector databases por cenário
    2. Modelar knowledge graphs para raciocínio estruturado
    3. Implementar GraphRAG (local + global)
    4. Construir pipelines híbridos (vector + grafo)
    5. Avaliar custo/latência/escala em volumes realistas
- **Diagrama**: Ícones representando cada objetivo
- **Animação**: Aparecer objetivos um a um (on click)
- **Tempo**: 2 min

---

#### Slide 3 — Competências Desenvolvidas
- **Tipo**: Conteúdo
- **Objetivo**: Conectar a aula ao Framework Etho de competências
- **Conteúdo**:
  - Tabela: 4 competências com nível B/I/A
  - C1 Programação Agêntica → **A**
  - C3 MCP & Tool Use → B
  - C4 Agent Memory → **A**
  - C5 AgentOps & Avaliação → I
  - Badge visual por competência
- **Diagrama**: Radar chart dos 4 pilares
- **Animação**: Radar aparece com wipe
- **Tempo**: 1 min

---

#### Slide 4 — Agenda
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar o roteiro da aula com tempos
- **Conteúdo**:
  - Bloco 1: Abertura → Vector DBs → Comparativo → Knowledge Graphs
  - Bloco 2: GraphRAG → Pipelines Híbridos → Operação em Escala → Fechamento
  - Tempos estimados por seção
- **Diagrama**: Timeline horizontal com 8 seções
- **Animação**: Timeline cresce da esquerda para direita
- **Tempo**: 1 min

---

#### Slide 5 — Motivação: Quando Similaridade Não Basta
- **Tipo**: Conteúdo
- **Objetivo**: Criar tensão — vector search sozinho não captura relacionamentos
- **Conteúdo**:
  - Vector search: encontra documentos *similares* por semântica
  - Mas: não sabe que "Dipirona" e "Sulfametoxazol" interagem
  - Exemplo: "Quais medicamentos interagem com o remédio que o Dr. Silva prescreveu para o paciente X?"
  - Vector search sozinho: retorna textos *sobre* interações, mas não *raciocina* sobre a cadeia
  - Pergunta: *Quando uma busca por similaridade não é suficiente?*
- **Diagrama**: Split — lado esquerdo (vector: nuvem de pontos), lado direito (grafo: nós conectados)
- **Animação**: Split — lado esquerdo primeiro, depois lado direito
- **Tempo**: 2 min

---

#### Slide 6 — Contexto: A Evolução do RAG
- **Tipo**: Conteúdo
- **Objetivo**: Explicar a evolução de RAG simples para GraphRAG
- **Conteúdo**:
  - Linha do tempo: 2020 (RAG original, Lewis) → 2022 (dense retrieval) → 2023 (RAG agêntico) → 2024 (GraphRAG, Microsoft)
  - Confluência: embeddings melhores + graph databases acessíveis + LLMs para extração de entidades
  - arXiv:2005.11401 — RAG base
  - arXiv:2404.16130 — GraphRAG (Microsoft)
  - arXiv:2306.08302 — Pan et al., LLMs + KGs (survey)
- **Diagrama**: Timeline horizontal com marcos
- **Animação**: Marcos aparecem sequencialmente
- **Tempo**: 1 min

---

### SEÇÃO B — Vector DBs: Modelo Mental (Slides 7-16 · 12 min)

---

#### Slide 7 — [SEÇÃO] Vector DBs: Modelo Mental
- **Tipo**: Seção
- **Objetivo**: Transição para o bloco de fundamentos de vector DBs
- **Conteúdo**: Número "1" grande + "Vector DBs: Modelo Mental"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 8 — O Que É um Vector DB?
- **Tipo**: Diagrama
- **Objetivo**: Apresentar a arquitetura canônica de um vector database
- **Conteúdo**:
  - Armazena embeddings (vetores densos) + metadata
  - Index para busca ANN (não brute force)
  - Query: vetor → top-k mais similares
  - Componentes: collection → points (id, vector, payload) → index
  - Diferença de DB relacional: similaridade, não igualdade
- **Diagrama**: Arquitetura de vector DB (collection → index → query)
- **Animação**: Componentes surgem do centro para fora
- **Tempo**: 2 min

---

#### Slide 9 — Embeddings: A Base
- **Tipo**: Conteúdo
- **Objetivo**: Recapitular embeddings (aprofundado em ETHAGT06)
- **Conteúdo**:
  - Texto → modelo de embedding → vetor denso (ex: 1536 dims)
  - Semântica capturada na geometria do espaço
  - Modelos: OpenAI text-embedding-3, Cohere, BGE, GTE
  - Dimensões: trade-off entre riqueza e custo de armazenamento/busca
  - Aprofundamento em ETHAGT06
- **Diagrama**: Texto → embedding → espaço vetorial (pontos próximos)
- **Tempo**: 1 min

---

#### Slide 10 — ANN: Approximate Nearest Neighbor
- **Tipo**: Conteúdo
- **Objetivo**: Explicar por que não usamos brute force
- **Conteúdo**:
  - Brute force: O(N) — inviável para milhões de vetores
  - ANN: sacrifica exatidão por velocidade (recall vs latência)
  - Duas famílias principais: HNSW (graph-based) e IVF (cluster-based)
  - Trade-off fundamental: recall ↑ → latência ↑
  - Parâmetro de controle: ef_search (HNSW), nprobe (IVF)
- **Diagrama**: Curva recall vs latência
- **Tempo**: 1.5 min

---

#### Slide 11 — HNSW: Hierarchical Navigable Small World
- **Tipo**: Diagrama
- **Objetivo**: Apresentar o algoritmo dominante em vector DBs
- **Conteúdo**:
  - Grafo hierárquico de camadas: top (sparse, fast) → bottom (dense, precise)
  - Busca: começa no topo, desce camada por camada
  - Vantagem: recall alto, latência baixa
  - Desvantagem: construção lenta, memória
  - Usado por: Qdrant, Milvus, Weaviate, pgvector (opcional)
  - Fonte: Malkov & Yashunin, arXiv:1603.09320
- **Diagrama**: Estrutura hierárquica de HNSW (3 camadas)
- **Animação**: Camadas aparecem de cima para baixo
- **Tempo**: 2 min

---

#### Slide 12 — IVF: Inverted File Index
- **Tipo**: Diagrama
- **Objetivo**: Apresentar a alternativa baseada em clustering
- **Conteúdo**:
  - K-means divide o espaço em clusters (Voronoi cells)
  - Busca: encontra cluster mais próximo → busca dentro dele
  - nprobe: quantos clusters vizinhos explorar
  - Vantagem: construção mais rápida, bom para datasets muito grandes
  - Desvantagem: recall menor que HNSW para mesmo custo
  - Combinável com PQ (Product Quantization) para compressão
- **Diagrama**: Espaço particionado em células de Voronoi
- **Tempo**: 1.5 min

---

#### Slide 13 — Métricas de Similaridade: Cosine, Dot, Euclidean
- **Tipo**: Comparação
- **Objetivo**: Apresentar as 3 métricas e quando usar cada
- **Conteúdo**:
  - Cosine: ângulo entre vetores — ignora magnitude
  - Dot product: cosine × magnitudes — sensível a norma
  - Euclidean (L2): distância geométrica — sensível a magnitude e direção
  - Fórmulas visuais para cada
  - Se embeddings são normalizados: cosine = dot product
- **Diagrama**: 3 visualizações lado a lado (círculo unitário, plano, distância)
- **Animação**: Cada métrica aparece com click
- **Tempo**: 2 min

---

#### Slide 14 — Quando Cada Métrica?
- **Tipo**: Conteúdo
- **Objetivo**: Dar critério prático de escolha
- **Conteúdo**:
  - Cosine: default para texto (embeddings não normalizados)
  - Dot: quando embeddings já são normalizados (mais rápido)
  - Euclidean: quando magnitude importa (ex: features multimodais)
  - Pergunta técnica: *Cosine vs dot — quando a diferença importa?*
  - Armadilha: misturar métricas entre index e query = recall destruído
- **Diagrama**: Árvore de decisão simples
- **Tempo**: 1 min

---

#### Slide 15 — Metadata Filtering (Payloads)
- **Tipo**: Diagrama
- **Objetivo**: Explicar filtering de metadata e o trade-off pre vs post
- **Conteúdo**:
  - Payload: JSON anexado a cada vetor (ex: `{"source": "doc.pdf", "page": 3}`)
  - Pre-filtering: filtra antes da busca ANN (preciso, mas pode ser lento)
  - Post-filtering: filtra depois da busca ANN (rápido, mas pode reduzir recall)
  - Qdrant: filtering otimizado no index (vantagem chave)
  - Padrão: `vector + filter → top-k`
- **Diagrama**: Fluxo pre-filter vs post-filter
- **Tempo**: 1.5 min

---

#### Slide 16 — Híbrido: Sparse + Dense (BM25 + Dense)
- **Tipo**: Diagrama
- **Objetivo**: Introduzir retrieval híbrido sparse+dense
- **Conteúdo**:
  - Dense: semântica (sinônimos, paráfrase) — falha em termos exatos
  - Sparse (BM25/SPLADE): termos exatos (nomes próprios, códigos) — falha em semântica
  - Híbrido: combina ambos com fusão de scores (RRF ou ponderado)
  - Reciprocal Rank Fusion (RRF): simples e eficaz
  - Qdrant 1.10+: sparse vectors nativos
- **Diagrama**: Duas trilhas (sparse + dense) convergindo para RRF
- **Tempo**: 1 min

---

### SEÇÃO C — Comparativo de Vector DBs (Slides 17-25 · 10 min)

---

#### Slide 17 — [SEÇÃO] Comparativo de Vector DBs
- **Tipo**: Seção
- **Objetivo**: Transição para o comparativo prático
- **Conteúdo**: "2 — Comparativo de Vector DBs"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 18 — O Landscape: 5 Contenders
- **Tipo**: Diagrama
- **Objetivo**: Visão geral do ecossistema
- **Conteúdo**:
  - 5 vector DBs canônicos: Qdrant, Milvus, Weaviate, Chroma, pgvector
  - Eixos de comparação: linguagem, escala, filtering, ecosystem, maturidade
  - Não existe "melhor" — existe "melhor para seu cenário"
- **Diagrama**: Grid 2x3 com logos e 1 linha de descrição cada
- **Animação**: Cada DB aparece com click
- **Tempo**: 1.5 min

---

#### Slide 19 — Qdrant: Filtering Forte
- **Tipo**: Conteúdo
- **Objetivo**: Destacar os pontos fortes do Qdrant
- **Conteúdo**:
  - Escrito em Rust: performance e safety
  - Filtering otimizado no index (não é post-filter)
  - Sparse vectors nativos (híbrido sem infra extra)
  - Multi-tenancy via payloads
  - Melhor quando: filtering complexo é requisito
- **Diagrama**: Logo + bullet points
- **Tempo**: 1 min

---

#### Slide 20 — Milvus: Escala
- **Tipo**: Conteúdo
- **Objetivo**: Destacar os pontos fortes do Milvus
- **Conteúdo**:
  - Arquitetura distribuída desde o início (cloud-native)
  - Escala horizontal para bilhões de vetores
  - Suporte a múltiplos index types (HNSW, IVF, DiskANN)
  - Melhor quando: escala massiva é o requisito #1
  - Trade-off: complexidade operacional maior
- **Diagrama**: Logo + bullet points
- **Tempo**: 1 min

---

#### Slide 21 — Weaviate: Modules
- **Tipo**: Conteúdo
- **Objetivo**: Destacar os pontos fortes do Weaviate
- **Conteúdo**:
  - Modules integrados: generative, Q&A, multi-modal
  - Schema-first: define classes e propriedades
  - GraphQL API nativa
  - Melhor quando: quer pipeline RAG completo sem orquestrar 5 serviços
  - Trade-off: menos flexível para casos não previstos pelos modules
- **Diagrama**: Logo + bullet points
- **Tempo**: 1 min

---

#### Slide 22 — Chroma: Simplicidade
- **Tipo**: Conteúdo
- **Objetivo**: Destacar os pontos fortes do Chroma
- **Conteúdo**:
  - API minimalista: `client.add(docs)` → `client.query(text)`
  - Embutido no processo Python (sem servidor separado)
  - Melhor quando: prototipagem, MVP, dev local
  - Trade-off: não é production-ready para escala (ainda)
- **Diagrama**: Logo + bullet points
- **Tempo**: 1 min

---

#### Slide 23 — pgvector: Operacional
- **Tipo**: Conteúdo
- **Objetivo**: Destacar os pontos fortes do pgvector
- **Conteúdo**:
  - Extensão do PostgreSQL: vector DB dentro do DB que você já tem
  - HNSW e IVFFlat disponíveis
  - ACID, transações, JOINs com vetores
  - Melhor quando: já usa Postgres e não quer adicionar infra
  - Trade-off: não escala como solução dedicada para bilhões de vetores
- **Diagrama**: Logo + bullet points
- **Tempo**: 1 min

---

#### Slide 24 — Tabela Comparativa
- **Tipo**: Comparação
- **Objetivo**: Sistematizar os trade-offs
- **Conteúdo**:
  - Tabela: Qdrant vs Milvus vs Weaviate vs Chroma vs pgvector
  - Eixos: linguagem, escala máxima, filtering, híbrido, multi-tenancy, custo operacional, curva de aprendizado, production-ready
  - Discussão: *Para um MVP, qual escolher? E para 1M de usuários?*
- **Diagrama**: Tabela comparativa colorida (heat map)
- **Tempo**: 2 min

---

#### Slide 25 — Quando NÃO Usar Vector DB
- **Tipo**: Conteúdo
- **Objetivo**: Ser honesto — vector DB nem sempre é a resposta
- **Conteúdo**:
  - Busca exata (igualdade): DB relacional é melhor
  - Dados estruturados com relacionamentos: knowledge graph
  - Volume pequeno (< 10k docs): brute force em memória
  - Latência ultra-baixa: cache + keyword search
  - Regra: não adicione vector DB se Postgres resolve
- **Diagrama**: Árvore de decisão "preciso de vector DB?"
- **Tempo**: 1.5 min

---

### SEÇÃO D — Knowledge Graphs (Slides 26-40 · 15 min)

---

#### Slide 26 — [SEÇÃO] Knowledge Graphs
- **Tipo**: Seção
- **Objetivo**: Transição para o bloco de knowledge graphs
- **Conteúdo**: Número "3" grande + "Knowledge Graphs"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 27 — O Que É um Knowledge Graph?
- **Tipo**: Comparação
- **Objetivo**: Apresentar a diferença fundamental: vector vs graph
- **Conteúdo**:
  - Vector DB: similaridade semântica (proximidade no espaço)
  - Knowledge Graph: relacionamentos estruturados (travessia de nós)
  - Vector: "documentos parecidos com X"
  - Graph: "entidades conectadas a X via relação Y"
  - Complementares, não concorrentes
- **Diagrama**: `12-Diagrams/ETHAGT07/vector-vs-graph.mmd`
- **Tempo**: 2 min

---

#### Slide 28 — Triplas: Sujeito → Predadado → Objeto
- **Tipo**: Diagrama
- **Objetivo**: Apresentar o modelo de dados fundamental de um KG
- **Conteúdo**:
  - Tripla: (sujeito, predicado, objeto)
  - Exemplo: ("Dipirona", "interage_com", "Warfarin")
  - Exemplo: ("Dr. Silva", "prescreveu", "Dipirona")
  - Exemplo: ("Paciente X", "consultou", "Dr. Silva")
  - Encadeamento: Paciente X → Dr. Silva → Dipirona → Warfarin (multi-hop!)
- **Diagrama**: 3 nós conectados por arestas rotuladas
- **Animação**: Triplas aparecem uma a uma, depois o encadeamento
- **Tempo**: 2 min

---

#### Slide 29 — Propriedades e Labels
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar que nós e arestas podem ter propriedades
- **Conteúdo**:
  - Nó: label (tipo) + propriedades (key-value)
  - Aresta: tipo + propriedades (ex: data, fonte, confiança)
  - Exemplo: Nó "Dipirona" {tipo: "Medicamento", classe: "analgésico"}
  - Exemplo: Aresta "interage_com" {severidade: "moderada", fonte: "FDA"}
  - Labeled Property Graph (LPG) — modelo do Neo4j
- **Diagrama**: Nó e aresta com propriedades expandidas
- **Tempo**: 1.5 min

---

#### Slide 30 — Neo4j e Cypher
- **Tipo**: Conteúdo
- **Objetivo**: Introduzir a ferramenta dominante e sua linguagem
- **Conteúdo**:
  - Neo4j: graph database nativa (Labeled Property Graph)
  - Cypher: linguagem declarativa para grafos (como SQL para relacional)
  - Alternativas: Memgraph (in-memory, mais rápido), ArangoDB (multi-modelo)
  - RDF/SPARQL: outro paradigma (W3C, mais acadêmico)
  - Foco do curso: Neo4j + Cypher (ecossistema, maturidade)
- **Diagrama**: Logos Neo4j, Memgraph, ArangoDB
- **Tempo**: 1 min

---

#### Slide 31 — Query Cypher: Exemplo
- **Tipo**: Código
- **Objetivo**: Mostrar Cypher na prática
- **Conteúdo**:
  - "Encontre co-autores de X"
  - Snippet:
    ```cypher
    MATCH (a:Author {name: "X"})-[:WROTE]->(p:Paper)<-[:WROTE]-(b:Author)
    WHERE b <> a
    RETURN DISTINCT b.name AS coauthor, count(p) AS papers
    ORDER BY papers DESC
    LIMIT 10
    ```
  - Padrão visual: nós entre parênteses, arestas entre colchetes
  - Analogia: MATCH = SELECT, mas com travessia de grafo
- **Diagrama**: Query + grafo visual resultante lado a lado
- **Animação**: Query aparece, depois grafo resulta
- **Tempo**: 2 min

---

#### Slide 32 — Modelagem para Raciocínio
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar que a modelagem do grafo determina o que é possível raciocinar
- **Conteúdo**:
  - Modelagem ingênua: nós genéricos, arestas vagas → queries fracas
  - Modelagem rica: labels específicos, relações tipadas, propriedades → raciocínio multi-hop
  - Pergunta de modelagem: "Quais perguntas o agente precisa responder?"
  - Anti-pattern: modelar tudo como "RELATED_TO"
  - Princípio: o grafo é o schema do raciocínio
- **Diagrama**: Grafo mal modelado vs bem modelado
- **Tempo**: 2 min

---

#### Slide 33 — Extração de Entidades com LLM (NER)
- **Tipo**: Diagrama
- **Objetivo**: Mostrar como construir um KG a partir de texto não-estruturado
- **Conteúdo**:
  - Texto → LLM com prompt de NER → entidades estruturadas
  - Prompt: "Extraia todas as entidades do texto com tipo e propriedades"
  - Output: `[{"name": "Dipirona", "type": "Medicamento"}, ...]`
  - Desafio: entidades ambíguas, resolução de coreferência
  - Ferramentas: LangChain LLMGraphTransformer, GLiNER, spaCy
- **Diagrama**: Pipeline: Texto → LLM → Entidades → Nós do grafo
- **Tempo**: 2 min

---

#### Slide 34 — Extração de Relações com LLM
- **Tipo**: Diagrama
- **Objetivo**: Mostrar a etapa de extração de relações
- **Conteúdo**:
  - Dadas 2 entidades → LLM classifica a relação
  - Prompt: "Qual a relação entre A e B? Escolha: [interage_com, prescreveu, ...]"
  - Output: triplas (sujeito, predicado, objeto)
  - Desafio: alucinação de relações inexistentes
  - Mitigação: schema restrito + validação + confiança na aresta
- **Diagrama**: Pipeline: Entidades → LLM → Triplas → Arestas do grafo
- **Tempo**: 1.5 min

---

#### Slide 35 — Inferência no Grafo
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar que grafos permitem raciocínio além do que está explícito
- **Conteúdo**:
  - Explícito: "A interage com B" e "B interage com C"
  - Inferido: "A pode interagir com C" (via transitividade — com cautela)
  - Cypher: pathfinding (shortestPath, allShortestPaths)
  - Pergunta multi-hop: "Todos os medicamentos que o paciente X toma indiretamente"
  - LLM + grafo: LLM formula a query Cypher, grafo executa, LLM interpreta
- **Diagrama**: Grafo com path destacado (A → B → C)
- **Tempo**: 2 min

---

#### Slide 36 — Pergunta: Cardinalidade de um KG Empresarial
- **Tipo**: Exercício
- **Objetivo**: Engajar a turma com uma pergunta de modelagem
- **Conteúdo**:
  - "Qual a cardinalidade típica de um KG empresarial? Quantas relações por entidade?"
  - Pistas: depende do domínio (farmacêutica vs jurídico vs RH)
  - Ordem de magnitude: 10k-100k entidades, 50k-500k relações
  - Densidade: 5-15 relações por entidade (em média)
  - Discussão em duplas (2 min)
- **Diagrama**: Caixa de discussão
- **Tempo**: 2 min

---

### SEÇÃO E — GraphRAG (Slides 37-51 · 15 min)

---

#### Slide 37 — [SEÇÃO] GraphRAG
- **Tipo**: Seção
- **Objetivo**: Transição para o bloco de GraphRAG
- **Conteúdo**: Número "4" grande + "GraphRAG"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 38 — Por Que GraphRAG?
- **Tipo**: Conteúdo
- **Objetivo**: Explicar a lacuna que GraphRAG preenche
- **Conteúdo**:
  - Vector RAG: recupera chunks isolados — perde visão global
  - Problema: "Quais são os temas principais deste corpus de 1000 docs?"
  - Vector RAG: não consegue responder (precisa de todos os chunks)
  - GraphRAG: constrói grafo de entidades + comunidades → síntese global
  - Multi-hop: vector RAG falha em perguntas que exigem encadear 3+ hops
- **Diagrama**: Vector RAG (chunks isolados) vs GraphRAG (grafo + comunidades)
- **Tempo**: 2 min

---

#### Slide 39 — Microsoft GraphRAG: Visão Geral
- **Tipo**: Diagrama
- **Objetivo**: Apresentar a arquitetura do GraphRAG da Microsoft
- **Conteúdo**:
  - Pipeline de construção:
    1. Text chunking
    2. Extração de entidades + relações (LLM)
    3. Construção do grafo
    4. Detecção de comunidades (Leiden algorithm)
    5. Sumarização hierárquica de comunidades (LLM)
  - Pipeline de query:
    - Local search: entidades relevantes + vizinhança
    - Global search: map-reduce sobre sumários de comunidades
  - Fonte: Edge et al., arXiv:2404.16130
- **Diagrama**: `12-Diagrams/ETHAGT07/graphrag-pipeline.mmd`
- **Animação**: Pipeline aparece etapa por etapa
- **Tempo**: 3 min

---

#### Slide 40 — Construção do Grafo de Comunidades
- **Tipo**: Diagrama
- **Objetivo**: Aprofundar a etapa de community detection
- **Conteúdo**:
  - Grafo de entidades → algoritmo Leiden → comunidades
  - Comunidade: grupo de entidades densamente conectadas entre si
  - Hierarquia: comunidades grandes contêm subcomunidades
  - Análogo a "capítulos de um livro" — estrutura temática emergente
  - Resultado: grafo particionado em níveis hierárquicos
- **Diagrama**: Grafo colorido por comunidade (ex: 5 cores)
- **Tempo**: 2 min

---

#### Slide 41 — Sumarização Hierárquica
- **Tipo**: Conteúdo
- **Objetivo**: Explicar como comunidades viram sumários
- **Conteúdo**:
  - Para cada comunidade (no nível mais baixo): LLM gera sumário
  - Sumários de subcomunidades → LLM gera sumário da comunidade pai
  - Resultado: árvore de sumários do específico ao geral
  - Vantagem: responde perguntas globais sem ler todos os chunks
  - Custo: uma chamada de LLM por comunidade (caro na construção)
- **Diagrama**: Árvore de sumários (folhas → raiz)
- **Tempo**: 1.5 min

---

#### Slide 42 — Local Search
- **Tipo**: Diagrama
- **Objetivo**: Apresentar o modo Local do GraphRAG
- **Conteúdo**:
  - Input: pergunta do usuário
  - Passo 1: identificar entidades relevantes na pergunta (LLM)
  - Passo 2: expandir vizinhança no grafo (entidades + relações + chunks associados)
  - Passo 3: LLM gera resposta com o contexto local
  - Melhor para: perguntas específicas sobre entidades conhecidas
  - Exemplo: "Quem são os co-autores de X?"
- **Diagrama**: Grafo com subgrafo local destacado
- **Tempo**: 1.5 min

---

#### Slide 43 — Global Search
- **Tipo**: Diagrama
- **Objetivo**: Apresentar o modo Global do GraphRAG
- **Conteúdo**:
  - Input: pergunta ampla ("Quais temas principais do corpus?")
  - Map: para cada comunidade (nível escolhido), LLM gera resposta parcial
  - Reduce: LLM agrega respostas parciais em resposta final
  - Melhor para: perguntas que exigem visão holística
  - Exemplo: "Quais as tendências de pesquisa nesta área?"
- **Diagrama**: Map-reduce sobre comunidades
- **Tempo**: 1.5 min

---

#### Slide 44 — Local vs Global: Quando Cada
- **Tipo**: Comparação
- **Objetivo**: Dar critério prático de escolha
- **Conteúdo**:
  - Local: pergunta menciona entidades específicas → foco no subgrafo
  - Global: pergunta é temática/ampla → síntese entre comunidades
  - Híbrido: começa local, escala para global se insuficiente
  - Heurística: "Esta pergunta precisa de 1 entidade ou de todo o corpus?"
- **Diagrama**: Tabela comparativa Local vs Global
- **Tempo**: 1 min

---

#### Slide 45 — GraphRAG vs Vector RAG
- **Tipo**: Comparação
- **Objetivo**: Sistematizar quando GraphRAG supera vector RAG
- **Conteúdo**:
  - Vector RAG melhor: lookup factual, pergunta de um hop, latência baixa
  - GraphRAG melhor: multi-hop, raciocínio sobre relacionamentos, visão global
  - Custo: GraphRAG é 10-100x mais caro na construção
  - Latência: Global search é mais lento (map-reduce)
  - Regra: GraphRAG quando o valor do raciocínio justifica o custo
- **Diagrama**: Tabela: Vector RAG vs GraphRAG (critérios, custo, latência, recall)
- **Tempo**: 2 min

---

#### Slide 46 — DEMO: GraphRAG em Neo4j
- **Tipo**: Código
- **Objetivo**: Demo ao vivo — construir KG e responder pergunta multi-hop
- **Conteúdo**:
  - Referência: `05-Labs/ETHAGT07/Lab2-GraphRAG-Neo4j`
  - Passo 1: carregar corpus técnico
  - Passo 2: extrair entidades/relações com LLM
  - Passo 3: construir grafo no Neo4j
  - Passo 4: query Cypher multi-hop
  - Mostrar: vector RAG falha na mesma pergunta, GraphRAG acerta
- **Diagrama**: Terminal + Neo4j Browser lado a lado
- **Animação**: Passos aparecem sequencialmente
- **Tempo**: 3 min

---

#### Slide 47 — Pergunta da DEMO
- **Tipo**: Exercício
- **Objetivo**: Engajar a turma com uma pergunta sobre a demo
- **Conteúdo**:
  - "O GraphRAG errou alguma coisa na demo? Onde?"
  - "Qual o custo aproximado da construção do grafo (em tokens)?"
  - "Se o corpus mudar (novos docs), quanto custa reindexar?"
  - Discussão em duplas (2 min)
- **Diagrama**: Caixa de discussão
- **Tempo**: 2 min

---

#### Slide 48 — Custos de Construção
- **Tipo**: Conteúdo
- **Objetivo**: Ser transparente sobre o custo de construir GraphRAG
- **Conteúdo**:
  - Extração de entidades: 1 chamada LLM por chunk
  - Extração de relações: 1 chamada LLM por par de entidades
  - Sumarização de comunidades: 1 chamada LLM por comunidade
  - Ordem de magnitude: 1000 docs → ~5k-15k chamadas LLM
  - Custo estimado: $50-$500 dependendo do modelo
  - Pergunta: *Por que GraphRAG é caro? Justifique o custo.*
- **Diagrama**: Breakdown de custo por etapa (bar chart)
- **Tempo**: 1.5 min

---

#### Slide 49 — Custos de Manutenção
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar que GraphRAG tem custo recorrente, não só inicial
- **Conteúdo**:
  - Novos documentos: extrair entidades/relações + atualizar comunidades
  - Atualização incremental: mais barato que reconstrução total, mas complexo
  - Drift de entidades: mesma entidade com nomes diferentes → merge
  - Comunidades podem mudar: re-sumarização necessária
  - Lineage: rastrear qual documento originou qual tripla
- **Diagrama**: Ciclo de manutenção (add docs → extract → update graph → re-summarize)
- **Tempo**: 1 min

---

#### Slide 50 — Pergunta: Vale a Pena?
- **Tipo**: Exercício
- **Objetivo**: Estimular pensamento crítico sobre ROI
- **Conteúdo**:
  - "Para qual domínio GraphRAG vale o custo de construção?"
  - "E para qual domínio é overkill?"
  - Critério: valor do raciocínio multi-hop vs custo de manutenção
  - Exemplos: farmacêutica (vale), jurídico (vale), blog pessoal (não vale)
- **Diagrama**: Matriz 2x2 (valor do raciocínio vs custo)
- **Tempo**: 1.5 min

---

#### Slide 51 — Recap: Vector vs Graph vs GraphRAG
- **Tipo**: Resumo
- **Objetivo**: Sintetizar as 3 abordagens antes de avançar para híbridos
- **Conteúdo**:
  - Vector DB: similaridade semântica, barato, rápido
  - Knowledge Graph: relacionamentos estruturados, modelagem cara, raciocínio multi-hop
  - GraphRAG: KG + sumarização de comunidades, caro na construção, responde perguntas globais
  - Próximo: combinar vector + grafo em pipeline híbrido
- **Diagrama**: 3 colunas comparativas
- **Tempo**: 1 min

---

### SEÇÃO F — Pipelines Híbridos (Slides 52-62 · 12 min)

---

#### Slide 52 — [SEÇÃO] Pipelines Híbridos
- **Tipo**: Seção
- **Objetivo**: Transição para a combinação de vector + grafo
- **Conteúdo**: Número "5" grande + "Pipelines Híbridos"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 53 — Vector + Grafo: Por Que Combinar?
- **Tipo**: Conteúdo
- **Objetivo**: Justificar a combinação
- **Conteúdo**:
  - Vector: bom em "encontrar documentos sobre X"
  - Grafo: bom em "encontrar entidades relacionadas a X"
  - Híbrido: "encontrar documentos sobre entidades relacionadas a X"
  - Exemplo: "Artigos sobre medicamentos que interagem com o que o paciente X toma"
  - Vector sozinho: não sabe interações. Grafo sozinho: não tem texto dos artigos.
- **Diagrama**: Venn diagram (vector ∩ graph = híbrido)
- **Tempo**: 1.5 min

---

#### Slide 54 — Arquitetura Híbrida
- **Tipo**: Diagrama
- **Objetivo**: Apresentar a arquitetura canônica de retrieval híbrido
- **Conteúdo**:
  - Componentes:
    1. Ingestão: texto → embeddings (vector DB) + entidades/relações (grafo)
    2. Query: pergunta → vector search + graph traversal
    3. Fusão: combinar resultados (RAG com contexto do grafo)
    4. Geração: LLM com chunks + subgrafo como contexto
  - Sync: vector DB e grafo devem referenciar os mesmos documentos
- **Diagrama**: `12-Diagrams/ETHAGT07/hybrid-retrieval.mmd`
- **Tempo**: 2 min

---

#### Slide 55 — RetrievalAgent: Escolhendo Estratégia
- **Tipo**: Diagrama
- **Objetivo**: Mostrar que o agente decide qual estratégia de retrieval usar
- **Conteúdo**:
  - Nem toda pergunta precisa de grafo
  - RetrievalAgent classifica a pergunta:
    - "O que é X?" → vector search (simples)
    - "Quem está conectado a X?" → graph traversal
    - "Documentos sobre entidades relacionadas a X?" → híbrido
  - Implementação: LLM como router (classifica intenção da pergunta)
  - Alternativa: sempre híbrido e deixar o LLM filtrar (mais caro, mais simples)
- **Diagrama**: Router: pergunta → {vector | graph | híbrido} → resultado
- **Tempo**: 2 min

---

#### Slide 56 — Implementação do Router
- **Tipo**: Código
- **Objetivo**: Mostrar código real do router
- **Conteúdo**:
  - Snippet:
    ```python
    def retrieve(question: str) -> list[Document]:
        strategy = classify_strategy(question)
        if strategy == "vector":
            return vector_search(question)
        elif strategy == "graph":
            return graph_traverse(question)
        else:  # híbrido
            entities = extract_entities(question)
            related = graph.find_related(entities)
            return vector_search(question, filter=related)
    ```
  - `classify_strategy`: LLM com prompt simples ("vector/graph/hybrid?")
  - Trade-off: router adiciona 1 chamada LLM, mas economiza retrieval desnecessário
- **Diagrama**: Code block com syntax highlighting
- **Tempo**: 2 min

---

#### Slide 57 — Manutenção: Incremental Update
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar como manter o pipeline híbrido atualizado
- **Conteúdo**:
  - Novo documento chega → 2 pipelines disparam:
    1. Embedding → insert no vector DB
    2. Extração de entidades/relações → insert/update no grafo
  - Sync: ambos devem referenciar o mesmo doc_id
  - Desafio: se extração falha, grafo fica incompleto (vector tem, grafo não)
  - Solução: retry queue + reconciliation job
- **Diagrama**: Pipeline de ingestão dual (vector + graph)
- **Tempo**: 1.5 min

---

#### Slide 58 — Lineage e Provenance
- **Tipo**: Conteúdo
- **Objetivo**: Explicar rastreabilidade no pipeline híbrido
- **Conteúdo**:
  - Lineage: qual documento originou qual tripla do grafo
  - Provenance: qual tripla originou qual parte da resposta
  - Implementação: `doc_id` como propriedade em nós e arestas
  - Valor: debugging ("por que o agente disse isso?"), auditoria, correção
  - Sem lineage: grafo é caixa preta — impossível explicar respostas
- **Diagrama**: Resposta → tripla → documento (chain of provenance)
- **Tempo**: 1 min

---

#### Slide 59 — Caso: Base de Conhecimento Técnica
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar o caso de estudo do projeto do módulo
- **Conteúdo**:
  - Corpus: documentação técnica + issues + changelogs
  - Vector DB: busca por "como fazer X"
  - Grafo: "X depende de Y", "X substituiu Z", "X foi introduzido na v2.3"
  - Híbrido: "documentação sobre features que dependem de X"
  - Agente: escolhe estratégia e justifica a escolha
- **Diagrama: Diagrama do caso (corpus → pipeline híbrido → agente)
- **Tempo**: 1.5 min

---

#### Slide 60 — Exercício: Vector, Graph, ou Híbrido?
- **Tipo**: Exercício
- **Objetivo**: Praticar a decisão em cenários reais
- **Conteúdo**:
  - 5 cenários:
    1. Catálogo de produtos com busca por similaridade → Vector
    2. Base de conhecimento médica com relações entre doenças e tratamentos → Graph (ou híbrido)
    3. Documentos jurídicos com referências cruzadas → Híbrido
    4. Chatbot de RH com perguntas sobre políticas → Vector (ou híbrido)
    5. Sistema de recomendação de filmes → Híbrido (ou graph)
  - Em grupos: vector, graph, ou híbrido? Justificar.
- **Diagrama**: 5 cards com cenários
- **Tempo**: 2 min

---

#### Slide 61 — Pergunta: Sempre Híbrido?
- **Tipo**: Exercício
- **Objetivo**: Combater o reflexo de "mais complexo = melhor"
- **Conteúdo**:
  - Verdadeiro/falso: "Sempre preferir híbrido."
  - Resposta: Falso — híbrido adiciona complexidade e custo
  - Híbrido só quando: vector sozinho falha E o valor justifica o custo
  - Anti-pattern: "vamos fazer híbrido por precaução" → over-engineering
  - Regra: comece com vector, adicione grafo com evidência de gap
- **Diagrama**: Escada de complexidade (vector → graph → híbrido → GraphRAG)
- **Tempo**: 1 min

---

#### Slide 62 — Benchmark: Vector vs Grafo vs Híbrido
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar resultados reais de comparação
- **Conteúdo**:
  - Dataset: corpus técnico com perguntas multi-hop
  - Métricas: success rate, latência p50/p99, custo por query
  - Resultado típico:
    - Vector: 60% success, 200ms, $0.01/query
    - Graph: 75% success, 400ms, $0.02/query
    - Híbrido: 85% success, 500ms, $0.03/query
  - Híbrido melhora success rate em casos multi-hop sem explodir custo
  - Critério de sucesso do projeto
- **Diagrama**: Gráfico de barras (success rate) + tabela (latência/custo)
- **Tempo**: 1 min

---

### SEÇÃO G — Operação em Escala (Slides 63-70 · 8 min)

---

#### Slide 63 — [SEÇÃO] Operação em Escala
- **Tipo**: Seção
- **Objetivo**: Transição para tópicos de produção
- **Conteúdo**: Número "6" grande + "Operação em Escala"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 64 — Sharding e Replicação
- **Tipo**: Conteúdo
- **Objetivo**: Explicar como vector DBs escalam horizontalmente
- **Conteúdo**:
  - Sharding: dividir vetores em partições (por hash ou range)
  - Replicação: cópias para disponibilidade e leitura paralela
  - Qdrant: sharding por collection, replicação configurável
  - Milvus: arquitetura distribuída nativa (QueryNode, DataNode, Proxy)
  - Trade-off: mais shards = mais paralelismo, mas mais coordenação
- **Diagrama**: Cluster com shards e réplicas
- **Tempo**: 1.5 min

---

#### Slide 65 — Consistência
- **Tipo**: Conteúdo
- **Objetivo**: Discutir modelos de consistência em vector DBs
- **Conteúdo**:
  - Strong: toda leitura vê o último write (mais caro)
  - Eventual: leituras podem ver dados stale (mais rápido)
  - Bounded staleness: stale por no máximo T segundos
  - Qdrant: configurável por collection
  - Para RAG: eventual costuma bastar (embeddings não mudam a cada segundo)
- **Diagrama**: Espectro strong ←→ eventual
- **Tempo**: 1 min

---

#### Slide 66 — Reindexação e Drift de Embeddings
- **Tipo**: Conteúdo
- **Objetivo**: Explicar o problema de trocar modelo de embedding
- **Conteúdo**:
  - Modelo de embedding novo → vetores antigos são incompatíveis
  - Reindexação total: re-embeddar todos os documentos (caro, demorado)
  - Estratégias:
    - Dual index: manter novo e velho durante transição
    - Zero-downtime reindex: construir novo index em background, swap quando pronto
  - Drift: se documentos mudam, embeddings antigos perdem relevância
  - Frequência de reindex: depende da volatilidade do corpus
- **Diagrama**: Timeline de reindexação (dual index → swap)
- **Tempo**: 2 min

---

#### Slide 67 — Custo de Armazenamento (Quantização)
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar como reduzir custo de memória
- **Conteúdo**:
  - Vetor de 1536 dims em float32 = 6 KB por vetor
  - 100M vetores = 600 GB (só vetores, sem index)
  - Quantização:
    - float32 → float16: 50% redução, perda mínima
    - Product Quantization (PQ): 90%+ redução, perda moderada
    - Binary quantization: 97% redução, perda maior
  - Qdrant: suporta quantização com re-scoring (busca rápida + re-rank preciso)
- **Diagrama**: Tabela de trade-off (precisão vs tamanho)
- **Tempo**: 1.5 min

---

#### Slide 68 — Observabilidade
- **Tipo**: Conteúdo
- **Objetivo**: Definir métricas mínimas para operar vector DBs em produção
- **Conteúdo**:
  - Latência de query: p50, p95, p99
  - Recall@k: verdadeiros vizinhos vs retornados (amostragem)
  - Cache hit rate: queries repetidas ( economiza ANN)
  - Index size vs collection size
  - Throughput: queries por segundo
  - Alertas: p99 > threshold, recall < threshold, index desatualizado
- **Diagrama**: Dashboard com métricas
- **Tempo**: 1.5 min

---

### SEÇÃO H — Fechamento (Slides 69-80 · 10 min)

---

#### Slide 69 — [SEÇÃO] Boas Práticas e Anti-Patterns
- **Tipo**: Seção
- **Objetivo**: Transição para o fechamento
- **Conteúdo**: "7 — Boas Práticas e Anti-Patterns"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 70 — Boas Práticas (DO)
- **Tipo**: Conteúdo
- **Objetivo**: Checklist de boas práticas
- **Conteúdo**:
  - Comece com vector DB, adicione grafo com evidência de gap
  - Normalize embeddings se usar cosine (vira dot, mais rápido)
  - Defina schema de entidades/relações antes de extrair
  - Valide triplas extraídas por LLM (confiança + amostragem)
  - Mantenha lineage: doc_id em cada nó e aresta
  - Monitore recall@k em produção (não só latência)
  - Reindexação planejada quando trocar modelo de embedding
  - Híbrido só quando success rate do vector é insuficiente
- **Diagrama**: Checklist verde (etho-success)
- **Tempo**: 2 min

---

#### Slide 71 — Anti-Patterns (DON'T)
- **Tipo**: Conteúdo
- **Objetivo**: Checklist do que NÃO fazer
- **Conteúdo**:
  - Começar com GraphRAG quando vector RAG basta
  - Misturar métricas entre index e query
  - Modelar grafo com "RELATED_TO" genérico em tudo
  - Confiar cegamente em triplas extraídas por LLM (alucinação)
  - Sem lineage — impossível debugar respostas erradas
  - Não monitorar recall (latência boa ≠ qualidade boa)
  - Reindexar em horário de pico sem dual index
  - Adicionar vector DB quando Postgres já resolve
  - Híbrido "por precaução" sem evidência de gap
- **Diagrama**: Checklist vermelho (etho-danger)
- **Tempo**: 2 min

---

#### Slide 72 — Caso de Estudo: GraphRAG em Farmacêutica
- **Tipo**: Diagrama
- **Objetivo**: Mostrar todos os conceitos em um caso real
- **Conteúdo**:
  - Domínio: interações medicamentosas em base farmacêutica
  - Corpus: 50k documentos (bulas, papers, guidelines)
  - Vector DB: busca por "documentos sobre efeito colateral X"
  - Grafo: medicamento → interage_com → medicamento → contraindicado_para → condição
  - GraphRAG: comunidades de medicamentos relacionados → visão de classes terapêuticas
  - Resultado: multi-hop "paciente com condição X + medicação Y → risco?"
  - Custo: ~$200 de construção, justificado por valor clínico
- **Diagrama**: Arquitetura do caso (corpus → vector + graph → GraphRAG → resposta)
- **Tempo**: 2 min

---

#### Slide 73 — Resumo da Aula
- **Tipo**: Resumo
- **Objetivo**: Sintetizar os pontos-chave
- **Conteúdo**:
  - Vector DB: similaridade semântica via ANN (HNSW/IVF), métricas, filtering
  - 5 vector DBs com trade-offs distintos (Qdrant, Milvus, Weaviate, Chroma, pgvector)
  - Knowledge Graph: triplas, propriedades, raciocínio multi-hop via Cypher
  - GraphRAG: comunidades + sumarização hierárquica → local vs global
  - Híbrido: vector + grafo, RetrievalAgent escolhe estratégia
  - Escala: sharding, reindexação, quantização, observabilidade
  - Regra: comece simples (vector), adicione complexidade com evidência
- **Diagrama**: 7 ícones com os pontos-chave
- **Tempo**: 2 min

---

#### Slide 74 — Checklist da Aula
- **Tipo**: Resumo
- **Objetivo**: Confirmar que todos os tópicos foram cobertos
- **Conteúdo**:
  - [ ] Explicou ANN (HNSW, IVF) e métricas
  - [ ] Comparou 5 vector DBs por cenário
  - [ ] Modelou knowledge graph com triplas e Cypher
  - [ ] Apresentou GraphRAG (local + global)
  - [ ] Construiu pipeline híbrido com router
  - [ ] Discutiu escala, reindexação e observabilidade
- **Diagrama**: Checklist visual
- **Tempo**: 1 min

---

#### Slide 75 — Quiz: Pergunta 1
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "Qual métrica de similaridade é equivalente a dot product quando os embeddings estão normalizados?"
  - A) Euclidean
  - B) Cosine
  - C) Manhattan
  - D) Jaccard
  - Resposta: B
- **Tempo**: 1 min

---

#### Slide 76 — Quiz: Pergunta 2
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "Quando GraphRAG supera vector RAG de forma mais clara?"
  - A) Quando a pergunta é sobre um fato específico em um documento
  - B) Quando a pergunta exige raciocínio multi-hop entre entidades
  - C) Quando a latência é o requisito mais importante
  - D) Quando o corpus é pequeno (< 100 documentos)
  - Resposta: B
- **Tempo**: 1 min

---

#### Slide 77 — Quiz: Pergunta 3
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "Em um pipeline híbrido, o que o RetrievalAgent faz?"
  - A) Sempre faz busca vetorial e grafo em paralelo
  - B) Classifica a pergunta para escolher vector, graph ou híbrido
  - C) Substitui o vector DB por um grafo
  - D) Gera embeddings para o grafo
  - Resposta: B
- **Tempo**: 1 min

---

#### Slide 78 — Conexão com Próximos Módulos
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar como ETHAGT07 conecta com o resto da especialização
- **Conteúdo**:
  - ETHAGT14 — Escalabilidade: vector DBs em produção multi-tenant
  - ETHAGT90 — Capstone: integra vector + grafo no projeto final
  - ETHAGT05 — Memória: vector DB como memória semântica de agentes
  - ETHAGT12 — AgentOps: observabilidade de pipelines híbridos
- **Diagrama**: Mapa da especialização com ETHAGT07 no centro
- **Tempo**: 1 min

---

#### Slide 79 — Leitura Recomendada e Referências
- **Tipo**: Referências
- **Objetivo**: Indicar o que ler e listar fontes
- **Conteúdo**:
  - Obrigatório: Edge, D. et al. *GraphRAG: From Local to Global* (Microsoft, arXiv:2404.16130)
  - Obrigatório: Lewis, P. et al. *RAG* (arXiv:2005.11401)
  - Recomendado: Pan, S. et al. *Unifying Large Language Models and Knowledge Graphs* (arXiv:2306.08302)
  - Documentação: Qdrant, Milvus, Weaviate, Neo4j, pgvector
  - Próxima aula: ETHAGT14 — Escalabilidade
- **Tempo**: 1 min

---

#### Slide 80 — Q&A / Encerramento
- **Tipo**: Capa
- **Objetivo**: Abrir para perguntas e encerrar
- **Conteúdo**:
  - "Perguntas?"
  - Contato do professor
  - "Na próxima aula: ETHAGT14 — Escalabilidade"
  - Lembrete: iniciar Lab 1 (Vector DB Bake-off)
- **Diagrama**: Logo Etho + fundo etho-dark
- **Tempo**: 2 min

---

## Resumo do Storyboard

| Seção | Slides | Tempo | Conteúdo |
|---|---|---|---|
| A — Abertura | 1-6 | 8 min | Capa, objetivos, competências, agenda, motivação, contexto |
| B — Vector DBs | 7-16 | 12 min | ANN, HNSW, IVF, métricas, filtering, sparse+dense |
| C — Comparativo | 17-25 | 10 min | Qdrant, Milvus, Weaviate, Chroma, pgvector, quando NÃO usar |
| D — Knowledge Graphs | 26-36 | 15 min | Triplas, Neo4j, Cypher, modelagem, extração, inferência |
| E — GraphRAG | 37-51 | 15 min | Microsoft GraphRAG, local vs global, DEMO, custos |
| F — Híbridos | 52-62 | 12 min | Vector+grafo, RetrievalAgent, manutenção, benchmark |
| G — Escala | 63-68 | 8 min | Sharding, consistência, reindexação, quantização, observabilidade |
| H — Fechamento | 69-80 | 10 min | Boas práticas, anti-patterns, caso, resumo, quiz, referências, Q&A |
| **Total** | **80** | **90 min** | |

---

## Diagramas Necessários

| # | Slide | Diagrama | Tipo | Fonte |
|---|---|---|---|---|
| D1 | 8 | Arquitetura de vector DB | Flowchart | Novo |
| D2 | 9 | Embeddings → espaço vetorial | Visualização | Novo |
| D3 | 10 | Curva recall vs latência | Gráfico | Novo |
| D4 | 11 | Estrutura hierárquica HNSW | Flowchart | arXiv:1603.09320 |
| D5 | 12 | Células de Voronoi (IVF) | Visualização | Novo |
| D6 | 13 | Métricas: cosine, dot, euclidean | 3 painéis | Novo |
| D7 | 14 | Árvore de decisão de métrica | Fluxograma | Novo |
| D8 | 15 | Pre-filter vs post-filter | Comparação | Novo |
| D9 | 16 | Sparse + Dense → RRF | Sequência | Novo |
| D10 | 18 | Landscape de 5 vector DBs | Grid 2x3 | Novo |
| D11 | 24 | Tabela comparativa (heat map) | Tabela | Novo |
| D12 | 25 | Árvore "preciso de vector DB?" | Fluxograma | Novo |
| D13 | 27 | Vector vs Graph | Comparação | `12-Diagrams/ETHAGT07/vector-vs-graph.mmd` |
| D14 | 28 | Triplas (sujeito → predicado → objeto) | Grafo | Novo |
| D15 | 29 | Nó e aresta com propriedades | Diagrama | Novo |
| D16 | 31 | Query Cypher + grafo resultante | Código + Grafo | Novo |
| D17 | 32 | Grafo mal modelado vs bem modelado | Comparação | Novo |
| D18 | 33 | Pipeline NER (texto → LLM → entidades) | Sequência | Novo |
| D19 | 34 | Pipeline extração de relações | Sequência | Novo |
| D20 | 35 | Path highlighting no grafo | Grafo | Novo |
| D21 | 38 | Vector RAG vs GraphRAG | Comparação | Novo |
| D22 | 39 | GraphRAG pipeline | Flowchart | `12-Diagrams/ETHAGT07/graphrag-pipeline.mmd` |
| D23 | 40 | Grafo colorido por comunidade (Leiden) | Grafo | Novo |
| D24 | 41 | Árvore de sumários hierárquicos | Árvore | Novo |
| D25 | 42 | Local search (subgrafo local) | Grafo | Novo |
| D26 | 43 | Global search (map-reduce) | Fluxograma | Novo |
| D27 | 44 | Tabela Local vs Global | Tabela | Novo |
| D28 | 45 | Vector RAG vs GraphRAG (tabela) | Tabela | Novo |
| D29 | 48 | Breakdown de custo por etapa | Bar chart | Novo |
| D30 | 49 | Ciclo de manutenção | Ciclo | Novo |
| D31 | 50 | Matriz valor vs custo | Matriz 2x2 | Novo |
| D32 | 51 | Vector vs Graph vs GraphRAG (3 colunas) | Comparação | Novo |
| D33 | 53 | Venn diagram (vector ∩ graph) | Venn | Novo |
| D34 | 54 | Arquitetura híbrida | Flowchart | `12-Diagrams/ETHAGT07/hybrid-retrieval.mmd` |
| D35 | 55 | RetrievalAgent router | Fluxograma | Novo |
| D36 | 57 | Pipeline de ingestão dual | Sequência | Novo |
| D37 | 58 | Chain of provenance | Sequência | Novo |
| D38 | 59 | Caso: base de conhecimento técnica | Flowchart | Novo |
| D39 | 61 | Escada de complexidade | Escada | Novo |
| D40 | 62 | Benchmark (barras + tabela) | Gráfico | Novo |
| D41 | 64 | Cluster com shards e réplicas | Diagrama | Novo |
| D42 | 66 | Timeline de reindexação (dual index) | Timeline | Novo |
| D43 | 67 | Tabela quantização (precisão vs tamanho) | Tabela | Novo |
| D44 | 68 | Dashboard de observabilidade | Dashboard | Novo |
| D45 | 72 | Caso GraphRAG farmacêutica | Flowchart | `09-CaseStudies/` (referência) |
| D46 | 78 | Mapa da especialização | Mind map | Novo |

---

## Pontos de Engajamento

| # | Slide | Tipo | Pergunta / Atividade | Tempo |
|---|---|---|---|---|
| E1 | 5 | Reflexão | *Quando uma busca por similaridade não é suficiente?* | 1 min |
| E2 | 14 | Pergunta técnica | *Cosine vs dot — quando a diferença importa?* | 1 min |
| E3 | 24 | Discussão | *Para um MVP, qual escolher? E para 1M de usuários?* | 2 min |
| E4 | 36 | Exercício | *Qual a cardinalidade típica de um KG empresarial?* | 2 min |
| E5 | 46 | DEMO | GraphRAG em Neo4j ao vivo | 3 min |
| E6 | 47 | Pergunta da DEMO | *O GraphRAG errou algo? Qual o custo em tokens?* | 2 min |
| E7 | 48 | Pergunta | *Por que GraphRAG é caro? Justifique o custo.* | 1 min |
| E8 | 50 | Discussão | *Para qual domínio GraphRAG vale? E qual é overkill?* | 1.5 min |
| E9 | 60 | Exercício em grupo | 5 cenários: vector, graph, ou híbrido? | 2 min |
| E10 | 61 | Verdadeiro/falso | *Sempre preferir híbrido.* | 1 min |
| E11 | 75-77 | Quiz | 3 perguntas de verificação | 3 min |

---

## Pendências de Produção

- [ ] Produzir 43 diagramas novos (D1-D12, D14-D32, D35-D46)
- [ ] Confirmar 3 diagramas existentes (D13, D22, D34) em `12-Diagrams/ETHAGT07/`
- [ ] Screenshot do Neo4j Browser para DEMO (Slide 46)
- [ ] Screenshot de código com syntax highlighting (Slides 31, 56)
- [ ] Imagem de fundo para capa (Slide 1) — rede de nós + vetores
- [ ] Badge de competências (Slide 3)
- [ ] Timeline de evolução do RAG (Slide 6)
- [ ] Gráfico de benchmark vector vs graph vs híbrido (Slide 62)
- [ ] Dashboard de observabilidade mockup (Slide 68)
- [ ] Caso de estudo farmacêutico detalhado (Slide 72) — verificar `09-CaseStudies/`

---

> **Aguardando aprovação deste storyboard para gerar os slides detalhados com notas do professor.**
