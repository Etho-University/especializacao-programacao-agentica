# ETHAGT11 — Event-Driven Agents & Workflow Orchestration

> **Apostila do curso** · Especialização em Programação Agêntica · Universidade Etho
> Fase C — Multi-Agentes, Ferramentas e Orquestração · Carga 25 h · Versão 1.0 · Julho 2026
> *Material de referência duradouro (nível pós-graduação lato sensu). Os slides são auxiliares.*

---

## Sumário

- **Capítulo 1** — Por que event-driven
- **Capítulo 2** — Mensageria (Kafka, RabbitMQ, NATS)
- **Capítulo 3** — Orquestração de workflows
- **Capítulo 4** — Durable execution para agentes
- **Capítulo 5** — Patterns de resiliência
- **Capítulo 6** — Produção: ordering, escala, observabilidade
- **Capítulo 7** — Casos de estudo
- **Capítulo 8** — Referências e leituras

---

## Capítulo 1 — Por que event-driven

### 1.1 Os limites da orquestração síncrona

Até aqui, imaginamos agentes que se chamam *síncronamente*: o agente A chama o agente B, espera a resposta, continua. Esse modelo é natural para protótipos, mas *quebra em produção*:

- **Bloqueio:** se B demora, A fica preso esperando — recursos ociosos.
- **Acoplamento:** A precisa *conhecer* B (endereço, disponibilidade). Mudar B afeta A.
- **Fragilidade:** se B cai no meio, A falha — sem recuperação automática.
- **Escala limitada:** a cadeia síncrona não paraleliza nem distribui bem.

### 1.2 Event-driven: desacoplamento, escala, resiliência

A alternativa **event-driven** inverte o modelo: agentes não se chamam — eles *publicam* e *consomem eventos*. Um evento ("documento recebido") é publicado num *barramento*; os agentes interessados (*consumidores*) reagem. Quem publica não sabe (nem precisa saber) quem consome.

> **Diagrama de referência:** [`12-Diagrams/ETHAGT11/event-driven.mmd`](../../12-Diagrams/ETHAGT11/event-driven.mmd).

Os ganhos são grandes:

- **Desacoplamento:** produtor e consumidor não se conhecem — adicionar um novo consumidor não mexe no produtor.
- **Escala:** consumidores paralelizam; o barramento distribui.
- **Resiliência:** se um consumidor cai, o evento fica na fila; ele recupera ao voltar.

### 1.3 O trade-off: complexidade e debugging

O event-driven *não* é grátis. O custo é **complexidade**:

- **Fluxo implícito:** não há uma função "main" que mostra o caminho — o fluxo emerge das reações a eventos. Entender "o que acontece quando" exige tracing.
- **Debugging difícil:** um bug pode envolver eventos publicados por A, consumidos por B, que publica C... — a cadeia é assíncrona e distribuída.
- **Eventual consistency:** o estado converge *eventualmente*, não imediatamente — há janelas de inconsistência.

A regra de projeto (ecoando ETHAGT03): **não adote event-driven por padrão.** Use-o quando o *desacoplamento, a escala ou a resiliência* justificam a complexidade — tipicamente em sistemas com muitos agentes, longa duração ou alta carga.

---

## Capítulo 2 — Mensageria (Kafka, RabbitMQ, NATS)

### 2.1 O barramento de eventos

O coração de um sistema event-driven é o **barramento de mensagens** — a infraestrutura que recebe, armazena e entrega eventos. As três opções dominantes têm naturezas distintas.

### 2.2 Kafka: o log distribuído

O **Kafka** modela a mensageria como um *log append-only particionado*. Tópicos são divididos em *partições*; eventos são appendados em ordem *por partição*; consumidores leem o log. Pontos-chave:

- **Ordenação por partição:** eventos na *mesma partição* ficam ordenados (use uma *chave* de particionamento para garantir ordem de eventos relacionados, ex.: por `entity_id`).
- **Durabilidade:** o log é persistido e replicado; eventos sobrevivem a falhas.
- **Replay:** consumidores podem *releer* o log do início — útil para reprocessar.
- **Escala massiva:** projetado para volumes gigantescos.

