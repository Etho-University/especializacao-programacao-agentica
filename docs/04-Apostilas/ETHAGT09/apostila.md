# ETHAGT09 — Comunicação e Coordenação Multi-Agente

> **Apostila do curso** · Especialização em Programação Agêntica · Universidade Etho
> Fase C — Multi-Agentes, Ferramentas e Orquestração · Carga 25 h · Versão 1.0 · Julho 2026
> *Material de referência duradouro (nível pós-graduação lato sensu). Os slides são auxiliares.*

---

## Sumário

- **Capítulo 1** — O espectro da comunicação A2A
- **Capítulo 2** — Padrões de conversação
- **Capítulo 3** — Blackboard
- **Capítulo 4** — Actor Model
- **Capítulo 5** — Negociação e conflito
- **Capítulo 6** — Protocolos e padrões emergentes (A2A)
- **Capítulo 7** — Casos de estudo
- **Capítulo 8** — Referências e leituras

---

## Capítulo 1 — O espectro da comunicação A2A

### 1.1 Do agente isolado ao sistema de agentes

Até aqui, tratamos o agente como uma entidade *isolada*: um Augmented LLM em loop (ETHAGT01). Este módulo abre a **Fase C**, onde o foco muda do agente individual para os **sistemas de agentes** — múltiplos agentes que colaboram, coordenam e, às vezes, competem. A tese é que muitas tarefas são melhores resolvidas por *vários agentes especializados cooperando* do que por um único agente generalista, exatamente como uma equipe de especialistas supera um generalista em problemas complexos.

Mas cooperação exige **comunicação** — e comunicação entre agentes (Agent-to-Agent, A2A) é um problema de engenharia não-trivial. Este módulo trata os *modelos* de comunicação; ETHAGT10 trata as *topologias* (como os agentes se organizam); ETHAGT11 trata a *orquestração* (como o sistema roda em produção).

### 1.2 A taxonomia unificada: Collaboration

Na taxonomia de ETHAGT01, *Collaboration* era o sexto bloco. Agora ele ganha centro: a colaboração é definida por *como* os agentes trocam informação e *como* coordenam suas ações. Organizamos os modelos de comunicação em dois eixos:

| Eixo | Pólo A | Pólo B |
|---|---|---|
| **Acoplamento temporal** | Síncrono (request/response, esperam-se) | Assíncrono (eventos, não bloqueante) |
| **Topologia de mensagem** | Direta (p2p, um-para-um) | Compartilhada (blackboard, pub/sub) |

Cada modelo que veremos ocupa uma posição nesse espaço.

### 1.3 Schemas de mensagem: a importância da estrutura

A2A sem estrutura é caos: agentes "conversam" em texto livre, mal-interpretam-se, quebram contratos. A regra, ecoando ETHAGT02 (ACI), é tratar a comunicação A2A como uma **API** — com *schemas* explícitos. Uma mensagem A2A bem desenhada tem:

- **Tipo/ação:** o que esta mensagem *faz* (pergunta, resposta, delegação, resultado).
- **Payload estruturado:** o conteúdo, tipado (não texto livre).
- **Metadados:** remetente, destinatário, timestamp, correlation id (para rastrear conversas).
- **Versão:** para evoluir o protocolo sem quebrar agentes existentes.

```python
class AgentMessage(BaseModel):
    version: str = "1.0"
    msg_type: Literal["query", "response", "delegate", "result"]
    from_agent: str
    to_agent: str
    correlation_id: str
    payload: dict
```

### 1.4 Erros de comunicação

A comunicação A2A herda todos os modos de falha da comunicação distribuída: mensagens *perdidas* (rede falha), *duplicadas* (retry reenvia), *fora de ordem* (chegam trocadas), *entregues a destino errado* (roteamento errado). Um sistema multi-agente robusto precisa tratar esses casos — não assumir entrega perfeita. ETHAGT11 aprofunda resiliência; aqui registramos que *assumir comunicação confiável é o primeiro bug*.

---

## Capítulo 2 — Padrões de conversação

Como os agentes *conversam*? Há padrões recorrentes na literatura, cada com seus trade-offs.

### 2.1 Two-agent dialogue (estilo CAMEL)

