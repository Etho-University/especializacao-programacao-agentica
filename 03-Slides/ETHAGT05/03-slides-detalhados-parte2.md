# ETHAGT05 — Slides Detalhados + Notas do Professor (Parte 2: Slides 36-70)

> Universidade Etho · Especialização em Programação Agêntica
> Cada slide contém: título, objetivo, conteúdo, notas do professor, diagrama, animação, imagem, tempo.

---

## SEÇÃO D — Gerenciamento de Contexto (continuação · Slides 36-40)

---

### Slide 36 — Diagrama: Eviction Flow

**Título**: Eviction Flow — Decisão de Retenção
**Objetivo**: Visualizar o fluxo de decisão de eviction.
**Conteúdo**:
- Novo evento → `score = relevance × decay(age)`
- `score > threshold`? → manter na memória
- Entidade crítica? (ex.: pagamento) → decay lento, manter mais tempo
- Recall frequente? → aumenta score (reforço)
- Caso contrário → arquivar / apagar

**Diagrama**: `12-Diagrams/ETHAGT05/eviction-flow.mmd`
**Animação**: Fluxo step-by-step (evento → score → decisão)
**Imagem**: Diagrama mermaid renderizado
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vejam o fluxo. Cada evento recebe um score: `score = relevance × decay(age)`. Relevance é a importância semântica (ex.: um pagamento tem alta relevance; uma menção trivial tem baixa). Decay é uma função de decaimento — quanto mais velho, menor o score. Se score > threshold, mantém. Se não, verifica se é entidade crítica (pagamento, contrato, prazo) — se for, decay lento, mantém mais tempo. Recall frequente aumenta o score (reforço). Caso contrário, arquiva ou apaga. Esta é a base das políticas de eviction em produção (MemGPT, Zep, A-MEM).
💡 ANALOGIA: É como o algoritmo do Facebook/Instagram. Nem todo post fica no seu feed para sempre. O algoritmo calcula: relevância (você interagiu?), recência (é novo?), e frequência (você sempre engaja com este autor?). O eviction flow faz isso para memória de agente.
➡️ TRANSIÇÃO: "Há uma abordagem ainda mais sofisticada: entity-centric memory."

---

### Slide 37 — Estratégia 4: Entity-Centric Memory (MemGPT, Zep)

**Título**: Estratégia 4 — Entity-Centric Memory
**Objetivo**: Apresentar a abordagem de memória centrada em entidades.
**Conteúdo**:
- Em vez de uma lista de mensagens, **organizar memória por entidade**
- Cada entidade (usuário, projeto, tarefa) tem seu próprio "perfil" de memória
- O modelo decide quando **page-in** (carregar) e **page-out** (descarregar) entidades
- **MemGPT**: self-editing memory — o modelo atualiza suas próprias notas
- **Zep**: memória de longo prazo com graph + vector
- **Vantagem**: contexto sempre relevante à entidade ativa

**Diagrama**: Entidades como "pastas" de memória com page-in/page-out
**Animação**: Entidade ativa é "page-in" para a context window
**Imagem**: Agente no centro, entidades como pastas, setas de page-in/out
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Entity-centric memory é a abordagem mais sofisticada. Em vez de tratar a memória como uma lista linear de mensagens, você organiza por entidade: "usuário", "projeto X", "tarefa Y", "empresa Z". Cada entidade tem seu próprio perfil/notes. O modelo decide (via function calls) qual entidade está ativa e faz page-in (carrega para a context window) e page-out (descarrega para o disco). Isso é exatamente a ideia do MemGPT (self-editing memory) e do Zep (memória de longo prazo com graph + vector). A vantagem: o contexto é sempre relevante à entidade ativa — você não polui a context window com entidades irrelevantes.
💡 ANALOGIA: É como organizar arquivos por cliente em vez de por data. Se você está trabalhando com o cliente X, você abre a pasta do cliente X (page-in). Não precisa de pastas dos clientes Y e Z abertas ao mesmo tempo (page-out). Quando muda de cliente, troca de pasta.
⚠️ ERROS COMUNS: Alunos acham que entity-centric é "vector DB". Não — entity-centric é uma forma de ORGANIZAR a memória (por entidade). Vector DB é um storage. Você pode ter entity-centric memory usando vector DB como backend.
➡️ TRANSIÇÃO: "Mas nem tudo deve ser memória vetorial. Vamos ser críticos."

---

### Slide 38 — Quando Memória Vetorial é Pior que Relacional

**Título**: Quando Vector DB é Pior que Relacional
**Objetivo**: Ser crítico — nem tudo deve ser vector DB.
**Conteúdo**:
- **Vector DB é ótimo para**: recall por significado, fuzzy matching, "mais ou menos"
- **Vector DB é péssimo para**: exact match, ordenação temporal, agregação, joins
- **Exemplos onde relacional ganha**:
  - "Todos os eventos do usuário X no mês Y" → SQL (WHERE + ORDER BY)
  - "Qual o saldo atual?" → KB relacional (não embedding)
  - "Listar entidades do tipo 'projeto'" → tabela (não similaridade)
- **Regra**: vector para recall semântico, relacional para fatos estruturados, KG para relações

**Diagrama**: 3 colunas: Vector DB | Relacional | Knowledge Graph — com casos de uso
**Animação**: Colunas aparecem sequencialmente
**Imagem**: 3 ícones (vetor, tabela, grafo) com casos
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vector DB virou hype — todo mundo quer usar. Mas vector DB é uma ferramenta, não a solução universal. Vector DB é ótimo para recall semântico: "o que na minha memória se parece com X?". É péssimo para exact match, ordenação temporal, agregação, e joins. Para "todos os eventos do usuário X no mês Y", SQL é muito mais rápido e preciso. Para "qual o saldo atual?", KB relacional é correto — não embedding. Para "quem trabalha com Python e está livre na semana 20?", Knowledge Graph (query multi-hop). A regra: vector para recall semântico, relacional para fatos estruturados, KG para relações. Use o tool certo para o job.
💡 ANALOGIA: É como ferramentas. Martelo é ótimo para pregar, péssimo para aparafusar. Vector DB é ótimo para similaridade, péssimo para ordenação. Não use martelo para parafuso.
❓ PERGUNTA PARA A TURMA: "Citem um caso onde vector DB seria a escolha ERRADA." (Resposta: saldo bancário, lista de usuários, agregações temporais, anything que precise de exatidão.)
⚠️ ERROS COMUNS: Alunos colocam TUDO no vector DB. "Vou fazer vector search para verificar se o usuário existe." Não — isso é exact match, use tabela. Vector search é para "quais usuários são parecidos com X".
➡️ TRANSIÇÃO: "Vamos praticar isso com um exercício."

---

### Slide 39 — Exercício: Política de Eviction

**Título**: Exercício — Política de Eviction
**Objetivo**: Praticar o design de uma política de eviction.
**Conteúdo**:
- **Cenário**: assistente pessoal com 1 ano de interações (~365 conversas)
- **Em trios**: escrever política de eviction combinando relevância e idade
- **Exemplo**: "eventos com > 6 meses e score < 0.5 são arquivados"
- **Considerar**: entidades críticas (pagamentos, prazos), frequência de recall, PII
- 3 min discussão, 1 min compartilhar

