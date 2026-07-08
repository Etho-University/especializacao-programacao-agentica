# ETHAGT06 — Slides Detalhados + Notas do Professor (Parte 2: Slides 45-85)

> Universidade Etho · Especialização em Programação Agêntica
> Cada slide contém: título, objetivo, conteúdo, notas do professor, diagrama, animação, imagem, tempo.

---

## SEÇÃO F — Agentic RAG (Slides 45-55 · 15 min)

---

### Slide 45 — [SEÇÃO] Agentic RAG

**Título**: 5 — Agentic RAG: O Agente Dirige Todo o Processo
**Objetivo**: Transição visual para o paradigma mais avançado.
**Conteúdo**: "5 — Agentic RAG: O Agente Dirige Todo o Processo"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "5" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O topo da escalada. Adaptive, CRAG e Self-RAG são pipelines com gates de decisão. Agentic RAG é diferente: não há pipeline predefinido. O AGENTE decide tudo — planeja as buscas, refina queries, decide quando parar. O loop do agente É o pipeline. Conexão com ETHAGT01: é o Augmented LLM com retrieval in-loop.
➡️ TRANSIÇÃO: "A ideia central."

---

### Slide 46 — A Ideia: Agente Dirige Todo o Processo

**Título**: O Agente Dirige Todo o Processo
**Objetivo**: Mostrar a diferença fundamental do Agentic RAG.
**Conteúdo**:
- Adaptive/CRAG/Self-RAG: pipeline fixo com gates de decisão
- **Agentic RAG**: o AGENTE decide tudo — planeja busca, refina queries, decide parar
- O agente tem tools de busca (web, interno, KG) e as chama como qualquer tool
- Não há pipeline predefinido — o loop do agente É o pipeline
- Conexão com ETHAGT01: é o Augmented LLM com retrieval in-loop

**Diagrama**: Pipeline fixo (gates) vs Loop de agente (D10)
**Animação**: Lado esquerdo (pipeline) aparece; depois lado direito (loop)
**Imagem**: Comparação pipeline vs loop
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A diferença fundamental. Adaptive, CRAG e Self-RAG são pipelines: você define os nós (retrieve, grade, generate) e os edges (condições). São determinísticos na estrutura. Agentic RAG é diferente: não há estrutura predefinida. O agente recebe a pergunta e decide, a cada iteração, o que fazer: buscar agora? refinar a query? combinar fontes? parar e responder? As tools de busca (search_internal, search_web, search_kg) são ferramentas como qualquer outra — o agente as chama quando decide.
💡 ANALOGIA: Adaptive/CRAG/Self-RAG são como receitas — passos predefinidos com variações. Agentic RAG é como um chef criando um prato novo: ele decide os ingredientes, a ordem, quando parar. Sem receita — só expertise e julgamento.
❓ PERGUNTA PARA A TURMA: "Qual o risco de Agentic RAG?" (resposta: loop infinito, custo imprevisível, menos controle — por isso max_steps é essencial)
⚠️ ERROS COMUNS: Alunos pulam direto para Agentic sem entender Adaptive/CRAG/Self-RAG. Anti-pattern. Comece simples.
➡️ TRANSIÇÃO: "O que o agente faz exatamente?"

---

### Slide 47 — Planeja Busca, Refina Queries, Decide Parar

**Título**: Capacidades do Agente RAG
**Objetivo**: Detalhar as capacidades do agente.
**Conteúdo**:
- **Planeja**: "Preciso buscar X, depois Y, depois combinar"
- **Refina queries**: "A busca por X retornou pouco — vou reformular"
- **Decide parar**: "Tenho informação suficiente para responder" ou "Preciso de mais um hop"
- max_steps como guardrail (lição de ETHAGT01)
- O agente raciocina sobre o QUE recuperou e o QUE ainda falta

**Diagrama**: Loop do agente com planejamento
**Animação**: Loop animado com thought/action/observation
**Imagem**: Ícone de cérebro (planejamento)
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Três capacidades únicas do Agentic RAG. (1) Planeja: antes de buscar, o agente raciocina sobre QUEM precisa buscar ("preciso de X e Y, nesta ordem"). (2) Refina: se a primeira busca retornou pouco, o agente reformula a query. (3) Decide parar: o agente julga se tem informação suficiente. Essas capacidades emergem do loop Thought/Action/Observation (ReAct, de ETHAGT01). Crucial: max_steps como guardrail — sem ele, o agente pode entrar em loop infinito.
💡 ANALOGIA: É como um detetive investigando um caso. Ele planeja quem interrogar (planeja), reformula perguntas se a testemunha não colabora (refina), e decide quando tem provas suficientes para fechar o caso (decide parar). Adaptive/CRAG/Self-RAG são investigadores com protocolo rígido; Agentic é o detetive experiente que improvisa.
⚠️ ERROS COMUNS: Alunos não colocam critério de parada no prompt do agente. Resultado: o agente não sabe quando parar. Ensine: "Pare quando tiver informação suficiente para responder completamente."
➡️ TRANSIÇÃO: "A capacidade mais poderosa: multi-hop."

---

### Slide 48 — Multi-Hop: Cadeias de Recuperação

**Título**: Multi-Hop: Cadeias de Recuperação
**Objetivo**: Introduzir o conceito de multi-hop retrieval.
**Conteúdo**:
- **Single-hop**: uma busca → resposta
- **Multi-hop**: múltiplas buscas encadeadas, cada uma dependendo da anterior
- **Exemplo**: "Quem fundou a empresa que criou o ChatGPT?"
  - Hop 1: buscar "quem criou o ChatGPT?" → OpenAI
  - Hop 2: buscar "quem fundou a OpenAI?" → Sam Altman, Elon Musk, etc.
  - Resposta: sintetizar
- Sem agente: difícil de orquestrar

**Diagrama**: Multi-hop retrieval (D10)
**Animação**: Hops aparecem em sequência
**Imagem**: Cadeia de elos
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Multi-hop é a killer feature do Agentic RAG. Single-hop: uma busca resolve. Multi-hop: a resposta da primeira busca é INPUT para a segunda. "Quem fundou a empresa que criou o ChatGPT?" — você não sabe a empresa de antemão. Hop 1 descobre (OpenAI). Hop 2 busca os fundadores. Sem agente, isso é muito difícil — você teria que prever as queries. Com agente, é natural: o agente vê a primeira resposta e formula a próxima query.
💡 ANALOGIA: É como uma investigação em camadas. Você descobre quem é o suspeito (hop 1), depois investiga o passado do suspeito (hop 2), depois os aliases (hop 3). Cada hop depende do anterior. Sem agente, você teria que prever tudo — impossível em casos complexos.
❓ PERGUNTA PARA A TURMA: "Pensem em uma pergunta multi-hop do sistema de vocês." (deixar responder)
⚠️ ERROS COMUNS: Alunos acham que multi-hop é "fazer várias buscas em paralelo". Não — multi-hop é SEQUENCIAL e DEPENDENTE. Paralelo é outra coisa (retrieve de múltiplas fontes ao mesmo tempo).
➡️ TRANSIÇÃO: "Vamos ver um trace real."

---

### Slide 49 — Exemplo Multi-Hop Detalhado

**Título**: Multi-Hop — Trace Detalhado
**Objetivo**: Concretizar multi-hop com um trace real.
**Conteúdo**:
- **Pergunta**: "Qual a diferença entre a política de férias da Etho e a legislação brasileira?"
- **Trace do agente**:
  - Thought: "Preciso de duas fontes"
  - Action: search_etho_docs("política de férias")
  - Observation: "30 dias após 1 ano..."
  - Action: search_web("CLT férias Brasil")
  - Observation: "30 dias corridos após 12 meses..."
  - Thought: "Agora posso comparar"
  - Answer: "A Etho segue a CLT, com diferença em..."