O padrão mais simples: dois agentes com papéis complementares dialogam até completar a tarefa. O paper *CAMEL* (Li et al., *Communicative Agents for Mind Exploration*, arXiv:2303.17760) popularizou o "role-playing" entre agentes: um agente-usuário dá instruções, um agente-assistente executa, e eles refinam juntos. Esse padrão é bom para *brainstorming* e tarefas onde a troca iterativa melhora o resultado.

### 2.2 Group chat (estilo AutoGen)

O *AutoGen* (Wu et al., arXiv:2308.08155) introduz o **group chat**: múltiplos agentes num "canal" compartilhado, onde um seleciona quem fala a seguir. Há estratégias de seleção:

- **Round-robin:** cada um fala na ordem (justo, mas rígido).
- **Selector (LLM):** um agente (ou o próprio LLM) decide quem fala a seguir, com base no estado (flexível, mas custa uma chamada).
- **Dynamic:** qualquer agente pode "intervir" quando tem algo a dizer.

O group chat é poderoso para *debate* e *síntese multi-perspectiva*, mas pode divergir (conversa sem foco) e é caro (muitas chamadas).

> **Diagrama de referência:** [`12-Diagrams/ETHAGT09/handoff.mmd`](../../12-Diagrams/ETHAGT09/handoff.mmd).

### 2.3 Handoff / transfer (estilo OpenAI Swarm)

O **OpenAI Swarm** (2024) introduz um modelo elegante: agentes leves que podem *transferir* o controle uns aos outros. Quando um agente percebe que a tarefa saiu do seu escopo, ele faz um *handoff* — passa o controle (com o contexto) para o agente apropriado. Diferente do roteamento central (supervisor), a transferência é *peer-to-peer*: o agente decide para quem passar.

```
   agente A (triagem) ──handoff──► agente B (técnico) ──handoff──► agente C (fecha)
```

O handoff é bom para fluxos onde a *especialidade* muda ao longo da tarefa, e onde a decisão de "quem continua" é local (o agente atual sabe melhor). O limite: coordenação complexa (muitos agentes, dependências) fica confusa sem um coordenador central.

### 2.4 Supervisor vs handoff vs group chat

| Padrão | Decisão de "quem age" | Custo | Adequação |
|---|---|---|---|
| **Supervisor** | Central (um roteador) | +1 chamada de roteamento | Controle, previsibilidade |
| **Handoff** | Local (agente atual decide) | Embutida no agente | Especialidade muda, P2P |
| **Group chat** | Selector | +N chamadas de seleção | Debate, multi-perspectiva |

Não há "melhor" — a escolha depende de *onde* a decisão de coordenação deve morrer.

---

## Capítulo 3 — Blackboard

### 3.1 Espaço compartilhado de estado

O padrão **blackboard** (quadro-negro) abandona a mensagem direta: em vez de agentes se enviarem mensagens uns aos outros, eles *escrevem e leem num espaço compartilhado* — o blackboard. Cada agente contribui com o que sabe, lê o que os outros escreveram, e age quando vê oportunidade. A coordenação é *pelo estado compartilhado*, não por mensagens endereçadas.

> **Diagrama de referência:** [`12-Diagrams/ETHAGT09/blackboard.mmd`](../../12-Diagrams/ETHAGT09/blackboard.mmd).

```
          ┌──────────── BLACKBOARD (estado compartilhado) ───────────┐
          │  hipótese: "X" · evidência: [e1, e2] · próxima ação: "?" │
          └───▲───────────▲───────────▲───────────▲──────────────────┘
              │           │           │           │
         agente A    agente B    agente C    agente D  (especialistas)
```

### 3.2 Quando o blackboard brilha

- **Problema dinâmico** onde a contribuição de cada especialista depende do estado acumulado (ex.: diagnóstico médico — cada especialista adiciona achados).
- **Contribuintes variáveis** — agentes entram e saem conforme têm algo a dizer.
- **Necessidade de visão global** — todos veem o mesmo estado compartilhado.

### 3.3 Blackboard vs mensagens diretas

| | Blackboard | Mensagens diretas |
|---|---|---|
| Acoplamento | Baixo (agentes não se conhecem) | Alto (agentes conhecem-se) |
| Visão | Global (estado compartilhado) | Local (só o que recebem) |
| Concorrência | Agentes leem/escrevem o mesmo estado | Cada um tem seu estado |
| Complexidade | Sincronização do estado compartilhado | Roteamento de mensagens |

