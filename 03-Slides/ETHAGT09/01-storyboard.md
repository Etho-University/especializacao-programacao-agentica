# ETHAGT09 — Comunicação e Coordenação Multi-Agente
## Storyboard da Apresentação

> **Universidade Etho · Especialização em Programação Agêntica**
> Fase C — Sistemas Multi-Agente · 25 h
> Storyboard v1.0 · Julho 2026

---

## Metadados da Apresentação

| Campo | Valor |
|---|---|
| Código | ETHAGT09 |
| Título | Comunicação e Coordenação Multi-Agente (A2A · blackboard · actor model) |
| Duração estimada | 90 min (2 blocos de 45 min) |
| Total de slides | 72 |
| Público | Arquitetos, Engenheiros de Software, Engenheiros de IA, Cientistas de Dados, Tech Leads |
| Pré-requisitos | ETHAGT04 (Reasoning & Planning) |
| Competências | C1 (A), C2 (I), C3 (B), C4 (B), C5 (B) |

---

## Mapa Visual da Apresentação

```
BLOCO 1 (45 min)                              BLOCO 2 (45 min)
┌──────────────────────────────┐              ┌──────────────────────────────┐
│ SEÇÃO A — Abertura (8 min)   │              │ SEÇÃO E — Actor Model (13 m) │
│  Capa · Objetivos · Agenda   │              │  Atores · Encapsulamento     │
│  Motivação · Contexto        │              │  Concorrência sem locks      │
├──────────────────────────────┤              │  DEMO: 2 arquiteturas        │
│ SEÇÃO B — Espectro A2A (10m) │              ├──────────────────────────────┤
│  Direta vs async             │              │ SEÇÃO F — Negociação (10 min)│
│  Topologias · Schemas        │              │  Bargaining · Auction        │
│  Erros · Garantias           │              │  Conflito · Deadlock         │
├──────────────────────────────┤              ├──────────────────────────────┤
│ SEÇÃO C — Padrões Conv (13m) │              │ SEÇÃO G — Protocolos (8 min) │
│  CAMEL · AutoGen · Swarm     │              │  A2A Protocol · MCP vs A2A   │
│  Handoff · MetaGPT           │              │  Orquestração · FIPA         │
├──────────────────────────────┤              ├──────────────────────────────┤
│ SEÇÃO D — Blackboard (10 min)│              │ SEÇÃO H — Fechamento (18 min)│
│  Espaço compartilhado        │              │  Boas práticas · Anti-patterns│
│  vs mensagens diretas        │              │  Caso MetaGPT · Exercício    │
│  Implementação               │              │  Resumo · Quiz · Refs · Q&A  │
└──────────────────────────────┘              └──────────────────────────────┘
```

---

## Storyboard Detalhado

### SEÇÃO A — Abertura (Slides 1-7 · 8 min)

---

#### Slide 1 — Capa
- **Tipo**: Capa
- **Objetivo**: Identificar a aula, professor e contexto
- **Conteúdo**:
  - ETHAGT09 — Comunicação e Coordenação Multi-Agente
  - A2A · Blackboard · Actor Model
  - Universidade Etho · Especialização em Programação Agêntica
  - Fase C — Sistemas Multi-Agente
  - Professor · Data
- **Diagrama**: Logo Etho + imagem de fundo (rede de agentes interconectados)
- **Animação**: Fade in do título
- **Tempo**: 1 min

---

#### Slide 2 — Objetivos do Módulo
- **Tipo**: Conteúdo
- **Objetivo**: Deixar claro o que o aluno deve conseguir fazer ao final
- **Conteúdo**:
  - Objetivo geral: Dominar modelos de comunicação e coordenação entre agentes
  - 5 objetivos específicos:
    1. Distinguir padrões de comunicação A2A
    2. Implementar troca estruturada de mensagens (com schemas)
    3. Aplicar blackboard para coordenação com espaço compartilhado
    4. Aplicar actor model para concorrência e isolamento
    5. Lidar com negociação, conflito e consenso
  - Saber escolher o padrão conforme o problema
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
  - C2 Multi-Agent Systems → **I**
  - C3 MCP & Tool Use → B
  - C4 Agent Memory → B
  - C5 AgentOps & Avaliação → B
  - Badge visual por competência
- **Diagrama**: Radar chart dos 5 pilares
- **Animação**: Radar aparece com wipe
- **Tempo**: 1 min

---

#### Slide 4 — Agenda
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar o roteiro da aula com tempos
- **Conteúdo**:
  - Bloco 1: Abertura → Espectro A2A → Padrões de Conversação → Blackboard
  - Bloco 2: Actor Model → Negociação → Protocolos → Fechamento
  - Tempos estimados por seção
- **Diagrama**: Timeline horizontal com 8 seções
- **Animação**: Timeline cresce da esquerda para direita
- **Tempo**: 1 min

---

#### Slide 5 — Motivação: O Problema da Coordenação
- **Tipo**: Conteúdo
- **Objetivo**: Criar tensão — agentes sem protocolo viram caos
- **Conteúdo**:
  - Cenário: agente de pesquisa e agente de escrita precisam colaborar
  - Sem padrão: mensagens se perdem, estado diverge, ninguém sabe quem faz o quê
  - "Dois agentes inteligentes não produzem um sistema inteligente automaticamente"
  - Pergunta: *Quantos agentes colaborando antes de virar caos?*
- **Diagrama**: Imagem de "caos" (mensagens cruzadas sem ordem) → vs → "ordem" (protocolo estruturado)
- **Animação**: Split — lado esquerdo (caos), depois lado direito (ordem)
- **Tempo**: 2 min

---

#### Slide 6 — Contexto: Por Que Agora
- **Tipo**: Conteúdo
- **Objetivo**: Explicar a confluência que tornou multi-agente viável
- **Conteúdo**:
  - Linha do tempo: 2022 (ReAct) → 2023 (AutoGen, CAMEL) → 2024 (Swarm, A2A Protocol) → 2025 (MetaGPT, padronização)
  - Confluência: reasoning + tool calling + frameworks multi-agente + redução de custo
  - Survey arXiv:2308.00352 — LLM-based Multi-Agent Systems
  - Google A2A Protocol (2024) como marco de padronização
- **Diagrama**: Timeline horizontal com marcos
- **Animação**: Marcos aparecem sequencialmente
- **Tempo**: 1 min

