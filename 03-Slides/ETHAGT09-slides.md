# ETHAGT09 — Comunicação e Coordenação Multi-Agente — Slides

> Apresentação para aula síncrona · ~50 min · 13 slides

## Estrutura da aula
- Abertura (5 min): gancho/motivação
- Teoria (25 min): conceitos principais com diagramas de referência
- Demonstração (10 min): código ao vivo ou walkthrough de lab
- Exercício (5 min): questão rápida ou discussão
- Fechamento (5 min): conexão com próximo módulo, leitura recomendada

## Slides

### Slide 1 — Título
- ETHAGT09 — Comunicação e Coordenação Multi-Agente (A2A · blackboard · actor model)
- Professor, data, Universität Etho
- Pré-requisito: ETHAGT04
- ~1 min

### Slide 2 — Agenda
1. O espectro da comunicação A2A
2. Padrões de conversação (two-agent, group, handoff)
3. Blackboard (espaço compartilhado)
4. Actor Model
5. Negociação e conflito
6. Protocolos emergentes (A2A Protocol, MCP vs A2A)
- ~1 min

### Slide 3 — Gancho / Motivação
- Problema: dois agentes precisam colaborar mas não têm protocolo de comunicação
- Exemplo: agente de pesquisa e agente de escrita precisam trocar informações — sem padrão, viram bagunça
- A solução: padrões de comunicação e coordenação
- Pergunta: *Quantos agentes colaborando antes de virar caos?*
- ~3 min

### Slide 4 — O Espectro da Comunicação A2A
- Direta (request/response) vs assíncrona (eventos)
- Broadcast vs p2p vs pub/sub
- Schemas de mensagem (estrutura, versão, campos obrigatórios)
- Erros: mensagens perdidas, duplicadas, fora de ordem
- Pergunta: *Como garantir que uma mensagem não se perdeu?*
- ~4 min

### Slide 5 — Padrões de Conversação
- Two-agent dialogue (estilo CAMEL): role-playing entre assistente e usuário simulado
- Group chat (estilo AutoGen GroupChat): round-robin, selector, dynamic
- Handoff / transfer (estilo OpenAI Swarm): agente passa controle para outro
- Quando cada padrão brilha
- Pergunta: *Handoff vs delegação (supervisor) — qual a diferença?*
- ~4 min

### Slide 6 — Blackboard
- Espaço compartilhado de estado: agentes escrevem e leem
- Quando brilha: problema dinâmico, múltiplos especialistas contribuem
- vs mensagens diretas: blackboard reduz acoplamento
- Implementação (em memória + persistente para resiliência)
- Diagrama: `12-Diagrams/ETHAGT09/blackboard.mmd`
- ~4 min

### Slide 7 — Actor Model
- Atores encapsulam estado; só se comunicam por mensagens
- Localização transparente; concorrência sem locks
- Akka / Erlang / asyncio actors
- Aplicação a agentes distribuídos (cada agente = um ator)
- Diagrama: `12-Diagrams/ETHAGT09/actor-model.mmd`
- Pergunta: *Actor model vs shared state — qual é mais seguro para dados críticos?*
- ~4 min

### Slide 8 — DEMO: Duas Arquiteturas, um Problema
- Código ao vivo: mesma tarefa (pesquisar + resumir + formatar)
- Versão 1: AutoGen-style group chat (agentes conversam)
- Versão 2: Blackboard (agentes compartilham espaço)
- Comparar: número de mensagens, tempo, acoplamento
- Referência: `05-Labs/ETHAGT09/Lab1-Duas-Arquiteturas`
- ~5 min

### Slide 9 — Negociação e Conflito
- Negociação entre agentes (Bargaining, Auction)
- Resolução de conflito (voting, mediator)
- Convergência e deadlock
- Exemplo: agentes com objetivos parcialmente conflitantes (ex: velocidade vs qualidade)
- Diagrama: `12-Diagrams/ETHAGT09/negotiation.mmd`
- ~3 min

### Slide 10 — Protocolos Emergentes
- A2A Protocol (Google, 2024): padrão para agentes se comunicarem
- MCP vs A2A: complementares (MCP = agent↔system, A2A = agent↔agent) ou competidores?
- Padrões de orquestração de workflow multi-agente
- Estado da padronização (ainda imaturo)
- ~3 min

### Slide 11 — Exercício: Schema de Mensagem A2A
- Cenário: agentes de compra e venda negociando preço
- Em duplas: escrever schema JSON de mensagem com versionamento
- Incluir: sender, receiver, message_type, payload, timestamp, version
- 3 min, compartilhar no quadro
- ~4 min

### Slide 12 — Conexão com Próximo Módulo
- ETHAGT10 — Padrões de Arquitetura Multi-Agente: topologias completas
- ETHAGT11 — Event-Driven Agents: comunicação assíncrona em escala
- Leitura: Wu et al. *AutoGen* (arXiv:2308.08155)
- Li et al. *CAMEL* (arXiv:2303.17760)
- Google *A2A Protocol* spec
- ~2 min

### Slide 13 — Referências
- Wu, Q. et al. *AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation* (arXiv:2308.08155)
- Li, G. et al. *CAMEL: Communicative Agents for Mind Exploration* (arXiv:2303.17760)
- Hewitt, C. *Actor Model* (1973)
- OpenAI Swarm (repo)
- Google *A2A Protocol* spec
- ~1 min
