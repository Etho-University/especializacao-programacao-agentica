# ETHAGT11 — Event-Driven Agents & Workflow Orchestration
## Storyboard da Apresentação

> **Universidade Etho · Especialização em Programação Agêntica**
> Fase C — Orquestração & Produção · 25 h
> Storyboard v1.0 · Julho 2026

---

## Metadados da Apresentação

| Campo | Valor |
|---|---|
| Código | ETHAGT11 |
| Título | Event-Driven Agents & Workflow Orchestration |
| Duração estimada | 90 min (2 blocos de 45 min) |
| Total de slides | 76 (~70 planejados) |
| Público | Arquitetos, Engenheiros de Software, Engenheiros de IA, Platform Engineers, Tech Leads |
| Pré-requisitos | ETHAGT10 |
| Competências | C1 (A), C2 (A), C3 (B), C4 (B), C5 (I) |

---

## Mapa Visual da Apresentação

```
BLOCO 1 (45 min)                              BLOCO 2 (45 min)
┌──────────────────────────────┐              ┌──────────────────────────────┐
│ SEÇÃO A — Abertura (8 min)   │              │ SEÇÃO E — Durable Exec (12m) │
│  Capa · Objetivos · Agenda   │              │  Crashes · Long-running      │
│  Motivação · Contexto        │              │  HITL · Replays · DEMO       │
├──────────────────────────────┤              ├──────────────────────────────┤
│ SEÇÃO B — Por que ED (9 min) │              │ SEÇÃO F — Resiliência (12m)  │
│  Limites síncrono            │              │  Retries · Idempotência      │
│  Event-driven · Trade-offs   │              │  Saga · Circuit breakers     │
├──────────────────────────────┤              │  Produção: ordering, escala  │
│ SEÇÃO C — Mensageria (15 min)│              ├──────────────────────────────┤
│  Kafka · RabbitMQ · NATS     │              │ SEÇÃO G — Fechamento (24 min)│
│  CQRS · Saga · CloudEvents   │              │  Exercício · Boas práticas   │
│  DEMO: Agente com Kafka      │              │  Caso de estudo · Resumo     │
├──────────────────────────────┤              │  Quiz · Projeto · Referências│
│ SEÇÃO D — Workflows (10 min) │              │  Q&A                         │
│  Temporal · Prefect · Airflow│              └──────────────────────────────┘
└──────────────────────────────┘
```

---

## Storyboard Detalhado

### SEÇÃO A — Abertura (Slides 1-6 · 8 min)

---

#### Slide 1 — Capa
- **Tipo**: Capa
- **Objetivo**: Identificar a aula, professor e contexto
- **Conteúdo**:
  - ETHAGT11 — Event-Driven Agents & Workflow Orchestration
  - Universidade Etho · Especialização em Programação Agêntica
  - Fase C — Orquestração & Produção
  - Professor · Data
- **Diagrama**: Logo Etho + imagem de fundo abstrata (fluxos de eventos/topologias)
- **Animação**: Fade in do título
- **Tempo**: 1 min

---

#### Slide 2 — Objetivos do Módulo
- **Tipo**: Conteúdo
- **Objetivo**: Deixar claro o que o aluno deve conseguir fazer ao final
- **Conteúdo**:
  - Objetivo geral: Construir sistemas de agentes orientados a eventos com orquestração robusta
  - 5 objetivos específicos (1 linha cada):
    1. Diferenciar orquestração síncrona de event-driven assíncrona
    2. Aplicar filas (Kafka, RabbitMQ, NATS) para coordenação de agentes
    3. Implementar durable execution (Temporal, Prefect) para workflows longos
    4. Lidar com falhas, retries, idempotência, compensação
    5. Avaliar escala, ordering, exactly-once vs at-least-once
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
  - C5 AgentOps & Avaliação → I
  - Badge visual por competência
- **Diagrama**: Radar chart dos 5 pilares
- **Animação**: Radar aparece com wipe
- **Tempo**: 1 min

---

#### Slide 4 — Agenda
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar o roteiro da aula com tempos
- **Conteúdo**:
  - Bloco 1: Abertura → Por que Event-Driven → Mensageria → Workflows
  - Bloco 2: Durable Execution → Resiliência → Fechamento
  - Tempos estimados por seção
- **Diagrama**: Timeline horizontal com 7 seções
- **Animação**: Timeline cresce da esquerda para direita
- **Tempo**: 1 min

---

#### Slide 5 — Motivação: O Crash no Ticket 5.000
- **Tipo**: Conteúdo
- **Objetivo**: Criar tensão — agentes síncronos perdem tudo em crash
- **Conteúdo**:
  - Cenário: processamento de 10.000 tickets por um agente
  - O processo cai no ticket 5.000 — recomeça do zero
  - Horas de processamento perdidas, custo de API desperdiçado
  - Pergunta: *Qual o pior crash que você já viu em produção?*
  - A solução: event-driven + durable execution
- **Diagrama**: Timeline de execução com "X" vermelho no ticket 5.000 → recomeço
- **Animação**: Barra de progresso avança até 50%, trava, volta ao zero
- **Tempo**: 2 min

---

#### Slide 6 — Contexto: Evolução para Event-Driven
- **Tipo**: Conteúdo
- **Objetivo**: Explicar a confluência que tornou event-driven essencial para agentes
- **Conteúdo**:
  - Linha do tempo: 2011 (Kafka na LinkedIn) → 2016 (Temporal predecessores) → 2019 (Temporal open source) → 2023 (agentes de longa duração) → 2024 (durable execution para LLM agents)
  - Confluência: agentes longos + custo de recomputação + necessidade de resiliência
  - Kreps *The Log* como fundamento conceitual
  - CloudEvents (CNCF) como padrão emergente
- **Diagrama**: Timeline horizontal com marcos
- **Animação**: Marcos aparecem sequencialmente
- **Tempo**: 1 min

---

### SEÇÃO B — Por que Event-Driven (Slides 7-13 · 9 min)

---

#### Slide 7 — [SEÇÃO] Por que Event-Driven
- **Tipo**: Seção
- **Objetivo**: Transição para o bloco de fundamentos
- **Conteúdo**: Número "1" grande + "Por que Event-Driven"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 8 — Limites da Orquestração Síncrona
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar onde a orquestração síncrona quebra
- **Conteúdo**:
  - Acoplamento temporal: caller e callee devem estar vivos ao mesmo tempo
  - Falta de resiliência: falha no meio = perda de progresso
  - Difícil escalar: bottleneck no orquestrador síncrono
  - Custo de recomputação: cada retry recomeça do zero
  - Exemplo: agente que processa 10 tools em série — se cai na tool 7, perde tudo