O texto canônico é *The Log* (Jay Kreps, LinkedIn), que articula a filosofia do Kafka.

### 2.3 RabbitMQ: filas e routing

O **RabbitMQ** é um *message broker* clássico baseado em AMQP: *exchanges* roteiam mensagens para *filas* baseado em regras (routing keys, bindings). É mais flexível no roteamento e mais simples para padrões como *work queue* e *pub/sub* com filtragem. Adequado para sistemas de complexidade moderada com necessidades de roteamento rico.

### 2.4 NATS: leveza e performance

O **NATS** é um sistema de mensageria *leve e rápido*, com o *JetStream* adicionando persistência (similar ao log do Kafka). Destaca-se por baixo overhead, simplicidade de operação e performance — bom para sistemas que querem semânticas de mensageria sem o peso operacional do Kafka.

### 2.5 Quando cada; patterns (CQRS, saga)

| Sistema | Quando escolher |
|---|---|
| **Kafka** | Volume massivo, necessidade de log/replay, ordering por partição |
| **RabbitMQ** | Roteamento rico, filas de trabalho, complexidade moderada |
| **NATS** | Leveza, performance, operação simples |

Patterns que emergem: **CQRS** (separar modelo de escrita do de leitura, útil quando agentes escrevem e leem de formas distintas) e **saga** (orquestrar transações multi-etapa com compensação — Capítulo 5).

---

## Capítulo 3 — Orquestração de workflows

### 3.1 Workflow engine vs agentes que decidem

Há uma tensão arquitetural: o fluxo do sistema deve ser controlado por uma *workflow engine* (código que define os passos) ou por *agentes que decidem* (o LLM escolhe)? A resposta real: *ambos, em camadas*. A workflow engine cuida da *infraestrutura* (ordem garantida, retries, estado durável); os agentes cuidam das *decisões* (o que fazer em cada etapa). É a distinção workflow/agente de ETHAGT01, agora em escala de produção.

### 3.2 Temporal: durable execution

O **Temporal** é a ferramenta canônica de *durable execution*: você escreve um *workflow* como código (funções), e o Temporal garante que ele execute *até o fim*, sobrevivendo a crashes, reinícios e falhas de rede. O estado do workflow é persistido a cada passo; se o processo morre, o Temporal retoma do último passo concluído.

Conceitos do Temporal:

- **Workflow:** a função que orquestra (chama atividades, espera sinais/timers). *Não deve* ter efeitos colaterais não-determinísticos.
- **Activity:** uma unidade de trabalho executável (chamar uma API, rodar um agente). Pode falhar e ser retentada.
- **Signal / Timer:** mecanismos de interação externa (um humano aprova; um timer expira).

### 3.3 Prefect, Airflow (comparativo)

**Prefect** e **Airflow** são alternativas de orquestração, com foco histórico em *data pipelines*. Para agentes, o Temporal costuma ser mais adequado pela ênfase em *durable execution* e em workflows de longa duração com interação — mas Prefect também suporta esses cenários. A escolha depende do ecossistema e da equipe.

### 3.4 Quando orquestrar via código vs via agente supervisor

- **Via código (workflow engine):** quando o fluxo é *previsível* e você quer *garantias* (ordem, retries, auditoria). Use para a *espinha dorsal* do sistema.
- **Via agente supervisor:** quando o fluxo é *adaptativo* e a decisão de próximo passo é do LLM. Use para as *partes abertas*.

Muitas vezes, o melhor é *híbrido*: a workflow engine orquestra os *passos fixos* (com garantias), e dentro de cada passo, um agente decide o que fazer.

---

## Capítulo 4 — Durable execution para agentes

### 4.1 Sobreviver a crashes

