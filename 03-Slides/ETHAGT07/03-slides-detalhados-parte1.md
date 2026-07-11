# ETHAGT07 — Slides Detalhados + Notas do Professor (Parte 1: Slides 1-36)

> Universidade Etho · Especialização em Programação Agêntica
> Cada slide contém: título, objetivo, conteúdo, notas do professor, diagrama, animação, imagem, tempo.

---

## SEÇÃO A — Abertura (Slides 1-6 · 8 min)

---

### Slide 1 — Capa

**Título**: ETHAGT07 — Knowledge Graphs & Vector Databases para Agentes
**Objetivo**: Identificar a aula, o professor e o contexto dentro da especialização.
**Conteúdo**:
- ETHAGT07 — Knowledge Graphs & Vector Databases para Agentes
- Universidade Etho · Especialização em Programação Agêntica
- Fase B — Infraestrutura Cognitiva · 30 h
- Professor · Data

**Diagrama**: Logo Etho (canto sup. esquerdo) + imagem de fundo abstrata (rede de nós + vetores)
**Animação**: Fade in do título (300ms)
**Imagem**: Fundo `etho-dark` (#0F1E2D) com pattern sutil de nós e vetores
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Bem-vindos. Esta aula é sobre a infraestrutura cognitiva dos agentes — onde armazenamos e recuperamos conhecimento. Se ETHAGT06 mostrou COMO fazer retrieval, aqui vamos fundar ONDE e COM QUE ESTRUTURA. Vector databases e knowledge graphs não são concorrentes: são complementos. Ao final, vocês vão saber escolher, modelar e operar ambos, inclusive GraphRAG.
💡 ANALOGIA: O vector DB é a memória semântica (eu sei que algo é parecido). O knowledge graph é a memória relacional (eu sei que A está conectado a B via C). Um agente maduro usa as duas.
❓ PERGUNTA PARA A TURMA: "Quem aqui já usou um vector DB em produção? E um knowledge graph?" (levantar mãos — calibrar nível)
⚠️ ERROS COMUNS: Alunos chegam pensando que vector DB resolve tudo. Preciso plantar a dúvida cedo: similaridade ≠ raciocínio.
➡️ TRANSIÇÃO: "Vamos começar definindo o que vocês vão conseguir fazer ao final desta aula."

---

### Slide 2 — Objetivos do Módulo

**Título**: Objetivos do Módulo
**Objetivo**: Deixar claro o que o aluno deve conseguir FAZER ao final da aula.
**Conteúdo**:
- **Objetivo geral**: Escolher, modelar e operar vector databases e knowledge graphs como infraestrutura cognitiva de agentes — incluindo GraphRAG
- **Objetivos específicos**:
  1. Comparar vector databases por cenário (Qdrant, Milvus, Weaviate, Chroma, pgvector)
  2. Modelar knowledge graphs para raciocínio estruturado
  3. Implementar GraphRAG (local + global)
  4. Construir pipelines híbridos (vector + grafo)
  5. Avaliar custo/latência/escala em volumes realistas

**Diagrama**: 5 ícones representando cada objetivo (comparativo, grafo, GraphRAG, híbrido, escala)
**Animação**: Objetivos aparecem um a um (on click)
**Imagem**: Ícones minimalistas em `etho-accent` (#E85D2F)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Cada objetivo é mensurável. Não é "entender" — é "comparar", "modelar", "implementar", "construir", "avaliar". O objetivo #4 — pipelines híbridos — é o coração do projeto do módulo. Se ao final vocês não conseguem justificar por que escolheram vector vs grafo vs híbrido para um cenário, eu falhei.
💡 ANALOGIA: É como escolher ferramenta de marcenaria. Serra e martelo não competem — você usa cada um para o que serve. Vector e grafo são ferramentas cognitivas diferentes.
❓ PERGUNTA PARA A TURMA: "Qual desses objetivos vocês acham mais desafiador?" (deixar responder — costuma ser #3 GraphRAG ou #4 híbrido)
⚠️ ERROS COMUNS: Alunos confundem GraphRAG com "RAG usando grafo". GraphRAG é uma técnica específica da Microsoft (comunidades + sumarização hierárquica), não é só "grafo no RAG".
➡️ TRANSIÇÃO: "Antes de saber o que vamos fazer, vamos ver onde estamos no mapa de competências."

---

### Slide 3 — Competências Desenvolvidas

**Título**: Competências Desenvolvidas
**Objetivo**: Conectar a aula ao Framework Etho de competências.
**Conteúdo**:

| Competência | Nível ao final | Próximo nível em |
|---|---|---|
| C1 Programação Agêntica | **A** (Avançado) | ETHAGT14, ETHAGT90 |
| C3 MCP & Tool Use | **B** (Básico) | ETHAGT08 |
| C4 Agent Memory | **A** (Avançado) | ETHAGT05, ETHAGT90 |
| C5 AgentOps & Avaliação | **I** (Intermediário) | ETHAGT12 |

**Diagrama**: Radar chart com 4 eixos mostrando nível B/I/A
**Animação**: Radar aparece com wipe (left-to-right, 500ms)
**Imagem**: Badge visual por competência (círculos coloridos)
**Tempo**: 1 min

**Rodape**: AgentOps = Agent Operations — operacao e monitoramento de agentes em producao  ·  MCP = Model Context Protocol — Protocolo de Contexto de Modelo

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Este módulo leva C1 e C4 ao nível Avançado. Em C1, vocês já constroem agentes (ETHAGT01) — agora vocês dominam a infraestrutura cognitiva que sustenta raciocínio multi-hop. Em C4 (Agent Memory), vector DB é a memória semântica e knowledge graph é a memória relacional de um agente. C5 fica em Intermediário porque observabilidade de retrieval híbrido é aprofundada em ETHAGT12.
💡 ANALOGIA: C4 é a memória do agente. Hoje vocês vão além de "lembrar de fatos" (vector) para "lembrar de relações" (grafo). Um agente sem memória relacional é amnésico em causa-e-efeito.
⚠️ ERROS COMUNS: Alunos acham que "Avançado em C1" significa "saber muitos frameworks". Significa justificar arquitetura com evidência de trade-offs.
➡️ TRANSIÇÃO: "Vamos ver como esta aula está estruturada para entregar essas competências."

---

### Slide 4 — Agenda da Aula

**Título**: Agenda da Aula
**Objetivo**: Mostrar o roteiro da aula com tempos estimados.
**Conteúdo**:
- **Bloco 1 (45 min)**:
  - Abertura (8 min) — objetivos, motivação, contexto
  - Vector DBs (12 min) — ANN, HNSW, IVF, métricas, filtering
  - Comparativo (10 min) — 5 DBs, quando NÃO usar
  - Knowledge Graphs (15 min) — triplas, Neo4j, Cypher, extração
  - Intervalo (5 min)
- **Bloco 2 (45 min)**:
  - GraphRAG (15 min) — Microsoft GraphRAG, local vs global, DEMO
  - Híbridos (12 min) — vector + grafo, router, benchmark
  - Escala (8 min) — sharding, reindexação, observabilidade
  - Fechamento (10 min) — boas práticas, caso, quiz, Q&A

**Diagrama**: Timeline horizontal com 8 seções coloridas
**Animação**: Timeline cresce da esquerda para direita (500ms)
**Imagem**: Ícones de relógio por seção
**Tempo**: 1 min

**Rodape**: ANN = Approximate Nearest Neighbor — busca vetorial aproximada

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A aula tem dois blocos. O primeiro estabelece vector DBs e knowledge graphs como fundamentos separados. O segundo une os dois: GraphRAG, híbridos e escala. A DEMO do GraphRAG (Slide 46) é o clímax — mostro vector RAG falhando e GraphRAG acertando a mesma pergunta multi-hop.
💡 ANALOGIA: O bloco 1 é aprender os ingredientes (vector e grafo). O bloco 2 é cozinhar a receita (GraphRAG e híbridos). O fechamento é a avaliação do prato (benchmark e boas práticas).
⚠️ ERROS COMUNS: Alunos chegam atrasados e perdem a motivação (Slide 5). Avisar que o "split vector vs grafo" define o tom de toda a aula.
➡️ TRANSIÇÃO: "Vamos começar pelo porquê. Quando similaridade não basta?"

---

### Slide 5 — Motivação: Quando Similaridade Não Basta

**Título**: Quando Similaridade Não Basta
**Objetivo**: Criar tensão cognitiva — vector search sozinho não captura relacionamentos.
**Conteúdo**:
- **Vector search**: encontra documentos *similares* por semântica
- **Mas**: não sabe que "Dipirona" e "Warfarin" interagem
- **Exemplo**: "Quais medicamentos interagem com o remédio que o Dr. Silva prescreveu para o paciente X?"
- Vector search sozinho: retorna textos *sobre* interações, mas não *raciocina* sobre a cadeia
- **Pergunta**: *Quando uma busca por similaridade não é suficiente?*

**Diagrama**: Split — esquerdo (vector: nuvem de pontos) | direito (grafo: nós conectados)
**Animação**: Split — lado esquerdo aparece primeiro, depois lado direito
**Imagem**: Ícone de nuvem de pontos (esquerda) vs grafo conectado (direita)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vector search é incrível para "encontre documentos parecidos com X". Mas a pergunta do exemplo exige encadear três fatos: (1) Dr. Silva prescreveu Dipirona para paciente X, (2) Dipirona interage com Warfarin, (3) paciente X toma Warfarin. Vector search não encadeia — ele recupera textos isolados. Para raciocínio multi-hop, precisamos de estrutura: um knowledge graph.
💡 ANALOGIA: Vector search é como buscar livros na estante por tema (todos os livros sobre "interações medicamentosas" estão juntos). Mas saber que ESTE paciente toma AQUELE remédio que interage com ESTE outro — isso é relacionamento, não similaridade. Relacionamento vive em grafo, não em nuvem de pontos.
❓ PERGUNTA PARA A TURMA: "Pensem no sistema de vocês: existe uma pergunta que exige encadear 2+ fatos? O vector search atual responde?" (deixar pensar 30s)
⚠️ ERROS COMUNS: Alunos acham que "prompt maior" ou "mais chunks" resolve multi-hop. Não resolve de forma confiável — o LLM pode alucinar a cadeia. Estrutura (grafo) garante a cadeia.
➡️ TRANSIÇÃO: "Essa lacuna não é nova. Mas por que só agora temos uma solução industrial?"

---

### Slide 6 — Contexto: A Evolução do RAG

**Título**: A Evolução do RAG
**Objetivo**: Explicar a evolução de RAG simples para GraphRAG.
**Conteúdo**:
- **Linha do tempo**:
  - 2020: RAG original (Lewis et al., arXiv:2005.11401)
  - 2022: Dense retrieval amadurece
  - 2023: RAG agêntico (ETHAGT06)
  - 2024: GraphRAG (Microsoft, arXiv:2404.16130)
- **Confluência**: embeddings melhores + graph databases acessíveis + LLMs para extração de entidades
- **Survey**: Pan et al. (arXiv:2306.08302) unifica LLMs e KGs

**Diagrama**: Timeline horizontal com marcos + 3 setas convergindo para "GraphRAG viável"
**Animação**: Marcos aparecem sequencialmente (on click)
**Imagem**: Convergência de 3 rios (embeddings, grafos, LLMs) em um lago
**Tempo**: 1 min

**Rodape**: RAG = Retrieval-Augmented Generation — Geracao Aumentada por Recuperacao

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: RAG existe desde 2020, mas era "recupera chunk, gera resposta". Em 2024, a Microsoft publicou GraphRAG, que constrói um grafo de entidades a partir do corpus, detecta comunidades e sumariza hierarquicamente. Isso permite responder perguntas GLOBAIS ("quais os temas principais?") que vector RAG não consegue. A confluência: embeddings ficaram baratos, graph databases (Neo4j) ficaram acessíveis em cloud, e LLMs ficaram bons em extrair entidades/relações.
💡 ANALOGIA: É como a evolução da cartografia. Vector RAG é um atlas (você acha a página certa). GraphRAG é um GPS com rotas (você navega entre pontos). O GPS é mais caro de construir, mas responde perguntas que o atlas não consegue.
❓ PERGUNTA PARA A TURMA: "Qual dos 3 fatores vocês acham que foi o gatilho mais recente?" (Resposta: LLMs para extração — sem extração automática de entidades, construir KG era proibitivo)
⚠️ ERROS COMUNS: Alunos acham que GraphRAG é "novo". O paper é de 2024, mas knowledge graphs existem há décadas. O que é novo é a automação da construção via LLM.
➡️ TRANSIÇÃO: "Agora que sabemos por que estamos aqui, vamos ao primeiro bloco: como funciona um vector DB por dentro."

---

## SEÇÃO B — Vector DBs: Modelo Mental (Slides 7-16 · 12 min)

---

### Slide 7 — [SEÇÃO] Vector DBs: Modelo Mental

**Título**: 1 — Vector DBs: Modelo Mental
**Objetivo**: Transição visual para o bloco de fundamentos de vector DBs.
**Conteúdo**: Número "1" grande + "Vector DBs: Modelo Mental"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "1" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Início do bloco de fundamentos. Vamos responder: o que é um vector DB por dentro? Como ele busca em milhões de vetores em milissegundos? E quais são as métricas e técnicas de filtering que fazem a diferença?
➡️ TRANSIÇÃO: "Primeiro: o que é, afinal, um vector DB?"

---

### Slide 8 — O Que É um Vector DB?

**Título**: O Que É um Vector DB?
**Objetivo**: Apresentar a arquitetura canônica de um vector database.
**Conteúdo**:
- Armazena embeddings (vetores densos) + metadata
- Index para busca ANN (não brute force)
- Query: vetor → top-k mais similares
- Componentes: collection → points (id, vector, payload) → index
- Diferença de DB relacional: similaridade, não igualdade

**Diagrama**: D1 — Arquitetura de vector DB (collection → index → query)
**Animação**: Componentes surgem do centro para fora
**Imagem**: Ícones de coleção, índice e query
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Um vector DB armazena vetores (embeddings de texto, imagem, áudio) junto com metadata (payload). A diferença fundamental para um DB relacional: você não busca por IGUALDADE (WHERE id = 42), você busca por SIMILARIDADE (top-k vetores mais próximos do meu query vector). Para isso em escala, você não pode comparar o query com todos os vetores (brute force) — usa um index de Approximate Nearest Neighbor (ANN).
💡 ANALOGIA: DB relacional é como buscar um livro pelo ISBN (igualdade exata). Vector DB é como buscar "livros parecidos com este" (similaridade). São paradigmas diferentes, com estruturas de index diferentes.
❓ PERGUNTA PARA A TURMA: "Por que não usar brute force em tudo?" (Resposta: O(N) não escala — 100M vetores × 1536 dims = 150 bilhões de comparações por query)
⚠️ ERROS COMUNS: Alunos acham que vector DB é "Postgres com uma coluna de array". Não — o index ANN é o que faz ser um vector DB. Sem HNSW/IVF, é só armazenamento.
➡️ TRANSIÇÃO: "E o que armazenamos? Embeddings. Vamos recapitular."

---

### Slide 9 — Embeddings: A Base

**Título**: Embeddings: A Base
**Objetivo**: Recapitular embeddings (aprofundado em ETHAGT06).
**Conteúdo**:
- Texto → modelo de embedding → vetor denso (ex: 1536 dims)
- Semântica capturada na geometria do espaço
- Modelos: OpenAI text-embedding-3, Cohere, BGE, GTE
- Dimensões: trade-off entre riqueza e custo de armazenamento/busca
- Aprofundamento em ETHAGT06

**Diagrama**: D2 — Texto → embedding → espaço vetorial (pontos próximos)
**Animação**: Texto → vetor → pontos (sequencial)
**Imagem**: Visualização de embeddings em 2D (projeção t-SNE)
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Embeddings são a representação vetorial da semântica. Um modelo transforma texto em um vetor denso onde "proximidade" = "semelhança de significado". A dimensão (1536 para OpenAI text-embedding-3-small, 3072 para o large) é um trade-off: mais dimensões = mais riqueza semântica, mas mais custo de armazenamento e busca. Não vou aprofundar embeddings aqui — isso é ETHAGT06. Hoje assumo que vocês já geram embeddings e foco em COMO armazenar e buscar eficientemente.
💡 ANALOGIA: Embedding é como um código postal da semântica. Textos sobre o mesmo tema têm "CEPs" próximos. O vector DB é a agência dos correios que encontra os CEPs mais próximos do seu query.
⚠️ ERROS COMUNS: Alunos mudam de modelo de embedding sem reindexar. Vetores do modelo antigo e novo são INCOMPATÍVEIS — cosine similarity entre eles é lixo. Voltamos a isso no Slide 66.
➡️ TRANSIÇÃO: "Dado que temos milhões de embeddings, como buscamos rápido? ANN."

---

### Slide 10 — ANN: Approximate Nearest Neighbor

**Título**: ANN: Approximate Nearest Neighbor
**Objetivo**: Explicar por que não usamos brute force.
**Conteúdo**:
- Brute force: O(N) — inviável para milhões de vetores
- ANN: sacrifica exatidão por velocidade (recall vs latência)
- Duas famílias principais: HNSW (graph-based) e IVF (cluster-based)
- Trade-off fundamental: recall ↑ → latência ↑
- Parâmetro de controle: ef_search (HNSW), nprobe (IVF)

**Diagrama**: D3 — Curva recall vs latência
**Animação**: Curva é desenhada da esquerda para direita
**Imagem**: Gráfico com eixos recall (Y) e latência (X)
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Brute force compara o query vector com TODOS os vetores. Para 10 milhões de vetores de 1536 dims, isso são 15 bilhões de multiplicações por query — inviável. ANN (Approximate Nearest Neighbor) sacrifica um pouco de exatidão (recall) por velocidade gigantesca. Em vez de 100% de recall em segundos, obtemos 95% de recall em milissegundos. As duas famílias dominantes: HNSW (graph-based) e IVF (cluster-based). O trade-off é controlável: aumente ef_search (HNSW) ou nprobe (IVF) para mais recall ao custo de mais latência.
💡 ANALOGIA: É como buscar um livro em uma livraria. Brute force é ler todas as capas uma a uma. ANN é ir direto na seção do gênero (IVF) ou seguir um índice alfabético navegável (HNSW). Você pode perder um livro mal classificado, mas encontra 95% na hora.
❓ PERGUNTA PARA A TURMA: "Quando você aceitaria 90% de recall em vez de 100%?" (Resposta: quase sempre em RAG — o LLM tolera algum ruído. Recall exato só importa em matching determinístico)
⚠️ ERROS COMUNS: Alunos acham que "recall baixo = ruim". Em RAG, recall@10 de 90% é excelente — você recupera 9 dos 10 documentos realmente relevantes, e o LLM lida com o resto.
➡️ TRANSIÇÃO: "Vamos aprofundar as duas famílias. Primeiro: HNSW."

---

### Slide 11 — HNSW: Hierarchical Navigable Small World

**Título**: HNSW: Hierarchical Navigable Small World
**Objetivo**: Apresentar o algoritmo dominante em vector DBs.
**Conteúdo**:
- Grafo hierárquico de camadas: top (sparse, fast) → bottom (dense, precise)
- Busca: começa no topo, desce camada por camada
- Vantagem: recall alto, latência baixa
- Desvantagem: construção lenta, memória
- Usado por: Qdrant, Milvus, Weaviate, pgvector (opcional)
- Fonte: Malkov & Yashunin, arXiv:1603.09320

**Diagrama**: D4 — Estrutura hierárquica de HNSW (3 camadas)
**Animação**: Camadas aparecem de cima para baixo
**Imagem**: Camadas como "mapas em zoom" (topo = visão ampla, base = detalhe)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: HNSW constrói um grafo em camadas. A camada do topo é esparsa (poucos nós, mas bem distribuídos) — serve para "pousar" perto da região certa rapidamente. As camadas inferiores são mais densas (mais nós) — refinam a busca. A busca começa no topo, navega rápido até a região, depois desce camada por camada, refinando. É como um GPS: primeiro você voa para a cidade (topo), depois dirige para o bairro (meio), depois caminha até a porta (base).
💡 ANALOGIA: É a estratégia de "fly, drive, walk" dos mapas. Cada camada é um nível de zoom. Você não começa caminhando de São Paulo a Recife — você voa, depois dirige, depois caminha.
❓ PERGUNTA PARA A TURMA: "Por que a construção do HNSW é lenta?" (Resposta: cada inserção precisa decidir em quais camadas o nó aparece e conectar arestas em cada uma — é trabalho por vetor)
⚠️ ERROS COMUNS: Alunos acham que HNSW é "exato". Não é — é aproximado. Mas com ef_search alto, recall aproxima de 100%. A aproximação é controlável.
➡️ TRANSIÇÃO: "A alternativa baseada em clustering: IVF."

---

### Slide 12 — IVF: Inverted File Index

**Título**: IVF: Inverted File Index
**Objetivo**: Apresentar a alternativa baseada em clustering.
**Conteúdo**:
- K-means divide o espaço em clusters (Voronoi cells)
- Busca: encontra cluster mais próximo → busca dentro dele
- nprobe: quantos clusters vizinhos explorar
- Vantagem: construção mais rápida, bom para datasets muito grandes
- Desvantagem: recall menor que HNSW para mesmo custo
- Combinável com PQ (Product Quantization) para compressão

**Diagrama**: D5 — Espaço particionado em células de Voronoi
**Animação**: Células aparecem, depois setas de nprobe
**Imagem**: Espaço 2D colorido por célula
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: IVF divide o espaço vetorial em clusters usando k-means. Cada cluster tem um centroide. Na busca, você calcula a distância do query aos centroides (rápido — são poucos), escolhe os mais próximos e busca só dentro desses clusters. O nprobe controla quantos clusters vizinhos explorar: nprobe=1 é rápido mas pode perder o vizinho real (se ele está na fronteira); nprobe alto é mais preciso mas mais lento.
💡 ANALOGIA: É como um sistema de CEPs. Você não busca em todo o país — vai direto para o CEP do query e explora os CEPs vizinhos (nprobe). Mais CEPs vizinhos = mais cobertura, mais tempo.
⚠️ ERROS COMUNS: Alunos deixam nprobe=1 (default) e reclamam de recall baixo. nprobe é o parâmetro #1 de tuning de IVF — ajuste conforme seu dataset.
➡️ TRANSIÇÃO: "Independente do index, você precisa de uma métrica de similaridade."

---

### Slide 13 — Métricas de Similaridade: Cosine, Dot, Euclidean

**Título**: Métricas: Cosine, Dot, Euclidean
**Objetivo**: Apresentar as 3 métricas e quando usar cada.
**Conteúdo**:
- Cosine: ângulo entre vetores — ignora magnitude
- Dot product: cosine × magnitudes — sensível a norma
- Euclidean (L2): distância geométrica — sensível a magnitude e direção
- Fórmulas visuais para cada
- Se embeddings são normalizados: cosine = dot product

**Diagrama**: D6 — 3 visualizações lado a lado (círculo unitário, plano, distância)
**Animação**: Cada métrica aparece com click
**Imagem**: Fórmulas matemáticas renderizadas
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A métrica define o que "similar" significa. Cosine mede o ÂNGULO entre vetores — dois vetores apontando na mesma direção são similares, mesmo que um seja 10x maior. Dot product é cosine multiplicado pelas magnitudes — se os vetores não são normalizados, a magnitude "contamina" a similaridade. Euclidean (L2) é a distância geométrica direta. Insight chave: SE os embeddings são normalizados (norma = 1), cosine e dot product dão o MESMO ranking. Por isso muita gente normaliza e usa dot (mais rápido de computar).
💡 ANALOGIA: Cosine é como comparar a DIREÇÃO de duas setas (norte vs nordeste). Dot é direção + força. Euclidean é a distância das pontas. Para texto, direção (cosine) costuma ser o que importa — "cachorro late" e "cães ladram" têm a mesma direção semântica.
⚠️ ERROS COMUNS: Alunos indexam com cosine e query com euclidean (ou vice-versa). O ranking fica inconsistente e o recall despenca. Métrica de index = métrica de query, SEMPRE.
➡️ TRANSIÇÃO: "Mas na prática, como escolher? Tem uma árvore de decisão."

---

### Slide 14 — Quando Cada Métrica?

**Título**: Quando Cada Métrica?
**Objetivo**: Dar critério prático de escolha.
**Conteúdo**:
- Cosine: default para texto (embeddings não normalizados)
- Dot: quando embeddings já são normalizados (mais rápido)
- Euclidean: quando magnitude importa (ex: features multimodais)
- Pergunta técnica: *Cosine vs dot — quando a diferença importa?*
- Armadilha: misturar métricas entre index e query = recall destruído

**Diagrama**: D7 — Árvore de decisão simples
**Animação**: Ramos aparecem sequencialmente
**Imagem**: Fluxograma com 3 saídas
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Regra prática: se você não sabe, use cosine. É o default para texto. Se você normaliza os embeddings (norma = 1), mude para dot product — é computacionalmente mais barato (uma multiplicação a menos por dimensão) e dá o mesmo ranking. Euclidean só quando magnitude carrega informação — raro em texto NLP, comum em features multimodais (ex: áudio onde volume importa).
💡 ANALOGIA: Cosine é a escolha segura (como dirigir devagar). Dot com normalização é a otimização (como dirigir na velocidade ideal). Euclidean é o caso especial (como dirigir off-road — só quando precisa).
❓ PERGUNTA PARA A TURMA: "Cosine vs dot — quando a diferença importa?" (Resposta: quando os embeddings NÃO são normalizados e têm magnitudes variáveis. Se normalizados, dá no mesmo — prefira dot pela velocidade)
⚠️ ERROS COMUNS: Alunos usam cosine em embeddings normalizados — funciona, mas desperdiça computação. Normalize e use dot.
➡️ TRANSIÇÃO: "Além da métrica, outro eixo crítico: filtering de metadata."

---

### Slide 15 — Metadata Filtering (Payloads)

**Título**: Metadata Filtering (Payloads)
**Objetivo**: Explicar filtering de metadata e o trade-off pre vs post.
**Conteúdo**:
- Payload: JSON anexado a cada vetor (ex: `{"source": "doc.pdf", "page": 3}`)
- Pre-filtering: filtra antes da busca ANN (preciso, mas pode ser lento)
- Post-filtering: filtra depois da busca ANN (rápido, mas pode reduzir recall)
- Qdrant: filtering otimizado no index (vantagem chave)
- Padrão: `vector + filter → top-k`

**Diagrama**: D8 — Fluxo pre-filter vs post-filter
**Animação**: Dois fluxos aparecem lado a lado
**Imagem**: Pipeline com filter e ANN
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Na prática, você quase nunca busca só por similaridade — você filtra. "Documentos do ano de 2024, categoria jurídica, top-10 mais similares." A pergunta é: filtra ANTES ou DEPOIS do ANN? Pre-filtering filtra o conjunto primeiro, depois faz ANN só nos que passaram — preciso, mas se o filtro é muito restritivo, o ANN tem poucos vetores e fica lento ou vazio. Post-filtering faz ANN em tudo e descarta os que não passam no filtro — rápido, mas se o filtro descarta muitos, seu top-10 vira top-2 (recall destruído). Qdrant otimiza o filtering DENTRO do index — é a vantagem chave dele.
💡 ANALOGIA: Pre-filter é como peneirar a farinha antes de medir (preciso, mas a peneira pode travar). Post-filter é como medir tudo e descartar os grumos depois (rápido, mas você pode descartar demais). Qdrant tem uma peneira inteligente integrada na medida.
⚠️ ERROS COMUNS: Alunos usam post-filter com filtro restritivo e ficam com top-10 = 2 resultados. Sempre teste recall com seus filtros reais, não só sem filtro.
➡️ TRANSIÇÃO: "Antes de fechar este bloco: retrieval híbrido sparse + dense."

---

### Slide 16 — Híbrido: Sparse + Dense (BM25 + Dense)

**Título**: Híbrido: Sparse + Dense
**Objetivo**: Introduzir retrieval híbrido sparse+dense.
**Conteúdo**:
- Dense: semântica (sinônimos, paráfrase) — falha em termos exatos
- Sparse (BM25/SPLADE): termos exatos (nomes próprios, códigos) — falha em semântica
- Híbrido: combina ambos com fusão de scores (RRF ou ponderado)
- Reciprocal Rank Fusion (RRF): simples e eficaz
- Qdrant 1.10+: sparse vectors nativos

**Diagrama**: D9 — Duas trilhas (sparse + dense) convergindo para RRF
**Animação**: Trilhas aparecem, depois RRF funde
**Imagem**: Fluxo duplo convergindo
**Tempo**: 1 min

**Rodape**: BM25 = Best Matching 25 — algoritmo de ranking para busca textual

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Dense (embeddings) é ótimo em semântica — "cachorro" encontra "cão". Mas falha em termos exatos — se você busca por " Lei 13.709/2018", o dense pode trazer leis semelhantes mas não a exata. Sparse (BM25) é o oposto: acerta termos exatos, falha em paráfrase. Híbrido combina os dois. A fusão mais simples e eficaz é RRF (Reciprocal Rank Fusion): para cada resultado, some 1/(rank + k) de cada trilha. Não precisa calibrar pesos — RRF é robusto e parameter-light.
💡 ANALOGIA: Dense é como um tradutor que entende sinonímia (mas pode confundir homônimos). Sparse é como um índice de livro (acerta a página exata, mas não entende paráfrase). Híbrido usa os dois — um para conceito, outro para precisão.
⚠️ ERROS COMUNS: Alunos tentam ponderar scores (0.7*dense + 0.3*sparse) e passam semanas tunando pesos. RRF evita isso — é robusto sem calibração. Comece com RRF.
➡️ TRANSIÇÃO: "Agora que dominamos o modelo mental, vamos ao comparativo prático dos 5 vector DBs."

---

## SEÇÃO C — Comparativo de Vector DBs (Slides 17-25 · 10 min)

---

### Slide 17 — [SEÇÃO] Comparativo de Vector DBs

**Título**: 2 — Comparativo de Vector DBs
**Objetivo**: Transição para o comparativo prático.
**Conteúdo**: "2 — Comparativo de Vector DBs"
**Diagrama**: Fundo `etho-primary`
**Animação**: Morph (400ms)
**Imagem**: Número "2" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vamos comparar os 5 vector DBs canônicos do mercado. A mensagem central: NÃO existe "melhor vector DB" — existe "melhor para seu cenário". Vamos olhar cada um pelo seu ponto forte.
➡️ TRANSIÇÃO: "O landscape: 5 contenders."

---

### Slide 18 — O Landscape: 5 Contenders

**Título**: O Landscape: 5 Contenders
**Objetivo**: Visão geral do ecossistema.
**Conteúdo**:
- 5 vector DBs canônicos: Qdrant, Milvus, Weaviate, Chroma, pgvector
- Eixos de comparação: linguagem, escala, filtering, ecosystem, maturidade
- Não existe "melhor" — existe "melhor para seu cenário"

**Diagrama**: D10 — Grid 2x3 com logos e 1 linha de descrição cada
**Animação**: Cada DB aparece com click
**Imagem**: Logos dos 5 DBs
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esses são os 5 que vocês encontrarão no mercado. Qdrant (Rust, filtering forte), Milvus (escala massiva), Weaviate (modules integrados), Chroma (simplicidade), pgvector (extensão do Postgres). Cada um brilha em um cenário. Não memorizem features — memorizem o TRADE-OFF de cada.
💡 ANALOGIA: É como escolher carro. Chroma é o Uber (simples, te leva lá). pgvector é a picape (faz tudo, já tem na garagem). Qdrant é o esportivo (rápido e preciso). Milvus é o caminhão (escala pesada). Weaviate é a van (tudo integrado).
➡️ TRANSIÇÃO: "Vamos um a um. Qdrant."

---

### Slide 19 — Qdrant: Filtering Forte

**Título**: Qdrant: Filtering Forte
**Objetivo**: Destacar os pontos fortes do Qdrant.
**Conteúdo**:
- Escrito em Rust: performance e safety
- Filtering otimizado no index (não é post-filter)
- Sparse vectors nativos (híbrido sem infra extra)
- Multi-tenancy via payloads
- Melhor quando: filtering complexo é requisito

**Diagrama**: Logo Qdrant + bullet points
**Animação**: Bullets aparecem sequencialmente
**Imagem**: Logo do Qdrant
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Qdrant é escrito em Rust — isso dá performance e memory safety. O ponto forte dele é o filtering: ao contrário de muitos DBs que fazem post-filtering, Qdrant otimiza o filter DENTRO do index HNSW. Isso significa que você pode ter filtros complexos sem destruir o recall. Além disso, Qdrant tem sparse vectors nativos desde 1.10 — você faz híbrido sem precisar de uma infra separada para BM25.
💡 ANALOGIA: Qdrant é o DB "filtering-first". Se seu caso tem muitos filtros (tenant, categoria, data), Qdrant brilha.
⚠️ ERROS COMUNS: Alunos escolhem Qdrant "porque é Rust". A linguagem é meio; o fim é o filtering otimizado. Escolha pelo trade-off, não pelo hype.
➡️ TRANSIÇÃO: "Milvus: escala."

---

### Slide 20 — Milvus: Escala

**Título**: Milvus: Escala
**Objetivo**: Destacar os pontos fortes do Milvus.
**Conteúdo**:
- Arquitetura distribuída desde o início (cloud-native)
- Escala horizontal para bilhões de vetores
- Suporte a múltiplos index types (HNSW, IVF, DiskANN)
- Melhor quando: escala massiva é o requisito #1
- Trade-off: complexidade operacional maior

**Diagrama**: Logo Milvus + bullet points
**Animação**: Bullets aparecem sequencialmente
**Imagem**: Logo do Milvus
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Milvus foi desenhado desde o início como sistema distribuído. Tem componentes separados (QueryNode, DataNode, Proxy) que escalam independentemente. Se você tem 1 bilhão de vetores e precisa escalar horizontalmente, Milvus é a escolha. O custo disso é complexidade operacional — você precisa orquestrar múltiplos componentes.
💡 ANALOGIA: Milvus é o "big rig" dos vector DBs. Se você tem carga pesada (bilhões), é ele. Se você tem 1 milhão de vetores, é overkill — a complexidade não se paga.
⚠️ ERROS COMUNS: Alunos escolhem Milvus por "escala futura" sem ter o volume hoje. A complexidade operacional custa caro em engineering time. Comece simples, migre quando precisar.
➡️ TRANSIÇÃO: "Weaviate: modules."

---

### Slide 21 — Weaviate: Modules

**Título**: Weaviate: Modules
**Objetivo**: Destacar os pontos fortes do Weaviate.
**Conteúdo**:
- Modules integrados: generative, Q&A, multi-modal
- Schema-first: define classes e propriedades
- GraphQL API nativa
- Melhor quando: quer pipeline RAG completo sem orquestrar 5 serviços
- Trade-off: menos flexível para casos não previstos pelos modules

**Diagrama**: Logo Weaviate + bullet points
**Animação**: Bullets aparecem sequencialmente
**Imagem**: Logo do Weaviate
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Weaviate é "batteries-included". Tem modules que integram geração (chamar LLM), Q&A (retrieve + answer em uma query), e multi-modal (texto + imagem). Se você quer um pipeline RAG completo sem orquestrar Qdrant + LangChain + Cohere, Weaviate te dá isso pronto. O custo: se seu caso foge do que os modules cobrem, você briga contra a abstração.
💡 ANALOGIA: Weaviate é como um carro com GPS, ar-condicionado e banco elétrico de fábrica. Prático. Mas se você quer customizar o motor, é mais difícil que num carro pelado.
➡️ TRANSIÇÃO: "Chroma: simplicidade."

---

### Slide 22 — Chroma: Simplicidade

**Título**: Chroma: Simplicidade
**Objetivo**: Destacar os pontos fortes do Chroma.
**Conteúdo**:
- API minimalista: `client.add(docs)` → `client.query(text)`
- Embutido no processo Python (sem servidor separado)
- Melhor quando: prototipagem, MVP, dev local
- Trade-off: não é production-ready para escala (ainda)

**Diagrama**: Logo Chroma + bullet points
**Animação**: Bullets aparecem sequencialmente
**Imagem**: Logo do Chroma
**Tempo**: 1 min

**Rodape**: MVP = Minimum Viable Product — Produto Minimo Viavel

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Chroma é o "importe e use". Você adiciona documentos em uma linha e query em outra. Ele roda embutido no processo Python — sem Docker, sem servidor. É perfeito para protótipos, MVPs e desenvolvimento local. O trade-off: não está pronto para escala de produção (ainda). Para milhões de vetores em produção, considere Qdrant ou Milvus.
💡 ANALOGIA: Chroma é o SQLite dos vector DBs. Embutido, simples, perfeito para começar. Para produção com escala, você migra (como migra de SQLite para Postgres).
⚠️ ERROS COMUNS: Alunos começam com Chroma e tentam levar para produção sem migrar. Funciona até parar de funcionar. Plano de migração desde o dia 1.
➡️ TRANSIÇÃO: "pgvector: operacional."

---

### Slide 23 — pgvector: Operacional

**Título**: pgvector: Operacional
**Objetivo**: Destacar os pontos fortes do pgvector.
**Conteúdo**:
- Extensão do PostgreSQL: vector DB dentro do DB que você já tem
- HNSW e IVFFlat disponíveis
- ACID, transações, JOINs com vetores
- Melhor quando: já usa Postgres e não quer adicionar infra
- Trade-off: não escala como solução dedicada para bilhões de vetores

**Diagrama**: Logo pgvector + bullet points
**Animação**: Bullets aparecem sequencialmente
**Imagem**: Logo do Postgres + pgvector
**Tempo**: 1 min

**Rodape**: ACID = Atomicity Consistency Isolation Durability — propriedades de transacoes

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: pgvector é uma extensão do PostgreSQL. Você adiciona a coluna de vetor e faz busca vetorial COM JOINs relacionais — tudo no mesmo DB, com ACID, transações, backups que você já tem. Para a maioria das aplicações (até ~1M de vetores), pgvector resolve sem adicionar infra. O trade-off: para bilhões de vetores, soluções dedicadas (Qdrant, Milvus) escalam melhor.
💡 ANALOGIA: pgvector é como ter uma picape que já está na sua garagem. Se você já tem Postgres, pgvector te dá vector DB "de graça" (sem nova infra). Só troque de veículo se a picapa não aguenta a carga.
❓ PERGUNTA PARA A TURMA: "Quando pgvector é melhor que Qdrant?" (Resposta: quando você já tem Postgres e quer simplicidade operacional + transações ACID. Não vale adicionar Qdrant se pgvector resolve seu volume)
⚠️ ERROS COMUNS: Alunos subestimam pgvector. Para 90% das aplicações RAG, pgvector resolve. Não adicione vector DB dedicado sem evidência de que pgvector não basta.
➡️ TRANSIÇÃO: "Vamos sistematizar tudo numa tabela."

---

### Slide 24 — Tabela Comparativa

**Título**: Tabela Comparativa
**Objetivo**: Sistematizar os trade-offs.
**Conteúdo**:
- Tabela: Qdrant vs Milvus vs Weaviate vs Chroma vs pgvector
- Eixos: linguagem, escala máxima, filtering, híbrido, multi-tenancy, custo operacional, curva de aprendizado, production-ready
- Discussão: *Para um MVP, qual escolher? E para 1M de usuários?*

**Diagrama**: D11 — Tabela comparativa colorida (heat map)
**Animação**: Colunas aparecem uma a uma
**Imagem**: Heat map verde→amarelo→vermelho
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esta tabela sintetiza os trade-offs. Não decorem — entendam o padrão: soluções dedicadas (Qdrant, Milvus) escalam mais mas custam mais em complexidade. Soluções embutidas (Chroma, pgvector) são simples mas têm teto de escala. Weaviate é o meio-termo "tudo integrado".
❓ PERGUNTA PARA A TURMA: "Para um MVP, qual escolher? E para 1M de usuários?" (Resposta típica: MVP = Chroma ou pgvector. 1M usuários = Qdrant ou Milvus, dependendo do filtering)
⚠️ ERROS COMUNS: Alunos escolhem por "popularidade no GitHub". Popularidade ≠ fit para seu caso. Decida pelos trade-offs que importam para VOCÊ.
➡️ TRANSIÇÃO: "Mas antes de escolher qualquer vector DB, pergunte: você precisa mesmo de um?"

---

### Slide 25 — Quando NÃO Usar Vector DB

**Título**: Quando NÃO Usar Vector DB
**Objetivo**: Ser honesto — vector DB nem sempre é a resposta.
**Conteúdo**:
- Busca exata (igualdade): DB relacional é melhor
- Dados estruturados com relacionamentos: knowledge graph
- Volume pequeno (< 10k docs): brute force em memória
- Latência ultra-baixa: cache + keyword search
- Regra: não adicione vector DB se Postgres resolve

**Diagrama**: D12 — Árvore de decisão "preciso de vector DB?"
**Animação**: Ramos aparecem
**Imagem**: Fluxograma de decisão
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vector DB é on-trend, mas nem tudo precisa de um. Se você busca por igualdade (WHERE id = 42), relacional é mais rápido e mais barato. Se você tem relacionamentos estruturados (A depende de B), knowledge graph. Se você tem menos de 10k documentos, brute force em memória (numpy) é instantâneo e sem infra. Vector DB é para BUSCA POR SIMILARIDADE EM ESCALA. Se você não tem escala ou não busca por similaridade, não precisa.
💡 ANALOGIA: É como comprar um trator para cuidar de um jardim. O trator é ótimo — para uma fazenda. Para o jardim, uma enxada resolve e custa menos.
⚠️ ERROS COMUNS: Alunos adicionam vector DB "porque é moderno" quando um JOIN no Postgres resolve. Complexidade desnecessária = dívida técnica. Comece simples, adicione vector DB quando a evidência (latência, recall) pedir.
➡️ TRANSIÇÃO: "Falando em knowledge graph — esse é o próximo bloco grande."

---

## SEÇÃO D — Knowledge Graphs (Slides 26-36 · 15 min)

---

### Slide 26 — [SEÇÃO] Knowledge Graphs

**Título**: 3 — Knowledge Graphs
**Objetivo**: Transição para o bloco de knowledge graphs.
**Conteúdo**: Número "3" grande + "Knowledge Graphs"
**Diagrama**: Fundo `etho-primary`
**Animação**: Morph (400ms)
**Imagem**: Número "3" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Início do segundo paradigma de armazenamento cognitivo: knowledge graphs. Se vector DB é "similaridade", knowledge graph é "relacionamento". Vamos ver o modelo de dados (triplas), a ferramenta dominante (Neo4j + Cypher), e como construir um KG a partir de texto não-estruturado com LLMs.
➡️ TRANSIÇÃO: "Primeiro: o que é, fundamentalmente, um knowledge graph?"

---

### Slide 27 — O Que É um Knowledge Graph?

**Título**: O Que É um Knowledge Graph?
**Objetivo**: Apresentar a diferença fundamental: vector vs graph.
**Conteúdo**:
- Vector DB: similaridade semântica (proximidade no espaço)
- Knowledge Graph: relacionamentos estruturados (travessia de nós)
- Vector: "documentos parecidos com X"
- Graph: "entidades conectadas a X via relação Y"
- Complementares, não concorrentes

**Diagrama**: D13 — `12-Diagrams/ETHAGT07/vector-vs-graph.mmd`
**Animação**: Árvore de decisão cresce
**Imagem**: Split vector (nuvem) vs graph (rede)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A diferença fundamental: vector DB responde "o que é similar a X?" (proximidade no espaço vetorial). Knowledge graph responde "o que está conectado a X, e como?" (travessia de nós e arestas). São paradigmas complementares. Um agente maduro usa os dois: vector para recuperar documentos, graph para raciocinar sobre relacionamentos.
💡 ANALOGIA: Vector DB é como uma biblioteca organizada por tema (você acha livores parecidos). Knowledge graph é como uma árvore genealógica (você sabe quem é parente de quem e como). Um não substitui o outro — você precisa dos dois.
⚠️ ERROS COMUNS: Alunos tratam vector DB e knowledge graph como "escolha binária". Não é. A escolha é "qual usar para CADA pergunta", e a resposta madura é "ambos, em pipeline híbrido" (voltamos a isso na Seção F).
➡️ TRANSIÇÃO: "Qual é o modelo de dados de um knowledge graph? A tripla."

---

### Slide 28 — Triplas: Sujeito → Predicado → Objeto

**Título**: Triplas: Sujeito → Predicado → Objeto
**Objetivo**: Apresentar o modelo de dados fundamental de um KG.
**Conteúdo**:
- Tripla: (sujeito, predicado, objeto)
- Exemplo: ("Dipirona", "interage_com", "Warfarin")
- Exemplo: ("Dr. Silva", "prescreveu", "Dipirona")
- Exemplo: ("Paciente X", "consultou", "Dr. Silva")
- Encadeamento: Paciente X → Dr. Silva → Dipirona → Warfarin (multi-hop!)

**Diagrama**: D14 — 3 nós conectados por arestas rotuladas
**Animação**: Triplas aparecem uma a uma, depois o encadeamento
**Imagem**: Grafo pequeno com nós e arestas
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Um knowledge graph é um conjunto de triplas. Cada tripla é (sujeito, predicado, objeto). "Dipirona interage_com Warfarin." "Dr. Silva prescreveu Dipirona." "Paciente X consultou Dr. Silva." A mágica está no ENCADEAMENTO: se o paciente X consultou o Dr. Silva, que prescreveu Dipirona, que interage com Warfarin — e sabemos que o paciente X toma Warfarin — então há um RISCO. Esse raciocínio multi-hop é exatamente o que vector search não faz bem. O grafo encadeia porque as arestas são explícitas e navegáveis.
💡 ANALOGIA: Triplas são como frases de três palavras (sujeito-verbo-objeto). O knowledge graph é um texto feito só dessas frases — e o significado emerge das conexões. "Paciente consulta doutor prescreve remédio interage com outro remédio" é uma narrativa de risco clínico, codificada em grafo.
❓ PERGUNTA PARA A TURMA: "Pensem no domínio de vocês: quais 3 triplas seriam mais valiosas?" (deixar pensar — costuma revelar o modelo mental do domínio)
⚠️ ERROS COMUNS: Alunos modelam com predicados vagos ("RELATED_TO"). Isso destrói o raciocínio — você não sabe QUAL é a relação. Predicados devem ser específicos ("interage_com", "prescreveu", "dependede").
➡️ TRANSIÇÃO: "Triplas são o esqueleto. Propriedades são a carne."

---

### Slide 29 — Propriedades e Labels

**Título**: Propriedades e Labels
**Objetivo**: Mostrar que nós e arestas podem ter propriedades.
**Conteúdo**:
- Nó: label (tipo) + propriedades (key-value)
- Aresta: tipo + propriedades (ex: data, fonte, confiança)
- Exemplo: Nó "Dipirona" {tipo: "Medicamento", classe: "analgésico"}
- Exemplo: Aresta "interage_com" {severidade: "moderada", fonte: "FDA"}
- Labeled Property Graph (LPG) — modelo do Neo4j

**Diagrama**: D15 — Nó e aresta com propriedades expandidas
**Animação**: Propriedades surgem ao redor do nó e aresta
**Imagem**: Nó com "cartões" de propriedade
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: No Labeled Property Graph (modelo do Neo4j), cada nó tem um LABEL (tipo, ex: "Medicamento") e PROPRIEDADES (key-value, ex: classe=analgésico). Cada aresta tem um TIPO (ex: "interage_com") e PROPriedades (ex: severidade=moderada, fonte=FDA, data=2024-01-15). Isso permite queries ricas: "todas as interações de severidade alta registradas pela FDA em 2024".
💡 ANALOGIA: Label é a "espécie" do nó (é um Medicamento? um Médico? um Paciente?). Propriedades são os "atributos" (qual a classe? qual a severidade?). Aresta com propriedades é como um verbo com advérbio: não só "interage", mas "interage FORTEMENTE segundo a FDA".
⚠️ ERROS COMUNS: Alunos sobrecarregam nós com propriedades que deveriam ser arestas. Se "Dipirona é da classe analgésicos", isso pode ser propriedade OU aresta para um nó "Analgésico". Regra: se a classe é um conceito com próprias relações, vire nó. Se é só um atributo, vire propriedade.
➡️ TRANSIÇÃO: "Como consultamos isso? Neo4j e Cypher."

---

### Slide 30 — Neo4j e Cypher

**Título**: Neo4j e Cypher
**Objetivo**: Introduzir a ferramenta dominante e sua linguagem.
**Conteúdo**:
- Neo4j: graph database nativa (Labeled Property Graph)
- Cypher: linguagem declarativa para grafos (como SQL para relacional)
- Alternativas: Memgraph (in-memory, mais rápido), ArangoDB (multi-modelo)
- RDF/SPARQL: outro paradigma (W3C, mais acadêmico)
- Foco do curso: Neo4j + Cypher (ecossistema, maturidade)

**Diagrama**: Logos Neo4j, Memgraph, ArangoDB
**Animação**: Logos aparecem
**Imagem**: Logos das ferramentas
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Neo4j é a graph database dominante. Usa o modelo Labeled Property Graph e tem a linguagem Cypher (declarativa, como SQL é para relacional). Existem alternativas: Memgraph (in-memory, mais rápido para certos casos), ArangoDB (multi-modelo: grafo + documento + chave-valor). Há também o paradigma RDF/SPARQL (W3C, mais acadêmico, usado em Linked Open Data). O curso foca em Neo4j + Cypher pela maturidade e ecossistema — é o que vocês encontrarão no mercado.
💡 ANALOGIA: Cypher é para grafos o que SQL é para tabelas. Você descreve o PADRÃO que quer encontrar, e o engine encontra. Não precisa escrever o algoritmo de travessia — só o que você quer.
➡️ TRANSIÇÃO: "Vamos ver Cypher na prática."

---

### Slide 31 — Query Cypher: Exemplo

**Título**: Query Cypher: "Co-autores de X"
**Objetivo**: Mostrar Cypher na prática.
**Conteúdo**:
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

**Diagrama**: D16 — Query + grafo visual resultante lado a lado
**Animação**: Query aparece, depois grafo resulta
**Imagem**: Código + grafo
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esta query encontra co-autores de "X". Lê-se: encontre um Author "X" que WROTE um Paper, que também foi WROTE por outro Author "b" (diferente de "a"). Retorne o nome de b e quantos papers co-escreveram, ordenado por prolificidade. O padrão visual de Cypher: nós entre parênteses `(a:Author)`, arestas entre colchetes e setas `-[r:WROTE]->`. Isso é muito mais legível que JOINs recursivos em SQL.
💡 ANALOGIA: MATCH é como um "ctrl+F" no grafo. Você descreve o padrão (Author → Paper ← Author) e o engine encontra todas as ocorrências. Em SQL, isso seria um self-join com subquery — bem mais opaco.
❓ PERGUNTA PARA A TURMA: "Como adaptariam para 'co-autores de co-autores' (2-hop)?" (Resposta: adicionar mais um nível de travessia `()-[:WROTE]->()<-[:WROTE]-()`)
⚠️ ERROS COMUNS: Alunos esquecem o `WHERE b <> a` e o próprio autor aparece como "co-autor". Sempre exclua o nó de origem.
➡️ TRANSIÇÃO: "Mas Cypher é só a linguagem. A modelagem é o que importa."

---

### Slide 32 — Modelagem para Raciocínio

**Título**: Modelagem para Raciocínio
**Objetivo**: Mostrar que a modelagem do grafo determina o que é possível raciocinar.
**Conteúdo**:
- Modelagem ingênua: nós genéricos, arestas vagas → queries fracas
- Modelagem rica: labels específicos, relações tipadas, propriedades → raciocínio multi-hop
- Pergunta de modelagem: "Quais perguntas o agente precisa responder?"
- Anti-pattern: modelar tudo como "RELATED_TO"
- Princípio: o grafo é o schema do raciocínio

**Diagrama**: D17 — Grafo mal modelado vs bem modelado
**Animação**: Lado esquerdo (ruim) aparece, depois direito (bom)
**Imagem**: Comparação de grafos
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A modelagem do grafo determina o que você consegue raciocinar. Se tudo é "RELATED_TO", você não consegue distinguir "interage_com" de "substitui" de "depende_de". A pergunta de modelagem é REVERSA: comece pelas perguntas que o agente precisa responder ("quais medicamentos interagem com X?", "qual médico prescreveu Y?"), e modele o grafo para suportar essas perguntas. O grafo é o SCHEMA do raciocínio.
💡 ANALOGIA: É como projetar um banco de dados relacional. Se você modela tudo em uma tabela genérica "Coisa", suas queries são fracas. Se você modela com tabelas específicas (Medicamento, Prescrição, Interação), suas queries são poderosas. No grafo, o princípio é o mesmo: labels e relações específicas = raciocínio poderoso.
⚠️ ERROS COMUNS: Alunos modelam o grafo "para parecer com a realidade" sem pensar nas queries. Modelagem orientada a queries: pergunte "quais perguntas?", depois modele. Itere quando as perguntas mudarem.
➡️ TRANSIÇÃO: "Mas como construímos um grafo a partir de texto? Extração de entidades."

---

### Slide 33 — Extração de Entidades com LLM (NER)

**Título**: Extração de Entidades com LLM (NER)
**Objetivo**: Mostrar como construir um KG a partir de texto não-estruturado.
**Conteúdo**:
- Texto → LLM com prompt de NER → entidades estruturadas
- Prompt: "Extraia todas as entidades do texto com tipo e propriedades"
- Output: `[{"name": "Dipirona", "type": "Medicamento"}, ...]`
- Desafio: entidades ambíguas, resolução de coreferência
- Ferramentas: LangChain LLMGraphTransformer, GLiNER, spaCy

**Diagrama**: D18 — Pipeline: Texto → LLM → Entidades → Nós do grafo
**Animação**: Pipeline flui da esquerda para direita
**Imagem**: Fluxo de extração
**Tempo**: 2 min

**Rodape**: LLM = Large Language Model — Modelo de Linguagem de Grande Escala  ·  NER = Named Entity Recognition — Reconhecimento de Entidades Nomeadas

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Named Entity Recognition (NER) é a extração de entidades de texto. Hoje, usamos LLMs com um prompt: "Extraia todas as entidades com tipo e propriedades." O output é JSON estruturado. O desafio é ambiguidade: "Dipirona" e "Dipirona sódica" são a mesma entidade? ("coreferência"). Outro desafio: entidades novas que não estão no schema. Ferramentas: LangChain LLMGraphTransformer (automatiza NER + relações), GLiNER (NER sem LLM, mais rápido), spaCy (clássico, regrado).
💡 ANALOGIA: NER é como um estudante de medicina lendo um prontuário e sublinhando os termos médicos (entidades). O LLM é esse estudante — mas escala para milhões de documentos.
⚠️ ERROS COMUNS: Alunos confiam cegamente no NER do LLM. LLMs alucinam entidades ("extraem" coisas que não estão no texto). Mitigação: schema restrito (só permita tipos pré-definidos) + validação + amostragem humana para auditoria.
➡️ TRANSIÇÃO: "Entidades são os nós. Relações são as arestas."

---

### Slide 34 — Extração de Relações com LLM

**Título**: Extração de Relações com LLM
**Objetivo**: Mostrar a etapa de extração de relações.
**Conteúdo**:
- Dadas 2 entidades → LLM classifica a relação
- Prompt: "Qual a relação entre A e B? Escolha: [interage_com, prescreveu, ...]"
- Output: triplas (sujeito, predicado, objeto)
- Desafio: alucinação de relações inexistentes
- Mitigação: schema restrito + validação + confiança na aresta

**Diagrama**: D19 — Pipeline: Entidades → LLM → Triplas → Arestas do grafo
**Animação**: Pipeline flui
**Imagem**: Extração de relações
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Dadas duas entidades, o LLM classifica a relação entre elas. O prompt oferece um schema restrito de relações: "Qual a relação entre A e B? Opções: [interage_com, prescreveu, contraindicado_para]." O output é uma tripla. O desafio crítico: ALUCINAÇÃO. O LLM pode inventar relações que não existem no texto. Mitigação: (1) schema restrito (não deixe o LLM inventar predicados); (2) validação (a relação está realmente no texto de origem?); (3) score de confiança na aresta (permanece, mas com flag de "baixa confiança").
💡 ANALOGIA: É como um jornalista verificando fontes. O LLM "reporta" a relação; você precisa de um "editor" que confirme com o texto original. Sem verificação, você publica notícia falsa no grafo.
⚠️ ERROS COMUNS: Alunos extraem relações sem validação e o grafo fica cheio de alucinações. O agente raciocina sobre relações falsas e dá respostas erradas — com confiança. Lineage (doc_id na aresta) permite auditar e corrigir.
➡️ TRANSIÇÃO: "Com entidades e relações, podemos raciocinar — inclusive inferir o implícito."

---

### Slide 35 — Inferência no Grafo

**Título**: Inferência no Grafo
**Objetivo**: Mostrar que grafos permitem raciocínio além do que está explícito.
**Conteúdo**:
- Explícito: "A interage com B" e "B interage com C"
- Inferido: "A pode interagir com C" (via transitividade — com cautela)
- Cypher: pathfinding (shortestPath, allShortestPaths)
- Pergunta multi-hop: "Todos os medicamentos que o paciente X toma indiretamente"
- LLM + grafo: LLM formula a query Cypher, grafo executa, LLM interpreta

**Diagrama**: D20 — Grafo com path destacado (A → B → C)
**Animação**: Path é desenhado nó a nó
**Imagem**: Grafo com caminho em destaque
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Grafos permitem raciocínio além do explícito. Se "A interage com B" e "B interage com C", podemos inferir (com cautela!) que "A pode interagir com C". Cypher tem pathfinding: `shortestPath`, `allShortestPaths` encontram caminhos entre nós. Isso responde perguntas multi-hop: "todos os medicamentos que o paciente X toma indiretamente (via interações)". O padrão moderno: LLM formula a query Cypher a partir da pergunta em linguagem natural, o grafo executa, e o LLM interpreta o resultado para o usuário.
💡 ANALOGIA: É como um detetive conectando pistas. Cada tripla é uma pista. O caminho A→B→C é a dedução. O LLM é o detetive que formula a investigação (query Cypher); o grafo é o quadro de investigação que executa a busca.
⚠️ ERROS COMUNS: Alunos inferem relações por transitividade sem cautela. "A interage com B" e "B interage com C" NÃO garante que "A interage com C" — interações não são estritamente transitivas. Use a inferência como HIPÓTESE a verificar, não como fato.
➡️ TRANSIÇÃO: "Antes de avançar, um exercício de modelagem."

---

### Slide 36 — Pergunta: Cardinalidade de um KG Empresarial

**Título**: Cardinalidade de um KG Empresarial
**Objetivo**: Engajar a turma com uma pergunta de modelagem.
**Conteúdo**:
- "Qual a cardinalidade típica de um KG empresarial? Quantas relações por entidade?"
- Pistas: depende do domínio (farmacêutica vs jurídico vs RH)
- Ordem de magnitude: 10k-100k entidades, 50k-500k relações
- Densidade: 5-15 relações por entidade (em média)
- Discussão em duplas (2 min)

**Diagrama**: Caixa de discussão (`etho-warning`)
**Animação**: Pergunta aparece com fade
**Imagem**: Ícone de discussão
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vamos discutir em duplas. Qual a cardinalidade típica? A resposta depende do domínio: farmacêutica tem muitas relações (interações medicamentosas), jurídico tem muitas referências cruzadas, RH tem menos. Ordem de magnitude típica: 10k-100k entidades, 50k-500k relações. Densidade: 5-15 relações por entidade em média. Isso importa para dimensionar infra (Neo4j lida com milhões de triplas confortavelmente).
💡 ANALOGIA: Cardinalidade é como o "tamanho" do cérebro do agente. Mais relações = mais capacidade de raciocínio, mas também mais custo de manutenção e mais risco de ruído.
❓ PERGUNTA PARA A TURMA: "Para o domínio de vocês: estimem entidades e relações." (2 min em duplas — depois compartilhar 2-3 estimativas)
⚠️ ERROS COMUNS: Alunos subestimam cardinalidade e ficam surpresos com o volume. Para um corpus de 50k documentos, espere 100k+ entidades e 500k+ relações. Dimensione infra para isso.
➡️ TRANSIÇÃO: "Intervalo. Depois: GraphRAG — a técnica que une knowledge graph e RAG."