- **Diagrama**: Cadeia síncrona com ponto de falha destacado
- **Animação**: Falha aparece em vermelho na posição 7
- **Tempo**: 2 min

---

#### Slide 9 — O que é Event-Driven
- **Tipo**: Diagrama
- **Objetivo**: Definir o paradigma event-driven de forma clara
- **Conteúdo**:
  - Componentes se comunicam via eventos (mensagens assíncronas)
  - Produtor publica evento → broker roteia → consumidor processa
  - Desacoplamento temporal: produtor e consumidor não precisam coincidir
  - Desacoplamento espacial: não precisam se conhecer
  - Evento = fato que ocorreu (passado), não comando (futuro)
- **Diagrama**: `12-Diagrams/ETHAGT11/event-driven.mmd`
- **Animação**: Produtor → broker → consumidor aparecem sequencialmente
- **Tempo**: 2 min

---

#### Slide 10 — Benefícios: Desacoplamento, Escala, Resiliência
- **Tipo**: Conteúdo
- **Objetivo**: Listar os ganhos concretos do paradigma
- **Conteúdo**:
  - Desacoplamento: componentes evoluem independentemente
  - Escala horizontal: consumidores paralelos por partição
  - Resiliência: broker persiste eventos; consumers recuperam de onde pararam
  - Replay: reprocessar histórico de eventos
  - Backpressure natural: consumer puxa no seu ritmo
- **Diagrama**: 5 ícones com labels (etho-success)
- **Animação**: Ícones surgem um a um
- **Tempo**: 1.5 min

---

#### Slide 11 — Trade-offs: Complexidade, Eventual Consistency, Debugging
- **Tipo**: Conteúdo
- **Objetivo**: Ser honesto sobre o preço do paradigma
- **Conteúdo**:
  - Complexidade: mais componentes móveis (broker, consumers, DLQ)
  - Eventual consistency: estado convergi apenas depois de processar eventos
  - Debugging distribuído: trace espalhado por serviços
  - Ordering: garantir ordem global é caro/impossível
  - "Event-driven não é grátis — é uma troca consciente"
- **Diagrama**: Balança: benefícios vs custos
- **Tempo**: 1.5 min

---

#### Slide 12 — Síncrono vs Assíncrono (Comparação)
- **Tipo**: Comparação
- **Objetivo**: Sistematizar quando cada paradigma se aplica
- **Conteúdo**:
  - Coluna 1: Síncrono — simples, baixa latência, acoplado, frágil
  - Coluna 2: Assíncrono (event-driven) — resiliente, escalável, complexo, eventual
  - Coluna 3: Híbrido — síncrono para UX, assíncrono para processamento
  - Pergunta: *Suas tools de agente são síncronas ou assíncronas?*
- **Diagrama**: 3 colunas comparativas
- **Animação**: Colunas aparecem uma a uma
- **Tempo**: 1 min

---

#### Slide 13 — Exercício Rápido: Síncrono ou Assíncrono?
- **Tipo**: Exercício
- **Objetivo**: Praticar a decisão em cenários reais
- **Conteúdo**:
  - 4 cenários curtos:
    1. "Responder pergunta do usuário em chat" → Síncrono
    2. "Processar 10.000 documentos" → Assíncrono
    3. "Buscar em RAG e responder" → Síncrono (com timeout)
    4. "Coordenar 3 agentes em pipeline longo" → Assíncrono
  - Votação rápida (mãos levantadas)
- **Diagrama**: 4 cards com cenários
- **Tempo**: 1.5 min

---

### SEÇÃO C — Mensageria (Slides 14-27 · 15 min)

---

#### Slide 14 — [SEÇÃO] Mensageria
- **Tipo**: Seção
- **Objetivo**: Transição para o bloco de mensageria
- **Conteúdo**: "2 — Mensageria: Kafka, RabbitMQ, NATS"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 15 — O Log como Abstração Central
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar o conceito fundacional de Kafka
- **Conteúdo**:
  - "O Log" (Kreps, LinkedIn) — append-only, ordenado, imutável
  - Tópico = log particionado; cada partição é uma sequência ordenada
  - Consumer mantém offset (posição no log)
  - Replay: voltar o offset e reprocessar
  - Fonte: Kreps, *The Log*
- **Diagrama**: Log imutável com offsets e consumers lendo em posições diferentes
- **Animação**: Mensagens são appendadas; consumers avançam offset
- **Tempo**: 2 min

---

#### Slide 16 — Kafka: Arquitetura (Topics, Partitions, Log)
- **Tipo**: Diagrama
- **Objetivo**: Mostrar a anatomia do Kafka
- **Conteúdo**:
  - Topic → N partitions → cada partition é um log imutável
  - Producer escreve em partition (por key ou round-robin)
  - Consumer Group: um consumer por partition
  - Replicação: leader + followers por partition
  - Retenção por tempo ou tamanho
- **Diagrama**: `12-Diagrams/ETHAGT11/event-driven.mmd` (parte Kafka)
- **Animação**: Componentes surgem do tópico para fora
- **Tempo**: 2 min

---

#### Slide 17 — Kafka: Particionamento e Ordering
- **Tipo**: Diagrama
- **Objetivo**: Explicar o modelo de ordering do Kafka
- **Conteúdo**:
  - Ordering garantido **dentro** de uma partição, não global
  - Key = agente_id → mesmo agente → mesma partição → ordering preservado
  - Sem key → round-robin → sem ordering garantido
  - Pergunta: *Ordering por partição — como garantir que mensagens do mesmo agente vão pra mesma partição?*
  - Resposta: hash(key) % num_partitions
- **Diagrama**: 3 partições com mensagens coloridas por agent_id
- **Animação**: Mensagens com mesma key caem na mesma partição
- **Tempo**: 2 min

---

#### Slide 18 — Kafka: Consumer Groups e Escala Horizontal
- **Tipo**: Diagrama
- **Objetivo**: Mostrar como Kafka escala consumidores
- **Conteúdo**:
  - Consumer Group: conjunto de consumers que dividem as partições
  - 1 consumer por partição dentro do grupo
  - Adicionar consumers → rebalanceamento → mais paralelismo
  - Limite: # consumers ≤ # partições
  - Offset commit: at-least-once (commit após processar) vs at-most-once (commit antes)
- **Diagrama**: 3 partições → 3 consumers em um group
- **Animação**: Consumers aparecem; setas de atribuição partition→consumer
- **Tempo**: 1.5 min

---

#### Slide 19 — RabbitMQ: Filas, Exchanges, Routing
- **Tipo**: Diagrama
- **Objetivo**: Apresentar o modelo AMQP do RabbitMQ
- **Conteúdo**:
  - Exchange → binding → queue
  - Tipos de exchange: direct, topic, fanout, headers
  - Routing rico: mensagens vão para filas baseadas em routing key
  - ACK manual: consumer ack após processar
  - Dead letter exchange para mensagens que falham
