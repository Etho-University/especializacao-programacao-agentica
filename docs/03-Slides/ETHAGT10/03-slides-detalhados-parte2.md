# ETHAGT10 — Slides Detalhados + Notas do Professor (Parte 2: Slides 35-62)

> Universidade Etho · Especialização em Programação Agêntica
> Cada slide contém: título, objetivo, conteúdo, notas do professor, diagrama, animação, imagem, tempo.

---

## SEÇÃO E — Pipeline e Orchestrator-Workers (Slides 35-40 · 10 min)

---

### Slide 35 — [SEÇÃO] Pipeline e Orchestrator-Workers

**Título**: 4 — Pipeline e Orchestrator-Workers: Fluxo Controlado
**Objetivo**: Transição visual para o bloco de topologias de fluxo.
**Conteúdo**: Número "4" grande + "Pipeline e Orchestrator-Workers: Fluxo Controlado"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "4" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Início do Bloco 2. Vamos cobrir pipeline (fixo e dinâmico), orchestrator-workers, e a composição de topologias. Conexão com ETHAGT03 (5 workflows canônicos), onde vimos esses padrões em detalhe.
➡️ TRANSIÇÃO: "Primeiro: pipeline fixo vs dinâmico."

---

### Slide 36 — Pipeline Fixo vs Dinâmico

**Título**: Pipeline Fixo vs Dinâmico
**Objetivo**: Distinguir pipeline fixo de dinâmico em multi-agente.
**Conteúdo**:
- **Pipeline fixo**: A → B → C (sequência predefinida, código orquestra)
  - Cada step é um agente especializado
  - Ordem é hardcoded, não há decisão de roteamento
- **Pipeline dinâmico**: A decide se vai para B ou C (runtime decision)
  - O próximo step é decidido pelo agente em runtime
- Fixo = workflow (ETHAGT03), dinâmico = agente orquestrando agentes
- **Exemplo multi-agente**: research → draft → review → publish (4 agentes em pipeline)

**Diagrama**: 2 fluxogramas lado a lado (esteira linear vs esteira com bifurcação)
**Animação**: Fluxogramas aparecem um de cada vez
**Imagem**: Esteira de produção (fixo) vs bifurcação (dinâmico)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Pipeline fixo é a topologia mais simples: você define a ordem no código. Agente A executa, passa para B, B executa, passa para C. Não há LLM decidindo a ordem — é determinístico. Pipeline dinâmico permite que cada step decida o próximo: A pode decidir ir para B ou pular para C dependendo do resultado. Em multi-agente, cada step é um agente especializado. Exemplo: research agent → draft agent → review agent → publish agent. Fixo = previsível e barato. Dinâmico = flexível mas com custo de decisão.
💡 ANALOGIA: Pipeline fixo = linha de montagem (cada estação na ordem). Pipeline dinâmico = fluxograma com decisão (depois da estação A, pode ir para B ou C dependendo do resultado).
⚠️ ERROS COMUNS: Alunos implementam pipeline dinâmico quando fixo basta. Se a ordem é sempre a mesma, fixo é mais barato e previsível. Dinâmico só vale quando a ordem realmente varia.
➡️ TRANSIÇÃO: "Vamos revisitar orchestrator-workers."

---

### Slide 37 — Orchestrator-Workers Multi-Agente

**Título**: Orchestrator-Workers Multi-Agente
**Objetivo**: Revisitar orchestrator-workers no contexto multi-agente.
**Conteúdo**:
- **Orchestrator** = agente que particiona a tarefa e delega para workers
- **Diferença do supervisor**:
  - Orchestrator particiona UMA tarefa em sub-tarefas distintas
  - Supervisor roteia a tarefa inteira para um worker
- Orchestrator: "divida e conquiste" → síntese no final
- **Fonte**: Anthropic, Building Effective Agents (2024)
- **Aprofundamento**: ETHAGT03

**Diagrama**: Orchestrator no centro, workers em volta (estrela com síntese)
**Animação**: Orchestrator aparece, depois workers surgem, depois síntese
**Imagem**: Estrela com orchestrator no centro
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A distinção sutil mas importante: supervisor roteia a tarefa inteira para um worker (escolhe quem faz). Orchestrator pega uma tarefa, a divide em sub-tarefas, delega cada sub-tarefa para um worker, e sintetiza os resultados. Exemplo: "Escreva um relatório sobre IA em 2026". Supervisor escolhe um worker para fazer tudo. Orchestrator divide: worker A faz introdução, worker B faz estado da arte, worker C faz conclusão — depois sintetiza. O orchestrator é mais poderoso para tarefas que se decompõem naturalmente em partes distintas.
💡 ANALOGIA: Supervisor = recepcionista que encaminha para o setor certo. Orchestrator = arquiteto que pega um projeto grande, divide em módulos (fundação, estrutura, acabamento), delega cada um para um engenheiro, e integra.
⚠️ ERROS COMUNS: Alunos confundem orchestrator com supervisor. A diferença: orchestrator PARTICIONA (divide a tarefa), supervisor ROTEIA (escolhe quem faz a tarefa inteira).
➡️ TRANSIÇÃO: "Topologias não são mutuamente exclusivas — elas se compõem."

---

### Slide 38 — Composição: Pipeline + Hierarchical

**Título**: Composição — Pipeline + Hierarchical
**Objetivo**: Mostrar que topologias se compõem em sistemas reais.
**Conteúdo**:
- Pipeline onde um "step" é um sub-sistema hierarchical
- **Exemplo**: pipeline (research → [hierarchical: code review, security review, docs review] → publish)
  - O step de revisão é um supervisor com 3 workers especializados
- **Composição é a regra, não exceção** — sistemas reais são hybrid
- **Padrão**: pipeline no macro, hierarchical/swarm no micro