**Diagrama**: Template de política de eviction
**Animação**: Template aparece
**Imagem**: Caixa amarela (`etho-warning`) com template
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Hora de praticar. Em trios, 3 minutos. Vocês estão projetando a memória de um assistente pessoal que acumulou 1 ano de interações diárias — 365 conversas. Escrevam uma política de eviction. Usem o template: `score = ___ × relevance + ___ × recency + ___ × frequency`, threshold, entidades críticas, TTL para PII. Considerem: pagamentos e prazos duram mais? Recall frequente aumenta score? Dados sensíveis têm TTL menor? Depois de 3 minutos, peçam 1-2 trios para compartilhar.
💡 ANALOGIA: É como decidir o que guardar na geladeira. Alguns itens duram semanas (conservas), outros dias (verduras), outros horas (comida quente). Você precisa de uma política — não dá para tratar tudo igual.
❓ PERGUNTA PARA A TURMA: "Quais entidades vocês classificariam como críticas?" (Resposta típica: pagamentos, contratos, prazos, dados de saúde, decisões importantes.)
⚠️ ERROS COMUNS: Trios esquecem PII. Regra: PII deve ter TTL máximo — mesmo que relevante, expira por compliance (LGPD/GDPR).
➡️ TRANSIÇÃO: "Gestão de contexto resolve o curto prazo. Vamos ao longo prazo."

---

### Slide 40 — [Transição] De Contexto para Recall

**Título**: De Contexto para Recall
**Objetivo**: Transição da gestão de contexto para memória vetorial.
**Conteúdo**: "Gestão de contexto resolve o curto prazo. E o longo prazo?"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Setas: curto prazo (contexto) → longo prazo (vector DB)
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Até aqui falamos de DENTRO de uma sessão: janela deslizante, sumarização, eviction. Mas memória de longo prazo é ENTRE sessões — eventos de ontem, da semana passada, do mês passado. Para isso, precisamos de memória vetorial. Vamos à Seção E.
➡️ TRANSIÇÃO: "Memória vetorial para recall episódico."

---

## SEÇÃO E — Memória Vetorial para Recall (Slides 41-50 · 12 min)

---

### Slide 41 — [SEÇÃO] Memória Vetorial para Recall

**Título**: 4 — Memória Vetorial para Recall
**Objetivo**: Transição para memória episódica via embeddings.
**Conteúdo**: "4 — Memória Vetorial para Recall"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "4" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Início do bloco de memória vetorial. Vamos responder: como converter eventos em embeddings? Como recuperar por similaridade? Como filtrar por metadata? E o pipeline completo de recall episódico. No final, apresento o Lab 2.
➡️ TRANSIÇÃO: "Primeiro: como converter um evento em embedding."

---

### Slide 42 — Embedding de Eventos

**Título**: Embedding de Eventos
**Objetivo**: Mostrar como converter eventos em embeddings.
**Conteúdo**:
- Cada **evento** (mensagem, ação, observação) → texto → **embedding**
- **Embedding** = vetor de N dimensões (384, 768, 1536, 3072)
- **Modelos**: OpenAI text-embedding-3-small/large, Cohere, BGE, E5
- **Armazenar**: vector DB (Qdrant, Chroma, Pinecone, pgvector)
- **Metadata**: timestamp, user_id, session_id, type, entities
- Pipeline: `embed_event(event)` → `(vector, metadata)`

**Diagrama**: Evento → texto → embedding → vector DB
**Animação**: Pipeline step-by-step
**Imagem**: Fluxo: bolha (evento) → texto → vetor numérico → vector DB
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O primeiro passo da memória vetorial é converter cada evento em um embedding. Um evento pode ser uma mensagem do usuário, uma tool call, ou uma observation. Você converte o texto do evento em um vetor de N dimensões (384, 768, 1536 ou 3072, dependendo do modelo). Modelos comuns: OpenAI text-embedding-3-small (1536 dims, barato), OpenAI text-embedding-3-large (3072 dims, mais preciso), BGE (open-source), E5 (open-source). Você armazena o vetor + metadata (timestamp, user_id, session_id, type, entities) no vector DB. A metadata é crucial para filtering — veremos no Slide 44.
💡 ANALOGIA: É como catalogar um livro em uma biblioteca. O embedding é o "código de barras semântico" — captura o significado do livro. A metadata é a ficha catalográfica (autor, data, gênero). Para buscar por significado, usa o código de barras (vector search). Para filtrar por data/autor, usa a ficha (metadata).
⚠️ ERROS COMUNS: Alunos esquecem a metadata. Sem metadata, você só pode fazer vector search puro — não dá para filtrar por usuário, sessão, ou tempo. Regra: sempre armazene metadata junto com o embedding.
➡️ TRANSIÇÃO: "Com embeddings no vector DB, como recuperar?"

---

### Slide 43 — Recall por Similaridade Semântica

**Título**: Recall por Similaridade Semântica
**Objetivo**: Explicar como recuperar memórias relevantes.
**Conteúdo**:
- **Query**: converter pergunta atual em embedding
- **Buscar**: top-K eventos mais similares (cosine similarity)
- **Reinsertir**: colocar eventos recuperados no contexto do agente
- **Exemplo**: "como resolveu aquele bug de autenticação?" → recall de evento passado similar
- **Pós-recuperação**: nem sempre o mais similar é o mais útil → re-ranking

**Diagrama**: Query embedding → busca no vector DB → top-K → contexto
**Animação**: Query vira vetor, busca no DB, top-K destacados
**Imagem**: Vetor de query → vector DB → top-K bolhas destacadas → contexto
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Para recuperar memórias, você converte a query atual ("como resolveu aquele bug?") em embedding e busca no vector DB os top-K eventos mais similares por cosine similarity. Esses eventos recuperados são inseridos no contexto do agente — ele agora "lembra" do evento passado relevante. Exemplo: usuário pergunta "como resolveu aquele bug de autenticação?" → recall do evento "debugamos o JWT token expiry issue em 15/mar" → agente responde com base na memória recuperada. Mas: nem sempre o mais similar é o mais útil. Vector search é aproximado. Por isso precisamos de re-ranking (Slide 45).
💡 ANALOGIA: É como buscar no Google. Você digita uma query, o Google recupera milhões de páginas "similar", e ranqueia as top-10. No agente: query → vector search → top-K → contexto. Mas como o Google, às vezes o resultado #1 não é o melhor — por isso re-ranking.
❓ PERGUNTA PARA A TURMA: "Se o usuário pergunta 'lembra daquele deploy que falhou ontem?', o que recuperamos?" (Resposta: eventos com embedding similar a "deploy falhou", filtrados por timestamp = ontem.)
➡️ TRANSIÇÃO: "Mas vector search sozinho é insuficiente. Precisamos de metadata filtering."

---

### Slide 44 — Metadata Filtering

**Título**: Metadata Filtering
**Objetivo**: Mostrar como filtrar recall por metadata estruturada.
**Conteúdo**:
- **Vector search sozinho é insuficiente**: "aquela reunião de terça"
- **Metadata filter**: `session_id = X AND timestamp > Y AND type = "meeting"`
- **Combinação**: filter por metadata + rank por similaridade
- **Padrão**: pre-filter (filtra antes da busca) vs post-filter (filtra depois)
- **Vector DBs modernas** suportam hybrid search (vector + structured)

**Diagrama**: Pipeline: metadata filter → vector search → resultado filtrado
**Animação**: Filtro reduz o universo, depois vector search
**Imagem**: Funil: universo → filtro → sub-conjunto → vector search → top-K
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vector search puro não resolve tudo. Se o usuário pergunta "aquela reunião de terça", vector search sozinho retorna reuniões de qualquer dia, ordenadas por similaridade com "reunião". Você precisa FILTRAR por metadata (dia da semana = terça) ANTES de ranquear. Isso é hybrid search: metadata filter (estruturado) + vector search (semântico). A ordem importa: pre-filter (filtra o universo antes da busca) é mais eficiente que post-filter (filtra depois). Vector DBs modernas (Qdrant, Pinecone, pgvector) suportam hybrid search nativamente. Regra prática: sempre combine filter + rank. Raramente você quer só vector search puro.
💡 ANALOGIA: É como buscar um livro na biblioteca. Você não busca em todos os milhões de livros por similaridade. Você primeiro vai à seção "Ficção Científica" (metadata filter: gênero), depois busca por similaridade dentro dessa seção. Filter primeiro, rank depois.
⚠️ ERROS COMUNS: Alunos fazem vector search puro e depois filtram no código. Ineficiente — filtra milhões de vetores para descartar 99%. Regra: deixe o vector DB fazer o filter (pre-filter) para reduzir o universo antes da busca.
➡️ TRANSIÇÃO: "Mesmo com filter + vector, o top-K pode não ser o ideal. Precisamos de re-ranking."