A característica mais valiosa do durable execution para agentes é a **sobrevivência**: um agente que roda por *horas ou dias* (uma pesquisa longa, um processamento em massa) não pode perder tudo num crash. O durable execution persiste o estado a cada passo, permitindo retomar.

> **Diagrama de referência:** [`12-Diagrams/ETHAGT11/durable-execution.mmd`](../../12-Diagrams/ETHAGT11/durable-execution.mmd).

### 4.2 Long-running agents

Agentes de longa duração (horas, dias) são viáveis com durable execution: o workflow persiste entre execuções; timers acordam o agente em momentos certos; sinais trazem informação externa (um humano respondeu, um evento ocorreu). Isso habilita casos antes impraticáveis — um agente que monitora e age ao longo de dias.

### 4.3 Human-in-the-loop via timers/signals

O HITL (ETHAGT02 §4) ganha uma implementação robusta: o workflow *pausa* num passo que requer aprovação humana, e um *signal* externo (a aprovação) o retoma. Um *timer* pode escalarar para um humano alternativo (ou auto-decidir) se a aprovação não vier em N horas. Isso combina a *autonomia* do agente com a *supervisão* humana, de forma durável.

### 4.4 Replays e debug temporal

Como o estado é persistido, o workflow pode ser *replayado* a partir de qualquer ponto — essencial para debug ("o que o agente fez no passo 47?"). Esse "time travel" operacional é a contrapartida de produção do checkpointer de ETHAGT05.

---

## Capítulo 5 — Patterns de resiliência

### 5.1 Retries com backoff

Falhas transitórias são inevitáveis (rede, 503, timeout). O padrão é **retry com backoff exponencial e jitter** (ETHAGT02 §3.3): tentar de novo, esperando cada vez mais, com variação aleatória para evitar sincronização. Limite o número de retentativas para evitar loops infinitos.

### 5.2 Idempotência (chaves)

A retentatura cria um risco: se a operação *executou* mas a resposta *se perdeu*, a retentativa *executa de novo*. Daí a necessidade de **idempotência** via chave (ETHAGT02 §3.2): o sistema reconhece que já processou aquela chave e não reexecuta.

### 5.3 Compensação (saga)

Quando um passo de uma sequência *falha definitivamente* (não transitória), você precisa *desfazer* os passos anteriores já executados. O padrão **saga** faz exatamente isso: cada passo tem um passo *compensatório* associado (criar → deletar; cobrar → reembolsar).

> **Diagrama de referência:** [`12-Diagrams/ETHAGT11/saga.mmd`](../../12-Diagrams/ETHAGT11/saga.mmd).

```
   transferir(A→B):
     1. debitar A        (compensação: creditar A)
     2. creditar B       (compensação: debitar B)
     3. notificar        (compensação: enviar aviso de falha)
   ── se passo 2 falha ──► executar compensação de 1 (creditar A)
```

### 5.4 Circuit breakers

Se um serviço está falhando repetidamente, continuar tentando agrava (cascata de falhas). O **circuit breaker** "abre" após N falhas consecutivas, parando de tentar por um período (deixa o serviço se recuperar) antes de "fechar" e testar novamente. Previne falhas em cascata.

---

## Capítulo 6 — Produção: ordering, escala, observabilidade

### 6.1 Exactly-once vs at-least-once: mitos e realidade

A semântica de entrega é uma fonte de confusão:

- **At-most-once:** pode perder (rápido, não confiável).
- **At-least-once:** pode duplicar (confiável, exige idempotência).
- **Exactly-once:** *teoricamente* ideal, *praticamente* controverso — muitos sistemas só a conseguem com custo alto ou com idempotência embutida.

A realidade: **a maioria dos sistemas oferece at-least-once, e você trata duplicação com idempotência.** Buscar "exactly-once puro" é frequentemente uma caça ao snark. Projete para idempotência desde o início.

### 6.2 Sharding de consumidores