**Diagrama**: Pipeline com um step expandido como hierarchical
**Animação**: Pipeline aparece, depois um step "expande" em hierarchical
**Imagem**: Pipeline com zoom em um step mostrando hierarchical
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esta é uma lição crucial: topologias não são mutuamente exclusivas. Sistemas reais são hybrid. O padrão mais comum em produção: pipeline no macro (passos sequenciais) com hierarchical ou swarm no micro (dentro de cada step). Exemplo: um sistema de publicação de conteúdo pode ter pipeline (research → write → review → publish), mas o step de "review" internamente é hierarchical (supervisor com 3 revisores especializados). Não tente encaixar tudo em uma topologia — componha.
💡 ANALOGIA: É como uma empresa. O macro é um processo (pipeline: desenvolver → testar → deployar). Mas dentro de "desenvolver" há hierarchical (tech lead → devs frontend/backend). A empresa inteira é hybrid.
⚠️ ERROS COMUNS: Alunos tentam forçar uma única topologia. Se o sistema tem partes que são pipeline e partes que são hierarchical, use os dois. Hybrid não é "bagunça" — é realismo.
➡️ TRANSIÇÃO: "Quando pipeline é melhor que supervisor?"

---

### Slide 39 — Quando Pipeline > Supervisor

**Título**: Quando Pipeline > Supervisor
**Objetivo**: Critério para escolher pipeline sobre supervisor.
**Conteúdo**:
- **Pipeline é melhor quando**:
  - Passos são conhecidos e fixos (previsibilidade)
  - Ordem importa (A deve executar antes de B)
  - Custo precisa ser controlado (sem roteamento dinâmico)
  - Não há necessidade de decisão de roteamento em runtime
- **Supervisor é melhor quando**:
  - Passos são imprevisíveis
  - Ordem depende do contexto
  - Múltiplos workers podem ser necessários em ordem variável

**Diagrama**: Checklist de critérios (2 colunas)
**Animação**: Critérios aparecem um a um
**Imagem**: Checklist com checkmarks e X
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A pergunta-chave para escolher entre pipeline e supervisor: os passos são previsíveis? Se sim, pipeline. Se não, supervisor. Pipeline é determinístico e barato — você sabe exatamente quantos LLM calls vão acontecer. Supervisor é flexível mas imprevisível — pode chamar 2 workers ou 7, dependendo do raciocínio. Se custo e latência precisam ser controlados, pipeline. Se flexibilidade é mais importante, supervisor.
💡 ANALOGIA: Pipeline = receita de bolo (sempre os mesmos passos). Supervisor = cozinheiro criativo (decide os passos conforme prova). Receita é previsível e barata; cozinheiro é flexível mas imprevisível.
⚠️ ERROS COMUNS: Alunos usam supervisor "para ter flexibilidade" quando pipeline basta. Flexibilidade desnecessária = custo imprevisível. Se os passos são fixos, pipeline.
➡️ TRANSIÇÃO: "Vamos praticar."

---

### Slide 40 — Exercício: Pipeline ou Agente?

**Título**: Exercício — Pipeline ou Agente?
**Objetivo**: Praticar a escolha entre pipeline e agente orquestrador.
**Conteúdo**:
- 3 cenários:
  1. "Geração de relatório financeiro trimestral" → ?
  2. "Investigação de incidente de segurança" → ?
  3. "Processamento de pedidos de e-commerce" → ?
- Justificar em 1 frase cada

**Diagrama**: 3 cards com cenários
**Animação**: Cards aparecem um a um
**Imagem**: Cards em `etho-light`
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Para cada cenário, decidam pipeline ou agente orquestrador (supervisor). Justifiquem em 1 frase.
❓ RESPOSTAS ESPERADAS:
  1. **Pipeline** (etapas fixas: coletar dados → analisar → redigir → revisar → publicar)
  2. **Supervisor** (passos imprevisíveis: depende do incidente, pode precisar de forense, logs, entrevistas em ordem variável)
  3. **Pipeline** (processamento padronizado: validar → pagar → enviar → confirmar)
⚠️ ERROS COMUNS: Alunos votam supervisor para tudo "porque é mais flexível". Pipeline é mais barato e previsível quando os passos são fixos.
➡️ TRANSIÇÃO: "Agora as topologias assíncronas e escaláveis."

---

## SEÇÃO F — Event-Driven, Actor Model, Mesh (Slides 41-46 · 10 min)

---

### Slide 41 — [SEÇÃO] Event-Driven e Actor Model

**Título**: 5 — Event-Driven, Actor Model e Mesh: Escalabilidade Assíncrona
**Objetivo**: Transição visual para topologias assíncronas e escaláveis.
**Conteúdo**: Número "5" grande + "Event-Driven, Actor Model e Mesh"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "5" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Entramos nas topologias que escalam. Event-driven, actor model e mesh compartilham uma característica: assincronia. São topologias projetadas para sistemas distribuídos, não para uma única chamada síncrona. Event-driven é preview de ETHAGT11, onde aprofundamos.
➡️ TRANSIÇÃO: "Primeiro: event-driven."

---

### Slide 42 — Event-Driven Multi-Agente

**Título**: Event-Driven Multi-Agente
**Objetivo**: Introduzir event-driven como topologia multi-agente.
**Conteúdo**:
- Agentes reagem a eventos (não a chamadas diretas)
- **Event broker** (Kafka, Redis Streams, NATS) como barramento
- Fluxo: Agente A publica evento → Agente B consome → reage
- **Desacoplamento total**: A não sabe quem consome, B não sabe quem publicou
- **Preview**: ETHAGT11 (Event-Driven Agents em profundidade)

**Diagrama**: Event broker no centro, agentes pub/sub ao redor
**Animação**: Evento é publicado → broker distribui → agentes reagem
**Imagem**: Diagrama pub/sub com broker central
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Event-driven é a topologia dos sistemas distribuídos reais. Em vez de chamadas diretas (A chama B), agentes publicam e consomem eventos via um broker. O publicador não sabe quem vai consumir; o consumidor não sabe quem publicou. Isso dá desacoplamento total e resiliência — se um agente cai, outros continuam. É a topologia ideal para workflows longos, HITL assíncrono, e integração com sistemas externos. Aprofundamos isso em ETHAGT11.
💡 ANALOGIA: É como uma rede social. Você posta (publica evento); seus seguidores reagem (consomem). Você não sabe exatamente quem vai reagir; eles não precisam te conhecer pessoalmente. O feed é o broker.
⚠️ ERROS COMUNS: Alunos usam event-driven para tarefas síncronas simples. Event-driven adiciona complexidade (broker, serialização, idempotência). Se a tarefa é síncrona e simples, chamada direta é melhor.
➡️ TRANSIÇÃO: "A fundação teórica da escalabilidade é o actor model."

