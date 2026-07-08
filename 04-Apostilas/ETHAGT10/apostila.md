# ETHAGT10 — Padrões de Arquitetura Multi-Agente

> **Apostila do curso** · Especialização em Programação Agêntica · Universidade Etho
> Fase C — Multi-Agentes, Ferramentas e Orquestração · Carga 30 h · Versão 1.0 · Julho 2026
> *Material de referência duradouro (nível pós-graduação lato sensu). Os slides são auxiliares.*

---

## Sumário

- **Capítulo 1** — Catálogo de topologias
- **Capítulo 2** — Supervisor e Hierarchical
- **Capítulo 3** — Swarm e handoffs
- **Capítulo 4** — Pipeline e Orchestrator-Workers
- **Capítulo 5** — Event-Driven e Actor Model
- **Capítulo 6** — Tree, Recursive e Mesh
- **Capítulo 7** — Escolha e ADR de topologia
- **Capítulo 8** — Casos de estudo
- **Capítulo 9** — Referências e leituras

---

## Capítulo 1 — Catálogo de topologias

### 1.1 Topologia: como os agentes se organizam

ETHAGT09 tratou *como* os agentes comunicam; este módulo trata *como eles se organizam* — a **topologia** do sistema. A topologia é a decisão arquitetural mais importante de um sistema multi-agente: ela determina fluxo de controle, pontos de falha, escalabilidade e custo. Escolher mal a topologia é um erro caro que se manifesta como gargalos, deadlocks ou complexidade incontrolável.

> **Biblioteca de referência:** [`10-Architecture/architectures/catalog.md`](../../10-Architecture/architectures/catalog.md) documenta as 12 topologias com when-to-use/when-to-avoid.

### 1.2 As 12 topologias

| # | Topologia | Característica |
|---|---|---|
| 1 | **Single Agent** | Um agente (baseline; não é multi-agente) |
| 2 | **Supervisor** | Um roteador central delega a workers |
| 3 | **Hierarchical** | Árvore de supervisores → workers → sub-workers |
| 4 | **Blackboard** | Estado compartilhado, especialistas contribuem |
| 5 | **Actor Model** | Atores isolados, mensagens assíncronas |
| 6 | **Pipeline** | Sequência fixa de agentes (cada um transforma) |
| 7 | **Event-Driven** | Agentes reagem a eventos (desacoplados) |
| 8 | **Swarm** | Agentes leves, handoffs peer-to-peer |
| 9 | **Tree of Agents** | Exploração em árvore (estilo ToT/LATS) |
| 10 | **Recursive** | Agentes que criam agentes (meta) |
| 11 | **Agent Mesh** | Topologia flat peer-to-peer, todos conectados |
| 12 | **Hybrid** | Combinação das anteriores |

Este módulo aprofunda as 6 mais usadas (Supervisor, Hierarchical, Swarm, Pipeline, Event-Driven, Mesh); as demais são apresentadas no catálogo e aprofundadas conforme necessário em módulos seguintes.

### 1.3 A hierarquia conceitual do repositório

Vale reiterar a distinção do repositório (que evita confusão recorrente):

- **`10-Architecture` (aqui):** topologias de **sistema inteiro** — como os agentes se organizam.
- **`11-AgentPatterns`:** papéis **individuais** de agentes (supervisor, planner, critic...).
- **`13-Workflows`:** composições controladas (LLMs em caminhos predefinidos).

> **Hierarquia:** padrões *compõem* arquiteturas; workflows são *casos simples* de arquiteturas.

---

## Capítulo 2 — Supervisor e Hierarchical

### 2.1 Supervisor pattern

O **Supervisor** (popularizado pelo LangGraph) é a topologia multi-agente mais comum: um agente *supervisor* atua como roteador central — recebe a tarefa, decide qual *worker* (especialista) deve tratá-la, delega, e sintetiza o resultado. O supervisor é, essencialmente, o padrão *orchestrator-workers* (ETHAGT03 §5) instanciado com agentes.