Para escalar o consumo, *particione* o trabalho: múltiplos consumidores, cada um lidando com uma partição (por chave). Isso paraleliza mantendo a ordenação *por partição*. O erro comum: particionar mal (chave que não distribui) causa *hotspots* (uma partição sobrecarregada).

### 6.3 Distributed tracing

Em um pipeline event-driven multi-agente, um evento atravessa muitos serviços. O **distributed tracing** (OpenTelemetry) correlaciona os passos de *um evento* através dos serviços, formando um trace ponta-a-ponta. Sem tracing, depurar um pipeline assíncrono é quase impossível. ETHAGT12 aprofunda observabilidade.

### 6.4 Custo

Mensageria e durable execution adicionam custo de infraestrutura (clusters, armazenamento de log). Em volume alto, otimize: retenção de eventos (quanto tempo guardar?), particionamento (equilibrar), e escolha de ferramenta (NATS é mais barato que Kafka para volumes moderados).

---

## Capítulo 7 — Casos de estudo

### 7.1 Processamento de documentos em enterprise

Os casos canônicos de event-driven em agentes são pipelines de processamento de documentos em massa: um documento chega (evento), dispara agentes de classificação, extração, validação, indexação — cada um reagindo a eventos do anterior, em paralelo onde possível, com durable execution garantindo que nenhum documento se perca. A lição: **para volume e resiliência, o event-driven é o que torna o sistema viável.**

> **Leitura.** [`09-CaseStudies/`](../../09-CaseStudies/).

### 7.2 Lições transversais

1. **Síncrono para protótipos, event-driven para produção em escala.**
2. **Durable execution habilita agentes de longa duração** antes impraticáveis.
3. **Resiliência é composta:** retries + idempotência + saga + circuit breakers.
4. **Observabilidade (tracing) é pré-requisito** — sem ela, o event-driven é opaco.

---

## Capítulo 8 — Referências e leituras

### 8.1 Bibliografia fundamental

- **Temporal.io.** *Documentation* e *Durable Execution* primer.
- **Narkhede, N., Shapira, G. & Palino, T.** *Kafka: The Definitive Guide.*
- **Richards, M.** *Fundamentals of Software Architecture* (cap. event-driven).

### 8.2 Bibliografia complementar

- **NATS docs; RabbitMQ docs.**
- **Microsoft.** *Cloud Design Patterns* (saga, CQRS).
- **Kreps, J.** *The Log* (LinkedIn) — filosofia do Kafka.

### 8.3 Recursos práticos

- **CloudEvents** spec (CNCF) — padronização de eventos.
- **OpenTelemetry** — distributed tracing.
- **Ferramentas:** Kafka, NATS, RabbitMQ, Temporal, Prefect, Docker Compose.

### 8.4 Ficha de pesquisa

Fontes em [`20-Research/ETHAGT11-pesquisa.md`](../../20-Research/ETHAGT11-pesquisa.md). Última consulta: Julho 2026.

---

## Síntese do módulo

Ao concluir ETHAGT11, você deve ser capaz de:

1. **Diferenciar** orquestração síncrona de event-driven assíncrona e justificar a escolha.
2. **Aplicar** mensageria (Kafka/RabbitMQ/NATS) e patterns (CQRS, saga).
3. **Implementar** durable execution (Temporal) para workflows longos e HITL.
4. **Compor** resiliência (retries, idempotência, compensação, circuit breakers).
5. **Operar** em escala (ordering, sharding, tracing) com semânticas de entrega conscientes.

Com ETHAGT11, encerra-se a Fase C: o agente isolado tornou-se um *sistema de agentes coordenado e produtivo*. A Fase D (ETHAGT12-16) leva isso a produção com rigor (AgentOps, segurança, escala) e atinge a fronteira (meta-agentes, sociedades).

Próximos passos: ETHAGT12 (AgentOps e observabilidade), ETHAGT14 (escala distribuída), ETHAGT90 (Capstone integrador).

---

*Mantido por: Escola de Tecnologia — Universidade Etho · Área de Inteligência Artificial · Versão 1.0 · Julho 2026*