---

### Slide 43 — Actor Model: Fundação de Escalabilidade

**Título**: Actor Model — Fundação de Escalabilidade
**Objetivo**: Apresentar o actor model como fundação teórica.
**Conteúdo**:
- Cada agente = **ator** com: estado privado + mailbox + comportamento
- Atores se comunicam apenas por **mensagens assíncronas**
- Sem estado compartilhado → sem race conditions
- **Escalabilidade natural**: milhares de atores em paralelo
- **Frameworks**: Akka (JVM), Ray (Python), Microsoft AutoGen
- **Fonte**: Hewitt, 1973 (origem); AutoGen (arXiv:2308.08155)

**Diagrama**: Ator com mailbox (caixa de entrada) + mensagens assíncronas chegando
**Animação**: Mensagens chegam na mailbox → ator processa uma por vez → responde
**Imagem**: Ator como círculo com caixa de entrada
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O actor model é de 1973 (Hewitt), mas é a fundação de sistemas distribuídos modernos. Um ator tem: (1) estado privado que ninguém mais acessa; (2) uma mailbox onde recebe mensagens; (3) um comportamento que processa mensagens uma por vez. Atores se comunicam só por mensagens assíncronas — sem estado compartilhado, sem race conditions. Isso escala naturalmente: milhares de atores em paralelo, cada um isolado. Akka (JVM) e Ray (Python) são as implementações mais conhecidas. AutoGen (Microsoft, arXiv:2308.08155) usa conceitos de actor model para multi-agente.
💡 ANALOGIA: É como funcionários em cubículos. Cada um tem seu próprio espaço (estado privado), uma caixa de entrada (mailbox), e processa uma tarefa por vez. Eles se comunicam por memorandos (mensagens), nunca invadindo o cubículo um do outro. Escala porque cada cubículo é independente.
⚠️ ERROS COMUNS: Alunos acham que actor model é "muito acadêmico". É a base de Erlang (sistemas telecom de 99.9999999% uptime) e WhatsApp. Não é teoria — é prática comprovada.
➡️ TRANSIÇÃO: "A topologia mais descentralizada: mesh."

---

### Slide 44 — Agent Mesh: P2P sem Central

**Título**: Agent Mesh — P2P sem Central
**Objetivo**: Apresentar a topologia mais descentralizada.
**Conteúdo**:
- **Agent Mesh**: topologia flat peer-to-peer, sem orquestrador
- Cada agente pode falar com qualquer outro diretamente
- **Vantagem**: sem single point of failure, escalabilidade máxima
- **Desafio**: coordenação sem central → protocolos de consenso
- **Quando usar**: simulações, sistemas distribuídos, agentes autônomos
- **Quando evitar**: necessidade de controle global, consistência forte, muitos agentes (N² conexões)

**Diagrama**: Mesh de nós interconectados (grafo completo)
**Animação**: Nós aparecem e conexões surgem entre todos
**Imagem**: Grafo completo com nós interconectados
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Mesh é a topologia mais extrema de descentralização. Não há orquestrador, nem broker, nem hierarquia. Cada agente fala diretamente com qualquer outro. A vantagem: sem ponto único de falha, flexibilidade máxima. O desafio: coordenação. Sem uma autoridade central, como chegar a consenso? Precisa de protocolos distribuídos (Paxos, Raft) que são complexos. Outro problema: o número de conexões cresce quadraticamente (N²). Com 10 agentes = 100 conexões; com 100 agentes = 10.000. Mesh só funciona bem com poucos agentes altamente colaborativos.
💡 ANALOGIA: É como uma sala de aula onde todos os alunos conversam com todos diretamente. Flexible, mas caótico se forem muitos. Funciona com 5-6 pessoas; com 50 é barulheira.
⚠️ ERROS COMUNS: Alunos acham que mesh é "a topologia do futuro". Mesh é cara e complexa. Para a maioria dos casos de multi-agente LLM, swarm ou supervisor são melhores.
➡️ TRANSIÇÃO: "Vamos resgatar um padrão clássico: blackboard."

---

### Slide 45 — Blackboard: O Padrão Esquecido

**Título**: Blackboard — O Padrão Esquecido
**Objetivo**: Resgatar o padrão blackboard como topologia multi-agente.
**Conteúdo**:
- **Blackboard**: espaço compartilhado onde agentes leem e escrevem
- **Origem**: Hearsay-II (1971-1976), AI clássica
- Fluxo: Agente A escreve hipótese → Agente B lê e refina → Agente C lê e valida
- Não há orquestrador — agentes monitoram o blackboard e reagem
- **Quando usar**: problemas com múltiplas perspectivas, solução incremental
- **Conexão**: precursor do event-driven

**Diagrama**: Blackboard (quadro compartilhado) com agentes lendo/escrevendo
**Animação**: Agente escreve → outro lê e adiciona → outro valida
**Imagem**: Quadro negro compartilhado com anotações
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Blackboard é um padrão clássico de IA dos anos 70 (Hearsay-II, reconhecimento de fala). A ideia: um "quadro negro" compartilhado onde múltiplos especialistas escrevem suas contribuições. Não há orquestrador — cada agente monitora o quadro e contribui quando tem algo a acrescentar. É incremental: hipótese inicial → refinação → validação. É o precursor do event-driven — em vez de eventos efêmeros, um estado compartilhado persistente. Quando usar: problemas onde múltiplas perspectivas contribuem incrementalmente (diagnóstico médico, análise de código, planejamento estratégico).
💡 ANALOGIA: É como um mural de equipe no escritório. Cada pessoa passa, lê o que está lá, e adiciona sua contribuição. Ninguém coordena — o conhecimento emerge das contribuições.
⚠️ ERROS COMUNS: Alunos acham que blackboard é "obsoleto". É menos comum hoje, mas ainda útil para problemas onde o estado compartilhado é mais natural que eventos (diagnóstico incremental, brainstorming).
➡️ TRANSIÇÃO: "Vamos discutir mesh vs hierarchical."