---

### Slide 45 — Pós-Recuperação: Re-ranking

**Título**: Pós-Recuperação — Re-ranking
**Objetivo**: Explicar por que o top-K do vector DB não é suficiente.
**Conteúdo**:
- **Vector search é rápido mas impreciso** (aproximação)
- **Re-ranking**: modelo separado re-avuala os top-K resultados
- **Modelos**: Cohere Rerank, BGE Reranker, cross-encoder
- **Pipeline**: vector search (top 20) → re-ranker (top 5) → contexto
- **Trade-off**: re-ranking adiciona latência mas melhora precisão

**Diagrama**: Funil: 1000 candidatos → 20 (vector) → 5 (re-rank) → contexto
**Animação**: Funil estreita de 1000 → 20 → 5
**Imagem**: Funil de recuperação
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vector search usa approximate nearest neighbors (ANN) — é rápido mas impreciso. Os top-20 do vector DB podem incluir falsos positivos. Para melhorar a precisão, você adiciona um re-ranker: um modelo separado (cross-encoder) que re-avalia os top-20 e retorna os top-5 mais precisos. Modelos comuns: Cohere Rerank (API), BGE Reranker (open-source), cross-encoders em geral. O pipeline: vector search (top 20, rápido) → re-ranker (top 5, preciso) → contexto. O trade-off: re-ranking adiciona latência (~100-200ms) mas melhora significativamente a precisão. Para agentes de alta qualidade, vale a pena.
💡 ANALOGIA: É como contratar. Você faz uma triagem rápida (vector search: top 20 currículos). Depois faz entrevistas (re-ranking: top 5). A triagem é rápida mas imprecisa; as entrevistas são lentas mas precisas. Combine as duas.
⚠️ ERROS COMUNS: Alunos pulam o re-ranking para economizar latência. Regra: para agentes de produção, re-ranking melhora muito a qualidade do recall. A latência extra (~200ms) é justificável.
➡️ TRANSIÇÃO: "Vamos juntar tudo no pipeline completo."

---

### Slide 46 — Pipeline Completo de Recall

**Título**: Pipeline Completo de Recall Episódico
**Objetivo**: Visualizar o pipeline end-to-end de recall episódico.
**Conteúdo**:
- **1. Query atual** → embedding
- **2. Metadata filter** (user, session, time range)
- **3. Vector search** (top-K candidatos)
- **4. Re-ranking** (top-N final)
- **5. Inserção no contexto** do agente
- **6. Agente responde** com memória recuperada

**Diagrama**: Pipeline horizontal com 6 etapas
**Animação**: Etapas aparecem sequencialmente
**Imagem**: Pipeline horizontal (6 caixas conectadas)
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Este é o slide-chave da Seção E. O pipeline completo de recall episódico em 6 etapas. (1) Query atual é convertida em embedding. (2) Metadata filter reduz o universo (user_id, session_id, time range). (3) Vector search recupera top-K candidatos por similaridade. (4) Re-ranking refina para top-N mais precisos. (5) Os eventos recuperados são inseridos no contexto do agente. (6) O agente responde usando a memória recuperada. Este pipeline é a base do Lab 2 (Memória Episódica). Memorizem este fluxo — é o que vocês vão implementar.
💡 ANALOGIA: É como uma investigação policial. (1) Você tem uma pista (query). (2) Filtra suspeitos por região/perfil (metadata). (3) Busca por similaridade com o perfil (vector search). (4) Re-avalia os top suspeitos com mais detalhe (re-ranking). (5) Apresenta as evidências (inserção no contexto). (6) O detetive conclui (agente responde).
⚠️ ERROS COMUNS: Alunos pulam etapas. Regra: cada etapa tem um propósito. Filter sem vector perde semântica; vector sem filter é ineficiente; sem re-ranking perde precisão; sem inserção no contexto o agente não "vê" a memória.
➡️ TRANSIÇÃO: "Vamos comparar as opções de vector DB."

---

### Slide 47 — Qdrant/Chroma/Pinecone: Comparação

**Título**: Comparação de Vector DBs
**Objetivo**: Comparar as principais opções de vector DB.
**Conteúdo**:
- **Qdrant**: Rust, open-source, self-hosted ou cloud, alta performance
- **Chroma**: Python, easy setup, ideal para protótipos
- **Pinecone**: managed, serverless, escala automática
- **pgvector**: extensão PostgreSQL, unifica relacional + vetorial
- **Critério**: managed vs self-hosted, escala, custo, latência, hybrid search

**Diagrama**: Tabela comparativa
**Animação**: Colunas aparecem uma a uma
**Imagem**: Logos dos 4 vector DBs
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Quatro opções principais de vector DB. Qdrant: escrito em Rust, open-source, excelente performance, roda self-hosted ou na cloud deles. Ideal para quem quer controle. Chroma: Python-first, setup em 2 linhas, ideal para protótipos e Jupyter notebooks. Pinecone: managed serverless, você não gerencia infra, escala automática, paga por uso. pgvector: extensão do PostgreSQL, unifica relacional + vetorial em um só banco — ótimo para simplificar stack. A escolha: se você já tem Postgres, pgvector elimina um componente. Se quer simplicidade de protótipo, Chroma. Se quer performance e controle, Qdrant. Se quer zero-ops, Pinecone.
💡 ANALOGIA: É como escolher meio de hospedagem. Chroma é hostal (simples, rápido). Qdrant é Airbnb (controle, flexibilidade). Pinecone é hotel 5 estrelas (managed, caro). pgvector é morar com os pais (reutiliza o que já tem).
❓ PERGUNTA PARA A TURMA: "Se vocês já têm Postgres em produção, qual escolheriam?" (Resposta: pgvector — elimina um componente, unifica stack.)
➡️ TRANSIÇÃO: "Vocês vão implementar isso no Lab 2."

---

### Slide 48 — Lab 2: Memória Episódica

**Título**: Lab 2 — Memória Episódica
**Objetivo**: Apresentar o laboratório de memória episódica.
**Conteúdo**:
- **Lab 2** (5h): "Memória episódica"
- Agente recorda interações anteriores relevantes via recall vetorial
- **Comparar agente com e sem memória** em sessões espaçadas
- **Stack**: LangGraph + Qdrant + OpenAI embeddings
- **Referência**: `05-Labs/ETHAGT05/Lab2-Memoria-Episodica`

**Diagrama**: Arquitetura do lab
**Animação**: Componentes aparecem
**Imagem**: Arquitetura: Agente (LangGraph) + Qdrant + OpenAI
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: No Lab 2, vocês vão implementar o pipeline completo de recall episódico que vimos no Slide 46. Stack: LangGraph para o agente, Qdrant para o vector DB, OpenAI para embeddings e LLM. A entrega é um agente que recorda interações anteriores relevantes via recall vetorial, e uma comparação A/B: o mesmo agente COM memória vs SEM memória em sessões espaçadas. Vocês vão medir hit rate do recall, latência, e custo extra por interação. O objetivo é sentir a diferença: com memória, o agente é contextualmente consciente; sem, é amnésico.
💡 ANALOGIA: É como comparar um médico com prontuário (com memória) vs um médico sem prontuário (sem memória). O primeiro conhece seu histórico; o segundo pergunta tudo de novo. A qualidade do atendimento é drasticamente diferente.
➡️ TRANSIÇÃO: "Vamos praticar a escolha de estratégia com um exercício."

---

### Slide 49 — Pergunta: Embedding ou Metadata?