**Diagrama**: Trace de console estilizado
**Animação**: Linhas aparecem sequencialmente (simulando execução)
**Imagem**: Console/terminal estilizado
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Um trace real de multi-hop. A pergunta exige duas fontes: interna (Etho) e externa (CLT). O agente raciocina: "preciso de duas fontes". Busca na base interna. Depois busca na web. Combina. Responde. Observem como cada action depende do thought anterior, e cada thought processa a observation. É o loop ReAct puro (ETHAGT01), mas com tools de busca.
💡 ANALOGIA: É como um jornalista investigativo. Ele consulta o arquivo interno do jornal (Etho docs), depois busca na internet (CLT), depois escreve a matéria combinando as duas fontes. Cada passo é intencional.
⚠️ ERROS COMUNS: Alunos acham que o agente "sabe" que precisa de duas fontes. Não — ele raciocina a partir do prompt. Se o prompt não incentivar multi-hop, o agente pode fazer só um hop e responder incompleto.
➡️ TRANSIÇÃO: "Mas as tools de busca são especiais?"

---

### Slide 50 — Tools de Busca como Ferramentas do Agente

**Título**: Tools de Busca como Ferramentas do Agente
**Objetivo**: Mostrar que busca é uma tool como outra qualquer.
**Conteúdo**:
- O agente tem tools: `search_internal(query)`, `search_web(query)`, `search_kg(query)`
- ACI importa: tool bem documentada > prompt melhor (lição de ETHAGT01/ETHAGT02)
- O agente escolhe qual tool usar baseado na pergunta
- **Exemplo**: "Qual a política interna?" → `search_internal`; "Notícia de hoje?" → `search_web`
- Tool return format: lista de docs com score, não texto bruto

**Diagrama**: Agente com 3 tools de busca
**Animação**: Agente no centro; 3 tools ao redor
**Imagem**: Ícones de ferramentas
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Insight crucial: as tools de busca são tools como qualquer outra. O agente as chama quando decide. A lição de ETHAGT01/ETHAGT02 sobre ACI (Agent-Computer Interface) aplica totalmente: tool bem documentada > prompt melhor. A descrição da tool deve dizer QUANDO usar ("use search_internal para dados proprietários da empresa") e o que retorna (lista de docs com score, não texto bruto).
💡 ANALOGIA: É como uma caixa de ferramentas. Você tem martelo, chave de fenda, alicate. O agente é o mecânico que escolhe a ferramenta certa. Se as ferramentas forem mal etiquetadas (ACI ruim), o mecânico erra a escolha.
❓ PERGUNTA PARA A TURMA: "Quantas tools de busca vocês têm hoje? Documentadas como?" (calibrar)
⚠️ ERROS COMUNS: Alunos retornam texto bruto da tool. Melhor: lista estruturada de docs com score de relevância. Facilita o raciocínio do agente.
➡️ TRANSIÇÃO: "Vamos falar de fontes."

---

### Slide 51 — Múltiplas Fontes: Web, Interno, Knowledge Graph

**Título**: Múltiplas Fontes: Web, Interno, KG
**Objetivo**: Mostrar a diversidade de fontes.
**Conteúdo**:
- **Web search**: Tavily, SerpAPI, Brave Search — para dados externos e recentes
- **Interno**: vector DB (Qdrant, Milvus), SQL DB — para dados proprietários
- **Knowledge Graph**: Neo4j, GraphRAG — para dados relacionais estruturados
- O agente combina fontes: web para contexto + interno para detalhe
- O agente decide quando uma fonte é insuficiente e precisa de outra

**Diagrama**: 3 fontes convergindo para o agente
**Animação**: 3 fontes acendem; setas convergem para o agente
**Imagem**: Ícones de globo, servidor, grafo
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A diversidade de fontes é o superpoder do Agentic RAG. Web para dados externos e recentes (notícias, docs públicas). Interno para dados proprietários (documentação da empresa, base de conhecimento). Knowledge Graph para dados relacionais estruturados (quem trabalha com quem, hierarquias). O agente combina: web para contexto amplo + interno para detalhe específico. E decide quando uma fonte é insuficiente.
💡 ANALOGIA: É como um pesquisador com 3 bibliotecas: internet (web), biblioteca da empresa (interno), e base de dados relacional (KG). Ele sabe qual consultar para cada pergunta, e pode combinar.
⚠️ ERROS COMUNS: Alunos usam só vector DB. Limitante. Web e KG resolvem classes inteiras de perguntas que vector DB não consegue.
➡️ TRANSIÇÃO: "Uma fonte especial: Knowledge Graph via GraphRAG."

---

### Slide 52 — GraphRAG: Do Local ao Global

**Título**: GraphRAG: Do Local ao Global
**Objetivo**: Introduzir GraphRAG como padrão avançado.
**Conteúdo**:
- RAG tradicional: recupera chunks locais (vizinhança no espaço vetorial)
- **GraphRAG**: constrói grafo de conhecimento do corpus e recupera subgrafos
- **Vantagem**: responde perguntas globais ("quais os temas principais deste corpus?")
- Pipeline: extrair entidades/relações → agrupar em comunidades → sumarizar → recuperar
- Fonte: Edge et al., Microsoft, arXiv:2404.16130
- No Agentic RAG: o agente pode usar GraphRAG como uma tool

**Diagrama**: Grafo de conhecimento com comunidades (D11)
**Animação**: Grafo se forma; comunidades se agrupam
**Imagem**: Grafo com nós coloridos por comunidade
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: GraphRAG (Microsoft, 2024) resolve um problema que o RAG tradicional não consegue: perguntas GLOBAIS. "Quais os temas principais deste corpus?" — vector RAG recupera chunks locais, não consegue "enxergar" o todo. GraphRAG constrói um grafo de conhecimento: extrai entidades e relações do corpus, agrupa em comunidades (clusters temáticos), sumariza cada comunidade. Para perguntas globais, recupera subgrafos das comunidades relevantes. No Agentic RAG, GraphRAG é mais uma tool — o agente decide quando usar.
💡 ANALOGIA: Vector RAG é como olhar páginas individuais de um livro. GraphRAG é como olhar o índice e o sumário de capítulos — enxerga a estrutura global.
❓ PERGUNTA PARA A TURMA: "Qual pergunta global vocês gostariam de fazer no corpus de vocês?" (deixar responder)
⚠️ ERROS COMUNS: Alunos usam GraphRAG para perguntas locais. Overkill — vector RAG é mais rápido para "qual a política de X". GraphRAG brilha em globais.
➡️ TRANSIÇÃO: "Vamos ver tudo isso em ação. DEMO."

---

### Slide 53 — DEMO: Agentic RAG Multi-Hop

**Título**: DEMO — Agentic RAG Multi-Hop
**Objetivo**: Demo ao vivo — agente que refina queries e combina fontes.
**Conteúdo**:
- Código do `05-Labs/ETHAGT06/Lab2-Agentic-RAG-Multi-Hop`
- Agente com tools: `search_internal`, `search_web`
- Pergunta multi-hop: "Compare a política de férias da Etho com a CLT"
- Mostrar trace: planejamento → busca interna → busca web → síntese
- Mostrar max_steps guardrail em ação

**Diagrama**: Code block + terminal side-by-side
**Animação**: Highlight de linhas chave no trace
**Imagem**: Terminal ao vivo
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Demo ao vivo. Vou rodar o agente do Lab 2 com a pergunta "Compare a política de férias da Etho com a CLT". Observem o trace: o agente planeja ("preciso de duas fontes"), busca na base interna, busca na web, combina, responde. Notem o max_steps guardrail — se o agente não conseguir em N steps, ele para. Se a API falhar, tenho um screenshot do trace.
💡 ANALOGIA: É como assistir um detetive trabalhar ao vivo. Cada thought, cada action, cada observation é visível. Vocês veem o raciocínio emergindo.
⚠️ ERROS COMUNS: Se a API falhar, NÃO tente consertar ao vivo. Use o screenshot e siga. A turma perde a paciência com debugging ao vivo.
➡️ TRANSIÇÃO: "Pergunta sobre a demo."

---

### Slide 54 — Pergunta da DEMO