---

### Slide 46 — Pergunta: Mesh vs Hierarchical?

**Título**: Pergunta — Mesh vs Hierarchical?
**Objetivo**: Discussão sobre a escolha entre descentralizado e centralizado.
**Conteúdo**:
- "Mesh é sempre a topologia mais escalável?" (V/F — justifique)
- "Em que cenário mesh é melhor que hierarchical?"
- "E se precisarmos de uma decisão global coordenada?"
- Discussão aberta (3 min)

**Diagrama**: Caixa de discussão
**Animação**: Perguntas aparecem uma a uma
**Imagem**: Caixa amarela de discussão
**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A primeira pergunta é V/F e é pegadinha. "Mesh é sempre a topologia mais escalável?" — FALSO. Mesh escala em número de agentes autônomos, mas o número de conexões cresce quadraticamente (N²). Com 100 agentes, são 10.000 conexões. Hierarchical escala melhor para muitos agentes porque a estrutura de árvore é O(N), não O(N²). Mesh é melhor quando: poucos agentes altamente colaborativos. Hierarchical é melhor quando: muitos agentes com sub-domínios distintos.
❓ DINÂMICA: Deixar 3 min. Provocar: "Se mesh fosse sempre melhor, por que empresas usam hierarquia?"
➡️ TRANSIÇÃO: "Agora as topologias estruturadas avançadas e a segunda DEMO."

---

## SEÇÃO G — Tree, Recursive + DEMO (Slides 47-52 · 10 min)

---

### Slide 47 — [SEÇÃO] Tree, Recursive, Mesh

**Título**: 6 — Tree of Agents, Recursive e DEMO
**Objetivo**: Transição visual para topologias estruturadas avançadas.
**Conteúdo**: Número "6" grande + "Tree of Agents, Recursive e DEMO"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "6" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Última seção de conteúdo antes do fechamento. Vamos cobrir tree of agents (LATS), recursive (meta-agentes), e a segunda DEMO (swarm vs supervisor).
➡️ TRANSIÇÃO: "Primeiro: tree of agents."

---

### Slide 48 — Tree of Agents (LATS)

**Título**: Tree of Agents (LATS)
**Objetivo**: Apresentar tree of agents como topologia de exploração.
**Conteúdo**:
- **LATS** (Language Agent Tree Search): árvore de possíveis ações
- Agente expande múltiplas possibilidades → avalia → seleciona melhor caminho
- Como **MCTS** (Monte Carlo Tree Search) aplicado a agentes LLM
- **Quando usar**: problemas com múltiplos caminhos de solução, needing exploration
- **Custo**: exponencial com profundidade da árvore
- **Fonte**: arXiv:2310.01757; ETHAGT04

**Diagrama**: Árvore de exploração com nós (seleção, expansão, avaliação)
**Animação**: Árvore cresce nível por nível, ramos podados
**Imagem**: Árvore de decisão com nós coloridos
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Tree of Agents é inspirado em LATS (Language Agent Tree Search). Em vez de seguir um único caminho, o agente expande múltiplas possibilidades — como um jogador de xadrez que pensa vários movimentos à frente. Para cada estado, o agente gera N ações possíveis, simula, avalia, e seleciona o melhor caminho (podando os ruins). É a aplicação de MCTS (Monte Carlo Tree Search) a agentes LLM. É poderoso para problemas difíceis com múltiplos caminhos (matemática, programação competitiva, planejamento). Mas o custo explode exponencialmente com a profundidade: árvore de profundidade 3 com branching factor 5 = 125 simulações.
💡 ANALOGIA: É como um jogador de xadrez pensando 3 movimentos à frente. Cada movimento gera múltiplas respostas possíveis. Você não joga todos — você avalia e seleciona o melhor. Mas pensar muito fundo custa tempo (e tokens).
⚠️ ERROS COMUNS: Alunos usam tree para problemas simples. Tree é para problemas onde vale a pena explorar múltiplos caminhos. Para a maioria das tarefas, single-path (ReAct) é mais barato.
➡️ TRANSIÇÃO: "Agora recursive — a topologia mais poderosa e perigosa."

---

### Slide 49 — Recursive: Meta-Agentes

**Título**: Recursive — Meta-Agentes
**Objetivo**: Apresentar recursive como topologia de meta-agentes.
**Conteúdo**:
- **Recursive**: agente que instancia sub-agentes para resolver sub-tarefas
- **Meta-agente**: "preciso de especialista em X" → cria agente X → delega
- Auto-referência: sub-agentes podem criar sub-sub-agentes
- **Preview**: ETHAGT15 (meta-agentes e auto-aprendizado em profundidade)
- **Quando usar**: problemas abertos onde o conjunto de especialistas é desconhecido

**Diagrama**: Agente recursivo (fractal/self-similar)
**Animação**: Agente cria sub-agente → sub-agente cria sub-sub-agente (fractal)
**Imagem**: Estrutura fractal auto-similar
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Recursive é a topologia mais adaptativa: o agente decide, em runtime, que especialistas ele precisa e os instancia. Um meta-agente recebe uma tarefa aberta, raciocina "preciso de um especialista em Python para esta parte", cria um sub-agente Python, delega, e integra o resultado. O sub-agente Python pode, por sua vez, decidir "preciso de um especialista em regex" e criar outro sub-agente. É meta-programação: agentes criando agentes. A profundidade é teoricamente ilimitada. ETHAGT15 aprofunda isso (meta-agentes e auto-aprendizado). Quando usar: problemas muito abertos onde o conjunto de especialistas é desconhecido a priori.
💡 ANALOGIA: É como um detetive que, durante uma investigação, descobre que precisa de um especialista em balística. Ele "contrata" (instancia) esse especialista. O especialista pode descobrir que precisa de um químico. E assim por diante. A equipe cresce organicamente conforme a necessidade.
⚠️ ERROS COMUNS: Alunos acham que recursive é "auto-organização mágica". Recursive precisa de guardrails: max_depth, validação de sub-agentes, orçamento. Sem isso, é caos.
➡️ TRANSIÇÃO: "E é por isso que recursive pode ser anti-pattern."