**Título**: Embedding ou Metadata?
**Objetivo**: Praticar a escolha entre recall semântico e filtro estruturado.
**Conteúdo**:
- "Se o usuário pergunta 'aquela reunião de terça' — embedding ou metadata?"
  - **Resposta**: ambos! Metadata filter (dia da semana) + vector search (tópico)
- "E se pergunta 'como configurar deploy?' — embedding ou metadata?"
  - **Resposta**: embedding (semântico) + filter por `type="procedural"`
- "E se pergunta 'qual o saldo da conta?' — embedding ou metadata?"
  - **Resposta**: nenhum! KB relacional, não vector DB
- Discussão aberta (2 min)

**Diagrama**: 3 cenários lado a lado
**Animação**: Cenários aparecem um a um
**Imagem**: 3 caixas com cenários e respostas
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vamos praticar. Três cenários. Para cada um, vocês votam: embedding, metadata, ambos, ou nenhum? (1) "Aquela reunião de terça" — resposta: AMBOS. Metadata (terça) + vector (reunião). (2) "Como configurar deploy?" — resposta: embedding (semântico) + filter por type procedural. (3) "Qual o saldo da conta?" — resposta: NENHUM. KB relacional, não vector DB. A lição: nem tudo é vector search. Saber quando usar filter, vector, ambos, ou nenhum é essencial.
💡 ANALOGIA: É como escolher a ferramenta de busca. Para "encontre aquele parágrafo sobre X", usa busca semântica. Para "liste todos os itens comprados ontem", usa SQL. Para "saldo atual", usa lookup direto. Cada caso tem a ferramenta certa.
❓ PERGUNTA PARA A TURMA: "Citem mais um caso de cada tipo." (Respostas variam — o objetivo é praticar a taxonomia.)
⚠️ ERROS COMUNS: Alunos querem usar vector search para tudo. Regra: vector search é para recall semântico. Para exact match, agregação, ou lookup transacional, use relacional.
➡️ TRANSIÇÃO: "Até aqui falamos de eventos isolados. Mas eventos acumulados viram conhecimento."

---

### Slide 50 — [Transição] De Episódica para Semântica

**Título**: De Episódica para Semântica
**Objetivo**: Transição de memória episódica para consolidação semântica.
**Conteúdo**: "Eventos acumulados viram conhecimento?"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Setas: eventos → consolidação → fatos
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Memória episódica acumula eventos. Mas eventos não são conhecimento — são dados. Conhecimento surge quando você consolida: agrupa eventos relacionados, extrai fatos, remove redundância. Vamos à Seção F: consolidação e knowledge graphs.
➡️ TRANSIÇÃO: "Consolidação: como eventos viram fatos."

---

## SEÇÃO F — Memória Semântica e Grafos (Slides 51-57 · 8 min)

---

### Slide 51 — [SEÇÃO] Memória Semântica e Grafos

**Título**: 5 — Memória Semântica e Grafos
**Objetivo**: Transição para consolidação e knowledge graphs.
**Conteúdo**: "5 — Memória Semântica e Grafos"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "5" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Início do bloco de memória semântica. Vamos ver: como eventos episódicos viram fatos semânticos (consolidação)? Quando promover uma memória? Knowledge graph como memória estruturada. E o caso canônico: Generative Agents de Smallville.
➡️ TRANSIÇÃO: "Primeiro: o processo de consolidação."

---

### Slide 52 — Consolidação: Episódica → Semântica

**Título**: Consolidação — Episódica → Semântica
**Objetivo**: Mostrar como eventos episódicos viram fatos semânticos.
**Conteúdo**:
- **Consolidação**: processo de extrair fatos de eventos acumulados
- **Analogia biológica**: consolidação da memória durante o sono
- Em agentes: processo **offline ou em batch** que:
  1. Agrupa eventos relacionados
  2. Extrai fatos consolidados
  3. Remove redundância
  4. Promove para KB semântica
- **Exemplo**: 5 eventos "João perguntou sobre Python" → fato "João é desenvolvedor Python"

**Diagrama**: Eventos episódicos → processo de consolidação → fatos semânticos
**Animação**: Eventos convergem para fatos
**Imagem**: Múltiplos eventos → seta de consolidação → 1-2 fatos
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Consolidação é o processo que transforma eventos em fatos. Biologicamente, acontece durante o sono — o cérebro revisa o dia, agrupa experiências, e consolida em memórias de longo prazo. Em agentes, é um processo offline (ou em batch) que: (1) agrupa eventos relacionados (ex.: todas as interações com João sobre Python); (2) extrai fatos consolidados ("João é dev Python"); (3) remove redundância (não precisa de 5 eventos, 1 fato basta); (4) promove para a KB semântica. Exemplo: 5 eventos episódicos ("João perguntou sobre decorators", "João pediu ajuda com asyncio", "João compartilhou repo de FastAPI") → 1 fato semântico ("João é dev Python, nível intermediário-avançado, interessado em web dev").
💡 ANALOGIA: É como um editor que lê 100 reportagens sobre um tema e escreve 1 artigo de síntese. As 100 reportagens são eventos; o artigo é o fato consolidado. Você arquiva as reportagens (episódica) mas consulta o artigo (semântica) para o resumo.
⚠️ ERROS COMUNS: Alunos consolidam tudo imediatamente. Regra: consolidação precisa de massa crítica — espere acumular eventos suficientes (ex.: 3-5 ocorrências) antes de promover a fato.
➡️ TRANSIÇÃO: "Mas quando exatamente devemos promover?"

---

### Slide 53 — Quando Promover uma Memória?

**Título**: Quando Promover uma Memória?
**Objetivo**: Definir critérios para consolidação.
**Conteúdo**:
- Nem todo evento vira fato — **critérios de promoção**:
  - **Frequência**: evento recorrente (múltiplas ocorrências)
  - **Confiança**: fonte confiável ou confirmado múltiplas vezes
  - **Estabilidade**: fato não muda frequentemente
  - **Utilidade**: fato será relevante em sessões futuras
- **Quando NÃO promover**:
  - Eventos únicos e sem valor futuro
  - Fatos voláteis (saldo bancário, status de tarefa)
  - Informação sensível (PII desnecessária)

**Diagrama**: Checklist de critérios de promoção
**Animação**: Checklist aparece item por item
**Imagem**: Lista de verificação com 4 critérios
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Nem todo evento merece virar fato. Critérios de promoção: (1) Frequência — se aconteceu múltiplas vezes, é padrão, vira fato. (2) Confiança — fonte confiável (o próprio usuário disse) ou confirmado múltiplas vezes (3 eventos independentes). (3) Estabilidade — o fato não muda frequentemente. "João é dev Python" é estável; "saldo da conta" é volátil (não promova). (4) Utilidade — o fato será relevante em sessões futuras. Quando NÃO promover: eventos únicos sem valor futuro, fatos voláteis, e PII desnecessária (não consolide "João ganha R$X" sem consentimento).
💡 ANALOGIA: É como decidir o que vai para a Wikipedia. Nem tudo merece artigo. A Wikipedia tem critérios: notoriedade, fontes confiáveis, estabilidade. A consolidação de memória tem critérios análogos: frequência, confiança, estabilidade, utilidade.
⚠️ ERROS COMUNS: Alunos promovem fatos voláteis ("saldo da conta = R$1000"). Regra: saldo muda a cada transação. Promover é desperdício — mantenha como lookup relacional, não como fato semântico.
➡️ TRANSIÇÃO: "Quando os fatos têm relações entre si, knowledge graph é a estrutura ideal."

---

### Slide 54 — Knowledge Graph como Memória

**Título**: Knowledge Graph como Memória
**Objetivo**: Apresentar KG como camada de memória estruturada.
**Conteúdo**:
- **KG** = grafo de entidades + relações + atributos
- **Exemplo**: (João) --[trabalha_em]--> (Projeto X) --[usa]--> (Python)
- **Vantagens**: consulta estruturada, raciocínio multi-hop, explicitação de relações
- **Integração com LLM**: GraphRAG, Cypher + LLM, text-to-graph
- Profundidade em **ETHAGT07** — Knowledge Graphs para Agentes