**Título**: Pergunta da DEMO
**Objetivo**: Engajar a turma com uma pergunta sobre a demo.
**Conteúdo**:
- "O que acontece se o agente não encontrar nada na busca interna?"
- "Como o agente decide que tem informação suficiente para parar?"
- "E se o max_steps for muito baixo?"
- Discussão em duplas (2 min)

**Diagrama**: Caixa de discussão
**Animação**: Perguntas aparecem
**Imagem**: Ícone de pergunta
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vamos debater em duplas. Três perguntas. (1) Se a busca interna falha, o agente deve tentar web? Depende do prompt — se ele foi instruído a combinar fontes, sim. (2) Como decide parar? O critério está no prompt: "pare quando tiver informação suficiente". (3) max_steps muito baixo = resposta incompleta; muito alto = custo e latência.
❓ PERGUNTA PARA A TURMA: "Em duplas, 2 min. Depois, 2 duplas compartilham."
➡️ TRANSIÇÃO: "Vamos sistematizar toda a escalada."

---

### Slide 55 — A Escalada: Adaptive → CRAG → Self-RAG → Agentic

**Título**: A Escalada — Adaptive → CRAG → Self-RAG → Agentic
**Objetivo**: Sistematizar a evolução das 4 arquiteturas.
**Conteúdo**:
- **Adaptive**: decide SE recuperar
- **CRAG**: avalia docs recuperados
- **Self-RAG**: avalia docs + resposta
- **Agentic**: agente dirige todo o processo (planeja, busca, refina, para)
- Cada nível adiciona reflexão e controle
- **Trade-off**: mais controle = mais custo e complexidade
- **Regra**: comece com Adaptive, só suba com evidência de insuficiência

**Diagrama**: Escada/pirâmide de complexidade (D12)
**Animação**: Níveis aparecem de baixo para cima
**Imagem**: Escada com 4 degraus
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A escalada. Cada degrau adiciona reflexão: Adaptive decide SE recuperar; CRAG avalia docs; Self-RAG avalia resposta; Agentic dirige todo o processo. Mais reflexão = mais controle = mais custo e complexidade. A regra de ouro: COMECE COM ADAPTIVE. Só suba para CRAG se Adaptive é insuficiente (docs irrelevantes). Só suba para Self-RAG se CRAG é insuficiente (alucinação). Só suba para Agentic se Self-RAG é insuficiente (multi-hop, multi-source). Pular degraus é anti-pattern.
💡 ANALOGIA: É como aprender a dirigir. Adaptive é dirigir na cidade. CRAG é dirigir na rodovia. Self-RAG é dirigir à noite. Agentic é dirigir numa corrida. Você não começa pela corrida — começa pela cidade e sobe conforme ganha confiança.
❓ PERGUNTA PARA A TURMA: "Em qual degrau está o RAG de vocês hoje?" (deixar responder — a maioria estará em Adaptive ou nenhum)
⚠️ ERROS COMUNS: Alunos querem Agentic porque é "mais avançado". Mais avançado ≠ melhor para todo caso. Adaptive resolve 60-70% dos casos de produção.
➡️ TRANSIÇÃO: "Agora que vimos as arquiteturas, vamos à engenharia de qualidade."

---

## SEÇÃO G — Engenharia de Qualidade (Slides 56-66 · 15 min)

---

### Slide 56 — [SEÇÃO] Engenharia de Qualidade

**Título**: 6 — Engenharia de Qualidade: O RAG é Tão Bom Quanto Seus Chunks
**Objetivo**: Transição para técnicas de qualidade.
**Conteúdo**: "6 — Engenharia de Qualidade: O RAG é Tão Bom Quanto Seus Chunks"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "6" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: As arquiteturas (Adaptive, CRAG, Self-RAG, Agentic) são a estrutura. A engenharia de qualidade é o conteúdo. Chunking, re-ranking, query rewriting, hybrid search — são as técnicas que fazem o retrieval funcionar. Sem isso, nenhuma arquitetura salva.
➡️ TRANSIÇÃO: "Começando pelo fundamento: chunking."

---

### Slide 57 — Chunking: O Fundamento Esquecido

**Título**: Chunking: O Fundamento Esquecido
**Objetivo**: Mostrar que chunking é a decisão mais impactante.
**Conteúdo**:
- "Garbage in, garbage out" — chunking ruim contamina todo o pipeline
- Chunking fixo (512 tokens): simples, mas quebra contexto
- Chunking por sentença/parágrafo: preserva semântica
- Chunking semântico: agrupa por tópicos
- O chunk é o átomo do RAG — tudo depende dele

**Diagrama**: Documento → diferentes estratégias de chunk (D13)
**Animação**: Documento é dividido de 3 formas diferentes
**Imagem**: Ícone de tesoura
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Chunking é a decisão mais impactante e mais subestimada do RAG. É o átomo — tudo depende dele. Chunking fixo (512 tokens) é o padrão, mas quebra contexto. Chunking por sentença/parágrafo preserva melhor a semântica. Chunking semântico agrupa por tópicos. E a novidade: late chunking (Contextual Retrieval, Anthropic 2024). Antes de otimizar embeddings ou re-rankers, OTIMIZE O CHUNKING. É onde o ganho é maior.
💡 ANALOGIA: É como cortar ingredientes para um prato. O corte (chunking) determina a textura do prato final. Corte ruim = prato ruim, não importa o tempero (re-rank).
❓ PERGUNTA PARA A TURMA: "Qual estratégia de chunking vocês usam hoje?" (calibrar — maioria usa fixo)
⚠️ ERROS COMUNS: Alunos otimizam embeddings antes de chunking. Ordem errada. Chunking > embeddings > re-rank na hierarquia de impacto.
➡️ TRANSIÇÃO: "Vamos aprofundar em duas estratégias avançadas."

---

### Slide 58 — Chunking Semântico e Hierárquico

**Título**: Chunking Semântico e Hierárquico
**Objetivo**: Detalhar duas estratégias avançadas.
**Conteúdo**:
- **Chunking semântico**:
  - Detectar mudanças de tópico (embeddings de sentença → clustering)
  - Agrupar sentenças relacionadas em um chunk
- **Chunking hierárquico**:
  - Múltiplos níveis: seção → parágrafo → sentença
  - Recuperar no nível apropriado pergunta
  - Parent-child: recuperar filho, retornar pai para contexto
- Quando cada brilha: semântico para docs densos, hierárquico para docs estruturados

**Diagrama**: Estrutura hierárquica de chunks (D13)
**Animação**: Estrutura em árvore aparece
**Imagem**: Árvore hierárquica
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Duas estratégias avançadas. Chunking semântico: computa embeddings de cada sentença, detecta mudanças de tópico (saltos no espaço vetorial), agrupa sentenças relacionadas. Ideal para docs densos (manuais técnicos, papers). Chunking hierárquico: múltiplos níveis (seção/parágrafo/sentença); você recupera no nível apropriado à pergunta. Parent-child: recupera o filho (chunk pequeno, match preciso) mas retorna o pai (chunk maior, contexto rico). Ideal para docs estruturados (livros, leis).
💡 ANALOGIA: Chunking semântico é como agrupar conversas por assunto — cada grupo é um tópico. Chunking hierárquico é como um livro com capítulos, seções, parágrafos — você pode ler o sumário (pai) ou o parágrafo (filho).
⚠️ ERROS COMUNS: Alunos usam chunking semântico em docs muito curtos. Para docs de 1 parágrafo, semântico não adiciona nada. Hierárquico em docs planos também não ajuda.
➡️ TRANSIÇÃO: "E a novidade de 2024?"

---

### Slide 59 — Late Chunking (Contextual Retrieval)

**Título**: Late Chunking (Contextual Retrieval)
**Objetivo**: Introduzir a técnica mais recente de chunking.
**Conteúdo**:
- **Problema**: chunk isolado perde contexto do documento
- **Late chunking** (Anthropic Contextual Retrieval, 2024):
  - Processar o documento inteiro no modelo ANTES de chunkar
  - Cada chunk recebe contexto do documento
  - Embeddings capturam contexto, não só fragmento
- Implementação: passar documento completo, depois chunkar, depois embedar
- Reduz falhas de recuperação em 30-50% (Anthropic)