---

### Slide 50 — Recursive: Anti-Pattern?

**Título**: Recursive — Anti-Pattern?
**Objetivo**: Discutir quando recursive é perigoso.
**Conteúdo**:
- **Recursive é anti-pattern quando**:
  - Custo explode (cada nível = LLM calls adicionais)
  - Profundidade incontrolável (sem max_depth)
  - Sub-agentes redundantes (mesma tarefa instanciada múltiplas vezes)
  - Latência inaceitável (serialização de níveis)
- **Quando recursive NÃO é anti-pattern**:
  - Decomposição natural do problema
  - max_depth definido
  - Sub-tarefas são genuinamente distintas
- **Pergunta**: *Recursive é sempre anti-pattern? Quando não?*

**Diagrama**: Árvore recursiva crescendo infinitamente (vermelho) vs truncada com max_depth (verde)
**Animação**: Árvore cresce → trava no max_depth
**Imagem**: Comparação árvore infinita vs truncada
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Recursive é a topologia mais polarizante: poderosa quando bem usada, desastrosa quando mal usada. É anti-pattern quando: (1) custo explode — cada nível adiciona LLM calls, e sem orçamento você gasta fortunas; (2) profundidade incontrolável — sem max_depth, sub-agentes criam sub-sub-agentes indefinidamente; (3) redundância — o mesmo especialista é instanciado múltiplas vezes para a mesma tarefa; (4) latência — cada nível é serial, a latência acumula. NÃO é anti-pattern quando: o problema se decompõe naturalmente, max_depth é definido, e as sub-tarefas são genuinamente distintas. A regra: recursive precisa de guardrails desde o início.
💡 ANALOGIA: É como uma empresa que contrata consultores que contratam sub-consultores que contratam sub-sub-consultores. Sem limite, você tem uma torre de intermediários cobrando por nada. Com limite e clareza, é eficiente.
❓ PERGUNTA PARA A TURMA: "Recursive é sempre anti-pattern? Quando não?" (Resposta: não é sempre. É anti-pattern sem guardrails. Com max_depth, validação e orçamento, é adaptativo e útil.)
⚠️ ERROS COMUNS: Alunos implementam recursive sem max_depth. SEMPRE defina max_depth (ex.: 3) antes de qualquer outra coisa.
➡️ TRANSIÇÃO: "Vamos para a segunda DEMO."

---

### Slide 51 — DEMO: Swarm vs Supervisor (Lab 2)

**Título**: DEMO — Swarm vs Supervisor
**Objetivo**: Demo ao vivo — mesma tarefa em duas topologias, medir.
**Conteúdo**:
- Código do `05-Labs/ETHAGT10/Lab2-Swarm-vs-Supervisor`
- **Tarefa**: "Revisão de PR com 3 especialistas"
- **Versão 1**: Supervisor (3 workers: code, security, docs)
- **Versão 2**: Swarm (3 agentes com handoffs)
- **Medir**: latência, custo (tokens), qualidade (subjetiva)
- Mostrar trace comparativo lado a lado

**Diagrama**: 2 traces lado a lado (swarm vs supervisor) com métricas
**Animação**: Métricas aparecem (latência, custo, qualidade)
**Imagem**: Traces comparativos com barras de métricas
**Tempo**: 4 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Segunda DEMO. Mesma tarefa (revisão de PR com 3 especialistas) em duas topologias: supervisor e swarm. Vou rodar as duas e comparar as métricas. Observem: (1) latência — swarm deve ser mais rápido (sem hop de supervisor); (2) custo — swarm deve usar menos tokens (1 agente ativo por vez); (3) qualidade — supervisor deve ter vantagem se precisar síntese. A lição: as métricas confirmam (ou refutam) a teoria. Em produção, meçam sempre — não assumam.
❓ PERGUNTA PARA A TURMA (durante a demo): "Notem a diferença no número de LLM calls. Supervisor: 1 (rotear) + 3 (workers) + 1 (sintetizar) = 5 mínimo. Swarm: 1 + handoffs ≈ 3-4."
⚠️ SE A API FALHAR: Mostrar traces comparativos salvos. Dizer: "Estas são as métricas que deveríamos ver. Observem a diferença de latência e custo."
➡️ TRANSIÇÃO: "Vamos discutir os resultados."

---

### Slide 52 — Pergunta da DEMO

**Título**: Pergunta da DEMO
**Objetivo**: Engajar a turma com análise dos resultados da demo.
**Conteúdo**:
- "Qual topologia teve menor latência? Por quê?"
- "Qual teve menor custo? E melhor qualidade?"
- "Em que cenário você inverteria a escolha?"
- Discussão em duplas (2 min)

**Diagrama**: Caixa de discussão
**Animação**: Perguntas aparecem uma a uma
**Imagem**: Caixa amarela de discussão
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vamos discutir os resultados da DEMO. As perguntas são projetadas para conectar métricas com decisão: latência, custo, qualidade. A terceira pergunta é a mais importante: "em que cenário você inverteria a escolha?" — mostra que a topologia não é fixa, depende do requisito.
❓ RESPOSTAS ESPERADAS:
  1. Swarm teve menor latência (sem hop de supervisor)
  2. Swarm menor custo; supervisor melhor qualidade (se síntese foi boa)
  3. Inverteria se: precisa síntese (swarm → supervisor) ou se latência deixa de importar (swarm → supervisor para ter consistência)