---

#### Slide 7 — [SEÇÃO] O Espectro da Comunicação A2A
- **Tipo**: Seção
- **Objetivo**: Transição para o bloco de fundamentos de comunicação
- **Conteúdo**: Número "1" grande + "O Espectro da Comunicação A2A"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

### SEÇÃO B — O Espectro da Comunicação A2A (Slides 8-15 · 10 min)

---

#### Slide 8 — Comunicação Direta vs Assíncrona
- **Tipo**: Comparação
- **Objetivo**: Estabelecer o espectro fundamental de comunicação
- **Conteúdo**:
  - Síncrona (request/response): agente A pergunta → B responde → continua
  - Assíncrona (eventos): agente A publica → B reage quando puder
  - Trade-off: latência vs desacoplamento
  - Analogia: telefone (síncrono) vs e-mail (assíncrono)
- **Diagrama**: Duas timelines lado a lado
- **Animação**: Setas síncronas aparecem, depois assíncronas
- **Tempo**: 2 min

---

#### Slide 9 — Topologias: Broadcast vs P2P vs Pub/Sub
- **Tipo**: Diagrama
- **Objetivo**: Mostrar as 3 topologias canônicas de comunicação
- **Conteúdo**:
  - Broadcast: 1 → todos (anúncio global)
  - P2P (point-to-point): 1 → 1 (conversa direta)
  - Pub/Sub: produtores → tópicos → consumidores (desacoplado)
  - Quando cada uma brilha
  - Pergunta: *Qual topologia para 10 agentes debatendo um diagnóstico?*
- **Diagrama**: 3 mini-diagramas em grid 1x3
- **Animação**: Cada topologia aparece com click
- **Tempo**: 2 min

---

#### Slide 10 — Schemas de Mensagem A2A
- **Tipo**: Código
- **Objetivo**: Mostrar que mensagens A2A precisam de estrutura
- **Conteúdo**:
  - Campos obrigatórios: sender, receiver, message_type, payload, timestamp, version
  - Exemplo de schema JSON
  - Por que versionar: agentes evoluem independentemente
  - Sem schema = "telefone sem fio"
- **Diagrama**: Bloco de código JSON com highlight dos campos
- **Animação**: Campos surgem um a um
- **Tempo**: 2 min

---

#### Slide 11 — Versionamento de Mensagens
- **Tipo**: Conteúdo
- **Objetivo**: Aprofundar o porquê do versionamento
- **Conteúdo**:
  - Agentes podem estar em versões diferentes (deploy independente)
  - Estratégias: semver no schema, campo `version` obrigatório
  - Compatibilidade: backward, forward, full
  - Exemplo: v1 não tem `priority`, v2 adiciona — v1 ignora, v2 usa
- **Diagrama**: Timeline de versões de schema
- **Tempo**: 1.5 min

---

#### Slide 12 — Erros: Mensagens Perdidas e Duplicadas
- **Tipo**: Conteúdo
- **Objetivo**: Ser honesto sobre falhas de comunicação
- **Conteúdo**:
  - Perdida: agente envia, receptor nunca recebe (rede, crash)
  - Duplicada: agente envia 1x, receptor processa 2x (retry mal implementado)
  - Impacto em agentes: decisão baseada em dado faltante ou ação executada 2x
  - Mitigação: acknowledgments, idempotência, deduplication keys
- **Diagrama**: 2 ícones de erro com fluxos visuais
- **Tempo**: 1.5 min

---

#### Slide 13 — Erros: Fora de Ordem
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar que ordem importa em sistemas multi-agente
- **Conteúdo**:
  - Mensagem 2 chega antes da 1 → estado inconsistente
  - Causa: rotas diferentes, latência variável
  - Mitigação: sequence numbers, timestamps lamport, fila ordenada
  - Em LLM agents: ordem do contexto importa — desordem = alucinação
- **Diagrama**: Sequência numérica embaralhada
- **Tempo**: 1 min

---

#### Slide 14 — Garantias de Entrega
- **Tipo**: Comparação
- **Objetivo**: Sistematizar as semânticas de entrega
- **Conteúdo**:
  - At-most-once: pode perder, nunca duplica (fire-and-forget)
  - At-least-once: nunca perde, pode duplicar (com retry)
  - Exactly-once: nunca perde, nunca duplica (ideal, caro)
  - Trade-off: simplicidade vs confiabilidade vs custo
  - Pergunta: *Qual garantia para transferência bancária entre agentes?*
- **Diagrama**: Tabela comparativa 3x3
- **Tempo**: 1.5 min

---

#### Slide 15 — Exercício Rápido: Topologia Ideal
- **Tipo**: Exercício
- **Objetivo**: Praticar a escolha de topologia e garantia
- **Conteúdo**:
  - 4 cenários curtos:
    1. "Triager despacha para especialista" → P2P + handoff
    2. "3 agentes votam em um diagnóstico" → Broadcast + at-least-once
    3. "Agente publica evento de conclusão" → Pub/Sub + at-most-once
    4. "Negociação comprador/vendedor" → P2P + exactly-once
  - Votação rápida (mãos levantadas)
- **Diagrama**: 4 cards com cenários
- **Tempo**: 2 min

---

### SEÇÃO C — Padrões de Conversação (Slides 16-26 · 13 min)

---

#### Slide 16 — [SEÇÃO] Padrões de Conversação
- **Tipo**: Seção
- **Objetivo**: Transição para os padrões de conversação multi-agente
- **Conteúdo**: "2 — Padrões de Conversação"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 17 — Três Padrões Canônicos
- **Tipo**: Diagrama
- **Objetivo**: Visão geral dos 3 padrões de conversação
- **Conteúdo**:
  1. Two-agent dialogue (estilo CAMEL) — 2 agentes conversam
  2. Group chat (estilo AutoGen) — N agentes em um grupo
  3. Handoff / transfer (estilo Swarm) — agente passa controle
  - Cada padrão resolve um problema de coordenação diferente
- **Diagrama**: 3 mini-diagramas em grid 1x3
- **Animação**: Cada padrão aparece com click
- **Tempo**: 2 min

---

#### Slide 18 — Two-Agent Dialogue (CAMEL)
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar o padrão de diálogo entre 2 agentes
- **Conteúdo**:
  - CAMEL: Communicative Agents for Mind Exploration
  - Role-playing: agente A como "assistente", agente B como "usuário simulado"
  - Estrutura: task → inception prompting → turnos de diálogo
  - Fonte: arXiv:2303.17760
  - Quando brilha: tarefas que exigem refinamento iterativo entre 2 perspectivas
