# ETHAGT05 — Slides Detalhados + Notas do Professor (Parte 1: Slides 1-35)

> Universidade Etho · Especialização em Programação Agêntica
> Cada slide contém: título, objetivo, conteúdo, notas do professor, diagrama, animação, imagem, tempo.

---

## SEÇÃO A — Abertura (Slides 1-6 · 8 min)

---

### Slide 1 — Capa

**Título**: ETHAGT05 — Memória de Agentes
**Objetivo**: Identificar a aula, o professor e o contexto dentro da especialização.
**Conteúdo**:
- ETHAGT05 — Memória de Agentes (working · episódica · semântica · procedural)
- Universidade Etho · Especialização em Programação Agêntica
- Fase B — Memória, Contexto e Persistência · 25 h
- Professor · Data

**Diagrama**: Logo Etho (canto sup. esquerdo) + imagem de fundo abstrata (camadas de memória empilhadas)
**Animação**: Fade in do título (300ms)
**Imagem**: Fundo `etho-dark` (#0F1E2D) com pattern sutil de camadas sobrepostas
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Bem-vindos. Esta é a aula de memória de agentes — o módulo que transforma um agente amnésico em um agente com contexto acumulado, aprendizado e persistência. Até agora nossos agentes viviam no "agora" — esqueciam tudo ao fechar a sessão. Hoje vamos arquitetar sistemas de memória que dão a agentes continuidade entre sessões, recall de eventos passados, e conhecimento consolidado sobre o mundo e o usuário.
💡 ANALOGIA: É a diferença entre um hóspede de hotel (esquece cada conversa ao fechar a porta) e um amigo de longa data (lembra do que conversamos, do que gosta, do que planejamos).
❓ PERGUNTA PARA A TURMA: "Quantos de vocês já ficaram frustrados com o ChatGPT 'esquecendo' algo no meio de uma conversa longa?" (levantar mãos — a maioria vai levantar)
⚠️ ERROS COMUNS: Alunos chegam achando que "memória" é só vector DB. Não — memória é uma arquitetura com 4 camadas. Vector DB é só uma delas.
➡️ TRANSIÇÃO: "Vamos começar definindo o que vocês vão conseguir fazer ao final desta aula."

---

### Slide 2 — Objetivos do Módulo

**Título**: Objetivos do Módulo
**Objetivo**: Deixar claro o que o aluno deve conseguir FAZER ao final da aula.
**Conteúdo**:
- **Objetivo geral**: Arquitetar sistemas de memória que dão a agentes persistência, contexto acumulado e aprendizado — para além da context window
- **Objetivos específicos**:
  1. Distinguir tipos de memória (working, episódica, semântica, procedural) e quando cada é necessária
  2. Implementar persistência via checkpointer (Postgres/SQLite/Redis)
  3. Gerenciar a janela de contexto: sumarização, eviction, janela deslizante
  4. Construir memória vetorial para recall episódico
  5. Lidar com consistência, privacidade e custo de memória

**Diagrama**: 5 ícones representando cada objetivo (camadas, banco, tesoura, lupa, escudo)
**Animação**: Objetivos aparecem um a um (on click)
**Imagem**: Ícones minimalistas em `etho-accent` (#E85D2F)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Cada objetivo é mensurável. Não é "entender tipos de memória" — é "distinguir" e "decidir quando usar cada". Não é "saber o que é checkpointer" — é "implementar" persistência real. Se ao final da aula você não consegue fazer essas 5 coisas, eu falhei como professor. Vamos revisar estes objetivos no final.
💡 ANALOGIA: É como um checklist de arquitetura. O engenheiro não diz "entendo memória" — ele justifica: "para este caso, working + checkpointer bastam; para aquele, preciso de vector DB com eviction".
❓ PERGUNTA PARA A TURMA: "Qual desses objetivos vocês acham mais desafiador?" (deixar responder — costuma ser #3 ou #5)
⚠️ ERROS COMUNS: Alunos confundem "memória" com "vector DB". O objetivo #1 é entender que há 4 camadas. O objetivo #4 é construir UMA delas. Não misturem.
➡️ TRANSIÇÃO: "Antes de saber o que vamos fazer, vamos saber onde estamos no mapa da especialização."

---

### Slide 3 — Competências Desenvolvidas

**Título**: Competências Desenvolvidas
**Objetivo**: Conectar a aula ao Framework Etho de competências.
**Conteúdo**:

| Competência | Nível ao final | Próximo nível em |
|---|---|---|
| C1 Programação Agêntica | **A** (Avançado) | ETHAGT07, ETHAGT09 |
| C4 Agent Memory | **I** (Intermediário) | ETHAGT14, ETHAGT15 |
| C5 AgentOps & Avaliação | **B** (Básico) | ETHAGT12 |
| C6 Agent Security | **B** (Básico) | ETHAGT13 |

**Diagrama**: Radar chart com 4 eixos mostrando nível B/I/A
**Animação**: Radar aparece com wipe (left-to-right, 500ms)
**Imagem**: Badge visual por competência (círculos coloridos)
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O Framework Etho tem 6 competências em 3 níveis (Básico, Intermediário, Avançado). Este módulo eleva C1 ao nível Avançado — você já era Intermediário em ETHAGT01-04; agora você consegue justificar arquiteturas de memória completas. C4 — Agent Memory — atinge Intermediário aqui, que é o foco da aula: você conhece as 4 camadas, implementa checkpointer e vector DB, e sabe os trade-offs. C5 e C6 ficam em Básico: você toca observabilidade de memória e segurança (PII, esquecimento), mas o aprofundamento vem em ETHAGT12 e ETHAGT13.
💡 ANALOGIA: É como aprender a construir uma casa. ETHAGT01-04 ensinaram a fundação e a estrutura. Hoje vocês aprendem o sistema de memória da casa — onde guardar, como recuperar, quando descartar. Avançado em C1 significa que você agora decide a planta toda.
⚠️ ERROS COMUNS: Alunos acham que "Básico" em C6 (Security) significa que segurança não importa aqui. Importa — PII em memória de longo prazo é crítico. Básico significa que é introdução; o aprofundamento vem em ETHAGT13.
➡️ TRANSIÇÃO: "Vamos ver como esta aula está estruturada para entregar essas competências."

---

### Slide 4 — Agenda

**Título**: Agenda da Aula
**Objetivo**: Mostrar o roteiro da aula com tempos estimados.
**Conteúdo**:
- **Bloco 1 (45 min)**:
  - Abertura (8 min) — objetivos, motivação, contexto
  - Tipos de Memória (12 min) — as 4 camadas + MemGPT
  - Checkpointer (15 min) — estado persistente, backends, DEMO
  - Gerenciamento de Contexto (10 min) — custo, sumarização, eviction
  - Intervalo (5 min)
- **Bloco 2 (45 min)**:
  - Memória Vetorial (12 min) — embedding, recall, re-ranking, Lab 2
  - Semântica e Grafos (8 min) — consolidação, KG, Generative Agents
  - Produção (8 min) — consistência, PII, esquecimento, custo
  - Fechamento (12 min) — boas práticas, quiz, projeto, Q&A

**Diagrama**: Timeline horizontal com 8 seções coloridas
**Animação**: Timeline cresce da esquerda para direita (500ms)
**Imagem**: Ícones de relógio por seção
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A aula tem dois blocos. O primeiro estabelece a teoria (4 camadas), a persistência (checkpointer) e a gestão de contexto. O segundo é mais prático: memória vetorial, consolidação semântica, desafios de produção (PII, custo), e fechamento. Há uma DEMO ao vivo no Slide 28 — checkpointer em Postgres. O quiz final tem 3 perguntas — é individual e serve para vocês auto-avaliarem.
💡 ANALOGIA: É como construir uma biblioteca. Primeiro definimos os tipos de prateleira (4 camadas), depois como preservar os livros (checkpointer), depois como gerenciar o espaço (eviction), depois como catalogar (vector DB), depois como consolidar conhecimento (semântica), e finalmente como manter a biblioteca segura e útil (produção).
⚠️ ERROS COMUNS: Alunos chegam atrasados e perdem a Seção B (4 camadas). Avisar que a Seção B é a fundação — sem ela, o resto não faz sentido.
➡️ TRANSIÇÃO: "Vamos começar pelo porquê. Por que memória é tão crítica?"

---

### Slide 5 — Motivação: O Agente Amnésico

**Título**: O Agente Amnésico
**Objetivo**: Criar tensão cognitiva — agentes sem memória são inúteis em sessões longas.
**Conteúdo**:
- "Agente sem memória é um hóspede que esquece cada conversa ao fechar a porta"
- **Exemplos de falha**:
  - Assistente de produtividade: "lembra do projeto X?" — não sabe
  - Agente de suporte: pergunta a mesma coisa a cada ticket
  - Coding agent: não lembra das convenções do seu repositório
  - NPC de jogo: esquece que você já o ajudou ontem
- **Sem memória**: não aprende, não melhora, não personaliza
- **Pergunta**: *Quanto contexto você acha que um assistente pessoal precisa reter?*

**Diagrama**: Split — esquerda: agente reiniciando (amnésia) | direita: agente evoluindo (memória acumulada)
**Animação**: Split — lado esquerdo aparece primeiro, depois lado direito
**Imagem**: Ícone de "reset" (esquerda) vs ícone de "livro/cadernos empilhados" (direita)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O agente sem memória é tragicamente limitado. Ele é ótimo em uma conversa isolada, mas não acumula nada. Toda vez que você fecha a sessão, ele volta à estaca zero. Isso quebra casos de uso centrais: assistente pessoal (precisa lembrar preferências), suporte (precisa saber histórico de tickets), coding agent (precisa saber convenções do projeto). Sem memória, o agente é um consultor novo a cada interação — caro e frustrante.
💡 ANALOGIA: Imagine ter um médico que te atende bem em cada consulta, mas esquece seu histórico médico a cada visita. Você teria que explicar tudo de novo: alergias, cirurgias, medicações. Inviável a longo prazo. A memória é o que transforma uma consulta episódica em um acompanhamento contínuo.
❓ PERGUNTA PARA A TURMA: "Quanto contexto você acha que um assistente pessoal precisa reter?" (deixar responder — normalmente: meses a anos)
⚠️ ERROS COMUNS: Alunos acham que "context window maior resolve". Não resolve. 200k tokens é ~150k palavras — um livro médio. Não dá para 1 ano de interações diárias. E mesmo que coubesse, custo e qualidade degradam.
➡️ TRANSIÇÃO: "Essa limitação sempre existiu. Mas por que só agora temos soluções viáveis?"

---

### Slide 6 — Contexto: Por Que Memória Agora

**Título**: Por Que Memória Agora
**Objetivo**: Explicar a confluência histórica que tornou memória de agentes viável e necessária.
**Conteúdo**:
- **Linha do tempo**:
  - 2020: GPT-3 (2k tokens, sem tools, sem persistência)
  - 2022: 4k-8k tokens (GPT-3.5, ChatGPT)
  - 2023: 16k-32k tokens + tool calling + LangGraph com checkpointer
  - 2024: 128k-200k tokens + agent frameworks com persistência nativa
  - 2025: MemGPT, Zep, A-MEM, Letta (memória como camada de primeira classe)
- **Confluência de 4 fatores**:
  1. Context windows maiores (128k+)
  2. Custo menor (GPT-4o-mini, Claude Haiku)
  3. Frameworks com checkpointer (LangGraph, OpenAI SDK)
  4. Vector DBs acessíveis (Qdrant, Chroma, Pinecone)
- **Mas**: context window maior ≠ memória resolvida (custo, latência, falta de estrutura)
- **Marco**: MemGPT (arXiv:2310.08560) — LLMs como sistemas operacionais

**Diagrama**: Timeline horizontal com marcos + 4 setas convergindo para "Memória viável"
**Animação**: Marcos aparecem sequencialmente (on click)
**Imagem**: Convergência de 4 rios em um lago
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Memória de agentes não é ideia nova — sistemas especialistas dos anos 80 já tinham "memória" (regras + fatos). Mas três coisas mudaram: (1) context windows cresceram o suficiente para manter estado rico em uma sessão; (2) custo baixou o suficiente para múltiplas chamadas + persistência; (3) frameworks como LangGraph trouxeram checkpointer nativo, e vector DBs ficaram acessíveis. O paper MemGPT (2023) é o marco porque formaliza a analogia LLM-como-SO — context window como RAM, memória persistente como disco. Isso inspirou Zep, A-MEM, Letta.
💡 ANALOGIA: É como a invenção do disco rígido. Computadores sem armazenamento persistente (só RAM) eram limitados a uma sessão. O disco rígido permitiu acumular trabalho entre sessões. Memória de agentes é o "disco rígido" dos LLMs.
❓ PERGUNTA PARA A TURMA: "Qual desses 4 fatores vocês acham que foi o gatilho mais recente?" (Resposta: frameworks com checkpointer — vector DBs e context windows já existiam, mas sem um modelo de estado persistente, não havia como integrá-los)
⚠️ ERROS COMUNS: Alunos acham que memória é "nova tecnologia". Vector DBs existem há anos; checkpointer é padrão em sistemas distribuídos há décadas. O que é novo é a integração com LLMs de forma prática.
➡️ TRANSIÇÃO: "Agora que sabemos por que estamos aqui, vamos às 4 camadas de memória."

---

## SEÇÃO B — Tipos de Memória (Slides 7-16 · 12 min)

---

### Slide 7 — [SEÇÃO] Tipos de Memória

**Título**: 1 — Tipos de Memória
**Objetivo**: Transição visual para o bloco de fundamentos de memória.
**Conteúdo**: Número "1" grande + "Tipos de Memória"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "1" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Início do bloco de fundamentos. Vamos responder: quais são os tipos de memória que um agente precisa? Não é um — são quatro. Working, episódica, semântica, procedural. Cada uma tem um propósito, um storage típico, e um padrão de recuperação. Vamos uma por uma, depois integraremos.
➡️ TRANSIÇÃO: "Primeiro: a camada mais básica — working memory, a context window."

---

### Slide 8 — Working Memory: A Context Window

**Título**: Working Memory — A Context Window
**Objetivo**: Apresentar a camada mais básica de memória.
**Conteúdo**:
- **Working memory** = context window do LLM (tokens visíveis no prompt)
- **Efêmera**: desaparece ao fim da sessão (ou da chamada)
- **Limitada**: 4k a 200k tokens (modelo-dependente)
- **Estratégias**:
  - Token budget (orçamento fixo por sessão)
  - Sliding window (manter só as últimas N mensagens)
  - System prompt + últimas N mensagens (preserva instrução)
- **Custo**: cada token no contexto é processado a cada chamada (input cost)

**Diagrama**: Caixa "Context Window" com tokens entrando e saindo
**Animação**: Tokens entram e saem da janela
**Imagem**: Balde com tokens, entrada por cima, saída por baixo
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A context window é a memória de trabalho — o que o LLM "vê" no momento. É como a memória de curto prazo humana: você segura informação enquanto trabalha, mas solta ao terminar. A questão é que cada token no contexto custa dinheiro e processamento a cada chamada. Se você tem 50k tokens de contexto e faz 10 chamadas em um loop, você paga por 500k tokens de input — mesmo que a maior parte não tenha mudado. Estratégias como sliding window e token budget são essenciais para controle de custo.
💡 ANALOGIA: É como uma mesa de trabalho. A context window é a superfície da mesa — só cabe uma certa quantidade de papéis. Se a mesa enche, você precisa arquivar (evict) ou fotocopiar/resumir antes de arquivar. O que sai da mesa não some — vai para a gaveta (memória persistente).
❓ PERGUNTA PARA A TURMA: "Se um modelo tem 200k tokens de context window, isso é muito ou pouco?" (Resposta: para uma sessão, é muito. Para 1 ano de uso diário, é quase nada — ~1 livro por dia.)
⚠️ ERROS COMUNS: Alunos acham que context window é "memória". É working memory — efêmera e custa por uso. Memória de longo prazo é outra coisa (checkpointer + vector DB).
➡️ TRANSIÇÃO: "E mesmo com context windows grandes, há um problema: nem tudo no contexto é igualmente útil."

---

### Slide 9 — Limites da Context Window

**Título**: Limites da Context Window
**Objetivo**: Mostrar que mesmo context windows grandes não resolvem memória.
**Conteúdo**:
- **"Lost in the Middle"** (arXiv:2307.03172): LLMs ignoram informação no meio do contexto
  - Recall accuracy em curva U: alta no início, baixa no meio, alta no fim
- **Custo cresce** com o tamanho do contexto (linearmente em API, mas significativo)
- **Latência aumenta** com contexto maior (mais tokens para processar)
- **200k tokens ≠ 200k tokens úteis**: ruído, redundância, irrelevância
- **Conclusão**: context window é working memory, não memória de longo prazo

**Diagrama**: Gráfico de "recall accuracy" vs posição no contexto (curva U)
**Animação**: Curva U aparece com wipe
**Imagem**: Curva U de "Lost in the Middle" (Liu et al., 2023)
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O paper "Lost in the Middle" (Liu et al., 2023) mostrou empiricamente que LLMs perdem precisão no meio de contextos longos. Se você coloca um fato crítico no meio de 100k tokens de contexto, o modelo tem alta chance de ignorá-lo. Isso destrói a ilusão de que "context window grande resolve tudo". Mesmo com 1M de tokens, a informação no meio será sub-utilizada. A lição é: contexto deve ser curado (relevante), não acumulado (tudo). Por isso precisamos de estratégias de eviction e recall seletivo.
💡 ANALOGIA: É como uma biblioteca. Se você tem 10 livros, acha qualquer um rapidamente. Se tem 10 milhões sem catalogação, você se perde — mesmo que todos estejam "lá". Mais contexto sem estrutura = menos útil, não mais.
❓ PERGUNTA PARA A TURMA: "Já notaram o ChatGPT esquecendo algo que estava no meio de uma conversa longa?" (a maioria vai concordar — é o Lost in the Middle)
⚠️ ERROS COMUNS: Alunos acham que "custo cresce quadraticamente porque attention é O(n²)". Não — em API, custo é linear em tokens. O que cresce é latência e degradação de qualidade. Computação interna é O(n²), mas isso é problema do provedor, não do seu bolso.
➡️ TRANSIÇÃO: "Então working memory não basta. Precisamos de memória de longo prazo. Comecemos pela episódica."

---

### Slide 10 — Memória Episódica: Eventos com Timestamp

**Título**: Memória Episódica — Eventos com Timestamp
**Objetivo**: Apresentar a memória de eventos passados.
**Conteúdo**:
- **Episódica** = registro de eventos com timestamp (o que aconteceu, quando)
- **Exemplo**: "Usuário perguntou sobre React hooks em 12/mar" → recall por similaridade
- **Armazenamento típico**: vector DB (embedding + metadata de tempo)
- **Recall**: "o que aconteceu antes que se pareça com X?"
- **Diferença de log**: episódica é recuperável por *significado*, não só por query estruturada
- **Inspirado em**: Tulving (1972) — memória episódica cognitiva

**Diagrama**: Timeline de eventos com embeddings ao lado
**Animação**: Eventos aparecem na timeline, embeddings destacados
**Imagem**: Linha do tempo com bolhas (eventos) e vetores (embeddings) ao lado
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Memória episódica é o registro de eventos — "o que aconteceu, quando, com quem". Em agentes, cada evento (mensagem, action, observation) é armazenado com timestamp e embedding. A recuperação é por similaridade semântica: "o que na minha memória se parece com a situação atual?" Isso é diferente de um log estruturado, onde você faz query SQL. Aqui você recupera por significado. É a base do que chamamos de "memória vetorial" e vamos aprofundar na Seção E.
💡 ANALOGIA: É como o seu diário pessoal. Você anota eventos com datas. Para lembrar, você não busca por "entrada com ID 1234" — você pensa "o que escrevi sobre aquela viagem?" e relê entradas similares. A memória episódica do agente funciona assim: busca por significado, não por chave estruturada.
❓ PERGUNTA PARA A TURMA: "Qual a diferença entre memória episódica e um log de banco de dados?" (Resposta: episódica é recuperável por significado via similaridade; log é recuperável por query estruturada. Episódica é fuzzy; log é exato.)
⚠️ ERROS COMUNS: Alunos acham que episódica é "log". Não — log é estruturado e query-able por SQL. Episódica é embedding-based e recall por similaridade. São complementares, não iguais.
➡️ TRANSIÇÃO: "Episódica armazena eventos. Mas eventos acumulados viram conhecimento — a memória semântica."

---

### Slide 11 — Memória Semântica: Fatos e Conhecimento

**Título**: Memória Semântica — Fatos e Conhecimento
**Objetivo**: Apresentar a memória de fatos consolidados.
**Conteúdo**:
- **Semântica** = fatos, conhecimento sobre o mundo/usuário (o que é verdade)
- **Exemplo**: "João é desenvolvedor Python" (fato, não evento)
- **Armazenamento típico**: KB estruturada, knowledge graph, tabela de perfil
- **Como surge**: consolidação da episódica (múltiplos eventos → um fato)
- **Diferença de episódica**: semântica não tem "quando", tem "o que é"
- **Inspirado em**: Tulving (1972) — memória semântica cognitiva

**Diagrama**: Transformação de eventos episódicos em fato semântico
**Animação**: Eventos convergem para um fato
**Imagem**: 3 balões (eventos) → seta de consolidação → 1 ícone (fato)
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Memória semântica armazena fatos — não eventos. "João é desenvolvedor Python" é um fato; "João perguntou sobre decorators em 12/mar" é um evento. Fatos não têm timestamp relevante — são verdade (até mudarem). Fatos surgem por consolidação: você observa vários eventos (João pergunta sobre Python, compartilha repositórios, pede ajuda com asyncio) e consolida: "João é dev Python". Vamos ver consolidação em detalhe na Seção F. O armazenamento típico é KB estruturada (JSON, SQLite) ou knowledge graph.
💡 ANALOGIA: É a diferença entre episódios de série (memória episódica) e a bíblia da série (memória semântica). Os episódios são eventos individuais com timestamps; a bíblia consolida: "quem são os personagens, o que é verdade sobre o mundo, quais as regras". Você consulta a bíblia para fatos estáveis; rele episódios para contexto específico.
❓ PERGUNTA PARA A TURMA: "'O usuário prefere respostas em português' — é episódica ou semântica?" (Resposta: semântica — é um fato estável sobre o usuário, não um evento)
⚠️ ERROS COMUNS: Alunos confundem episódica e semântica. Regra: se tem "quando", é episódica. Se é "o que é verdade", é semântica. Saldo bancário? Semântica (mas volátil). "João depositou R$100 ontem"? Episódica.
➡️ TRANSIÇÃO: "E para completar: a memória de 'como fazer' — procedural."

---

### Slide 12 — Memória Procedural: Skills Aprendidas

**Título**: Memória Procedural — Skills Aprendidas
**Objetivo**: Apresentar a memória de "como fazer".
**Conteúdo**:
- **Procedural** = sequências de actions para objetivos recorrentes (skills)
- **Exemplo**: "para deploy: rodar testes → build → push → deploy" (aprendido, não hardcoded)
- **Armazenamento típico**: biblioteca de playbooks, prompt templates, tool sequences
- **Como surge**: reflexão sobre sucessos/falhas (estilo Reflexion, arXiv:2303.11366)
- **Diferença das outras**: procedural é sobre *como agir*, não sobre *o que aconteceu* ou *o que é verdade*
- **Inspirado em**: Squire (memória de habilidades); Reflexion (Shinn et al.)

**Diagrama**: Loop de reflexão → skill extraída → biblioteca procedural
**Animação**: Loop gira, skill é extraída
**Imagem**: Ícone de engrenagem (skill) sendo adicionada a uma biblioteca
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Memória procedural armazena "como fazer" — sequências de actions que levam a um objetivo. Em agentes, isso aparece como playbooks, prompt templates, ou tool sequences aprendidas. Como surge? Reflexão: o agente tenta uma tarefa, falha, reflete ("o que deu errado?"), e extrai uma lição ("próxima vez, faça X antes de Y"). Essa lição vira uma skill na biblioteca procedural. O paper Reflexion (arXiv:2303.11366) formaliza esse ciclo. Diferença das outras memórias: procedural não é sobre "o que aconteceu" (episódica) nem "o que é verdade" (semântica) — é sobre "como agir".
💡 ANALOGIA: É como aprender a dirigir. Primeiro você pensa em cada passo (embreagem, marcha, acelerador) — working memory. Depois de muita prática, vira automático — procedural. No agente: primeira vez que ele faz deploy, pensa em cada step. Décima vez, ele tem um playbook. Vigésima vez, o playbook está refinado com lições aprendidas.
⚠️ ERROS COMUNS: Alunos confundem procedural com "tools". Tools são implementações fixas. Procedural é a sequência aprendida de *quando e como* usar tools. Você pode ter a tool `run_tests` sem ter a skill procedural "sempre rode testes antes de deploy".
➡️ TRANSIÇÃO: "Agora que vimos as 4 individualmente, vamos integrá-las."

---

### Slide 13 — As 4 Camadas: Visão Integrada

**Título**: As 4 Camadas de Memória
**Objetivo**: Mostrar as 4 camadas lado a lado e quando cada uma é necessária.
**Conteúdo**:

| Camada | O que armazena | Onde armazena | Como recupera | Quando usar |
|---|---|---|---|---|
| **Working** | Mensagens atuais | Context window | No prompt | Sempre (base) |
| **Episódica** | Eventos (com timestamp) | Vector DB | Similaridade + metadata | Recall de contexto |
| **Semântica** | Fatos (KB/KG) | KB / Knowledge Graph | Query estruturada | Verdade estável |
| **Procedural** | Skills (playbooks) | Playbook library | Match de objetivo | Tarefas repetidas |

**Diagrama**: Tabela comparativa colorida (4 colunas)
**Animação**: Colunas aparecem uma a uma (on click)
**Imagem**: 4 colunas coloridas em `etho-info`, `etho-accent`, `etho-success`, `etho-warning`
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: As 4 camadas não são alternativas — são complementares. Um agente completo usa todas, mas nem sempre todas são necessárias. Chatbot simples: só working. Assistente pessoal: working + episódica + semântica. Coding agent: working + episódica + procedural. NPC de jogo: working + episódica + procedural. A arte está em decidir quais camadas seu caso precisa. A regra geral: comece com working + checkpointer. Adicione episódica quando precisar de recall cross-sessão. Adicione semântica quando eventos acumulados virarem fatos. Adicione procedural quando o agente repete tarefas e pode aprender.
💡 ANALOGIA: É como os sistemas de memória de um profissional. Working: o que você está fazendo agora. Episódica: seu diário de projetos. Semântica: seu conhecimento geral da área. Procedural: suas habilidades e playbooks. Todos coexistem; você não apaga um para usar outro.
❓ PERGUNTA PARA A TURMA: "Para um chatbot de FAQ, quais camadas são necessárias?" (Resposta: working + semântica. Episódica e procedural são opcionais.)
⚠️ ERROS COMUNS: Alunos querem implementar as 4 camadas desde o dia 1. Não — comece com working + checkpointer. Adicione as outras conforme a necessidade surgir. Over-engineering de memória é anti-pattern.
➡️ TRANSIÇÃO: "Vamos visualizar a arquitetura integrada."

---

### Slide 14 — Diagrama: As 4 Camadas de Memória

**Título**: Arquitetura Integrada de Memória
**Objetivo**: Visualizar a arquitetura integrada de memória.
**Conteúdo**:
- Agente no centro, conectado às 4 camadas
- **Working** (context window, volátil)
- **Episódica** (vector DB, recall por similaridade)
- **Semântica** (KB/KG, fatos e relações)
- **Procedural** (skills, sequências de actions)
- Checkpointer persistindo o estado do agente

**Diagrama**: `12-Diagrams/ETHAGT05/memory-layers.mmd`
**Animação**: Camadas surgem do centro (Agente) para fora
**Imagem**: Diagrama mermaid renderizado
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Este é o slide-chave do bloco de fundamentos. Memorizem este diagrama. O agente no centro acessa 4 camadas de memória, cada uma com um storage e um padrão de recuperação distintos. O checkpointer (Postgres, Redis) persiste o *estado* do agente entre sessões — não é uma das 4 camadas, é a infraestrutura que permite o agente sobreviver entre sessões. Working é efêmera e sempre presente. As outras três são persistentes e opcionais (depende do caso de uso).
💡 ANALOGIA: É como a arquitetura de um cérebro digital. Working é o córtex pré-frontal (memória de trabalho agora). Episódica é o hipocampo (eventos). Semântica é o córtex temporal (fatos). Procedural são os gânglios da base (habilidades). Checkpointer é... bem, não tem análogo biológico — é a persistência que nosso cérebro não precisa (ele já é persistente).
⚠️ ERROS COMUNS: Alunos acham que checkpointer É uma camada de memória. Não — checkpointer persiste o *estado do grafo do agente* (messages, intermediate results, metadata). As 4 camadas são tipos de *conteúdo* memorizado. Checkpointer é infraestrutura de persistência.
➡️ TRANSIÇÃO: "Esta taxonomia é inspirada na cognição humana. Mas cuidado com o literalismo."

---

### Slide 15 — Inspiração Cognitiva sem Literalismo

**Título**: Inspiração Cognitiva sem Literalismo
**Objetivo**: Alertar contra a armadilha de copiar o cérebro literalmente.
**Conteúdo**:
- "A memória humana é inspiração, não especificação." — Paráfrase didática
- **Working** ↔ memória de trabalho (Baddeley, 1974)
- **Episódica/Semântica** ↔ Tulving (1972)
- **Procedural** ↔ memória de habilidades (Squire)
- **Mas**: LLMs não consolidam durante o sono, não têm hipocampo, não esquecem por razões biológicas
- **Aprendizado**: use a taxonomia como *framework de design*, não como modelo neural

**Diagrama**: Ícone de "cérebro" com seta para "arquitetura de software"
**Animação**: Seta aparece com wipe
**Imagem**: Cérebro estilizado → engrenagens de software
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A taxonomia working/episódica/semântica/procedural vem da psicologia cognitiva — Tulving (1972), Baddeley (1974), Squire. É útil como framework de design porque organiza os tipos de memória que um agente precisa. MAS: LLMs não são cérebros. Eles não consolidam memória durante o "sono", não têm hipocampo, não esquecem por razões biológicas. Copiar o cérebro literalmente leva a arquiteturas bizarras (ex.: simular "sono" para consolidação). Use a taxonomia como mapa conceitual, não como blueprint neural.
💡 ANALOGIA: É como a asa do avião. Inspirada na asa do pássaro (aerodinâmica), mas não é uma asa de pássaro — não bate, é fixa, tem turbinas. A inspiração guia; a engenharia entrega.
❓ PERGUNTA PARA A TURMA: "Inspiração cognitiva é framework de design ou modelo neural?" (Resposta: framework de design. Use para organizar pensamento, não para replicar biologia.)
⚠️ ERROS COMUNS: Alunos tentam replicar fenômenos cognitivos (ex.: "esquecimento orgânico", "consolidação noturna") sem benefício prático. Foque no que importa: o agente precisa reter, recuperar e esquecer de forma útil.
➡️ TRANSIÇÃO: "A melhor instância dessa taxonomia em produção é o MemGPT."

---

### Slide 16 — MemGPT: LLMs como Sistemas Operacionais

**Título**: MemGPT — LLMs como Sistemas Operacionais
**Objetivo**: Apresentar a analogia central do MemGPT como referência arquitetural.
**Conteúdo**:
- **MemGPT** (Packer et al., arXiv:2310.08560): LLM como SO
- **Context window** = RAM (limitada, rápida)
- **Memória persistente** = disco (ilimitada, lenta)
- O modelo **gerencia sua própria memória**: decide o que page-in / page-out
- **Self-editing memory**: o modelo atualiza suas próprias notas/perfil
- **Inspirou**: Zep, A-MEM, Letta

**Diagrama**: Analogia SO: RAM (context window) ↔ Disco (memória persistente)
**Animação**: Page-in/page-out animado entre RAM e disco
**Imagem**: Lado a lado: SO (RAM/DISCO/MMU) vs MemGPT (Context/Persistent/Self-editing)
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O MemGPT é o paper canônico de memória de agentes (out/2023). A ideia central: tratar o LLM como um sistema operacional. A context window é a RAM — limitada e rápida. A memória persistente é o disco — ilimitada e lenta. O modelo gerencia sua própria memória: ele decide (via function calls) o que carregar do disco para a RAM (page-in) e o que descarregar (page-out). Isso é self-editing memory — o modelo atualiza suas próprias notas, perfil, contexto. Inspirou Zep (memória de longo prazo em produção), A-MEM (memória agêntica), e Letta (framework de produção). A analogia SO é poderosa porque todo engenheiro entende page-in/page-out, caching, eviction.
💡 ANALOGIA: É como você gerenciando seu desktop. Você tem 10 abas abertas (RAM). Está lento. Você fecha as menos usadas (page-out) e mantém as ativas. Quando precisa de uma fechada, reabre (page-in). O MemGPT faz isso automaticamente, via function calls que o próprio modelo decide.
❓ PERGUNTA PARA A TURMA: "Se o modelo decide o que page-in/out, não há risco de ele decidir mal?" (Resposta: sim, e é um problema ativo de pesquisa. Mas a alternativa — gerenciar via código fixo — perde a adaptabilidade.)
⚠️ ERROS COMUNS: Alunos acham que MemGPT é "vector DB". Não — MemGPT é uma arquitetura de gestão de memória. Vector DB é um dos componentes possíveis (para a camada episódica).
➡️ TRANSIÇÃO: "Vimos as 4 camadas. Agora vamos à infraestrutura que permite persistência entre sessões: o checkpointer."

---

## SEÇÃO C — Checkpointer e Estado Persistente (Slides 17-29 · 15 min)

---

### Slide 17 — [SEÇÃO] Checkpointer e Estado Persistente

**Título**: 2 — Checkpointer e Estado Persistente
**Objetivo**: Transição para persistência de estado.
**Conteúdo**: "2 — Checkpointer e Estado Persistente"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "2" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Início do bloco de checkpointer. Vamos responder: por que precisamos de persistência de estado? Como o LangGraph modela isso? Quais backends existem? E como retomar (resume), reproduzir (replay) e ramificar (branch) execuções passadas? Tem uma DEMO ao vivo no final.
➡️ TRANSIÇÃO: "Primeiro: o problema que o checkpointer resolve."

---

### Slide 18 — O Problema: Estados Efêmeros

**Título**: Estados Efêmeros
**Objetivo**: Mostrar por que precisamos de persistência de estado.
**Conteúdo**:
- **Sem checkpointer**: agente perde todo estado ao reiniciar
- **Casos que quebram**:
  - Servidor reinicia → conversa perdida
  - HITL demora dias → contexto evaporou
  - Debug: não dá para reproduzir execução passada
  - A/B testing: não dá para voltar no tempo
- **Solução**: serializar estado em storage durável (a cada step)

**Diagrama**: Agente "morre" (estado perdido) vs agente "hiberna" (estado persistido)
**Animação**: Split — esquerdo (estado perdido), direito (estado persistido)
**Imagem**: Esquerda: agente "apagando" | Direita: agente "hibernando" com banco de dados
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Sem checkpointer, o agente é um ser efêmero. A cada restart, ele perde tudo — conversa, contexto, estado intermediário. Isso quebra casos reais: (1) servidor reinicia (deploy, crash) — conversa com usuário perdida; (2) HITL — o humano demora dias para aprovar, e quando volta, o contexto evaporou; (3) debug — você quer reproduzir um bug de ontem, mas não há estado salvo; (4) A/B testing — você quer voltar no tempo e tentar caminho diferente. A solução é serializar o estado do agente em storage durável, a cada step. Isso é o checkpointer.
💡 ANALOGIA: É como um videogame. Sem save: você morre e volta ao início. Com save: você continua de onde parou, dias depois. O checkpointer é o "save" do agente.
⚠️ ERROS COMUNS: Alunos acham que checkpointer é só "salvar mensagens". Não — checkpointer serializa o *estado completo do grafo* (messages + intermediate results + metadata + posição no grafo). É mais rico que só log.
➡️ TRANSIÇÃO: "Como o LangGraph modela isso?"

---

### Slide 19 — LangGraph Checkpointer: Conceito

**Título**: LangGraph Checkpointer — Conceito
**Objetivo**: Introduzir o modelo de checkpointer do LangGraph.
**Conteúdo**:
- **Checkpointer** = camada que serializa o estado do grafo a cada step
- **Estado** = qualquer objeto serializável (TypedDict, Pydantic, dataclass)
- Cada **node execution** → checkpoint gravado
- **`thread_id`** identifica a conversa/sessão
- **`checkpoint_id`** identifica o momento (versionado)
- Profundidade em ETHAGT03 (StateGraph)

**Diagrama**: Grafo com checkpoints em cada node
**Animação**: Checkpoints aparecem após cada node
**Imagem**: Grafo LangGraph com ícones de "save" em cada nó
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O LangGraph tem um modelo elegante de checkpointer. A cada vez que um node do grafo executa, o estado é serializado e gravado no backend (Postgres, SQLite, Redis). O `thread_id` identifica a conversa — é a chave que agrupa checkpoints de uma mesma sessão. O `checkpoint_id` identifica o momento — cada step tem um ID único, permitindo voltar a qualquer ponto. Isso habilita resume (continuar), replay (reproduzir) e branching (ramificar). Em ETHAGT03 vimos StateGraph; aqui aprofundamos a persistência.
💡 ANALOGIA: É como um save de videogame com slots. O `thread_id` é o slot (cada jogador tem o seu). O `checkpoint_id` é o momento do save (você pode ter múltiplos saves em um mesmo slot). Resume carrega o último; replay carrega um específico; branching cria um novo save a partir de um antigo.
⚠️ ERROS COMUNS: Alunos confundem thread_id com session_id. Em LangGraph, thread_id é o identificador da conversa/persistência; session_id é mais amplo (pode abranger múltiplas threads). Use thread_id como chave de agrupamento.
➡️ TRANSIÇÃO: "Mas o estado precisa ser serializável. Vamos ver como modelar isso."

---

### Slide 20 — Estado Serializável

**Título**: Estado Serializável
**Objetivo**: Mostrar como modelar estado serializável.
**Conteúdo**:
- **Estado deve ser JSON-serializable** (ou com serializer custom)
- **Padrão**: TypedDict com messages, intermediate results, metadata
- **Pegadinha**: objetos não-serializáveis (conexões DB, file handles, closures)
- **Solução**: separar estado serializável de recursos efêmeros

```python
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, START
from langgraph.checkpoint.postgres import PostgresSaver

class AgentState(TypedDict):
    messages: Annotated[list, add_messages]
    intermediate_results: dict
    metadata: dict
    schema_version: int

graph = StateGraph(AgentState)
checkpointer = PostgresSaver.from_conn_string(DB_URI)
app = graph.compile(checkpointer=checkpointer)
```

**Diagrama**: Code block com State definition
**Animação**: Highlight de linhas chave (TypedDict, checkpointer, compile)
**Imagem**: Syntax highlighting (tema dark)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O estado precisa ser serializável — pode virar JSON (ou bytes) para ir ao backend. O padrão é um TypedDict com messages (lista de mensagens), intermediate_results (resultados parciais), metadata (info auxiliar como user_id, session_id), e schema_version (para migração). A pegadinha: você não pode serializar conexões de DB, file handles, ou closures — esses são recursos efêmeros. A solução é separar: estado serializável vai no TypedDict; recursos efêmeros são injetados via `RunnableConfig` em runtime. Reparem no `schema_version` — vamos voltar a ele no Slide 27.
💡 ANALOGIA: É como salvar um jogo. Você pode salvar posição, inventário, HP (serializável). Mas não pode salvar "a conexão com o servidor" ou "o estado do controle" — esses são efêmeros. O checkpointer serializa o serializável; o runtime recria o efêmero.
⚠️ ERROS COMUNS: Alunos colocam objetos não-serializáveis no estado (ex.: `engine = create_engine(...)`) e quebram o checkpointer. Regra: se não vira JSON, não vai no estado.
➡️ TRANSIÇÃO: "Quais backends temos para gravar esses checkpoints?"

---

### Slide 21 — Backends: Postgres, SQLite, Redis

**Título**: Backends de Checkpointer
**Objetivo**: Apresentar as implementações de checkpointer disponíveis.
**Conteúdo**:
- **Postgres**: produção, multi-tenant, ACID, escalável
- **SQLite**: desenvolvimento local, single-node, zero-config
- **Redis**: baixa latência, TTL automático, ideal para sessões curtas
- **Outros**: MongoDB, DynamoDB (comunidade)
- **Critério**: durabilidade vs latência vs escala

**Diagrama**: 3 colunas com prós/contras
**Animação**: Colunas aparecem sequencialmente
**Imagem**: Logos de Postgres, SQLite, Redis
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O LangGraph oferece três backends oficiais de checkpointer. Postgres é a escolha de produção: ACID, multi-tenant, escala bem, é robusto. SQLite é para desenvolvimento: zero-config, roda em arquivo local, ideal para protótipos e debug. Redis é para casos de baixa latência: sessions curtas com TTL automático (dados expiram sozinhos). A escolha depende do trade-off: Postgres para durabilidade, Redis para velocidade, SQLite para simplicidade. Há backends de comunidade (MongoDB, DynamoDB), mas os três oficiais cobrem 95% dos casos.
💡 ANALOGIA: É como escolher meio de transporte. SQLite é uma bicicleta (simples, local, zero-config). Postgres é um carro de família (robusto, multiuso, escala). Redis é um foguete (rápido, mas volatile — TTL expira).
❓ PERGUNTA PARA A TURMA: "Qual backend você usaria para um agente em produção multi-tenant?" (Resposta: Postgres — ACID, escala, multi-tenant nativo)
➡️ TRANSIÇÃO: "Vamos comparar os três lado a lado."

---

### Slide 22 — Comparação de Backends

**Título**: Comparação de Backends
**Objetivo**: Sistematizar trade-offs dos backends de checkpointer.
**Conteúdo**:

| Eixo | Postgres | SQLite | Redis |
|---|---|---|---|
| **Durabilidade** | ✅ Alta | ✅ Alta (disco local) | ⚠️ Média |
| **Latência** | ⚠️ Média | ✅ Baixa | ✅ Baixíssima |
| **Multi-tenant** | ✅ Sim | ❌ Não | ✅ Sim |
| **ACID** | ✅ Sim | ✅ Sim | ⚠️ Parcial |
| **TTL nativo** | ❌ Não | ❌ Não | ✅ Sim |
| **Custo** | ⚠️ Médio | ✅ Zero | ⚠️ Médio |
| **Operação** | ⚠️ Requer DBA | ✅ Zero-config | ⚠️ Requer ops |
| **Uso típico** | Produção | Desenvolvimento | Cache de sessão |

- **Regra**: comece com SQLite (dev), vá para Postgres (prod), use Redis para cache de sessão

**Diagrama**: Tabela comparativa colorida
**Animação**: Linhas aparecem uma a uma
**Imagem**: Tabela com cores semânticas (verde/amarelo/vermelho)
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vamos sistematizar. Postgres ganha em durabilidade, multi-tenant e ACID — é a escolha de produção. SQLite ganha em latência e simplicidade — é a escolha de dev. Redis ganha em latência baixíssima e TTL nativo — é a escolha para cache de sessão curta. A regra prática: comece com SQLite no desenvolvimento (zero-config, itere rápido); migre para Postgres em produção (multi-tenant, escala); considere Redis como camada de cache para sessões ativas (sub-milissegundo). Não tente usar Redis como fonte de verdade — persistência é limitada.
💡 ANALOGIA: É como escolher onde guardar documentos importantes. SQLite é uma gaveta da sua mesa (rápido, local). Postgres é um cofre de banco (robusto, compartilhado). Redis é um post-it na parede (super rápido, mas some).
❓ PERGUNTA PARA A TURMA: "Se você tivesse que escolher UM backend para começar, qual seria?" (Resposta: SQLite para dev; Postgres para prod)
⚠️ ERROS COMUNS: Alunos querem usar Redis como storage principal. Não — Redis é volátil por padrão; use para cache com TTL, não como fonte de verdade.
➡️ TRANSIÇÃO: "Agora vamos ao recurso mais poderoso do checkpointer: resume."

---

### Slide 23 — Resume: Retomando Execução

**Título**: Resume — Retomando Execução
**Objetivo**: Mostrar como retomar uma execução interrompida.
**Conteúdo**:
- **Resume**: carregar estado do último checkpoint e continuar
- **Casos**: HITL demora, servidor reinicia, usuário volta dias depois
- **Código**: `graph.invoke(None, config={"configurable": {"thread_id": "xyz"}})`
- O agente retoma exatamente de onde parou (mensagens, contexto, steps)
- **Pegadinha**: modelo pode ter mudado (versão diferente) → estado pode ser incompatível

**Diagrama**: Fluxo: execução → interrupção → dias depois → resume
**Animação**: Timeline: execução → pause → dias → resume
**Imagem**: Linha do tempo com pause e resume
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Resume é o recurso central do checkpointer. Você passa `thread_id` e o LangGraph carrega o último checkpoint dessa thread, reconstruindo o estado. O agente continua de onde parou — como se nunca tivesse sido interrompido. Isso é poderoso para HITL: o agente pausa, o humano demora 3 dias para aprovar, e quando volta, o resume continua. Ou: servidor reinicia (deploy), e o agente volta ao exato estado pré-crash. A pegadinha: se o modelo mudou (ex.: GPT-4-turbo → GPT-4o), o comportamento pode ser ligeiramente diferente. E se o schema do estado mudou, pode quebrar — veremos versionamento no Slide 27.
💡 ANALOGIA: É como pausar um filme. Você para no minuto 45, vai dormir, e no dia seguinte continua do minuto 45 — não do início. O checkpointer é o "pause" do agente.
⚠️ ERROS COMUNS: Alunos esquecem de passar o `thread_id` no resume e o agente começa do zero (nova thread). Regra: o `thread_id` é a chave de continuidade.
➡️ TRANSIÇÃO: "Vamos visualizar este fluxo."

---

### Slide 24 — Diagrama: Checkpointer Resume

**Título**: Checkpointer Resume — Pause e Retomada
**Objetivo**: Visualizar o fluxo de pause/resume com checkpointer.
**Conteúdo**:
- Agente em execução (sessão 1) → estado serializado → Checkpointer (Postgres)
- Checkpointer → `thread_id` → Agente retoma (dias depois, sessão 2)
- Mesmo `thread_id` → Agente retoma (semana depois, sessão 3)
- HITL: humano aprova → resume

**Diagrama**: `12-Diagrams/ETHAGT05/checkpointer-resume.mmd`
**Animação**: Fluxo step-by-step (sessão 1 → pause → sessão 2)
**Imagem**: Diagrama mermaid renderizado
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vejam o fluxo. Sessão 1: agente executa, estado é serializado no Postgres (com thread_id). Sessão 2 (dias depois): agente é recriado, passa o mesmo thread_id, carrega o último checkpoint, e continua. Sessão 3 (semana depois): mesma coisa — o thread_id é a âncora de continuidade. O HITL também funciona: o agente interrompe para aprovação humana, o humano aprova, e o resume continua do ponto de interrupção. Tudo isso é transparente para o agente — ele não "sabe" que foi pausado.
💡 ANALOGIA: É como uma série da Netflix. Você assiste episódio 3, para, e no dia seguinte abre a Netflix e ela pergunta "continuar de onde parou?" — exatamente no minuto. O thread_id é o seu perfil; o checkpoint_id é o timestamp do episódio.
➡️ TRANSIÇÃO: "Resume continua. Mas às vezes queremos REPRODUZIR — é o replay."

---

### Slide 25 — Replay: Debugando o Passado

**Título**: Replay — Debugando o Passado
**Objetivo**: Mostrar como reproduzir execução passada para debug.
**Conteúdo**:
- **Replay**: carregar checkpoint de um momento específico e re-executar
- **Casos**: "por que o agente tomou decisão X?" → replay a partir do checkpoint anterior
- **Diferença de resume**: replay re-executa, resume continua
- **Útil para**: debugging, A/B testing de prompts, regressão
- **Ferramentas**: LangSmith + checkpointer = replay visual

**Diagrama**: Timeline de checkpoints com cursor de replay
**Animação**: Cursor se move para um checkpoint e re-executa
**Imagem**: Timeline com botão "replay from here"
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Replay é diferente de resume. Resume continua de onde parou. Replay volta a um momento específico e re-executa a partir dali. É essencial para debug: "o agente decidiu X no step 5; por quê?" Você replay a partir do checkpoint do step 4, e vê exatamente o que entrou no prompt, qual a tool call, qual a observation. Também é útil para A/B testing: você replay com um prompt diferente e compara. O LangSmith integra com checkpointer para replay visual — você vê o grafo, o estado, o trace em cada step.
💡 ANALOGIA: É como o "instant replay" nos esportes. Algo aconteceu, você volta no tempo e revê para entender. No agente: você volta ao checkpoint e re-executa para entender a decisão.
⚠️ ERROS COMUNS: Alunos confundem replay com resume. Resume = continuar. Replay = re-executar do passado. São operações diferentes com propósitos diferentes.
➡️ TRANSIÇÃO: "E se em vez de re-executar o mesmo caminho, você quiser tentar outro? É o branching."

---

### Slide 26 — Branching: Time Travel

**Título**: Branching — Time Travel
**Objetivo**: Mostrar como criar ramos alternativos a partir de um checkpoint.
**Conteúdo**:
- **Branching**: partir de um checkpoint e seguir caminho diferente
- **Casos**: "e se o agente tivesse usado tool Y em vez de X?"
- **Como**: fork do `checkpoint_id` → nova execução com parâmetros diferentes
- **Análogo a**: `git checkout <commit>` + `git checkout -b <novo-branch>`
- **Pergunta**: *Time travel: ferramenta de debug ou risco de segurança?*

**Diagrama**: Árvore de checkpoints com ramos (estilo git graph)
**Animação**: Ramos aparecem a partir de um checkpoint
**Imagem**: Git graph com branch
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Branching é o time travel do checkpointer. Você pega um checkpoint antigo (ex.: step 5 de ontem), faz um fork, e executa a partir dali com parâmetros diferentes. É como `git checkout <commit>` seguido de `git checkout -b <novo-branch>`. Você cria uma linha do tempo alternativa. Isso é poderoso para: "e se?" (experimentação), A/B testing rigoroso (mesmo estado inicial, caminhos diferentes), e exploração de estratégias. A pergunta de segurança: branching permite revisitar estados passados com dados possivelmente sensíveis. Em produção, branching deve ser auditado.
💡 ANALOGIA: É como save scumming em jogos. Você salva antes de uma decisão difícil, tenta um caminho, se não gostar, volta ao save e tenta outro. O checkpointer permite isso para agentes.
❓ PERGUNTA PARA A TURMA: "Time travel é ferramenta de debug ou risco de segurança?" (Resposta: ambos. Em dev, é ferramenta poderosa. Em prod, precisa de controle de acesso — não queremos qualquer um revisitando estados com PII.)
⚠️ ERROS COMUNS: Alunos acham que branching "desfaz" a execução original. Não — a execução original persiste; você cria um RAMO novo. Como no git: o branch main não some porque você criou um branch feature.
➡️ TRANSIÇÃO: "Mas e se o schema do estado evoluir entre branches ou sessões?"

---

### Slide 27 — Versionamento de Schema de Estado

**Título**: Versionamento de Schema de Estado
**Objetivo**: Lidar com evolução do schema de estado ao longo do tempo.
**Conteúdo**:
- **Problema**: estado v1 (sem campo "priority") vs estado v2 (com "priority")
- Checkpoints antigos têm schema diferente → quebra ao retomar
- **Estratégias**:
  - **Migração lazy**: converter no load
  - **Version field no estado**: `schema_version: 2`
  - **Backward compatibility**: campos novos com default
- **Analogia**: migração de DB, mas para estado de agente

**Diagrama**: Estado v1 → migração → Estado v2
**Animação**: Versões aparecem sequencialmente
**Imagem**: Estados com versões (v1, v2, v3)
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O schema do estado evolui. Hoje você tem `messages, intermediate_results`. Amanhã adiciona `priority`. Na semana que vem, `user_profile`. Mas os checkpoints antigos (gravados com schema v1) não têm esses campos. Quando você tenta dar resume em uma thread antiga, o código espera `priority` mas o checkpoint não tem → KeyError → quebra. Solução: (1) `schema_version` no estado — permite saber qual versão você está carregando; (2) Migração lazy — ao carregar um checkpoint v1, você converte para v2 preenchendo defaults; (3) Backward compatibility — campos novos sempre com default. É exatamente como migração de DB, mas para estado de agente.
💡 ANALOGIA: É como atualizar um app no celular. O app v2 espera um campo que o v1 não salvava. Quando o usuário atualiza, o app migra os dados antigos para o novo schema. Sem isso, o app quebra ao abrir dados antigos.
⚠️ ERROS COMUNS: Alunos não versionam o schema desde o dia 1. Depois, quando precisam adicionar campo, quebram todos os checkpoints antigos. Regra: `schema_version: 1` desde o primeiro commit. Sempre.
➡️ TRANSIÇÃO: "Chegou a hora da DEMO."

---

### Slide 28 — DEMO: Checkpointer em Postgres

**Título**: DEMO — Checkpointer em Postgres
**Objetivo**: Demo ao vivo — agente interrompido e retomado.
**Conteúdo**:
- Código do `05-Labs/ETHAGT05/Lab1-Checkpointer-Postgres`
- **Passo 1**: agente inicia tarefa (`thread_id = "demo-001"`)
- **Passo 2**: agente é interrompido (`Ctrl+C` no terminal)
- **Passo 3**: dias depois (simulado), retoma com mesmo `thread_id`
- Mostrar estado preservado (mensagens, contexto, steps)
- Replay de execução anterior para debug

**Diagrama**: Code block + terminal side-by-side
**Animação**: Highlight de linhas chave (`thread_id`, resume)
**Imagem**: VS Code com código + terminal com logs
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Demo ao vivo. Vou iniciar um agente com `thread_id = "demo-001"`. Ele começa uma tarefa (ex.: pesquisa multi-step). No meio, eu mato o processo com `Ctrl+C`. O agente "morre". Agora eu reinicio o script, passo o mesmo `thread_id`, e o agente retoma exatamente de onde parou — como se o `Ctrl+C` nunca tivesse acontecido. O segredo: o estado foi serializado no Postgres a cada step. No resume, o LangGraph carrega o último checkpoint e reconstrói o estado. Vou também mostrar o replay: voltar a um checkpoint anterior e ver o que o agente "pensou" em cada step.
💡 ANALOGIA: É como o truque de mágica de "serrar a pessoa ao meio". Eu "mato" o agente (Ctrl+C), e ele "revive" intacto. A mágica é o checkpointer.
⚠️ ERROS COMUNS: Se a API ou o Postgres cair na demo (acontece), tenho screenshot do resume pré-gravado. Não improvisar — seguir o plano B.
➡️ TRANSIÇÃO: "Vamos discutir o que acabamos de ver."

---

### Slide 29 — Pergunta da DEMO

**Título**: Pergunta da DEMO
**Objetivo**: Engajar a turma com uma pergunta sobre a demo.
**Conteúdo**:
- "O que acontece se o modelo foi atualizado entre sessão 1 e sessão 2?"
- "E se o schema do estado mudou?"
- "Como você testaria que o resume funciona corretamente?"
- Discussão em duplas (2 min)

**Diagrama**: Caixa de discussão
**Animação**: Perguntas aparecem uma a uma
**Imagem**: Ícone de "pergunta" + duplas discutindo
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vamos discutir em duplas, 2 minutos. Três perguntas: (1) o que acontece se o modelo mudou (ex.: GPT-4-turbo → GPT-4o)? (2) E se o schema mudou? (3) Como testar que resume funciona? Deixem a turma discutir. Depois, peçam 1-2 duplas para compartilhar.
💡 ANALOGIA: É como perguntar "o que acontece se você trocar o motor do carro no meio de uma viagem?" Provavelmente funciona, mas você precisa verificar.
❓ PERGUNTA PARA A TURMA: "Como vocês testariam que o resume funciona?" (Resposta esperada: rodar sem interrupção, depois com interrupção + resume, comparar outputs. Devem ser idênticos ou muito próximos.)
➡️ TRANSIÇÃO: "Checkpointer resolve persistência. Mas a context window ainda é finita. Vamos à gestão de contexto."

---

## SEÇÃO D — Gerenciamento de Contexto (Slides 30-35 · parcial)

---

### Slide 30 — [SEÇÃO] Gerenciamento de Contexto

**Título**: 3 — Gerenciamento de Contexto
**Objetivo**: Transição para o problema de janela de contexto finita.
**Conteúdo**: "3 — Gerenciamento de Contexto"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "3" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Início do bloco de gestão de contexto. O checkpointer persiste o estado entre sessões, mas DENTRO de uma sessão, a context window é finita. Mesmo com 200k tokens, ela enche. Vamos ver: por que enche? Quanto custa? E as estratégias para gerenciar: janela deslizante, sumarização, eviction, entity-centric memory.
➡️ TRANSIÇÃO: "Primeiro: o problema."

---

### Slide 31 — O Problema: Context Window é Finita

**Título**: Context Window é Finita
**Objetivo**: Estabelecer a tensão fundamental de gerenciamento de contexto.
**Conteúdo**:
- Mesmo com 200k tokens, a context window **enche**
- Conversas longas + tools + retrieval → estouro de contexto
- **Sintomas**: agente "esquece" início da conversa, respostas degradam, erro 400
- **Tensão**: mais contexto = mais informação, mas também mais custo, latência e ruído
- **Solução**: estratégias ativas de gerenciamento (não apenas "encher até estourar")

**Diagrama**: Balde enchendo de tokens até transbordar
**Animação**: Balde enche progressivamente
**Imagem**: Balde com tokens caindo, transbordando no fim
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A context window é finita. Mesmo 200k tokens enchem em uma conversa longa com tools e retrieval. Os sintomas são conhecidos: o agente "esquece" o início da conversa (Lost in the Middle), as respostas degradam (mais contexto = mais ruído), e eventualmente você toma erro 400 (context overflow). A tensão fundamental: mais contexto traz mais informação, mas também mais custo, mais latência, e mais ruído. A solução não é "encher até estourar" — é gerenciar ativamente. Vamos ver 4 estratégias.
💡 ANALOGIA: É como uma mala de viagem. Você pode encher até fechar à força, mas fica pesada, desorganizada, e você não acha nada. Melhor: curar o que coloca, priorizar o essencial.
⚠️ ERROS COMUNS: Alunos acham que "context window grande elimina a necessidade de gestão". Falso. Custa mais, degrada qualidade, e Lost in the Middle persiste.
➡️ TRANSIÇÃO: "Mas antes das estratégias, vamos desmistificar o custo."

---

### Slide 32 — Custo: Quadrático ou Linear? Visão Crítica

**Título**: Custo — Quadrático ou Linear?
**Objetivo**: Desmistificar a afirmação "custo cresce quadraticamente".
**Conteúdo**:
- **Mito**: "attention é O(n²) → custo quadraticamente"
- **Realidade**: attention é O(n²) em *computação*, mas:
  - **KV cache**: tokens já processados não são recomputados
  - **Sliding window attention**: só atende a uma janela local
  - **Custo de API** é *linear* em tokens (preço por token in/out)
- **Mas**: latência sim cresce, e qualidade degrada com contexto longo
- **Conclusão**: o problema não é só custo — é *qualidade* e *latência*

**Diagrama**: Gráfico: custo (linear) vs latência (sub-linear) vs qualidade (curva U invertida)
**Animação**: Três curvas aparecem
**Imagem**: Gráfico com 3 linhas (custo, latência, qualidade vs tamanho do contexto)
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Há um mito comum: "attention é O(n²), então custo cresce quadraticamente com o contexto". Vamos ser precisos. A *computação interna* da attention é O(n²) em tokens — isso é verdade. MAS: (1) provedores usam KV cache — tokens já processados não são recomputados; (2) sliding window attention — só atende a uma janela local; (3) o custo de API que VOCÊ paga é linear em tokens (preço por token de input + output). Então seu bolso sente linearmente. O que cresce de verdade é: latência (mais tokens = mais processamento) e degradação de qualidade (Lost in the Middle). A conclusão: o problema do contexto longo não é só custo — é qualidade e latência.
💡 ANALOGIA: É como dirigir em uma estrada. O custo do combustível cresce linearmente com a distância (não quadraticamente). Mas a fadiga do motorista cresce — e a chance de acidente também. Contexto longo é assim: o custo é linear, mas a qualidade do raciocínio cai.
❓ PERGUNTA PARA A TURMA: "Se o custo é linear, por que preocupar com contexto grande?" (Resposta: latência e qualidade. 200k tokens custam 200x mais que 1k, mas a qualidade NÃO é 200x melhor — é até pior.)
⚠️ ERROS COMUNS: Alunos repetem "custo quadrático" sem entender. A computação é O(n²), mas o custo de API é linear. Não confunda.
➡️ TRANSIÇÃO: "Então precisamos de estratégias. Comecemos pela mais simples."

---

### Slide 33 — Estratégia 1: Janela Deslizante

**Título**: Estratégia 1 — Janela Deslizante
**Objetivo**: Apresentar a estratégia mais simples de gerenciamento de contexto.
**Conteúdo**:
- **Manter apenas as últimas N mensagens** no contexto
- **Simples, previsível, barato**
- **Mas**: perde contexto antigo ("do que estávamos falando?")
- **Variação**: system prompt + últimas N mensagens (preserva instrução)
- **Quando usar**: chatbots simples, conversas curtas, não críticas

**Diagrama**: Janela deslizante sobre uma sequência de mensagens
**Animação**: Janela se move sobre as mensagens
**Imagem**: Lista de mensagens com uma "janela" destacando as últimas N
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A estratégia mais simples: janela deslizante. Você mantém apenas as últimas N mensagens no contexto. As antigas são descartadas. É simples, previsível e barata — o contexto nunca excede N mensagens. A desvantagem: perde contexto antigo. Se o usuário disse "estou trabalhando no projeto X" há 20 mensagens, e você mantém só 10, o agente esquece do projeto X. A variação comum: system prompt (fixo) + últimas N mensagens. Isso preserva a instrução do sistema. Use para chatbots simples e conversas curtas. Para conversas longas, você precisa de algo mais sofisticado (sumarização, eviction).
💡 ANALOGIA: É como uma conversa em um bar barulhento. Você só consegue lembrar dos últimos 5 minutos de conversa. O que foi dito antes sumiu. Funciona para conversas curtas; desastroso para projetos de longo prazo.
⚠️ ERROS COMUNS: Alunos usam janela deslizante para casos que precisam de memória de longo prazo. Regra: janela deslizante é para conversas curtas e isoladas. Se o caso precisa de contexto cross-sessão, use checkpointer + memória persistente.
➡️ TRANSIÇÃO: "Para conversas longas, precisamos de sumarização."

---

### Slide 34 — Estratégia 2: Sumarização em Cascata

**Título**: Estratégia 2 — Sumarização em Cascata
**Objetivo**: Mostrar como sumarizar contexto progressivamente.
**Conteúdo**:
- Quando contexto enche: **sumarizar mensagens antigas** → substituir por sumário
- **Sumarização em cascata**: sumário de sumários (níveis de compressão)
- Cada nível: menos detalhe, mais abstração
- **Pegadinha**: sumário pode perder informação crítica
- **Quando usar**: conversas longas, agentes de suporte, reuniões

**Diagrama**: Pirâmide invertida: mensagens → sumário L1 → sumário L2 → sumário L3
**Animação**: Níveis de sumário aparecem de baixo para cima
**Imagem**: Pirâmide invertida com níveis de compressão
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Sumarização em cascata é para conversas longas. Quando o contexto enche, você sumariza as mensagens antigas e as substitui por um sumário. À medida que a conversa continua, o sumário cresce, e você sumariza o sumário — criando níveis (L1, L2, L3). Cada nível tem menos detalhe e mais abstração. L1: sumário de 50 mensagens em 2k tokens. L2: sumário de 5 sumários L1 em 500 tokens. L3: sumário de todos em 100 tokens. A pegadinha: sumário é lossy — você pode perder o detalhe crítico que importaria depois. Mitigação: manter eventos originais no vector DB (episódica) mesmo após sumarização, com fallback para o nível inferior.
💡 ANALOGIA: É como ler um livro resumido. O livro original (mensagens) tem 500 páginas. O resumo (L1) tem 50. O resumo do resumo (L2) tem 5. A sinopse (L3) tem 1 parágrafo. Cada nível perde detalhe, mas ganha abstração.
⚠️ ERROS COMUNS: Alunos usam sumário cego (sem critério) e perdem informação crítica. Regra: sumarização deve preservar entidades críticas, decisões, e datas. Se perder isso, é inútil.
➡️ TRANSIÇÃO: "E se em vez de sumarizar, você decidir inteligentemente o que manter e o que descartar?"

---

### Slide 35 — Estratégia 3: Eviction por Relevância

**Título**: Estratégia 3 — Eviction por Relevância
**Objetivo**: Apresentar eviction inteligente (não só por tempo).
**Conteúdo**:
- Nem tudo no contexto é igualmente relevante
- **Eviction por relevância**: `score = f(recência, importância, frequência de acesso)`
- **Manter**: system prompt, últimas mensagens, entidades ativas, fatos críticos
- **Evitar**: mensagens antigas de baixa importância, tool outputs verbosos, redundâncias
- **Análogo a**: LRU cache, mas com score semântico

**Diagrama**: Matriz relevância × idade com zonas (manter / arquivar / apagar)
**Animação**: Zonas aparecem na matriz
**Imagem**: Matriz 2D com quadrantes coloridos
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Eviction por relevância é mais sofisticada que janela deslizante ou sumarização cega. Em vez de descartar por tempo (janela) ou comprimir tudo (sumário), você calcula um SCORE para cada item no contexto: `score = f(recência, importância, frequência de acesso)`. Itens com score alto ficam; score baixo são evictados (arquivados ou apagados). Isso é análogo a LRU cache, mas com score semântico — não só "quando foi acessado", mas "quão importante é". Manter: system prompt (sempre), últimas mensagens, entidades ativas, fatos críticos. Evitar: mensagens antigas de baixa importância, tool outputs verbosos, redundâncias. Vamos ver o fluxo no próximo slide.
💡 ANALOGIA: É como limpar o email. Você não apaga por data (janela) nem arquiva tudo (sumário). Você decide: este é importante (manter na caixa de entrada), este é antigo mas irrelevante (arquivar), este é spam (apagar).
⚠️ ERROS COMUNS: Alunos usam eviction só por recência (LRU puro). Regra: recência é um fator, mas importância e frequência também. Um fato crítico de 6 meses atrás pode ser mais importante que uma mensagem de 5 minutos atrás.
➡️ TRANSIÇÃO: "Vamos ver o fluxo de decisão visualmente."
