# ETHAGT10 — Padrões de Arquitetura Multi-Agente — Slides

> Apresentação para aula síncrona · ~50 min · 14 slides

## Estrutura da aula
- Abertura (5 min): gancho/motivação
- Teoria (25 min): conceitos principais com diagramas de referência
- Demonstração (10 min): código ao vivo ou walkthrough de lab
- Exercício (5 min): questão rápida ou discussão
- Fechamento (5 min): conexão com próximo módulo, leitura recomendada

## Slides

### Slide 1 — Título
- ETHAGT10 — Padrões de Arquitetura Multi-Agente (topologias)
- Professor, data, Universität Etho
- Pré-requisito: ETHAGT09
- ~1 min

### Slide 2 — Agenda
1. Catálogo das 12 topologias
2. Supervisor e Hierarchical
3. Swarm e handoffs
4. Pipeline e Orchestrator-Workers
5. Event-Driven e Actor Model
6. Tree, Recursive, Mesh
7. Escolha e ADR
- ~1 min

### Slide 3 — Gancho / Motivação
- Problema: equipe escolhe topologia sem critério — "vamos de supervisor" por default
- Exemplo: sistema de revisão de PR com 3 especialistas — supervisor funciona, mas swarm talvez seja mais simples
- A solução: catálogo de topologias + matriz de decisão
- Pergunta: *Qual foi a topologia mais comum que vocês já usaram em projetos?*
- ~3 min

### Slide 4 — Catálogo das 12 Topologias
- Visão geral: Single Agent, Supervisor, Hierarchical, Blackboard, Actor Model, Pipeline, Event-Driven, Swarm, Tree of Agents, Recursive, Agent Mesh, Hybrid
- Para cada: descrição em 1 linha, when-to-use, when-to-avoid
- Diagramas de cada topologia em `12-Diagrams/ETHAGT10/`
- ~5 min

### Slide 5 — Supervisor e Hierarchical
- Supervisor pattern (LangGraph): supervisor como roteador com tool calls
- Hierarchical: árvore de supervisor → workers → sub-workers
- Quando escalar hierarquia (3 níveis) vs flat
- Casos de falha: supervisor gargalo, workers redundantes
- Pergunta: *Em quantos níveis de hierarquia o supervisor se torna gargalo?*
- ~4 min

### Slide 6 — Swarm e Handoffs
- OpenAI Swarm: agentes leves com transferência de controle
- Quando transfer é melhor que roteamento central
- Limites: coordenação complexa, estado compartilhado
- Diagrama: `12-Diagrams/ETHAGT10/swarm-topology.mmd` (referência)
- ~3 min

### Slide 7 — Pipeline e Orchestrator-Workers
- Pipeline fixo vs dinâmico
- Orchestrator-Workers revisitado em multi-agente (ETHAGT03 + agentes)
- Composição com hierarchical (workers que são supervisores de sub-workers)
- ~3 min

### Slide 8 — Event-Driven e Actor Model
- Event-driven em multi-agente (preview; profundidade em ETHAGT11)
- Actor model como fundação de escalabilidade (cada agente = ator)
- Mesh de agentes: topologia flat peer-to-peer
- Pergunta: *Mesh vs Hierarchical — quando preferir um ao outro?*
- ~3 min

### Slide 9 — Tree, Recursive, Mesh
- Tree of Agents (LATS em sistema multi-agente)
- Recursive: meta-agentes que instanciam sub-agentes
- Agent Mesh: topologia flat peer-to-peer sem central
- Discussão: *Recursive é sempre anti-pattern? Quando não?*
- ~3 min

### Slide 10 — DEMO: Hierarchical Teams
- Código ao vivo: supervisor + 2 workers (pesquisa + escrita) + sub-worker (formatação)
- Mostrar fluxo: supervisor recebe tarefa → delega → workers devolvem → supervisor sintetiza
- Trace mostrando cada nível
- Referência: `05-Labs/ETHAGT10/Lab1-Hierarchical-Teams`
- ~5 min

### Slide 11 — Escolha e ADR
- Matriz de decisão: consistência × latência × custo × flexibilidade
- Estrutura de ADR de topologia (contexto, decisão, consequências)
- Sinais de evolução: quando a topologia precisa mudar
- Exercício: *Escreva o esqueleto de um ADR para um cenário dado*
- ~4 min

### Slide 12 — Exercício: Topologia para 6 Cenários
- Cenários projetados:
  1. Chatbot de suporte com escalonamento humano
  2. Sistema de revisão de código com 3 especialistas
  3. Pipeline de geração de relatório financeiro
  4. Simulação de mercado com múltiplos agentes
  5. Assistente pessoal multi-função
  6. Sistema de pesquisa autônoma
- Em grupos: propor topologia + justificar em 2 frases
- ~4 min

### Slide 13 — Conexão com Próximo Módulo
- ETHAGT11 — Event-Driven Agents: orquestração assíncrona
- ETHAGT14 — Escalabilidade: topologias em produção
- ETHAGT15 — Meta-Agentes: recursive e auto-aprendizado
- Leitura: Hong et al. *MetaGPT* (arXiv:2308.00352)
- LangGraph *Multi-Agent* examples
- ~2 min

### Slide 14 — Referências
- Hong, S. et al. *MetaGPT: Meta Programming for Multi-Agent Collaborative Framework* (arXiv:2308.00352)
- LangGraph *Multi-Agent* examples (hierarchical_agent_teams)
- OpenAI Swarm (repo, 2024)
- Chen, W. et al. *AgentVerse* (arXiv:2308.10848)
- Microsoft AutoGen docs
- ~1 min
