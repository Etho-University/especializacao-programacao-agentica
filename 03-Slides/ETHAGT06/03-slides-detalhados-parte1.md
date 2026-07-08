# ETHAGT06 — Slides Detalhados + Notas do Professor (Parte 1: Slides 1-44)

> Universidade Etho · Especialização em Programação Agêntica
> Cada slide contém: título, objetivo, conteúdo, notas do professor, diagrama, animação, imagem, tempo.

---

## SEÇÃO A — Abertura (Slides 1-7 · 8 min)

---

### Slide 1 — Capa

**Título**: ETHAGT06 — RAG Agêntico
**Objetivo**: Identificar a aula, o professor e o contexto dentro da especialização.
**Conteúdo**:
- ETHAGT06 — RAG Agêntico (Adaptive · Corrective · Self-RAG · Agentic)
- Universidade Etho · Especialização em Programação Agêntica
- Fase B — RAG Avançado · 30 h
- Professor · Data

**Diagrama**: Logo Etho (canto sup. esquerdo) + imagem de fundo abstrata (base de dados / neural retrieval)
**Animação**: Fade in do título (300ms)
**Imagem**: Fundo `etho-dark` (#0F1E2D) com pattern sutil de nós e arestas
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Bem-vindos. Esta é a aula que separa quem faz RAG de quem faz RAG que funciona em produção. Vamos evoluir do RAG "ingênuo" — aquele que funciona na demo e quebra em produção — para o RAG agêntico, onde o agente decide *quando*, *o quê* e *como* recuperar. Veremos 4 arquiteturas (Adaptive, CRAG, Self-RAG, Agentic), técnicas de qualidade (chunking, re-rank, HyDE, hybrid) e como avaliar tudo isso com métricas reais.
💡 ANALOGIA: É como a diferença entre um estagiário que sempre busca no mesmo arquivo (RAG ingênuo) e um pesquisador sênior que decide quando precisa consultar, avalia se a fonte é boa, reflete se a resposta está correta e sabe quando buscar em outro lugar (RAG agêntico).
❓ PERGUNTA PARA A TURMA: "Quantos de vocês já usaram RAG em produção?" (levantar mãos — calibrar nível da turma)
⚠️ ERROS COMUNS: Alunos chegam querendo pular direto para Agentic RAG. Preciso redirecionar: "Comece com Adaptive. Suba de nível só com evidência de insuficiência."
➡️ TRANSIÇÃO: "Vamos começar definindo o que vocês vão conseguir fazer ao final desta aula."

---

### Slide 2 — Objetivos do Módulo

**Título**: Objetivos do Módulo
**Objetivo**: Deixar claro o que o aluno deve conseguir FAZER ao final da aula.
**Conteúdo**:
- **Objetivo geral**: Evoluir além do RAG "ingênuo" para RAG agêntico, onde o agente decide *quando*, *o quê* e *como* recuperar, com correção iterativa e auto-avaliação
- **Objetivos específicos**:
  1. Diagnosticar limites do RAG ingênuo em produção
  2. Implementar Adaptive RAG, CRAG, Self-RAG e Agentic RAG
  3. Aplicar técnicas de qualidade: chunking inteligente, re-ranking, query rewriting, hybrid search
  4. Construir pipeline de avaliação de RAG (faithfulness, relevance, context recall/precision)
  5. Produzir um sistema RAG multi-tenant com segurança

**Diagrama**: 5 ícones representando cada objetivo (lupa com X, engrenagens, diamante, gráfico de métricas, escudo)
**Animação**: Objetivos aparecem um a um (on click)
**Imagem**: Ícones minimalistas em `etho-accent` (#E85D2F)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Cada objetivo é mensurável. Não é "entender" — é "diagnosticar", "implementar", "aplicar", "construir", "produzir". Se ao final da aula você não consegue fazer essas cinco coisas, eu falhei como professor. O objetivo #4 (pipeline de avaliação) é o mais subestimado — é o que separa RAG que "parece funcionar" de RAG que "provavelmente funciona".
💡 ANALOGIA: É como um checklist de pré-voo. O piloto não diz "entendo como o RAG voa" — ele verifica cada item: rota, combustível, condições. Hoje, nosso checklist é estes 5 objetivos.
❓ PERGUNTA PARA A TURMA: "Qual desses objetivos vocês acham mais desafiador?" (deixar responder — costuma ser #2 ou #4)
⚠️ ERROS COMUNS: Alunos acham que "fazer RAG agêntico" = "usar LangGraph". Não. Arquitetura é o que importa; framework é instanciação.
➡️ TRANSIÇÃO: "Antes de saber o que vamos fazer, vamos ver onde estamos no mapa de competências."

---

### Slide 3 — Competências Desenvolvidas

**Título**: Competências Desenvolvidas
**Objetivo**: Conectar a aula ao Framework Etho de competências.
**Conteúdo**:

| Competência | Nível ao final | Próximo nível em |
|---|---|---|
| C1 Programação Agêntica | **A** (Avançado) | ETHAGT07, ETHAGT90 |
| C3 MCP & Tool Use | **B** (Básico) | ETHAGT08 |
| C4 Agent Memory | **I** (Intermediário) | ETHAGT05 |
| C5 AgentOps & Avaliação | **I** (Intermediário) | ETHAGT12 |

**Diagrama**: Radar chart com 4 eixos mostrando nível B/I/A
**Animação**: Radar aparece com wipe (left-to-right, 500ms)
**Imagem**: Badge visual por competência (círculos coloridos)
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Este módulo leva a competência C1 ao nível **Avançado** — você será capaz de projetar e justificar arquiteturas RAG completas. C5 (AgentOps & Avaliação) atinge Intermediário porque construímos um pipeline de avaliação automatizado com Ragas. C4 (Agent Memory) fica em Intermediário porque o estado entre hops do Agentic RAG é uma forma de memória de trabalho.
💡 ANALOGIA: É como aprender a dirigir. ETHAGT01 foi sair do estacionamento. ETHAGT04 foi dirigir na cidade. Hoje você vai dirigir em rodovia com trânsito intenso — Adaptive, CRAG, Self-RAG e Agentic são as manobras que você precisa dominar.
⚠️ ERROS COMUNS: Alunos acham que "Avançado em C1" significa "saber LangGraph avançado". Não — significa ser capaz de escolher a arquitetura certa e justificar com trade-offs.
➡️ TRANSIÇÃO: "Vamos ver como esta aula está estruturada para entregar essas competências."

---

### Slide 4 — Agenda da Aula

**Título**: Agenda da Aula
**Objetivo**: Mostrar o roteiro da aula com tempos estimados.
**Conteúdo**:
- **Bloco 1 (~58 min)**:
  - Abertura (8 min) — objetivos, motivação, contexto
  - RAG Ingênuo Falha (10 min) — 4 tipos de falha, mito vector DB
  - Adaptive RAG (12 min) — quando recuperar, routing
  - Corrective RAG (15 min) — avaliador, 3 caminhos, web fallback
  - Self-RAG (13 min) — tokens de reflexão, prompting
- **Bloco 2 (~52 min)**:
  - Agentic RAG (15 min) — multi-hop, GraphRAG, DEMO
  - Engenharia de Qualidade (15 min) — chunking, re-rank, HyDE, hybrid
  - Avaliação de RAG (10 min) — métricas, Ragas, eval pipeline
  - Fechamento (12 min) — boas práticas, anti-patterns, quiz, projeto, Q&A

**Diagrama**: Timeline horizontal com 9 seções coloridas
**Animação**: Timeline cresce da esquerda para direita (500ms)
**Imagem**: Ícones de relógio por seção
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A aula tem dois blocos. O primeiro é a escalada: Adaptive → CRAG → Self-RAG, cada um adicionando mais reflexão e controle. O segundo é a consolidação: Agentic RAG (o topo), engenharia de qualidade (chunking, re-rank), avaliação (Ragas) e fechamento. Há um intervalo de 5 min entre os blocos.
💡 ANALOGIA: É como uma escalada. O bloco 1 é a subida — cada arquitetura é um degrau. O bloco 2 é o cume e a descida: Agentic é o topo, qualidade e avaliação são a consolidação, o fechamento é o relatório da expedição.
⚠️ ERROS COMUNS: Alunos chegam atrasados e perdem a motivação (Slide 6). Avisar que a Seção B (RAG Ingênuo Falha) define o diagnóstico que motiva todas as arquiteturas seguintes.
➡️ TRANSIÇÃO: "Vamos começar conectando com o que vocês já sabem de ETHAGT04."

---

### Slide 5 — Pré-requisitos: ETHAGT04 e o Que Você Já Sabe

**Título**: Pré-requisitos: ETHAGT04 e o Que Você Já Sabe
**Objetivo**: Ancorar a aula no conhecimento prévio de RAG.
**Conteúdo**:
- ETHAGT04 cobriu: RAG básico, vector DBs, embeddings, pipeline retrieve→generate
- O que você já deveria saber: cosine similarity, top-k retrieval, LangChain básico
- O que esta aula adiciona: o agente entra no loop de recuperação
- Você NÃO precisa ter feito ETHAGT04 se já pratica RAG em produção

**Diagrama**: Ponte ETHAGT04 (pipeline fixo) → ETHAGT06 (agente in-loop)
**Animação**: Ponte desliza da esquerda para direita
**Imagem**: Ícone de ponte conectando dois blocos
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: ETHAGT04 estabeleceu o básico: embeddings, vector DBs, o pipeline retrieve→generate. Hoje vamos questionar esse pipeline. A pergunta central: e se o agente decidisse, a cada pergunta, SE recuperar, O QUÊ recuperar, e COMO usar o que recuperou? É essa a diferença entre RAG fixo e RAG agêntico.
💡 ANALOGIA: ETHAGT04 ensinou a cozinhar com receita (pipeline fixo). Hoje vocês vão cozinhar sem receita, adaptando ao que tem na geladeira (agente decide).
⚠️ ERROS COMUNS: Alunos sem ETHAGT04 podem ficar perdidos nos fundamentos. Se for o caso, faça um recap rápido de embeddings e top-k.
➡️ TRANSIÇÃO: "Mas por que estamos falando disso? Porque o RAG ingênuo falha silenciosamente."

---

### Slide 6 — Motivação: RAG "Funciona" Até Parar de Funcionar

**Título**: RAG "Funciona" Até Parar de Funcionar
**Objetivo**: Criar tensão cognitiva — RAG ingênuo falha silenciosamente em produção.
**Conteúdo**:
- **Cenário real**: pergunta "qual a política de férias para estagiários?" — recupera chunks errados, responde com info genérica
- O usuário não sabe que a resposta está errada — confiança alta, grounding baixo
- "Vector DB + top-k" parece funcionar na demo e quebra em produção
- **Pergunta**: *Quantos de vocês já usaram RAG e obtiveram resposta errada com alta confiança?*

**Diagrama**: Split — esquerda: usuário feliz na demo (verde) | direita: usuário frustrado em produção (vermelho)
**Animação**: Split — lado esquerdo aparece primeiro, depois lado direito
**Imagem**: Ícones de sorriso (esquerda) vs frustração (direita)
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Este é o problema central desta aula. O RAG ingênuo falha silenciosamente: não dá erro 500, não crasha. Ele responde com confiança alta mesmo quando está errado. O usuário age sobre informação falsa. Em produção, isso é pior do que não responder — porque pelo menos "não sei" é honesto. A pergunta-chave da aula: como fazer o RAG avaliar a si mesmo antes de responder?
💡 ANALOGIA: É como um médico que sempre dá um diagnóstico confiante, mesmo quando não sabe. Às vezes acerta (perguntas fáceis), mas quando erra, o paciente confia e piora. Preferível um médico que diga "preciso pesquisar mais" (fallback) ou "tenho 60% de certeza" (reflexão).
❓ PERGUNTA PARA A TURMA: "Quantos de vocês já usaram RAG e obtiveram resposta errada com alta confiança?" (levantar mãos — a maioria que usou RAG vai levantar)
⚠️ ERROS COMUNS: Alunos acham que "prompt melhor" resolve. Não resolve. O problema é sistêmico: chunking, embedding, recuperação, sem avaliação.
➡️ TRANSIÇÃO: "Essa limitação não é nova. Mas como evoluímos do RAG original até o RAG agêntico?"

---

### Slide 7 — Contexto: Do RAG Fixo ao RAG In-Loop

**Título**: Do RAG Fixo ao RAG In-Loop
**Objetivo**: Explicar a evolução histórica do RAG de 2020 a 2025.
**Conteúdo**:
- **Linha do tempo**:
  - 2020: RAG original (Lewis et al., arXiv:2005.11401) — pipeline fixo retrieve→generate
  - 2023: Self-RAG (Asai et al., arXiv:2310.11511) — modelo reflete sobre recuperação
  - 2024: CRAG (Yan et al., arXiv:2401.15884) — avaliador de relevância + web fallback
  - 2024: GraphRAG (Edge et al., arXiv:2404.16130) — do local ao global via grafo
  - 2025: Agentic RAG — agente dirige todo o processo
- **RAG fixo**: query → retrieve → generate (pipeline rígido)
- **RAG agêntico**: agente decide se/quando/o quê/como recuperar, com correção iterativa
- 4 arquiteturas que veremos: Adaptive → CRAG → Self-RAG → Agentic

**Diagrama**: Timeline horizontal com marcos (D1)
**Animação**: Marcos aparecem sequencialmente (on click)
**Imagem**: Convergência de 5 papers em "RAG Agêntico"
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O RAG original (Lewis et al., 2020) era fixo: sempre recupera, sempre gera. Em 2023-2024, três papers mudaram isso: Self-RAG (reflexão), CRAG (correção) e GraphRAG (global). Em 2025, a síntese: Agentic RAG, onde o agente dirige todo o processo. A evolução não é "mais complexo = melhor" — é "mais reflexão = mais confiável". Cada arquitetura adiciona um checkpoint de decisão.
💡 ANALOGIA: É como a evolução dos pilotos automáticos. Primeiro (RAG fixo): segue rota programada, não adapta. Depois (Adaptive): decide se precisa desviar. Depois (CRAG): avalia se a rota é segura. Depois (Self-RAG): reflete se está voando bem. Por fim (Agentic): pilota tudo sozinho, decide para onde ir.
❓ PERGUNTA PARA A TURMA: "Qual desses papers vocês já leram?" (calibrar familiaridade com a literatura)
⚠️ ERROS COMUNS: Alunos confundem Self-RAG com CRAG. Self-RAG é o modelo que reflete; CRAG é o pipeline que avalia.
➡️ TRANSIÇÃO: "Antes de construir, precisamos diagnosticar. Por que o RAG ingênuo falha?"

---

## SEÇÃO B — Por que o RAG Ingênuo Falha (Slides 8-14 · 10 min)

---

### Slide 8 — [SEÇÃO] Por que o RAG Ingênuo Falha

**Título**: 1 — Por que o RAG Ingênuo Falha
**Objetivo**: Transição visual para o diagnóstico de falhas.
**Conteúdo**: Número "1" grande + "Por que o RAG Ingênuo Falha"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "1" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Início do bloco de diagnóstico. Vamos desconstruir o pipeline ingênuo e identificar 4 classes de falha sistemáticas. Só sabendo onde falha, sabemos onde agir com Adaptive, CRAG, Self-RAG e Agentic.
➡️ TRANSIÇÃO: "Primeiro: o pipeline ingênuo e seus pontos de falha."

---

### Slide 9 — O Pipeline do RAG Ingênuo

**Título**: O Pipeline do RAG Ingênuo e Seus Pontos de Falha
**Objetivo**: Mostrar o pipeline canônico e onde ele quebra.
**Conteúdo**:
- Pipeline: query → embed → vector search (top-k) → stuff into prompt → generate
- Cada etapa tem pontos de falha:
  - **Embed**: sinônimos não capturados, multilingual distante
  - **Search**: top-k traz irrelevante junto com relevante
  - **Stuff**: contexto quebrado, janela estourada, lost in the middle
  - **Generate**: alucinação sobre docs ruins
- Fonte: arXiv:2005.11401 (RAG original, Lewis et al.)

**Diagrama**: `12-Diagrams/ETHAGT06/` — pipeline com pontos de falha destacados (D2)
**Animação**: Cada etapa acende, depois pontos de falha aparecem em vermelho
**Imagem**: Fluxograma com 4 estágios e marcadores de alerta
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Este é o pipeline que vocês já conhecem de ETHAGT04. Ele funciona — para perguntas fáceis. O problema é que ele não tem NENHUMA reflexão sobre qualidade. Não pergunta "esta pergunta precisa de retrieval?", não pergunta "os docs recuperados são bons?", não pergunta "a resposta está correta?". Cada etapa é uma caixa preta que confia na anterior. Quando uma falha, a falha se propaga silenciosamente.
💡 ANALOGIA: É como uma linha de montagem sem controle de qualidade. Cada estação faz sua parte e passa adiante. Se a estação 2 produziu peça com defeito, a estação 3 não sabe — continua montando. O produto final parece certo mas está quebrado por dentro.
❓ PERGUNTA PARA A TURMA: "Em qual dessas 4 etapas vocês já tiveram mais problemas?" (deixar responder — costuma ser search ou generate)
⚠️ ERROS COMUNS: Alunos focam só no generate (prompt). Mas se o retrieval é ruim, nenhum prompt salva. Retrieval é o gargalo mais subestimado.
➡️ TRANSIÇÃO: "Vamos detalhar cada uma das 4 falhas, começando pelo chunking."

---

### Slide 10 — Falha 1: Chunking Quebra Contexto

**Título**: Falha 1: Chunking Quebra Contexto
**Objetivo**: Mostrar que o chunking ingênuo (tamanho fixo) destrói semântica.
**Conteúdo**:
- Chunking por tamanho fixo (ex.: 512 tokens) corta no meio de uma ideia
- **Exemplo**: política de férias dividida entre dois chunks — nenhum faz sentido sozinho
- Sobreposição (overlap) ajuda mas não resolve
- **Consequência**: embedding captura fragmento sem contexto → recuperação irrelevante
- Preview da solução: chunking semântico, hierárquico, late-chunking (Seção G)

**Diagrama**: Documento cortado ao meio com contexto perdido (D3)
**Animação**: Tesoura corta o documento; metades se separam
**Imagem**: Documento com linha de corte vermelha
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O chunk é o átomo do RAG. Se o átomo é ruim, a molécula inteira é ruim. Chunking fixo é a abordagem mais comum e a mais ingênua: pega o documento, corta em pedaços de N tokens, pronto. O problema: ideias não respeitam limites de tokens. A política de férias pode ter uma condição ("para estagiários") em um chunk e a consequência ("30 dias") no outro. Recuperar só um dá informação incompleta ou errada.
💡 ANALOGIA: É como cortar um livro a cada 500 palavras sem olhar os capítulos. Você pode cortar uma frase ao meio, separar um parágrafo de seu contexto. O leitor recebe fragmentos ininteligíveis.
❓ PERGUNTA PARA A TURMA: "Qual tamanho de chunk vocês usam hoje? Fixo ou variável?" (calibrar maturidade)
⚠️ ERROS COMUNS: Overlap de 50 tokens resolve muito pouco se o conceito inteiro tem 800 tokens.
➡️ TRANSIÇÃO: "Mesmo com chunking bom, o embedding tem limites."

---

### Slide 11 — Falha 2: Embedding Não Captura Semântica

**Título**: Falha 2: Embedding Não Captura Semântica
**Objetivo**: Mostrar que embeddings têm limites semânticos.
**Conteúdo**:
- Embedding captura similaridade lexical, não raciocínio
- **Exemplo**: "férias de estagiário" vs "licença de aprendiz" — semanticamente equivalentes, lexicalmente diferentes
- Multilingual: mesma ideia em PT vs EN pode ter embeddings distantes
- Dados tabulares: embeddings de texto não capturam estrutura de tabela
- Preview da solução: query rewriting, HyDE, hybrid search (Seção G)

**Diagrama**: Dois pontos no espaço vetorial distantes mas semanticamente iguais (D3)
**Animação**: Dois pontos no espaço vetorial com linha tracejada "semanticamente igual"
**Imagem**: Espaço vetorial 2D com dois clusters
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Embeddings são poderosos mas têm cegueira semântica. Eles aprendem co-ocorrência lexical, não significado. "Férias de estagiário" e "licença de aprendiz" podem descrever a mesma coisa, mas se as palavras são diferentes, a similaridade vetorial é baixa. Isso piora com multilingual: o mesmo conceito em português e inglês pode ter embeddings distantes se o modelo não foi treinado em cross-lingual.
💡 ANALOGIA: É como duas pessoas descrevendo a mesma coisa com palavras diferentes. Um diz "férias", o outro "recesso". Para um humano, é a mesma coisa. Para um embedding lexical, são duas coisas distintas.
❓ PERGUNTA PARA A TURMA: "Vocês já tiveram problema de sinônimos no RAG de vocês?" (calibrar)
⚠️ ERROS COMUNS: Alunos acham que "embedding melhor" resolve tudo. Modelos melhores ajudam, mas query rewriting e hybrid search são mais impactantes.
➡️ TRANSIÇÃO: "Mesmo com embedding bom, top-k puro traz lixo."

---

### Slide 12 — Falha 3: Sem Re-Rank, Top-k Traz Lixo

**Título**: Falha 3: Sem Re-Rank, Top-k Traz Lixo
**Objetivo**: Mostrar que top-k puro mistura relevante com irrelevante.
**Conteúdo**:
- Top-k retorna os k mais similares — nem todos são relevantes
- Sem re-rank: o chunk #1 pode ser irrelevante e "afogar" os bons
- LLM recebe contexto poluído → alucinação ou confusão
- **Exemplo**: top-5 traz 1 chunk bom e 4 irrelevantes
- Preview da solução: re-ranking com Cohere, bge, Jina (Seção G)

**Diagrama**: Top-5 resultados com 1 verde e 4 vermelhos (D3)
**Animação**: 5 cards aparecem; 4 ficam vermelhos (irrelevantes)
**Imagem**: Lista de resultados com scores
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O retrieval por similaridade vetorial é uma aproximação. Ele pega os k mais próximos, mas "mais próximo" ≠ "mais relevante". Pense: você busca "política de férias" e o top-5 traz o chunk da política (bom), mas também chunks sobre "ferias comerciais" (irrelevante), "férias coletivas" (parcial), etc. O LLM recebe tudo isso e tenta sintetizar. Resultado: confusão, alucinação, ou pior — responde com o chunk errado porque ele veio primeiro.
💡 ANALOGIA: É como pedir 5 livros na biblioteca por título parecido e receber 1 que você queria e 4 que não têm nada a ver. Você lê os 5 e fica confuso. Re-ranking é como um bibliotecário que relê os 5 e te entrega só o bom.
❓ PERGUNTA PARA A TURMA: "Vocês usam re-rank hoje? Quantos?" (provavelmente minoria — motivar Seção G)
⚠️ ERROS COMUNS: Aumentar k (top-10, top-20) PIORA o problema. Mais contexto ≠ melhor. Sem re-rank, mais chunks = mais ruído.
➡️ TRANSIÇÃO: "Mas a pior falha é não saber que está falhando."

---

### Slide 13 — Falha 4: Sem Avaliação, Você Está Cego

**Título**: Falha 4: Sem Avaliação, Você Está Cego
**Objetivo**: Mostrar que sem métricas não há como saber se o RAG está bom.
**Conteúdo**:
- "Funciona na minha máquina" ≠ funciona em produção
- Sem métricas: melhoria é adivinhação
- Métricas que importam: faithfulness, answer relevance, context precision/recall
- Sem dataset de holdout: não há como detectar regressão
- Preview da solução: Ragas, TruLens, DeepEval (Seção H)

**Diagrama**: Pessoa vendada tentando melhorar RAG (D3)
**Animação**: Pessoa vendada caminhando em círculos
**Imagem**: Ícone de pessoa vendada
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esta é a falha mais subestimada. Sem métricas, você não sabe se sua mudança melhorou ou piorou o RAG. Você muda o chunking, "parece melhor" nas 3 perguntas que testou, mas pode ter regredido em 100 outras. Sem dataset de holdout, não há regressão detectável. Sem faithfulness, não há garantia de grounding. Esta é a diferença entre RAG de hobby e RAG de produção.
💡 ANALOGIA: É como tentar melhorar uma receita sem provar o resultado. Você muda o sal, acha que ficou melhor, mas não sabe porque não tem padrão de comparação. Dataset de holdout é o padrão; faithfulness é o paladar.
❓ PERGUNTA PARA A TURMA: "Vocês têm dataset de holdout para avaliar RAG hoje?" (provavelmente <30%)
⚠️ ERROS COMUNS: Alunos avaliam só "a resposta parece certa". Isso é subjetivo e enviesado. Precisamos de métricas automáticas e reproduzíveis.
➡️ TRANSIÇÃO: "Essas 4 falhas alimentam um mito perigoso."

---

### Slide 14 — O Mito "Vector DB Resolve Tudo" + Casos Problemáticos

**Título**: O Mito "Vector DB Resolve Tudo"
**Objetivo**: Desconstruir o mito e mostrar casos onde RAG ingênuo falha.
**Conteúdo**:
- O mito: "só joga no vector DB e funciona"
- A realidade: vector DB é uma peça, não a solução
- **Casos problemáticos**:
  - Dados tabulares: embeddings não capturam estrutura de tabela → usar SQL + texto
  - Multilingual: mesma ideia em idiomas diferentes → distância vetorial alta → embeddings multilingual
  - Multi-modal: texto + imagem + tabela → exigem estratégias diferentes → CLIP, GPT-4V
- **Pergunta**: *Qual o pior tipo de falha — não responder ou responder errado com confiança?*

**Diagrama**: 3 casos problemáticos em grid (D4)
**Animação**: Casos aparecem um a um
**Imagem**: Ícones de tabela, globo (multilingual), imagem+texto
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: "Vector DB resolve tudo" é o mito mais caro da indústria de IA. Vector DB é excelente para busca semântica em texto livre, mas falha em três cenários crônicos: dados tabulares (tabela não é texto), multilingual (cross-lingual exige modelos específicos), e multimodal (imagem precisa de vision embeddings). Em todos esses casos, a solução não é "vector DB melhor" — é estratégia diferente.
💡 ANALOGIA: É como dizer "Excel resolve tudo". Excel é ótimo para planilhas, mas péssimo para edição de vídeo, design gráfico ou programação. Vector DB é uma ferramenta — não a solução universal.
❓ PERGUNTA PARA A TURMA: "Qual o pior tipo de falha — não responder ou responder errado com confiança?" (deixar debater — resposta esperada: responder errado, porque o usuário age sobre informação falsa)
⚠️ ERROS COMUNS: Alunos tentam embedar tabelas como texto. Funciona mal. SQL retrieval é melhor para dados estruturados.
➡️ TRANSIÇÃO: "Agora que sabemos onde falha, vamos construir a primeira evolução: Adaptive RAG."

---

## SEÇÃO C — Adaptive RAG (Slides 15-23 · 12 min)

---

### Slide 15 — [SEÇÃO] Adaptive RAG

**Título**: 2 — Adaptive RAG: Decidir Quando Recuperar
**Objetivo**: Transição visual para a primeira evolução do RAG.
**Conteúdo**: "2 — Adaptive RAG: Decidir Quando Recuperar"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "2" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A primeira evolução: em vez de SEMPRE recuperar, o sistema decide SE recuperar. Parece simples, mas resolve dois problemas: reduz latência/custo em perguntas triviais, e evita "contaminar" a resposta com docs irrelevantes. Adaptive RAG é o ponto de partida — sempre comece aqui.
➡️ TRANSIÇÃO: "Primeiro: a ideia central."

---

### Slide 16 — A Ideia: Decidir Quando Recuperar

**Título**: Decidir Quando Recuperar
**Objetivo**: Mostrar que nem toda pergunta precisa de retrieval.
**Conteúdo**:
- **RAG ingênuo**: SEMPRE recupera, mesmo para "Quem é o presidente do Brasil?"
- **Adaptive RAG**: classificador decide se precisa recuperar
- **Três caminhos**:
  - Não precisa → responder direto (LLM puro)
  - Pergunta simples → recuperar top-3
  - Pergunta complexa → recuperar + query rewrite
- **Benefício**: menos latência e custo em perguntas triviais

**Diagrama**: Comparação "sempre recupera" vs "decide se recupera"
**Animação**: Lado esquerdo (sempre recupera) aparece, depois direito (decide)
**Imagem**: Ícone de bifurcação
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A observação chave: MUITAS perguntas não precisam de retrieval. "Quem é o presidente do Brasil?" — o GPT-4 sabe. "Qual a fórmula da água?" — sabe. Recuperar docs para essas perguntas adiciona latência, custo, e RISCO — porque os docs recuperados podem ser irrelevantes e confundir o modelo. Adaptive RAG adiciona um classificador na frente: "esta pergunta precisa de retrieval?" Se sim, recupera; se não, responde direto.
💡 ANALOGIA: É como um médico triagista. Nem todo paciente precisa de exames — alguns são resolvidos na consulta. O triagista decide quem precisa de exame (retrieve) e quem não precisa (responde direto). RAG ingênuo manda TODO paciente para exame — caro e ineficiente.
❓ PERGUNTA PARA A TURMA: "Pensem numa pergunta que o modelo sabe sem retrieval." (deixar responder — capitais, datas históricas, ciência básica)
⚠️ ERROS COMUNS: Alunos acham que "sempre recuperar" é mais seguro. Não é — recuperação irrelevante é uma forma de ruído que prejudica a resposta.
➡️ TRANSIÇÃO: "Mas quando decidimos recuperar, quanto recuperar?"

---

### Slide 17 — Decidir Quanto Recuperar

**Título**: Decidir Quanto Recuperar
**Objetivo**: Mostrar que a quantidade de chunks deve ser dinâmica.
**Conteúdo**:
- Top-k fixo (ex.: sempre 5) é subótimo
- **Pergunta factual**: 1-2 chunks bastam
- **Pergunta analítica**: 5-10 chunks podem ser necessários
- Estratégia: classificar complexidade → ajustar k dinamicamente
- **Trade-off**: mais chunks = mais contexto = mais custo + mais ruído

**Diagrama**: Sliding scale de k (1 → 10) com tipos de pergunta
**Animação**: Slider move de 1 para 10 conforme complexidade aumenta
**Imagem**: Régua com marcadores
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A segunda decisão: não só SE recuperar, mas QUANTO recuperar. Top-k fixo é preguiça arquitetural. Pergunta factual ("qual a capital da França?") precisa de 1 chunk. Pergunta analítica ("compare as políticas de férias de 2023 e 2024") pode precisar de 10 chunks. Classificar a complexidade e ajustar k dinamicamente economiza custo e reduz ruído. Mas atenção: mais chunks = mais contexto = mais custo E mais chance de trazer irrelevante.
💡 ANALOGIA: É como pedir referências em uma pesquisa. Pergunta simples precisa de 1 fonte. Tese de doutorado precisa de 50. Pedir sempre 5 é arbitrário.
⚠️ ERROS COMUNS: Alunos aumentam k sem re-rank. Resultado: top-20 com 3 bons e 17 ruins. Mais contexto ≠ melhor.
➡️ TRANSIÇÃO: "Como classificamos a complexidade? Estratégias de routing."

---

### Slide 18 — Estratégias de Routing por Complexidade

**Título**: Estratégias de Routing por Complexidade
**Objetivo**: Apresentar estratégias de classificação de perguntas.
**Conteúdo**:
- Routing por regras: keywords, comprimento da pergunta
- Routing por LLM: classificador zero-shot ("esta pergunta precisa de retrieval?")
- Routing por complexidade: simples / média / complexa
- Routing por fonte: base local vs web vs KG
- LangGraph: `RouteQuery` node com conditional edges

**Diagrama**: Árvore de decisão de routing
**Animação**: Árvore ramifica a partir da pergunta
**Imagem**: Fluxograma de decisão
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O classificador pode ser tão simples quanto regras (se tem "política", "regras", "processo" → recuperar) ou tão sofisticado quanto um LLM zero-shot. O sweet spot é geralmente um LLM leve (GPT-4o-mini, Claude Haiku) classificando com structured output. LangGraph torna isso trivial: um nó `route_query` com conditional edges.
💡 ANALOGIA: É como o sistema de triagem de uma central de atendimento. Regras simples ("se é faturamento → setor A") são rápidas mas limitadas. Um atendente humano (LLM) é mais flexível mas mais caro. O sweet spot é regras para casos óbvios + LLM para ambíguos.
⚠️ ERROS COMUNS: Alunos usam LLM para classificar perguntas óbvias. Regras bastam para "quem é X?" → direto. Reserve LLM para ambiguidade.
➡️ TRANSIÇÃO: "Vamos visualizar isso no diagrama."

---

### Slide 19 — Diagrama: Adaptive RAG

**Título**: Adaptive RAG — Diagrama
**Objetivo**: Visualizar o fluxo completo do Adaptive RAG.
**Conteúdo**:
- Fluxo: pergunta → classificador → (direto | simples | complexa) → gerar → resposta
- Classificador decide: responder direto, retrieve top-3, ou retrieve + query rewrite
- Fonte: LangGraph examples — `adaptive_rag`

**Diagrama**: `12-Diagrams/ETHAGT06/adaptive-rag.mmd` (D5)
**Animação**: Caminhos acendem um a um a partir do classificador
**Imagem**: Diagrama mermaid renderizado
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Este é o diagrama canônico do Adaptive RAG. Observem: o coração é o classificador (nó de decisão). Ele ramifica em 3 caminhos: direto (LLM puro, sem retrieval), simples (retrieve top-3), e complexa (retrieve + query rewrite). Todos convergem para "gerar resposta". A beleza é a simplicidade: 1 decisão, 3 caminhos. Implementar isso em LangGraph são ~50 linhas de código.
💡 ANALOGIA: É como um restaurante com 3 cardápios. O garçom (classificador) olha o cliente e decide: cliente apressado → prato rápido (direto); cliente normal → menu completo (retrieve); cliente gourmet → menu do chef (retrieve + rewrite).
❓ PERGUNTA PARA A TURMA: "Qual desses 3 caminhos vocês acham que será mais usado na prática?" (resposta: depende do caso de uso, mas geralmente 'simples' é o mais comum)
⚠️ ERROS COMUNS: Alunos implementam classificador muito complexo. Comece com 3 classes (direto/simples/complexa) e ajuste com dados.
➡️ TRANSIÇÃO: "Vamos concretizar com exemplos reais."

---

### Slide 20 — Exemplo Prático: Quando Responder Direto

**Título**: Quando Responder Direto
**Objetivo**: Concretizar a decisão com exemplos reais.
**Conteúdo**:
- "Quem é o presidente do Brasil?" → responder direto (conhecimento paramétrico)
- "Qual a política de férias para estagiários?" → recuperar (conhecimento específico)
- "Compare a política de férias de 2023 com a de 2024" → recuperar + query rewrite
- O classificador pode errar — por isso CRAG existe (próxima seção)

**Diagrama**: 3 cards com exemplos e decisões
**Animação**: Cards aparecem um a um com seta para o caminho escolhido
**Imagem**: 3 cards coloridos
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vamos praticar a decisão. Primeira pergunta: "Quem é o presidente do Brasil?" — conhecimento paramétrico do GPT-4, não precisa de retrieval. Segunda: "Qual a política de férias para estagiários?" — conhecimento específico da empresa, precisa de retrieval simples. Terceira: "Compare as políticas de 2023 e 2024" — complexa, precisa de retrieval + query rewrite (duas buscas). O ponto crucial: o classificador pode ERRAR. E quando erra, não há correção — por isso CRAG existe.
💡 ANALOGIA: É como um GPS que decide a rota. Às vezes escolhe a via expressa (certo), às vezes escolhe um atalho que é um beco sem saída (errado). Sem correção, você fica preso. CRAG é o GPS que recalcula a rota.
⚠️ ERROS COMUNS: Alunos confiam 100% no classificador. A real: ~85% de acerto é bom, mas os 15% de erro precisam de correção (CRAG/Self-RAG).
➡️ TRANSIÇÃO: "Como implementar isso? Vamos ver o código."

---

### Slide 21 — Implementação: Classificador com LangGraph

**Título**: Implementação: Adaptive RAG em LangGraph
**Objetivo**: Mostrar como implementar o Adaptive RAG.
**Conteúdo**:
- LangGraph StateGraph com nós: `route_query`, `retrieve`, `generate`
- Edge condicional: `route_query` → `generate` (direto) ou `retrieve` (precisa retrieval)
- Snippet: `structured_output` com Pydantic para classificar
- Query rewrite node para perguntas complexas
- Referência: LangGraph `adaptive_rag` example

**Diagrama**: `12-Diagrams/ETHAGT06/adaptive-rag.mmd` sobreposto ao código (D6)
**Animação**: Código aparece; nó correspondente acende no diagrama
**Imagem**: Split — código à esquerda, grafo à direita
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Em LangGraph, Adaptive RAG é um StateGraph simples. O nó `route_query` usa um LLM com structured output (Pydantic) para classificar a pergunta em 3 categorias. O conditional edge direciona para o caminho certo. O nó `retrieve` faz a busca. O nó `generate` cria a resposta. Query rewrite, se necessário, é um nó extra antes do retrieve. Total: ~50-80 linhas de código.
💡 ANALOGIA: É como montar um circuito com interruptores. Cada nó é um componente; cada edge é uma ligação. O conditional edge é um interruptor que muda o fluxo.
⚠️ ERROS COMUNS: Alunos colocam lógica de classificação no prompt do generate. Não — separe em nó próprio (`route_query`), fica testável e observável.
➡️ TRANSIÇÃO: "Mas Adaptive RAG tem limitações. Quais?"

---

### Slide 22 — Limitações do Adaptive RAG

**Título**: Limitações do Adaptive RAG
**Objetivo**: Ser honesto sobre os trade-offs.
**Conteúdo**:
- O classificador pode errar (falso negativo: não recupera quando deveria)
- Não avalia a qualidade dos docs recuperados — confia cegamente
- Não tem fallback se a base local não tem a resposta
- Não corrige: se recuperou lixo, gera com lixo
- → Motivação para CRAG (próxima seção)

**Diagrama**: Lista de limitações com ícones de alerta
**Animação**: Limitações aparecem uma a uma com ícone de alerta
**Imagem**: Ícones de aviso amarelo
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Adaptive RAG resolve o problema de "recuperar quando não precisa", mas NÃO resolve "recuperar lixo". Se o classificador diz "precisa recuperar" e o retrieve retorna chunks ruins, o Adaptive RAG gera com lixo. Sem avaliação de relevância, sem fallback, sem correção. É exatamente essa lacuna que CRAG preenche.
💡 ANALOGIA: É como um médico que sabe QUANDO pedir exames (Adaptive), mas não sabe interpretar resultados ruins. Ele pede o exame, recebe um laudo confuso, e prescreve com base nele mesmo assim. CRAG é o médico que valida o laudo.
➡️ TRANSIÇÃO: "Vamos praticar a decisão antes de avançar."

---

### Slide 23 — Exercício Rápido: Responder Direto ou Recuperar?

**Título**: Exercício: Direto ou Recuperar?
**Objetivo**: Praticar a decisão de routing.
**Conteúdo**:
- 5 perguntas rápidas — votar: "direto" ou "recuperar":
  1. "O que é Python?" → direto
  2. "Qual a política de home office da Etho?" → recuperar
  3. "Quem escreveu Dom Casmurro?" → direto
  4. "Compare as APIs de dois produtos internos" → recuperar + rewrite
  5. "Qual a temperatura de ebulição da água?" → direto
- Votação rápida (mãos levantadas)

**Diagrama**: 5 cards com perguntas
**Animação**: Perguntas aparecem uma a uma
**Imagem**: Cards coloridos
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vamos praticar. Para cada pergunta, levantem a mão para "direto" ou "recuperar". Vou rápido.
❓ PERGUNTA PARA A TURMA: Votar em cada uma das 5. Anotar divergências.
⚠️ ERROS COMUNS: A pergunta 4 (comparação) costuma gerar dúvida. Resposta: recuperar + rewrite, porque precisa de duas buscas (um produto, depois o outro) e query rewrite ajuda.
➡️ TRANSIÇÃO: "Vocês acabaram de fazer o trabalho do classificador do Adaptive RAG. Agora, e se o retrieval trouxer lixo? CRAG."

---

## SEÇÃO D — Corrective RAG / CRAG (Slides 24-34 · 15 min)

---

### Slide 24 — [SEÇÃO] Corrective RAG (CRAG)

**Título**: 3 — Corrective RAG (CRAG): Avaliar Antes de Confiar
**Objetivo**: Transição visual para a correção de recuperação.
**Conteúdo**: "3 — Corrective RAG (CRAG): Avaliar Antes de Confiar"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "3" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A segunda evolução: CRAG adiciona um avaliador de relevância. Em vez de confiar cegamente nos docs recuperados, o CRAG avalia cada um e decide: usar, corrigir, ou buscar em outro lugar (web). É o "controle de qualidade" que faltava no Adaptive.
➡️ TRANSIÇÃO: "A ideia central do CRAG."

---

### Slide 25 — A Ideia: Avaliar Antes de Confiar

**Título**: Avaliar Antes de Confiar
**Objetivo**: Mostrar que CRAG adiciona um avaliador de relevância.
**Conteúdo**:
- **Adaptive RAG**: decide SE recuperar, mas confia nos docs recuperados
- **CRAG**: recupera, AVALIA a relevância dos docs, e corrige se necessário
- **Três caminhos após avaliação**:
  1. Docs relevantes → usar e gerar
  2. Docs parcialmente relevantes → refinar (knowledge refinement)
  3. Docs irrelevantes → buscar na web (fallback)
- Fonte: Yan et al., arXiv:2401.15884

**Diagrama**: Adaptive (confia) vs CRAG (avalia) (D7)
**Animação**: Comparação lado a lado; CRAG adiciona o bloco "avaliador"
**Imagem**: Fluxograma com novo nó
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A observação do CRAG: Adaptive RAG decide SE recuperar, mas depois confia cegamente no que recuperou. Se o retrieve trouxer lixo, o Adaptive gera com lixo. CRAG adiciona um passo crucial: AVALIAR os docs recuperados antes de gerar. Se são bons, usa. Se são parcialmente bons, refina (extrai só o útil). Se são ruins, busca na web. Três caminhos, um avaliador.
💡 ANALOGIA: É como um cozinheiro que prova os ingredientes antes de cozinhar. Adaptive RAG pega os ingredientes e cozinha direto. CRAG prova: se estão bons, cozinha; se alguns estão estragados, descarta e usa só os bons; se todos estão estragados, vai ao mercado (web).
❓ PERGUNTA PARA A TURMA: "Em qual caso de vocês o CRAG seria útil?" (deixar responder)
⚠️ ERROS COMUNS: Alunos acham que CRAG é "adaptive com web". Não — o coração é o AVALIADOR, não o web fallback.
➡️ TRANSIÇÃO: "Como funciona o avaliador?"

---

### Slide 26 — O Retrieval Evaluator (Grau de Relevância)

**Título**: O Retrieval Evaluator
**Objetivo**: Explicar como o avaliador classifica os docs.
**Conteúdo**:
- Avaliador: LLM ou modelo leve que classifica cada doc recuperado
- **Três classes de relevância**: `correto` / `ambíguo` / `incorreto`
- Score de relevância agregado decide o caminho:
  - Maioria correta → usar
  - Mistura → refinar
  - Maioria incorreta → web search
- Implementação: prompt estruturado ou modelo fine-tuned

**Diagrama**: Avaliador classificando docs em 3 buckets
**Animação**: Docs caem em 3 buckets coloridos
**Imagem**: 3 cestos (verde, amarelo, vermelho)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O avaliador é o coração do CRAG. Para cada doc recuperado, ele atribui uma classe: `correto` (relevante), `ambíguo` (parcialmente), ou `incorreto` (irrelevante). Pode ser um LLM com prompt estruturado (Pydantic) ou um modelo fine-tuned leve. A agregação dos scores decide o caminho: maioria correta → usa direto; mistura → refina; maioria incorreta → web. O paper original usa um modelo treinado, mas na prática prompting funciona bem.
💡 ANALOGIA: É como um jurado em um tribunal. Cada jurado (avaliador) vota: culpado, inocente, ou dúvida. A maioria decide a sentença (caminho). Prompt é o jurado leigo; modelo fine-tuned é o juiz experiente.
⚠️ ERROS COMUNS: Alunos usam threshold binário (relevante/não). 3 classes (correto/ambíguo/incorreto) são mais informativas e permitem o caminho "refinar".
➡️ TRANSIÇÃO: "Vamos ver os 3 caminhos em detalhe."

---

### Slide 27 — Três Caminhos: Usar / Corrigir / Web

**Título**: Três Caminhos: Usar / Corrigir / Web
**Objetivo**: Visualizar os três caminhos do CRAG.
**Conteúdo**:
- **Caminho 1 (relevante)**: usar docs diretamente → gerar resposta
- **Caminho 2 (ambíguo)**: knowledge refinement — extrair apenas partes relevantes
- **Caminho 3 (irrelevante)**: web search como fallback → gerar com web results
- Trigger de fallback: quando a base local não tem a resposta

**Diagrama**: Fluxograma com 3 ramificações (D7)
**Animação**: Ramificações aparecem uma a uma
**Imagem**: 3 caminhos coloridos (verde, amarelo, azul)
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Os 3 caminhos do CRAG. Caminho 1 (verde): docs são relevantes, usa direto — equivale ao RAG ingênuo mas com confirmação de qualidade. Caminho 2 (amarelo): docs são parcialmente relevantes, knowledge refinement extrai só o útil (decompor em sentenças, re-avaliar, filtrar). Caminho 3 (azul): docs são irrelevantes, web search como fallback. O web search só ativa quando a base local falha — é o plano B, não o padrão.
💡 ANALOGIA: É como um pesquisador. Caminho 1: achou a referência perfeita, usa. Caminho 2: achou um artigo parcialmente útil, extrai só a parte relevante. Caminho 3: não achou nada na biblioteca, vai para o Google Scholar (web).
➡️ TRANSIÇÃO: "Vamos ver o fluxo completo no diagrama."

---

### Slide 28 — Diagrama: CRAG Flow

**Título**: CRAG Flow — Diagrama
**Objetivo**: Visualizar o fluxo completo do CRAG.
**Conteúdo**:
- Fluxo: query → retrieve (KB local) → avaliador → (sim/ambíguo/não) → gerar → resposta
- O avaliador é o coração do CRAG
- Web search só é acionado quando docs locais são irrelevantes
- Fonte: arXiv:2401.15884; LangGraph example `crag`

**Diagrama**: `12-Diagrams/ETHAGT06/crag-flow.mmd` (D7)
**Animação**: Caminhos acendem um a um a partir do avaliador
**Imagem**: Diagrama mermaid renderizado
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O diagrama canônico do CRAG. Observem: o fluxo começa como o RAG ingênuo (query → retrieve), mas adiciona o nó "avaliador" (retrieve evaluator). O avaliador ramifica em 3: "sim" (usar), "ambíguo" (combinar local + web), "não" (web search). Todos convergem para "gerar resposta". A chave: o avaliador é uma camada de controle de qualidade entre retrieve e generate.
💡 ANALOGIA: É como uma esteira de fábrica com estação de inspeção. O produto passa pela inspeção (avaliador); se aprovado, segue (usar); se parcial, vai para retrabalho (refinar); se reprovado, vai para fornecedor alternativo (web).
❓ PERGUNTA PARA A TURMA: "Qual caminho vocês acham que será mais comum na prática?" (resposta: 'sim' se a base é boa; 'ambíguo' é o mais interessante)
⚠️ ERROS COMUNS: Alunos acham que CRAG sempre busca na web. Não — web é o ÚLTIMO recurso, só quando a base local falha completamente.
➡️ TRANSIÇÃO: "Vamos detalhar cada caminho, começando pelo feliz."

---

### Slide 29 — Caminho 1: Usar (Docs Relevantes)

**Título**: Caminho 1: Usar (Docs Relevantes)
**Objetivo**: Detalhar o caminho "feliz" do CRAG.
**Conteúdo**:
- Avaliador classifica como `correto` → docs vão direto para geração
- Equivale ao RAG ingênuo, mas com confirmação de qualidade
- É o caminho mais comum quando a base é boa e a pergunta é clara
- Latência: mínima (só o overhead do avaliador)

**Diagrama**: Caminho verde no fluxograma
**Animação**: Caminho verde acende
**Imagem**: Setas verdes
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O caminho feliz. O avaliador diz "correto" para a maioria dos docs, e eles vão direto para o gerador. É o equivalente ao RAG ingênuo, mas com uma diferença crucial: agora SABEMOS que os docs são bons, porque o avaliador confirmou. Em uma base bem curada, este será o caminho mais comum (~80%). O overhead é só uma chamada de LLM a mais (o avaliador).
💡 ANALOGIA: É como o controle de qualidade que aprova 95% dos produtos. Parece desperdício, mas quando ele REJEITA os 5% defeituosos, evita recall caro.
➡️ TRANSIÇÃO: "E quando os docs são parcialmente bons?"

---

### Slide 30 — Caminho 2: Corrigir (Docs Parciais) — Knowledge Refinement

**Título**: Caminho 2: Corrigir (Knowledge Refinement)
**Objetivo**: Detalhar o caminho de correção.
**Conteúdo**:
- Avaliador classifica como `ambíguo` → docs têm partes relevantes e irrelevantes
- Knowledge refinement: extrair apenas as partes relevantes de cada doc
- Técnicas: decompor em sentenças, re-avaliar, filtrar
- Resultado: contexto limpo para o gerador
- **Trade-off**: mais um step de LLM = mais latência e custo

**Diagrama**: Doc bruto → filtro → doc limpo
**Animação**: Doc bruto entra; filtro remove partes; doc limpo sai
**Imagem**: Ícone de funil/peneira
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O caminho de correção. O avaliador diz "ambíguo" — os docs têm partes boas e ruins. Knowledge refinement é a solução: decompor cada doc em sentenças, re-avaliar cada sentença individualmente, e ficar só com as relevantes. O resultado é um contexto limpo. Trade-off: mais uma chamada de LLM (custo + latência), mas a qualidade da resposta melhora significativamente.
💡 ANALOGIA: É como peneirar areia. Você tem uma pá de areia com pedras (doc com partes irrelevantes). Passa na peneira (refinement) e fica só com a areia fina (sentenças relevantes). Demora mais, mas o resultado é melhor.
⚠️ ERROS COMUNS: Alunos tentam refinement sem re-avaliar sentenças. Sem re-avaliação, você só corta por heurística (ex.: tamanho), não por relevância.
➡️ TRANSIÇÃO: "E quando os docs são completamente irrelevantes? Web search."

---

### Slide 31 — Caminho 3: Web Search (Docs Irrelevantes) — Fallback

**Título**: Caminho 3: Web Search (Fallback)
**Objetivo**: Detalhar o fallback para web.
**Conteúdo**:
- Avaliador classifica como `incorreto` → base local não tem a resposta
- Web search: usar Tavily, SerpAPI, ou busca nativa do modelo
- Combinar web results com qualquer fragmento útil dos docs locais
- **Quando ativa**: base desatualizada, pergunta sobre evento recente, gap de cobertura
- **Pergunta**: *Quando CRAG decide buscar na web? Quando o avaliador diz "incorreto"*

**Diagrama**: Base local (vazia) → Web search → resposta
**Animação**: Base local aparece vazia; seta vai para web; web preenche
**Imagem**: Ícone de globo (web)
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O caminho do fallback. O avaliador diz "incorreto" para a maioria — a base local não tem nada útil. CRAG então busca na web (Tavily, SerpAPI, Brave, ou a busca nativa do modelo). O web search retorna resultados que vão para o gerador. Quando isso ativa? Três cenários: (1) base desatualizada (pergunta sobre evento recente), (2) gap de cobertura (pergunta fora do escopo da base), (3) base pequena demais. Web search é o plano B, não o padrão.
💡 ANALOGIA: É como uma enciclopédia física. Você consulta (retrieve); se não tem o verbete (avaliador diz incorreto), vai para a internet (web search). A enciclopédia é a base de conhecimento confiável; a internet é o complemento para o que falta.
❓ PERGUNTA PARA A TURMA: "Quando CRAG decide buscar na web?" (resposta direta: quando o avaliador classifica os docs como irrelevantes)
⚠️ ERROS COMUNS: Alunos ativam web search sempre. Não — só quando a base local falha. Web search adiciona latência, custo, e risco (web results podem ser não confiáveis).
➡️ TRANSIÇÃO: "Vamos ver o código do avaliador."

---

### Slide 32 — Implementação: O Avaliador em Código

**Título**: Implementação: O Avaliador
**Objetivo**: Mostrar como implementar o retrieval evaluator.
**Conteúdo**:
- Snippet: função `grade_documents(state)` que classifica cada doc
- Pydantic model: `GradeDocuments` com `binary_score: "yes" | "no"`
- LangGraph node: `grade_documents` → conditional edge → `generate` | `web_search`
- Referência: LangGraph `crag` example

**Diagrama**: Code block com highlight no avaliador
**Animação**: Linhas do código destacam-se
**Imagem**: Syntax highlighting
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O avaliador em código. A função `grade_documents(state)` recebe o estado (com os docs recuperados), itera sobre cada doc, chama um LLM com structured output (Pydantic `GradeDocuments` com `binary_score: "yes" | "no"`), e acumula os docs aprovados. O conditional edge decide: se há docs aprovados, vai para `generate`; se nenhum, vai para `web_search`. Em LangGraph, isso são ~30 linhas.
💡 ANALOGIA: É como um filtro de spam de email. Cada email (doc) passa pelo classificador (avaliador); se é spam (irrelevante), descarta; se é legítimo (relevante), mantém. Se todos são spam, busca em outro lugar (web).
⚠️ ERROS COMUNS: Alunos usam threshold contínuo em vez de binário. Binário (yes/no) é mais simples e funciona bem. Se quiser 3 classes, use `correto/ambíguo/incorreto`.
➡️ TRANSIÇÃO: "Vamos sistematizar a comparação."

---

### Slide 33 — Comparação: RAG Ingênuo vs CRAG

**Título**: RAG Ingênuo vs CRAG
**Objetivo**: Sistematizar os ganhos do CRAG.
**Conteúdo**:
- **Tabela comparativa**:
  - RAG ingênuo: confia cegamente, sem fallback, sem avaliação
  - CRAG: avalia relevância, refina se parcial, web se irrelevante
- **Custo**: CRAG adiciona 1-2 chamadas de LLM (avaliador + possível refinement)
- **Ganho**: respostas com grounding muito maior
- **Quando NÃO usar CRAG**: latência crítica e base de alta qualidade

**Diagrama**: Tabela comparativa colorida
**Animação**: Linhas da tabela aparecem
**Imagem**: Tabela 2 colunas
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A comparação direta. RAG ingênuo: barato, rápido, mas confia cegamente. CRAG: adiciona 1-2 chamadas de LLM (avaliador + possível refinement), mas ganha controle de qualidade e fallback. O custo extra é ~$0.005 por query (avaliador). Em 10k queries/dia, são $50/dia — geralmente vale pelo ganho em confiabilidade.
💡 ANALOGIA: É como a diferença entre comprar sem marca (ingênuo, barato, arriscado) e comprar com certificação (CRAG, um pouco mais caro, garantido).
⚠️ ERROS COMUNS: Alunos usam CRAG em latência crítica (chatbot real-time com SLA <500ms). Nesses casos, o overhead do avaliador pode não caber.
➡️ TRANSIÇÃO: "Quando CRAG brilha e quando falha?"

---

### Slide 34 — Quando CRAG Brilha e Quando Falha

**Título**: CRAG — Quando Brilha e Quando Falha
**Objetivo**: Dar critérios práticos de uso.
**Conteúdo**:
- **Brilha**: base com cobertura parcial, perguntas diversas, dados que envelhecem
- **Falha**: avaliador erra (falso positivo de relevância), web search retorna lixo
- **Melhoria**: combinar CRAG com re-ranking (Seção G)
- **Limitação**: não reflete sobre a PRÓPRIA resposta — isso é Self-RAG (próxima seção)

**Diagrama**: Prós e contras em duas colunas
**Animação**: Prós e contras aparecem
**Imagem**: Polegar para cima (brilha) / para baixo (falha)
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: CRAG brilha quando a base tem cobertura parcial (algumas perguntas a base responde, outras não) e quando os dados envelhecem (web fallback para dados recentes). Falha quando o avaliador erra (falso positivo — classifica lixo como relevante) ou quando o web search retorna lixo. A limitação fundamental: CRAG avalia os DOCS, mas não avalia a RESPOSTA. Se a resposta gerada alucina sobre docs bons, CRAG não percebe. Isso é Self-RAG.
💡 ANALOGIA: CRAG é como um inspetor de matéria-prima. Ele garante que os ingredientes são bons. Mas não prova o prato final. Self-RAG prova o prato.
➡️ TRANSIÇÃO: "Vamos ao próximo nível: Self-RAG."

---

## SEÇÃO E — Self-RAG (Slides 35-44 · 13 min)

---

### Slide 35 — [SEÇÃO] Self-RAG

**Título**: 4 — Self-RAG: Modelo que Reflete sobre Recuperação
**Objetivo**: Transição visual para Self-RAG.
**Conteúdo**: "4 — Self-RAG: Modelo que Reflete sobre Recuperação"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "4" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A terceira evolução: Self-RAG. Se CRAG avalia os docs, Self-RAG avalia TUDO — docs, resposta, e o próprio processo. É o modelo refletindo sobre si mesmo.
➡️ TRANSIÇÃO: "A ideia central."

---

### Slide 36 — A Ideia: Modelo que Reflete sobre Recuperação

**Título**: Modelo que Reflete sobre Recuperação
**Objetivo**: Mostrar que Self-RAG vai além de avaliar docs — avalia a si mesmo.
**Conteúdo**:
- **CRAG**: avalia os docs recuperados (antes de gerar)
- **Self-RAG**: o modelo reflete sobre TODO o processo — antes, durante e depois de gerar
- Modelo treinado para emitir tokens de reflexão que controlam o fluxo
- Fonte: Asai et al., arXiv:2310.11511
- **Diferença chave**: Self-RAG julga se a resposta é suportada pelos docs

**Diagrama**: CRAG (avalia docs) vs Self-RAG (avalia docs + resposta) (D8)
**Animação**: Comparação; Self-RAG adiciona bloco "avalia resposta"
**Imagem**: Reflexo (self-reflection)
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A diferença fundamental. CRAG avalia os docs (antes de gerar). Self-RAG vai além: avalia a própria resposta (depois de gerar). Se a resposta não é totalmente suportada pelos docs, regenera. Se não tem utilidade, refaz. É o modelo se auto-avaliando em cada etapa. Isso é "self-reflection" — daí o nome.
💡 ANALOGIA: CRAG é como um cozinheiro que confere os ingredientes. Self-RAG é como um cozinheiro que confere os ingredientes, cozinha, PROVA o prato, e refaz se não ficou bom. É um loop de auto-avaliação.
❓ PERGUNTA PARA A TURMA: "Em qual caso vocês precisariam de Self-RAG em vez de CRAG?" (resposta: quando alucinação é inaceitável — jurídico, médico, financeiro)
⚠️ ERROS COMUNS: Alunos acham que Self-RAG é "CRAG com mais chamadas". Não — Self-RAG adiciona REFLEXÃO sobre a resposta (hallucination check), não só sobre os docs.
➡️ TRANSIÇÃO: "Como o modelo reflete? Tokens de reflexão."

---

### Slide 37 — Tokens de Reflexão

**Título**: Tokens de Reflexão do Self-RAG
**Objetivo**: Apresentar os tokens de reflexão do Self-RAG.
**Conteúdo**:
- `[Retrieve]` — decidir se precisa recuperar
- `[Retrieve(target)]` — decidir qual fonte recuperar
- `[Relevant]` / `[Irrelevant]` — julgar relevância do doc
- `[Fully supported]` / `[Partly supported]` / `[No support]` — julgar se a resposta é suportada
- `[Utility]` — julgar utilidade da resposta final
- Cada token controla uma decisão no pipeline

**Diagrama**: Lista de tokens com ícones e descrição
**Animação**: Tokens aparecem um a um
**Imagem**: Tokens estilizados como código
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Self-RAG original (Asai et al., 2023) é um modelo FINE-TUNED para emitir tokens especiais — os "reflection tokens". Cada token controla uma decisão: `[Retrieve]` decide se recupera; `[Relevant]` julga relevância do doc; `[Fully supported]` julga se a resposta tem grounding; `[Utility]` julga utilidade final. O modelo emite esses tokens DURANTE a geração, controlando o fluxo em tempo real. É elegante — a reflexão é embutida no modelo, não em prompts extras.
💡 ANALOGIA: É como um cirurgião que murmura checklist durante a operação: "[Anestesia?] ok. [Incisão?] ok. [Sangramento?] não. [Sutura?] ok." Os murmúrios (tokens) guiam a operação.
⚠️ ERROS COMUNS: Alunos tentam usar esses tokens com GPT-4. Não funcionam — GPT-4 não foi treinado para emiti-los. Para modelos não-treinados, usamos prompting (próximo slide).
➡️ TRANSIÇÃO: "Vamos ver o fluxo com tokens."

---

### Slide 38 — O Fluxo do Self-RAG

**Título**: Self-RAG — Fluxo com Tokens de Reflexão
**Objetivo**: Visualizar o fluxo completo com tokens de reflexão.
**Conteúdo**:
- Fluxo: pergunta → [Retrieve?] → se sim: recuperar → [Relevant?] → [Fully supported?] → resposta
- Se [No support]: regenerar ou recuperar mais
- O modelo decide em cada etapa via tokens de reflexão
- Fonte: arXiv:2310.11511

**Diagrama**: Fluxograma com tokens de reflexão nos edges (D8)
**Animação**: Tokens aparecem nos decision points
**Imagem**: Diagrama com tokens destacados
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O fluxo do Self-RAG. Observem os decision points: `[Retrieve?]` no início (como Adaptive), `[Relevant?]` depois do retrieve (como CRAG), e — o novo — `[Fully supported?]` depois de gerar. Se a resposta não é totalmente suportada, regenera. Se não tem utilidade, refaz. Cada decisão é um token emitido pelo modelo. É um pipeline cheio de checkpoints de auto-avaliação.
💡 ANALOGIA: É como um estudante fazendo prova com rubrica na mão. A cada questão, ele se pergunta: "preciso consultar o livro? ([Retrieve?])", "esta página é relevante? ([Relevant?])", "minha resposta está fundamentada? ([Fully supported?])". O estudante se auto-avalia em cada etapa.
❓ PERGUNTA PARA A TURMA: "Qual desses tokens é o mais importante?" (resposta: `[Fully supported]` — é o que diferencia Self-RAG de CRAG)
⚠️ ERROS COMUNS: Alunos acham que todos os tokens são obrigatórios. São opcionais — você pode usar só `[Retrieve]` e `[Fully supported]` se quiser.
➡️ TRANSIÇÃO: "Mas como funciona o modelo treinado?"

---

### Slide 39 — Modelo Treinado: Como Funciona

**Título**: Self-RAG Original — Modelo Treinado
**Objetivo**: Explicar a versão original (modelo fine-tuned).
**Conteúdo**:
- Self-RAG original: LLM fine-tuned para emitir tokens de reflexão
- Treinamento: dados com anotações de reflexão (relevância, suporte, utilidade)
- **Vantagem**: reflexão embutida no modelo, sem prompts extras
- **Desvantagem**: requer modelo específico — não funciona com GPT-4, Claude, etc.
- Por isso: adaptação para modelos não-treinados via prompting

**Diagrama**: Pipeline de treinamento do Self-RAG
**Animação**: Pipeline de treinamento animado
**Imagem**: Ícone de rede neural
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O Self-RAG ORIGINAL é um modelo fine-tuned. Os autores pegaram um LLM (Llama 2, etc.) e treinaram com dados anotados com os tokens de reflexão. Resultado: um modelo que emite os tokens naturalmente, sem prompts extras. A vantagem é elegância e eficiência (uma passada). A desvantagem é óbvia: você fica preso àquele modelo. Não pode usar GPT-4, Claude, ou qualquer modelo proprietário. Por isso, a adaptação via prompting é mais prática para a maioria.
💡 ANALOGIA: É como um músico treinado em jazz. Ele improvisa naturalmente, sem pensar. Mas se você quer jazz de um músico clássico, precisa dar partitura (prompting). O modelo treinado é o jazzista; prompting é a partitura.
⚠️ ERROS COMUNS: Alunos tentam baixar "Self-RAG model". Existe (Llama-Self-RAG), mas é pequeno e menos capaz que GPT-4. Para produção, prompting em modelo forte é melhor.
➡️ TRANSIÇÃO: "Como adaptar para qualquer modelo? Prompting."

---

### Slide 40 — Adaptação para Modelos Não-Treinados: Prompting

**Título**: Self-RAG via Prompting
**Objetivo**: Mostrar como aplicar Self-RAG sem modelo treinado.
**Conteúdo**:
- Ideia: replicar os tokens de reflexão via prompting estruturado
- Prompt pede ao LLM para:
  1. Decidir se precisa recuperar
  2. Avaliar relevância de cada doc
  3. Avaliar se a resposta é suportada
  4. Regenerar se não suportada
- **Custo**: múltiplas chamadas de LLM
- **Benefício**: funciona com qualquer modelo (GPT-4, Claude, Llama)

**Diagrama**: Mapeamento token → prompt
**Animação**: Tokens à esquerda, prompts à direita, setas conectando
**Imagem**: Tabela de mapeamento
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Para usar Self-RAG com GPT-4 ou Claude, replicamos os tokens via prompting. Em vez de o modelo emitir `[Fully supported]` naturalmente, fazemos um prompt estruturado: "Dada a resposta e os docs, julgue se a resposta é totalmente suportada. Retorne JSON `{supported: fully|partly|no}`." Se "no", regeneramos. O custo é múltiplas chamadas (decisão de retrieve + avaliação de docs + avaliação de resposta + possível regeneração), mas o benefício é flexibilidade — funciona com qualquer modelo.
💡 ANALOGIA: É como traduzir uma receita de chef para iniciante. O chef faz tudo de memória (modelo treinado). O iniciante precisa de passo-a-passo explícito (prompting). O resultado é o mesmo, o método é diferente.
⚠️ ERROS COMUNS: Alunos fazem um prompt gigante pedindo todas as reflexões de uma vez. Melhor separar em chamadas (cada reflexão é um nó no grafo) — fica testável e observável.
➡️ TRANSIÇÃO: "Vamos ver o código."

---

### Slide 41 — Implementação: Self-RAG via Prompt

**Título**: Implementação: Self-RAG via Prompt
**Objetivo**: Mostrar código prático de Self-RAG via prompting.
**Conteúdo**:
- Snippet: prompt estruturado que pede reflexão
- Pydantic models: `GradeDocuments`, `GradeHallucinations`, `GradeAnswer`
- LangGraph nodes: `grade_documents` → `generate` → `grade_hallucination` → `grade_answer` | `regenerate`
- Loop de regeneração com max_retries
- Referência: LangGraph `self_rag` example

**Diagrama**: Code block + grafo LangGraph lado a lado
**Animação**: Código e grafo aparecem juntos
**Imagem**: Split código/grao
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A implementação em LangGraph. Os Pydantic models definem as saídas estruturadas: `GradeDocuments` (relevância dos docs), `GradeHallucinations` (se a resposta é suportada), `GradeAnswer` (se a resposta é útil). Os nós do grafo: `grade_documents` (como CRAG), `generate`, `grade_hallucination` (o novo!), `grade_answer`. Se hallucination falha, regenera (com max_retries para evitar loop infinito). Total: ~100-150 linhas em LangGraph.
💡 ANALOGIA: É como uma redação com rubrica. Cada parágrafo passa por critérios: "tem evidência? (GradeDocuments)", "a tese é suportada? (GradeHallucinations)", "responde ao tema? (GradeAnswer)". Se falha, reescreve.
⚠️ ERROS COMUNS: Alunos não colocam max_retries na regeneração. Resultado: loop infinito se o modelo nunca consegue "fully supported". Sempre use guardrail.
➡️ TRANSIÇÃO: "Vamos sistematizar as 3 arquiteturas."

---

### Slide 42 — Comparação: Adaptive vs CRAG vs Self-RAG

**Título**: Adaptive vs CRAG vs Self-RAG
**Objetivo**: Sistematizar as três arquiteturas.
**Conteúdo**:
- **Tabela comparativa**:

| Checkpoint | Adaptive | CRAG | Self-RAG |
|---|---|---|---|
| Decide SE recuperar | ✅ | ❌ | ✅ |
| Avalia docs | ❌ | ✅ | ✅ |
| Avalia resposta (hallucination) | ❌ | ❌ | ✅ |

- Complexidade crescente: Adaptive < CRAG < Self-RAG
- Custo crescente: Adaptive < CRAG < Self-RAG
- Próximo passo: Agentic RAG (agente dirige tudo)

**Diagrama**: Tabela 3-colunas com checkpoints destacados (D9)
**Animação**: Checkpoints acendem um a um
**Imagem**: Tabela colorida
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A sistematização. Adaptive decide SE recuperar (1 checkpoint). CRAG adiciona avaliação de docs (2 checkpoints). Self-RAG adiciona avaliação da resposta (3 checkpoints). Cada nível adiciona reflexão e controle — mas também custo e complexidade. A regra: comece com Adaptive, suba só com evidência de insuficiência. A maioria dos casos se resolve com Adaptive + CRAG. Self-RAG é para casos críticos (jurídico, médico).
💡 ANALOGIA: É como níveis de inspeção. Adaptive é "checagem visual". CRAG é "inspeção com instrumentos". Self-RAG é "auditoria completa". Você não faz auditoria em todo produto — só nos críticos.
❓ PERGUNTA PARA A TURMA: "Qual vocês usariam no projeto de vocês?" (deixar justificarem)
⚠️ ERROS COMUNS: Alunos vão direto para Self-RAG "para ser seguro". Overkill. Adaptive + CRAG resolvem 80% dos casos.
➡️ TRANSIÇÃO: "Quando usar Self-RAG?"

---

### Slide 43 — Quando Usar Self-RAG

**Título**: Quando Usar Self-RAG
**Objetivo**: Dar critérios práticos de uso.
**Conteúdo**:
- **Use Self-RAG quando**:
  - Alucinação é inaceitável (jurídico, médico, financeiro)
  - Você pode pagar o custo de múltiplas chamadas
  - Precisa de garantia de que a resposta é suportada
- **Não use quando**:
  - Latência é crítica
  - Base é pequena e confiável
  - Caso de uso tolera imprecisão

**Diagrama**: Árvore de decisão
**Animação**: Árvore ramifica
**Imagem**: Fluxograma de decisão
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Critérios práticos. Self-RAG vale quando alucinação é inaceitável E você pode pagar o custo. Jurídico, médico, financeiro — são os casos clássicos. Não vale quando latência é crítica (chatbot real-time), base é pequena e confiável, ou o caso tolera imprecisão (recomendação de filme, por exemplo).
💡 ANALOGIA: É como usar auditoria forense. Vale para fraudes milionárias (jurídico). Overkill para conferir se a conta do café está certa.
➡️ TRANSIÇÃO: "Vamos praticar."

---

### Slide 44 — Exercício: Self-RAG via Prompting

**Título**: Exercício — Adaptive vs Self-RAG
**Objetivo**: Praticar a adaptação de Self-RAG.
**Conteúdo**:
- **Cenário**: sistema de FAQ jurídico com 10.000 documentos
- Em duplas: quando usar Adaptive RAG vs Self-RAG?
- **Critérios**: tipo de pergunta, custo, qualidade esperada
- Escrever o prompt de reflexão para um doc recuperado
- 3 min discussão, 2 min compartilhar

**Diagrama**: Caixa de discussão
**Animação**: Caixa aparece
**Imagem**: Ícone de duplas
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Exercício em duplas. Cenário: FAQ jurídico. Discutam: Adaptive ou Self-RAG? Pensem no tipo de pergunta (simples vs complexa), custo (orçamento), qualidade esperada (alucinação aceitável?). Depois, escrevam um prompt de reflexão para um doc recuperado — estilo Self-RAG via prompting.
❓ PERGUNTA PARA A TURMA: "Em 3 min, discutam em duplas. Depois, 2 duplas compartilham."
⚠️ ERROS COMUNS: Alunos escolhem Self-RAG "por segurança". Em FAQ jurídico, Adaptive + CRAG pode bastar. Self-RAG só se houver risco regulatório.
➡️ TRANSIÇÃO: "Vamos ao próximo bloco: Agentic RAG, onde o agente dirige tudo."

---

> **Fim da Parte 1 (Slides 1-44). Continua em `03-slides-detalhados-parte2.md` (Slides 45-85).**