- **Diagrama**: Exchange → bindings → múltiplas queues → consumers
- **Animação**: Mensagem roteada por routing key para queue correta
- **Tempo**: 2 min

---

#### Slide 20 — NATS: JetStream, Leveza, Performance
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar a alternativa leve
- **Conteúdo**:
  - NATS: mensagem simples, baixíssima latência, single binary
  - JetStream: persistência, streams, consumers duráveis
  - Modelos: at-least-once, exactly-once (com dedup window)
  - Ideal para edge, IoT, sistemas embarcados
  - Comparação de throughput: NATS > RabbitMQ > Kafka (em mensagens pequenas)
- **Diagrama**: Tabela de características NATS vs Kafka vs RabbitMQ (resumida)
- **Tempo**: 1.5 min

---

#### Slide 21 — Comparação: Kafka vs RabbitMQ vs NATS
- **Tipo**: Comparação
- **Objetivo**: Sistematizar os trade-offs entre os três
- **Conteúdo**:
  - Tabela comparativa nos eixos:
    - Modelo: log (Kafka) vs filas (RabbitMQ) vs stream (NATS)
    - Ordering: por partição (Kafka) vs por fila (RabbitMQ) vs por stream (NATS)
    - Retenção: configurável/dias (Kafka) vs ack-based (RabbitMQ) vs stream-based (NATS)
    - Throughput: altíssimo (Kafka) vs médio (RabbitMQ) vs alto (NATS)
    - Latência: média (Kafka) vs baixa (RabbitMQ) vs baixíssima (NATS)
    - Complexidade: alta (Kafka) vs média (RabbitMQ) vs baixa (NATS)
- **Diagrama**: Tabela comparativa colorida
- **Tempo**: 1.5 min

---

#### Slide 22 — Quando Usar Cada Um
- **Tipo**: Conteúdo
- **Objetivo**: Dar critério prático de escolha
- **Conteúdo**:
  - Kafka: volume altíssimo, replay necessário, log de eventos, event sourcing
  - RabbitMQ: routing complexo, filas de trabalho, request/reply, integrações legadas
  - NATS: baixa latência, edge, simplicidade operacional, mensagens pequenas
  - Regra: comece com o mais simples que resolve; Kafka é overkill para muitos casos
- **Diagrama**: Árvore de decisão simples
- **Tempo**: 1 min

---

#### Slide 23 — Padrão: CQRS
- **Tipo**: Diagrama
- **Objetivo**: Introduzir CQRS no contexto de agentes
- **Conteúdo**:
  - Command Query Responsibility Segregation
  - Write side (commands) → eventos → read side (queries) → views materializadas
  - Para agentes: comandos geram eventos; agentes de consulta leem views
  - Fonte: Microsoft *Cloud Design Patterns*
- **Diagrama**: Fluxo CQRS — command → event store → read model → query
- **Tempo**: 1 min

---

#### Slide 24 — Padrão: Saga (Visão Geral)
- **Tipo**: Diagrama
- **Objetivo**: Introduzir saga antes de aprofundar em resiliência
- **Conteúdo**:
  - Saga: sequência de transações locais com compensação
  - Se passo N falha, executam compensações dos passos 1..N-1
  - Dois estilos: orquestrada (central) vs coreografada (eventos)
  - Aprofundamento na Seção F
- **Diagrama**: `12-Diagrams/ETHAGT11/saga.mmd`
- **Tempo**: 1 min

---

#### Slide 25 — CloudEvents: Padronização de Eventos
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar o padrão CNCF para eventos
- **Conteúdo**:
  - CloudEvents: spec CNCF para descrição de eventos
  - Campos: id, source, type, specversion, time, data, subject
  - Interoperabilidade: mesmo formato entre Kafka, RabbitMQ, NATS, HTTP
  - Para agentes: tool outputs como CloudEvents padroniza observabilidade
- **Diagrama**: Exemplo de JSON CloudEvent
- **Tempo**: 1 min

---

#### Slide 26 — DEMO: Agente com Kafka
- **Tipo**: Código
- **Objetivo**: Demo ao vivo — dois agentes coordenados via tópicos Kafka
- **Conteúdo**:
  - Referência: `05-Labs/ETHAGT11/Lab1-Agente-Kafka`
  - Agente A publica "tarefa: pesquisar X" no tópico `agent-tasks`
  - Agente B consome, processa, publica resultado no tópico `agent-results`
  - Mostrar ordering por chave (mesmo agent_id = mesma partição)
  - Simular falha de consumer e mostrar reprocessamento
- **Diagrama**: Code block + terminal side-by-side
- **Animação**: Highlight de linhas chave (producer, consumer, key)
- **Tempo**: 3 min

---

#### Slide 27 — Pergunta da DEMO
- **Tipo**: Exercício
- **Objetivo**: Engajar a turma com uma pergunta sobre a demo
- **Conteúdo**:
  - "O que acontece se Agente B processar duas vezes a mesma mensagem?"
  - "Como garantir que o resultado não seja duplicado?"
  - Discussão em duplas (2 min)
- **Diagrama**: Caixa de discussão
- **Tempo**: 1.5 min

---

### SEÇÃO D — Orquestração de Workflows (Slides 28-36 · 10 min)

---

#### Slide 28 — [SEÇÃO] Orquestração de Workflows
- **Tipo**: Seção
- **Objetivo**: Transição para orquestração de workflows
- **Conteúdo**: "3 — Orquestração de Workflows: Temporal, Prefect, Airflow"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 29 — Workflow Engine vs Agentes que Decidem
- **Tipo**: Comparação
- **Objetivo**: Clarificar que workflow engine e agentes são complementares
- **Conteúdo**:
  - Workflow engine: passos predefinidos, determinísticos, duráveis
  - Agente que decide: rota dinâmica, flexível, menos previsível
  - Híbrido: agente decide dentro de activity; workflow garante durability
  - Pergunta: *Você orquestra via código ou via agente supervisor?*
- **Diagrama**: Espectro — workflow determinístico ←→ agente autônomo
- **Tempo**: 1.5 min

---

#### Slide 30 — Temporal: Conceitos (Workflow, Activity, Worker)
- **Tipo**: Diagrama
- **Objetivo**: Apresentar os conceitos fundamentais do Temporal
- **Conteúdo**:
  - Workflow: função que descreve a lógica (determinística, sem I/O direto)
  - Activity: unidade de trabalho (chamada de API, tool, I/O)
  - Worker: processo que executa workflows e activities
  - Temporal Server: armazena estado e histórico de execução
  - Task Queue: workflow/activity tasks esperando workers