➡️ TRANSIÇÃO: "Última seção: a decisão arquitetural."

---

## SEÇÃO H — Escolha, ADR e Fechamento (Slides 53-62 · 15 min)

---

### Slide 53 — [SEÇÃO] Escolha e ADR

**Título**: 7 — Escolha de Topologia e ADR
**Objetivo**: Transição visual para a decisão arquitetural justificada.
**Conteúdo**: Número "7" grande + "Escolha de Topologia e ADR"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "7" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Chegamos ao clímax da aula: como decidir. Vamos ver a matriz de decisão, o ADR de topologia, sinais de evolução, e um exercício prático. O objetivo: vocês saírem capazes de justificar uma escolha de topologia com evidência.
➡️ TRANSIÇÃO: "Primeiro: a matriz de decisão."

---

### Slide 54 — Matriz de Decisão

**Título**: Matriz de Decisão
**Objetivo**: Apresentar a matriz de decisão para escolha de topologia.
**Conteúdo**:
- **4 eixos**: consistência × latência × custo × flexibilidade
- Para cada topologia, avaliar nos 4 eixos (high/medium/low):
  - **Supervisor**: alta consistência, latência média, custo médio, flexibilidade baixa
  - **Swarm**: consistência baixa, latência baixa, custo baixo, flexibilidade alta
  - **Pipeline**: alta consistência, latência alta (serial), custo baixo, flexibilidade baixa
  - **Mesh**: consistência baixa, latência baixa, custo médio, flexibilidade máxima
  - **Hierarchical**: alta consistência, latência alta, custo alto, flexibilidade média
  - **Hybrid**: balanceado (depende da composição)

**Diagrama**: `12-Diagrams/ETHAGT10/decision-matrix.mmd`
**Animação**: Topologias aparecem na matriz uma a uma
**Imagem**: Matriz colorida com topologias posicionadas
**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esta matriz é a ferramenta mais prática da aula. 4 eixos: consistência (a saída é confiável e coordenada?), latência (quanto tempo até resposta?), custo (quantos tokens/LLM calls?), flexibilidade (dá para adaptar a contextos variados?). Para cada topologia, avalie nos 4 eixos. Supervisor ganha em consistência, perde em flexibilidade. Swarm ganha em latência e custo, perde em consistência. Pipeline ganha em previsibilidade, perde em flexibilidade. A escolha é um trade-off: qual eixo é mais importante para o seu caso?
💡 ANALOGIA: É como escolher um carro. Eixos: potência × economia × espaço × preço. Esportiva: muita potência, pouca economia. SUV: muito espaço, preço alto. Hatch: equilibrado. Qual é o melhor? Depende do que você precisa. Topologia é igual.
⚠️ ERROS COMUNS: Alunos tentam otimizar todos os eixos. Impossível — trade-offs são intrínsecos. Escolha qual eixo sacrificar.
➡️ TRANSIÇÃO: "A decisão precisa ser documentada. ADR."

---

### Slide 55 — ADR de Topologia

**Título**: ADR de Topologia
**Objetivo**: Apresentar a estrutura de um ADR para decisão de topologia.
**Conteúdo**:
- **ADR** (Architecture Decision Record) para topologia multi-agente
- **Estrutura**:
  1. **Contexto**: problema, requisitos, restrições
  2. **Decision**: topologia escolhida + justificativa
  3. **Consequências**: trade-offs aceitos, riscos, sinais de evolução
- **Exemplo**: "Revisão de PR → Supervisor (síntese necessária, 3 especialistas, baixa latência não crítica)"
- **Template**: `08-ADRs/ETHAGT10/`

**Diagrama**: Template de ADR (3 seções: Contexto, Decision, Consequências)
**Animação**: Seções aparecem uma a uma
**Imagem**: Documento ADR com 3 seções destacadas
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: ADR — Architecture Decision Record — é a prática de documentar decisões arquiteturais. Para topologia multi-agente, o ADR tem 3 seções: (1) Contexto — qual problema, quais requisitos (latência, custo, consistência), quais restrições; (2) Decision — qual topologia e por quê, conectando aos requisitos; (3) Consequências — quais trade-offs foram aceitos, quais riscos, e quais sinais indicarão que a topologia precisa evoluir. O ADR não é burocracia — é a defesa da sua decisão. Sem ADR, "vamos de supervisor" é uma opinião. Com ADR, é uma decisão justificada.
💡 ANALOGIA: É como o prontuário médico. O médico não prescreve "por experiência" — ele documenta: sintomas (contexto), diagnóstico e tratamento (decision), efeitos colaterais esperados (consequências). ADR é o prontuário da arquitetura.
⚠️ ERROS COMUNS: Alunos escrevem ADR depois da decisão, como justificativa. ADR deve ser escrito DURANTE a decisão — orienta o raciocínio.
➡️ TRANSIÇÃO: "Como saber quando mudar de topologia?"

---

### Slide 56 — Sinais de Evolução

**Título**: Sinais de Evolução
**Objetivo**: Identificar quando a topologia precisa mudar.
**Conteúdo**:
- **Supervisor precisa evoluir quando**:
  - Latência crescente (supervisor gargalo)
  - Workers > 7 (limite cognitivo)
  - Necessidade de paralelismo (supervisor serializa)
- **Swarm precisa evoluir quando**:
  - Necessidade de síntese global
  - Loops de handoff
  - Estado compartilhado crescendo
- **Pipeline precisa evoluir quando**:
  - Passos imprevisíveis
  - Necessidade de decisão dinâmica
- **Regra**: monitore métricas, não intuição