**Diagrama**: Mini knowledge graph com 5 nós e relações
**Animação**: Nós e arestas aparecem
**Imagem**: Grafo com 5 nós (João, Projeto X, Python, Sprint 20, Backend) e arestas rotuladas
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Knowledge graph é uma estrutura poderosa para memória semântica quando os fatos têm RELAÇÕES. Um KG armazena triplas: (entidade) --[relação]--> (entidade). Exemplo: (João) --[trabalha_em]--> (Projeto X) --[usa]--> (Python) --[é_tipo_de]--> (Backend). Vantagens: (1) consulta estruturada — "quem trabalha com Python?" é uma query direta; (2) raciocínio multi-hop — "quem trabalha com Python e está livre na semana 20?" percorre 2 hops; (3) explicitação de relações que vector DB não captura. Integração com LLM: GraphRAG (recuperação via grafo), Cypher + LLM (text-to-query), text-to-graph (LLM extrai triplas de texto). Vamos aprofundar em ETHAGT07.
💡 ANALOGIA: É como um organograma de empresa. Mostra quem reporta para quem, quem está em qual time, quem tem qual skill. Você pode responder "quem pode cobrir férias do João?" percorrendo o grafo. Vector DB não faz isso — só encontra "pessoas parecidas com João".
⚠️ ERROS COMUNS: Alunos querem usar KG para tudo. Regra: KG é para fatos com RELAÇÕES estruturadas. Se os fatos são isolados ("João gosta de Python"), tabela basta. Se têm relações ("João trabalha no projeto X que usa Python"), KG vale a pena.
➡️ TRANSIÇÃO: "Vamos ver um exemplo concreto de consolidação."

---

### Slide 55 — Exemplo: De Evento para Fato

**Título**: Exemplo — De Evento para Fato
**Objetivo**: Mostrar um exemplo concreto de consolidação.
**Conteúdo**:
- **Eventos episódicos** (vector DB):
  - "João perguntou sobre decorators em Python" (12/jan)
  - "João pediu ajuda com asyncio" (25/jan)
  - "João compartilhou repositório de FastAPI" (03/fev)
- **Consolidação** → **Fato semântico** (KB):
  - "João é desenvolvedor Python (nível intermediário-avançado)"
  - Interesses: decorators, asyncio, FastAPI
- **Ação**: agente agora *sabe* quem é João sem precisar recall de cada evento

**Diagrama**: 3 eventos → seta de consolidação → 1 perfil semântico
**Animação**: Eventos convergem para 1 perfil
**Imagem**: 3 balões de eventos → seta → 1 ícone de perfil
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Exemplo concreto. Vector DB tem 3 eventos sobre João: perguntou sobre decorators (12/jan), pediu ajuda com asyncio (25/jan), compartilhou repo de FastAPI (03/fev). A consolidação agrupa esses 3 eventos, extrai o padrão (João trabalha com Python, especificamente async web), e promove para a KB semântica: "João é dev Python, nível intermediário-avançado, interessado em decorators, asyncio, FastAPI". Agora o agente SABE quem é João sem precisar recall de cada evento. Quando um novo usuário pergunta "João está disponível para um projeto Python?", o agente consulta a KB e responde com base no perfil consolidado.
💡 ANALOGIA: É como um RH que lê 3 avaliações de performance de um funcionário e escreve 1 perfil sintético. As avaliações individuais ficam arquivadas (episódica); o perfil é a referência (semântica). Para decisões futuras (promoção, transferência), o RH consulta o perfil, não as 3 avaliações.
➡️ TRANSIÇÃO: "O caso canônico de memória em agentes é o Generative Agents."

---

### Slide 56 — Generative Agents: Memória de Smallville

**Título**: Generative Agents — Memória de Smallville
**Objetivo**: Mostrar o caso canônico de memória em agentes.
**Conteúdo**:
- **Park et al.** (arXiv:2304.03442): 25 agentes em Smallville
- Cada agente tem:
  - **Memory stream**: log de observações com timestamp
  - **Retrieval**: por recência + importância + relevância
  - **Reflection**: consolida eventos em insights de alto nível
- **Resultado**: agentes "lembram", planejam, socializam de forma emergente
- **Lição**: a arquitetura de memória *é* a identidade do agente

**Diagrama**: Memory stream de um agente de Smallville
**Animação**: Stream aparece com observações e scores
**Imagem**: Timeline de observações com scores (recency, importance, relevance)
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Generative Agents (Park et al., 2023) é o caso canônico de memória em agentes. 25 agentes virtuais em uma cidade chamada Smallville. Cada agente tem um memory stream — um log de observações com timestamp. A recuperação combina 3 fatores: recência (mais recente = maior peso), importância (definida por um prompt ao LLM: "quão importante é esta observação?"), e relevância (similaridade semântica com a situação atual). Além disso, reflection: periodicamente, o agente consolida eventos em insights de alto nível ("gosto de Klaus porque sempre me ajuda com projetos"). O resultado: agentes que lembram, planejam, e socializam de forma emergente — sem script. A lição profunda: a arquitetura de memória é a IDENTIDADE do agente. Troque a memória, troque o agente.
💡 ANALOGIA: É como a memória de uma pessoa. Suas experiências moldam quem você é. Dois gêmeos com experiências diferentes se tornam pessoas diferentes. Em Smallville, dois agentes com memory streams diferentes têm comportamentos diferentes.
❓ PERGUNTA PARA A TURMA: "A arquitetura de memória é a identidade do agente? Concordam?" (Discussão: sim — a memória molda decisões, preferências, comportamento social.)
⚠️ ERROS COMUNS: Alunos acham que Generative Agents é "vector DB". Não — é uma arquitetura completa (memory stream + retrieval scoreado + reflection). Vector DB é só o storage.
➡️ TRANSIÇÃO: "Vamos conectar com o próximo módulo."

---

### Slide 57 — Integração com KG (Preview ETHAGT07)

**Título**: Integração com Knowledge Graph (Preview ETHAGT07)
**Objetivo**: Conectar com o próximo módulo de Knowledge Graphs.
**Conteúdo**:
- **ETHAGT07** aprofunda: GraphRAG, ontologias, raciocínio multi-hop
- **Memória semântica + KG** = raciocínio estruturado de longo prazo
- **Exemplo**: "Quem trabalha com Python e está livre na semana 20?" → query no KG
- **Padrão**: vector DB para recall + KG para raciocínio + relacional para fatos transacionais

**Diagrama**: 3 camadas: Vector DB | Knowledge Graph | Relacional
**Animação**: Camadas aparecem
**Imagem**: 3 camadas empilhadas com casos de uso
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: ETHAGT07 vai aprofundar Knowledge Graphs para agentes — GraphRAG, ontologias, raciocínio multi-hop. A ideia: memória semântica + KG = raciocínio estruturado de longo prazo. Exemplo: "Quem trabalha com Python e está livre na semana 20?" — uma query no KG percorre (pessoa → skill → Python) e (pessoa → disponibilidade → semana 20). Vector DB não faz isso; relacional faz mas é rígido. O padrão em produção: vector DB para recall episódico + KG para raciocínio semântico + relacional para fatos transacionais. Três camadas, três propósitos.
➡️ TRANSIÇÃO: "Vamos aos desafios de produção."

---

## SEÇÃO G — Produção: Consistência, Privacidade, Custo (Slides 58-63 · 8 min)

---

### Slide 58 — [SEÇÃO] Produção: Consistência, Privacidade, Custo

**Título**: 6 — Produção: Consistência, Privacidade, Custo
**Objetivo**: Transição para os desafios de produção.
**Conteúdo**: "6 — Produção: Consistência, Privacidade, Custo"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "6" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Início do bloco de produção. Vimos as 4 camadas, checkpointer, gestão de contexto, memória vetorial, consolidação. Mas colocar memória em produção traz desafios novos: consistência em multi-agente, PII e direito ao esquecimento, custo vs benefício, e observabilidade. Vamos um por um.
➡️ TRANSIÇÃO: "Primeiro: consistência quando múltiplos agentes compartilham memória."