```
                 [supervisor (roteador)]
                /        |         \
        [worker A]  [worker B]  [worker C]
```

O supervisor decide a delegação *via tool calls* — cada worker é exposto como uma ferramenta, e o supervisor (um LLM) escolhe qual "chamar". Isso reúne os mundos de ETHAGT02 (tool calling) e ETHAGT09 (coordenação).

### 2.2 Quando usar Supervisor

- A tarefa se decompõe em *especialidades* claras, e um roteador central sabe qual aplicar.
- Você quer *controle e previsibilidade* (o supervisor é um ponto de decisão único e auditável).
- O número de workers é *moderado* (o supervisor consegue escolher entre eles).

### 2.3 Hierarchical

O **Hierarchical** generaliza o supervisor em *árvore*: supervisores delegam a workers, que podem ser *sub-supervisores* que delegam a sub-workers, e assim por diante. Isso escala o padrão supervisor para sistemas grandes, decompondo a decisão em níveis.

```
            [supervisor geral]
             /              \
     [sup. técnico]    [sup. negócio]
       /     \            /     \
    [w1]   [w2]       [w3]    [w4]
```

### 2.4 Quando escalar hierarquia vs flat

A escalada de hierarquia (3+ níveis) vale quando o número de agentes cresce a ponto de um supervisor único não consegue escolher entre todos (degradação por escala, ETHAGT02 §1.5). A hierarquia *divide* a decisão: cada supervisor cuida de poucos. O custo: mais chamadas de roteamento e potencial de *gargalo* nos supervisores superiores.

### 2.5 Casos de falha

- **Supervisor gargalo:** se todo fluxo passa por um supervisor sobrecarregado, ele vira ponto de contenção. Mitigação: paralelizar workers, hierarquizar.
- **Workers redundantes:** dois workers com escopos sobrepostos confundem o supervisor (mesmo anti-pattern de ETHAGT02 §5.2, agora entre agentes). Mitigação: fronteiras claras entre workers.

---

## Capítulo 3 — Swarm e handoffs

### 3.1 Swarm: agentes leves com transfer

O **Swarm** (OpenAI, 2024) propõe uma topologia diferente: agentes *leves* (stateless entre turnos) que se *transferem* o controle por handoffs (ETHAGT09 §2.3). Não há supervisor central; a decisão de "quem continua" é *local* — o agente atual decide para quem passar a tarefa.

### 3.2 Quando transfer é melhor que roteamento central

- A *especialidade muda ao longo da tarefa* e o agente atual é quem melhor sabe para quem passar.
- Você quer *menos overhead* (sem chamada extra de supervisor).
- A coordenação é *linear* (a tarefa flui de especialista em especialista).

### 3.3 Limites do swarm

O swarm degrada quando a coordenação é *complexa* (muitos agentes com dependências, need de visão global). Sem um coordenador, os handoffs podem ficar confusos ("ninguém sabe quem está no comando"). Para esses casos, Supervisor/Hierarchical são mais previsíveis.

---

## Capítulo 4 — Pipeline e Orchestrator-Workers

### 4.1 Pipeline

O **Pipeline** é a topologia mais simples: uma sequência *fixa* de agentes, onde cada um transforma a saída do anterior. É, essencialmente, o *prompt chaining* (ETHAGT03 §2) com agentes especializados em cada etapa.

```
   [agente 1: extrai] ──► [agente 2: enriquece] ──► [agente 3: valida] ──► output
```

Use quando o *fluxo é fixo e conhecido* e cada etapa tem especialista próprio. O custo/previsibilidade são os melhores (fluxo determinístico); a flexibilidade é a pior.

### 4.2 Orchestrator-Workers revisitado