- **Diagrama**: Diagrama de diálogo A↔B com turnos
- **Tempo**: 2 min

---

#### Slide 19 — CAMEL em Ação: Role-Playing
- **Tipo**: Código
- **Objetivo**: Mostrar um trace real de diálogo CAMEL
- **Conteúdo**:
  - Tarefa: "Escrever um artigo sobre energias renováveis"
  - Turno 1 (usuário): "Qual estrutura você sugere?"
  - Turno 2 (assistente): "Introdução, 3 seções técnicas, conclusão..."
  - Turno 3 (usuário): "Aprofunde a seção de solar"
  - Turno 4 (assistente): "Painéis fotovoltaicos convertem..."
  - Inception prompting mantém os papéis
- **Diagrama**: Console estilizado com turnos
- **Animação**: Turnos aparecem sequencialmente
- **Tempo**: 2 min

---

#### Slide 20 — Group Chat (AutoGen)
- **Tipo**: Diagrama
- **Objetivo**: Apresentar o padrão de chat em grupo
- **Conteúdo**:
  - AutoGen GroupChat: N agentes em um grupo orquestrado
  - Componentes: agentes + group chat manager
  - Manager decide quem fala a seguir
  - Fonte: arXiv:2308.08155
  - Quando brilha: tarefas que exigem múltiplas especialidades
- **Diagrama**: Hub-and-spoke com manager no centro
- **Tempo**: 2 min

---

#### Slide 21 — AutoGen GroupChat: Selector vs Round-Robin
- **Tipo**: Comparação
- **Objetivo**: Diferenciar as estratégias de seleção de próximo falante
- **Conteúdo**:
  - Round-robin: ordem fixa (A → B → C → A → ...)
  - Selector: LLM decide quem fala a seguir (baseado no contexto)
  - Dynamic: qualquer agente pode se "inscrever" para falar
  - Trade-off: previsibilidade vs adaptabilidade
  - Pergunta: *Qual estratégia para 5 especialistas debatendo um diagnóstico?*
- **Diagrama**: 3 mini-fluxos lado a lado
- **Tempo**: 2 min

---

#### Slide 22 — Handoff / Transfer (OpenAI Swarm)
- **Tipo**: Conteúdo
- **Objetivo**: Introduzir o padrão de handoff
- **Conteúdo**:
  - Swarm: agente transfere controle para outro agente
  - Handoff = "passa a bola" — o agente atual sai, o novo entra
  - Exemplo: Triager → handoff para Sales / Billing / Support
  - Leve, sem orquestrador central (diferente de GroupChat)
  - Fonte: OpenAI Swarm (repo + paper técnico)
- **Diagrama**: `12-Diagrams/ETHAGT09/handoff.mmd`
- **Tempo**: 2 min

---

#### Slide 23 — Handoff vs Delegação (Supervisor)
- **Tipo**: Comparação
- **Objetivo**: Esclarecer a diferença entre handoff e delegação
- **Conteúdo**:
  - Handoff (Swarm): controle TRANSFERIDO — agente original sai
  - Delegação (Supervisor/LangGraph): controle DELEGADO — supervisor espera retorno
  - Handoff = "transfere a chamada" vs Delegação = "coloca em espera e consulta"
  - Trade-off: simplicidade vs controle
  - Pergunta: *Handoff ou delegação para um sistema de suporte ao cliente?*
- **Diagrama**: Comparação lado a lado com setas de fluxo
- **Tempo**: 2 min

---

#### Slide 24 — MetaGPT: SOPs para Multi-Agente
- **Tipo**: Diagrama
- **Objetivo**: Mostrar como MetaGPT usa SOPs (Standard Operating Procedures)
- **Conteúdo**:
  - MetaGPT: agentes seguem SOPs como em uma equipe de software
  - Papéis: Product Manager, Architect, Engineer, QA
  - Cada papel tem entradas, processo e saídas definidos
  - Comunicação estruturada via artefatos (não chat livre)
  - Aprofundamento no caso de estudo (Slide 65)
- **Diagrama**: Pipeline MetaGPT com papéis e artefatos
- **Tempo**: 2 min

---

#### Slide 25 — Quando Cada Padrão Brilha
- **Tipo**: Conteúdo
- **Objetivo**: Dar critério prático de escolha
- **Conteúdo**:
  - Two-agent: refinamento iterativo entre 2 perspectivas
  - Group chat: múltiplas especialidades colaborando simultaneamente
  - Handoff: roteamento baseado em especialização (1 de cada vez)
  - Selector group chat: quando a ordem não é previsível
  - Round-robin: quando todos devem contribuir igualmente
- **Diagrama**: Tabela de decisão
- **Tempo**: 1.5 min

---

#### Slide 26 — Exercício: Quando Usar Cada Padrão
- **Tipo**: Exercício
- **Objetivo**: Praticar a decisão em cenários reais
- **Conteúdo**:
  - 4 cenários:
    1. "Writer e reviewer refinam um texto" → Two-agent (CAMEL)
    2. "3 especialistas debatem diagnóstico" → Group chat (selector)
    3. "Triager encaminha para dept correto" → Handoff (Swarm)
    4. "Equipe de dev constrói um feature" → MetaGPT (SOPs)
  - Votação rápida
- **Diagrama**: 4 cards com cenários
- **Tempo**: 2 min

---

### SEÇÃO D — Blackboard (Slides 27-33 · 10 min)

---

#### Slide 27 — [SEÇÃO] Blackboard
- **Tipo**: Seção
- **Objetivo**: Transição para o padrão blackboard
- **Conteúdo**: "3 — Blackboard: Espaço Compartilhado"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 28 — O Que É Blackboard
- **Tipo**: Conteúdo
- **Objetivo**: Definir o padrão blackboard
- **Conteúdo**:
  - Espaço compartilhado de estado: agentes escrevem e leem
  - Inspirado no blackboard físico de salas de aula
  - Desacoplamento: agentes não precisam se conhecer
  - Padrão clássico de IA (HEARSAY-II, 1970s)
  - Renascido com LLM agents: estado compartilhado como "memória coletiva"