**Diagrama**: Checklist de sinais por topologia
**Animação**: Sinais aparecem agrupados por topologia
**Imagem**: Semáforo com sinais de alerta
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Nenhuma topologia é definitiva. Sistemas evoluem, requisitos mudam, escala cresce. Os sinais de evolução são métricas observáveis: latência crescente, custo crescendo, workers demais, loops, estado crescendo. A regra de ouro: monitore métricas, não intuição. "Acho que está lento" não conta. "P95 de latência subiu de 5s para 15s nos últimos 30 dias" conta. Quando um sinal dispara, é hora de avaliar mudança de topologia — e escrever um novo ADR.
💡 ANALOGIA: É como o painel do carro. Você não troca de carro "por intuição". Você troca quando os sinais aparecem: consumo subindo, manutenção frequente, espaço insuficiente. Topologia é igual — mude quando as métricas indicam.
⚠️ ERROS COMUNS: Alunos trocam de topologia "por moda" (ex.: ouviram que swarm é melhor). Mude com base em métricas, não hype.
➡️ TRANSIÇÃO: "Vamos ver tudo isso em um caso de estudo: MetaGPT."

---

### Slide 57 — Caso de Estudo: MetaGPT Software House

**Título**: Caso de Estudo — MetaGPT Software House
**Objetivo**: Mostrar todos os conceitos em um caso real.
**Conteúdo**:
- **MetaGPT** simula uma software house completa
- **Papéis**: Product Manager → Architect → Engineer → QA → Tester
- **Topologia**: hierarchical com SOPs codificando o fluxo
- **Entrada**: "Build a 2048 game" → **Saída**: código + testes + docs
- **Resultado**: código funcional em minutos, não dias
- **Lição**: a topologia reflete a estrutura organizacional humana
- **Fonte**: arXiv:2308.00352

**Diagrama**: Hierarquia MetaGPT com fluxo de artefatos (PRD → design → code → tests)
**Animação**: Fluxo de artefatos animado (PRD → design doc → código → testes)
**Imagem**: Fluxograma MetaGPT completo
**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: MetaGPT é o caso de estudo perfeito porque aplica todos os conceitos da aula. A topologia é hierarchical (papéis em hierarquia) com elementos de pipeline (artefatos fluem: PRD → design → código → testes) e elementos de supervisor (cada papel orquestra suas sub-tarefas). A entrada é uma descrição em linguagem natural ("Build a 2048 game"). A saída é código funcional + testes + documentação. O resultado: em minutos, não dias. A lição fundamental: a topologia multi-agente reflete a estrutura organizacional humana. MetaGPT funciona porque codifica as SOPs de uma software house real. Você não inventa a topologia — você a espelha da organização que está simulando.
💡 ANALOGIA: É como simular uma empresa inteira em software. Cada agente é um funcionário. As SOPs são os processos da empresa. O resultado é o produto. MetaGPT mostra que multi-agente é mais poderoso quando reflete estruturas humanas provadas.
⚠️ ERROS COMUNS: Alunos acham que MetaGPT é "mágica". Não é — são SOPs bem definidas + papéis claros + topologia adequada. Sem SOPs, a mesma topologia produz caos.
➡️ TRANSIÇÃO: "Vamos praticar a decisão completa."

---

### Slide 58 — Exercício: 6 Cenários + ADR

**Título**: Exercício — 6 Cenários + ADR
**Objetivo**: Praticar a escolha de topologia com justificativa em ADR.
**Conteúdo**:
- 6 cenários:
  1. "Chatbot de suporte com escalonamento humano"
  2. "Sistema de revisão de código com 3 especialistas"
  3. "Pipeline de geração de relatório financeiro"
  4. "Simulação de mercado com múltiplos agentes"
  5. "Assistente pessoal multi-função"
  6. "Sistema de pesquisa autônoma com exploração"
- Em grupos: propor topologia + escrever esqueleto de ADR (contexto, decisão, consequências)
- 3 min discussão, 2 min compartilhar

**Diagrama**: 6 cards com cenários + template ADR
**Animação**: Cards aparecem + template ADR ao lado
**Imagem**: Cards + documento ADR em branco
**Tempo**: 4 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Último exercício e o mais completo. Em grupos, para cada cenário: (1) propor a topologia, (2) escrever o esqueleto de ADR (Contexto, Decision, Consequências). 3 minutos para discussão, 2 para compartilhar. Este exercício consolida tudo: vocês estão tomando a decisão e documentando — exatamente como farão em produção.
❓ RESPOSTAS DE REFERÊNCIA:
  1. Supervisor (escalonamento = roteamento central; síntese do histórico)
  2. Supervisor ou Swarm (supervisor se precisa síntese; swarm se independentes)
  3. Pipeline (etapas fixas e predefinidas)
  4. Actor Model / Mesh (agentes autônomos em paralelo, sem central)
  5. Swarm (multi-função com handoffs naturais)
  6. Tree (exploração de múltiplos caminhos) ou Recursive (se especialistas são desconhecidos)
⚠️ ERROS COMUNS: Grupos escrevem ADR genérico ("escolhemos supervisor porque é bom"). ADR específico: "escolhemos supervisor porque a síntese de 3 revisões é requisito, latência <30s é aceitável, e custo de 5 LLM calls é within budget."
➡️ TRANSIÇÃO: "Vamos resumir a aula."

---

### Slide 59 — Resumo da Aula + Checklist

**Título**: Resumo da Aula + Checklist
**Objetivo**: Sintetizar os pontos-chave e confirmar cobertura.
**Conteúdo**:
- **12 topologias** catalogadas (centralizadas, fluxo, descentralizadas, estruturadas, reativas)
- **Supervisor** = roteador com tool calls; **Hierarchical** = árvore de supervisores
- **Swarm** = handoffs sem central; **Pipeline** = sequência controlada
- **Actor Model** = mensagens assíncronas; **Mesh** = P2P flat
- **Tree** = exploração; **Recursive** = meta-agentes (cuidado com custo)
- **Escolha via matriz** (consistência × latência × custo × flexibilidade) + **ADR**
- **Sinais de evolução**: monitore métricas, não intuição
- **Checklist**:
  - [ ] Catalogou as 12 topologias
  - [ ] Implementou supervisor + hierarchical
  - [ ] Comparou swarm vs supervisor
  - [ ] Escreveu ADR de topologia
  - [ ] Identificou sinais de evolução

