# ETHAGT10 — Padrões de Arquitetura Multi-Agente (topologias)
## Storyboard da Apresentação

> **Universidade Etho · Especialização em Programação Agêntica**
> Fase C — Sistemas Multi-Agente · 30 h
> Storyboard v1.0 · Julho 2026

---

## Metadados da Apresentação

| Campo | Valor |
|---|---|
| Código | ETHAGT10 |
| Título | Padrões de Arquitetura Multi-Agente (topologias) |
| Duração estimada | 90 min (2 blocos de 45 min) |
| Total de slides | 62 |
| Público | Arquitetos, Engenheiros de Software, Engenheiros de IA, Tech Leads, Arquitetos de Solução |
| Pré-requisitos | ETHAGT09, ETHAGT03, Python Intermediário, LangGraph |
| Competências | C1 (A), C2 (A), C3 (B), C4 (B), C6 (B) |

---

## Mapa Visual da Apresentação

```
BLOCO 1 (45 min)                              BLOCO 2 (45 min)
┌──────────────────────────────┐              ┌──────────────────────────────┐
│ SEÇÃO A — Abertura (8 min)   │              │ SEÇÃO E — Pipeline (10 min) │
│  Capa · Objetivos · Agenda   │              │  Pipeline fixo vs dinâmico   │
│  Motivação · Contexto        │              │  Orchestrator-Workers        │
├──────────────────────────────┤              │  Composição hierarchical     │
│ SEÇÃO B — Catálogo (12 min)  │              ├──────────────────────────────┤
│  12 topologias em grid       │              │ SEÇÃO F — Event/Actor (10 m) │
│  Espectro centralizado↔desc. │              │  Event-driven · Actor model  │
│  Exercício de matching       │              │  Mesh · Blackboard           │
├──────────────────────────────┤              ├──────────────────────────────┤
│ SEÇÃO C — Supervisor (15 min)│              │ SEÇÃO G — Tree/Rec (10 min)  │
│  Supervisor pattern          │              │  Tree of Agents (LATS)       │
│  Hierarchical · MetaGPT      │              │  Recursive · Anti-pattern?   │
│  Crew formation · DEMO       │              │  DEMO: Swarm vs Supervisor   │
├──────────────────────────────┤              ├──────────────────────────────┤
│ SEÇÃO D — Swarm (10 min)     │              │ SEÇÃO H — Fechamento (15 min)│
│  OpenAI Swarm · Handoffs     │              │  Matriz · ADR · Sinais       │
│  Swarm vs Supervisor         │              │  MetaGPT · Exercício 6 cen.  │
│  Limites · Pergunta          │              │  Resumo · Quiz · Refs · Q&A  │
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
  - ETHAGT10 — Padrões de Arquitetura Multi-Agente (topologias)
  - Universidade Etho · Especialização em Programação Agêntica
  - Fase C — Sistemas Multi-Agente
  - Professor · Data
- **Diagrama**: Logo Etho + imagem de fundo abstrata (rede de nós/topologias)
- **Animação**: Fade in do título
- **Tempo**: 1 min

---

#### Slide 2 — Objetivos do Módulo
- **Tipo**: Conteúdo
- **Objetivo**: Deixar claro o que o aluno deve conseguir fazer ao final
- **Conteúdo**:
  - Objetivo geral: Dominar as topologias multi-agente — quando usar, trade-offs, e como escolher
  - 5 objetivos específicos:
    1. Caracterizar 12 topologias (when-to-use, when-to-avoid)
    2. Justificar a escolha via ADR
    3. Implementar ao menos 4 topologias em um mesmo domínio
    4. Medir trade-offs (custo, latência, qualidade)
    5. Identificar sinais de que a topologia precisa evoluir
  - Foco: decisão arquitetural justificada, não "vamos de supervisor"
- **Diagrama**: Ícones representando cada objetivo
- **Animação**: Aparecer objetivos um a um (on click)
- **Tempo**: 2 min

---

#### Slide 3 — Competências Desenvolvidas
- **Tipo**: Conteúdo
- **Objetivo**: Conectar a aula ao Framework Etho de competências
- **Conteúdo**:
  - Tabela: 5 competências com nível B/I/A
  - C1 Programação Agêntica → **A**
  - C2 Multi-Agent Systems → **A**
  - C3 MCP & Tool Use → B
  - C4 Agent Memory → B
  - C6 Agent Security → B
  - Badge visual por competência
- **Diagrama**: Radar chart dos 5 pilares
- **Animação**: Radar aparece com wipe
- **Tempo**: 1 min

---

#### Slide 4 — Agenda
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar o roteiro da aula com tempos
- **Conteúdo**:
  - Bloco 1: Abertura → Catálogo 12 topologias → Supervisor/Hierarchical → Swarm
  - Bloco 2: Pipeline → Event-Driven/Actor → Tree/Recursive → Escolha/ADR → Fechamento
  - Tempos estimados por seção
- **Diagrama**: Timeline horizontal com 8 seções
- **Animação**: Timeline cresce da esquerda para direita
- **Tempo**: 1 min

---

#### Slide 5 — Motivação: O Problema da Topologia Padrão
- **Tipo**: Conteúdo
- **Objetivo**: Criar tensão — times escolhem topologia sem critério
- **Conteúdo**:
  - "Vamos de supervisor" — a decisão default sem justificativa
  - Exemplo: sistema de revisão de PR com 3 especialistas (code, security, docs)
  - Supervisor funciona, mas swarm talvez seja mais simples e barato
  - Custo de escolher errado: gargalo de latência, custo excessivo, complexidade desnecessária
  - Pergunta: *Qual foi a topologia mais comum que vocês já usaram em projetos?*
- **Diagrama**: Imagem "supervisor gargalo" → vs → "swarm fluido"
- **Animação**: Split — lado esquerdo (gargalo), depois lado direito (swarm)
- **Tempo**: 2 min

---

#### Slide 6 — Contexto: Do Single Agent ao Multi-Agente
- **Tipo**: Conteúdo
- **Objetivo**: Explicar a evolução que tornou multi-agente viável
- **Conteúdo**:
  - Linha do tempo: 2023 (ReAct) → 2023 (AutoGen, arXiv:2308.08155) → 2023 (MetaGPT, arXiv:2308.00352) → 2023 (AgentVerse, arXiv:2308.10848) → 2024 (OpenAI Swarm, CrewAI, LangGraph multi-agent)
  - Confluência: reasoning + tool calling + frameworks multi-agente + custo reduzido
  - MetaGPT como marco: SOPs (Standard Operating Procedures) aplicadas a agentes
  - A pergunta deixou de ser "se" multi-agente, mas "qual topologia"
- **Diagrama**: Timeline horizontal com marcos
- **Animação**: Marcos aparecem sequencialmente
- **Tempo**: 1 min

---

### SEÇÃO B — Catálogo das 12 Topologias (Slides 7-16 · 12 min)

---

#### Slide 7 — [SEÇÃO] Catálogo das 12 Topologias
- **Tipo**: Seção
- **Objetivo**: Transição para o panorama das topologias
- **Conteúdo**: Número "1" grande + "Catálogo das 12 Topologias"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 8 — As 12 Topologias (Grid Panorâmico)
- **Tipo**: Diagrama
- **Objetivo**: Visão geral de todas as 12 topologias em um só slide
- **Conteúdo**:
  - Grid 4×3 com mini-diagrama de cada topologia:
    1. Single Agent · 2. Supervisor · 3. Hierarchical · 4. Blackboard
    5. Actor Model · 6. Pipeline · 7. Event-Driven · 8. Swarm
    9. Tree of Agents · 10. Recursive · 11. Agent Mesh · 12. Hybrid
  - Para cada: nome + 1 linha de descrição
  - Fonte: `10-Architecture/` + arXiv:2601.12560
- **Diagrama**: Grid 4×3 de mini-diagramas
- **Animação**: Cada topologia aparece com click (grupo de 4)
- **Tempo**: 3 min

---

#### Slide 9 — O Espectro: Centralizado ↔ Descentralizado
- **Tipo**: Diagrama
- **Objetivo**: Dar um eixo de comparação antes de detalhar cada topologia
- **Conteúdo**:
  - Eixo horizontal: Centralizado ←→ Descentralizado
  - Centralizado: Supervisor, Hierarchical, Pipeline, Orchestrator-Workers
  - Intermediário: Blackboard, Event-Driven
  - Descentralizado: Swarm, Mesh, Actor Model
  - Estruturado: Tree, Recursive (ortogonal ao eixo)
  - Trade-off: controle × flexibilidade
- **Diagrama**: Linha horizontal com topologias posicionadas
- **Animação**: Topologias aparecem no eixo gradualmente
- **Tempo**: 2 min

---

#### Slide 10 — Topologias Centralizadas: Supervisor e Hierarchical
- **Tipo**: Comparação
- **Objetivo**: Apresentar as topologias de controle central
- **Conteúdo**:
  - Supervisor: 1 roteador (LLM) + N workers (tools) — LangGraph
  - Hierarchical: árvore de supervisores → workers → sub-workers
  - When-to-use: tarefas decomponíveis, necessidade de controle
  - When-to-avoid: baixa latência, tarefas imprevisíveis
  - Pergunta: *Já usou supervisor em produção? Funcionou?*
- **Diagrama**: 2 mini-diagramas lado a lado
- **Animação**: Colunas aparecem uma a uma
- **Tempo**: 2 min

---

#### Slide 11 — Topologias de Fluxo: Pipeline e Orchestrator-Workers
- **Tipo**: Comparação
- **Objetivo**: Apresentar as topologias de fluxo controlado
- **Conteúdo**:
  - Pipeline: sequência fixa de agentes (A → B → C)
  - Pipeline dinâmico: próximo step decidido em runtime
  - Orchestrator-Workers: orchestrator delega para workers dinamicamente
  - When-to-use: passos predefinidos, previsibilidade
  - When-to-avoid: flexibilidade alta necessária
  - Aprofundamento: ETHAGT03 (5 workflows canônicos)
- **Diagrama**: 2 mini-diagramas lado a lado
- **Tempo**: 1.5 min

---

#### Slide 12 — Topologias Descentralizadas: Swarm, Mesh, Actor Model
- **Tipo**: Comparação
- **Objetivo**: Apresentar as topologias sem controle central
- **Conteúdo**:
  - Swarm: agentes leves com transfer() de controle (OpenAI)
  - Agent Mesh: topologia flat peer-to-peer, sem orquestrador
  - Actor Model: cada agente = ator com mailbox, mensagem assíncrona
  - When-to-use: flexibilidade, escalabilidade, sem gargalo central
  - When-to-avoid: consistência forte, coordenação complexa
- **Diagrama**: 3 mini-diagramas lado a lado
- **Tempo**: 1.5 min

---

#### Slide 13 — Topologias Estruturadas: Tree e Recursive
- **Tipo**: Comparação
- **Objetivo**: Apresentar as topologias de estrutura recursiva
- **Conteúdo**:
  - Tree of Agents: árvore de exploração (LATS — Language Agent Tree Search)
  - Recursive: meta-agentes que instanciam sub-agentes dinamicamente
  - When-to-use: exploração de soluções, decomposição recursiva
  - When-to-avoid: custo explode, profundidade incontrolável
  - Preview: ETHAGT15 (meta-agentes em profundidade)
- **Diagrama**: 2 mini-diagramas lado a lado
- **Tempo**: 1.5 min

---

#### Slide 14 — Topologias Reativas e Híbridas: Event-Driven, Blackboard, Hybrid
- **Tipo**: Comparação
- **Objetivo**: Apresentar as topologias reativas e combinatórias
- **Conteúdo**:
  - Event-Driven: agentes reagem a eventos (preview ETHAGT11)
  - Blackboard: espaço compartilhado onde agentes leem/escrevem
  - Hybrid: combinação de topologias (ex.: supervisor + swarm)
  - When-to-use: assincronia, desacoplamento, mundo real
  - When-to-avoid: simplicidade (over-engineering)
- **Diagrama**: 3 mini-diagramas lado a lado
- **Tempo**: 1.5 min

---

#### Slide 15 — Single Agent: O Baseline Esquecido
- **Tipo**: Conteúdo
- **Objetivo**: Lembrar que single agent é uma topologia válida
- **Conteúdo**:
  - Single Agent = 1 agente com N tools (não é multi-agente, mas é o baseline)
  - Quando NÃO ir para multi-agente:
    - Tarefa não se decompõe naturalmente
    - Latência não é problema
    - Custo precisa ser mínimo
  - Regra: comece com single agent, só suba para multi-agente com evidência
  - Conexão: ETHAGT01 (escalada de complexidade)
- **Diagrama**: Single agent com N tools (estrela)
- **Tempo**: 1 min

---

#### Slide 16 — Exercício Rápido: Matching Cenário → Topologia
- **Tipo**: Exercício
- **Objetivo**: Praticar a associação antes de aprofundar
- **Conteúdo**:
  - 6 cenários curtos:
    1. "Chatbot de suporte com escalonamento" → Supervisor
    2. "Revisão de PR com 3 especialistas" → Supervisor ou Swarm
    3. "Relatório financeiro em etapas" → Pipeline
    4. "Simulação de mercado" → Actor Model / Mesh
    5. "Assistente pessoal multi-função" → Swarm
    6. "Pesquisa autônoma com exploração" → Tree
  - Votação rápida (mãos levantadas)
- **Diagrama**: 6 cards com cenários
- **Tempo**: 2 min

---

### SEÇÃO C — Supervisor e Hierarchical (Slides 17-28 · 15 min)

---

#### Slide 17 — [SEÇÃO] Supervisor e Hierarchical
- **Tipo**: Seção
- **Objetivo**: Transição para a topologia mais comum em produção
- **Conteúdo**: "2 — Supervisor e Hierarchical: A Topologia Default"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 18 — Supervisor Pattern: O Roteador
- **Tipo**: Diagrama
- **Objetivo**: Apresentar o supervisor como padrão fundamental
- **Conteúdo**:
  - Supervisor = LLM que roteia tarefas para workers
  - Workers são especializados (pesquisa, escrita, análise, etc.)
  - Supervisor decide: qual worker chamar, em que ordem, quando sintetizar
  - Analogia: supervisor = tech lead, workers = desenvolvedores
  - Fonte: LangGraph multi-agent-collaboration
- **Diagrama**: `12-Diagrams/ETHAGT10/supervisor-topology.mmd`
- **Animação**: Supervisor aparece, depois workers surgem como tools
- **Tempo**: 2 min

---

#### Slide 19 — Supervisor como Tool Calls (LangGraph)
- **Tipo**: Código
- **Objetivo**: Mostrar a implementação canônica em LangGraph
- **Conteúdo**:
  - Cada worker = uma tool no supervisor
  - Supervisor LLM com `bind_tools([worker_a, worker_b, ...])`
  - Supervisor decide tool_call → worker executa → resultado volta
  - Snippet: `create_supervisor(model, workers=[researcher, writer])`
  - O supervisor é um agente ReAct onde as "tools" são outros agentes
- **Diagrama**: `12-Diagrams/ETHAGT10/supervisor-topology.mmd` (com tool calls)
- **Animação**: Fluxo step-by-step: supervisor → tool_call → worker → return
- **Tempo**: 3 min

---

#### Slide 20 — Hierarchical: Árvore de Supervisores
- **Tipo**: Diagrama
- **Objetivo**: Apresentar a generalização do supervisor para múltiplos níveis
- **Conteúdo**:
  - Hierarchical = supervisor de supervisores
  - Top supervisor → sub-supervisores → workers → sub-workers
  - Cada nível delega para o nível abaixo
  - Caso: "revisão de PR" → top supervisor → (code reviewer sup, security sup, docs sup) → workers
  - Fonte: LangGraph `hierarchical_agent_teams`
- **Diagrama**: `12-Diagrams/ETHAGT10/hierarchical-topology.mmd`
- **Animação**: Árvore cresce de cima para baixo
- **Tempo**: 2 min

---

#### Slide 21 — Quando Escalar Hierarquia: 3 Níveis vs Flat
- **Tipo**: Comparação
- **Objetivo**: Dar critério para decidir profundidade da hierarquia
- **Conteúdo**:
  - Flat (1 nível): supervisor + workers — simples, baixa latência
  - 2 níveis: top supervisor + sub-supervisores + workers — domínios distintos
  - 3 níveis: raramente necessário — custo e latência explodem
  - Critério: escalar quando workers de um supervisor > 5-7 (limite cognitivo)
  - Regra: prefira flat; só adicione nível com evidência de que flat é insuficiente
- **Diagrama**: 3 árvores lado a lado (1, 2, 3 níveis)
- **Tempo**: 2 min

---

#### Slide 22 — Casos de Falha: Supervisor Gargalo
- **Tipo**: Conteúdo
- **Objetivo**: Ser honesto sobre os modos de falha do supervisor
- **Conteúdo**:
  - Supervisor vira bottleneck: todas as requisições passam por ele
  - Latência cumulativa: supervisor serializa todas as chamadas
  - Custo: supervisor faz LLM call a cada roteamento
  - Single point of failure: se supervisor alucina, sistema inteiro falha
  - Sinal de alerta: latência > 30s para tarefas simples
- **Diagrama**: Diagrama com "funil" no supervisor (gargalo)
- **Tempo**: 1.5 min

---

#### Slide 23 — Casos de Falha: Workers Redundantes
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar o anti-pattern de overlap de responsabilidades
- **Conteúdo**:
  - Workers com responsabilidades sobrepostas → supervisor não sabe qual escolher
  - Resultado: roteamento errado, retrabalho, custo duplicado
  - Solução: responsabilidade exclusiva por worker (SRP — Single Responsibility)
  - Sinal: supervisor chama 2+ workers para a mesma sub-tarefa
- **Diagrama**: Diagrama de Venn mostrando overlap
- **Tempo**: 1 min

---

#### Slide 24 — DEMO: Hierarchical Teams (Code Walkthrough)
- **Tipo**: Código
- **Objetivo**: Demo ao vivo — supervisor + 2 workers + sub-worker
- **Conteúdo**:
  - Código do `05-Labs/ETHAGT10/Lab1-Hierarchical-Teams`
  - Topologia: supervisor → (researcher, writer) → writer → formatter (sub-worker)
  - Tarefa: "Escreva um resumo sobre tópico X"
  - Fluxo: supervisor delega → researcher pesquisa → writer escreve → writer delega formatação → formatter formata → supervisor sintetiza
  - Mostrar trace mostrando cada nível da hierarquia
- **Diagrama**: Code block + trace side-by-side
- **Animação**: Highlight de linhas chave + trace aparece nível por nível
- **Tempo**: 4 min

---

#### Slide 25 — Pergunta da DEMO
- **Tipo**: Exercício
- **Objetivo**: Engajar a turma com uma pergunta sobre a demo
- **Conteúdo**:
  - "Em quantos níveis de hierarquia o supervisor se torna gargalo?"
  - "O que acontece se o researcher retornar informação errada? Quem detecta?"
  - "O formatter deveria ser sub-worker do writer ou worker do supervisor?"
  - Discussão em duplas (2 min)
- **Diagrama**: Caixa de discussão
- **Tempo**: 2 min

---

#### Slide 26 — MetaGPT: SOPs como Hierarquia
- **Tipo**: Diagrama
- **Objetivo**: Conectar hierarchical ao paper canônico MetaGPT
- **Conteúdo**:
  - MetaGPT: framework multi-agente baseado em SOPs (Standard Operating Procedures)
  - Papéis: Product Manager → Architect → Engineer → QA
  - Cada papel = um agente com responsabilidade específica
  - SOPs codificam o fluxo: PRD → design doc → código → testes
  - Lição: a hierarquia reflete a organização humana de uma software house
  - Fonte: arXiv:2308.00352
- **Diagrama**: Hierarquia MetaGPT (PM → Architect → Engineer → QA)
- **Animação**: Papéis aparecem em sequência (top-down)
- **Tempo**: 2 min

---

#### Slide 27 — Crew Formation: Montando uma Equipe
- **Tipo**: Conteúdo
- **Objetivo**: Introduzir o conceito de crew formation (CrewAI, AgentVerse)
- **Conteúdo**:
  - Crew = conjunto de agentes com papéis, objetivos e backstory
  - CrewAI: `Agent(role, goal, backstory)` + `Task(description, agent)` + `Crew(agents, tasks, process)`
  - Process: sequential (pipeline) ou hierarchical (supervisor)
  - AgentVerse: assembling agents como montar uma equipe humana
  - Pergunta: *Como você montaria uma crew para revisar um PR?*
- **Diagrama**: Crew = agentes + tarefas + processo
- **Tempo**: 2 min

---

#### Slide 28 — Exercício Rápido: Hierarchical ou Flat?
- **Tipo**: Exercício
- **Objetivo**: Praticar a decisão de profundidade
- **Conteúdo**:
  - 4 cenários:
    1. "Sistema com 3 domínios distintos (code, security, docs)" → 2 níveis
    2. "Chatbot simples com 3 ferramentas" → Flat (1 supervisor)
    3. "Software house simulado com 6 papéis" → 2-3 níveis (MetaGPT)
    4. "Assistente de viagem com 4 sub-tarefas" → Flat
  - Votação rápida
- **Diagrama**: 4 cards com cenários
- **Tempo**: 2 min

---

### SEÇÃO D — Swarm e Handoffs (Slides 29-34 · 10 min)

---

#### Slide 29 — [SEÇÃO] Swarm e Handoffs
- **Tipo**: Seção
- **Objetivo**: Transição para a topologia descentralizada mais popular
- **Conteúdo**: "3 — Swarm e Handoffs: Controle Descentralizado"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 30 — OpenAI Swarm: Transfer de Controle
- **Tipo**: Diagrama
- **Objetivo**: Apresentar o padrão swarm com handoffs
- **Conteúdo**:
  - OpenAI Swarm (2024): agentes leves com `transfer()` de controle
  - Agente A recebe tarefa → se não for dele, `transfer(to=agent_b)`
  - Não há orquestrador central — o controle passa de agente para agente
  - Analogia: triagem em hospital — paciente é repassado até o especialista certo
  - Estado é passado no handoff (context transfer)
- **Diagrama**: `12-Diagrams/ETHAGT10/swarm-topology.mmd`
- **Animação**: Handoff animado (agente A → seta → agente B → seta → agente C)
- **Tempo**: 2 min

---

#### Slide 31 — Quando Transfer é Melhor que Roteamento Central
- **Tipo**: Comparação
- **Objetivo**: Dar critério para escolher swarm sobre supervisor
- **Conteúdo**:
  - Swarm é melhor quando:
    - Não há necessidade de síntese central
    - Agentes são especializados em domínios distintos
    - Latência importa (sem supervisor como hop extra)
    - Tarefa é "encontrar o especialista certo" (não orquestrar múltiplos)
  - Supervisor é melhor quando:
    - Síntese de múltiplos workers é necessária
    - Controle de ordem importa
    - Estado global precisa ser mantido
- **Diagrama**: 2 colunas comparativas (Swarm vs Supervisor)
- **Tempo**: 2 min

---

#### Slide 32 — Limites do Swarm
- **Tipo**: Conteúdo
- **Objetivo**: Ser honesto sobre as limitações
- **Conteúdo**:
  - Coordenação complexa: swarm não orquestra, só transfere
  - Estado compartilhado: cada handoff passa contexto, pode crescer
  - Loops: agente A transfere para B que transfere de volta para A
  - Sem visão global: nenhum agente "sabe" o estado do sistema
  - Debugging difícil: traçar o caminho do handoff é não-trivial
- **Diagrama**: 5 ícones de "perigo" com labels
- **Tempo**: 1.5 min

---

#### Slide 33 — Swarm vs Supervisor (Comparação Estrutural)
- **Tipo**: Comparação
- **Objetivo**: Sistematizar os trade-offs
- **Conteúdo**:
  - Tabela: Swarm vs Supervisor
  - Eixos: controle central, síntese, latência, custo, complexidade, escalabilidade, debugging, estado global
  - Swarm: baixo controle, sem síntese, baixa latência, escalável
  - Supervisor: alto controle, síntese nativa, latência média, debugging mais fácil
- **Diagrama**: Tabela comparativa colorida
- **Tempo**: 2 min

---

#### Slide 34 — Pergunta: Swarm ou Supervisor?
- **Tipo**: Exercício
- **Objetivo**: Discussão sobre escolha entre as duas topologias
- **Conteúdo**:
  - "Para o caso de revisão de PR com 3 especialistas: swarm ou supervisor?"
  - "E se precisarmos sintetizar as 3 revisões em um relatório?"
  - "E se cada especialista trabalha de forma independente?"
  - Discussão aberta (3 min)
- **Tempo**: 3 min

---

### SEÇÃO E — Pipeline e Orchestrator-Workers (Slides 35-40 · 10 min)

---

#### Slide 35 — [SEÇÃO] Pipeline e Orchestrator-Workers
- **Tipo**: Seção
- **Objetivo**: Transição para topologias de fluxo controlado
- **Conteúdo**: "4 — Pipeline e Orchestrator-Workers: Fluxo Controlado"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 36 — Pipeline Fixo vs Dinâmico
- **Tipo**: Comparação
- **Objetivo**: Distinguir pipeline fixo de dinâmico em multi-agente
- **Conteúdo**:
  - Pipeline fixo: A → B → C (sequência predefinida, código orquestra)
  - Pipeline dinâmico: A decide se vai para B ou C (runtime decision)
  - Fixo = workflow (ETHAGT03), dinâmico = agente orquestrando agentes
  - Multi-agente pipeline: cada step é um agente especializado
  - Exemplo: research → draft → review → publish (4 agentes em pipeline)
- **Diagrama**: 2 fluxogramas lado a lado (fixo vs dinâmico)
- **Tempo**: 2 min

---

#### Slide 37 — Orchestrator-Workers Multi-Agente
- **Tipo**: Diagrama
- **Objetivo**: Revisitar orchestrator-workers no contexto multi-agente
- **Conteúdo**:
  - Orchestrator = agente que particiona a tarefa e delega para workers
  - Diferença do supervisor: orchestrator particiona UMA tarefa em sub-tarefas
  - Supervisor roteia a tarefa inteira para um worker
  - Orchestrator: "divida e conquiste" → síntese no final
  - Fonte: Anthropic, Building Effective Agents (2024)
  - Aprofundamento: ETHAGT03
- **Diagrama**: Orchestrator no centro, workers em volta (estrela)
- **Tempo**: 2 min

---

#### Slide 38 — Composição: Pipeline + Hierarchical
- **Tipo**: Diagrama
- **Objetivo**: Mostrar que topologias se compõem
- **Conteúdo**:
  - Pipeline onde um "step" é um sub-sistema hierarchical
  - Exemplo: pipeline (research → [hierarchical: code review, security review, docs review] → publish)
  - O step de revisão é um supervisor com 3 workers especializados
  - Composição é a regra, não exceção — sistemas reais são hybrid
  - Padrão: pipeline no macro, hierarchical/swarm no micro
- **Diagrama**: Pipeline com um step expandido como hierarchical
- **Animação**: Pipeline aparece, depois um step "expande" em hierarchical
- **Tempo**: 2 min

---

#### Slide 39 — Quando Pipeline > Supervisor
- **Tipo**: Conteúdo
- **Objetivo**: Critério para escolher pipeline sobre supervisor
- **Conteúdo**:
  - Pipeline é melhor quando:
    - Passos são conhecidos e fixos (previsibilidade)
    - Ordem importa (A deve executar antes de B)
    - Custo precisa ser controlado (sem roteamento dinâmico)
    - Não há necessidade de decisão de roteamento em runtime
  - Supervisor é melhor quando:
    - Passos são imprevisíveis
    - Ordem depende do contexto
    - Múltiplos workers podem ser necessários em ordem variável
- **Diagrama**: Checklist de critérios
- **Tempo**: 2 min

---

#### Slide 40 — Exercício: Pipeline ou Agente?
- **Tipo**: Exercício
- **Objetivo**: Praticar a escolha entre pipeline e agente orquestrador
- **Conteúdo**:
  - 3 cenários:
    1. "Geração de relatório financeiro trimestral" → Pipeline (fixo)
    2. "Investigação de incidente de segurança" → Supervisor (dinâmico)
    3. "Processamento de pedidos de e-commerce" → Pipeline (fixo)
  - Justificar em 1 frase cada
- **Diagrama**: 3 cards com cenários
- **Tempo**: 2 min

---

### SEÇÃO F — Event-Driven, Actor Model, Mesh (Slides 41-46 · 10 min)

---

#### Slide 41 — [SEÇÃO] Event-Driven e Actor Model
- **Tipo**: Seção
- **Objetivo**: Transição para topologias assíncronas e escaláveis
- **Conteúdo**: "5 — Event-Driven, Actor Model e Mesh: Escalabilidade Assíncrona"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 42 — Event-Driven Multi-Agente
- **Tipo**: Diagrama
- **Objetivo**: Introduzir event-driven como topologia multi-agente
- **Conteúdo**:
  - Agentes reagem a eventos (não a chamadas diretas)
  - Event broker (Kafka, Redis Streams, NATS) como barramento
  - Agente A publica evento → Agente B consome → reage
  - Desacoplamento total: A não sabe quem consome, B não sabe quem publicou
  - Preview: ETHAGT11 (Event-Driven Agents em profundidade)
- **Diagrama**: Event broker no centro, agentes pub/sub ao redor
- **Tempo**: 2 min

---

#### Slide 43 — Actor Model: Fundação de Escalabilidade
- **Tipo**: Diagrama
- **Objetivo**: Apresentar o actor model como fundação teórica
- **Conteúdo**:
  - Cada agente = ator com: estado privado + mailbox + comportamento
  - Atores se comunicam apenas por mensagens assíncronas
  - Sem estado compartilhado → sem race conditions
  - Escalabilidade natural: milhares de atores em paralelo
  - Frameworks: Akka (JVM), Ray (Python), Microsoft AutoGen
  - Fonte: Hewitt, 1973 (origem); AutoGen (arXiv:2308.08155)
- **Diagrama**: Ator com mailbox (caixa de entrada) + mensagens assíncronas
- **Tempo**: 2 min

---

#### Slide 44 — Agent Mesh: P2P sem Central
- **Tipo**: Diagrama
- **Objetivo**: Apresentar a topologia mais descentralizada
- **Conteúdo**:
  - Agent Mesh: topologia flat peer-to-peer, sem orquestrador
  - Cada agente pode falar com qualquer outro diretamente
  - Vantagem: sem single point of failure, escalabilidade máxima
  - Desafio: coordenação sem central → protocolos de consenso
  - Quando usar: simulações, sistemas distribuídos, agentes autônomos
  - Quando evitar: necessidade de controle global, consistência forte
- **Diagrama**: Mesh de nós interconectados (grafo completo)
- **Tempo**: 2 min

---

#### Slide 45 — Blackboard: O Padrão Esquecido
- **Tipo**: Conteúdo
- **Objetivo**: Resgatar o padrão blackboard como topologia multi-agente
- **Conteúdo**:
  - Blackboard: espaço compartilhado onde agentes leem e escrevem
  - Origem: Hearsay-II (1971-1976), AI clássica
  - Agente A escreve hipótese → Agente B lê e refina → Agente C lê e valida
  - Não há orquestrador — agentes monitoram o blackboard e reagem
  - Quando usar: problemas com múltiplas perspectivas, solução incremental
  - Conexão: precursor do event-driven
- **Diagrama**: Blackboard (quadro compartilhado) com agentes lendo/escrevendo
- **Tempo**: 2 min

---

#### Slide 46 — Pergunta: Mesh vs Hierarchical?
- **Tipo**: Exercício
- **Objetivo**: Discussão sobre a escolha entre descentralizado e centralizado
- **Conteúdo**:
  - "Mesh é sempre a topologia mais escalável?" (V/F — justifique)
  - "Em que cenário mesh é melhor que hierarchical?"
  - "E se precisarmos de uma decisão global coordenada?"
  - Discussão aberta (3 min)
- **Tempo**: 3 min

---

### SEÇÃO G — Tree, Recursive + DEMO (Slides 47-52 · 10 min)

---

#### Slide 47 — [SEÇÃO] Tree, Recursive, Mesh
- **Tipo**: Seção
- **Objetivo**: Transição para topologias estruturadas avançadas
- **Conteúdo**: "6 — Tree of Agents, Recursive e DEMO"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 48 — Tree of Agents (LATS)
- **Tipo**: Diagrama
- **Objetivo**: Apresentar tree of agents como topologia de exploração
- **Conteúdo**:
  - LATS (Language Agent Tree Search): árvore de possíveis ações
  - Agente expande múltiplas possibilidades → avalia → seleciona melhor caminho
  - Como MCTS (Monte Carlo Tree Search) aplicado a agentes LLM
  - Quando usar: problemas com múltiplos caminhos de solução, needing exploration
  - Custo: exponencial com profundidade da árvore
- **Diagrama**: Árvore de exploração com nós (seleção, expansão, avaliação)
- **Tempo**: 2 min

---

#### Slide 49 — Recursive: Meta-Agentes
- **Tipo**: Diagrama
- **Objetivo**: Apresentar recursive como topologia de meta-agentes
- **Conteúdo**:
  - Recursive: agente que instancia sub-agentes para resolver sub-tarefas
  - Meta-agente: "preciso de especialista em X" → cria agente X → delega
  - Auto-referência: sub-agentes podem criar sub-sub-agentes
  - Preview: ETHAGT15 (meta-agentes e auto-aprendizado em profundidade)
  - Quando usar: problemas abertos onde o conjunto de especialistas é desconhecido
- **Diagrama**: Agente recursivo (fractal/self-similar)
- **Tempo**: 2 min

---

#### Slide 50 — Recursive: Anti-Pattern?
- **Tipo**: Comparação
- **Objetivo**: Discutir quando recursive é perigoso
- **Conteúdo**:
  - Recursive é anti-pattern quando:
    - Custo explode (cada nível = LLM calls adicionais)
    - Profundidade incontrolável (sem max_depth)
    - Sub-agentes redundantes (mesma tarefa instanciada múltiplas vezes)
    - Latência inaceitável (serialização de níveis)
  - Quando recursive NÃO é anti-pattern:
    - Decomposição natural do problema
    - max_depth definido
    - Sub-tarefas são genuinamente distintas
  - Pergunta: *Recursive é sempre anti-pattern? Quando não?*
- **Diagrama**: Árvore recursiva crescendo vs truncada (com max_depth)
- **Tempo**: 2 min

---

#### Slide 51 — DEMO: Swarm vs Supervisor (Lab 2)
- **Tipo**: Código
- **Objetivo**: Demo ao vivo — mesma tarefa em duas topologias, medir
- **Conteúdo**:
  - Código do `05-Labs/ETHAGT10/Lab2-Swarm-vs-Supervisor`
  - Tarefa: "Revisão de PR com 3 especialistas"
  - Versão 1: Supervisor (3 workers: code, security, docs)
  - Versão 2: Swarm (3 agentes com handoffs)
  - Medir: latência, custo (tokens), qualidade (subjetiva)
  - Mostrar: trace comparativo lado a lado
- **Diagrama**: 2 traces lado a lado (swarm vs supervisor)
- **Animação**: Métricas aparecem (latência, custo, qualidade)
- **Tempo**: 4 min

---

#### Slide 52 — Pergunta da DEMO
- **Tipo**: Exercício
- **Objetivo**: Engajar a turma com análise dos resultados da demo
- **Conteúdo**:
  - "Qual topologia teve menor latência? Por quê?"
  - "Qual teve menor custo? E melhor qualidade?"
  - "Em que cenário você inverteria a escolha?"
  - Discussão em duplas (2 min)
- **Diagrama**: Caixa de discussão
- **Tempo**: 2 min

---

### SEÇÃO H — Escolha, ADR e Fechamento (Slides 53-62 · 15 min)

---

#### Slide 53 — [SEÇÃO] Escolha e ADR
- **Tipo**: Seção
- **Objetivo**: Transição para a decisão arquitetural justificada
- **Conteúdo**: "7 — Escolha de Topologia e ADR"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 54 — Matriz de Decisão
- **Tipo**: Diagrama
- **Objetivo**: Apresentar a matriz de decisão para escolha de topologia
- **Conteúdo**:
  - 4 eixos: consistência × latência × custo × flexibilidade
  - Para cada topologia, avaliar nos 4 eixos (high/medium/low)
  - Supervisor: alta consistência, latência média, custo médio, flexibilidade baixa
  - Swarm: consistência baixa, latência baixa, custo baixo, flexibilidade alta
  - Pipeline: alta consistência, latência alta (serial), custo baixo, flexibilidade baixa
  - Mesh: consistência baixa, latência baixa, custo médio, flexibilidade máxima
  - Hybrid: balanceado
- **Diagrama**: `12-Diagrams/ETHAGT10/decision-matrix.mmd`
- **Animação**: Topologias aparecem na matriz uma a uma
- **Tempo**: 3 min

---

#### Slide 55 — ADR de Topologia
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar a estrutura de um ADR para decisão de topologia
- **Conteúdo**:
  - ADR (Architecture Decision Record) para topologia multi-agente
  - Estrutura:
    1. **Contexto**: problema, requisitos, restrições
    2. **Decision**: topologia escolhida + justificativa
    3. **Consequências**: trade-offs aceitos, riscos, sinais de evolução
  - Exemplo: "Revisão de PR → Supervisor (síntese necessária, 3 especialistas, baixa latência não crítica)"
  - Template: `08-ADRs/ETHAGT10/`
- **Diagrama**: Template de ADR (3 seções)
- **Tempo**: 2 min

---

#### Slide 56 — Sinais de Evolução
- **Tipo**: Conteúdo
- **Objetivo**: Identificar quando a topologia precisa mudar
- **Conteúdo**:
  - Sinais de que supervisor precisa evoluir:
    - Latência crescente (supervisor gargalo)
    - Workers > 7 (limite cognitivo)
    - Necessidade de paralelismo (supessor serializa)
  - Sinais de que swarm precisa evoluir:
    - Necessidade de síntese global
    - Loops de handoff
    - Estado compartilhado crescendo
  - Sinais de que pipeline precisa evoluir:
    - Passos imprevisíveis
    - Necessidade de decisão dinâmica
  - Regra: monitore métricas, não intuição
- **Diagrama**: Checklist de sinais por topologia
- **Tempo**: 2 min

---

#### Slide 57 — Caso de Estudo: MetaGPT Software House
- **Tipo**: Diagrama
- **Objetivo**: Mostrar todos os conceitos em um caso real
- **Conteúdo**:
  - MetaGPT simula uma software house completa
  - Papéis: Product Manager → Architect → Engineer → QA → Tester
  - Topologia: hierarchical com SOPs codificando o fluxo
  - Entrada: "Build a 2048 game" → Saída: código + testes + docs
  - Resultado: código funcional em minutos, não dias
  - Lição: a topologia reflete a estrutura organizacional humana
  - Fonte: arXiv:2308.00352
- **Diagrama**: Hierarquia MetaGPT com fluxo de artefatos
- **Tempo**: 3 min

---

#### Slide 58 — Exercício: 6 Cenários + ADR
- **Tipo**: Exercício
- **Objetivo**: Praticar a escolha de topologia com justificativa
- **Conteúdo**:
  - 6 cenários:
    1. "Chatbot de suporte com escalonamento humano" → Supervisor
    2. "Sistema de revisão de código com 3 especialistas" → Supervisor ou Swarm
    3. "Pipeline de geração de relatório financeiro" → Pipeline
    4. "Simulação de mercado com múltiplos agentes" → Actor Model / Mesh
    5. "Assistente pessoal multi-função" → Swarm
    6. "Sistema de pesquisa autônoma com exploração" → Tree / Recursive
  - Em grupos: propor topologia + escrever esqueleto de ADR (contexto, decisão, consequências)
  - 3 min discussão, 2 min compartilhar
- **Diagrama**: 6 cards com cenários
- **Tempo**: 4 min

---

#### Slide 59 — Resumo da Aula + Checklist
- **Tipo**: Resumo
- **Objetivo**: Sintetizar os pontos-chave e confirmar cobertura
- **Conteúdo**:
  - 12 topologias catalogadas (centralizadas, fluxo, descentralizadas, estruturadas, reativas)
  - Supervisor = roteador com tool calls; Hierarchical = árvore de supervisores
  - Swarm = handoffs sem central; Pipeline = sequência controlada
  - Actor Model = mensagens assíncronas; Mesh = P2P flat
  - Tree = exploração; Recursive = meta-agentes (cuidado com custo)
  - Escolha via matriz (consistência × latência × custo × flexibilidade) + ADR
  - Sinais de evolução: monitore métricas, não intuição
  - Checklist:
    - [ ] Catalogou as 12 topologias
    - [ ] Implementou supervisor + hierarchical
    - [ ] Comparou swarm vs supervisor
    - [ ] Escreveu ADR de topologia
    - [ ] Identificou sinais de evolução
- **Diagrama**: 7 ícones com pontos-chave + checklist
- **Tempo**: 2 min

---

#### Slide 60 — Quiz: 3 Perguntas Rápidas
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - P1: "Qual topologia NÃO tem orquestrador central?"
    - A) Supervisor · B) Hierarchical · C) Swarm · D) Pipeline
    - Resposta: C
  - P2: "Em LangGraph, o supervisor roteia para workers via:"
    - A) Mensagens de evento · B) Tool calls · C) Handoffs · D) Mailbox
    - Resposta: B
  - P3: "Recursive é anti-pattern quando:"
    - A) O problema se decompõe naturalmente
    - B) max_depth não está definido
    - C) Sub-tarefas são distintas
    - D) A profundidade é 1
    - Resposta: B
- **Tempo**: 2 min

---

#### Slide 61 — Conexão com Próximos Módulos + Referências
- **Tipo**: Referências
- **Objetivo**: Mostrar conexões e indicar leitura
- **Conteúdo**:
  - Conexões:
    - ETHAGT11 — Event-Driven Agents (event-driven em profundidade)
    - ETHAGT14 — Escalabilidade (topologias em produção)
    - ETHAGT15 — Meta-Agentes (recursive e auto-aprendizado)
    - ETHAGT90 — Capstone (projeto final)
  - Leitura obrigatória:
    - Hong, S. et al. *MetaGPT* (arXiv:2308.00352)
    - LangGraph *Multi-Agent* examples (`hierarchical_agent_teams`)
    - OpenAI Swarm (repo, 2024)
  - Leitura recomendada:
    - Chen, W. et al. *AgentVerse* (arXiv:2308.10848)
    - Microsoft AutoGen docs (arXiv:2308.08155)
  - Próximos passos:
    1. Ler: MetaGPT paper
    2. Rodar: Lab 1 (Hierarchical Teams)
    3. Iniciar: Lab 2 (Swarm vs Supervisor)
    4. Próxima aula: ETHAGT11 — Event-Driven Agents
- **Tempo**: 2 min

---

#### Slide 62 — Q&A / Encerramento
- **Tipo**: Capa
- **Objetivo**: Abrir para perguntas e encerrar
- **Conteúdo**:
  - "Perguntas?"
  - Contato do professor
  - "Na próxima aula: ETHAGT11 — Event-Driven Agents"
  - Lembrete: entregar Lab 1 antes da próxima aula
- **Diagrama**: Logo Etho + fundo etho-dark
- **Tempo**: 2 min

---

## Resumo do Storyboard

| Seção | Slides | Tempo | Conteúdo |
|---|---|---|---|
| A — Abertura | 1-6 | 8 min | Capa, objetivos, competências, agenda, motivação, contexto |
| B — Catálogo | 7-16 | 12 min | 12 topologias em grid, espectro centralizado↔descentralizado, exercício de matching |
| C — Supervisor e Hierarchical | 17-28 | 15 min | Supervisor pattern, tool calls, hierarchical, casos de falha, DEMO, MetaGPT, crew formation |
| D — Swarm | 29-34 | 10 min | OpenAI Swarm, handoffs, swarm vs supervisor, limites, discussão |
| E — Pipeline | 35-40 | 10 min | Pipeline fixo vs dinâmico, orchestrator-workers, composição, exercício |
| F — Event/Actor/Mesh | 41-46 | 10 min | Event-driven, actor model, mesh, blackboard, discussão |
| G — Tree/Recursive/DEMO | 47-52 | 10 min | Tree of Agents (LATS), recursive, anti-pattern, DEMO swarm vs supervisor |
| H — Fechamento | 53-62 | 15 min | Matriz de decisão, ADR, sinais de evolução, MetaGPT caso, exercício 6 cenários, resumo, quiz, referências, Q&A |
| **Total** | **62** | **90 min** | |

---

## Diagramas Necessários

| # | Slide | Diagrama | Tipo | Fonte |
|---|---|---|---|---|
| D1 | 8 | Grid 12 topologias (4×3) | Grid | Novo |
| D2 | 9 | Espectro centralizado↔descentralizado | Eixo | Novo |
| D3 | 10 | Supervisor e Hierarchical (mini) | Comparação | `12-Diagrams/ETHAGT10/supervisor-topology.mmd`, `hierarchical-topology.mmd` |
| D4 | 11 | Pipeline e Orchestrator-Workers (mini) | Comparação | Novo |
| D5 | 12 | Swarm, Mesh, Actor Model (mini) | Comparação | `12-Diagrams/ETHAGT10/swarm-topology.mmd` + novos |
| D6 | 13 | Tree e Recursive (mini) | Comparação | Novo |
| D7 | 14 | Event-Driven, Blackboard, Hybrid (mini) | Comparação | Novo |
| D8 | 15 | Single Agent com N tools | Estrela | Novo |
| D9 | 18 | Supervisor pattern (topologia) | Flowchart | `12-Diagrams/ETHAGT10/supervisor-topology.mmd` |
| D10 | 19 | Supervisor como tool calls (LangGraph) | Sequência | `12-Diagrams/ETHAGT10/supervisor-topology.mmd` |
| D11 | 20 | Hierarchical (árvore de supervisores) | Flowchart | `12-Diagrams/ETHAGT10/hierarchical-topology.mmd` |
| D12 | 21 | 3 níveis vs flat (comparação) | 3 árvores | Novo |
| D13 | 22 | Supervisor gargalo (funil) | Flowchart | Novo |
| D14 | 23 | Workers redundantes (Venn) | Venn | Novo |
| D15 | 26 | MetaGPT SOPs (hierarquia) | Hierarquia | arXiv:2308.00352 |
| D16 | 27 | Crew formation (agentes + tarefas + processo) | Flowchart | CrewAI |
| D17 | 30 | Swarm topology com handoffs | Flowchart | `12-Diagrams/ETHAGT10/swarm-topology.mmd` |
| D18 | 33 | Swarm vs Supervisor (tabela) | Tabela | Novo |
| D19 | 36 | Pipeline fixo vs dinâmico | Comparação | Novo |
| D20 | 37 | Orchestrator-Workers (estrela) | Flowchart | Anthropic |
| D21 | 38 | Pipeline + Hierarchical (composição) | Flowchart | Novo |
| D22 | 42 | Event-driven (pub/sub) | Flowchart | Novo |
| D23 | 43 | Actor model (mailbox) | Flowchart | Novo |
| D24 | 44 | Agent Mesh (grafo P2P) | Grafo | Novo |
| D25 | 45 | Blackboard (espaço compartilhado) | Flowchart | Novo |
| D26 | 48 | Tree of Agents (LATS) | Árvore | Novo |
| D27 | 49 | Recursive (meta-agentes) | Fractal | Novo |
| D28 | 50 | Recursive anti-pattern (árvore crescendo vs truncada) | Comparação | Novo |
| D29 | 54 | Matriz de decisão | Matriz | `12-Diagrams/ETHAGT10/decision-matrix.mmd` |
| D30 | 55 | ADR template (3 seções) | Template | Novo |
| D31 | 56 | Sinais de evolução (checklist) | Checklist | Novo |
| D32 | 57 | MetaGPT software house (hierarquia + artefatos) | Flowchart | arXiv:2308.00352 |

---

## Pontos de Engajamento

| # | Slide | Tipo | Interação |
|---|---|---|---|
| E1 | 5 | Pergunta | "Qual foi a topologia mais comum que vocês já usaram?" |
| E2 | 16 | Exercício | Matching cenário → topologia (6 cenários, votação) |
| E3 | 25 | Discussão | "Em quantos níveis o supervisor vira gargalo?" (duplas, 2 min) |
| E4 | 27 | Pergunta | "Como você montaria uma crew para revisar um PR?" |
| E5 | 28 | Exercício | Hierarchical ou flat? (4 cenários, votação) |
| E6 | 34 | Discussão | "Swarm ou supervisor para revisão de PR?" (3 min) |
| E7 | 40 | Exercício | Pipeline ou agente? (3 cenários) |
| E8 | 46 | Discussão | "Mesh é sempre a topologia mais escalável?" (3 min) |
| E9 | 50 | Pergunta | "Recursive é sempre anti-pattern? Quando não?" |
| E10 | 52 | Discussão | Análise dos resultados da DEMO swarm vs supervisor (2 min) |
| E11 | 58 | Exercício | 6 cenários + esqueleto de ADR (grupos, 5 min) |
| E12 | 60 | Quiz | 3 perguntas de verificação |

---

## Pendências de Produção

- [ ] Produzir 24 diagramas novos (D1, D2, D4, D6, D7, D8, D12, D13, D14, D15, D16, D18, D19, D20, D21, D22, D23, D24, D25, D26, D27, D28, D30, D31, D32)
- [ ] Validar 4 diagramas existentes (D3, D9-D11, D17, D29) contra o storyboard
- [ ] Screenshot do trace da DEMO hierarchical (Slide 24)
- [ ] Screenshot do trace comparativo swarm vs supervisor (Slide 51)
- [ ] Screenshot do código com syntax highlighting (Slides 19, 24, 51)
- [ ] Imagem de fundo para capa (Slide 1)
- [ ] Badge de competências (Slide 3)
- [ ] Timeline de marcos multi-agente (Slide 6)
- [ ] Template de ADR em `08-ADRs/ETHAGT10/` (Slide 55)
- [ ] Confirmar referências aos Labs (`05-Labs/ETHAGT10/Lab1`, `Lab2`)

---

> **Aguardando aprovação deste storyboard para gerar os slides detalhados com notas do professor.**