O blackboard troca *complexidade de roteamento* por *complexidade de sincronização* — é melhor quando o roteamento seria caótico (muitos agentes, padrões de interação imprevisíveis).

### 3.4 Implementação

O blackboard pode ser *em memória* (para uma sessão) ou *persistente* (um banco/KV store compartilhado). A implementação precisa resolver concorrência (quem escreve quando?) — frequentemente com locks, filas de contribuição ou um *controlador* que serializa escritas.

---

## Capítulo 4 — Actor Model

### 4.1 Atores encapsulam estado

O **Actor Model** (Hewitt, 1973) é um modelo de computação concorrente onde o universo é composto de *atores*: entidades que encapsulam *estado privado* e só interagem por *troca assíncrona de mensagens*. Não há estado compartilhado; não há locks; cada ator processa uma mensagem por vez. Esse modelo, originado nos anos 70 (Erlang, Akka), mapeia-se com naturalidade elegante para agentes distribuídos.

> **Diagrama de referência:** [`12-Diagrams/ETHAGT09/actor-model.mmd`](../../12-Diagrams/ETHAGT09/actor-model.mmd).

### 4.2 Propriedades

- **Encapsulamento:** o estado do ator é privado; só mensagens o alteram. Isso elimina *race conditions* no estado do ator.
- **Localização transparente:** um ator pode estar no mesmo processo ou do outro lado do mundo — a comunicação é a mesma (envia mensagem). Isso torna a distribuição trivial conceitualmente.
- **Concorrência sem locks:** como cada ator processa uma mensagem por vez, não há contenção no estado; a concorrência é *entre* atores, não *dentro* deles.

### 4.3 Aplicação a agentes distribuídos

Mapear cada agente para um ator dá-nos, de graça, isolamento, concorrência segura e distribuição. Frameworks como **Akka** (JVM), o modelo de concorrência de **Erlang/Elixir**, e abstrações sobre **asyncio** em Python implementam esse modelo. Para agentes que rodam em múltiplos processos/máquinas (ETHAGT14), o actor model é uma fundação sólida.

### 4.4 "Actor model é mais lento que shared-state?"

Não necessariamente. O overhead de passagem de mensagem existe, mas a *ausência de locks* e o paralelismo natural compensam em sistemas com muita concorrência. O trade-off real é de *complexidade de raciocínio*: o actor model é mais fácil de raciocinar (sem race conditions) mas mais verboso (tudo é mensagem).

---

## Capítulo 5 — Negociação e conflito

### 5.1 Quando agentes não concordam

Nem toda colaboração é harmoniosa. Agentes podem ter *objetivos parcialmente conflitantes* (comprador quer preço baixo, vendedor quer alto) ou *visões diferentes* (especialistas discordam sobre um diagnóstico). Precisamos de mecanismos de **negociação** e **resolução de conflito**.

> **Diagrama de referência:** [`12-Diagrams/ETHAGT09/negotiation.mmd`](../../12-Diagrams/ETHAGT09/negotiation.mmd).

### 5.2 Bargaining e auction

- **Bargaining (negociação):** agentes fazem propostas e contrapropostas, convergindo (ou não) para um acordo. Modelos clássicos de teoria dos jogos se aplicam.
- **Auction (leilão):** um recurso/tarefa é alocado ao agente que mais "valoriza" — por um mecanismo de leilão (inglês, holandês, Vickrey).

Esses mecanismos são úteis quando há *competição* por recursos ou quando múltiplos agentes podem fazer a tarefa e escolhe-se o melhor.

### 5.3 Resolução de conflito

Quando especialistas discordam:

- **Voting:** cada um vota; a maioria vence (simples, mas ignora intensidade/confiança).
- **Mediator:** um agente (ou humano) arbitra, ponderando os argumentos.
- **Weighted:** votos ponderados por confiança/expertise de cada agente.

### 5.4 Convergência e deadlock

O risco da negociação é o **deadlock**: agentes insistem em posições incompatíveis e o sistema nunca converge. Defesas: limite de rodadas (depois do qual, escalonar para humano ou aceitar o melhor parcial), concessões forçadas (agentes instruídos a ceder após N rodadas), e critérios de desempate determinísticos.

---

## Capítulo 6 — Protocolos e padrões emergentes (A2A)

### 6.1 A2A Protocol (Google, 2025)