**Diagrama**: Chunk isolado vs chunk com contexto (D13)
**Animação**: Chunk isolado (pobre) vs chunk com contexto (rico)
**Imagem**: Comparação antes/depois
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A novidade mais impactante de 2024: late chunking (Contextual Retrieval, Anthropic). O problema: quando você chunka um documento e embeda cada chunk isoladamente, o embedding perde o contexto do documento inteiro. A solução: passar o documento COMPLETO pelo modelo primeiro (capturando contexto), depois chunkar, e cada chunk "carrega" esse contexto. Resultado: embeddings muito mais ricos. A Anthropic reporta redução de 30-50% nas falhas de recuperação. É caro (processa o doc inteiro), mas o ganho é enorme.
💡 ANALOGIA: É como ler um capítulo inteiro antes de destacar uma frase. Se você destaca a frase sem ler o resto, pode não entender. Com contexto, o destaque faz sentido.
❓ PERGUNTA PARA A TURMA: "Vocês conheciam Contextual Retrieval?" (provavelmente minoria — motivar)
⚠️ ERROS COMUNS: Alunos acham que late chunking é "chunking maior". Não — é processar o doc inteiro ANTES de chunkar, dando contexto a cada chunk.
➡️ TRANSIÇÃO: "Agora, re-ranking."

---

### Slide 60 — Re-Ranking: Por Que e Como

**Título**: Re-Ranking: Por Que e Como
**Objetivo**: Explicar o porquê do re-ranking.
**Conteúdo**:
- Recuperação (BM25/densa): rápida, barata, mas imprecisa
- **Re-ranking**: lento, caro, mas preciso
- Pipeline: retrieve top-50 → re-rank → top-5 para o LLM
- O re-ranker avalia relevância query-doc, não só similaridade
- Reduz ruído no contexto do LLM

**Diagrama**: Funil: top-50 → re-rank → top-5
**Animação**: Funil estreita de 50 para 5
**Imagem**: Ícone de funil
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Re-ranking resolve o problema do "top-k traz lixo". A ideia: recupere MUITOS (top-50) com um método rápido e barato (BM25 ou densa), depois re-rankeie os top-50 com um modelo PRECISO (cross-encoder), e fique só com os top-5 para o LLM. O re-ranker avalia relevância real query-doc (não só similaridade vetorial), e é mais caro/lento — por isso aplicado só aos top-50, não a toda a base. Resultado: contexto limpo para o LLM.
💡 ANALOGIA: É como contratar. Você recebe 100 currículos (retrieve top-100), faz uma triagem rápida (re-rank), entrevista os 5 melhores (top-5 para o LLM). Triagem rápida é barata; entrevista é cara mas precisa.
⚠️ ERROS COMUNS: Alunos fazem re-rank de toda a base. Caro e lento. Re-rank só dos top-50 (ou top-100) já recuperados.
➡️ TRANSIÇÃO: "Quais re-rankers usar?"

---

### Slide 61 — Re-Rankers: Cohere, bge, Jina

**Título**: Re-Rankers: Cohere, bge, Jina
**Objetivo**: Comparar os re-rankers disponíveis.
**Conteúdo**:
- **Cohere Rerank**: API comercial, alta qualidade, paga por requisição
- **bge-reranker (BAAI)**: open-source, roda local, bom custo-benefício
- **Jina Reranker**: API e self-hosted, foco em multilingual
- Critério de escolha: latência, custo, qualidade, privacidade
- **Trade-off**: re-ranker cross-encoder é mais preciso mas mais lento

**Diagrama**: Tabela comparativa de re-rankers
**Animação**: Linhas da tabela aparecem
**Imagem**: Logos dos 3 re-rankers
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Três opções principais. Cohere Rerank: API comercial, melhor qualidade, paga por requisição ($0.002 por call aprox). bge-reranker (BAAI): open-source, roda local, ótimo custo-benefício (só computação). Jina Reranker: API e self-hosted, forte em multilingual. Critério de escolha: se privacidade é crítica → bge local; se qualidade é prioridade → Cohere; se multilingual → Jina. Todos são cross-encoders (mais precisos que bi-encoders mas mais lentos).
💡 ANALOGIA: É como escolher tradutor. Cohere é o tradutor profissional (caro, excelente). bge é o estagiário fluente (grátis, bom). Jina é o poliglota (multilingual). Escolha conforme o caso.
❓ PERGUNTA PARA A TURMA: "Qual vocês usariam no projeto de vocês?" (deixar justificarem)
➡️ TRANSIÇÃO: "Agora, query transformation."

---

### Slide 62 — Query Rewriting e HyDE

**Título**: Query Rewriting e HyDE
**Objetivo**: Introduzir query transformation.
**Conteúdo**:
- **Query rewriting**: LLM reescreve a pergunta do usuário para melhorar recuperação
  - "férias estagiário" → "política de licença para aprendizes e estagiários"
- **HyDE (Hypothetical Document Embeddings)**:
  - Gerar resposta HIPOTÉTICA à pergunta
  - Embedar a resposta hipotética (não a pergunta)
  - Buscar por similaridade com a resposta hipotética
- **Por que funciona**: resposta hipotética é mais próxima dos docs relevantes que a pergunta
- **Pergunta**: *Query rewriting: o agente deve reescrever a pergunta do usuário? Quando?*

**Diagrama**: Fluxo HyDE: pergunta → resposta hipotética → embed → search (D14)
**Animação**: Fluxo HyDE aparece passo a passo
**Imagem**: Setas do fluxo
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Duas técnicas de query transformation. Query rewriting: o LLM reescreve a pergunta do usuário para ser mais "amigável" à recuperação. "Férias estagiário" vira "política de licença para aprendizes e estagiários" — mais termos para casar com docs. HyDE vai além: em vez de reescrever a pergunta, gera uma RESPOSTA HIPOTÉTICA e embeda a resposta. Por que funciona? A resposta hipotética está mais próxima (no espaço vetorial) dos docs relevantes que a pergunta original. A pergunta é uma "questão"; a resposta é um "documento" — documentos casam melhor com documentos.
💡 ANALOGIA: Query rewriting é como reformular sua busca no Google ("férias estagiário" → "direitos trabalhistas estagiário férias"). HyDE é mais esperto: você imagina a resposta ideal e busca por algo parecido com ela. Como "eu acho que a resposta diria X" e busca por X.
❓ PERGUNTA PARA A TURMA: "Query rewriting: o agente deve sempre reescrever? Quando não?" (resposta: não para perguntas diretas; sim para perguntas ambíguas ou com sinônimos)
⚠️ ERROS COMUNS: Alunos aplicam HyDE sempre. Adiciona latência (uma chamada de LLM). Vale para perguntas abstratas; para diretas, query rewriting basta.
➡️ TRANSIÇÃO: "Agora, hybrid search."

---

### Slide 63 — Hybrid Search: BM25 + Densa

**Título**: Hybrid Search: BM25 + Densa
**Objetivo**: Mostrar que combinar busca lexical e densa é melhor.
**Conteúdo**:
- **BM25 (lexical)**: captura keywords exatas, termos técnicos, nomes próprios
- **Densa (embedding)**: captura semântica, sinônimos, paráfrase
- **Hybrid**: combinar scores de ambos com reciprocal rank fusion (RRF)
- Resultado: melhor recall que qualquer método isolado
- Implementação: Qdrant e Milvus suportam hybrid nativamente

**Diagrama**: Dois ramos (BM25 + densa) → fusão → top-k (D15)
**Animação**: Dois ramos se fundem
**Imagem**: Dois rios se unindo
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Hybrid search é o padrão de produção. BM25 (lexical) é excelente para keywords exatas, termos técnicos, nomes próprios, códigos. Densa (embedding) é excelente para semântica, sinônimos, paráfrases. Combinados com reciprocal rank fusion (RRF), você obtém o melhor dos dois: recall maior que qualquer método isolado. Qdrant e Milvus suportam hybrid nativamente — não há motivo para não usar em produção.
💡 ANALOGIA: BM25 é como buscar por número de telefone exato. Densa é como buscar por "aquele restaurante italiano perto do parque". Você precisa dos dois — um não substitui o outro.
❓ PERGUNTA PARA A TURMA: "Vocês usam hybrid search hoje?" (provavelmente minoria — motivar)
⚠️ ERROS COMUNS: Alunos usam SÓ densa porque "é mais moderna". BM25 ainda vence em muitos casos (termos técnicos). Hybrid é o padrão.
➡️ TRANSIÇÃO: "Agora, multi-vector."