- **Diagrama**: Conceito visual — lousa com notas de múltiplos agentes
- **Tempo**: 2 min

---

#### Slide 29 — Blackboard Diagram
- **Tipo**: Diagrama
- **Objetivo**: Mostrar a arquitetura do blackboard
- **Conteúdo**:
  - 3 agentes conectados a um blackboard central
  - Blackboard armazena facts, hypotheses, partial results
  - Agentes leem → processam → escrevem de volta
  - Sem comunicação direta entre agentes
- **Diagrama**: `12-Diagrams/ETHAGT09/blackboard.mmd`
- **Animação**: Agentes surgem, depois blackboard, depois conexões
- **Tempo**: 2 min

---

#### Slide 30 — Quando Blackboard Brilha
- **Tipo**: Conteúdo
- **Objetivo**: Dar critério de uso
- **Conteúdo**:
  - Problema dinâmico: estado muda conforme agentes contribuem
  - Múltiplos especialistas: cada um contribui com seu conhecimento
  - Contribuição incremental: ninguém tem a resposta completa
  - Exemplos: diagnóstico médico multi-especialidade, planejamento estratégico
  - Pergunta: *Quando blackboard é preferível a mensagens diretas?*
- **Diagrama**: Checklist de critérios
- **Tempo**: 2 min

---

#### Slide 31 — Blackboard vs Mensagens Diretas
- **Tipo**: Comparação
- **Objetivo**: Sistematizar o trade-off
- **Conteúdo**:
  - Blackboard: baixo acoplamento, estado compartilhado, sem ordem garantida
  - Mensagens diretas: alto acoplamento, explícito, ordem controlada
  - Blackboard escala melhor com N agentes (O(N) vs O(N²))
  - Mensagens diretas dão mais controle sobre o fluxo
  - Regra: blackboard quando N é grande e contribuições são independentes
- **Diagrama**: Tabela comparativa
- **Tempo**: 2 min

---

#### Slide 32 — Implementação: Em Memória + Persistente
- **Tipo**: Código
- **Objetivo**: Mostrar como implementar blackboard na prática
- **Conteúdo**:
  - Em memória: dict/List compartilhado (rápido, volátil)
  - Persistente: Postgres/Redis (resiliente, distribuído)
  - Estrutura: entradas com agent_id, timestamp, content, type
  - Snippet: classe Blackboard com read/write/list
  - Locking: read-write lock ou CRDT para concorrência
- **Diagrama**: Code block + arquitetura
- **Tempo**: 2 min

---

#### Slide 33 — Exercício: Blackboard ou Mensagens?
- **Tipo**: Exercício
- **Objetivo**: Praticar a decisão entre blackboard e mensagens diretas
- **Conteúdo**:
  - 3 cenários:
    1. "5 agentes contribuem com partes de um relatório" → Blackboard
    2. "Agente pergunta preço a outro" → Mensagem direta
    3. "3 agentes debatem com estado compartilhado" → Blackboard
  - Discutir em duplas (2 min)
- **Diagrama**: 3 cards com cenários
- **Tempo**: 2 min

---

### SEÇÃO E — Actor Model (Slides 34-44 · 13 min)

---

#### Slide 34 — [SEÇÃO] Actor Model
- **Tipo**: Seção
- **Objetivo**: Transição para o actor model
- **Conteúdo**: "4 — Actor Model: Concorrência sem Locks"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 35 — O Que É Actor Model
- **Tipo**: Conteúdo
- **Objetivo**: Definir o actor model
- **Conteúdo**:
  - Atores encapsulam estado; só se comunicam por mensagens
  - Cada ator tem um mailbox (fila de mensagens)
  - Processa uma mensagem por vez — sem locks, sem race conditions
  - Fonte: Hewitt, 1973 (clássico)
  - Renascido com LLM agents: cada agente = um ator isolado
- **Diagrama**: Conceito — ator com mailbox e estado privado
- **Tempo**: 2 min

---

#### Slide 36 — Actor Model Diagram
- **Tipo**: Diagrama
- **Objetivo**: Mostrar a arquitetura do actor model
- **Conteúdo**:
  - 3 atores com mailboxes individuais
  - Comunicação assíncrona via mensagens
  - Estado privado encapsulado em cada ator
  - Sem estado compartilhado = sem locks
- **Diagrama**: `12-Diagrams/ETHAGT09/actor-model.mmd`
- **Animação**: Mensagens fluem entre atores
- **Tempo**: 2 min

---

#### Slide 37 — Princípios: Encapsulamento e Isolamento
- **Tipo**: Conteúdo
- **Objetivo**: Aprofundar os princípios fundamentais
- **Conteúdo**:
  - Encapsulamento: estado do ator é inacessível externamente
  - Isolamento: falha em um ator não derruba outros
  - "Share nothing" — único caminho de interação é mensagem
  - Implicação para agentes: cada agente tem estado protegido
  - Pergunta: *Actor model vs shared state — qual é mais seguro para dados críticos?*
- **Diagrama**: Caixa fechada (ator) com apenas "slot" de mensagens
- **Tempo**: 2 min

---

#### Slide 38 — Concorrência sem Locks
- **Tipo**: Comparação
- **Objetivo**: Mostrar a vantagem concorrência do actor model
- **Conteúdo**:
  - Shared state: múltiplas threads + locks → deadlocks, race conditions
  - Actor model: 1 mensagem por vez por ator → sem locks
  - Escala horizontalmente: adicione mais atores
  - Trade-off: overhead de serialização de mensagens
  - Regra: "don't communicate by sharing memory; share memory by communicating"
- **Diagrama**: Thread+lock vs Actor com mailbox
- **Tempo**: 2 min

---

#### Slide 39 — Localização Transparente
- **Tipo**: Conteúdo
- **Objetivo**: Explicar a vantagem de distribuição
- **Conteúdo**:
  - Ator local vs ator remoto: mesma interface (mensagem)
  - Roteamento transparente: framework decide para onde enviar
  - Escala: mova atores para outros nós sem mudar código
  - Aplicação: agentes distribuídos em múltiplos servidores
  - Pergunta: *Como isso muda a arquitetura de deployment?*
- **Diagrama**: Nós de computação com atores migrando
- **Tempo**: 1.5 min

---