Assim como o MCP (ETHAGT08) padroniza a comunicação agente↔ferramenta, o **A2A Protocol** (Google, 2025) visa padronizar a comunicação **agente↔agente** — um padrão aberto para que agentes de diferentes provedores/frameworks interajam. O ecossistema está em formação.

### 6.2 MCP vs A2A: complementares

Uma confusão comum: MCP e A2A competem? **Não — são complementares.** MCP padroniza como um agente *usa ferramentas* (vertical: agente→sistema). A2A padroniza como agentes *conversam entre si* (horizontal: agente→agente). Um sistema pode usar ambos: agentes que se coordenam via A2A, cada um usando ferramentas via MCP.

### 6.3 Estado da padronização

A padronização A2A ainda é incipiente (2025-2026). Frameworks (AutoGen, LangGraph, CrewAI) têm seus próprios formatos de mensagem. A expectativa é que o A2A Protocol consolide isso, como o MCP fez para ferramentas — mas é cedo para tratar qualquer padrão como definitivo. Acompanhe a evolução.

---

## Capítulo 7 — Casos de estudo

### 7.1 MetaGPT: software house multi-agente

O **MetaGPT** (Hong et al., ICLR 2024; arXiv:2308.00352) é o caso canônico de coordenação multi-agente: simula uma *software house* com agentes-papéis (product manager, arquiteto, engenheiro, QA) que colaboram via *SOPs* (Standard Operating Procedures) estruturadas. A lição: a coordenação não emerge sozinha do "conversem livremente" — ela emerge de *estrutura* (papéis, protocolos, artifacts compartilhados). Sem estrutura, o group chat divaga; com estrutura, converge.

> **Leitura.** Detalhes em [`09-CaseStudies/`](../../09-CaseStudies/).

### 7.2 Lições transversais

1. **Estrutura vence caos.** Papéis, schemas de mensagem e protocolos são o que torna a colaboração multi-agente confiável.
2. **O modelo de comunicação é uma decisão de arquitetura.** Direta vs blackboard vs actor — escolha pelo problema.
3. **Padrões emergentes (A2A) vão consolidar o espaço.** Acompanhe, mas não dependa de imaturidade.

---

## Capítulo 8 — Referências e leituras

### 8.1 Bibliografia fundamental

- **Wu, Q. et al.** *AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation.* arXiv:2308.08155, 2023. 🏛
- **Li, G. et al.** *CAMEL: Communicative Agents for Mind Exploration.* arXiv:2303.17760, 2023. 🏛
- **Hong, S. et al.** *MetaGPT.* ICLR 2024. arXiv:2308.00352. 🏛
- **Hewitt, C.** *Actor Model.* 1973. 🏛 (clássico)

### 8.2 Bibliografia complementar

- **OpenAI Swarm** (repo + paper técnico, 2024) — handoffs.
- **Google.** *A2A Protocol.* 2025.
- **Chen, W. et al.** *AgentVerse.* arXiv:2308.10848.
- **Guo, T. et al.** *LLM-based Multi-Agents: A Survey.* arXiv:2402.01680.

### 8.3 Recursos práticos

- **LangGraph** `examples/multi_agent/` (hierarchical_agent_teams, multi-agent-collaboration).
- **Akka / Erlang** docs (actor model); **CrewAI** (role-based).

### 8.4 Ficha de pesquisa

Fontes em [`20-Research/ETHAGT09-pesquisa.md`](../../20-Research/ETHAGT09-pesquisa.md). Última consulta: Julho 2026.

---

## Síntese do módulo

Ao concluir ETHAGT09, você deve ser capaz de:

1. **Distinguir** modelos de comunicação A2A (síncrono/assíncrono, direta/compartilhada) e escolher pelo problema.
2. **Implementar** troca estruturada de mensagens (schemas versionados).
3. **Aplicar** blackboard, actor model e padrões de conversação (dialogue, group chat, handoff).
4. **Lidar** com negociação, conflito e deadlock.
5. **Posicionar** MCP e A2A como complementares.

Próximos passos: ETHAGT10 transforma esses modelos de comunicação em *topologias* de sistema; ETHAGT11 leva a coordenação à produção (event-driven, durable execution).

---

*Mantido por: Escola de Tecnologia — Universidade Etho · Área de Inteligência Artificial · Versão 1.0 · Julho 2026*