- **Diagrama**: Arquitetura Temporal — Client → Server → Task Queue → Worker
- **Animação**: Componentes aparecem um a um
- **Tempo**: 2 min

---

#### Slide 31 — Temporal: Durable Execution
- **Tipo**: Diagrama
- **Objetivo**: Explicar o conceito central de durable execution
- **Conteúdo**:
  - Estado da execução é persistido a cada step
  - Se o worker cai, outro worker retoma do último step completado
  - Não há perda de progresso — o histórico é a fonte de verdade
  - Replay: re-executar o workflow usando o histórico gravado
  - Fonte: Temporal *Durable Execution* primer
- **Diagrama**: `12-Diagrams/ETHAGT11/durable-execution.mmd`
- **Animação**: Worker cai (X vermelho) → novo worker retoma do checkpoint
- **Tempo**: 2 min

---

#### Slide 32 — Temporal: Código como Workflow
- **Tipo**: Código
- **Objetivo**: Mostrar que o workflow é código Python/Go comum
- **Conteúdo**:
  - Snippet: workflow como função async com `await activity(...)`
  - Determinismo: sem `datetime.now()`, sem `random()`, sem I/O direto
  - I/O vai em activities; workflow orquestra
  - Timers: `await workflow.sleep(...)` (durable, sobrevive a restart)
  - Signals: receber input externo durante execução
- **Diagrama**: Code block com workflow + activity
- **Tempo**: 1.5 min

---

#### Slide 33 — Prefect: Python Puro, Mais Simples
- **Tipo**: Código
- **Objetivo**: Mostrar a alternativa mais simples
- **Conteúdo**:
  - `@flow` e `@task` decorators
  - Menos verboso que Temporal; integração natural com Python
  - Menos durável: estado no Prefect server, não no código
  - Bom para data pipelines e protótipos de agentes
  - Snippet de código
- **Diagrama**: Code block comparando com Temporal
- **Tempo**: 1 min

---

#### Slide 34 — Airflow: Agendamento vs Orquestração em Tempo Real
- **Tipo**: Conteúdo
- **Objetivo**: Posicionar Airflow corretamente
- **Conteúdo**:
  - Airflow: DAGs agendadas (batch, cron-like)
  - Não é orquestração em tempo real nem durable execution
  - Ótimo para ETL e pipelines de dados agendados
  - Para agentes de longa duração com HITL: Temporal é mais adequado
- **Diagrama**: Espectro: Airflow (batch/agendado) ←→ Temporal (real-time/durable)
- **Tempo**: 1 min

---

#### Slide 35 — Comparação: Temporal vs Prefect vs Airflow
- **Tipo**: Comparação
- **Objetivo**: Sistematizar os trade-offs
- **Conteúdo**:
  - Tabela nos eixos: durable execution, complexidade, HITL, timers, replay, linguagem, custo operacional
  - Temporal: máximo durability, complexidade média, HITL nativo
  - Prefect: durabilidade média, simplicidade alta, HITL limitado
  - Airflow: durabilidade baixa, agendamento forte, sem HITL em tempo real
- **Diagrama**: Tabela comparativa colorida
- **Tempo**: 1.5 min

---

#### Slide 36 — Quando Orquestrar via Código vs via Agente Supervisor
- **Tipo**: Conteúdo
- **Objetivo**: Decisão arquitetural: workflow engine ou agente
- **Conteúdo**:
  - Workflow engine (Temporal): passos previsíveis, determinismo, auditoria
  - Agente supervisor: rota dinâmica, decisões contextuais, flexibilidade
  - Híbrido: agente dentro de activity Temporal — flexibilidade + durability
  - Regra: orquestração determinística no workflow; decisões inteligentes no agente
- **Diagrama**: Árvore de decisão
- **Tempo**: 1 min

---

### SEÇÃO E — Durable Execution para Agentes (Slides 37-46 · 12 min)

---

#### Slide 37 — [SEÇÃO] Durable Execution para Agentes
- **Tipo**: Seção
- **Objetivo**: Transição para durable execution aplicado a agentes
- **Conteúdo**: "4 — Durable Execution para Agentes"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 38 — Sobreviver a Crashes
- **Tipo**: Diagrama
- **Objetivo**: Mostrar como durable execution sobrevive a falhas
- **Conteúdo**:
  - Estado persistido a cada step (não a cada minuto — a cada chamada)
  - Kill do processo → novo worker pega o histórico → replay até o último step → continua
  - Comparação: sem durability = recomeça do zero; com durability = retoma do checkpoint
  - Para agentes: cada tool call é um activity → checkpoint automático
- **Diagrama**: `12-Diagrams/ETHAGT11/durable-execution.mmd`
- **Animação**: Crash → recovery com seta indicando ponto de retomada
- **Tempo**: 2 min

---

#### Slide 39 — Long-Running Agents (horas, dias)
- **Tipo**: Conteúdo
- **Objetivo**: Expandir o horizonte de duração de agentes
- **Conteúdo**:
  - Agente tradicional: segundos a minutos (context window limita)
  - Agente durável: horas, dias, semanas
  - Padrão: workflow que chama agente em loop, persistindo estado entre iterações
  - Casos: pesquisa longitudinal, monitoramento contínuo, processamento em massa
  - Cuidado: custo acumulado de tokens — orçamento por execução
- **Diagrama**: Timeline expandida — agente rodando por dias com checkpoints
- **Tempo**: 1.5 min

---

#### Slide 40 — Human-in-the-Loop via Timers e Signals
- **Tipo**: Diagrama
- **Objetivo**: Mostrar como HITL funciona em workflows duráveis
- **Conteúdo**:
  - Signal: mensagem externa entregue ao workflow em execução
  - Timer: `workflow.sleep(dias)` — pausa durável, não consome recursos
  - Padrão HITL: workflow pausa em `await signal` → humano aprova → workflow continua
  - Timeout: se humano não responde em X → caminho alternativo
  - Para agentes: agente propõe ação → workflow pausa → humano aprova → executa
- **Diagrama**: Sequência — workflow → pause (await signal) → humano aprova → resume
- **Animação**: Workflow pausa (amarelo) → signal chega → resume (verde)
- **Tempo**: 2 min

---

#### Slide 41 — Replays e Debug Temporal
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar o poder do replay para debugging
- **Conteúdo**:
  - Replay: re-executar workflow usando histórico gravado (sem re-executar activities)
  - Debug temporal: voltar no tempo, inspecionar estado em qualquer step
  - "Time travel debugging" — ver exatamente o que o agente decidiu em cada ponto
  - Ferramenta: Temporal Web UI mostra histórico completo de execução