#### Slide 40 — Akka / Erlang / asyncio
- **Tipo**: Comparação
- **Objetivo**: Mostrar implementações reais do actor model
- **Conteúdo**:
  - Erlang/OTP: pioneiro, tolerância a falha (supervisores)
  - Akka (JVM): actor system para Scala/Java
  - Python asyncio: coroutines como atores leves (sem supervisão nativa)
  - Para LLM agents: asyncio + framework (LangGraph, AutoGen)
  - Snippet: actor simples em asyncio
- **Diagrama**: 3 colunas comparativas
- **Tempo**: 2 min

---

#### Slide 41 — Aplicação a Agentes Distribuídos
- **Tipo**: Conteúdo
- **Objetivo**: Conectar actor model a sistemas multi-agente LLM
- **Conteúdo**:
  - Cada agente = um ator com mailbox
  - Tool execution = mensagem para ator especializado
  - Memória = estado privado do ator
  - Escala: agentes em nós diferentes, coordenados por mensagens
  - Caso de uso: agentes de pesquisa distribuídos processando em paralelo
- **Diagrama**: Topologia distribuída com agentes como atores
- **Tempo**: 1.5 min

---

#### Slide 42 — Actor Model vs Shared State
- **Tipo**: Comparação
- **Objetivo**: Sistematizar o trade-off para LLM agents
- **Conteúdo**:
  - Shared state (blackboard): leitura/escrita compartilhada, precisa de locks
  - Actor model: estado isolado, mensagens assíncronas, sem locks
  - Blackboard + Actor = híbrido: ator gerencia o blackboard
  - Pergunta: *Verdadeiro ou falso: "Actor model é mais lento que shared-state."*
  - Resposta: Falso — em cenários de alta concorrência, actor model escala melhor
- **Diagrama**: Tabela comparativa
- **Tempo**: 1.5 min

---

#### Slide 43 — DEMO: Duas Arquiteturas, um Problema
- **Tipo**: Código
- **Objetivo**: Demo ao vivo — mesma tarefa em 2 arquiteturas
- **Conteúdo**:
  - Tarefa: pesquisar + resumir + formatar um relatório
  - Versão 1: AutoGen-style group chat (agentes conversam)
  - Versão 2: Blackboard (agentes compartilham espaço)
  - Comparar: número de mensagens, tempo, acoplamento
  - Referência: `05-Labs/ETHAGT09/Lab1-Duas-Arquiteturas`
- **Diagrama**: Code block + terminal side-by-side
- **Animação**: Highlight de linhas chave
- **Tempo**: 4 min

---

#### Slide 44 — Pergunta da DEMO
- **Tipo**: Exercício
- **Objetivo**: Engajar a turma com uma pergunta sobre a demo
- **Conteúdo**:
  - "Qual arquitetura foi mais fácil de debugar? Por quê?"
  - "Em qual delas adicionar um 4º agente seria mais simples?"
  - Discussão em duplas (2 min)
- **Diagrama**: Caixa de discussão
- **Tempo**: 2 min

---

### SEÇÃO F — Negociação e Conflito (Slides 45-52 · 10 min)

---

#### Slide 45 — [SEÇÃO] Negociação e Conflito
- **Tipo**: Seção
- **Objetivo**: Transição para negociação entre agentes
- **Conteúdo**: "5 — Negociação e Conflito"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 46 — Por Que Agentes Negociam
- **Tipo**: Conteúdo
- **Objetivo**: Motivar a necessidade de negociação
- **Conteúdo**:
  - Agentes têm objetivos próprios — podem conflitar
  - Exemplo: comprador quer preço baixo, vendedor quer preço alto
  - Sem negociação: impasse ou força bruta
  - Com negociação: convergência para acordo mutuamente aceitável
  - Pergunta: *O que acontece quando dois agentes têm objetivos parcialmente conflitantes?*
- **Diagrama**: Dois agentes com setas de tensão
- **Tempo**: 1.5 min

---

#### Slide 47 — Bargaining
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar o padrão de barganha
- **Conteúdo**:
  - Bargaining: proposta → contraproposta → ... → acordo ou impasse
  - Estratégias: conceder gradativamente, fixar reserva, BATNA
  - Convergência: cada parte cede até encontrar zona de acordo
  - Exemplo: comprador propõe 100, vendedor contrapropõe 150, convergem em 120
  - Risco: loops infinitos sem estratégia de cessão
- **Diagrama**: Fluxo de proposta/contraproposta
- **Tempo**: 2 min

---

#### Slide 48 — Auction
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar o padrão de leilão
- **Conteúdo**:
  - Auction: 1 vendedor, N compradores competem
  - Tipos: English (ascendente), Dutch (descendente), sealed-bid, Vickrey
  - Quando brilha: valor subjetivo, múltiplos interessados
  - Exemplo: agentes competindo por recursos computacionais
  - Vencedor: maior lance (ou segundo maior no Vickrey)
- **Diagrama**: Fluxo de leilão com lances
- **Tempo**: 1.5 min

---

#### Slide 49 — Negotiation Diagram
- **Tipo**: Diagrama
- **Objetivo**: Visualizar o fluxo completo de negociação
- **Conteúdo**:
  - Comprador propõe 100 → Vendedor contrapropõe 150
  - Comprador propõe 120 → Vendedor aceita → acordo
  - Caminho alternativo: rejeita após N rounds → escalar ou timeout
  - Diagrama mostra convergência e fallback
- **Diagrama**: `12-Diagrams/ETHAGT09/negotiation.mmd`
- **Animação**: Propostas fluem sequencialmente
- **Tempo**: 2 min

---

#### Slide 50 — Resolução de Conflito: Voting e Mediator
- **Tipo**: Comparação
- **Objetivo**: Mostrar estratégias para resolver divergências
- **Conteúdo**:
  - Voting: cada agente vota, maioria vence (simples, pode errar)
  - Weighted voting: votos ponderados por confiança/expertise
  - Mediator: agente neutro facilita consenso (mais caro, mais robusto)
  - Trade-off: simplicidade vs qualidade da decisão
  - Pergunta: *Voting ou mediator para 3 especialistas com diagnóstico divergente?*
- **Diagrama**: 2 fluxos lado a lado
- **Tempo**: 2 min

---