---

### Slide 59 — Consistência em Multi-Agente

**Título**: Consistência em Multi-Agente
**Objetivo**: Mostrar os desafios de memória compartilhada entre agentes.
**Conteúdo**:
- Múltiplos agentes compartilham memória → **problemas de concorrência**
- **Race condition**: agente A lê fato, B atualiza, A usa fato desatualizado
- **Estratégias**:
  - **Eventual consistency**: aceitar defasagem (mais simples)
  - **Strong consistency**: locks / transações (mais caro)
  - **Event sourcing**: log de mudanças (auditável)
- **Padrão**: cada agente tem memória local + memória compartilhada via message bus

**Diagrama**: 3 agentes + memória compartilhada com locks
**Animação**: Race condition aparece (A lê, B atualiza, A usa desatualizado)
**Imagem**: Sequence diagram com race condition
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Em sistemas multi-agente, a memória é frequentemente compartilhada — e isso traz problemas de concorrência. Race condition: agente A lê um fato ("saldo = 100"), agente B atualiza ("saldo = 50"), e A usa o fato desatualizado ("saldo = 100") — erro. Estratégias: (1) Eventual consistency — aceitar defasagem, mais simples, padrão em muitos sistemas; (2) Strong consistency — locks e transações, mais caro mas correto; (3) Event sourcing — log de mudanças, auditável, permite replay. O padrão em produção: cada agente tem memória LOCAL (rápida, privada) + memória COMPARTILHADA via message bus (eventualmente consistente). Vamos aprofundar em ETHAGT09 (Multi-Agent) e ETHAGT14 (Escalabilidade).
💡 ANALOGIA: É como 3 editores editando o mesmo Google Doc simultaneamente. Sem sincronização, um sobrescreve o outro. Com (eventual consistency), cada um vê a versão do outro eventualmente. Com (strong consistency, locks), só um edita por vez. Com (event sourcing), há um log de quem mudou o quê.
⚠️ ERROS COMUNS: Alunos assumem que memória compartilhada é sempre consistente. Regra: concorrência SEMPRE traz race conditions. Planeje a estratégia de consistência desde o design.
➡️ TRANSIÇÃO: "Mas consistência é só o começo. E privacidade?"

---

### Slide 60 — PII em Memória: Redação e Retenção

**Título**: PII em Memória — Redação e Retenção
**Objetivo**: Lidar com dados pessoais em memória de longo prazo.
**Conteúdo**:
- Memória acumula PII: nomes, emails, preferências, histórico
- **Riscos**: vazamento, profiling, inferência indevida
- **Redação**: mascarar PII antes de armazenar (NER + replacement)
- **Retenção**: definir TTL por tipo de dado (ex.: conversas = 90 dias, perfil = até consentimento)
- **Compliance**: LGPD/GDPR exigem minimização de dados

**Diagrama**: Pipeline: evento → NER → redação → armazenamento seguro
**Animação**: PII é detectada e mascarada no pipeline
**Imagem**: Pipeline com etapa de "redação NER"
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Memória de longo prazo acumula PII — nomes, emails, preferências, histórico de conversas. Riscos: vazamento (se o vector DB for comprometido), profiling (inferência indevida de características), e inferência (deduzir informações não explicitamente armazenadas). Estratégias: (1) Redação — detectar PII com NER (Named Entity Recognition) e mascarar antes de armazenar. Ex.: "João Silva (CPF 123.456.789-00)" → "USUARIO_42 (CPF_REDACTED)". (2) Retenção — definir TTL por tipo: conversas efêmeras 90 dias, perfil do usuário até consentimento, dados sensíveis nunca sem consentimento explícito. (3) Compliance — LGPD (Brasil) e GDPR (Europa) exigem minimização de dados. Não armazene o que não precisa.
💡 ANALOGIA: É como um médico guardando prontuários. Ele não anota tudo o que você disse — anota o relevante. E tem regras de retenção (prontuários por X anos, depois destroem). E protege com senha. A memória do agente precisa do mesmo cuidado.
⚠️ ERROS COMUNS: Alunos armazenam PII em texto claro sem redação. Regra: redija PII ANTES de armazenar. Se você não precisa do CPF explícito, armazene um hash ou "USER_X".
➡️ TRANSIÇÃO: "E quando o usuário pede para ser esquecido?"

---

### Slide 61 — Direito ao Esquecimento em Memória Vetorial

**Título**: Direito ao Esquecimento em Vector DB
**Objetivo**: Discutir como implementar "esquecer" em vector DB.
**Conteúdo**:
- **Desafio**: "esquecer tudo sobre o usuário X" em vector DB
- **Problema**: embeddings não são reversíveis — não dá para "apagar" um fato de um embedding
- **Estratégias**:
  - **Delete por metadata**: `WHERE user_id = X` (se metadata foi armazenada)
  - **Re-embed**: remover evento e re-gerar sumários consolidados
  - **Cryptographic erasure**: encriptar por usuário, destruir chave
- **Pergunta**: *Como implementar direito ao esquecimento em memória vetorial?*

**Diagrama**: 3 estratégias lado a lado
**Animação**: Estratégias aparecem
**Imagem**: 3 colunas com as estratégias
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O "direito ao esquecimento" (LGPD Art. 18, GDPR Art. 17) é um desafio em memória vetorial. O problema: embeddings não são reversíveis — você não pode "apagar" um fato de dentro de um embedding consolidado. Estratégias: (1) Delete por metadata — se você armazenou `user_id` como metadata, faz `DELETE WHERE user_id = X`. Rápido, mas não cobre sumários consolidados que já incorporaram a informação do usuário. (2) Re-embed — remove eventos do usuário e re-gera sumários consolidados sem eles. Caro, mas consistente. (3) Cryptographic erasure — encripta os dados por usuário com uma chave única; para esquecer, destrói a chave. Instantâneo e criptograficamente seguro, mas requer planejamento desde o início. Nenhuma é perfeita; combine depende do caso.
💡 ANALOGIA: É como tentar "des-fazer" um bolo. Você misturou farinha, ovos, açúcar e assou. Não dá para tirar só o açúcar. Opções: (1) jogar o bolo fora (delete); (2) fazer um bolo novo sem açúcar (re-embed); (3) ter assado em formas separadas criptografadas e jogar a forma certa fora (cryptographic erasure).
❓ PERGUNTA PARA A TURMA: "Como vocês implementariam direito ao esquecimento?" (Resposta: depende — combine estratégias, planeje desde o início com metadata + cryptographic erasure.)
⚠️ ERROS COMUNS: Alunos acham que "apagar do vector DB" resolve. Não — se a informação foi consolidada em sumários ou fatos semânticos, ainda está lá, implícita. Re-embed ou cryptographic erasure são necessários.
➡️ TRANSIÇÃO: "E quando NÃO devemos memorizar?"

---

### Slide 62 — Custo de Memória vs Benefício

**Título**: Custo de Memória vs Benefício
**Objetivo**: Critério para decidir quando NÃO memorizar.
**Conteúdo**:
- Memória não é grátis: storage, embedding, recall, contexto adicional
- **Pergunta-chave**: "esta memória vai melhorar uma decisão futura?"
- **Quando NÃO memorizar**:
  - Eventos sem valor futuro ("qual a temperatura agora?")
  - Informação facilmente recalculável ("saldo atual")
  - Dados que mudam rápido demais para consolidar
  - Conteúdo sem consentimento do usuário
- **Regra**: melhor memória mínima e útil que memória máxima e ruidosa