---

### Slide 64 — Multi-Vector: ColBERT

**Título**: Multi-Vector: ColBERT
**Objetivo**: Introduzir representações multi-vetoriais.
**Conteúdo**:
- Embedding tradicional: 1 vetor por documento (sentence embedding)
- **ColBERT**: 1 vetor POR TOKEN do documento
- Recuperação: max-similarity entre tokens da query e tokens do doc
- **Vantagem**: granularidade muito maior, captura match a nível de token
- **Desvantagem**: armazenamento e computação muito maiores
- Quando usar: corpora técnicos com terminologia específica

**Diagrama**: 1 vetor/doc vs N vetores/doc
**Animação**: Documento vira 1 vetor (tradicional) vs N vetores (ColBERT)
**Imagem**: Comparação de representações
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: ColBERT é uma evolução radical. Embedding tradicional: 1 vetor por documento (sentence embedding). ColBERT: 1 vetor POR TOKEN. Em vez de comprimir todo o documento em 1 vetor, você mantém N vetores (um por token). A recuperação usa max-similarity: para cada token da query, encontra o token mais similar no doc. Granularidade muito maior — captura match a nível de termo técnico. A desvantagem é óbvia: armazenamento e computação N vezes maiores. Use em corpora técnicos com terminologia muito específica.
💡 ANALOGIA: Embedding tradicional é como resumir um livro em uma frase (perde detalhe). ColBERT é como manter cada palavra do livro indexada (granular, mas caro).
⚠️ ERROS COMUNS: Alunos usam ColBERT para tudo. Overkill para a maioria dos casos. Reserve para corpora técnicos específicos.
➡️ TRANSIÇÃO: "E quando há imagens e tabelas?"

---

### Slide 65 — Multimodal RAG: Texto, Imagem, Tabela

**Título**: Multimodal RAG: Texto, Imagem, Tabela
**Objetivo**: Mostrar que RAG vai além de texto.
**Conteúdo**:
- **Texto**: embedding de texto (padrão)
- **Imagem**: CLIP, vision embeddings — buscar por descrição ou imagem
- **Tabela**: converter para texto estruturado ou embedar como dado tabular
- Multimodal: combinar texto + imagem + tabela no mesmo espaço
- Modelos: GPT-4V, Claude Vision, LLaVA para geração multimodal
- Desafio: chunking de imagem (regiões), alinhamento modal

**Diagrama**: 3 modalidades → espaço compartilhado
**Animação**: 3 modalidades convergem para um espaço
**Imagem**: Ícones de texto, imagem, tabela
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: RAG multimodal vai além de texto. Imagens: usar CLIP ou vision embeddings para buscar por descrição ("foto de gato") ou por imagem similar. Tabelas: converter para texto estruturado (markdown) ou usar embeddings tabulares. A combinação de modalidades é o desafio — alinhar texto, imagem e tabela no mesmo espaço de recuperação. Modelos como GPT-4V e Claude Vision geram respostas multimodais. O desafio maior é chunking de imagem (dividir em regiões relevantes).
💡 ANALOGIA: É como uma enciclopédia ilustrada. Você busca por texto (descrição), por imagem (foto), ou por tabela (dados). O RAG multimodal integra tudo.
⚠️ ERROS COMUNS: Alunos tentam embedar imagens com embeddings de texto. Não funciona — precisa de CLIP ou vision embeddings específicos.
➡️ TRANSIÇÃO: "Vamos praticar a escolha."

---

### Slide 66 — Exercício: Escolhendo a Estratégia

**Título**: Exercício — Escolhendo a Estratégia
**Objetivo**: Praticar a escolha de técnicas de qualidade.
**Conteúdo**:
- 3 cenários — em duplas, escolher estratégia:
  1. Documentação técnica em inglês (10k páginas) → hybrid + re-rank
  2. FAQ jurídico em português (5k docs) → query rewriting + semantic chunking
  3. Catálogo de produtos com imagens (50k items) → multimodal + ColBERT
- Justificar com 2 critérios cada
- 2 min discussão

**Diagrama**: 3 cards com cenários
**Animação**: Cards aparecem
**Imagem**: Ícones dos 3 cenários
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Exercício em duplas. 3 cenários, escolham a estratégia de qualidade e justifiquem. (1) Documentação técnica em inglês: termos técnicos exigem BM25 (match lexical); paráfrases exigem densa; hybrid + re-rank é o ideal. (2) FAQ jurídico em PT: sinônimos jurídicos (reescrita); docs densos (chunking semântico). (3) Catálogo com imagens: imagens precisam de CLIP; terminologia de produto (ColBERT granular).
❓ PERGUNTA PARA A TURMA: "Em duplas, 2 min. Depois, 2 duplas compartilham."
➡️ TRANSIÇÃO: "Agora, avaliação."

---

## SEÇÃO H — Avaliação de RAG (Slides 67-73 · 10 min)

---

### Slide 67 — [SEÇÃO] Avaliação de RAG

**Título**: 7 — Avaliação de RAG: Sem Métricas, Você Está Cego
**Objetivo**: Transição para avaliação.
**Conteúdo**: "7 — Avaliação de RAG: Sem Métricas, Você Está Cego"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "7" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A seção mais subestimada. Sem métricas, você não sabe se seu RAG melhorou ou piorou. Sem dataset de holdout, não há como detectar regressão. Esta seção é o que separa RAG de hobby de RAG de produção.
➡️ TRANSIÇÃO: "Por que avaliar RAG é diferente?"

---

### Slide 68 — Por Que Avaliar RAG é Diferente

**Título**: Por Que Avaliar RAG é Diferente
**Objetivo**: Mostrar que RAG tem componentes que falham independentemente.
**Conteúdo**:
- Avaliação de LLM puro: a resposta está certa ou errada
- **Avaliação de RAG**: 3 componentes independentes:
  1. Retrieval: os docs recuperados são relevantes?
  2. Generation: a resposta é fiel aos docs?
  3. End-to-end: a resposta responde à pergunta?
- Cada componente precisa de métricas próprias
- Sem isso: não sabe se o problema é retrieval ou generation

**Diagrama**: 3 componentes com métricas separadas
**Animação**: 3 componentes acendem com suas métricas
**Imagem**: 3 blocos conectados
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Avaliar RAG é mais complexo que avaliar LLM puro porque há 3 componentes que falham independentemente. (1) Retrieval: os docs recuperados são relevantes? (context precision/recall). (2) Generation: a resposta é fiel aos docs? (faithfulness). (3) End-to-end: a resposta responde à pergunta? (answer relevance). Sem medir cada componente separadamente, você não sabe onde otimizar. Se faithfulness é baixa, o problema é generation (alucinação). Se context recall é baixo, o problema é retrieval (não achou os docs).
💡 ANALOGIA: É como diagnosticar um carro que não anda. Pode ser o motor (generation), o combustível (retrieval), ou a transmissão (end-to-end). Sem medir cada parte, você troca peças às cegas.
❓ PERGUNTA PARA A TURMA: "Se faithfulness é 0.95 mas answer relevance é 0.40, qual o problema?" (resposta: generation está fiel mas não responde — o LLM não está usando bem os docs, ou os docs não respondem à pergunta)
➡️ TRANSIÇÃO: "Vamos às métricas de geração."

---

### Slide 69 — Métricas: Faithfulness e Answer Relevance

**Título**: Métricas — Faithfulness e Answer Relevance
**Objetivo**: Detalhar as métricas de geração.
**Conteúdo**:
- **Faithfulness**: a resposta é fiel aos docs recuperados? (sem alucinação)
  - Decompor resposta em claims → verificar cada claim contra os docs
  - Score = claims suportadas / total de claims