#### Slide 51 — Convergência e Deadlock
- **Tipo**: Conteúdo
- **Objetivo**: Lidar com o risco de não convergir
- **Conteúdo**:
  - Convergência: acordo alcançado em N rounds
  - Deadlock: nenhum agente cede, loop infinito
  - Causas: estratégia rígida, sem BATNA, orgulho do agente
  - Mitigação: max_rounds, timeout, concessão forçada, escalar para mediator
  - Critério de sucesso do projeto: convergência em ≥ 80% dos casos
- **Diagrama**: Fluxo com branch de deadlock → timeout
- **Tempo**: 1.5 min

---

#### Slide 52 — Exemplo: Objetivos Parcialmente Conflitantes
- **Tipo**: Conteúdo
- **Objetivo**: Caso real de negociação com tensão
- **Conteúdo**:
  - Cenário: agente de velocidade (quer rápido) vs agente de qualidade (quer completo)
  - Negociação: trade-off entre tempo e profundidade
  - Solução: definir orçamento de tempo + threshold de qualidade mínima
  - Convergência: ambos aceitam um meio-termo documentado
  - Pergunta: *Como evitar que o agente de qualidade nunca aceite?*
- **Diagrama: Eixo tempo × qualidade com zona de acordo
- **Tempo**: 1.5 min

---

### SEÇÃO G — Protocolos e Padrões Emergentes (Slides 53-59 · 8 min)

---

#### Slide 53 — [SEÇÃO] Protocolos Emergentes
- **Tipo**: Seção
- **Objetivo**: Transição para padrões de comunicação
- **Conteúdo**: "6 — Protocolos e Padrões Emergentes"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 54 — A2A Protocol (Google, 2024)
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar o protocolo A2A do Google
- **Conteúdo**:
  - A2A (Agent-to-Agent) Protocol: padrão aberto para comunicação entre agentes
  - Objetivo: interoperabilidade entre agentes de diferentes frameworks
  - Agent Card: manifesto de capacidades do agente
  - Tasks: unidade de trabalho delegável entre agentes
  - Status: emerging spec (ainda em evolução)
- **Diagrama**: Agent Card + Task flow
- **Tempo**: 2 min

---

#### Slide 55 — A2A Protocol: Como Funciona
- **Tipo**: Diagrama
- **Objetivo**: Mostrar o fluxo do protocolo A2A
- **Conteúdo**:
  - 1. Agente A descobre Agent Card de B (via URL)
  - 2. A envia Task para B
  - 3. B processa e retorna status + resultado
  - 4. Streaming opcional para tarefas longas
  - Suporte a SSE (Server-Sent Events) para updates em tempo real
- **Diagrama**: Sequência de mensagens A2A
- **Animação**: Passos aparecem sequencialmente
- **Tempo**: 2 min

---

#### Slide 56 — MCP vs A2A
- **Tipo**: Comparação
- **Objetivo**: Esclarecer a relação entre MCP e A2A
- **Conteúdo**:
  - MCP (Model Context Protocol): agent ↔ system (tools, data sources)
  - A2A (Agent-to-Agent): agent ↔ agent (delegação, colaboração)
  - Complementares, não competidores!
  - Analogia: MCP = como o agente fala com ferramentas; A2A = como agentes falam entre si
  - Pergunta: *MCP e A2A são complementares ou competidores?*
- **Diagrama**: Diagrama Venn ou 2 eixos
- **Tempo**: 1.5 min

---

#### Slide 57 — Padrões de Orquestração Multi-Agente
- **Tipo**: Conteúdo
- **Objetivo**: Visão geral de orquestração
- **Conteúdo**:
  - Centralizada (supervisor/orchestrator): um agente coordena os demais
  - Descentralizada (peer-to-peer): agentes se coordenam sem líder
  - Hierárquica: supervisor → sub-supervisores → agentes
  - Market-based: agentes "licitam" tarefas
  - Trade-off: controle vs flexibilidade vs escalabilidade
- **Diagrama**: 4 mini-topologias
- **Tempo**: 1.5 min

---

#### Slide 58 — FIPA e Padrões Históricos
- **Tipo**: Conteúdo
- **Objetivo**: Contextualizar com padrões clássicos de multi-agente
- **Conteúdo**:
  - FIPA (Foundation for Intelligent Physical Agents): padrões de comunicação ACL
  - FIPA-ACL: performatives (request, inform, propose, accept, reject)
  - Aprendizado: LLM agents redescobrem conceitos de FIPA
  - KQML: predecessor de FIPA (anos 90)
  - Lição: muita coisa "nova" já foi pensada — aprender com o passado
- **Diagrama**: Timeline FIPA → KQML → A2A
- **Tempo**: 1.5 min

---

#### Slide 59 — Estado da Padronização
- **Tipo**: Conteúdo
- **Objetivo**: Ser honesto sobre a maturidade do ecossistema
- **Conteúdo**:
  - MCP: mais maduro (Anthropic, amplamente adotado)
  - A2A: emergente (Google, adoção crescente)
  - FIPA: maduro mas sub-adotado em LLM agents
  - Fragmentação: cada framework tem seu próprio protocolo
  - Tendência: convergência para MCP + A2A como camadas complementares
- **Diagrama**: Matriz de maturidade
- **Tempo**: 1.5 min

---

### SEÇÃO H — Fechamento (Slides 60-72 · 18 min)

---

#### Slide 60 — [SEÇÃO] Boas Práticas e Anti-Patterns
- **Tipo**: Seção
- **Objetivo**: Transição para o fechamento
- **Conteúdo**: "7 — Boas Práticas e Anti-Patterns"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 61 — Boas Práticas (DO)
- **Tipo**: Conteúdo
- **Objetivo**: Checklist de boas práticas em comunicação multi-agente
- **Conteúdo**:
  - Comece com 2 agentes antes de escalar para N
  - Defina schemas de mensagem com versionamento desde o dia 1
  - Use blackboard quando N é grande e contribuições são independentes
  - Defina max_rounds em negociações (evitar deadlock)
  - Logue todas as mensagens A2A (traces são seu debugging)
  - Isole agentes como atores (estado protegido)
  - Documente o protocolo de handoff/delegação explicitamente
- **Diagrama**: Checklist verde (etho-success)
- **Tempo**: 2 min

---