- **Diagrama**: Timeline com marcadores de replay navegáveis
- **Tempo**: 1.5 min

---

#### Slide 42 — O Problema do Non-Determinism
- **Tipo**: Conteúdo
- **Objetivo**: Explicar a armadilha clássica do replay
- **Conteúdo**:
  - Replay pressupõe que o workflow re-executa de forma idêntica
  - Non-determinism quebra o replay:
    - `datetime.now()` → valor diferente a cada replay
    - `random()` → resultado diferente
    - I/O direto no workflow → estado externo mudou
    - Código do workflow alterado entre execução e replay
  - Solução: todo I/O e não-determinismo vão em activities
- **Diagrama**: Replay quebrado vs replay correto
- **Tempo**: 2 min

---

#### Slide 43 — Determinismo em Código de Workflow
- **Tipo**: Código
- **Objetivo**: Mostrar as regras práticas de código determinístico
- **Conteúdo**:
  - No workflow: usar `workflow.now()`, `workflow.random()` (seeded do histórico)
  - No workflow: NUNCO fazer I/O direto (HTTP, DB, filesystem)
  - No workflow: NUNCA usar `time.sleep()` — usar `workflow.sleep()`
  - Em activities: tudo permitido (I/O, side effects, chamadas de API)
  - Snippet: código correto vs código quebrado lado a lado
- **Diagrama**: Dois snippets: "✗ Quebrado" vs "✓ Correto"
- **Tempo**: 1.5 min

---

#### Slide 44 — DEMO: Workflow Durável em Temporal
- **Tipo**: Código
- **Objetivo**: Demo ao vivo — agente de longa duração sobrevivendo a kill do processo
- **Conteúdo**:
  - Referência: `05-Labs/ETHAGT11/Lab2-Workflow-Temporal`
  - Workflow que processa tickets em loop, chamando agente como activity
  - Mostrar execução em andamento na Temporal Web UI
  - Kill do worker (Ctrl+C) → reiniciar → workflow retoma do último ticket
  - Sem perda de progresso, sem reprocessamento
- **Diagrama**: Terminal + Temporal Web UI lado a lado
- **Animação**: Kill → restart → continuação destacada
- **Tempo**: 3 min

---

#### Slide 45 — Pergunta da DEMO
- **Tipo**: Exercício
- **Objetivo**: Engajar com pergunta sobre replay e tools externas
- **Conteúdo**:
  - "Replay: se uma tool externa mudou de comportamento, o replay quebra?"
  - "O que acontece se o agente tomar decisão diferente no replay?"
  - Discussão aberta (2 min)
- **Diagrama**: Caixa de discussão
- **Tempo**: 2 min

---

#### Slide 46 — Exercício: HITL com Signal
- **Tipo**: Exercício
- **Objetivo**: Praticar o padrão de human-in-the-loop
- **Conteúdo**:
  - Cenário: agente propõe enviar email para cliente
  - Em duplas: esboçar o workflow com signal de aprovação + timeout de 24h
  - O que acontece se o humano rejeitar? E se não responder?
  - 2 min discussão, 1 min compartilhar
- **Diagrama**: Esqueleto de workflow para preencher
- **Tempo**: 3 min

---

### SEÇÃO F — Patterns de Resiliência & Produção (Slides 47-56 · 12 min)

---

#### Slide 47 — [SEÇÃO] Patterns de Resiliência
- **Tipo**: Seção
- **Objetivo**: Transição para patterns de resiliência
- **Conteúdo**: "5 — Patterns de Resiliência: Retries, Idempotência, Saga, Circuit Breakers"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 48 — Retries com Backoff (Exponential, Jitter)
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar o pattern mais fundamental de resiliência
- **Conteúdo**:
  - Retry simples: tentar N vezes
  - Backoff exponencial: 1s → 2s → 4s → 8s → 16s
  - Jitter: adicionar aleatoriedade para evitar thundering herd
  - Limite de tentativas + circuit breaker quando excedido
  - Para agentes: retry em tool calls com timeout
  - Snippet: função `retry_with_backoff()`
- **Diagrama**: Timeline de retries com backoff crescente
- **Tempo**: 1.5 min

---

#### Slide 49 — Idempotência (Chaves de Idempotência)
- **Tipo**: Conteúdo
- **Objetivo**: Explicar por que idempotência é essencial em event-driven
- **Conteúdo**:
  - At-least-once delivery: mensagens podem chegar mais de uma vez
  - Idempotência: processar 2x = processar 1x (mesmo resultado)
  - Chave de idempotência: ID único por operação
  - Antes de processar: verificar se já processou aquela chave
  - Armazenar chaves processadas (Redis, DB)
- **Diagrama**: Fluxo — recebe mensagem → checa chave → já processou? → ignora/processa
- **Tempo**: 1.5 min

---

#### Slide 50 — Idempotência em Tool de "Enviar Email"
- **Tipo**: Código
- **Objetivo**: Aplicar idempotência em um caso concreto
- **Conteúdo**:
  - Tool: `send_email(to, subject, body, idempotency_key)`
  - Antes de enviar: `SELECT 1 FROM sent_emails WHERE key = ?`
  - Se existe: retornar resultado anterior (não reenvia)
  - Se não existe: enviar, gravar key + resultado, retornar
  - Pergunta: *Como garantir idempotência em tool de "enviar email"?*
  - Resposta do exercício do syllabus
- **Diagrama**: Code block + fluxo de decisão
- **Tempo**: 1.5 min

---

#### Slide 51 — Compensação: Saga Pattern
- **Tipo**: Diagrama
- **Objetivo**: Aprofundar o padrão saga
- **Conteúdo**:
  - Saga: sequência de transações locais com compensação
  - Passo 1 (execute) → Passo 2 (execute) → Passo 3 (FALHA)
  - Compensar Passo 2 → Compensar Passo 1
  - Não é rollback — é uma ação reversa ( nem sempre perfeita)
  - Dois estilos: orquestrada (central) vs coreografada (eventos)
- **Diagrama**: `12-Diagrams/ETHAGT11/saga.mmd`
- **Animação**: Passos executam → falha → compensações revertem
- **Tempo**: 2 min

---

#### Slide 52 — Saga: Transferência entre Contas
- **Tipo**: Diagrama
- **Objetivo**: Caso concreto de saga compensatória
- **Conteúdo**:
  - Transferência: debita conta A → credita conta B → notifica usuário
  - Se "notifica" falha: compensar "credita B" (estorna) → compensar "debita A" (devolve)
  - Saga orquestrada: orquestrador coordena passos e compensações
  - Saga coreografada: cada serviço publica evento e reage
  - Exercício do syllabus: escrever a lógica de compensação
