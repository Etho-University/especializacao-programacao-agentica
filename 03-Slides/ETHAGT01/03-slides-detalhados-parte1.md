# ETHAGT01 — Slides Detalhados + Notas do Professor (Parte 1: Slides 1-31)

> Universidade Etho · Especialização em Programação Agêntica
> Cada slide contém: título, objetivo, conteúdo, notas do professor, diagrama, animação, imagem, tempo.

---

## SEÇÃO A — Abertura (Slides 1-6 · 8 min)

---

### Slide 1 — Capa

**Título**: ETHAGT01 — Arquitetura Cognitiva de Agentes LLM
**Objetivo**: Identificar a aula, o professor e o contexto dentro da especialização.
**Conteúdo**:
- ETHAGT01 — Arquitetura Cognitiva de Agentes LLM
- Universidade Etho · Especialização em Programação Agêntica
- Fase A — Fundamentos Agênticos · 25 h
- Professor · Data

**Diagrama**: Logo Etho (canto sup. esquerdo) + imagem de fundo abstrata (redes neurais / circuitos)
**Animação**: Fade in do título (300ms)
**Imagem**: Fundo `etho-dark` (#0F1E2D) com pattern sutil de nós e arestas
**Tempo**: 1 min

**Rodapé**: `LLM` = Large Language Model — Modelo de Linguagem de Grande Escala

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Bem-vindos. Esta é a primeira aula da Especialização em Programação Agêntica. Hoje vamos estabelecer o bloco fundamental — o Augmented LLM em loop — que será a base de todos os módulos seguintes. Não vamos falar de frameworks hoje; vamos falar de arquitetura. Se você entender o bloco fundamental, todo framework será apenas uma instanciação dele.
💡 ANALOGIA: É como aprender a cozinhar vs aprender a usar uma panela específica. Hoje vocês vão aprender a cozinhar. As panelas (LangGraph, CrewAI, etc.) vêm depois.
❓ PERGUNTA PARA A TURMA: "Quantos de vocês já usaram um framework de agentes em produção?" (levantar mãos — calibrar nível da turma)
⚠️ ERROS COMUNS: Alunos chegam querendo aprender LangGraph/CrewAI. Preciso redirecionar: "Framework é instanciação. Arquitetura é o que importa."
➡️ TRANSIÇÃO: "Vamos começar definindo o que vocês vão conseguir fazer ao final desta aula."

---

### Slide 2 — Objetivos do Módulo

**Título**: Objetivos do Módulo
**Objetivo**: Deixar claro o que o aluno deve conseguir FAZER ao final da aula.
**Conteúdo**:
- **Objetivo geral**: Estabelecer o bloco fundamental — Augmented LLM em loop — e a distinção workflow vs agente
- **Objetivos específicos**:
  1. Explicar a transição de "LLM como oráculo" para "LLM como controlador cognitivo"
  2. Decompor um agente em Perception · Brain · Planning · Action · Tool Use
  3. Implementar um agente ReAct do zero (sem framework)
  4. Diferenciar workflows de agentes e justificar quando usar cada
  5. Adicionar observabilidade mínima desde a primeira implementação
  6. Avaliar criticamente 3 frameworks sob a lente dos princípios

**Diagrama**: 6 ícones representando cada objetivo (loop, brain, código, bifurcação, gráfico, lupa)
**Animação**: Objetivos aparecem um a um (on click)
**Imagem**: Ícones minimalistas em `etho-accent` (#E85D2F)
**Tempo**: 2 min

**Rodapé**: `ReAct` = Reasoning and Acting — padrão onde o agente intercala Thought, Action e Observation em loop

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Cada objetivo é mensurável. Não é "entender" — é "explicar", "decompor", "implementar", "diferenciar", "adicionar", "avaliar". Se ao final da aula você não consegue fazer essas seis coisas, eu falhei como professor. Vamos revisar estes objetivos no final para confirmar.
💡 ANALOGIA: É como um checklist de pré-voo. O piloto não diz "entendo como voar" — ele verifica cada item: flaps, trem, motor. Hoje, nosso checklist é estes 6 objetivos.
❓ PERGUNTA PARA A TURMA: "Qual desses objetivos vocês acham mais desafiador?" (deixar responder — costuma ser #4 ou #6)
⚠️ ERROS COMUNS: Alunos confundem "apender ReAct" com "aprender LangGraph". ReAct é o padrão; LangGraph é uma implementação. O objetivo #3 é implementar ReAct SEM framework.
➡️ TRANSIÇÃO: "Antes de saber o que vamos fazer, vamos saber onde estamos no mapa da especialização."

---

### Slide 3 — Competências Desenvolvidas

**Título**: Competências Desenvolvidas
**Objetivo**: Conectar a aula ao Framework Etho de competências.
**Conteúdo**:

| Competência | Nível ao final | Próximo nível em |
|---|---|---|
| C1 Programação Agêntica | **I** (Intermediário) | ETHAGT04-16 |
| C3 MCP & Tool Use | **B** (Básico) | ETHAGT02, ETHAGT08 |
| C4 Agent Memory | **B** (Básico) | ETHAGT05 |
| C5 AgentOps & Avaliação | **B** (Básico) | ETHAGT12 |

**Diagrama**: Radar chart com 4 eixos mostrando nível B/I
**Animação**: Radar aparece com wipe (left-to-right, 500ms)
**Imagem**: Badge visual por competência (círculos coloridos)
**Tempo**: 1 min

**Rodapé**: `MCP` = Model Context Protocol — Protocolo de Contexto de Modelo (padrão aberto da Anthropic para conectar LLMs a ferramentas) · `AgentOps` = Agent Operations — práticas de operação e monitoramento de agentes em produção

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O Framework Etho tem 6 competências em 3 níveis (Básico, Intermediário, Avançado). Este módulo toca 4 delas. A competência C1 — Programação Agêntica — atinge nível Intermediário aqui, o que significa que você consegue construir um agente funcional e justificar escolhas arquiteturais. As outras três ficam em Básico — você conhece o conceito e consegue operar, mas o aprofundamento vem em módulos posteriores.
💡 ANALOGIA: É como aprender a dirigir. Hoje você vai sair do estacionamento (Básico) e dirigir na cidade (Intermediário em C1). Dirigir na neblina de noite em uma rodovia (Avançado) vem depois.
⚠️ ERROS COMUNS: Alunos acham que "Básico" significa "superficial". Não — significa que é a fundação. Sem C3 Básico, você não entende ACI em ETHAGT02.
➡️ TRANSIÇÃO: "Vamos ver como esta aula está estruturada para entregar essas competências."

---

### Slide 4 — Agenda

**Título**: Agenda da Aula
**Objetivo**: Mostrar o roteiro da aula com tempos estimados.
**Conteúdo**:
- **Bloco 1 (45 min)**:
  - Abertura (8 min) — objetivos, motivação, contexto
  - Fundamentos (22 min) — Augmented LLM, ReAct, DEMO
  - Workflows vs Agentes (10 min) — 5 padrões, decisão
  - Intervalo (5 min)
- **Bloco 2 (45 min)**:
  - Frameworks (15 min) — Python puro vs LangGraph vs OpenAI SDK
  - Observabilidade (8 min) — traces, logs, custo
  - Fechamento (12 min) — boas práticas, caso de estudo, quiz, Q&A

**Diagrama**: Timeline horizontal com 6 seções coloridas
**Animação**: Timeline cresce da esquerda para direita (500ms)
**Imagem**: Ícones de relógio por seção
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A aula tem dois blocos. O primeiro estabelece a teoria e mostra a demo. O segundo é mais prático: frameworks, observabilidade e fechamento. Há um intervalo de 5 min entre os blocos. O quiz final tem 5 perguntas — é individual e serve para vocês auto-avaliarem.
💡 ANALOGIA: É como um prato de restaurante: primeiro a entrada (abertura), depois o prato principal (fundamentos), a sobremesa (frameworks), e o café (fechamento). Cada parte tem um propósito.
⚠️ ERROS COMUNS: Alunos chegam atrasados e perdem a abertura. Avisar que a motivação (Slide 5) define o tom de toda a aula.
➡️ TRANSIÇÃO: "Vamos começar pelo porquê. Por que estamos aqui?"

---

### Slide 5 — Motivação: O Problema do Oráculo

**Título**: O Problema do Oráculo
**Objetivo**: Criar tensão cognitiva — LLM puro falha em tarefas multi-step.
**Conteúdo**:
- **Cenário**: "Reserve voo + hotel + carro para a conferência em São Paulo"
- **LLM puro (oráculo)**: responde uma vez, não pode agir, não pode verificar, não pode iterar
- **O que falta**:
  - Não pode chamar APIs de reserva
  - Não pode verificar disponibilidade
  - Não pode adaptar se o voo está cheio
  - Não pode lembrar do estado entre passos
- **Pergunta**: *Quantos de vocês já tentaram fazer uma tarefa multi-step com ChatGPT puro e fracassaram?*

**Diagrama**: Split — esquerda: oráculo (bola de cristal) | direita: loop multi-step
**Animação**: Split — lado esquerdo aparece primeiro, depois lado direito
**Imagem**: Ícone de bola de cristal (esquerda) vs fluxograma de loop (direita)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O LLM puro é como um oráculo — você faz uma pergunta, ele responde, e acabou. Mas tarefas reais não funcionam assim. "Reserve voo + hotel + carro" requer: buscar voos, verificar disponibilidade, escolher, reservar, adaptar se não houver vaga, conectar com hotel, etc. Cada passo depende do anterior. O LLM puro não pode fazer isso porque não pode agir (sem tools), não pode observar (sem environment), e não pode iterar (sem loop).
💡 ANALOGIA: Imagine pedir para um consultor de viagens te ajudar, mas ele só pode falar uma vez. Ele não pode pesquisar, não pode ligar para o hotel, não pode verificar preços. Só pode dar um palpite baseado no que ele já sabe. É assim que o LLM puro funciona.
❓ PERGUNTA PARA A TURMA: "Quantos de vocês já tentaram fazer uma tarefa multi-step com ChatGPT puro e fracassaram?" (levantar mãos — a maioria vai levantar)
⚠️ ERROS COMUNS: Alunos acham que "prompt melhor" resolve. Não resolve. O problema não é o prompt — é a ausência de loop, tools e memória.
➡️ TRANSIÇÃO: "Essa limitação não é nova. Mas por que só agora temos uma solução viável?"

---

### Slide 6 — Contexto: Por Que Agora

**Título**: Por Que Agora
**Objetivo**: Explicar a confluência histórica que tornou agentes viáveis em 2024-2025.
**Conteúdo**:
- **Linha do tempo**:
  - 2020: GPT-3 (capacidade de linguagem, sem tools)
  - 2022: Chain-of-Thought (reasoning emergente)
  - Mar/2023: ReAct (paper, Yao et al.)
  - Jun/2023: Function calling (OpenAI API)
  - Dez/2024: Anthropic *Building Effective Agents* (marco)
  - 2025: Agent frameworks amadurecem (LangGraph, CrewAI, OpenAI SDK)
- **Confluência de 4 fatores**:
  1. Reasoning (CoT, ToT, Reflexion)
  2. Tool calling estruturado (function calling)
  3. Context window expandida (128k+)
  4. Redução de custo (GPT-4o-mini, Claude Haiku)

**Diagrama**: Timeline horizontal com marcos + 4 setas convergindo para "Agentes viáveis"
**Animação**: Marcos aparecem sequencialmente (on click)
**Imagem**: Convergência de 4 rios em um lago
**Tempo**: 1 min

**Rodapé**: `CoT` = Chain-of-Thought — Cadeia de Pensamento (técnica de prompting que leva o modelo a raciocinar passo a passo) · `ToT` = Tree of Thoughts — Árvore de Pensamentos (explora múltiplos caminhos de raciocínio em árvore)

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Agentes não são ideia nova — o conceito existe desde a década de 90 (agentes autônomos em IA clássica). Mas três coisas mudaram: (1) LLMs ficaram bons o suficiente em reasoning para planejar; (2) tool calling estruturado permitiu ação confiável; (3) context window cresceu o suficiente para manter estado. O custo baixou o suficiente para que múltiplas chamadas em loop sejam viáveis economicamente. A publicação da Anthropic em dez/2024 é o marco porque sistematiza o que funciona em produção.
💡 ANALOGIA: É como a invenção do avião. O conceito de voar existia há séculos (Da Vinci), mas só foi possível quando motor leve o suficiente (combustão interna) + aerodinâmica (estrutura) + materiais (alumínio) convergiram. Agentes precisavam que reasoning + tools + context + custo convergissem.
❓ PERGUNTA PARA A TURMA: "Qual desses 4 fatores vocês acham que foi o gatilho mais recente?" (Resposta: custo — os outros já existiam, mas o custo tornou o loop economicamente viável)
⚠️ ERROS COMUNS: Alunos acham que agentes são "nova tecnologia". O padrão ReAct é de 2022. O que é novo é a viabilidade econômica e a qualidade do reasoning.
➡️ TRANSIÇÃO: "Agora que sabemos por que estamos aqui, vamos ao bloco fundamental."

---

## SEÇÃO B — Fundamentos (Slides 7-22 · 22 min)

---

### Slide 7 — [SEÇÃO] Do LLM ao Agente

**Título**: 1 — Do LLM ao Agente
**Objetivo**: Transição visual para o bloco de fundamentos.
**Conteúdo**: Número "1" grande + "Do LLM ao Agente"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "1" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Início do bloco de fundamentos. Vamos responder: o que muda quando transformamos um LLM em agente? Qual é a anatomia de um agente? E qual é a transição histórica e técnica?
➡️ TRANSIÇÃO: "Primeiro: o que é um agente, afinal?"

---

### Slide 8 — Definições: O Que É um Agente?

**Título**: O Que É um Agente?
**Objetivo**: Mostrar que "agente" tem definições concorrentes e o recuo pragmático de Anthropic.
**Conteúdo**:
- **Definição ampla**: Sistema autônomo que opera por longos períodos, usando múltiplas tools, sem intervenção humana
- **Definição restritiva**: Sistema que segue um workflow predefinido com LLM em alguns steps
- **Recuo pragmático (Anthropic)**: "Agentic systems" = workflows + agentes
  - Workflows: LLMs e tools orquestrados via **código predefinido**
  - Agentes: LLM **direciona seu próprio processo** e tool usage
- **Pergunta**: *Qual definição sua equipe usa hoje?*

**Diagrama**: 3 colunas comparativas com exemplos
**Animação**: Colunas aparecem uma a uma (on click)
**Imagem**: Espectro: Workflow (esquerda, verde) ←→ Agente (direita, rosa)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A palavra "agente" é problemática. Cada empresa, cada paper, cada framework usa uma definição diferente. A Anthropic fez algo inteligente: em vez de brigar pela definição "correta", cunhou "agentic systems" como guarda-chuva. Dentro dele, há workflows (você controla o fluxo via código) e agentes (o modelo controla o fluxo). Essa distinção é ARQUITETURAL, não semântica. Ela determina como você constrói, testa e opera o sistema.
💡 ANALOGIA: É como a diferença entre um trem (workflow — trilhos predefinidos, sem flexibilidade) e um táxi (agente — motorista decide o caminho, flexível mas imprevisível). Ambos te levam ao destino, mas com trade-offs diferentes.
❓ PERGUNTA PARA A TURMA: "Qual definição sua equipe usa hoje? Vocês chamam tudo de 'agente' ou distinguem?" (Deixar 2-3 pessoas responderem)
⚠️ ERROS COMUNS: Alunos chamam qualquer coisa com LLM de "agente". Se não há loop e autonomia, é um workflow. Usar "agente" para tudo infla expectativas e confunde stakeholders.
➡️ TRANSIÇÃO: "Se concordamos na definição, vamos decompor um agente em partes."

---

### Slide 9 — Taxonomia Unificada

**Título**: Taxonomia Unificada de Agentes
**Objetivo**: Apresentar a decomposição canônica de um agente em 6 componentes.
**Conteúdo**:
- Fonte: arXiv:2601.12560 (Arunkumar et al., 2026)
- **6 componentes**:
  1. **Perception** — como o agente percebe o mundo (input, tool results, environment)
  2. **Brain** — o LLM (motor cognitivo, reasoning)
  3. **Planning** — decompor objetivo em sub-tarefas
  4. **Action** — executar (tool calls, API calls)
  5. **Tool Use** — selecionar e usar ferramentas
  6. **Collaboration** — comunicação com outros agentes ou humanos

**Diagrama**: Mind map radial — hexágono com Brain no centro e 5 componentes ao redor
**Animação**: Componentes aparecem um a um no hexágono (on click)
**Imagem**: Hexágono colorido, cada vértice = 1 componente
**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O survey de arXiv:2601.12560 propôs uma taxonomia que cobre praticamente todo sistema agêntico. O Brain é o LLM — o motor cognitivo. Perception é como o agente recebe informação do mundo: prompt do usuário, resultado de tools, estado do ambiente. Planning é a capacidade de decompor um objetivo complexo em passos — hoje implementada via CoT, ToT, Reflexion (aprofundado em ETHAGT04). Action é a execução efetiva — chamar uma API, escrever um arquivo, enviar um email. Tool Use é a seleção e uso de ferramentas — intimamente ligado a ACI (ETHAGT02). Collaboration é comunicação com outros agentes (ETHAGT09-10) ou humanos (HITL). Hoje vamos focar em Brain + Action + Tool Use + Perception. Planning fica para ETHAGT04 e Collaboration para ETHAGT09.
💡 ANALOGIA: Pense num ser humano. Brain = cérebro. Perception = sentidos (visão, audição). Planning = pensar "primeiro faço A, depois B". Action = mover as mãos. Tool Use = pegar uma chave de fenda. Collaboration = pedir ajuda a um colega. Um agente LLM tem todos esses componentes, mas em escala diferente.
❓ PERGUNTA PARA A TURMA: "Qual desses 6 componentes vocês acham que é o mais fraco hoje em dia?" (Resposta comum: Planning — LLMs ainda são ruins em planejamento de longo prazo)
⚠️ ERROS COMUNS: Alunos acham que "Brain" é tudo. Não — sem Perception (tool results), o agente é cego. Sem Action, é só um oráculo. O poder vem da composição dos 6.
➡️ TRANSIÇÃO: "Com essa anatomia em mente, vamos ver a transição histórica: do LLM como gerador único para LLM como controlador cognitivo."

---

### Slide 10 — Transição: Geração Única → Controle Cognitivo

**Título**: De Geração Única para Controle Cognitivo
**Objetivo**: Mostrar a mudança de paradigma e suas implicações.
**Conteúdo**:
- **Antes (Geração única)**:
  - prompt → response (1 step)
  - Sem estado, sem memória, sem iteração
  - Custo previsível, latência baixa
- **Agora (Controle cognitivo)**:
  - prompt → plan → act → observe → adapt → ... → response (N steps)
  - Estado persistente, memória entre steps
  - Custo variável, latência alta
  - Erro composto (falha em step N propaga)
- **Implicações arquiteturais**:
  - Estado (checkpointer)
  - Memória (working vs persistente)
  - Orçamento (max_steps, max_cost)
  - Observabilidade (traces)
  - Error handling (retry, fallback, HITL)

**Diagrama**: Comparação visual — "1-step" (seta única) vs "N-step loop" (ciclo)
**Animação**: Setas mostrando a transição (esquerda → direita)
**Imagem**: Duas caixas lado a lado
**Tempo**: 2 min

**Rodapé**: `HITL` = Human-in-the-Loop — Humano no Ciclo (padrão onde humanos aprovam/editam ações críticas em checkpoints)

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A transição de geração única para controle cognitivo não é apenas "mais chamadas de LLM". É uma mudança de paradigma com implicações arquiteturais profundas. Quando você tem 1 step, o custo é previsível (1 chamada × tokens). Com N steps, o custo varia — uma query simples pode ser 1 step, uma complexa pode ser 20. A latência passa de segundos para minutos. O erro deixa de ser isolado e passa a ser composto — se o step 3 alucina uma action, o step 4 age sobre informação errada. Isso exige: estado (para resumir de onde parou), memória (para não repetir erros), orçamento (para não gastar infinito), observabilidade (para debugar), e error handling (para recuperar).
💡 ANALOGIA: É a diferença entre pedir um prato no restaurante (1 step — você pede, recebe) vs cozinhar (N steps — planejar, comprar, cortar, cozinhar, provar, ajustar). Cozinhar é mais poderoso mas exige mais infraestrutura: cozinha, utensílios, tempo, cleanup.
⚠️ ERROS COMUNS: Alunos subestimam o custo. Um agente com 10 steps, cada um com 2k tokens de contexto, a $0.01/1k tokens = $0.20 por execução. Em escala (1000 usuários/dia), são $200/dia = $6k/mês. Sem orçamento, você descobre no fim do mês.
➡️ TRANSIÇÃO: "Essa transição nos leva ao bloco fundamental que torna tudo possível: o Augmented LLM."

---

### Slide 11 — [SEÇÃO] O Augmented LLM

**Título**: 2 — O Augmented LLM: O Bloco Fundamental
**Objetivo**: Transição para o bloco fundamental de Anthropic.
**Conteúdo**: "2 — O Augmented LLM: O Bloco Fundamental"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "2" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Este é o slide mais importante da aula. Se vocês só lembrarem de uma coisa, deve ser esta: o Augmented LLM é o bloco fundamental de qualquer sistema agêntico. Tudo — workflows, agentes, multi-agentes — é composição deste bloco.
➡️ TRANSIÇÃO: "Vamos ver o que compõe este bloco."

---

### Slide 12 — O Bloco Fundamental

**Título**: O Augmented LLM
**Objetivo**: Apresentar o Augmented LLM como bloco base de todo sistema agêntico.
**Conteúdo**:
- **Definição (Anthropic)**: LLM enhanced with retrieval, tools, and memory
- **4 componentes**:
  - **LLM** — motor cognitivo (reasoning, geração)
  - **Retrieval** — o modelo gera suas próprias queries (não pipeline fixo)
  - **Tools** — extensão de ação (APIs, DB, execução, busca)
  - **Memory** — working (context window) vs persistente (checkpointer)
- **Princípio**: o modelo **decide** quando recuperar, qual tool chamar, o que reter
- **Interface bem documentada**: a regra de ouro (ACI)

**Diagrama**: `12-Diagrams/ETHAGT01/augmented-llm.mmd`
**Animação**: Componentes surgem do centro (LLM) para fora (on click)
**Imagem**: Diagrama do augmented LLM
**Tempo**: 3 min

**Rodapé**: `ACI` = Agent-Computer Interface — Interface Agente-Computador (design das tools; análoga à HCI para humanos)

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O Augmented LLM não é "LLM + alguma coisa". É uma mudança qualitativa: o modelo passa a ser ATIVO na decisão de quando usar cada capacidade. No RAG tradicional, o pipeline é fixo: query → retrieve → generate. No Augmented LLM, o modelo decide: "Preciso recuperar? Sim. Qual query? 'preço do produto X'. Recuperei. Preciso de mais? Não. Vou usar uma tool? Sim, verificar estoque." Essa autonomia é o que transforma um gerador de texto em um controlador cognitivo. A interface bem documentada — ACI — é tão crítica que a Anthropic dedicou um apêndice inteiro a ela. Vamos aprofundar ACI em ETHAGT02, mas o princípio fica desde já: invista tanto esforço na interface da tool quanto investiria na interface com um humano.
💡 ANALOGIA: O LLM puro é como um cérebro em uma jarra — inteligente mas isolado. O Augmented LLM é como um cérebro com olhos (perception via retrieval), mãos (tools) e memória (memory). A diferença não é só capacidade — é autonomia. O cérebro decide quando olhar, quando agir, quando lembrar.
❓ PERGUNDA PARA A TURMA: "Qual desses 4 componentes vocês acham que é mais negligenciado em produção?" (Resposta comum: Memory — a maioria esquece de persistir estado entre sessões)
⚠️ ERROS COMUNS: Alunos implementam "LLM + tools" e chamam de Augmented LLM. Faltam retrieval e memory. Sem retrieval, o agente não acessa conhecimento externo. Sem memory, cada interação é stateless — o agente não aprende com erros anteriores.
➡️ TRANSIÇÃO: "Vamos aprofundar cada componente, começando por retrieval."

---

### Slide 13 — Retrieval In-Loop

**Título**: Retrieval In-Loop
**Objetivo**: Explicar que retrieval não é pipeline externo — é decisão do modelo.
**Conteúdo**:
- **RAG tradicional (fixo)**:
  - query → retrieve → generate (pipeline predefinido)
  - Sempre recupera, independentemente da necessidade
- **RAG agêntico (in-loop)**:
  - Modelo decide SE e QUANDO recuperar
  - Modelo gera suas próprias search queries
  - Pode recuperar múltiplas vezes com queries diferentes
  - Pode decidir que não precisa recuperar
- **Vantagem**: eficiência (nem toda pergunta precisa de RAG) + flexibilidade (queries adaptativas)
- **Aprofundamento**: ETHAGT06 — RAG Agêntico

**Diagrama**: Comparação RAG fixo (pipeline linear) vs RAG agêntico (loop com decisão)
**Animação**: Setas mostrando decisão do modelo (diamond)
**Imagem**: Duas arquiteturas lado a lado
**Tempo**: 2 min

**Rodapé**: `RAG` = Retrieval-Augmented Generation — Geração Aumentada por Recuperação (técnica que recupera conhecimento externo antes de gerar a resposta)

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A grande diferença do retrieval in-loop é a DECISÃO. No RAG tradicional, você sempre recupera — mesmo para "oi, tudo bem?". Isso desperdiça tokens e latência. No RAG agêntico, o modelo avalia: "Esta pergunta precisa de conhecimento externo?" Se sim, gera uma query de busca. Se não, responde direto. E pode fazer isso múltiplas vezes: recuperar, avaliar, recuperar de novo com query diferente. Isso é poderoso mas caro — cada retrieval é uma chamada extra.
💡 ANALOGIA: RAG tradicional é como um estudante que sempre consulta o livro antes de responder, mesmo para "quanto é 2+2". RAG agêntico é como um estudante que sabe quando precisa consultar e quando não precisa — e sabe fazer buscas cada vez mais específicas.
❓ PERGUNTA PARA A TURMA: "Em que cenário o RAG fixo é melhor que o agêntico?" (Resposta: quando todas as queries precisam de retrieval e a latência extra do loop de decisão é desperdício)
⚠️ ERROS COMUNS: Alunos implementam RAG agêntico mas esquecem de dar ao modelo uma tool de "decisão". Sem a tool de busca ser explicitamente chamável, o modelo não pode decidir.
➡️ TRANSIÇÃO: "Se retrieval é acesso a conhecimento, tools são acesso a ação."

---

### Slide 14 — Tools como Extensão de Ação

**Título**: Tools como Extensão de Ação
**Objetivo**: Introduzir tool calling estruturado e seu papel no Augmented LLM.
**Conteúdo**:
- **O que são tools**: capacidades que o modelo não tem (API, DB, execução, busca web)
- **Tool calling estruturado**:
  - JSON Schema define nome, descrição, parâmetros
  - Modelo gera `tool_call` com argumentos
  - Sistema executa e retorna `observation`
  - Modelo consome a observation e continua
- **Exemplo** (calculator tool):
```python
TOOLS = [{
    "type": "function",
    "function": {
        "name": "calculator",
        "description": "Executa operação aritmética",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {"type": "number"},
                "b": {"type": "number"},
                "op": {"type": "string", "enum": ["+", "-", "*", "/"]}
            },
            "required": ["a", "b", "op"]
        }
    }
}]
```
- **Aprofundamento**: ETHAGT02 — Tool Calling e ACI

**Diagrama**: Fluxo: LLM → tool_call (JSON) → execução → observation → LLM
**Animação**: Fluxo step-by-step (on click)
**Imagem**: Diagrama de sequência
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Tools são a forma do agente AGIR no mundo. Sem tools, o agente só pode falar. Com tools, pode chamar APIs, executar código, buscar em banco de dados, enviar emails. O tool calling estruturado (function calling) é o mecanismo que tornou isso confiável: em vez de parsear texto livre, o modelo gera um JSON com schema definido. O sistema executa a função e retorna o resultado. O modelo consome o resultado e decide o próximo passo. Note a clareza da descrição: "Executa operação aritmética" — não é "faz conta". A descrição é o que o modelo usa para decidir QUANDO chamar essa tool. Descrição ruim = tool errada chamada.
💡 ANALOGIA: É como dar a um funcionário um manual de ferramentas. Cada ferramenta tem um nome, uma descrição do que faz, e parâmetros de uso. O funcionário (LLM) decide qual ferramenta pegar baseado na tarefa. Se o manual for confuso, ele pega a ferramenta errada.
❓ PERGUNTA PARA A TURMA: "O que acontece se duas tools tiverem descrições sobrepostas?" (Resposta: o modelo fica confuso e pode chamar a errada — daí a importância de ACI)
⚠️ ERROS COMUNS: Alunos colocam 20 tools com descrições vagas e reclamam que o modelo chama a errada. Menos tools, bem descritas, > muitas tools mal descritas.
➡️ TRANSIÇÃO: "Se tools são ação, memory é continuidade."

---

### Slide 15 — Memory: Working vs Persistente

**Título**: Memory: Working vs Persistente
**Objetivo**: Panorama de memória — sem aprofundar (ETHAGT05).
**Conteúdo**:
- **Working memory (context window)**:
  - Tudo que o modelo "vê" no prompt atual
  - Efêmera — some quando a sessão acaba
  - Limitada (128k-200k tokens, mas custo cresce)
- **Persistent memory (checkpointer)**:
  - Estado serializado entre sessões
  - Postgres, Redis, SQLite
  - Permite resumir execução e retomar
- **Tensão fundamental**:
  - Mais memória = mais contexto = melhor decisão
  - Mais memória = mais tokens = mais custo e latência
- **Estratégias**: summarization, eviction, entity memory (aprofundado em ETHAGT05)

**Diagrama**: Duas caixas: "Context Window" (curto prazo, efêmera) ↔ "Checkpointer" (longo prazo, persistente)
**Animação**: Setas bidirecionais entre as duas
**Imagem**: Ícone de cérebro (working) vs disco (persistent)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Memory é o componente mais subestimado do Augmented LLM. Working memory é a context window — tudo que o modelo vê agora. É como a memória de trabalho humana: você consegue lembrar dos últimos 5 minutos da conversa, mas não de tudo. Persistent memory é o checkpointer: o estado é serializado e pode ser recuperado. É como um caderno de anotações — você escreve e consulta depois. A tensão é: mais contexto na working memory = melhor decisão, mas mais custo. A solução não é "colocar tudo na context window" — é ter estratégias de summarization (resumir conversa antiga), eviction (remover irrelevante) e entity memory (lembrar fatos sobre entidades). Tudo isso em ETHAGT05.
💡 ANALOGIA: Working memory é como a sua memória de curto prazo durante uma reunião — você lembra do que foi dito nos últimos 10 minutos. Persistent memory é como o caderno onde você anota decisões — pode consultar semanas depois. Sem o caderno, você esquece. Sem a memória de curto prazo, você perde o fio da meada.
⚠️ ERROS COMUNS: Alunos tentam colocar todo o histórico na context window. Funciona por um tempo, mas em uma conversa longa (100+ turnos), o custo explode e a qualidade cai (o modelo se perde no meio de tanto contexto).
➡️ TRANSIÇÃO: "Há um princípio que conecta retrieval, tools e memory: a interface bem documentada."

---

### Slide 16 — A Regra de Ouro: Interface Bem Documentada

**Título**: A Regra de Ouro: ACI
**Objetivo**: Fixar o princípio de ACI (Agent-Computer Interface) desde o início.
**Conteúdo**:
- **Princípio (Anthropic)**: "Invista tanto esforço em ACI quanto em HCI"
- **ACI = Agent-Computer Interface**:
  - Como o agente interage com tools (vs HCI = como humano interage com computador)
  - Descrição de tool = docstring para um júnior
  - Poka-yoke: fazer difícil errar
- **Caso real (SWE-bench)**:
  - Problema: agente usava paths relativos errados após sair do diretório raiz
  - Solução: mudaram a tool para exigir **paths absolutos**
  - Resultado: erro desapareceu, sem mexer no prompt
- **Regra**: tempo em tools > tempo no prompt principal

**Diagrama**: Ícone de regra de ouro + antes (path relativo, erro) → depois (path absoluto, sucesso)
**Animação**: Transformação antes → depois (morph)
**Imagem**: Ícone de chave de fenda ajustando uma tool
**Tempo**: 1 min

**Rodapé**: `HCI` = Human-Computer Interface — Interface Humano-Computador (design de como humanos interagem com software) · `SWE-bench` = Software Engineering Benchmark — benchmark que mede capacidade de resolver issues reais do GitHub

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Este é o princípio mais subestimado em agentes. A Anthropic gastou MAIS tempo otimizando as tools do que o prompt principal do agente SWE-bench. Por quê? Porque a tool é o ponto de contato entre o modelo e o mundo. Se a tool é confusa, o modelo erra — não importa quão bom seja o prompt. O caso dos paths é perfeito: o agente saía do diretório raiz e começava a usar paths relativos errados. A solução óbvia seria "ensinar o modelo no prompt a usar paths absolutos". Mas isso é frágil — o modelo pode esquecer. A solução robusta foi mudar a TOOL para exigir paths absolutos. Aí o modelo não PODE errar, mesmo que queira. Isso é poka-yoke: tornar o erro impossível pela design da interface.
💡 ANALOGIA: É como design de UI. Se usuários clicam no botão errado com frequência, a solução não é "treinar os usuários" — é mover o botão. Com agentes, se o modelo chama a tool errada, a solução não é "prompt melhor" — é redesenhar a tool.
❓ PERGUNTA PARA A TURMA: "Vocês já tiveram um bug onde a 'solução' era melhorar o prompt, mas o real problema era a tool?" (Deixar 1-2 responderem)
⚠️ ERROS COMUNS: Alunos passam horas refinando o prompt do sistema e 5 minutos escrevendo a descrição da tool. Inverter essa proporção.
➡️ TRANSIÇÃO: "Com o Augmented LLM definido, vamos colocá-lo em movimento: o Agent Loop."

---

### Slide 17 — [SEÇÃO] O Agent Loop: ReAct

**Título**: 3 — O Agent Loop: ReAct
**Objetivo**: Transição para o padrão fundacional.
**Conteúdo**: "3 — O Agent Loop: ReAct"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "3" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O Augmented LLM é o bloco. O Agent Loop é como você o coloca em movimento. ReAct é o padrão fundacional — todo framework de agentes implementa alguma variação dele.
➡️ TRANSIÇÃO: "Vamos ver o padrão."

---

### Slide 18 — ReAct: Thought → Action → Observation

**Título**: ReAct: O Padrão Fundacional
**Objetivo**: Apresentar o padrão ReAct e por que ele funciona.
**Conteúdo**:
- **Padrão**: Thought → Action → Observation em loop
- **Fonte**: Yao et al., ICLR 2023 (arXiv:2210.03629)
- **Por que funciona**:
  - Thought força reasoning explícito (não pular para ação)
  - Action executa no ambiente (grounding)
  - Observation traz fato real (não alucinável)
  - Loop permite adaptação (se observation é inesperada, repensar)
- **Guardrails**:
  - `max_steps` — limite de iterações
  - `max_cost` — orçamento de tokens
  - `timeout` — limite de tempo

**Diagrama**: `12-Diagrams/ETHAGT01/agent-loop.mmd`
**Animação**: Loop animado — Thought → Action → Observation → Thought (circular)
**Imagem**: Diagrama do agent loop
**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: ReAct combina duas capacidades que eram separadas: reasoning (Chain-of-Thought) e acting (tool use). Antes do ReAct, você tinha LLMs que pensavam mas não agiam, ou agentes que agiam mas não pensavam. ReAct unifica: o modelo PRIMEIRO pensa (Thought), DEPOIS age (Action), e então OBSERVA o resultado (Observation). A Observation é crítica — é o grounding. O modelo não pode alucinar o resultado de uma tool; a tool retorna o que retornar. Se for inesperado, o modelo repensa. O max_steps é não-negociável: sem ele, o agente pode entrar em loop infinito e gastar todo o seu orçamento.
💡 ANALOGIA: É como um cientista fazendo um experimento. Thought = hipótese ("se eu misturar A e B, deve dar C"). Action = experimento (misturar). Observation = resultado ("deu D, não C"). Thought = "interessante, minha hipótese estava errada, vou tentar com E". Esse loop é a essência do método científico — e do ReAct.
❓ PERGUNTA PARA A TURMA: "O que acontece se removermos o Thought e formos direto para Action?" (Resposta: o modelo perde a capacidade de raciocinar antes de agir — começa a chamar tools aleatoriamente sem plano)
⚠️ ERROS COMUNS: Alunos implementam o loop sem max_steps. O agente entra em loop ("pensar → agir → observar → pensar → agir → observar → ...") e só para quando o orçamento de tokens acaba. Always set max_steps.
➡️ TRANSIÇÃO: "Vamos ver um trace real para concretizar."

---

### Slide 19 — Trace Real de um Agente ReAct

**Título**: Trace Real de Execução
**Objetivo**: Mostrar a saída real de um agente ReAct em execução.
**Conteúdo**:
- Console output (estilizado com cores):
```
[STEP 0]
  Thought: "Preciso saber a previsão do tempo no RJ para amanhã"
  Action: search("previsão tempo Rio de Janeiro amanhã")
  Observation: "25°C, possibilidade de chuva à tarde"

[STEP 1]
  Thought: "Agora posso responder sobre o clima"
  Action: (sem tool_call — resposta final)
  Answer: "Leve guarda-chuva. Amanhã no RJ: 25°C com
          possibilidade de chuva à tarde."
```

**Diagrama**: Print de console estilizado (fundo escuro, texto colorido)
**Animação**: Linhas aparecem sequencialmente (simulando execução, 200ms por linha)
**Imagem**: Terminal screenshot estilizado
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Este é um trace real do que acontece quando você roda um agente ReAct. Note três coisas: (1) Cada step tem Thought, Action, e Observation explicitamente. (2) A Observation é fato — não é o modelo imaginando, é o resultado real da tool. (3) No step 1, o modelo decide que não precisa de mais tools e dá a resposta final. Isso é o agente decidindo parar — o que nem sempre acontece. Às vezes o modelo acha que precisa de mais informação e continua. Por isso max_steps.
💡 ANALOGIA: É como ver o "pensar em voz alta" de alguém resolvendo um problema. Você vê cada passo do raciocínio, não só a resposta final. Isso é INVALIÁVEL para debugging — sem o trace, você não sabe onde o agente errou.
❓ PERGUNTA PARA A TURMA: "Como você saberia se este agente está funcionando bem sem o trace?" (Resposta: não saberia — o trace é a única forma de ver o raciocínio)
⚠️ ERROS COMUNS: Alunos não logam o Thought — só logam a Action e a Observation. Sem o Thought, você não sabe POR QUE o agente escolheu aquela action. O Thought é a intenção; sem ela, o trace é opaco.
➡️ TRANSIÇÃO: "ReAct é poderoso, mas tem limitações. Vamos ser honestos sobre elas."

---

### Slide 20 — Limitações do ReAct

**Título**: Limitações do ReAct
**Objetivo**: Ser honesto sobre os trade-offs do padrão.
**Conteúdo**:
1. **Loops infinitos** — sem max_steps, o agente pode repetir Thought → Action → Observation indefinidamente
2. **Custo cumulativo** — cada iteração adiciona tokens ao contexto (context cresce)
3. **Alucinação em ação** — modelo pode chamar tool inexistente ou passar args errados
4. **Latência serial** — cada step espera o anterior; N steps = N × latência
5. **Erro composto** — falha em step N propaga para N+1 (e é difícil isolar)
6. **Context exhaustion** — em conversas longas, context window enche e qualidade cai

**Diagrama**: 6 ícones de "perigo" com labels (triângulo de advertência)
**Animação**: Ícones aparecem um a um (on click)
**Imagem**: Ícones em `etho-danger` (#C0392B)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: ReAct não é bala de prata. Cada limitação tem mitigação: loops infinitos → max_steps. Custo cumulativo → summarization do contexto. Alucinação em ação → validação de args antes de executar. Latência serial → paralelização onde possível. Erro composto → observabilidade + retry. Context exhaustion → eviction + entity memory. Mas nenhuma mitigação é perfeita — o arquiteto precisa estar ciente dos trade-offs. Em ETHAGT04 (Reasoning & Planning) vamos ver evoluções do ReAct que endereçam algumas dessas limitações: Reflexion (auto-crítica), Tree of Thoughts (exploração de múltiplos caminhos), LATS (busca em árvore).
💡 ANALOGIA: É como as limitações de um carro. Velocidade limitada → limite de requisições (rate limit). Consumo de combustível → tanque maior. Desgaste dos pneus → rodízio. Nenhuma é fatal, mas você precisa saber para gerenciar.
❓ PERGUNTA PARA A TURMA: "Qual dessas 6 limitações vocês acham mais crítica em produção?" (Resposta comum: #5 erro composto — é o mais difícil de debugar)
⚠️ ERROS COMUNS: Alunos implementam ReAct sem nenhuma mitigação e dizem "está funcionando". Funciona na demo, não em produção. Em produção, sem max_steps e sem observabilidade, o agente vai falhar de forma opaca.
➡️ TRANSIÇÃO: "Vamos ver isso na prática. Demo ao vivo."

---

### Slide 21 — DEMO: ReAct em 50 Linhas

**Título**: DEMO: ReAct em 50 Linhas
**Objetivo**: Demo ao vivo — implementação mínima em Python puro.
**Conteúdo**:
- Código: `19-Examples/ETHAGT01/exemplo-01-react-loop/main.py`
- Tool: `calculator(a, b, op)` — operações aritméticas
- Query: "Quanto é 123 * 456 + 789?"
- Loop principal:
```python
max_steps = 5
for step in range(max_steps):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=TOOLS,
        tool_choice="auto"
    )
    msg = response.choices[0].message
    messages.append(msg)

    if not msg.tool_calls:
        print(f"Resposta final: {msg.content}")
        break

    for tc in msg.tool_calls:
        args = json.loads(tc.function.arguments)
        result = calculator(**args)
        messages.append({
            "role": "tool",
            "tool_call_id": tc.id,
            "content": str(result)
        })
```

**Diagrama**: Code block (esquerda) + terminal (direita) side-by-side
**Animação**: Highlight de linhas chave durante execução
**Imagem**: Screenshot do VS Code + terminal
**Tempo**: 5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esta é a parte mais importante da aula. Vamos rodar um agente ReAct REAL em 50 linhas de Python. Sem framework, sem magia. O código é simples: (1) definimos uma tool (calculator) com JSON Schema; (2) o loop chama o LLM com a tool disponível; (3) se o LLM retornar tool_call, executamos e adicionamos o resultado às messages; (4) se não retornar tool_call, é a resposta final. Vou rodar ao vivo. Prestem atenção em três coisas: (a) como o modelo decide qual tool chamar; (b) como o resultado da tool volta para o modelo; (c) como o modelo decide quando parar. A query "123 * 456 + 789" vai exigir 2 calls de calculator: primeiro 123*456, depois resultado+789.
💡 ANALOGIA: É como ver o motor de um carro funcionando com o capô aberto. Depois disso, quando vocês usarem LangGraph ou CrewAI, vão saber o que está acontecendo por baixo.
❓ PERGUNTA PARA A TURMA: (após rodar) "Vocês viram quantos steps o agente usou? Por que não 1 só?" (Resposta: porque a calculator só faz uma operação por vez — o modelo precisa chamar 2x e combinar)
⚠️ ERROS COMUNS: Se a demo falhar (API indisponível), tenho screenshot do trace. Não tentar debugar ao vivo — mostrar o screenshot e seguir.
➡️ TRANSIÇÃO: "Antes de seguir, uma pergunta para vocês."

---

### Slide 22 — Pergunta da DEMO

**Título**: O Que Acontece Se...?
**Objetivo**: Engajar a turma com perguntas sobre edge cases da demo.
**Conteúdo**:
- **Pergunta 1**: "O que acontece se a tool retornar erro? Quem trata?"
- **Pergunta 2**: "E se o modelo não chamar tool nenhuma?"
- **Pergunta 3**: "E se o modelo chamar uma tool que não existe?"
- **Discussão em duplas** (2 min)
- **Compartilhar** (1 min)

**Diagrama**: Caixa de discussão com 3 perguntas
**Animação**: Perguntas aparecem uma a uma
**Imagem**: Ícone de balão de discussão
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Deixem os alunos discutirem em duplas por 2 minutos. As respostas esperadas são: (1) Se a tool retorna erro, o resultado do erro volta como Observation para o modelo — o modelo pode decidir tentar de novo com args diferentes ou desistir. Mas se não houver try/except, a exceção quebra o loop. (2) Se o modelo não chama tool, o código entra no `if not msg.tool_calls` e imprime a resposta final — mesmo que não seja a correta. (3) Se o modelo chama tool inexistente, `calculator(**args)` vai falhar com KeyError — sem validação, o loop quebra. A lição: o código de 50 linhas não tem error handling. Em produção, cada uma dessas situações precisa ser tratada.
💡 ANALOGIA: É como perguntar "o que acontece se o pneu furar?" antes de dirigir. Você não espera o pneu furar para pensar nisso — você tem estepe.
⚠️ ERROS COMUNS: Alunos acham que o modelo "sabe" tratar erros. Não sabe — ele só vê a Observation. Se a Observation for um traceback de Python, o modelo fica confuso. O ideal é capturar o erro e retornar uma mensagem estruturada: {"error": "division by zero", "suggestion": "try with b != 0"}.
➡️ TRANSIÇÃO: "Excelente discussão. Agora vamos ver quando usar ReAct (agente) vs quando usar algo mais simples (workflow)."

---

### Slide 23 — [SEÇÃO] Workflows vs Agentes

**Título**: 4 — Workflows vs Agentes
**Objetivo**: Transição para a decisão arquitetural.
**Conteúdo**: "4 — Workflows vs Agentes"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "4" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Já temos o Augmented LLM e o Agent Loop. Agora a pergunta crítica: QUANDO usar um agente autônomo vs um workflow predefinido? Esta é a decisão arquitetural mais importante que vocês vão tomar.
➡️ TRANSIÇÃO: "Vamos à distinção canônica."

---

### Slide 24 — A Distinção Canônica

**Título**: Workflows vs Agentes
**Objetivo**: Apresentar a distinção canônica de Anthropic.
**Conteúdo**:
- **Workflows**: LLMs e tools orquestrados via **código predefinido**
  - Você controla o fluxo
  - Previsível, testável, barato
  - Limitação: inflexível
- **Agentes**: LLM **direciona seu próprio processo** e tool usage
  - O modelo controla o fluxo
  - Flexível, adaptativo, poderoso
  - Limitação: imprevisível, caro, difícil de testar
- **Fonte**: Anthropic, *Building Effective Agents* (2024)
- **Critério**: comece com workflow; só use agente quando a flexibilidade for necessária

**Diagrama**: `12-Diagrams/ETHAGT01/workflow-vs-agent.mmd`
**Animação**: Diagrama aparece com wipe
**Imagem**: Diagrama workflow-vs-agent
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A distinção é sobre QUEM controla o fluxo. No workflow, é o seu código: "primeiro chame o LLM para classificar, depois chame para responder". No agente, é o modelo: "modelo, aqui está a tarefa e as tools, faça como achar melhor". Workflow = trilhos de trem. Agente = táxi. O trem é previsível mas inflexível. O táxi é flexível mas você não sabe o caminho que vai fazer. A recomendação da Anthropic é clara: comece com workflow. Só migre para agente quando tiver evidência de que o workflow é insuficiente. Por quê? Porque agente é mais caro, mais lento, mais imprevisível e mais difícil de testar.
💡 ANALOGIA: É como cozinhar com receita (workflow) vs cozinhar livre (agente). A receita é previsível — você segue os passos e o prato sai igual sempre. Cozinhar livre é criativo mas o resultado varia. Para um restaurante com 1000 pedidos idênticos, receita. Para um chef criando um prato novo, livre.
❓ PERGUNTA PARA A TURMA: "Em que situação vocês usariam agente em vez de workflow?" (Respostas esperadas: quando os passos são imprevisíveis, quando o input é muito variado, quando a tarefa exige adaptação)
⚠️ ERROS COMUNS: Alunos começam com agente porque é "mais legal". O resultado é um sistema caro, imprevisível e difícil de manter. Sempre comece com a solução mais simples.
➡️ TRANSIÇÃO: "Anthropic catalogou 5 padrões de workflow. Vamos vê-los."

---

### Slide 25 — Os 5 Workflows Canônicos (Panorama)

**Título**: Os 5 Workflows Canônicos
**Objetivo**: Visão geral dos 5 padrões (aprofundamento em ETHAGT03).
**Conteúdo**:
1. **Prompt Chaining** — sequência de steps (gerar → revisar → traduzir)
2. **Routing** — classificar e dispatch (tipo de query → handler especializado)
3. **Parallelization** — sectioning (dividir em subtasks) ou voting (múltiplas tentativas)
4. **Orchestrator-Workers** — orquestrador delega dinamicamente para workers
5. **Evaluator-Optimizer** — loop de refinamento (gerar → avaliar → melhorar)

**Diagrama**: 5 mini-diagramas em grid 2x3 (cada um com fluxo simples)
**Animação**: Cada workflow aparece com click (esquerda → direita, cima → baixo)
**Imagem**: 5 mini-diagramas canônicos da Anthropic
**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Estes 5 padrões são os blocos de composição para workflows. Cada um resolve um problema específico: Prompt Chaining para tarefas que se decompõem em sequência linear. Routing para entradas que precisam de handlers especializados. Parallelization para velocidade (sectioning) ou confiabilidade (voting). Orchestrator-Workers para tarefas cujas subtasks não são previsíveis (ex: mudar N arquivos em um repo). Evaluator-Optimizer para tarefas que beneficiam de refinamento iterativo. O aprofundamento de cada um vem em ETHAGT03, mas é importante conhecer o landscape agora porque a decisão "workflow ou agente" depende de saber se algum destes padrões resolve o problema.
💡 ANALOGIA: É como conhecer os padrões de design do GoF (Gang of Four). Você não usa todos em todo projeto, mas precisa saber que existem para escolher o certo quando precisa.
❓ PERGUNTA PARA A TURMA: "Qual destes 5 padrões vocês já usaram?" (Deixar levantar mãos para cada um — Prompt Chaining e Routing são os mais comuns)
⚠️ ERROS COMUNS: Alunos acham que Orchestrator-Workers é "agente" porque delega. Não é — o orquestrador segue um fluxo predefinido de delegar e sintetizar. A diferença do agente é que o agente decide o PRÓXIO STEP dinamicamente, não segue um template.
➡️ TRANSIÇÃO: "Como decidir qual usar? Vamos à árvore de decisão."

---

### Slide 26 — Árvore de Decisão: Workflow ou Agente?

**Título**: Workflow ou Agente?
**Objetivo**: Dar um critério prático de decisão.
**Conteúdo**:
- **Q1**: Consigo listar os passos a priori?
  - **Sim** → **Workflow** (comece pelo padrão mais simples)
  - **Não** → Q2
- **Q2**: O número de passos é previsível?
  - **Sim, mas variável** → Q3
  - **Não** → **Agente**
- **Q3**: Posso confiar no modelo sem HITL?
  - **Sim** → **Agente** (autônomo)
  - **Não** → **Agente + HITL forte** (checkpoints críticos)

**Diagrama**: `12-Diagrams/ETHAGT01/workflow-vs-agent.mmd` (árvore de decisão)
**Animação**: Ramos da árvore aparecem sequencialmente (on click)
**Imagem**: Fluxograma de decisão
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esta árvore é um guia, não uma lei. A primeira pergunta é a mais importante: "Consigo listar os passos?" Se sim, workflow. Se não, a segunda pergunta filtra: mesmo que não possa listar os passos, o número é previsível? Se sim, pode ser um workflow com ramificação. Se não, agente. A terceira pergunta é sobre confiança: posso deixar o modelo decidir sozinho ou preciso de humano no loop? Em produção, a resposta é quase sempre "preciso de HITL em pontos críticos".
💡 ANALOGIA: É como decidir entre receita e improvisação na cozinha. "Sei os passos?" → receita. "Não sei, mas é um prato de complexidade previsível?" → posso improvisar com estrutura. "Não faço ideia de quantos passos serão necessários?" → improvisação livre, mas com alguém provando no meio.
❓ PERGUNTA PARA A TURMA: "Pensem no sistema de vocês: workflow ou agente?" (10 segundos para pensar)
⚠️ ERROS COMUNS: Alunos respondem "agente" para tudo porque soa mais poderoso. A realidade é que 80% dos casos de uso são resolvidos com workflow. Agente é para os 20% que precisam de flexibilidade.
➡️ TRANSIÇÃO: "Mesmo que escolham agente, existe uma escalada de complexidade."

---

### Slide 27 — A Escalada de Complexidade

**Título**: A Escalada de Complexidade
**Objetivo**: Fixar o princípio "comece simples, só aumente com evidência".
**Conteúdo**:
- **Nível 0**: Single LLM call + retrieval + in-context examples
  - 90% dos casos. Antes de tudo, tente isto.
- **Nível 1**: Workflow simples (prompt chaining, routing)
  - Quando 1 call não basta mas os passos são previsíveis
- **Nível 2**: Workflow complexo (orchestrator-workers, evaluator-optimizer)
  - Múltiplos LLMs coordenados via código
- **Nível 3**: Agente autônomo
  - Modelo controla o fluxo com tools em loop
- **Nível 4**: Multi-agente
  - Múltiplos agentes colaborando (ETHAGT09-10)
- **Regra**: só suba um nível com **evidência** de que o nível atual é insuficiente

**Diagrama**: Pirâmide — base larga (Nível 0) → topo estreito (Nível 4)
**Animação**: Níveis aparecem de baixo para cima (on click)
**Imagem**: Pirâmide colorida com 5 níveis
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Este é o princípio mais importante da aula: COMECE SIMPLES. A Anthropic é explícita: "encontre a solução mais simples possível e só aumente a complexidade quando necessário". Por quê? Porque cada nível adiciona custo, latência, imprevisibilidade e dificuldade de manutenção. A maioria dos casos de uso (estimativa: 90%) é resolvida no Nível 0 — uma chamada de LLM com bom prompt, retrieval e examples. Só suba se tiver EVIDÊNCIA de que o nível atual falha. "Acho que precisa de agente" não é evidência. "Testamos workflow e a acurácia foi 60%, insuficiente para o caso de uso" é evidência.
💡 ANALOGIA: É como escalada de remédios. Você não começa com quimioterapia para uma dor de cabeça. Começa com paracetamol. Se não resolver, analisa a causa. Só escala para tratamento mais agressivo com diagnóstico claro.
❓ PERGUNTA PARA A TURMA: "Em que nível está o sistema de vocês hoje?" (Deixar responder — a maioria estará em Nível 0 ou 1)
⚠️ ERROS COMUNS: Alunos pulam do Nível 0 direto para Nível 3 ou 4 porque "agentes são o futuro". O resultado é um sistema 10x mais caro e complexo do que precisava ser.
➡️ TRANSIÇÃO: "Vamos praticar esta decisão com 6 cenários."

---

### Slide 28 — Exercício Rápido: Workflow ou Agente?

**Título**: Workflow ou Agente?
**Objetivo**: Praticar a decisão em cenários reais.
**Conteúdo**:
- 6 cenários — votação rápida (mãos levantadas):
  1. "Traduzir documentação técnica EN→PT" → **Workflow** (prompt chaining)
  2. "Resolver issue de GitHub arbitrário" → **Agente** (passos imprevisíveis)
  3. "Classificar ticket de suporte por tipo" → **Workflow** (routing)
  4. "Pesquisar e sintetizar tema novo" → **Agente** (busca iterativa)
  5. "Revisar código em busca de bugs" → **Workflow** (parallelization/voting)
  6. "Negociar contrato com fornecedor" → **Agente + HITL** (alta stakes)

**Diagrama**: 6 cards com cenários (grid 2x3)
**Animação**: Cards aparecem um a um
**Imagem**: Ícones representando cada cenário
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Voto rápido. Para cada cenário, levantem a mão se acham que é workflow. Depois se acham que é agente. As respostas: (1) Workflow — tradução é sequência linear: traduzir → revisar → ajustar termos técnicos. (2) Agente — cada issue é diferente, não dá para predefinir passos. (3) Workflow — classificação é routing puro. (4) Agente — pesquisa requer iteração: buscar → avaliar → buscar mais → sintetizar. (5) Workflow — múltiplos revisores em paralelo (voting). (6) Agente + HITL — negociação é aberta mas erros são caros, então humano aprova cada step crítico.
💡 ANALOGIA: É como triagem médica. Cada paciente é um cenário. A maioria é resfriado (workflow — protocolo fixo). Alguns são complexos (agente — diagnóstico diferencial iterativo). E alguns são cirurgia (agente + HITL — alto risco, humano no loop).
⚠️ ERROS COMUNS: Alunos votam "agente" em tudo. Lembrar: se os passos são previsíveis, é workflow, mesmo que use LLM em cada step.
➡️ TRANSIÇÃO: "Intervalo. Voltamos em 5 min para a parte prática: frameworks."

---

### Slide 29 — [SEÇÃO] Implementação: Do Zero vs Framework

**Título**: 5 — Implementação: Do Zero vs Framework
**Objetivo**: Transição para comparação de implementação.
**Conteúdo**: "5 — Implementação: Do Zero vs Framework"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "5" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Já entendemos o que é um agente, o bloco fundamental, o loop, e quando usar. Agora vamos ver COMO implementar. Vamos comparar 3 abordagens: Python puro, LangGraph, e OpenAI Agents SDK. O objetivo não é dizer qual é "melhor" — é entender os trade-offs.
➡️ TRANSIÇÃO: "O mesmo agente, 3 implementações."

---

### Slide 30 — Três Implementações do Mesmo Agente

**Título**: O Mesmo Agente, 3 Implementações
**Objetivo**: Mostrar que o mesmo agente pode ser implementado de 3 formas com trade-offs diferentes.
**Conteúdo**:
- **Versão 1: Python puro + OpenAI SDK**
  - ~50 linhas
  - Controle total, transparência total
  - Mais código, mais responsabilidade
- **Versão 2: LangGraph**
  - ~20 linhas
  - StateGraph + checkpointer embutido
  - Abstrai loop e estado
- **Versão 3: OpenAI Agents SDK**
  - ~15 linhas
  - Agent(model, tools, instructions) → run()
  - Máxima produtividade, mínima transparência
- **Mensagem**: menos código ≠ melhor
  - Depende do CONTROLE que você precisa
  - Depende da TRANSPARÊNCIA que você exige
  - Depende do CONTEXTO (produção vs POC)

**Diagrama**: 3 colunas com contagem de linhas e ícones de controle/transparência
**Animação**: Colunas aparecem uma a uma (on click)
**Imagem**: 3 ícones: chave inglesa (puro), framework (LG), caixa preta (SDK)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O ponto central é: o mesmo agente ReAct com calculator tool pode ser implementado em 50, 20 ou 15 linhas. A diferença não é só "menos código" — é o que você vê e o que você controla. No Python puro, você vê o prompt efetivo exato, controla o loop, serializa o estado. No LangGraph, o loop é abstraído pelo StateGraph, o estado é serializado pelo checkpointer, mas você ainda vê os nodes. No OpenAI SDK, você define Agent com instructions e tools, chama run(), e tudo acontece "por baixo dos panos". Menos código é mais produtivo para POC. Em produção, menos transparência pode ser problemática — se o agente fizer algo inesperado, você precisa debugar.
💡 ANALOGIA: É como dirigir carro manual vs automático vs autônomo. Manual (Python puro): você controla tudo, vê tudo, mas é mais trabalho. Automático (LangGraph): mais fácil, mas você não controla as marchas. Autônomo (OpenAI SDK): você só diz o destino e confia no sistema. Cada um tem seu lugar.
❓ PERGUNTA PARA A TURMA: "Qual vocês escolheriam para um POC de 1 semana? E para produção com 10k usuários?" (POC: SDK. Produção: depende, mas geralmente LangGraph ou Python puro para controle)
⚠️ ERROS COMUNS: Alunos escolhem o SDK para produção porque "é mais fácil". Mas quando o agente falha em produção e você não sabe por quê, a transparência do Python puro vale o esforço extra.
➡️ TRANSIÇÃO: "Vamos ver cada uma em detalhe."

---

### Slide 31 — Python Puro: O Que Você Controla

**Título**: Python Puro: Controle Total
**Objetivo**: Mostrar as vantagens do Python puro.
**Conteúdo**:
- **Você controla**:
  - Prompt efetivo (exatamente o que o modelo recebe)
  - Loop (while not done → você decide quando parar)
  - Estado (você serializa e deserializa)
  - Tools (você valida args antes de executar)
- **Você vê**:
  - Cada mensagem no histórico
  - Cada tool_call e seu resultado
  - Custo de cada step
- **Snippet** (loop principal):
```python
for step in range(max_steps):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=TOOLS,
        tool_choice="auto"
    )
    msg = response.choices[0].message
    messages.append(msg)
    if not msg.tool_calls:
        break
    for tc in msg.tool_calls:
        result = calculator(**json.loads(tc.function.arguments))
        messages.append({"role": "tool", "tool_call_id": tc.id, "content": str(result)})
```

**Diagrama**: `12-Diagrams/ETHAGT01/framework-comparison.mmd` (lado esquerdo — Python puro)
**Animação**: Código aparece com syntax highlighting
**Imagem**: Diagrama framework-comparison (lado esquerdo)
**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: No Python puro, você é o mestre. O prompt que você escreve é EXATAMENTE o que o modelo recebe — sem wrapping, sem system prompts ocultos. O loop é seu: você decide max_steps, você decide quando parar, você decide o que fazer com cada resposta. O estado é explícito: a lista `messages` é o estado, e você pode serializá-la como quiser (JSON, pickle, Postgres). As tools são suas: você pode validar args, fazer try/except, logar antes/depois. A desvantagem é que VOCÊ é responsável por tudo. Se esquecer max_steps, loop infinito. Se não validar args, crash. Se não logar, debug cego. Mas para quem quer entender o que está acontecendo, não há substituto.
💡 ANALOGIA: É como cozinhar do zero vs usar mistura de bolo. Do zero você controla cada ingrediente, cada temperatura, cada tempo. A mistura é mais rápida mas você não sabe o que tem dentro. Em produção, às vezes você precisa saber exatamente o que tem dentro.
❓ PERGUNTA PARA A TURMA: "Quem aqui já implementou um agente em Python puro?" (Calibrar experiência da turma)
⚠️ ERROS COMUNS: Alunos acham que Python puro é "muito trabalho". O loop são 15 linhas. O trabalho não está no loop — está nas tools, no prompt, no error handling. E esse trabalho existe independentemente do framework.
➡️ TRANSIÇÃO: "Agora o mesmo agente com LangGraph."