#### Slide 62 — Anti-Patterns (DON'T)
- **Tipo**: Conteúdo
- **Objetivo**: Checklist do que NÃO fazer
- **Conteúdo**:
  - Começar com group chat de 5 agentes sem necessidade
  - Sem schema de mensagem ("telefone sem fio")
  - Negociação sem max_rounds (deadlock infinito)
  - Shared state sem locks (race condition)
  - Actor model para tudo (overhead desnecessário em tarefas simples)
  - Não logar mensagens (debug cego em multi-agente)
  - Misturar MCP e A2A sem entender a diferença
  - Confiar que agentes "vão se entender" sem protocolo
- **Diagrama**: Checklist vermelho (etho-danger)
- **Tempo**: 2 min

---

#### Slide 63 — Caso de Estudo: MetaGPT
- **Tipo**: Diagrama
- **Objetivo**: Mostrar todos os conceitos em um caso real
- **Conteúdo**:
  - MetaGPT: framework multi-agente para desenvolvimento de software
  - Papéis: Product Manager → Architect → Engineer → QA
  - Comunicação via artefatos estruturados (não chat livre)
  - SOPs codificam o workflow: cada papel sabe o que esperar
  - Resultado: gera código funcional de ponta a ponta
  - Lição: estrutura > improvisação em sistemas multi-agente
- **Diagrama**: Pipeline MetaGPT com papéis e artefatos
- **Tempo**: 3 min

---

#### Slide 64 — Exercício: Schema de Mensagem A2A
- **Tipo**: Exercício
- **Objetivo**: Praticar o design de um schema de comunicação
- **Conteúdo**:
  - Cenário: agentes de compra e venda negociando preço
  - Em duplas: escrever schema JSON de mensagem com versionamento
  - Incluir: sender, receiver, message_type, payload, timestamp, version
  - Considerar: como representar proposta, contraproposta, aceitação
  - 3 min discussão, compartilhar no quadro
- **Diagrama**: Template de schema em branco
- **Tempo**: 4 min

---

#### Slide 65 — Resumo da Aula
- **Tipo**: Resumo
- **Objetivo**: Sintetizar os pontos-chave
- **Conteúdo**:
  - Espectro A2A: síncrono vs assíncrono, topologias, schemas, garantias
  - Padrões de conversação: CAMEL (2-agent), AutoGen (group), Swarm (handoff)
  - Blackboard: espaço compartilhado, baixo acoplamento, escala com N
  - Actor model: isolamento, concorrência sem locks, distribuição transparente
  - Negociação: bargaining, auction, voting, mediator, evitar deadlock
  - Protocolos: MCP (agent↔system) + A2A (agent↔agent) = complementares
  - MetaGPT: SOPs estruturados > chat livre
- **Diagrama**: 7 ícones com os pontos-chave
- **Tempo**: 2 min

---

#### Slide 66 — Checklist da Aula
- **Tipo**: Resumo
- **Objetivo**: Confirmar que todos os tópicos foram cobertos
- **Conteúdo**:
  - [ ] Definiu o espectro A2A (síncrono/assíncrono, topologias)
  - [ ] Apresentou schemas de mensagem com versionamento
  - [ ] Explicou 3 padrões de conversação (CAMEL, AutoGen, Swarm)
  - [ ] Demontrou blackboard vs mensagens diretas
  - [ ] Implementou actor model ou mostrou a demo
  - [ ] Discutiu negociação, conflito e deadlock
  - [ ] Comparou MCP vs A2A Protocol
- **Diagrama**: Checklist visual
- **Tempo**: 1 min

---

#### Slide 67 — Quiz: Pergunta 1
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "Quando blackboard é preferível a mensagens diretas?"
  - A) Quando há apenas 2 agentes
  - B) Quando N é grande e contribuições são independentes
  - C) Quando a ordem das mensagens é crítica
  - D) Quando o acoplamento entre agentes deve ser máximo
  - Resposta: B
- **Tempo**: 1 min

---

#### Slide 68 — Quiz: Pergunta 2
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "Qual é a diferença entre handoff (Swarm) e delegação (supervisor)?"
  - A) Handoff é síncrono, delegação é assíncrona
  - B) Handoff transfere controle (agente sai), delegação mantém supervisor
  - C) Handoff é para 2 agentes, delegação para N
  - D) Não há diferença
  - Resposta: B
- **Tempo**: 1 min

---

#### Slide 69 — Quiz: Pergunta 3
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "MCP e A2A Protocol são:"
  - A) Competidores — um substitui o outro
  - B) Complementares — MCP é agent↔system, A2A é agent↔agent
  - C) A mesma coisa com nomes diferentes
  - D) Ambos obsoletos
  - Resposta: B
- **Tempo**: 1 min

---

#### Slide 70 — Quiz: Pergunta 4
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "Verdadeiro ou falso: 'Actor model é mais lento que shared-state.'"
  - A) Verdadeiro — locks são mais rápidos
  - B) Falso — em alta concorrência, actor model escala melhor sem locks
  - C) Depende — sempre (contexto importa)
  - D) Impossível determinar sem benchmark
  - Resposta: B (com caveat: contexto importa, mas a afirmação geral é falsa)
- **Tempo**: 1 min

---

#### Slide 71 — Conexão com Próximos Módulos + Referências
- **Tipo**: Referências
- **Objetivo**: Mostrar conexões e indicar leitura
- **Conteúdo**:
  - ETHAGT10 — Padrões de Arquitetura Multi-Agente: topologias completas
  - ETHAGT11 — Event-Driven Agents: comunicação assíncrona em escala
  - ETHAGT15 — (depende deste módulo)
  - Leitura obrigatória:
    - Wu et al. *AutoGen* (arXiv:2308.08155)
    - Li et al. *CAMEL* (arXiv:2303.17760)
    - Hewitt, C. *Actor Model* (1973)
  - Recomendado: Google *A2A Protocol* spec; OpenAI Swarm (repo)
  - Survey: arXiv:2308.00352
- **Diagrama**: Mapa da especialização com ETHAGT09 destacado
- **Tempo**: 1.5 min

---

#### Slide 72 — Projeto, Labs e Q&A
- **Tipo**: Capa
- **Objetivo**: Apresentar projeto/labs e encerrar
- **Conteúdo**:
  - Projeto: sistema de negociação entre agentes (comprador/vendedor ou especialistas)
    - Entrega: código + traces + análise de convergência
    - Critério: convergência ≥ 80% + análise de falhas
  - Lab 1 (4h): "Duas arquiteturas, um problema" — AutoGen vs blackboard
  - Lab 2 (4h): "Actor model com handoffs" — swarm com transferência de controle
  - Próxima aula: ETHAGT10 — Padrões de Arquitetura Multi-Agente
  - "Perguntas?"
  - Contato do professor