- **Diagrama**: Fluxo saga com 3 passos + 3 compensações
- **Tempo**: 1.5 min

---

#### Slide 53 — Circuit Breakers
- **Tipo**: Diagrama
- **Objetivo**: Introduzir circuit breaker para proteger tools falhando
- **Conteúdo**:
  - Estados: CLOSED (normal) → OPEN (falhando, rejeita) → HALF-OPEN (testa)
  - Após N falhas consecutivas: OPEN (para de chamar a tool)
  - Após timeout: HALF-OPEN (permite 1 tentativa)
  - Se sucesso: CLOSED; se falha: OPEN
  - Para agentes: se uma tool de API está down, circuit breaker evita desperdício de tokens
- **Diagrama**: State machine — Closed → Open → Half-Open → Closed/Open
- **Animação**: Transições entre estados
- **Tempo**: 1.5 min

---

#### Slide 54 — Composição de Patterns
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar como os patterns se combinam
- **Conteúdo**:
  - Retry + Idempotência: retry é seguro porque idempotência garante não-duplicação
  - Saga + Idempotência: compensações são idempotentes
  - Circuit Breaker + Retry: breaker protege; retry recupera
  - Durable Execution + tudo: Temporal oferece retry, timeout, idempotência embutidos
  - Regra: não reinvente — Temporal já tem a maioria
- **Diagrama**: Matriz de composição
- **Tempo**: 1 min

---

#### Slide 55 — [SEÇÃO] Produção: Ordering, Escala, Observabilidade
- **Tipo**: Seção
- **Objetivo**: Transição para tópicos de produção
- **Conteúdo**: "6 — Produção: Ordering, Escala, Observabilidade"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 56 — Exactly-once vs At-least-once
- **Tipo**: Comparação
- **Objetivo**: Desconstruir o mito do exactly-once
- **Conteúdo**:
  - At-least-once: mensagem pode chegar 1+ vezes (default do Kafka)
  - At-most-once: mensagem pode se perder (fire and forget)
  - Exactly-once: cada mensagem é processada exatamente 1 vez
  - Realidade: exactly-once verdadeiro não existe na presença de falhas
  - Prática: at-least-once + idempotência = "effectively once"
  - Pergunta: *Exactly-once existe de verdade ou é mito?*
- **Diagrama**: Comparação visual dos 3 modelos
- **Tempo**: 1.5 min

---

#### Slide 57 — Sharding de Consumidores
- **Tipo**: Diagrama
- **Objetivo**: Mostrar como escalar consumidores de eventos
- **Conteúdo**:
  - Consumer Group: partições divididas entre consumers
  - Sharding por chave: agent_id → partition → consumer dedicado
  - Adicionar consumers → rebalanceamento automático
  - Limite: # consumers ativos ≤ # partições
  - Para agentes: cada shard processa um conjunto de agentes
- **Diagrama**: Múltiplas partições → múltiplos consumers em paralelo
- **Tempo**: 1 min

---

#### Slide 58 — Distributed Tracing em Pipelines de Agentes
- **Tipo**: Diagrama
- **Objetivo**: Conectar tracing ao contexto event-driven
- **Conteúdo**:
  - Em event-driven: trace espalhado por producer, broker, consumer
  - OpenTelemetry: spans distribuídos com context propagation
  - Trace ID propagado via headers de mensagem
  - Visualização: timeline de spans cruzando serviços
  - Para agentes: cada tool call = span; cada agente = service
  - Aprofundamento em ETHAGT12 (AgentOps)
- **Diagrama**: Trace distribuído com spans em múltiplos serviços
- **Tempo**: 1.5 min

---

#### Slide 59 — Custo da Mensageria
- **Tipo**: Conteúdo
- **Objetivo**: Lembrar que mensageria não é grátis
- **Conteúdo**:
  - Infraestrutura: brokers, ZooKeeper/KRaft, monitoramento
  - Storage: retenção de logs consome disco
  - Network: replicação entre datacenters
  - Operação: equipe de platform engineering
  - Para agentes: cada evento tem custo de storage + processamento
  - Regra: mensure custo por evento antes de escalar
- **Diagrama**: Breakdown de custos (pizza chart conceitual)
- **Tempo**: 1 min

---

#### Slide 60 — V/F: "Event-driven é sempre mais escalável"
- **Tipo**: Exercício
- **Objetivo**: Quebrar o mito da escalabilidade automática
- **Conteúdo**:
  - Verdadeiro ou Falso: "Event-driven é sempre mais escalável"
  - Resposta: **Falso**
  - Event-driven escala horizontalmente, mas introduz overhead de broker, latência de fila, complexidade de debugging
  - Para tarefas simples e síncronas, a escalabilidade não compensa o custo
  - Exercício do syllabus
- **Diagrama**: Card V/F com explicação
- **Tempo**: 1 min

---

### SEÇÃO G — Fechamento (Slides 61-70 · 24 min)

---

#### Slide 61 — [SEÇÃO] Fechamento
- **Tipo**: Seção
- **Objetivo**: Transição para o fechamento
- **Conteúdo**: "7 — Fechamento: Boas Práticas, Caso de Estudo, Quiz"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 62 — Exercício: Saga Compensatória
- **Tipo**: Exercício
- **Objetivo**: Praticar saga em cenário real
- **Conteúdo**:
  - Cenário: sistema de transferência entre contas (debita A → credita B → notifica)
  - Em duplas: escrever a lógica de compensação para cada passo falhar
  - Quais compensações não são perfeitas? (ex.: notificação já enviada)
  - 3 min discussão, 2 min apresentar 2 exemplos
- **Diagrama**: Esqueleto de saga para preencher
- **Tempo**: 5 min

---

#### Slide 63 — Boas Práticas (DO)
- **Tipo**: Conteúdo
- **Objetivo**: Checklist de boas práticas
- **Conteúdo**:
  - Comece com at-least-once + idempotência (não persiga exactly-once)
  - Use chaves de partição para preservar ordering por entidade
  - Coloque I/O em activities; mantenha workflows determinísticos
  - Defina DLQ (dead letter queue) desde o dia 1
  - Monitore lag de consumer (Kafka) / depth de fila (RabbitMQ)
  - Use circuit breakers em tools externas
  - Version seus eventos (schema registry)
- **Diagrama**: Checklist verde (etho-success)
- **Tempo**: 2 min

---