- **Answer relevance**: a resposta responde à pergunta?
  - Gerar perguntas a partir da resposta → comparar com pergunta original
  - Score = similaridade semântica
- **Tensão**: alta faithfulness pode baixar relevance (responde só com o que está nos docs)

**Diagrama**: Fórmula visual de faithfulness
**Animação**: Resposta decompõe em claims; cada claim é verificada
**Imagem**: Claims como blocos
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: As duas métricas de geração. Faithfulness mede fidelidade aos docs (sem alucinação): decompõe a resposta em claims atômicas, verifica cada claim contra os docs, score = suportadas/total. Se a resposta diz "a política é de 30 dias" e os docs dizem isso, claim suportada. Se diz "e inclui bônus" e os docs não dizem, claim NÃO suportada — faithfulness cai. Answer relevance mede se a resposta responde à pergunta: gera perguntas hipotéticas a partir da resposta, compara com a pergunta original. Tensão: alta faithfulness (só usa docs) pode baixar relevance (não responde tudo se os docs não cobrem).
💡 ANALOGIA: Faithfulness é como verificar se um jornalista não inventou fatos (cada afirmação tem fonte). Answer relevance é como verificar se a matéria responde ao tema da pauta. As duas são independentes — um jornalista pode ser fiel (não inventa) mas irrelevante (fala de outro tema).
⚠️ ERROS COMUNS: Alunos otimizam só faithfulness. Resultado: respostas fiéis mas inúteis. Precisamos das duas métricas.
➡️ TRANSIÇÃO: "Agora, métricas de retrieval."

---

### Slide 70 — Métricas: Context Precision e Context Recall

**Título**: Métricas — Context Precision e Context Recall
**Objetivo**: Detalhar as métricas de retrieval.
**Conteúdo**:
- **Context precision**: dos docs recuperados, quantos são relevantes?
  - Score = relevantes no top-k / k
  - Penaliza ruído (docs irrelevantes que "afogam" os bons)
- **Context recall**: dos docs necessários, quantos foram recuperados?
  - Score = recuperados / necessários
  - Penaliza gaps (docs que faltam)
- **Tensão**: mais docs recuperados → mais recall, menos precision
- Re-ranking melhora precision sem sacrificar recall

**Diagrama**: Matriz precision × recall
**Animação**: Matriz 2x2 aparece
**Imagem**: Quadrantes
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: As duas métricas de retrieval. Context precision: dos k docs recuperados, quantos são realmente relevantes? Penaliza ruído — se top-10 tem 2 bons e 8 ruins, precision é 0.20. Context recall: dos docs NECESSÁRIOS (segundo ground truth), quantos foram recuperados? Penaliza gaps — se a resposta precisava de 3 docs e só achou 1, recall é 0.33. Tensão clássica: mais docs = mais recall (mais chance de achar) mas menos precision (mais ruído). Re-ranking é o truque: recupera muito (recall), re-rankeia e fica com pouco (precision).
💡 ANALOGIA: Precision é como a proporção de ouro no cascalho (quanto do que você achou é valioso). Recall é como quanto do ouro total você encontrou (não deixou passar). Re-ranking é como a bateia que separa ouro de cascalho.
⚠️ ERROS COMUNS: Alunos otimizam só recall (achar tudo). Mas se precision é baixa, o LLM recebe muito ruído. Precisamos das duas.
➡️ TRANSIÇÃO: "Frameworks para automatizar isso."

---

### Slide 71 — Frameworks: Ragas, TruLens, DeepEval

**Título**: Frameworks: Ragas, TruLens, DeepEval
**Objetivo**: Comparar os frameworks de avaliação.
**Conteúdo**:
- **Ragas**: foco em RAG, métricas padronizadas, open-source, integração LangChain
- **TruLens**: tracing + avaliação, dashboard interativo, foco em produção
- **DeepEval**: testes unitários para LLM, integra CI/CD, pytest-style
- Critério de escolha: stack existente, necessidade de tracing, CI/CD
- Todos usam LLM-as-judge internamente

**Diagrama**: Tabela comparativa de frameworks
**Animação**: Linhas da tabela aparecem
**Imagem**: Logos dos 3 frameworks
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Três frameworks. Ragas: foco específico em RAG, métricas padronizadas (faithfulness, answer relevance, context precision/recall), open-source, integra com LangChain. TruLens: tracing + avaliação, dashboard interativo, foco em produção (você vê os traces E as métricas). DeepEval: testes unitários estilo pytest para LLMs, integra CI/CD. Critério de escolha: se você já usa LangChain → Ragas; se precisa de tracing em produção → TruLens; se quer testes no CI/CD → DeepEval. Todos usam LLM-as-judge internamente (GPT-4, Claude) para computar as métricas.
💡 ANALOGIA: Ragas é como o controle de qualidade na fábrica. TruLens é como o monitor de produção (dashboard ao vivo). DeepEval é como os testes automatizados no pipeline de deploy.
❓ PERGUNTA PARA A TURMA: "Qual stack vocês usam hoje?" (calibrar)
➡️ TRANSIÇÃO: "Vamos ver o pipeline de avaliação no diagrama."

---

### Slide 72 — Diagrama: Eval Pipeline

**Título**: Eval Pipeline — Diagrama
**Objetivo**: Visualizar o pipeline de avaliação.
**Conteúdo**:
- Pipeline: pergunta → retrieve → generate → resposta
- Eval coleta: pergunta, docs recuperados, resposta gerada
- Métricas computadas: faithfulness, answer_relevance, context_precision, context_recall
- Dataset de holdout: perguntas + ground truth (docs e respostas esperadas)
- Execução: batch eval em CI/CD para detectar regressão

**Diagrama**: `12-Diagrams/ETHAGT06/eval-pipeline.mmd` (D16)
**Animação**: Métricas aparecem uma a uma
**Imagem**: Diagrama mermaid renderizado
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O pipeline de avaliação. Observem: o pipeline RAG normal (pergunta → retrieve → generate → resposta) corre em paralelo com o "eval pipeline". O eval coleta 3 coisas: a pergunta, os docs recuperados, e a resposta gerada. Com essas 3 + o ground truth (resposta e docs esperados), computa as 4 métricas. Em produção, isso roda em batch sobre o dataset de holdout (50-100 perguntas curadas), e em CI/CD para bloquear deploy em regressão. É o equivalente a testes automatizados para RAG.
💡 ANALOGIA: É como uma linha de produção com estação de qualidade. Os produtos (respostas) são fabricados normalmente; a estação de qualidade (eval) amostra, mede, e bloqueia o lote se algo falhar.
❓ PERGUNTA PARA A TURMA: "Quantas perguntas tem o holdout de vocês?" (provavelmente zero para a maioria — motivar)
⚠️ ERROS COMUNS: Alunos fazem eval manual ("eu li e parece bom"). Subjetivo, enviesado, não reproduzível. Eval automático é obrigatório em produção.
➡️ TRANSIÇÃO: "Como funciona o LLM-as-judge?"

---

### Slide 73 — LLM-as-Judge e Dataset de Holdout

**Título**: LLM-as-Judge e Dataset de Holdout
**Objetivo**: Detalhar LLM-as-judge e a importância do holdout.
**Conteúdo**:
- **LLM-as-judge**: usar um LLM (GPT-4, Claude) para avaliar respostas
- **Vieses a mitigar**:
  - Position bias (prefere primeira opção) → randomizar ordem
  - Self-preference (prefere próprio estilo) → usar modelo diferente do gerador
  - Length bias (prefere respostas longas) → normalizar
- **Dataset de holdout**: perguntas curadas com ground truth
- **Regressão**: se faithfulness cai de 0.90 para 0.82 após mudança → bloquear deploy
- Critério do projeto: faithfulness ≥ 0.85, context recall ≥ 0.80