Já vimos o orchestrator-workers como workflow (ETHAGT03 §5) e como supervisor (§2.1 aqui). Em multi-agente, a distinção relevante: o *orchestrator* é um agente que *planeja dinamicamente* quais workers chamar, enquanto o *supervisor* é mais um *roteador*. A fronteira é tênue; o ponto é que a decomposição pode ser estática (pipeline), dinâmica-por-roteador (supervisor) ou dinâmica-por-planejamento (orchestrator).

---

## Capítulo 5 — Event-Driven e Actor Model

### 5.1 Event-Driven (preview; profundidade em ETHAGT11)

Na topologia **Event-Driven**, agentes não se chamam diretamente — eles *publicam* e *consomem eventos*. Um evento ("novo documento") dispara agentes que reagem ("classificar", "indexar", "notificar"). Isso *desacopla* os agentes: quem publica não precisa saber quem consome.

```
   [produtor] ──evento──► (barramento) ──► [consumidor A], [consumidor B]
```

O event-driven brilha em *escala e resiliência* (produtores e consumidores independentes, tolerantes a falhas) e em sistemas com *muitos agentes reagindo a mudanças*. O custo é *complexidade* (debugar fluxos assíncronos é difícil). ETHAGT11 é dedicado a essa topologia.

### 5.2 Actor Model como fundação de escala

O **Actor Model** (ETHAGT09 §4), como topologia, estrutura cada agente como um ator isolado comunicando por mensagens. É a fundação natural para *agentes distribuídos* em múltiplas máquinas (ETHAGT14): isolamento, concorrência sem locks, localização transparente.

### 5.3 Mesh de agentes

O **Agent Mesh** é a topologia *flat peer-to-peer*: todos os agentes podem falar com todos, sem hierarquia. É a mais flexível e a mais caótica — sem coordenação, o mesh tende ao ruído. Funciona em sistemas pequenos e altamente cooperativos; escala mal sem protocolos fortes de coordenação.

---

## Capítulo 6 — Tree, Recursive e Mesh

### 6.1 Tree of Agents

A **Tree of Agents** estrutura a execução como uma *árvore de exploração*: o agente-raiz decompõe, os filhos exploram ramos, avalia-se e poda. É a topologia correspondente às estratégias de raciocínio ToT/LATS (ETHAGT04 §4) elevadas a sistema. Útil quando há *busca* e *avaliação de alternativas*; caro (muitos agentes/nós).

### 6.2 Recursive (meta-agentes)

A topologia **Recursive** contém agentes que *criam outros agentes* — meta-agentes. Um agente, ao perceber uma sub-tarefa recorrente, gera um sub-agente especializado para ela. Isso é a fronteira da auto-organização, aprofundada em ETHAGT15. Como toda recursão sem base-case, corre o risco de *explosão* (agentes criando agentes infinitamente) — precisa de cercas.

### 6.3 Quando recursive é anti-pattern

A recursão é sedutora mas perigosa: sem limites rígidos (orçamento de agentes, profundidade máxima, critério de parada), o sistema explode em complexidade e custo. Use recursão só quando a *auto-criação* traz valor mensurável — não como exercício de elegância.

### 6.4 Hybrid

A maioria dos sistemas reais é **Hybrid**: combina topologias (ex.: supervisor no topo, event-driven entre workers, um sub-sistema swarm). A topologia híbrida é a mais realista e a mais difícil de justificar — exige ADR (Capítulo 7) que explique *por que cada parte usa a topologia que usa*.

---

## Capítulo 7 — Escolha e ADR de topologia

### 7.1 Matriz de decisão

A escolha de topologia deve ser guiada por requisitos explícitos, não por preferência. As dimensões:

| Requisito | Favorece |
|---|---|
| Previsibilidade / controle | Supervisor, Pipeline |
| Flexibilidade / adaptação | Swarm, Orchestrator |
| Escala / distribuição | Event-Driven, Actor, Mesh |
| Visão global / coordenação | Supervisor, Blackboard |
| Especialidade linear | Pipeline, Swarm (handoffs) |
| Busca / alternativas | Tree of Agents |