**Diagrama**: Matriz custo × benefício de memória
**Animação**: Quadrantes aparecem
**Imagem**: Matriz 2x2 (custo baixo/alto × benefício baixo/alto)
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Memória tem custo: storage (você paga pelo volume), embedding (cada evento novo precisa de embedding), recall (cada recuperação custa latência e compute), e contexto adicional (mais memória no contexto = mais tokens = mais custo de LLM). A pergunta-chave: "esta memória vai melhorar uma decisão futura?" Se não, não memorize. Casos para NÃO memorizar: (1) Eventos sem valor futuro — "qual a temperatura agora?" não precisa de memória, é lookup. (2) Informação facilmente recalculável — "saldo atual" muda a cada transação, recalcule. (3) Dados voláteis — mudam rápido demais para consolidar. (4) Conteúdo sem consentimento — LGPD/GDPR. A regra de ouro: melhor memória MÍNIMA e ÚTIL que memória MÁXIMA e ruidosa. Menos é mais.
💡 ANALOGIA: É como guardar móveis. Você não guarda tudo — só o que vale a pena guardar. Guardar coisas inúteis custa espaço (storage), dificulta achar o útil (ruído no recall), e custa o aluguel do guarda-volumes. Memória de agente é igual.
❓ PERGUNTA PARA A TURMA: "Citem 3 casos onde NÃO vale a pena memorizar." (Respostas: temperatura atual, saldo, status de tarefa volátil, conversa trivial sem valor futuro.)
⚠️ ERROS COMUNS: Alunos memorizam tudo ("por via das dúvidas"). Regra: memória máxima é anti-pattern. Cura o que memoriza — priorize qualidade sobre quantidade.
➡️ TRANSIÇÃO: "E para fechar a Seção G: observabilidade de memória."

---

### Slide 63 — Observabilidade de Memória

**Título**: Observabilidade de Memória
**Objetivo**: Mostrar que memória precisa de observabilidade própria.
**Conteúdo**:
- Memória é um sistema — precisa de **monitoring**:
  - Quem acessou qual memória, quando?
  - **Hit rate** do recall (quantos recalls retornam algo útil?)
  - **Latência** do recall
  - Custo de storage vs custo de recall
  - **Drift**: a memória está desatualizada?
- **Ferramentas**: LangSmith (memory traces), dashboards custom, audit logs
- Profundidade em **ETHAGT12** — AgentOps

**Diagrama**: Dashboard de memória com métricas
**Animação**: Métricas aparecem
**Imagem**: Dashboard com gráficos (hit rate, latência, custo)
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Memória é um sistema como qualquer outro — precisa de observabilidade. O que monitorar: (1) Quem acessou qual memória, quando — auditabilidade, especialmente para PII. (2) Hit rate do recall — se 90% dos recalls retornam nada útil, seu pipeline está mal configurado. (3) Latência do recall — recall lento degrada a experiência. (4) Custo de storage vs custo de recall — às vezes é mais barato re-embed do que armazenar. (5) Drift — a memória está desatualizada? (ex.: "João trabalha no projeto X" mas João mudou de projeto). Ferramentas: LangSmith tem memory traces; você pode construir dashboards custom; e audit logs são essenciais para compliance. Vamos aprofundar em ETHAGT12 (AgentOps).
💡 ANALOGIA: É como o painel de um carro. Você não dirige no escuro — temperatura do motor, nível de combustível, velocidade. A memória do agente precisa do mesmo: hit rate, latência, drift. Sem isso, é caixa preta.
⚠️ ERROS COMUNS: Alunos colocam memória em produção sem observabilidade. Regra: se você não mede hit rate e latência, não sabe se sua memória está funcionando. Observabilidade desde o dia 1.
➡️ TRANSIÇÃO: "Vamos ao fechamento."

---

## SEÇÃO H — Fechamento (Slides 64-70 · 12 min)

---

### Slide 64 — Boas Práticas (DO)

**Título**: Boas Práticas de Memória (DO)
**Objetivo**: Checklist de boas práticas de memória.
**Conteúdo**:
- ✅ Comece com working memory + checkpointer (antes de vector DB)
- ✅ Modele estado serializável desde o dia 1
- ✅ Use `thread_id` consistente (conversa = thread)
- ✅ Versione o schema de estado (`schema_version`)
- ✅ Combine vector + metadata (não use só similaridade)
- ✅ Defina política de eviction desde o início
- ✅ Redação de PII antes de armazenar
- ✅ Observe a memória (hit rate, latência, drift)

**Diagrama**: Checklist verde (`etho-success`)
**Animação**: Itens aparecem um a um com checkmark
**Imagem**: Lista verde com ícones de checkmark
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Fechamento com boas práticas. (1) Comece com working + checkpointer — vector DB vem depois. (2) Modele estado serializável desde o dia 1 — não deixe para depois. (3) thread_id consistente — é a chave de continuidade. (4) Versione o schema — `schema_version: 1` desde o início. (5) Combine vector + metadata — hybrid search, nunca só vector. (6) Política de eviction desde o início — não deixe a memória crescer infinitamente. (7) Redação de PII antes de armazenar — compliance e segurança. (8) Observe a memória — hit rate, latência, drift. Estas 8 práticas são a fundação. Peçam exemplos da turma: qual delas eles já aplicam?
💡 ANALOGIA: É como os 10 mandamentos da memória de agentes. Sigam e terão sistemas robustos; ignorem e terão caos.
❓ PERGUNTA PARA A TURMA: "Qual destas práticas vocês já aplicam? Qual é a mais negligenciada?" (Discussão rápida.)
➡️ TRANSIÇÃO: "E o que NÃO fazer."

---

### Slide 65 — Anti-Patterns (DON'T)

