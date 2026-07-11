# ETHAGT10 — Slides Detalhados + Notas do Professor (Parte 1: Slides 1-31)

> Universidade Etho · Especialização em Programação Agêntica
> Cada slide contém: título, objetivo, conteúdo, notas do professor, diagrama, animação, imagem, tempo.

---

## SEÇÃO A — Abertura (Slides 1-6 · 8 min)

---

### Slide 1 — Capa

**Título**: ETHAGT10 — Padrões de Arquitetura Multi-Agente (topologias)
**Objetivo**: Identificar a aula, o professor e o contexto dentro da especialização.
**Conteúdo**:
- ETHAGT10 — Padrões de Arquitetura Multi-Agente (topologias)
- Universidade Etho · Especialização em Programação Agêntica
- Fase C — Sistemas Multi-Agente · 30 h
- Professor · Data

**Diagrama**: Logo Etho (canto sup. esquerdo) + imagem de fundo abstrata (rede de nós/topologias interconectadas)
**Animação**: Fade in do título (300ms)
**Imagem**: Fundo `etho-dark` (#0F1E2D) com pattern sutil de nós e arestas
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Bem-vindos à décima aula da especialização. Hoje damos um salto qualitativo: saímos de agentes individuais e entramos em sistemas multi-agente. Mas o foco não é "como construir agentes" — é "como organizá-los". A pergunta central de hoje: dada uma tarefa complexa, qual topologia você escolhe e por quê? Se você responder "supervisor" sem justificativa, você falhou esta aula.
💡 ANALOGIA: É como organizar uma equipe de pessoas. Você pode ter um chefe que delega tudo (supervisor), uma estrutura hierárquica (hierarchical), um time que se repassa tarefas (swarm), ou uma esteira de produção (pipeline). A topologia da equipe determina o sucesso.
❓ PERGUNTA PARA A TURMA: "Quantos de vocês já usaram multi-agente em produção?" (levantar mãos — calibrar nível)
⚠️ ERROS COMUNS: Alunos chegam querendo "a melhor topologia". Não existe melhor — existe a mais adequada para o contexto.
➡️ TRANSIÇÃO: "Vamos começar definindo o que vocês vão conseguir fazer ao final desta aula."

---

### Slide 2 — Objetivos do Módulo

**Título**: Objetivos do Módulo
**Objetivo**: Deixar claro o que o aluno deve conseguir FAZER ao final da aula.
**Conteúdo**:
- **Objetivo geral**: Dominar as topologias multi-agente — quando usar cada, trade-offs, e como escolher
- **Objetivos específicos**:
  1. Caracterizar 12 topologias (when-to-use, when-to-avoid)
  2. Justificar a escolha via ADR
  3. Implementar ao menos 4 topologias em um mesmo domínio
  4. Medir trade-offs (custo, latência, qualidade)
  5. Identificar sinais de que a topologia precisa evoluir

**Diagrama**: 5 ícones representando cada objetivo (catálogo, documento ADR, código, gráfico de trade-offs, semáforo)
**Animação**: Objetivos aparecem um a um (on click)
**Imagem**: Ícones minimalistas em `etho-accent` (#E85D2F)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Cada objetivo é mensurável. O objetivo #1 é catalogar — conhecer as 12 topologias. O #2 é justificar — não basta escolher, tem que defender a escolha em ADR. O #3 é implementar — teoria sem prática não vale. O #4 é medir — trade-offs não são opinativos, são quantificáveis. O #5 é evoluir — nenhuma topologia é definitiva. O foco de hoje é decisão arquitetural justificada, não "vamos de supervisor".
💡 ANALOGIA: É como um arquiteto de software escolhendo entre monolito, microsserviços e serverless. Cada um tem prós e contras. A decisão depende do contexto, e deve ser documentada.
❓ PERGUNTA PARA A TURMA: "Qual desses objetivos vocês acham mais desafiador?" (deixar responder — costuma ser #4 ou #5)
⚠️ ERROS COMUNS: Alunos confundem "conhecer 12 topologias" com "decorar 12 topologias". Conhecer = saber when-to-use e when-to-avoid.
➡️ TRANSIÇÃO: "Vamos ver onde esta aula se conecta com o Framework Etho de competências."

---

### Slide 3 — Competências Desenvolvidas

**Título**: Competências Desenvolvidas
**Objetivo**: Conectar a aula ao Framework Etho de competências.
**Conteúdo**:

| Competência | Nível ao final | Próximo nível em |
|---|---|---|
| C1 Programação Agêntica | **A** (Avançado) | ETHAGT14, ETHAGT15 |
| C2 Multi-Agent Systems | **A** (Avançado) | ETHAGT11, ETHAGT16 |
| C3 MCP & Tool Use | **B** (Básico) | ETHAGT02, ETHAGT08 |
| C4 Agent Memory | **B** (Básico) | ETHAGT05 |
| C6 Agent Security | **B** (Básico) | ETHAGT13 |

**Diagrama**: Radar chart com 5 eixos mostrando nível B/A
**Animação**: Radar aparece com wipe (left-to-right, 500ms)
**Imagem**: Badge visual por competência (círculos coloridos)
**Tempo**: 1 min

**Rodape**: MCP = Model Context Protocol — Protocolo de Contexto de Modelo

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Este módulo atinge nível Avançado em duas competências. C1 — Programação Agêntica — atinge A aqui, o que significa que você consegue projetar sistemas multi-agente complexos e justificar escolhas de topologia. C2 — Multi-Agent Systems — também atinge A, pois este é o módulo central de multi-agente. As outras três ficam em Básico — você conhece o conceito, mas o aprofundamento vem em módulos posteriores (ETHAGT02 para tools, ETHAGT05 para memória, ETHAGT13 para segurança).
💡 ANALOGIA: É como aprender a reger uma orquestra. Você já toca um instrumento (single agent). Hoje você aprende a conduzir múltiplos instrumentistas (multi-agente). Maestro de orquestra sinfônica (sociedades) vem em ETHAGT16.
⚠️ ERROS COMUNS: Alunos acham que "Avançado" significa "domínio completo". Não — significa que você decide arquitetura com justificativa. A maestria vem com prática e módulos subsequentes.
➡️ TRANSIÇÃO: "Vamos ver como esta aula está estruturada para entregar essas competências."

---

### Slide 4 — Agenda

**Título**: Agenda da Aula
**Objetivo**: Mostrar o roteiro da aula com tempos estimados.
**Conteúdo**:
- **Bloco 1 (45 min)**:
  - Abertura (8 min) — objetivos, motivação, contexto
  - Catálogo das 12 Topologias (12 min) — grid, espectro, exercício
  - Supervisor e Hierarchical (15 min) — supervisor pattern, hierarchical, DEMO, MetaGPT
  - Swarm e Handoffs (10 min) — OpenAI Swarm, swarm vs supervisor
  - Intervalo (5 min)
- **Bloco 2 (45 min)**:
  - Pipeline e Orchestrator-Workers (10 min)
  - Event-Driven, Actor Model, Mesh (10 min)
  - Tree, Recursive + DEMO (10 min)
  - Fechamento (15 min) — matriz, ADR, sinais, MetaGPT caso, quiz, Q&A

**Diagrama**: Timeline horizontal com 8 seções coloridas
**Animação**: Timeline cresce da esquerda para direita (500ms)
**Imagem**: Ícones de relógio por seção
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A aula tem dois blocos. O primeiro cobre o panorama (catálogo) e detalha as duas topologias mais comuns (supervisor e swarm). O segundo cobre as topologias avançadas e termina com a decisão arquitetural (matriz + ADR). Há duas DEMOs: hierarchical teams (Slide 24) e swarm vs supervisor (Slide 51). O quiz final tem 3 perguntas.
💡 ANALOGIA: É como um tour por uma cidade. Primeiro o mapa geral (catálogo), depois visitamos os bairros principais (supervisor, swarm), e no final aprendemos a escolher onde morar (ADR).
⚠️ ERROS COMUNS: Alunos acham que podem pular o catálogo (Seção B) e ir direto para ADR. Não — sem conhecer as opções, não há decisão.
➡️ TRANSIÇÃO: "Vamos começar pelo porquê. Por que a escolha de topologia importa?"

---

### Slide 5 — Motivação: O Problema da Topologia Padrão

**Título**: O Problema da Topologia Padrão
**Objetivo**: Criar tensão cognitiva — times escolhem topologia sem critério.
**Conteúdo**:
- **"Vamos de supervisor"** — a decisão default sem justificativa
- **Cenário**: sistema de revisão de PR com 3 especialistas (code, security, docs)
- Supervisor funciona, mas swarm talvez seja mais simples e barato
- **Custo de escolher errado**:
  - Gargalo de latência (supervisor serializa)
  - Custo excessivo (LLM call a cada roteamento)
  - Complexidade desnecessária (hierarchical onde flat basta)
- **Pergunta**: *Qual foi a topologia mais comum que vocês já usaram em projetos?*

**Diagrama**: Split — esquerda: supervisor gargalo (funil) | direita: swarm fluido (handoffs)
**Animação**: Split — lado esquerdo aparece primeiro, depois lado direito
**Imagem**: Ícone de funil (esquerda) vs fluxo de setas (direita)
**Tempo**: 2 min

**Rodape**: LLM = Large Language Model — Modelo de Linguagem de Grande Escala  ·  PR = Pull Request — requisicao de pull (GitHub)

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O problema mais comum em produção não é técnico — é de decisão. Times escolhem "supervisor" porque é o exemplo mais visto em tutoriais, não porque é a topologia certa. No cenário de revisão de PR, um supervisor com 3 workers (code, security, docs) funciona, mas: (1) toda revisão passa pelo supervisor (latência cumulativa); (2) se os 3 especialistas são independentes, não há razão para um roteador central; (3) swarm com handoffs seria mais simples. Escolher errado tem custo real: latência, tokens, complexidade de manutenção.
💡 ANALOGIA: É como um hospital onde todo paciente, não importa o problema, passa pela recepção, depois pelo clínico geral, depois pelo especialista. Se você já sabe que é cardiológico, por que passar pelo clínico? Swarm é a triagem direta; supervisor é o encaminhamento burocrático.
❓ PERGUNTA PARA A TURMA: "Qual foi a topologia mais comum que vocês já usaram em projetos?" (a maioria vai dizer supervisor ou nem saber o nome)
⚠️ ERROS COMUNS: Alunos acham que supervisor é "o padrão correto". É o padrão mais comum, mas raramente o mais correto sem análise.
➡️ TRANSIÇÃO: "Essa pergunta — 'qual topologia' — só faz sentido porque multi-agente se tornou viável. Vamos ver por quê."

---

### Slide 6 — Contexto: Do Single Agent ao Multi-Agente

**Título**: Do Single Agent ao Multi-Agente
**Objetivo**: Explicar a evolução que tornou multi-agente viável e a pergunta mudou.
**Conteúdo**:
- **Linha do tempo**:
  - 2023: ReAct (agente individual) → AutoGen (arXiv:2308.08155)
  - 2023: MetaGPT (arXiv:2308.00352) — SOPs para multi-agente
  - 2023: AgentVerse (arXiv:2308.10848) — assembling agents
  - 2024: OpenAI Swarm (handoffs), CrewAI, LangGraph multi-agent
  - 2026: arXiv:2601.12560 — survey de taxonomia de arquiteturas
- **Confluência**: reasoning + tool calling + frameworks multi-agente + custo reduzido
- **MetaGPT como marco**: SOPs (Standard Operating Procedures) aplicadas a agentes
- A pergunta deixou de ser "se" multi-agente, mas **"qual topologia"**

**Diagrama**: Timeline horizontal com marcos + seta convergindo para "Multi-agente viável"
**Animação**: Marcos aparecem sequencialmente (on click)
**Imagem**: Convergência de rios em um lago
**Tempo**: 1 min

**Rodape**: ReAct = Reasoning and Acting — padrao de loop Thought / Action / Observation

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Multi-agente não é ideia nova — sistemas multi-agente existem desde os anos 90 (Weiss, clássico). Mas três coisas mudaram: (1) LLMs ficaram bons em reasoning e role-playing, permitindo agentes com papéis distintos; (2) frameworks como AutoGen, MetaGPT e LangGraph tornaram a composição viável; (3) o custo baixou o suficiente para múltiplos agentes em loop. MetaGPT (2023) é o marco porque mostrou que SOPs (procedimentos operacionais padrão) podem ser codificados em agentes, replicando a estrutura de uma software house. Hoje a pergunta não é "se" multi-agente, mas "qual topologia usar".
💡 ANALOGIA: É como a evolução de times em uma startup. Começa com um fundor fazendo tudo (single agent). Depois contrata 2-3 pessoas (supervisor/swarm). Depois organiza em departamentos (hierarchical). A estrutura evolui com o tamanho.
❓ PERGUNTA PARA A TURMA: "Qual desses marcos vocês conheciam?" (maioria conhece Swarm/CrewAI; poucos conhecem AgentVerse)
⚠️ ERROS COMUNS: Alunos acham que multi-agente é "tecnologia nova". O conceito é dos anos 90. O que é novo é a viabilidade com LLMs.
➡️ TRANSIÇÃO: "Agora que sabemos por que estamos aqui, vamos ao panorama das 12 topologias."

---

## SEÇÃO B — Catálogo das 12 Topologias (Slides 7-16 · 12 min)

---

### Slide 7 — [SEÇÃO] Catálogo das 12 Topologias

**Título**: 1 — Catálogo das 12 Topologias
**Objetivo**: Transição visual para o panorama das topologias.
**Conteúdo**: Número "1" grande + "Catálogo das 12 Topologias"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "1" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Início do bloco de catálogo. Vamos ver as 12 topologias em um único grid, depois posicionar todas em um eixo (centralizado ↔ descentralizado), e finalmente fazer um exercício de matching. O objetivo desta seção é dar o panorama antes de aprofundar.
➡️ TRANSIÇÃO: "Primeiro: quais são as 12 topologias?"

---

### Slide 8 — As 12 Topologias (Grid Panorâmico)

**Título**: As 12 Topologias
**Objetivo**: Visão geral de todas as 12 topologias em um só slide.
**Conteúdo**:
- Grid 4×3 com mini-diagrama de cada topologia:
  1. **Single Agent** · 1 agente + N tools (baseline)
  2. **Supervisor** · roteador central + workers
  3. **Hierarchical** · árvore de supervisores → workers
  4. **Blackboard** · espaço compartilhado incremental
  5. **Actor Model** · atores com mailbox, async
  6. **Pipeline** · sequência fixa de agentes
  7. **Event-Driven** · agentes reagem a eventos
  8. **Swarm** · handoffs sem central
  9. **Tree of Agents** · árvore de exploração (LATS)
  10. **Recursive** · meta-agentes criam sub-agentes
  11. **Agent Mesh** · P2P flat, todos com todos
  12. **Hybrid** · composição das anteriores
- Fonte: `10-Architecture/architectures/catalog.md` + arXiv:2601.12560

**Diagrama**: Grid 4×3 de mini-diagramas (estrela, estrela com centro, árvore, quadro, círculos com mailbox, esteira, pub/sub, grafo de handoffs, árvore de decisão, fractal, grafo completo, composição)
**Animação**: Cada topologia aparece com click (grupo de 4)
**Imagem**: Cada mini-diagrama em cor distinta
**Tempo**: 3 min

**Rodape**: LATS = Language Agent Tree Search — Busca em Arvore com LLM

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Estas são as 12 topologias que vamos cobrir hoje. Não precisam decorar todas — precisam saber quando usar cada uma. Vamos agrupá-las: centralizadas (supervisor, hierarchical), de fluxo (pipeline, orchestrator-workers), descentralizadas (swarm, mesh, actor), estruturadas (tree, recursive) e reativas/híbridas (event-driven, blackboard, hybrid). Cada uma tem when-to-use e when-to-avoid documentados no catálogo de arquiteturas.
💡 ANALOGIA: É como um catálogo de plantas de uma construtora. Você não compra todas — você escolhe a que cabe no terreno, no orçamento e no estilo de vida. Topologia multi-agente é a planta da casa.
❓ PERGUNTA PARA A TURMA: "Quantas destas vocês já viram em produção?" (maioria viu supervisor e pipeline; poucas viram mesh ou tree)
⚠️ ERROS COMUNS: Alunos tentam memorizar 12 topologias de uma vez. Melhor: lembrar dos 5 grupos (centralizadas, fluxo, descentralizadas, estruturadas, híbridas).
➡️ TRANSIÇÃO: "Para compará-las, precisamos de um eixo. Vamos posicioná-las no espectro centralizado ↔ descentralizado."

---

### Slide 9 — O Espectro: Centralizado ↔ Descentralizado

**Título**: O Espectro: Centralizado ↔ Descentralizado
**Objetivo**: Dar um eixo de comparação antes de detalhar cada topologia.
**Conteúdo**:
- **Eixo horizontal**: Centralizado ←→ Descentralizado
- **Centralizado**: Supervisor, Hierarchical, Pipeline, Orchestrator-Workers
  - Controle forte, ordem previsível, gargalo central
- **Intermediário**: Blackboard, Event-Driven
  - Desacoplamento parcial, coordenação via barramento
- **Descentralizado**: Swarm, Mesh, Actor Model
  - Sem autoridade central, flexibilidade máxima, coordenação difícil
- **Estruturado** (ortogonal): Tree, Recursive
  - Estrutura recursiva, não se encaixa no eixo linear
- **Trade-off**: controle × flexibilidade

**Diagrama**: Linha horizontal com topologias posicionadas (setas indicando direção)
**Animação**: Topologias aparecem no eixo gradualmente (on click)
**Imagem**: Eixo com cores gradientes (azul → vermelho)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Este eixo é a ferramenta mental mais útil da aula. À esquerda, topologias centralizadas — alguém no controle (supervisor, orchestrator). À direita, descentralizadas — ninguém no controle, todos colaboram (swarm, mesh). No meio, híbridas (blackboard, event-driven). Ortogonal a esse eixo estão as estruturadas (tree, recursive) — que têm estrutura recursiva mas não são nem centralizadas nem descentralizadas no sentido clássico. O trade-off fundamental: quanto mais centralizado, mais controle mas mais gargalo; quanto mais descentralizado, mais flexibilidade mas mais difícil de coordenar.
💡 ANALOGIA: É como organizar uma empresa. Empresa vertical (centralizada) tem CEO no topo — controle total, mas gargalo de decisão. Empresa horizontal (descentralizada) tem squads autônomos — ágil, mas coordenação é difícil. Startup (estruturada) cresce recursivamente.
❓ PERGUNTA PARA A TURMA: "Em qual ponto do eixo fica o sistema de vocês hoje?" (respostas variam — maioria no centro-esquerda)
⚠️ ERROS COMUNS: Alunos acham que descentralizado é "sempre melhor". Não — descentralizado troca controle por flexibilidade. Se você precisa de consistência forte, centralizado é melhor.
➡️ TRANSIÇÃO: "Vamos detalhar as topologias por grupo, começando pelas centralizadas."

---

### Slide 10 — Topologias Centralizadas: Supervisor e Hierarchical

**Título**: Topologias Centralizadas: Supervisor e Hierarchical
**Objetivo**: Apresentar as topologias de controle central.
**Conteúdo**:
- **Supervisor**: 1 roteador (LLM) + N workers (tools) — LangGraph
  - Supervisor decide: qual worker, em que ordem, quando sintetizar
- **Hierarchical**: árvore de supervisores → workers → sub-workers
  - Top supervisor → sub-supervisores → workers
- **When-to-use**: tarefas decomponíveis, necessidade de controle, ≤10 workers
- **When-to-avoid**: baixa latência crítica, tarefas imprevisíveis, muitos workers
- **Pergunta**: *Já usou supervisor em produção? Funcionou bem?*

**Diagrama**: 2 mini-diagramas lado a lado (estrela com centro vs árvore de 3 níveis)
**Animação**: Colunas aparecem uma a uma (on click)
**Imagem**: Ícone de chefe (supervisor) vs ícone de hierarquia (árvore)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Supervisor é a topologia mais comum em produção. Um LLM atua como roteador: recebe a tarefa, decide qual worker chamar, coleta resultados, sintetiza. Em LangGraph, cada worker é exposto como uma tool no supervisor. Hierarchical generaliza isso: em vez de um supervisor, você tem uma árvore. Top supervisor delega para sub-supervisores, que delegam para workers. A diferença é escala: supervisor funciona até ~7 workers (limite cognitivo do roteador); hierarchical escala para dezenas, mas adiciona latência e complexidade.
💡 ANALOGIA: Supervisor = tech lead com desenvolvedores. Hierarchical = VP → diretores → gerentes → desenvolvedores. Quanto maior a empresa, mais níveis — mas cada nível adiciona overhead.
❓ PERGUNTA PARA A TURMA: "Já usou supervisor em produção? Funcionou?" (anotar experiências — algumas serão de gargalo)
⚠️ ERROS COMUNS: Alunos acham que hierarchical é "sempre melhor que supervisor". Hierarchical adiciona latência e complexidade. Só use quando supervisor com >7 workers está insustentável.
➡️ TRANSIÇÃO: "Agora as topologias de fluxo."

---

### Slide 11 — Topologias de Fluxo: Pipeline e Orchestrator-Workers

**Título**: Topologias de Fluxo: Pipeline e Orchestrator-Workers
**Objetivo**: Apresentar as topologias de fluxo controlado.
**Conteúdo**:
- **Pipeline**: sequência fixa de agentes (A → B → C)
  - Cada step é um agente especializado; ordem é predefinida no código
- **Pipeline dinâmico**: próximo step decidido em runtime
- **Orchestrator-Workers**: orchestrator particiona UMA tarefa em sub-tarefas e delega
  - Diferença do supervisor: orchestrator divide; supervisor roteia a tarefa inteira
- **When-to-use**: passos predefinidos, previsibilidade, ordem importa
- **When-to-avoid**: flexibilidade alta necessária, passos imprevisíveis
- **Aprofundamento**: ETHAGT03 (5 workflows canônicos)

**Diagrama**: 2 mini-diagramas lado a lado (esteira linear vs estrela com síntese)
**Animação**: Colunas aparecem uma a uma (on click)
**Imagem**: Ícone de esteira (pipeline) vs ícone de divisão (orchestrator)
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Pipeline é a topologia mais simples e previsível. Você define a ordem no código: agente A → agente B → agente C. Não há decisão de roteamento — cada step executa e passa para o próximo. Pipeline dinâmico permite que um step decida o próximo (ex.: A decide ir para B ou C). Orchestrator-workers é diferente de supervisor: o orchestrator pega UMA tarefa e a divide em sub-tarefas distintas, delegando cada uma para um worker, depois sintetiza. Supervisor roteia a tarefa inteira para um worker. A distinção vem da Anthropic (Building Effective Agents, 2024).
💡 ANALOGIA: Pipeline = linha de montagem (cada estação faz uma parte). Orchestrator = arquiteto que pega um projeto grande, divide em módulos, delega para engenheiros, e integra tudo. Supervisor = recepcionista que encaminha cada cliente para o setor certo.
⚠️ ERROS COMUNS: Alunos confundem pipeline com supervisor. Pipeline = ordem fixa no código. Supervisor = LLM decide a ordem. Se você está escrevendo `if` para decidir o próximo step, é pipeline dinâmico.
➡️ TRANSIÇÃO: "Agora as descentralizadas."

---

### Slide 12 — Topologias Descentralizadas: Swarm, Mesh, Actor Model

**Título**: Topologias Descentralizadas: Swarm, Mesh, Actor Model
**Objetivo**: Apresentar as topologias sem controle central.
**Conteúdo**:
- **Swarm**: agentes leves com `transfer()` de controle (OpenAI)
  - Agente A recebe tarefa → se não for dele, transfere para agente B
  - Sem orquestrador — controle passa de agente para agente
- **Agent Mesh**: topologia flat peer-to-peer, sem orquestrador
  - Cada agente fala com qualquer outro diretamente
- **Actor Model**: cada agente = ator com mailbox, mensagem assíncrona
  - Estado privado, sem estado compartilhado, escala natural
- **When-to-use**: flexibilidade, escalabilidade, sem gargalo central
- **When-to-avoid**: consistência forte, coordenação complexa, previsibilidade

**Diagrama**: 3 mini-diagramas lado a lado (handoffs em cadeia vs grafo completo vs círculos com mailbox)
**Animação**: Colunas aparecem uma a uma (on click)
**Imagem**: Ícones de mão repassando (swarm) vs rede (mesh) vs caixa de entrada (actor)
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: As três topologias descentralizadas compartilham a ausência de orquestrador central, mas diferem no mecanismo. Swarm (OpenAI, 2024) usa handoffs: um agente transfere controle para outro, passando o contexto. É leve e fluido. Agent Mesh é P2P: todos falam com todos, sem hierarquia. É flexível mas caro (N² conexões). Actor Model é a fundação teórica de sistemas distribuídos: cada agente é um ator com estado privado e mailbox. Comunicação é assíncrona por mensagens. Akka (JVM) e Ray (Python) implementam isso. Microsoft AutoGen usa conceitos de actor model.
💡 ANALOGIA: Swarm = jogo de queimada onde a bola passa de mão em mão. Mesh = grupo de WhatsApp onde todos falam com todos. Actor Model = correio — cada um tem sua caixa postal, mensagens assíncronas.
⚠️ ERROS COMUNS: Alunos acham que swarm é "mesh leve". Não — swarm transfere controle (um agente ativo por vez); mesh permite múltiplos ativos simultaneamente.
➡️ TRANSIÇÃO: "Agora as estruturadas."

---

### Slide 13 — Topologias Estruturadas: Tree e Recursive

**Título**: Topologias Estruturadas: Tree e Recursive
**Objetivo**: Apresentar as topologias de estrutura recursiva.
**Conteúdo**:
- **Tree of Agents**: árvore de exploração (LATS — Language Agent Tree Search)
  - Agente expande múltiplas possibilidades → avalia → seleciona melhor caminho
  - Como MCTS (Monte Carlo Tree Search) aplicado a agentes LLM
- **Recursive**: meta-agentes que instanciam sub-agentes dinamicamente
  - "Preciso de especialista em X" → cria agente X → delega
  - Sub-agentes podem criar sub-sub-agentes
- **When-to-use**: exploração de soluções, decomposição recursiva, problemas abertos
- **When-to-avoid**: custo explode, profundidade incontrolável, orçamento limitado
- **Preview**: ETHAGT15 (meta-agentes em profundidade)

**Diagrama**: 2 mini-diagramas lado a lado (árvore de decisão com nós vs fractal auto-similar)
**Animação**: Colunas aparecem uma a uma (on click)
**Imagem**: Ícone de árvore genealógica (tree) vs fractal (recursive)
**Tempo**: 1.5 min

**Rodape**: MCTS = Monte Carlo Tree Search — Busca em Arvore de Monte Carlo

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Tree of Agents é inspirado em LATS (Language Agent Tree Search, arXiv:2310.01757). Em vez de seguir um caminho, o agente expande múltiplas possibilidades, avalia cada uma, e seleciona o melhor caminho — como um jogador de xadrez que pensa vários movimentos à frente. É poderoso mas caro: o custo explode exponencialmente com a profundidade. Recursive é diferente: não é uma árvore de exploração, é meta-programação. Um meta-agente decide "preciso de um especialista em X", instancia um sub-agente X, delega, e integra o resultado. Sub-agentes podem criar sub-sub-agentes, recursivamente. É adaptativo mas perigoso: sem max_depth, custo e latência explodem.
💡 ANALOGIA: Tree = jogador de xadrez analisando movimentos. Recursive = gerente que contrata consultores, e cada consultor pode contratar sub-consultores. Sem controle, você tem uma empresa fantasma de contratados.
⚠️ ERROS COMUNS: Alunos acham que recursive é "sempre adaptativo e bom". Recursive é adaptativo mas caro. Sem max_depth e validação, é anti-pattern.
➡️ TRANSIÇÃO: "Agora as reativas e híbridas."

---

### Slide 14 — Topologias Reativas e Híbridas: Event-Driven, Blackboard, Hybrid

**Título**: Reativas e Híbridas: Event-Driven, Blackboard, Hybrid
**Objetivo**: Apresentar as topologias reativas e combinatórias.
**Conteúdo**:
- **Event-Driven**: agentes reagem a eventos via mensageria (Kafka, NATS)
  - Preview: ETHAGT11 (Event-Driven Agents em profundidade)
- **Blackboard**: espaço compartilhado onde agentes leem/escrevem incrementalmente
  - Origem: Hearsay-II (1971-1976), AI clássica
  - Precursor do event-driven
- **Hybrid**: composição das topologias anteriores (ex.: supervisor + event-driven + pipeline)
  - A regra em produção real, não a exceção
- **When-to-use**: assincronia, desacoplamento, mundo real (hybrid)
- **When-to-avoid**: simplicidade (over-engineering em protótipos)

**Diagrama**: 3 mini-diagramas lado a lado (pub/sub com broker vs quadro compartilhado vs composição de ícones)
**Animação**: Colunas aparecem uma a uma (on click)
**Imagem**: Ícone de eventos (raio) vs quadro negro (blackboard) vs quebra-cabeça (hybrid)
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Event-driven é a topologia assíncrona: agentes publicam e consomem eventos via um broker (Kafka, Redis Streams, NATS). Total desacoplamento — o publicador não sabe quem consome. É preview de ETHAGT11, onde aprofundamos. Blackboard é o padrão clássico (Hearsay-II, anos 70): um espaço compartilhado onde agentes escrevem hipóteses e outros agentes leem e refinam. É o precursor do event-driven — em vez de eventos, um quadro. Hybrid é a realidade: quase nenhum sistema de produção é topologia pura. Um sistema real pode ter pipeline no macro, hierarchical no micro, e event-driven para integração com sistemas externos.
💡 ANALOGIA: Event-driven = rede social (você posta, seguidores reagem). Blackboard = mural da equipe (todos escrevem e leem). Hybrid = empresa real (tem hierarquia, fluxos de processo, e comunicação informal).
⚠️ ERROS COMUNS: Alunos começam protótipos com hybrid. Comece simples (supervisor ou pipeline). Hybrid é para produção madura, não protótipo.
➡️ TRANSIÇÃO: "Antes de aprofundar, lembremos do baseline."

---

### Slide 15 — Single Agent: O Baseline Esquecido

**Título**: Single Agent — O Baseline Esquecido
**Objetivo**: Lembrar que single agent é uma topologia válida e frequentemente a melhor.
**Conteúdo**:
- **Single Agent** = 1 agente com N tools (não é multi-agente, mas é o baseline)
- **Quando NÃO ir para multi-agente**:
  - Tarefa não se decompõe naturalmente
  - Latência não é problema
  - Custo precisa ser mínimo
  - Um agente com boas tools resolve
- **Regra**: comece com single agent, só suba para multi-agente com evidência
- **Conexão**: ETHAGT01 (escalada de complexidade)

**Diagrama**: Single agent com N tools (estrela com 1 centro e múltiplas pontas)
**Animação**: Estrela aparece com ferramentas surgindo
**Imagem**: Ícone de agente único com múltiplas ferramentas
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Antes de qualquer topologia multi-agente, pergunte: single agent resolve? Um agente ReAct com boas tools pode fazer muita coisa. Multi-agente adiciona: custo (múltiplos LLMs), latência (coordenação), complexidade (debug, estado compartilhado). A regra é a mesma da Anthropic: comece simples, só escale com evidência. Se um agente com 10 tools resolve, não crie 3 agentes com 3-4 tools cada.
💡 ANALOGIA: É como contratar. Se um funcionário bom resolve, não contrate 3 medianos. Multi-agente é como uma equipe — só justificável quando um não dá conta.
⚠️ ERROS COMUNS: Alunos pulam para multi-agente por "moda". Multi-agente é overhead. Se single agent resolve, single agent é a topologia certa.
➡️ TRANSIÇÃO: "Vamos praticar o matching antes de aprofundar."

---

### Slide 16 — Exercício Rápido: Matching Cenário → Topologia

**Título**: Exercício: Matching Cenário → Topologia
**Objetivo**: Praticar a associação cenário-topologia antes de aprofundar.
**Conteúdo**:
- 6 cenários curtos:
  1. "Chatbot de suporte com escalonamento" → ?
  2. "Revisão de PR com 3 especialistas" → ?
  3. "Relatório financeiro em etapas" → ?
  4. "Simulação de mercado" → ?
  5. "Assistente pessoal multi-função" → ?
  6. "Pesquisa autônoma com exploração" → ?
- Votação rápida (mãos levantadas)

**Diagrama**: 6 cards com cenários + setas para topologias
**Animação**: Cards aparecem um a um
**Imagem**: Cards em `etho-light` com bordas coloridas
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vamos praticar. Para cada cenário, votem na topologia. Não há resposta única — o objetivo é vocês argumentarem. Leiam o cenário, pensem 10 segundos, votem.
❓ RESPOSTAS ESPERADAS (não revelar antes da votação):
  1. Supervisor (escalonamento = roteamento central) ou Swarm (handoffs)
  2. Supervisor (3 especialistas independentes, síntese) ou Swarm (se não precisa síntese)
  3. Pipeline (etapas fixas e predefinidas)
  4. Actor Model / Mesh (agentes autônomos em paralelo)
  5. Swarm (multi-função com handoffs naturais)
  6. Tree (exploração de múltiplos caminhos)
⚠️ ERROS COMUNS: Alunos votam "supervisor" para tudo. Supervisor é default, não é resposta universal.
➡️ TRANSIÇÃO: "Agora que temos o panorama, vamos aprofundar nas duas topologias mais comuns: supervisor e hierarchical."

---

## SEÇÃO C — Supervisor e Hierarchical (Slides 17-28 · 15 min)

---

### Slide 17 — [SEÇÃO] Supervisor e Hierarchical

**Título**: 2 — Supervisor e Hierarchical: A Topologia Default
**Objetivo**: Transição visual para o bloco de supervisor.
**Conteúdo**: Número "2" grande + "Supervisor e Hierarchical: A Topologia Default"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "2" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Entramos na topologia mais comum em produção. Vamos detalhar o supervisor pattern (como funciona em LangGraph), a generalização hierarchical, quando escalar hierarquia, casos de falha, e uma DEMO ao vivo. Também vamos conectar ao paper canônico MetaGPT.
➡️ TRANSIÇÃO: "Primeiro: o que é o supervisor pattern?"

---

### Slide 18 — Supervisor Pattern: O Roteador

**Título**: Supervisor Pattern: O Roteador
**Objetivo**: Apresentar o supervisor como padrão fundamental.
**Conteúdo**:
- **Supervisor** = LLM que roteia tarefas para workers especializados
- Workers são especializados: pesquisa, escrita, análise, etc.
- Supervisor decide:
  - Qual worker chamar
  - Em que ordem
  - Quando sintetizar
- **Analogia**: supervisor = tech lead, workers = desenvolvedores
- **Fonte**: LangGraph multi-agent-collaboration

**Diagrama**: `12-Diagrams/ETHAGT10/supervisor-topology.mmd`
**Animação**: Supervisor aparece primeiro, depois workers surgem como tools conectados
**Imagem**: Diagrama supervisor (rosa) com workers (azul) conectados
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O supervisor é essencialmente um agente ReAct onde as "tools" são outros agentes. O supervisor recebe a tarefa, raciocina sobre qual worker é mais adequado, chama esse worker, recebe o resultado, e decide o próximo passo. Pode chamar múltiplos workers em sequência ou paralelo. A vantagem é controle: o supervisor tem visão global do estado e pode orquestrar. A desvantagem é gargalo: toda requisição passa por ele.
💡 ANALOGIA: Supervisor = tech lead que recebe uma tarefa, pensa "isso é para o backend", passa para o dev backend, recebe o resultado, pensa "agora precisa frontend", passa para o dev frontend. Ele não escreve código — ele orquestra.
⚠️ ERROS COMUNS: Alunos acham que supervisor "pensa menos" que os workers. Supervisor pensa diferente — ele raciocina sobre roteamento, não sobre execução.
➡️ TRANSIÇÃO: "Como isso é implementado em LangGraph? Via tool calls."

---

### Slide 19 — Supervisor como Tool Calls (LangGraph)

**Título**: Supervisor como Tool Calls (LangGraph)
**Objetivo**: Mostrar a implementação canônica em LangGraph.
**Conteúdo**:
- Cada worker = uma tool no supervisor
- Supervisor LLM com `bind_tools([worker_a, worker_b, ...])`
- Fluxo: supervisor decide `tool_call` → worker executa → resultado volta
- Snippet:
  ```python
  supervisor = create_react_agent(
      model,
      tools=[researcher, writer, analyst]
  )
  ```
- O supervisor é um agente ReAct onde as "tools" são outros agentes

**Diagrama**: `12-Diagrams/ETHAGT10/supervisor-topology.mmd` (com tool calls anotados)
**Animação**: Fluxo step-by-step: supervisor → tool_call → worker → return → supervisor
**Imagem**: Code block com syntax highlighting + diagrama lado a lado
**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Em LangGraph, a implementação mais limpa de supervisor é tratar cada worker como uma tool. O supervisor é um agente ReAct com `bind_tools`, e cada tool, quando chamada, executa o worker correspondente (que é ele mesmo um agente ou subgrafo). Isso é elegante porque reutiliza todo o mecanismo de tool calling: o supervisor não precisa de lógica especial para rotear — ele simplesmente chama a tool certa, como qualquer agente ReAct. A diferença é que as "tools" são agentes completos, não funções simples.
💡 ANALOGIA: É como um gerente que tem atalhos na mesa para cada departamento. Ele aperta o botão "pesquisa" e o departamento de pesquisa executa. Ele não liga — ele delega via interface.
❓ PERGUNTA PARA A TURMA: "Se o supervisor é um ReAct com tools, o que impede que o supervisor chame a mesma tool em loop?" (Resposta: nada, se o prompt não orientar. Por isso observabilidade é crítica.)
⚠️ ERROS COMUNS: Alunos implementam supervisor com if/else em vez de tool calls. Isso perde a flexibilidade — você volta para pipeline. Supervisor = LLM decide, não código.
➡️ TRANSIÇÃO: "E quando um supervisor não é suficiente? Generalizamos para hierarchical."

---

### Slide 20 — Hierarchical: Árvore de Supervisores

**Título**: Hierarchical — Árvore de Supervisores
**Objetivo**: Apresentar a generalização do supervisor para múltiplos níveis.
**Conteúdo**:
- **Hierarchical** = supervisor de supervisores
- Estrutura: top supervisor → sub-supervisores → workers → (sub-workers)
- Cada nível delega para o nível abaixo
- **Caso**: revisão de PR → top supervisor → (code reviewer sup, security sup, docs sup) → workers
- **Fonte**: LangGraph `hierarchical_agent_teams`

**Diagrama**: `12-Diagrams/ETHAGT10/hierarchical-topology.mmd`
**Animação**: Árvore cresce de cima para baixo (nível por nível)
**Imagem**: Diagrama hierarchical (top rosa, sub laranja, workers azul)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Hierarchical surge quando um supervisor tem workers demais. Em vez de um supervisor com 15 workers (cognitivamente impossível de rotear bem), você cria sub-domínios. Top supervisor delega para sub-supervisores de cada domínio (code, security, docs), e cada sub-supervisor gerencia seus workers. O exemplo clássico é revisão de PR: top supervisor recebe "revise este PR", delega para 3 sub-supervisores (code review, security review, docs review), cada um com seus workers especializados. LangGraph tem o exemplo `hierarchical_agent_teams` que implementa isso.
💡 ANALOGIA: Hierarchical = empresa com departamentos. CEO → diretores de departamento → gerentes → funcionários. Cada nível abstrai o nível abaixo.
⚠️ ERROS COMUNS: Alunos criam hierarchical com 3 níveis "só porque sim". 3 níveis raramente é necessário. A maioria dos casos resolve com flat (1 supervisor) ou 2 níveis. 3 níveis = latência e custo explodindo.
➡️ TRANSIÇÃO: "Quando vale escalar a hierarquia? Vamos dar um critério."

---

### Slide 21 — Quando Escalar Hierarquia: 3 Níveis vs Flat

**Título**: Quando Escalar Hierarquia
**Objetivo**: Dar critério para decidir profundidade da hierarquia.
**Conteúdo**:
- **Flat (1 nível)**: supervisor + workers — simples, baixa latência
- **2 níveis**: top supervisor + sub-supervisores + workers — domínios distintos
- **3 níveis**: raramente necessário — custo e latência explodem
- **Critério**: escalar quando workers de um supervisor > 5-7 (limite cognitivo)
- **Regra**: prefira flat; só adicione nível com evidência de que flat é insuficiente

**Diagrama**: 3 árvores lado a lado (1 nível, 2 níveis, 3 níveis) com métricas de latência
**Animação**: Árvores aparecem uma a uma com métricas
**Imagem**: 3 diagramas com indicadores de custo/latência
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O critério para escalar hierarquia é o limite cognitivo do supervisor. Um supervisor roteando 3-5 workers funciona bem. Com 7+, o roteamento degrada — o LLM confunde workers, chama o errado, repete. É o mesmo limite cognitivo humano (Miller's 7±2). Quando você passa de 7 workers, crie sub-domínios. Mas cada nível adiciona: (1) latência (cada nível é um hop de LLM); (2) custo (cada supervisor faz LLM calls); (3) complexidade de debug (trace mais profundo). 3 níveis quase nunca vale — prefira reorganizar os workers.
💡 ANALOGIA: É como gerenciar pessoas. Um gerente com 3-5 subordinados diretos funciona. Com 10+, ele vira gargalo. Solução: criar coordenadores. Mas 3 níveis de gerência (VP → diretor → gerente → dev) raramente vale para times pequenos.
⚠️ ERROS COMUNS: Alunos escalam hierarquia "para parecer profissional". Hierarquia desnecessária é over-engineering. Comece flat.
➡️ TRANSIÇÃO: "Mas mesmo flat, o supervisor tem modos de falha. Vamos ser honestos."

---

### Slide 22 — Casos de Falha: Supervisor Gargalo

**Título**: Casos de Falha — Supervisor Gargalo
**Objetivo**: Ser honesto sobre os modos de falha do supervisor.
**Conteúdo**:
- **Supervisor vira bottleneck**: todas as requisições passam por ele
- **Latência cumulativa**: supervisor serializa todas as chamadas
- **Custo**: supervisor faz LLM call a cada roteamento
- **Single point of failure**: se supervisor alucina, sistema inteiro falha
- **Sinal de alerta**: latência > 30s para tarefas simples

**Diagrama**: Diagrama com "funil" no supervisor (gargalo visual)
**Animação**: Funil aparece destacando o gargalo
**Imagem**: Diagrama com supervisor em vermelho (alerta)
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O supervisor é o ponto mais crítico do sistema. Toda tarefa passa por ele. Se ele é lento, todo o sistema é lento. Se ele alucina (chama worker errado), todo o sistema falha. Se ele cai, nada funciona. Em produção, o sintoma mais comum é latência crescente: tarefas que antes levavam 5s agora levam 30s. Causa: o supervisor está sobrecarregado, serializando muitas requisições. Solução: (1) paralelizar workers independentes; (2) migrar para swarm se não precisa síntese; (3) hierarchical se são domínios distintos.
💡 ANALOGIA: É como uma portaria de prédio onde TODOS os visitantes precisam passar. Em horário de pico, a fila cresce. Solução: múltiplas portarias (swarm) ou portarias por ala (hierarchical).
⚠️ ERROS COMUNS: Alunos acham que "supervisor mais inteligente" resolve o gargalo. Não — gargalo é estrutural, não de qualidade do modelo. Precisa mudar a topologia.
➡️ TRANSIÇÃO: "Outro anti-pattern: workers redundantes."

---

### Slide 23 — Casos de Falha: Workers Redundantes

**Título**: Casos de Falha — Workers Redundantes
**Objetivo**: Mostrar o anti-pattern de overlap de responsabilidades.
**Conteúdo**:
- Workers com responsabilidades sobrepostas → supervisor não sabe qual escolher
- Resultado: roteamento errado, retrabalho, custo duplicado
- **Solução**: responsabilidade exclusiva por worker (SRP — Single Responsibility)
- **Sinal**: supervisor chama 2+ workers para a mesma sub-tarefa

**Diagrama**: Diagrama de Venn mostrando overlap entre workers
**Animação**: Overlap aparece em vermelho (conflito)
**Imagem**: Diagrama de Venn com 2-3 círculos sobrepostos
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O segundo anti-pattern clássico é workers com responsabilidades sobrepostas. Se o worker "pesquisador" e o worker "analista" ambos podem responder "analise este dado", o supervisor não sabe qual chamar. Resultado: às vezes chama um, às vezes outro, às vezes os dois (retrabalho e custo duplicado). A solução é Single Responsibility Principle: cada worker tem uma responsabilidade exclusiva e clara. Se dois workers se sobrepõem, funda-os ou redefina as fronteiras.
💡 ANALOGIA: É como ter dois funcionários com a mesma descrição de cargo. Quando chega uma tarefa, ninguém sabe quem faz. Resultado: ou ninguém faz, ou os dois fazem (retrabalho).
⚠️ ERROS COMUNS: Alunos criam workers genéricos ("assistente"). Workers genéricos sempre se sobrepõem. Seja específico: "pesquisador de web", "analisador de código", "escritor de documentação".
➡️ TRANSIÇÃO: "Vamos ver tudo isso em ação na DEMO."

---

### Slide 24 — DEMO: Hierarchical Teams (Code Walkthrough)

**Título**: DEMO — Hierarchical Teams
**Objetivo**: Demo ao vivo — supervisor + 2 workers + sub-worker.
**Conteúdo**:
- Código do `05-Labs/ETHAGT10/Lab1-Hierarchical-Teams`
- **Topologia**: supervisor → (researcher, writer) → writer → formatter (sub-worker)
- **Tarefa**: "Escreva um resumo sobre tópico X"
- **Fluxo**:
  1. Supervisor delega para researcher
  2. Researcher pesquisa → retorna
  3. Supervisor delega para writer
  4. Writer escreve → delega formatação para formatter
  5. Formatter formata → retorna para writer
  6. Writer retorna para supervisor
  7. Supervisor sintetiza resposta final
- Mostrar trace mostrando cada nível da hierarquia

**Diagrama**: Code block + trace side-by-side
**Animação**: Highlight de linhas chave + trace aparece nível por nível
**Imagem**: Screenshot do trace com níveis destacados
**Tempo**: 4 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esta é a primeira DEMO. Vou rodar o código do Lab 1 ao vivo. A topologia é hierarchical de 2 níveis: supervisor no topo, researcher e writer como workers, e formatter como sub-worker do writer. A tarefa é escrever um resumo. Observem no trace: cada nível aparece como um span. O supervisor delega, o researcher pesquisa, o supervisor delega para o writer, o writer delega formatação para o formatter, o formatter retorna, o writer retorna, o supervisor sintetiza. O trace mostra a hierarquia claramente.
❓ PERGUNTA PARA A TURMA (durante a demo): "Notem quantos LLM calls acontecem. Cada nível = pelo menos 1 call. Isso é custo."
⚠️ SE A API FALHAR: Mostrar o screenshot do trace salvo. Dizer: "Este é o trace que deveria aparecer. Observem a estrutura hierárquica nos spans."
⚠️ ERROS COMUNS: Alunos não percebem que cada nível adiciona latência. No trace, somem o tempo total: supervisor + researcher + supervisor + writer + formatter + writer + supervisor = 7 LLM calls mínimo.
➡️ TRANSIÇÃO: "Vamos discutir o que vimos."

---

### Slide 25 — Pergunta da DEMO

**Título**: Pergunta da DEMO
**Objetivo**: Engajar a turma com análise crítica da demo.
**Conteúdo**:
- "Em quantos níveis de hierarquia o supervisor se torna gargalo?"
- "O que acontece se o researcher retornar informação errada? Quem detecta?"
- "O formatter deveria ser sub-worker do writer ou worker do supervisor?"
- Discussão em duplas (2 min)

**Diagrama**: Caixa de discussão com as 3 perguntas
**Animação**: Perguntas aparecem uma a uma
**Imagem**: Caixa amarela de discussão
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vamos discutir em duplas. Cada dupla pega 2 minutos. Depois compartilhamos. As perguntas são projetadas para fazer vocês pensarem criticamente: (1) sobre escala — quando hierarchical degrada; (2) sobre robustez — quem valida a saída de um worker; (3) sobre design de hierarquia — onde colocar cada componente.
❓ RESPOSTAS ESPERADAS:
  1. Gargalo em 3+ níveis. Latência cumulativa.
  2. Ninguém detecta por padrão — o supervisor confia. Precisa de validação explícita (evaluator-optimizer).
  3. Depende. Se formatação é específica do writer, sub-worker faz sentido. Se é genérica, worker do supervisor (reutilizável).
➡️ TRANSIÇÃO: "A hierarchical que vimos tem um paralelo acadêmico importante: MetaGPT."

---

### Slide 26 — MetaGPT: SOPs como Hierarquia

**Título**: MetaGPT — SOPs como Hierarquia
**Objetivo**: Conectar hierarchical ao paper canônico MetaGPT.
**Conteúdo**:
- **MetaGPT**: framework multi-agente baseado em SOPs (Standard Operating Procedures)
- **Papéis**: Product Manager → Architect → Engineer → QA
- Cada papel = um agente com responsabilidade específica
- SOPs codificam o fluxo: PRD → design doc → código → testes
- **Lição**: a hierarquia reflete a organização humana de uma software house
- **Fonte**: arXiv:2308.00352

**Diagrama**: Hierarquia MetaGPT (PM → Architect → Engineer → QA) com artefatos fluindo
**Animação**: Papéis aparecem em sequência (top-down) com artefatos conectando
**Imagem**: Fluxograma MetaGPT com papéis e artefatos
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: MetaGPT (Hong et al., 2023) é o paper canônico de hierarchical multi-agent. A ideia central: pegar as SOPs de uma software house real (Product Manager escreve PRD, Architect faz design, Engineer codifica, QA testa) e codificá-las em agentes. Cada agente tem um papel, um conjunto de tools, e produz um artefato específico. O fluxo é um pipeline com elementos hierarchical: PRD → design doc → código → testes, cada etapa com um agente especializado. A lição fundamental: a topologia reflete a organização humana. Se você quer simular uma software house, a topologia deve espelhar a estrutura organizacional.
💡 ANALOGIA: MetaGPT é como simular uma empresa de software inteira. Cada agente é um funcionário com cargo, responsabilidade e entregável. As SOPs são os processos da empresa.
⚠️ ERROS COMUNS: Alunos acham que MetaGPT é "apenas um pipeline". É pipeline + hierarchical: a sequência é pipeline (PRD → design → código → testes), mas dentro de cada etapa pode haver hierarchical (Engineer tem sub-agentes para frontend, backend, etc.).
➡️ TRANSIÇÃO: "Outro conceito relacionado: crew formation."

---

### Slide 27 — Crew Formation: Montando uma Equipe

**Título**: Crew Formation — Montando uma Equipe
**Objetivo**: Introduzir o conceito de crew formation (CrewAI, AgentVerse).
**Conteúdo**:
- **Crew** = conjunto de agentes com papéis, objetivos e backstory
- **CrewAI**: `Agent(role, goal, backstory)` + `Task(description, agent)` + `Crew(agents, tasks, process)`
- **Process**: sequential (pipeline) ou hierarchical (supervisor)
- **AgentVerse** (arXiv:2308.10848): assembling agents como montar uma equipe humana
- **Pergunta**: *Como você montaria uma crew para revisar um PR?*

**Diagrama**: Crew = agentes + tarefas + processo (3 componentes conectados)
**Animação**: Componentes aparecem e se conectam
**Imagem**: Diagrama de crew com papéis, tarefas e processo
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Crew formation é o conceito de CrewAI: você define uma "equipe" de agentes, cada um com role (papel), goal (objetivo) e backstory (contexto/história). Depois define tasks (tarefas) e atribui cada task a um agent. Finalmente, define o process: sequential (pipeline — um após outro) ou hierarchical (supervisor orquestra). AgentVerse (Chen et al., 2023) traz a mesma ideia: assembling agents é como montar uma equipe humana — cada membro tem especialidade, e o processo define como trabalham juntos. A grande vantagem de crew formation é a abstração: você pensa em papéis e tarefas, não em código de orquestração.
💡 ANALOGIA: É como montar um time de projeto. Você define os papéis (desenvolvedor, designer, QA), as tarefas (codificar feature X, criar UI, testar), e o processo (sequencial ou com tech lead orquestrando). CrewAI formaliza isso para agentes.
❓ PERGUNTA PARA A TURMA: "Como você montaria uma crew para revisar um PR?" (discussão rápida — respostas: code reviewer, security reviewer, docs reviewer, com processo hierarchical)
⚠️ ERROS COMUNS: Alunos criam crews sem backstory. Backstory importa — dá contexto ao agente sobre quem ele é e como deve se comportar.
➡️ TRANSIÇÃO: "Vamos praticar a decisão de profundidade."

---

### Slide 28 — Exercício Rápido: Hierarchical ou Flat?

**Título**: Exercício — Hierarchical ou Flat?
**Objetivo**: Praticar a decisão de profundidade da hierarquia.
**Conteúdo**:
- 4 cenários:
  1. "Sistema com 3 domínios distintos (code, security, docs)" → ?
  2. "Chatbot simples com 3 ferramentas" → ?
  3. "Software house simulado com 6 papéis" → ?
  4. "Assistente de viagem com 4 sub-tarefas" → ?
- Votação rápida

**Diagrama**: 4 cards com cenários
**Animação**: Cards aparecem um a um
**Imagem**: Cards em `etho-light`
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Para cada cenário, votem: flat (1 supervisor), 2 níveis, ou 3 níveis. Pensem no critério: quantos workers? São domínios distintos? Precisa de síntese?
❓ RESPOSTAS ESPERADAS:
  1. 2 níveis (3 domínios distintos justificam sub-supervisores)
  2. Flat (3 ferramentas = 1 supervisor resolve)
  3. 2-3 níveis (MetaGPT: PM → Architect → Engineer → QA é pipeline, mas dentro de Engineering pode haver hierarchical)
  4. Flat (4 sub-tarefas em um domínio = 1 supervisor)
⚠️ ERROS COMUNS: Alunos votam hierarchical "para ser seguro". Hierarchical desnecessário adiciona latência e custo.
➡️ TRANSIÇÃO: "Vimos a topologia default. Agora a alternativa descentralizada: swarm."

---

## SEÇÃO D — Swarm e Handoffs (Slides 29-34 · 10 min)

---

### Slide 29 — [SEÇÃO] Swarm e Handoffs

**Título**: 3 — Swarm e Handoffs: Controle Descentralizado
**Objetivo**: Transição visual para o bloco de swarm.
**Conteúdo**: Número "3" grande + "Swarm e Handoffs: Controle Descentralizado"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "3" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Entramos na topologia descentralizada mais popular. Vamos ver como o swarm funciona (handoffs), quando é melhor que supervisor, seus limites, e uma comparação estruturada.
➡️ TRANSIÇÃO: "Primeiro: o que é swarm?"

---

### Slide 30 — OpenAI Swarm: Transfer de Controle

**Título**: OpenAI Swarm — Transfer de Controle
**Objetivo**: Apresentar o padrão swarm com handoffs.
**Conteúdo**:
- **OpenAI Swarm** (2024): agentes leves com `transfer()` de controle
- Fluxo: Agente A recebe tarefa → se não for dele, `transfer(to=agent_b)`
- Não há orquestrador central — controle passa de agente para agente
- **Analogia**: triagem em hospital — paciente é repassado até o especialista certo
- Estado é passado no handoff (context transfer)

**Diagrama**: `12-Diagrams/ETHAGT10/swarm-topology.mmd`
**Animação**: Handoff animado (agente A → seta → agente B → seta → agente C)
**Imagem**: Diagrama swarm com handoffs tracejados
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Swarm (OpenAI, 2024) é a topologia descentralizada baseada em handoffs. Não há supervisor. Em vez disso, cada agente pode transferir controle para outro agente. O agente A recebe a tarefa; se não for da sua especialidade, chama `transfer(to=agent_b)` e o controle passa para o agente B, junto com o contexto acumulado. O agente B continua; se precisar, transfere para C. É como uma triagem em hospital: o paciente é repassado de especialista em especialista até encontrar o certo. A vantagem: sem orquestrador central, sem hop extra, latência baixa. A desvantagem: sem visão global, coordenação difícil.
💡 ANALOGIA: É como um jogo de "quem sabe, responde". Alguém faz uma pergunta; se a pessoa não sabe, diz "pergunta pro João"; o João, se não sabe, diz "pergunta pro Pedro". A pergunta viaja até encontrar quem sabe. Ninguém coordena — o fluxo emerge.
⚠️ ERROS COMUNS: Alunos confundem swarm com mesh. Swarm transfere controle (1 ativo por vez). Mesh permite múltiplos ativos simultaneamente.
➡️ TRANSIÇÃO: "Quando swarm é melhor que supervisor?"

---

### Slide 31 — Quando Transfer é Melhor que Roteamento Central

**Título**: Quando Transfer é Melhor que Roteamento Central
**Objetivo**: Dar critério para escolher swarm sobre supervisor.
**Conteúdo**:
- **Swarm é melhor quando**:
  - Não há necessidade de síntese central
  - Agentes são especializados em domínios distintos
  - Latência importa (sem supervisor como hop extra)
  - Tarefa é "encontrar o especialista certo" (não orquestrar múltiplos)
- **Supervisor é melhor quando**:
  - Síntese de múltiplos workers é necessária
  - Controle de ordem importa
  - Estado global precisa ser mantido

**Diagrama**: 2 colunas comparativas (Swarm vs Supervisor)
**Animação**: Colunas aparecem uma a uma
**Imagem**: Tabela comparativa colorida
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O critério chave é: você precisa de síntese? Se a tarefa é "encontre o especialista certo e deixe ele resolver", swarm é melhor — sem hop de supervisor. Se a tarefa é "use 3 especialistas e sintetize um relatório", supervisor é melhor — alguém precisa agregar. Outro critério: latência. Swarm tem um agente ativo por vez, sem roteador. Supervisor adiciona um hop (o supervisor) a cada decisão. Se latência é crítica, swarm.
💡 ANALOGIA: Swarm = balcão de atendimento onde você é encaminhado de guichê em guichê. Supervisor = gerente que coordena 3 guichês e sintetiza o resultado. Se você só precisa de um especialista, balcão (swarm). Se precisa de 3 opiniões combinadas, gerente (supervisor).
⚠️ ERROS COMUNS: Alunos escolhem swarm "porque é mais moderno". Swarm é mais leve, não "melhor". Se precisa síntese, swarm não serve.
➡️ TRANSIÇÃO: "Mas swarm tem limites. Vamos ser honestos."

---

### Slide 32 — Limites do Swarm

**Título**: Limites do Swarm
**Objetivo**: Ser honesto sobre as limitações do swarm.
**Conteúdo**:
- **Coordenação complexa**: swarm não orquestra, só transfere
- **Estado compartilhado**: cada handoff passa contexto, pode crescer
- **Loops**: agente A transfere para B que transfere de volta para A
- **Sem visão global**: nenhum agente "sabe" o estado do sistema
- **Debugging difícil**: traçar o caminho do handoff é não-trivial

**Diagrama**: 5 ícones de "perigo" com labels
**Animação**: Ícones aparecem um a um
**Imagem**: Ícones de aviso (triângulo amarelo)
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Swarm não é bala de prata. Os 5 problemas mais comuns: (1) coordenação — swarm não orquestra tarefas paralelas, só transfere controle; (2) estado — cada handoff copia contexto, que cresce a cada transferência; (3) loops — sem detecção, A transfere para B que transfere para A indefinidamente; (4) sem visão global — nenhum agente tem o panorama do que aconteceu; (5) debugging — o trace é uma cadeia de handoffs, difícil de seguir. Em produção, o problema de loops é o mais grave: adicione max_handoffs e detecção de ciclo.
💡 ANALOGIA: É como uma linha de produção sem supervisor. Se algo dá errado, ninguém percebe — cada estação só faz sua parte. Sem visão global, problemas sistêmicos passam despercebidos.
⚠️ ERROS COMUNS: Alunos não implementam max_handoffs. Sem isso, loops infinitos gastam orçamento. Adicione `max_handoffs=10` desde o início.
➡️ TRANSIÇÃO: "Vamos sistematizar swarm vs supervisor."

---

### Slide 33 — Swarm vs Supervisor (Comparação Estrutural)

**Título**: Swarm vs Supervisor — Comparação Estrutural
**Objetivo**: Sistematizar os trade-offs entre as duas topologias.
**Conteúdo**:

| Eixo | Swarm | Supervisor |
|---|---|---|
| Controle central | Nenhum | Total |
| Síntese | Não nativa | Nativa |
| Latência | Baixa (sem hop) | Média (1 hop extra) |
| Custo | Baixo (1 agente ativo) | Médio (supervisor + workers) |
| Complexidade | Baixa | Média |
| Escalabilidade | Alta | Limitada (supervisor gargalo) |
| Debugging | Difícil (cadeia) | Mais fácil (ponto central) |
| Estado global | Não | Sim |

**Diagrama**: Tabela comparativa colorida (verde/amarelo)
**Animação**: Linhas da tabela aparecem uma a uma
**Imagem**: Tabela com cores indicando vantagens/desvantagens
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esta tabela é o resumo mais útil da aula. Usem-na como referência rápida. Os pontos-chave: swarm ganha em latência, custo e escalabilidade. Supervisor ganha em síntese, controle e debugging. A escolha depende do que é mais importante para o seu caso. Notem: não há "vencedor" — há trade-offs. A pergunta certa não é "qual é melhor?" mas "qual é melhor PARA ESTE CONTEXTO?".
💡 ANALOGIA: É como comparar bicicleta (swarm) com carro (supervisor). Bicicleta é mais barata, ágil, estaciona fácil. Carro é mais confortável, carrega mais, protege da chuva. Qual é melhor? Depende do trajeto.
⚠️ ERROS COMUNS: Alunos memorizam "swarm = escalável" sem entender por quê. Swarm escala porque não tem ponto central de gargalo. Mas perde em consistência.
➡️ TRANSIÇÃO: "Vamos discutir."

---

### Slide 34 — Pergunta: Swarm ou Supervisor?

**Título**: Pergunta — Swarm ou Supervisor?
**Objetivo**: Discussão sobre escolha entre as duas topologias.
**Conteúdo**:
- "Para o caso de revisão de PR com 3 especialistas: swarm ou supervisor?"
- "E se precisarmos sintetizar as 3 revisões em um relatório?"
- "E se cada especialista trabalha de forma independente?"
- Discussão aberta (3 min)

**Diagrama**: Caixa de discussão
**Animação**: Perguntas aparecem uma a uma
**Imagem**: Caixa amarela de discussão
**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Discussão aberta. As 3 perguntas são projetadas para mostrar que a resposta muda com o requisito. Revisão de PR com 3 especialistas: depende. Se precisa sintetizar (relatório unificado), supervisor. Se cada especialista trabalha independente (3 relatórios separados), swarm. A lição: NÃO existe resposta universal. A topologia depende dos requisitos.
❓ DINÂMICA: Deixar 3 min de discussão aberta. Pedir 2-3 alunos para compartilhar. Provocar: "E se o requisito mudar amanhã? A topologia precisa mudar também?"
➡️ TRANSIÇÃO: "Fim do Bloco 1. Intervalo de 5 min. Quando voltarmos: pipeline, event-driven e as topologias avançadas."

---

*(Fim da Parte 1 — continua em 03-slides-detalhados-parte2.md)*