**Diagrama**: Pipeline CI/CD com gate de qualidade
**Animação**: Pipeline CI/CD com gate verde/vermelho
**Imagem**: Ícone de portão (gate)
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: LLM-as-judge é como Ragas computa as métricas: usa um LLM (GPT-4, Claude) para julgar. Mas o juiz tem vieses. Position bias: se você pergunta "resposta A ou B é melhor?", o juiz prefere A (primeira). Solução: randomize a ordem. Self-preference: se o juiz é o mesmo modelo que gerou, ele prefere o próprio estilo. Solução: use modelo diferente (gerou com GPT-4, julga com Claude). Length bias: juiz prefere respostas longas. Solução: normalize por tamanho. Dataset de holdout: 50-100 perguntas curadas com ground truth. Regressão: se faithfulness cai de 0.90 para 0.82 após uma mudança, BLOQUEIE o deploy. Critério do projeto: faithfulness ≥ 0.85, context recall ≥ 0.80.
💡 ANALOGIA: LLM-as-judge é como um jurado de concurso. Ele tem preferências (viés). Você mitiga randomizando ordem, usando jurados diversos, e normalizando critérios. Holdout é como a prova de referência — sempre a mesma, para comparar ao longo do tempo.
❓ PERGUNTA PARA A TURMA: "Se faithfulness cair 5% numa mudança, o que vocês fazem?" (resposta: investigar a causa, reverter se necessário, NÃO deployar)
⚠️ ERROS COMUNS: Alunos usam o MESMO modelo para gerar e julgar. Self-preference enviesa. Use modelos diferentes.
➡️ TRANSIÇÃO: "Vamos ao fechamento."

---

## SEÇÃO I — Fechamento (Slides 74-85 · 12 min)

---

### Slide 74 — [SEÇÃO] Fechamento

**Título**: 8 — Boas Práticas, Anti-Patterns e Próximos Passos
**Objetivo**: Transição visual para o fechamento.
**Conteúdo**: "8 — Boas Práticas, Anti-Patterns e Próximos Passos"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "8" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Fechamento. Vamos consolidar com boas práticas, anti-patterns, resumo, quiz, conexão com próximos módulos, projeto e Q&A.
➡️ TRANSIÇÃO: "Começando pelo que fazer."

---

### Slide 75 — Boas Práticas (DO)

**Título**: Boas Práticas (DO)
**Objetivo**: Checklist de boas práticas.
**Conteúdo**:
- Comece com Adaptive RAG antes de pular para Agentic
- Avalie docs recuperados antes de gerar (CRAG)
- Use re-ranking sempre que possível
- Chunking semântico > chunking fixo
- Avaliação automatizada desde o dia 1 (Ragas)
- Dataset de holdout para regressão
- Hybrid search (BM25 + densa) como padrão
- max_steps em agentes RAG (guardrail)

**Diagrama**: Checklist verde (etho-success)
**Animação**: Itens aparecem com check verde
**Imagem**: Lista com checks
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: As 8 boas práticas. Comece com Adaptive (simples, resolve muito). Avalie docs (CRAG). Use re-rank (sempre que possível). Chunking semântico (não fixo). Avaliação desde o dia 1 (Ragas). Holdout (regressão). Hybrid search (padrão). max_steps (guardrail). Se vocês fizerem só 3 dessas, já estarão à frente de 80% dos RAGs em produção.
💡 ANALOGIA: É como os fundamentos de um esporte. Não importa quão fancy seja a jogada — sem fundamento (passe, recepção), não funciona.
❓ PERGUNTA PARA A TURMA: "Quantas dessas 8 vocês já fazem?" (levantar mãos por número)
➡️ TRANSIÇÃO: "E o que NÃO fazer?"

---

### Slide 76 — Anti-Patterns (DON'T)

**Título**: Anti-Patterns (DON'T)
**Objetivo**: Checklist do que NÃO fazer.
**Conteúdo**:
- Começar com Agentic RAG sem entender Adaptive/CRAG
- Chunking fixo sem pensar no conteúdo
- Confiar cegamente no top-k sem re-rank
- Sem avaliação — "funciona na demo"
- Sem fallback web quando a base local é insuficiente
- Adicionar mais docs sem re-rank (mais contexto ≠ melhor)
- Sem dataset de holdout — sem como detectar regressão
- Query rewriting automático sem validação

**Diagrama**: Checklist vermelho (etho-danger)
**Animação**: Itens aparecem com X vermelho
**Imagem**: Lista com X
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Os 8 anti-patterns. Pular direto para Agentic (sem entender o básico). Chunking fixo (preguiça). Confiar no top-k (sem re-rank). Sem avaliação ("funciona na demo"). Sem fallback (quando a base falha). Adicionar mais docs sem re-rank (mais ruído). Sem holdout (cego). Query rewriting automático (sem validar). Cada um desses é um erro caro em produção.
💡 ANALOGIA: É como os erros clássicos de culinária. Refogar no fogo alto (chunking fixo). Não provar o tempero (sem avaliação). Adicionar mais sal sem medir (mais docs sem re-rank). Cada um arruína o prato.
❓ PERGUNTA PARA A TURMA: "Qual desses vocês já cometeram?" (deixar confessar — gera risos e aprendizado)
➡️ TRANSIÇÃO: "Vamos ao resumo."

---

### Slide 77 — Resumo da Aula

**Título**: Resumo da Aula
**Objetivo**: Sintetizar os pontos-chave.
**Conteúdo**:
- RAG ingênuo falha silenciosamente — 4 tipos de falha sistemáticos
- **Adaptive RAG**: decide QUANDO recuperar
- **CRAG**: AVALIA docs antes de usar, com fallback web
- **Self-RAG**: reflete sobre docs E resposta (hallucination check)
- **Agentic RAG**: agente dirige todo o processo (multi-hop, multi-source)
- **Qualidade**: chunking + re-rank + hybrid + query rewriting
- **Avaliação**: faithfulness, relevance, context precision/recall com Ragas
- **Escalada**: Adaptive → CRAG → Self-RAG → Agentic (comece simples)

**Diagrama**: 8 ícones com os pontos-chave
**Animação**: Ícones aparecem um a um
**Imagem**: Grid de ícones
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O resumo em 8 pontos. RAG ingênuo falha (4 tipos). Adaptive decide quando. CRAG avalia docs. Self-RAG avalia resposta. Agentic dirige tudo. Qualidade: chunking + re-rank + hybrid + rewriting. Avaliação: 4 métricas com Ragas. Escalada: comece simples. Se vocês saírem com esses 8 pontos, a aula cumpriu o objetivo.
💡 ANALOGIA: É como o decálogo do RAG. 8 mandamentos para fazer RAG que funciona em produção.
➡️ TRANSIÇÃO: "Vamos confirmar com o checklist."

---

### Slide 78 — Checklist da Aula

**Título**: Checklist da Aula
**Objetivo**: Confirmar que todos os tópicos foram cobertos.
**Conteúdo**:
- [ ] Diagnosticou 4 tipos de falha do RAG ingênuo
- [ ] Explicou Adaptive RAG (decidir quando recuperar)
- [ ] Implementou CRAG (avaliar + 3 caminhos)
- [ ] Diferenciou Self-RAG (reflexão sobre resposta)
- [ ] Descreveu Agentic RAG (agente dirige, multi-hop)
- [ ] Listou 3+ técnicas de qualidade (chunking, re-rank, hybrid)
- [ ] Definiu 4 métricas de avaliação (faithfulness, relevance, precision, recall)

**Diagrama**: Checklist visual
**Animação**: Checks aparecem
**Imagem**: Lista com checkboxes
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vamos fazer o checklist juntos. Para cada item, levantem a mão se sentirem que dominam. Se algum não estiver claro, falem agora — vamos esclarecer antes do quiz.
❓ PERGUNTA PARA A TURMA: "Algum item que NÃO está claro?" (pausar — se houver, refaça brevemente)
➡️ TRANSIÇÃO: "Agora, o quiz."

---

### Slide 79 — Quiz: Pergunta 1

**Título**: Quiz — Pergunta 1
**Objetivo**: Verificar compreensão.
**Conteúdo**:
- "Qual é a diferença fundamental entre Adaptive RAG e Self-RAG?"
- A) Adaptive usa vector DB, Self-RAG usa grafo
- B) Adaptive decide quando recuperar, Self-RAG também avalia a resposta
- C) Adaptive é mais caro que Self-RAG
- D) Não há diferença significativa
- **Resposta**: B