### 7.2 O ADR de topologia

Toda decisão de topologia merece um **ADR** (Architecture Decision Record) que documente: o problema, as opções consideradas, a decisão, e a justificativa. O template está em [`24-Templates/template-adr.md`](../../24-Templates/template-adr.md). Um bom ADR força a explicitar trade-offs e sobrevive à partida do autor original.

### 7.3 Sinais de que a topologia precisa evoluir

- O supervisor virou gargalo (→ hierarquizar ou event-driven).
- Handoffs estão confusos (→ introduzir supervisor).
- O pipeline está cheio de `if` para casos não-previstos (→ swarm ou orchestrator).
- O mesh está caótico (→ introduzir estrutura: supervisor ou blackboard).

A topologia não é imutável — evolui com o sistema e a evidência.

---

## Capítulo 8 — Casos de estudo

### 8.1 MetaGPT: software house hierárquica

O **MetaGPT** (arXiv:2308.00352) é, novamente, o caso canônico: uma topologia *hierárquica* com SOPs estruturando papéis. A lição para topologias: a *estrutura* (papéis, artifacts, protocolos) é tão importante quanto a topologia — uma boa topologia sem estrutura diverge; uma topologia modesta com estrutura boa converge.

> **Leitura.** [`09-CaseStudies/`](../../09-CaseStudies/) e [`10-Architecture/architectures/catalog.md`](../../10-Architecture/architectures/catalog.md).

### 8.2 Lições transversais

1. **A topologia é a decisão mais cara.** Errar manifesta-se como gargalos e deadlocks.
2. **Estrutura > topologia sofisticada.** Papéis e protocolos importam tanto quanto o grafo.
3. **Híbrido é a realidade.** Justifique cada parte com ADR.

---

## Capítulo 9 — Referências e leituras

### 9.1 Bibliografia fundamental

- **Hong, S. et al.** *MetaGPT.* ICLR 2024. arXiv:2308.00352. 🏛
- **LangGraph.** *Multi-Agent* examples (`hierarchical_agent_teams`, `multi-agent-collaboration`).
- **OpenAI Swarm.** Repo + paper técnico, 2024.

### 9.2 Bibliografia complementar

- **Chen, W. et al.** *AgentVerse.* arXiv:2308.10848.
- **Wu, Q. et al.** *AutoGen.* arXiv:2308.08155.
- **Microsoft AutoGen docs** (`ConversableAgent`, `GroupChat`).

### 9.3 Recursos práticos

- **Frameworks:** LangGraph, AutoGen, OpenAI Agents SDK, CrewAI, Agno, PydanticAI.
- **Catálogo:** [`10-Architecture/architectures/catalog.md`](../../10-Architecture/architectures/catalog.md) (12 topologias).

### 9.4 Ficha de pesquisa

Fontes em [`20-Research/ETHAGT10-pesquisa.md`](../../20-Research/ETHAGT10-pesquisa.md). Última consulta: Julho 2026.

---

## Síntese do módulo

Ao concluir ETHAGT10, você deve ser capaz de:

1. **Caracterizar** as 12 topologias e seus when-to-use/when-to-avoid.
2. **Implementar** Supervisor, Hierarchical, Swarm, Pipeline e pelo menos mais uma.
3. **Justificar** a escolha de topologia via ADR (matriz de decisão).
4. **Medir** trade-offs (consistência × latência × custo × flexibilidade).
5. **Identificar** sinais de que a topologia precisa evoluir.

Próximos passos: ETHAGT11 leva a topologia escolhida à produção (event-driven, durable execution); ETHAGT14 trata escala distribuída; ETHAGT15 conecta com topologias recursivas (meta-agentes); ETHAGT90 integra tudo no Capstone.

---

*Mantido por: Escola de Tecnologia — Universidade Etho · Área de Inteligência Artificial · Versão 1.0 · Julho 2026*