**Diagrama**: 7 ícones com pontos-chave + checklist
**Animação**: Pontos aparecem + checklist marca item por item
**Imagem**: Resumo visual com ícones
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Recapitulando: vimos 12 topologias agrupadas em 5 categorias. Aprendemos supervisor e hierarchical em detalhe, swarm com handoffs, pipeline e orchestrator-workers, event-driven e actor model, mesh e blackboard, tree e recursive. Vimos que a escolha é um trade-off quantificável na matriz de decisão. E que toda decisão precisa de ADR. Sistemas evoluem com base em métricas, não intuição.
➡️ TRANSIÇÃO: "Vamos verificar a compreensão com um quiz rápido."

---

### Slide 60 — Quiz: 3 Perguntas Rápidas

**Título**: Quiz — 3 Perguntas
**Objetivo**: Verificar compreensão rápida.
**Conteúdo**:
- **P1**: "Qual topologia NÃO tem orquestrador central?"
  - A) Supervisor · B) Hierarchical · C) Swarm · D) Pipeline
  - **Resposta**: C
- **P2**: "Em LangGraph, o supervisor roteia para workers via:"
  - A) Mensagens de evento · B) Tool calls · C) Handoffs · D) Mailbox
  - **Resposta**: B
- **P3**: "Recursive é anti-pattern quando:"
  - A) O problema se decompõe naturalmente
  - B) max_depth não está definido
  - C) Sub-tarefas são distintas
  - D) A profundidade é 1
  - **Resposta**: B

**Diagrama**: 3 perguntas com opções
**Animação**: Perguntas aparecem uma a uma (on click para revelar resposta)
**Imagem**: Cards de quiz
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Quiz rápido, 3 perguntas, individual. Sem consulta. Se acertaram 2+, compreensão básica atingida.
❓ REVISÃO RÁPIDA:
  - P1: Swarm não tem orquestrador (handoffs descentralizados). Supervisor, hierarchical e pipeline têm controle central.
  - P2: Em LangGraph, cada worker é uma tool no supervisor. O supervisor é um ReAct com bind_tools.
  - P3: Recursive sem max_depth = profundidade incontrolável = anti-pattern. Com max_depth e sub-tarefas distintas, é adaptativo.
➡️ TRANSIÇÃO: "Vamos conectar com os próximos módulos."

---

### Slide 61 — Conexão com Próximos Módulos + Referências

**Título**: Conexão com Próximos Módulos + Referências
**Objetivo**: Mostrar conexões e indicar leitura.
**Conteúdo**:
- **Conexões**:
  - ETHAGT11 — Event-Driven Agents (event-driven em profundidade)
  - ETHAGT14 — Escalabilidade (topologias em produção)
  - ETHAGT15 — Meta-Agentes (recursive e auto-aprendizado)
  - ETHAGT90 — Capstone (projeto final)
- **Leitura obrigatória**:
  - Hong, S. et al. *MetaGPT* (arXiv:2308.00352)
  - LangGraph *Multi-Agent* examples (`hierarchical_agent_teams`)
  - OpenAI Swarm (repo, 2024)
- **Leitura recomendada**:
  - Chen, W. et al. *AgentVerse* (arXiv:2308.10848)
  - Microsoft AutoGen docs (arXiv:2308.08155)
- **Próximos passos**:
  1. Ler: MetaGPT paper
  2. Rodar: Lab 1 (Hierarchical Teams)
  3. Iniciar: Lab 2 (Swarm vs Supervisor)
  4. Próxima aula: ETHAGT11 — Event-Driven Agents

**Diagrama**: Mapa da especialização com ETHAGT10 no centro + lista de referências
**Animação**: Conexões aparecem uma a uma
**Imagem**: Mind map com ETHAGT10 conectando a ETHAGT11, 14, 15, 90
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: ETHAGT10 é o hub dos sistemas multi-agente. ETHAGT11 aprofunda event-driven. ETHAGT14 cobre escalabilidade em produção (topologias sob carga). ETHAGT15 aprofunda meta-agentes (recursive). ETHAGT90 é o capstone onde vocês aplicam tudo. Para a leitura: MetaGPT é obrigatório — é o paper que inspirou esta aula. LangGraph examples são a implementação de referência. AgentVerse e AutoGen são complementares valiosos.
➡️ TRANSIÇÃO: "Perguntas?"

---

### Slide 62 — Q&A / Encerramento

**Título**: Q&A / Encerramento
**Objetivo**: Abrir para perguntas e encerrar.
**Conteúdo**:
- "Perguntas?"
- Contato do professor
- "Na próxima aula: ETHAGT11 — Event-Driven Agents"
- Lembrete: entregar Lab 1 antes da próxima aula

**Diagrama**: Logo Etho + fundo `etho-dark`
**Animação**: Fade in
**Imagem**: Logo Etho centralizado em fundo escuro
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Hora de Q&A. Se não houver perguntas, fazer a pergunta inversa: "Qual topologia vocês usariam no projeto de vocês hoje, e por quê?" Lembrem: Lab 1 (Hierarchical Teams) deve ser entregue antes da próxima aula. Na próxima: ETHAGT11 — Event-Driven Agents, onde aprofundamos a topologia assíncrona que vimos rapidamente hoje.
❓ SE NÃO HOUVER PERGUNTAS: "Pensem no sistema de vocês. Qual topologia ele usa hoje? Qual deveria usar? A resposta é a mesma?"
➡️ ENCERRAMENTO: "Obrigado. Na próxima aula, event-driven em profundidade."

---

## Resumo de Cobertura

| Objetivo | Slides | Coberto em |
|---|---|---|
| Caracterizar 12 topologias | 7-16 | Catálogo + exercício de matching |
| Justificar escolha via ADR | 53-58 | Matriz + ADR + exercício 6 cenários |
| Implementar topologias | 24, 51 | DEMOs (hierarchical + swarm vs supervisor) |
| Medir trade-offs | 51-52 | DEMO swarm vs supervisor com métricas |
| Identificar sinais de evolução | 56 | Sinais de evolução por topologia |

---

*(Fim da Parte 2 — fim dos slides detalhados)*