#### Slide 64 — Anti-Patterns (DON'T)
- **Tipo**: Conteúdo
- **Objetivo**: Checklist do que NÃO fazer
- **Conteúdo**:
  - Perseguir exactly-once sem idempotência
  - I/O direto em código de workflow (non-determinism)
  - Sem DLQ (mensagens falhadas somem)
  - Sem schema versioning (quebra consumidores ao evoluir)
  - Ordering global esperado em Kafka (só existe por partição)
  - Sem monitoring de lag (consumer fica atrás sem ninguém saber)
  - Usar Airflow para orquestração em tempo real
  - Começar com Kafka quando RabbitMQ bastava
- **Diagrama**: Checklist vermelho (etho-danger)
- **Tempo**: 2 min

---

#### Slide 65 — Caso de Estudo: Processamento de Documentos em Enterprise
- **Tipo**: Diagrama
- **Objetivo**: Mostrar todos os conceitos em um caso real
- **Conteúdo**:
  - Pipeline: ingestão (Kafka) → classificação (agente) → extração (agente) → validação (HITL) → publicação
  - Temporal orquestra o workflow; agentes são activities
  - Saga compensatória se validação falha
  - Circuit breaker no agente de extração (API de LLM)
  - DLQ para documentos que falham após N retries
  - Distributed tracing via OpenTelemetry
  - Lição: event-driven + durable execution + resiliência = produção
- **Diagrama**: Arquitetura completa do pipeline
- **Tempo**: 3 min

---

#### Slide 66 — Resumo da Aula
- **Tipo**: Resumo
- **Objetivo**: Sintetizar os pontos-chave
- **Conteúdo**:
  - Event-driven = desacoplamento, escala, resiliência (com complexidade)
  - Mensageria: Kafka (log/volume), RabbitMQ (routing), NATS (leveza)
  - Temporal = durable execution: sobreviver a crashes, long-running, HITL
  - Resiliência: retry + idempotência + saga + circuit breaker
  - Produção: at-least-once + idempotência = "effectively once"
  - Determinismo é a regra de ouro do replay
- **Diagrama**: 6 ícones com os pontos-chave
- **Tempo**: 2 min

---

#### Slide 67 — Checklist da Aula
- **Tipo**: Resumo
- **Objetivo**: Confirmar que todos os tópicos foram cobertos
- **Conteúdo**:
  - [ ] Diferenciou síncrono de event-driven
  - [ ] Comparou Kafka, RabbitMQ e NATS
  - [ ] Explicou durable execution e Temporal
  - [ ] Implementou retries e idempotência
  - [ ] Escreveu uma saga compensatória
  - [ ] Discutiu exactly-once vs at-least-once
- **Diagrama**: Checklist visual
- **Tempo**: 1 min

---

#### Slide 68 — Quiz: Pergunta 1
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "Quando Temporal é preferível a Kafka puro?"
  - A) Quando você precisa de máximo throughput
  - B) Quando você precisa de durable execution, HITL e orquestração de workflow
  - C) Quando você quer o broker mais leve
  - D) Quando você não precisa de ordering
  - Resposta: B
- **Tempo**: 1 min

---

#### Slide 69 — Quiz: Pergunta 2
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "Em Kafka, como garantir ordering de mensagens do mesmo agente?"
  - A) Usar ordering global (não existe)
  - B) Usar a mesma chave de partição (agent_id)
  - C) Aumentar o número de partições
  - D) Usar RabbitMQ no lugar
  - Resposta: B
- **Tempo**: 1 min

---

#### Slide 70 — Quiz: Pergunta 3
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "O que quebra um replay no Temporal?"
  - A) Usar `workflow.sleep()` no workflow
  - B) Non-determinism (I/O direto, datetime.now(), random no workflow)
  - C) Chamar activities
  - D) Usar signals
  - Resposta: B
- **Tempo**: 1 min

---

#### Slide 71 — Quiz: Pergunta 4
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "Qual é a estratégia prática para 'effectively once'?"
  - A) Implementar exactly-once delivery no broker
  - B) At-least-once delivery + idempotência no consumidor
  - C) At-most-once + retry infinito
  - D) Usar transações distribuídas (2PC)
  - Resposta: B
- **Tempo**: 1 min

---

#### Slide 72 — Quiz: Pergunta 5
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "Em uma saga de transferência, se o passo 'notificar' falha, o que se faz?"
  - A) Nada — a transferência já foi feita
  - B) Compensar os passos anteriores (estornar crédito e débito)
  - C) Retentar infinitamente até notificar
  - D) Cancelar a transação via 2PC
  - Resposta: B
- **Tempo**: 1 min

---

#### Slide 73 — Conexão com Próximos Módulos
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar como ETHAGT11 conecta com o resto da especialização
- **Conteúdo**:
  - ETHAGT12 — AgentOps: observabilidade + avaliação (aprofunda tracing)
  - ETHAGT14 — Escalabilidade: event-driven em produção em larga escala
  - ETHAGT90 — Projeto final: pipeline event-driven como componente
- **Diagrama**: Mapa da especialização com ETHAGT11 destacado
- **Tempo**: 1 min

---

#### Slide 74 — Projeto do Módulo e Labs
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar projeto e laboratórios
- **Conteúdo**:
  - Projeto: pipeline event-driven para processamento de tickets em massa
    - Durable execution, retries e compensação
    - Entrega: código + ADR + análise de falhas injetadas (chaos)
    - Critério: pipeline sobrevive a ≥2 falhas injetadas sem perda de dados
  - Lab 1 (4h): "Agente com Kafka" — dois agentes coordenados via tópicos
  - Lab 2 (5h): "Workflow durável em Temporal" — agente sobrevivendo a kill
- **Tempo**: 1 min

---

#### Slide 75 — Leitura Recomendada e Referências
- **Tipo**: Referências
- **Objetivo**: Indicar o que ler antes da próxima aula
- **Conteúdo**:
  - Obrigatório: Temporal.io *Durable Execution* primer
  - Obrigatório: Kreps, *The Log* (LinkedIn Engineering)
  - Recomendado: Narkhede et al., *Kafka: The Definitive Guide*
  - Recomendado: Microsoft *Cloud Design Patterns* (saga, CQRS)
  - Complementar: CloudEvents spec (CNCF); NATS docs; RabbitMQ docs
  - Vídeo: Temporal *Durable Execution* talks (YouTube)
- **Tempo**: 1 min

---

#### Slide 76 — Q&A / Encerramento
- **Tipo**: Capa
- **Objetivo**: Abrir para perguntas e encerrar
- **Conteúdo**:
  - "Perguntas?"
  - Contato do professor
  - "Na próxima aula: ETHAGT12 — AgentOps: Observabilidade & Avaliação"
- **Diagrama**: Logo Etho + fundo etho-dark
- **Tempo**: 2 min

---

## Resumo do Storyboard

