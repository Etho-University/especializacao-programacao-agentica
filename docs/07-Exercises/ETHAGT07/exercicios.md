# ETHAGT07 — Lista de Exercícios

> Curso: Knowledge Graphs & Vector Databases para Agentes. Fixação de conceitos. Use a apostila `04-Apostilas/ETHAGT07/apostila.md` como referência.

## Múltipla escolha

**1. No algoritmo HNSW (Hierarchical Navigable Small World), o objetivo é:**

a) Indexar conhecimento em grafos
b) Busca aproximada de vizinhos mais próximos (ANN) com boa relação latência/recall
c) Comprimir embeddings
d) Extrair entidades de texto

**2. Em GraphRAG (Microsoft), a diferença entre Local search e Global search é:**

a) Local é mais barato; Global é mais preciso
b) Local responde sobre entidades específicas e suas vizinhanças; Global sintetiza informações em nível de comunidade/tema
c) Local usa vector DB; Global usa grafo
d) Não há diferença

**3. Quando pgvector é preferível a Qdrant dedicado?**

a) Sempre
b) Quando já se usa PostgreSQL e a escala de vetores é moderada, aproveitando operações ACID e joins com dados relacionais
c) Quando se precisa de máxima performance
d) Nunca

**4. Em um knowledge graph, uma "tripla" representa:**

a) Três vector databases
b) Uma relação (sujeito, predicado, objeto) — ex.: (PessoaX, CO_AUTOR_DE, PessoaY)
c) Três agentes
d) Três chunks de texto

## Verdadeiro ou Falso (justificado)

**1.** "Sempre preferir pipelines híbridos (vector + grafo) em vez de um só." — Justifique.

**2.** "GraphRAG é caro porque exige extração de entidades/relações e construção de comunidades." — Justifique.

**3.** "Metadata filtering em vector DBs (payloads) permite filtrar por atributos sem reprocessar embeddings." — Justifique.

**4.** "Extração de entidades e relações com LLM é determinística — roda duas vezes e dá o mesmo resultado." — Justifique.

## Código curto

**1.** Escreva uma query Cypher que encontra todos os co-autores de um pesquisador X (grafo com nós Person e relação CO_AUTHORED_WITH).

**2.** Escreva o pseudocódigo de um RetrievalAgent que decide entre busca vetorial e busca em grafo com base no tipo de pergunta.

**3.** Escreva o pseudocódigo de uma busca híbrida: combinar resultados de BM25 (sparse) e densa, com fusão por score normalizado.

## Análise de trade-off

**1.** Para 3 cenários (FAQ, rede de co-autores acadêmicos, perguntas factuais simples), vector DB ou knowledge graph?

**2.** Compare GraphRAG (local) vs. vector RAG para uma pergunta multi-hop. Quando GraphRAG supera?

**3.** Compare Qdrant vs. pgvector para uma aplicação multi-tenant com 10M vetores. Que fatores influenciam a escolha?

## Debug / diagnóstico

**1.** Uma busca vetorial retorna resultados semanticamente próximos mas que violam um filtro de tenant (dados de outro cliente aparecem). Diagnóstico e correção.

**2.** Um GraphRAG responde bem a perguntas locais mas falha em perguntas globais ("quais são os temas principais do corpus?"). Diagnóstico provável.