- **Diagrama**: Logo Etho + fundo etho-dark
- **Tempo**: 2 min

---

## Resumo do Storyboard

| Seção | Slides | Tempo | Conteúdo |
|---|---|---|---|
| A — Abertura | 1-7 | 8 min | Capa, objetivos, competências, agenda, motivação, contexto |
| B — Espectro A2A | 8-15 | 10 min | Direta vs assíncrona, topologias, schemas, versionamento, erros, garantias |
| C — Padrões de Conversação | 16-26 | 13 min | CAMEL, AutoGen GroupChat, Swarm handoff, MetaGPT, exercício |
| D — Blackboard | 27-33 | 10 min | Espaço compartilhado, quando usar, vs mensagens, implementação |
| E — Actor Model | 34-44 | 13 min | Atores, encapsulamento, concorrência, Akka/Erlang, DEMO |
| F — Negociação e Conflito | 45-52 | 10 min | Bargaining, auction, voting, mediator, deadlock |
| G — Protocolos Emergentes | 53-59 | 8 min | A2A Protocol, MCP vs A2A, orquestração, FIPA, padronização |
| H — Fechamento | 60-72 | 18 min | Boas práticas, anti-patterns, MetaGPT, exercício, resumo, quiz, referências, Q&A |
| **Total** | **72** | **90 min** | |

---

## Diagramas Necessários

| # | Slide | Diagrama | Tipo | Fonte |
|---|---|---|---|---|
| D1 | 9 | Topologias (broadcast, P2P, pub/sub) | Grid 1x3 | Novo |
| D2 | 10 | Schema de mensagem A2A (JSON) | Código | Novo |
| D3 | 17 | 3 padrões de conversação | Grid 1x3 | Novo |
| D4 | 19 | CAMEL role-playing trace | Console | arXiv:2303.17760 |
| D5 | 20 | AutoGen GroupChat (hub-and-spoke) | Flowchart | arXiv:2308.08155 |
| D6 | 22 | Handoff (Swarm) | Flowchart | `12-Diagrams/ETHAGT09/handoff.mmd` |
| D7 | 24 | Pipeline MetaGPT (SOPs) | Pipeline | MetaGPT paper |
| D8 | 29 | Blackboard pattern | Flowchart | `12-Diagrams/ETHAGT09/blackboard.mmd` |
| D9 | 36 | Actor model | Flowchart | `12-Diagrams/ETHAGT09/actor-model.mmd` |
| D10 | 38 | Thread+lock vs Actor (comparação) | Comparação | Novo |
| D11 | 43 | DEMO: 2 arquiteturas lado a lado | Comparação | `05-Labs/ETHAGT09/Lab1-Duas-Arquiteturas` |
| D12 | 49 | Negociação (bargaining flow) | Flowchart | `12-Diagrams/ETHAGT09/negotiation.mmd` |
| D13 | 52 | Eixo tempo × qualidade (zona de acordo) | Gráfico | Novo |
| D14 | 55 | A2A Protocol (sequência) | Sequência | Google A2A spec |
| D15 | 56 | MCP vs A2A (Venn) | Venn | Novo |
| D16 | 57 | 4 topologias de orquestração | Grid 2x2 | Novo |
| D17 | 63 | MetaGPT caso de estudo | Pipeline | MetaGPT paper |
| D18 | 71 | Mapa da especialização | Mind map | Novo |

---

## Pontos de Engajamento

| # | Slide | Tipo | Interação |
|---|---|---|---|
| E1 | 5 | Pergunta aberta | "Quantos agentes colaborando antes de virar caos?" |
| E2 | 9 | Pergunta aberta | "Qual topologia para 10 agentes debatendo um diagnóstico?" |
| E3 | 14 | Pergunta aberta | "Qual garantia para transferência bancária entre agentes?" |
| E4 | 15 | Exercício rápido | 4 cenários — escolher topologia + garantia (votação) |
| E5 | 21 | Pergunta aberta | "Qual estratégia para 5 especialistas debatendo?" |
| E6 | 23 | Pergunta aberta | "Handoff ou delegação para suporte ao cliente?" |
| E7 | 26 | Exercício rápido | 4 cenários — escolher padrão de conversação (votação) |
| E8 | 30 | Pergunta aberta | "Quando blackboard é preferível a mensagens diretas?" |
| E9 | 33 | Exercício em duplas | 3 cenários — blackboard ou mensagens (2 min) |
| E10 | 37 | Pergunta aberta | "Actor model vs shared state — qual mais seguro?" |
| E11 | 42 | V/F | "Actor model é mais lento que shared-state." |
| E12 | 43-44 | DEMO + Discussão | Duas arquiteturas ao vivo + pergunta em duplas |
| E13 | 46 | Pergunta aberta | "O que acontece com objetivos parcialmente conflitantes?" |
| E14 | 50 | Pergunta aberta | "Voting ou mediator para diagnóstico divergente?" |
| E15 | 52 | Pergunta aberta | "Como evitar que agente de qualidade nunca aceite?" |
| E16 | 56 | Pergunta aberta | "MCP e A2A são complementares ou competidores?" |
| E17 | 64 | Exercício em duplas | Schema de mensagem A2A com versionamento (3 min) |
| E18 | 67-70 | Quiz (4 perguntas) | Verificação de compreensão |

---

## Pendências de Produção

- [ ] Produzir 10 diagramas novos (D1, D2, D3, D4, D5, D7, D10, D13, D14, D15, D16, D17, D18)
- [ ] Verificar diagramas existentes (D6, D8, D9, D12) — já em `12-Diagrams/ETHAGT09/`
- [ ] Screenshot do trace CAMEL (Slide 19)
- [ ] Screenshot do código da DEMO com syntax highlighting (Slide 43)
- [ ] Imagem de fundo para capa (Slide 1) — rede de agentes interconectados
- [ ] Badge de competências (Slide 3)
- [ ] Timeline de marcos históricos (Slide 6)
- [ ] Preparar código da DEMO: `05-Labs/ETHAGT09/Lab1-Duas-Arquiteturas`
- [ ] Template de schema JSON em branco para exercício (Slide 64)

---

> **Aguardando aprovação deste storyboard para gerar os slides detalhados com notas do professor.**