**Título**: Anti-Patterns de Memória (DON'T)
**Objetivo**: Checklist do que NÃO fazer em memória.
**Conteúdo**:
- ❌ Encher context window até estourar (sem gestão ativa)
- ❌ Usar vector DB para tudo (quando relacional bastava)
- ❌ Não versionar schema de estado (quebra no resume)
- ❌ Armazenar PII sem redação
- ❌ Sem política de eviction (memória cresce infinitamente)
- ❌ Confiar cegamente no recall (sem re-ranking)
- ❌ Misturar memória de usuários diferentes (cross-contamination)
- ❌ Sem observabilidade de memória ("caixa preta")
- ❌ Promover tudo para semântica (sem critério de consolidação)

**Diagrama**: Checklist vermelho (`etho-danger`)
**Animação**: Itens aparecem com X
**Imagem**: Lista vermelha com ícones de X
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Anti-patterns. (1) Encher context window até estourar — sem gestão ativa, você terá erro 400 e qualidade degradada. (2) Vector DB para tudo — relacional é melhor para fatos estruturados. (3) Não versionar schema — quebra no resume quando você adiciona campos. (4) PII sem redação — risco legal e de segurança. (5) Sem eviction — memória cresce infinitamente, custo explode. (6) Confiar cegamente no recall — vector search é aproximado, sempre faça re-ranking. (7) Cross-contamination — misturar memória de usuários diferentes quebra privacidade. (8) Sem observabilidade — caixa preta, não sabe se funciona. (9) Promover tudo para semântica — sem critério, você terá fatos voláteis e ruidosos. Peçam exemplos da turma: qual destes eles já cometeram?
💡 ANALOGIA: É como a lista de "não faça" na cozinha. Não deixe a faca na pia, não corte na mão, não misture carne crua com vegetais. Na memória de agentes, os anti-patterns são equivalentes — parecem óbvios, mas todo mundo comete.
❓ PERGUNTA PARA A TURMA: "Qual destes anti-patterns vocês já cometeram?" (Discussão rápida — humor ajuda a fixar.)
➡️ TRANSIÇÃO: "Vamos resumir."

---

### Slide 66 — Resumo da Aula

**Título**: Resumo da Aula
**Objetivo**: Sintetizar os pontos-chave.
**Conteúdo**:
- **4 camadas de memória**: working (context window), episódica (vector DB), semântica (KB/KG), procedural (skills)
- **Checkpointer** = persistência de estado (Postgres/SQLite/Redis) → resume, replay, branching
- **Gerenciamento de contexto**: janela deslizante, sumarização em cascata, eviction por relevância, entity-centric
- **Memória vetorial**: embedding + metadata filter + re-ranking = recall episódico
- **Consolidação**: episódica → semântica (com critérios de promoção)
- **Produção**: consistência, PII, direito ao esquecimento, custo vs benefício, observabilidade
- **MemGPT** e **Generative Agents** como referências canônicas

**Diagrama**: 7 ícones com os pontos-chave
**Animação**: Ícones aparecem sequencialmente
**Imagem**: Grid de 7 ícones (camadas, banco, contexto, vetor, consolidação, produção, papers)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Resumo em 7 pontos. (1) 4 camadas de memória — working, episódica, semântica, procedural. Cada uma tem propósito, storage e padrão de recuperação distintos. (2) Checkpointer persiste estado entre sessões — Postgres/SQLite/Redis — habilitando resume, replay, branching. (3) Gestão de contexto dentro de uma sessão — janela deslizante, sumarização em cascata, eviction por relevância, entity-centric. (4) Memória vetorial é o pipeline de recall episódico: embedding + metadata filter + re-ranking. (5) Consolidação transforma eventos em fatos, com critérios (frequência, confiança, estabilidade, utilidade). (6) Produção traz desafios: consistência multi-agente, PII e direito ao esquecimento, custo vs benefício, observabilidade. (7) MemGPT e Generative Agents são as referências canônicas — leiam os papers.
💡 ANALOGIA: É como o resumo de um curso de arquitetura. Você aprende os tipos de fundação (4 camadas), como preservar (checkpointer), como gerenciar espaço (eviction), como catalogar (vector DB), como consolidar conhecimento (semântica), e como manter seguro (produção).
➡️ TRANSIÇÃO: "Vamos verificar a compreensão com o quiz."

---

### Slide 67 — Quiz: Pergunta 1

**Título**: Quiz — Pergunta 1
**Objetivo**: Verificar compreensão.
**Conteúdo**:
- "Qual tipo de memória é mais apropriado para 'o usuário prefere respostas em português'?"
- A) Working memory (context window)
- B) Memória episódica (vector DB)
- C) Memória semântica (KB / perfil)
- D) Memória procedural (skills)
- **Resposta**: C — é um fato estável sobre o usuário, não um evento

**Diagrama**: Quiz box com 4 opções
**Animação**: Opções aparecem; resposta destacada após clique
**Imagem**: Caixa amarela com pergunta e opções A/B/C/D
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Pergunta 1 do quiz. "Prefere respostas em português" é um fato estável sobre o usuário — não é um evento (episódica), não é uma skill (procedural), e não deve ser re-promptado a cada sessão (working). Resposta: C — memória semântica. Deixem a turma responder individualmente, sem consulta. Depois, revelem a resposta.
➡️ TRANSIÇÃO: "Pergunta 2."

---

### Slide 68 — Quiz: Pergunta 2

**Título**: Quiz — Pergunta 2
**Objetivo**: Verificar compreensão.
**Conteúdo**:
- "O que acontece se o schema de estado mudar e um checkpoint antigo for carregado?"
- A) Erro 500 e crash do agente
- B) O agente ignora campos novos e continua
- C) Depende — sem versionamento, quebra; com migração lazy, funciona
- D) O checkpointer reescreve o estado automaticamente
- **Resposta**: C — sem versionamento, campos novos podem causar erro; com migração lazy, o estado é convertido no load

**Diagrama**: Quiz box com 4 opções
**Animação**: Opções aparecem; resposta destacada
**Imagem**: Caixa amarela com pergunta e opções
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Pergunta 2 do quiz. Se o schema mudou (novo campo adicionado) e você carrega um checkpoint antigo, depende: sem versionamento, pode quebrar (KeyError, TypeError); com `schema_version` + migração lazy, o estado é convertido no load e funciona. Resposta: C. A lição: sempre versione o schema desde o dia 1.
➡️ TRANSIÇÃO: "Pergunta 3."

---

### Slide 69 — Quiz: Pergunta 3

**Título**: Quiz — Pergunta 3
**Objetivo**: Verificar compreensão.
**Conteúdo**:
- "Usuário pede: 'lembra daquela conversa sobre deploy na semana passada?' Qual estratégia de recall usar?"
- A) Apenas vector search (similaridade semântica com "deploy")
- B) Apenas metadata filter (timestamp da semana passada)
- C) Metadata filter (tempo) + vector search (tópico) + re-ranking
- D) Sumarização em cascata
- **Resposta**: C — combinar filtro temporal com busca semântica e re-ranking para precisão

**Diagrama**: Quiz box com 4 opções
**Animação**: Opções aparecem; resposta destacada
**Imagem**: Caixa amarela com pergunta e opções
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Pergunta 3 do quiz. A query tem componente temporal ("semana passada") e semântico ("deploy"). A estratégia correta é combinar: metadata filter (tempo) + vector search (tópico) + re-ranking. Resposta: C. Só vector (A) retorna conversas sobre deploy de qualquer época. Só metadata (B) retorna qualquer conversa da semana. Sumarização (D) é gestão de contexto, não recall. A lição: hybrid search é o padrão.
➡️ TRANSIÇÃO: "Vamos ao encerramento."

---

### Slide 70 — Conexão, Projeto e Q&A

**Título**: Conexão, Projeto e Q&A
**Objetivo**: Conectar com próximos módulos, apresentar projeto e encerrar.
**Conteúdo**:
- **Próximos módulos**:
  - ETHAGT06 — RAG Agêntico (memória + recuperação combinados)
  - ETHAGT07 — Knowledge Graphs (memória semântica aprofundada)
  - ETHAGT14 — Escalabilidade (memória em produção multi-tenant)
- **Projeto do módulo**: projetar memória de agente pessoal de longo prazo (4 camadas + ADR + política de privacidade/evicção)
- **Labs**: Lab 1 (Checkpointer em Postgres, 4h) · Lab 2 (Memória Episódica, 5h)
- **Leitura**: Packer et al. *MemGPT* (arXiv:2310.08560)
- "Perguntas?"
- Contato do professor

**Diagrama**: Logo Etho + fundo `etho-dark`
**Animação**: Fade in
**Imagem**: Logo Etho centralizado, fundo escuro
**Tempo**: 4 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Encerramento. Próximos módulos: ETHAGT06 (RAG Agêntico — memória + recuperação), ETHAGT07 (Knowledge Graphs — memória semântica aprofundada), ETHAGT14 (Escalabilidade — memória em multi-tenant). O projeto do módulo é projetar a memória de um agente pessoal de longo prazo com as 4 camadas, justificando trade-offs em um ADR e documentando política de privacidade/eviction. Dois labs: Lab 1 (Checkpointer em Postgres, 4h) e Lab 2 (Memória Episódica, 5h). Leitura recomendada: MemGPT (arXiv:2310.08560) e Generative Agents (arXiv:2304.03442). Q&A — deixem a turma perguntar. Se não houver perguntas, façam a pergunta inversa: "Qual camada de memória acharam menos clara?"
💡 ANALOGIA: É como o fim de um curso de arquitetura. Vocês agora têm as ferramentas para projetar sistemas de memória. A prática (projeto + labs) vai consolidar. A leitura (papers) vai aprofundar.
❓ PERGUNTA PARA A TURMA: "Perguntas?" (Se silêncio: "Qual parte foi menos clara?" ou "Qual tipo de memória vocês vão usar primeiro no trabalho?")
⚠️ ERROS COMUNS: Alunos saem sem ter clareza do projeto. Regra: confirmem prazos (Lab 1 = 1 semana, Lab 2 = 2 semanas, Projeto = 2 semanas) e critérios de avaliação antes de sair.