| Seção | Slides | Tempo | Conteúdo |
|---|---|---|---|
| A — Abertura | 1-6 | 8 min | Capa, objetivos, competências, agenda, motivação (crash no ticket 5.000), contexto (evolução event-driven) |
| B — Por que Event-Driven | 7-13 | 9 min | Limites síncrono, event-driven, benefícios, trade-offs, comparação, exercício |
| C — Mensageria | 14-27 | 15 min | O Log, Kafka (partições, ordering, consumer groups), RabbitMQ, NATS, comparação, CQRS, saga, CloudEvents, DEMO Kafka |
| D — Orquestração de Workflows | 28-36 | 10 min | Workflow vs agente, Temporal (conceitos, durable exec, código), Prefect, Airflow, comparação, decisão |
| E — Durable Execution | 37-46 | 12 min | Crashes, long-running, HITL (timers/signals), replays, non-determinism, DEMO Temporal, exercício |
| F — Resiliência & Produção | 47-60 | 12 min | Retries, idempotência, saga, circuit breakers, composição, exactly-once, sharding, tracing, custo, V/F |
| G — Fechamento | 61-76 | 24 min | Exercício saga, boas práticas, anti-patterns, caso de estudo, resumo, checklist, quiz (5), conexão, projeto, labs, referências, Q&A |
| **Total** | **76** | **90 min** | |

---

## Diagramas Necessários

| # | Slide | Diagrama | Tipo | Fonte |
|---|---|---|---|---|
| D1 | 9 | Event-driven (produtor → broker → consumidor) | Flowchart | `12-Diagrams/ETHAGT11/event-driven.mmd` |
| D2 | 15 | O Log imutável (offsets, consumers) | Flowchart | Kreps *The Log* |
| D3 | 16 | Kafka: arquitetura (topics, partitions, log) | Flowchart | `12-Diagrams/ETHAGT11/event-driven.mmd` |
| D4 | 17 | Kafka: particionamento e ordering por chave | Diagrama | Novo |
| D5 | 18 | Kafka: consumer groups e escala horizontal | Diagrama | Novo |
| D6 | 19 | RabbitMQ: exchanges, bindings, queues | Flowchart | RabbitMQ docs |
| D7 | 21 | Comparação Kafka vs RabbitMQ vs NATS | Tabela 3 colunas | Novo |
| D8 | 23 | CQRS (command → event → read model) | Flowchart | Microsoft *Cloud Design Patterns* |
| D9 | 24 | Saga (visão geral) | Flowchart | `12-Diagrams/ETHAGT11/saga.mmd` |
| D10 | 25 | CloudEvent (JSON exemplo) | Código | CNCF CloudEvents spec |
| D11 | 30 | Temporal: arquitetura (server, worker, task queue) | Flowchart | Temporal docs |
| D12 | 31 | Durable execution (crash → recovery) | Sequência | `12-Diagrams/ETHAGT11/durable-execution.mmd` |
| D13 | 35 | Comparação Temporal vs Prefect vs Airflow | Tabela | Novo |
| D14 | 38 | Sobreviver a crashes (checkpoint + replay) | Sequência | `12-Diagrams/ETHAGT11/durable-execution.mmd` |
| D15 | 40 | HITL via timers e signals | Sequência | Novo |
| D16 | 42 | Non-determinism quebrando replay | Comparação | Novo |
| D17 | 51 | Saga pattern (execute + compensação) | Flowchart | `12-Diagrams/ETHAGT11/saga.mmd` |
| D18 | 52 | Saga: transferência entre contas | Flowchart | `12-Diagrams/ETHAGT11/saga.mmd` |
| D19 | 53 | Circuit breaker (state machine) | State diagram | Novo |
| D20 | 56 | Exactly-once vs at-least-once vs at-most-once | Comparação | Novo |
| D21 | 57 | Sharding de consumidores | Diagrama | Novo |
| D22 | 58 | Distributed tracing (spans em múltiplos serviços) | Timeline | OpenTelemetry |
| D23 | 65 | Caso de estudo: pipeline enterprise completo | Flowchart | Novo |
| D24 | 73 | Mapa da especialização com ETHAGT11 | Mind map | Novo |

---

## Pontos de Engajamento

| # | Slide | Tipo | Interação | Tempo |
|---|---|---|---|---|
| E1 | 5 | Pergunta aberta | *Qual o pior crash que você já viu em produção?* | 1 min |
| E2 | 13 | Exercício rápido | Votação: síncrono ou assíncrono? (4 cenários) | 1.5 min |
| E3 | 17 | Pergunta conceitual | *Como garantir ordering de mensagens do mesmo agente?* | — |
| E4 | 26 | DEMO ao vivo | Agente com Kafka — dois agentes coordenados via tópicos | 3 min |
| E5 | 27 | Discussão em duplas | *O que acontece se processar a mesma mensagem 2x?* | 1.5 min |
| E6 | 29 | Pergunta aberta | *Você orquestra via código ou via agente supervisor?* | — |
| E7 | 44 | DEMO ao vivo | Workflow durável em Temporal — sobrevivendo a kill | 3 min |
| E8 | 45 | Discussão aberta | *Replay quebra se tool externa mudou de comportamento?* | 2 min |
| E9 | 46 | Exercício em duplas | HITL com signal: esboçar workflow de aprovação | 3 min |
| E10 | 50 | Pergunta conceitual | *Como garantir idempotência em tool de "enviar email"?* | — |
| E11 | 56 | Pergunta provocativa | *Exactly-once existe de verdade ou é mito?* | — |
| E12 | 60 | V/F | *Event-driven é sempre mais escalável* | 1 min |
| E13 | 62 | Exercício em duplas | Saga compensatória: transferência entre contas | 5 min |
| E14 | 68-72 | Quiz (5 perguntas) | Múltipla escolha com respostas | 5 min |

---

## Pendências de Produção

- [ ] Criar diagramas no diretório `12-Diagrams/ETHAGT11/`: event-driven.mmd, saga.mmd, durable-execution.mmd
- [ ] Produzir 15 diagramas novos (D2, D4, D5, D6, D7, D8, D10, D11, D13, D15, D16, D19, D20, D21, D22, D23, D24)
- [ ] Screenshot da Temporal Web UI com execução em andamento (Slide 44)
- [ ] Screenshot do código com syntax highlighting (Slides 26, 32, 33, 43, 44, 50)
- [ ] Imagem de fundo para capa (Slide 1)
- [ ] Badge de competências (Slide 3)
- [ ] Timeline de marcos históricos (Slide 6)
- [ ] Preparar ambiente Docker Compose para DEMO Kafka (Slide 26)
- [ ] Preparar ambiente Temporal local para DEMO durable execution (Slide 44)

---

> **Aguardando aprovação deste storyboard para gerar os slides detalhados com notas do professor.**