**Diagrama**: 4 opções
**Animação**: Opções aparecem; resposta revelada após votação
**Imagem**: Cards A/B/C/D
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Quiz individual, sem consulta. Pergunta 1: diferença entre Adaptive e Self-RAG. Resposta: B. Adaptive decide quando recuperar; Self-RAG também avalia a resposta (hallucination check). Votem A, B, C ou D.
❓ PERGUNTA PARA A TURMA: Votação de mãos. Anotar distribuição.
➡️ TRANSIÇÃO: "Pergunta 2."

---

### Slide 80 — Quiz: Pergunta 2

**Título**: Quiz — Pergunta 2
**Objetivo**: Verificar compreensão.
**Conteúdo**:
- "Em CRAG, quando o sistema decide buscar na web?"
- A) Sempre, como primeiro passo
- B) Quando o avaliador classifica os docs como irrelevantes
- C) Quando a resposta é muito curta
- D) Quando o usuário pede explicitamente
- **Resposta**: B

**Diagrama**: 4 opções
**Animação**: Opções aparecem; resposta revelada
**Imagem**: Cards A/B/C/D
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Pergunta 2: quando CRAG busca na web? Resposta: B. Quando o avaliador classifica os docs como irrelevantes (incorreto). Web é fallback, não padrão. Votem.
❓ PERGUNTA PARA A TURMA: Votação.
➡️ TRANSIÇÃO: "Pergunta 3."

---

### Slide 81 — Quiz: Pergunta 3

**Título**: Quiz — Pergunta 3
**Objetivo**: Verificar compreensão.
**Conteúdo**:
- "Qual métrica mede se a resposta é fiel aos documentos recuperados?"
- A) Context precision
- B) Answer relevance
- C) Faithfulness
- D) Context recall
- **Resposta**: C

**Diagrama**: 4 opções
**Animação**: Opções aparecem; resposta revelada
**Imagem**: Cards A/B/C/D
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Pergunta 3: métrica de fidelidade aos docs. Resposta: C. Faithfulness decompõe a resposta em claims e verifica cada uma contra os docs. Votem.
❓ PERGUNTA PARA A TURMA: Votação. Anotar acertos — ≥2 = compreensão básica.
➡️ TRANSIÇÃO: "Vamos conectar com o que vem depois."

---

### Slide 82 — Conexão com Próximos Módulos

**Título**: Conexão com Próximos Módulos
**Objetivo**: Mostrar como ETHAGT06 conecta com o resto da especialização.
**Conteúdo**:
- **ETHAGT07** — Knowledge Graphs & Vector DBs: além do RAG plano (GraphRAG em profundidade)
- **ETHAGT90** — Projeto final (aplicar Agentic RAG)
- Conexão com ETHAGT01: Agentic RAG = Augmented LLM com retrieval in-loop
- Conexão com ETHAGT05: memória do agente RAG (estado entre hops)
- Conexão com ETHAGT12: AgentOps — traces de agentes RAG

**Diagrama**: Mapa da especialização com ETHAGT06 destacado
**Animação**: ETHAGT06 acende no centro; setas para ETHAGT07, ETHAGT90
**Imagem**: Mapa mental
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: ETHAGT06 é pivô. ETHAGT07 aprofunda Knowledge Graphs e Vector DBs (GraphRAG em profundidade). ETHAGT90 é o projeto final — onde vocês aplicam Agentic RAG. Conexões: ETHAGT01 (Augmented LLM), ETHAGT05 (memória entre hops), ETHAGT12 (AgentOps — traces de agentes RAG). Vocês saem daqui prontos para aprofundar em qualquer direção.
➡️ TRANSIÇÃO: "Referências."

---

### Slide 83 — Referências Completas

**Título**: Referências Completas
**Objetivo**: Listar todas as fontes.
**Conteúdo**:
1. Lewis, P. et al. *Retrieval-Augmented Generation*. arXiv:2005.11401, 2020
2. Asai, A. et al. *Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection*. arXiv:2310.11511, 2023
3. Yan, S. et al. *Corrective Retrieval Augmented Generation (CRAG)*. arXiv:2401.15884, 2024
4. Edge, D. et al. *GraphRAG: From Local to Global*. Microsoft, arXiv:2404.16130, 2024
5. Anthropic. *Contextual Retrieval*. 2024
6. LangGraph examples: `adaptive_rag`, `crag`, `self_rag`, `agentic_rag`
7. Cohere. *Rerank Documentation*
8. Ragas: *Evaluation framework for RAG*

**Diagrama**: Lista numerada
**Animação**: Itens aparecem
**Imagem**: Ícones de paper/livro
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: As 8 referências. As 4 canônicas (RAG original, Self-RAG, CRAG, GraphRAG) são leitura obrigatória. Anthropic Contextual Retrieval é o último grito. LangGraph examples são a implementação de referência. Cohere e Ragas são as ferramentas. Todas no repositório da especialização.
➡️ TRANSIÇÃO: "E o projeto."

---

### Slide 84 — Projeto do Módulo + Labs

**Título**: Projeto do Módulo + Labs
**Objetivo**: Apresentar o projeto e laboratórios.
**Conteúdo**:
- **Projeto**: construir sistema RAG de produção sobre corpus técnico
  - Pipeline agêntico (Adaptive/CRAG/Agentic)
  - Eval automatizado com Ragas
  - Entrega: sistema + eval report + ADR
  - Critério: faithfulness ≥ 0.85 e context recall ≥ 0.80
- **Lab 1** (4h): "Diagnosticando falhas" — RAG ingênuo em corpus problemático
- **Lab 2** (5h): "Agentic RAG multi-hop" — agente que refina queries e combina fontes

**Diagrama**: Timeline do projeto + labs
**Animação**: Timeline aparece
**Imagem**: Ícones de projeto e labs
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O projeto é a consolidação. Vocês constroem um sistema RAG de produção com pipeline agêntico, eval automatizado (Ragas), e justificam escolhas em ADR. Critério de sucesso: faithfulness ≥ 0.85 e context recall ≥ 0.80. Lab 1 (4h) diagnostica falhas do RAG ingênuo. Lab 2 (5h) implementa Agentic RAG multi-hop. São ~20h de trabalho prático.
💡 ANALOGIA: O projeto é como uma prova de piloto. Vocês não só dirigem — vocês planejam a rota, escolhem o carro, e relatam o que funcionou.
❓ PERGUNTA PARA A TURMA: "Alguma dúvida sobre o projeto?" (esclarecer prazos)
➡️ TRANSIÇÃO: "E finalmente, Q&A."

---

### Slide 85 — Q&A / Encerramento

**Título**: Perguntas?
**Objetivo**: Abrir para perguntas e encerrar.
**Conteúdo**:
- "Perguntas?"
- Contato do professor
- "Na próxima aula: ETHAGT07 — Knowledge Graphs & Vector DBs"
- Leitura: Asai et al. *Self-RAG* (arXiv:2310.11511) antes da próxima aula

**Diagrama**: Logo Etho + fundo etho-dark
**Animação**: Fade out
**Imagem**: Logo Etho centralizado
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Chegamos ao fim. Perguntas? Se não houver, façam a pergunta inversa: "qual parte foi menos clara?" Lembrem-se: leiam Self-RAG (Asai et al.) antes da próxima aula — ETHAGT07 aprofunda Knowledge Graphs e Vector DBs, e GraphRAG. Obrigado pela atenção.
❓ PERGUNTA PARA A TURMA: "Perguntas? Ou qual parte foi menos clara?"
⚠️ ERROS COMUNS: Encerrar sem deixar tempo para Q&A. Sempre reserve pelo menos 2-3 min.
➡️ TRANSIÇÃO: Fim da aula.

---

> **Fim da Parte 2 (Slides 45-85). Fim da apresentação ETHAGT06.**
