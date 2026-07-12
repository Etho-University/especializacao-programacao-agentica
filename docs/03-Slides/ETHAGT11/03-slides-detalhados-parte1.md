# ETHAGT11 — Slides Detalhados + Notas do Professor (Parte 1: Slides 1-38)

> Universidade Etho · Especialização em Programação Agêntica
> Cada slide contém: título, objetivo, conteúdo, notas do professor, diagrama, animação, imagem, tempo.

---

## SEÇÃO A — Abertura (Slides 1-6 · 8 min)

---

### Slide 1 — Capa

**Título**: ETHAGT11 — Event-Driven Agents & Workflow Orchestration
**Objetivo**: Identificar a aula, o professor e o contexto dentro da especialização.
**Conteúdo**:
- ETHAGT11 — Event-Driven Agents & Workflow Orchestration
- Universidade Etho · Especialização em Programação Agêntica
- Fase C — Orquestração & Produção · 25 h
- Professor · Data

**Diagrama**: Logo Etho (canto sup. esquerdo) + imagem de fundo abstrata (fluxos de eventos, topologias de mensageria)
**Animação**: Fade in do título (300ms)
**Imagem**: Fundo `etho-dark` (#0F1E2D) com pattern sutil de nós e fluxos
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Bem-vindos. Chegamos à Fase C — Orquestração & Produção. Hoje vamos falar de como construir sistemas de agentes que sobrevivem a falhas, executem por horas ou dias, e coordenem via eventos. Se até agora vocês construíram agentes síncronos que morrem no primeiro crash, hoje isso muda.
💡 ANALOGIA: É como a diferença entre enviar um email (assíncrono, resiliente) e fazer uma ligação telefônica (síncrono, ambos precisam estar presentes). Hoje vocês vão aprender o "email" da orquestração de agentes.
❓ PERGUNTA PARA A TURMA: "Quantos de vocês já tiveram um agente que caiu no meio de um processamento longo e perdeu tudo?" (levantar mãos — calibrar dor real)
⚠️ ERROS COMUNS: Alunos chegam achando que Kafka resolve tudo. Kafka é uma peça — não é a solução completa. Durabilidade de execução (Temporal) é o complemento essencial.
➡️ TRANSIÇÃO: "Vamos começar definindo o que vocês vão conseguir fazer ao final desta aula."

---

### Slide 2 — Objetivos do Módulo

**Título**: Objetivos do Módulo
**Objetivo**: Deixar claro o que o aluno deve conseguir FAZER ao final da aula.
**Conteúdo**:
- **Objetivo geral**: Construir sistemas de agentes orientados a eventos com orquestração robusta (durable execution, filas, workflows de longa duração)
- **Objetivos específicos**:
  1. Diferenciar orquestração síncrona de event-driven assíncrona
  2. Aplicar filas (Kafka, RabbitMQ, NATS) para coordenação de agentes
  3. Implementar durable execution (Temporal, Prefect) para workflows longos
  4. Lidar com falhas, retries, idempotência, compensação
  5. Avaliar escala, ordering, exactly-once vs at-least-once

**Diagrama**: 5 ícones representando cada objetivo (eventos, filas, engrenagem durável, escudo, escala)
**Animação**: Objetivos aparecem um a um (on click)
**Imagem**: Ícones minimalistas em `etho-accent` (#E85D2F)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Cada objetivo é mensurável. Não é "entender event-driven" — é "diferenciar", "aplicar", "implementar", "lidar", "avaliar". Se ao final da aula você não consegue fazer essas cinco coisas, eu falhei como professor. Vamos revisar estes objetivos no final.
💡 ANALOGIA: É como um checklist de pré-voo do piloto. Cada item é verificado: flaps, trem, motor. Hoje nosso checklist é estes 5 objetivos.
❓ PERGUNTA PARA A TURMA: "Qual desses objetivos vocês acham mais desafiador?" (deixar responder — costuma ser #3 durable execution ou #5 exactly-once)
⚠️ ERROS COMUNS: Alunos confundem "aprender Kafka" com "aprender event-driven". Kafka é uma ferramenta; event-driven é um paradigma. O objetivo #1 é paradigmático, não técnico.
➡️ TRANSIÇÃO: "Antes de saber o que vamos fazer, vamos ver onde estamos no Framework Etho."

---

### Slide 3 — Competências Desenvolvidas

**Título**: Competências Desenvolvidas
**Objetivo**: Conectar a aula ao Framework Etho de competências.
**Conteúdo**:

| Competência | Nível ao final | Próximo nível em |
|---|---|---|
| C1 Programação Agêntica | **A** (Avançado) | ETHAGT90 (Projeto final) |
| C2 Multi-Agent Systems | **A** (Avançado) | ETHAGT90 |
| C3 MCP & Tool Use | B (Básico) | — |
| C4 Agent Memory | B (Básico) | — |
| C5 AgentOps & Avaliação | I (Intermediário) | ETHAGT12 |

**Diagrama**: Radar chart com 5 eixos mostrando nível B/I/A
**Animação**: Radar aparece com wipe (left-to-right, 500ms)
**Imagem**: Badge visual por competência (círculos coloridos)
**Tempo**: 1 min

**Rodape**: AgentOps = Agent Operations — operacao e monitoramento de agentes em producao  ·  MCP = Model Context Protocol — Protocolo de Contexto de Modelo

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O Framework Etho tem 6 competências em 3 níveis. Este módulo eleva C1 e C2 ao nível Avançado — significa que vocês vão ser capazes de arquitetar sistemas multi-agente orientados a eventos em produção. C5 atinge Intermediário aqui (vocês veem tracing distribuído, mas AgentOps profunda vem em ETHAGT12).
💡 ANALOGIA: Vocês já sabem dirigir na cidade (Básico). Em ETHAGT10 (multi-agente), aprenderam rodovia (Intermediário). Agora vão dirigir em tráfego intenso com GPS e sistemas de segurança (Avançado).
⚠️ ERROS COMUNS: Alunos acham que "Avançado" significa "domínio total". Avançado significa que você arquiteta, justifica e opera. Domínio de produção vem com experiência.
➡️ TRANSIÇÃO: "Vamos ver como esta aula está estruturada."

---

### Slide 4 — Agenda

**Título**: Agenda da Aula
**Objetivo**: Mostrar o roteiro da aula com tempos estimados.
**Conteúdo**:
- **Bloco 1 (45 min)**:
  - Abertura (8 min) — objetivos, motivação (crash no ticket 5.000), contexto
  - Por que Event-Driven (9 min) — limites síncrono, paradigma, trade-offs
  - Mensageria (15 min) — Kafka, RabbitMQ, NATS, CQRS, saga, CloudEvents, DEMO
  - Workflows (10 min) — Temporal, Prefect, Airflow, decisão
  - Intervalo (3 min)
- **Bloco 2 (45 min)**:
  - Durable Execution (12 min) — crashes, long-running, HITL, replays, DEMO
  - Resiliência & Produção (12 min) — retries, idempotência, saga, circuit breakers
  - Fechamento (18 min) — boas práticas, caso de estudo, quiz, projeto, Q&A

**Diagrama**: Timeline horizontal com 7 seções coloridas
**Animação**: Timeline cresce da esquerda para direita (500ms)
**Imagem**: Ícones de relógio por seção
**Tempo**: 1 min

**Rodape**: HITL = Human-in-the-Loop — Humano no Ciclo

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A aula tem dois blocos. O primeiro cobre fundamentos (por que event-driven), mensageria (a "poeira" de brokers) e workflow engines. O segundo aprofunda durable execution, resiliência e fecha com boas práticas. Há duas DEMOS ao vivo — uma com Kafka, outra com Temporal.
💡 ANALOGIA: É como um prato de degustação. Entrada (abertura), prato principal (mensageria + workflows), sobremesa (durable execution), café (resiliência), e o 'petit four' (fechamento). Cada parte tem propósito.
⚠️ ERROS COMUNS: Alunos chegam atrasados e perdem a motivação. Avisar que o Slide 5 (crash no ticket 5.000) define o tom de toda a aula.
➡️ TRANSIÇÃO: "Vamos começar pelo porquê. Por que estamos aqui?"

---

### Slide 5 — Motivação: O Crash no Ticket 5.000

**Título**: O Crash no Ticket 5.000
**Objetivo**: Criar tensão — agentes síncronos perdem tudo em crash.
**Conteúdo**:
- **Cenário**: Agente processando 10.000 tickets de suporte em série
- O processo cai no ticket 5.000 — recomeça do zero
- Horas de processamento perdidas, custo de API desperdiçado
- **Sem durability**: cada retry recomeça do ticket 1
- **Com durability**: retoma do ticket 5.001
- **Pergunta**: *Qual o pior crash que você já viu em produção?*

**Diagrama**: Timeline de execução com "X" vermelho no ticket 5.000 → recomeço do zero (sem durability) vs retomada (com durability)
**Animação**: Barra de progresso avança até 50%, trava (X vermelho), volta ao zero (sem durability) / continua (com durability)
**Imagem**: Ícone de progress bar com marcador de falha
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Este é o problema central da aula. Um agente síncrono processando 10.000 tickets — cada um exige uma chamada de LLM (custo + latência). Se o processo cai no ticket 5.000, você perde metade do trabalho. Sem durability, cada restart recomeça do zero. Com durable execution, o sistema retoma exatamente do último checkpoint.
💡 ANALOGIA: É como escrever um documento de 100 páginas sem salvar. Se o computador cai na página 50, você recomeça do zero. Com auto-save, você perde no máximo 1 parágrafo.
❓ PERGUNTA PARA A TURMA: "Qual o pior crash que vocês já viram em produção?" (deixar 2-3 alunos compartilharem — histórias de dor são engajadoras)
⚠️ ERROS COMUNS: Alunos acham que "retry resolve". Retry sem durability recomeça do início. O problema não é a falha — é a perda de progresso.
➡️ TRANSIÇÃO: "Essa solução não veio do nada. Vamos ver como chegamos aqui."

---

### Slide 6 — Contexto: Evolução para Event-Driven

**Título**: Evolução para Event-Driven
**Objetivo**: Explicar a confluência que tornou event-driven essencial para agentes.
**Conteúdo**:
- **Linha do tempo**:
  - 2011: Kafka na LinkedIn (processamento de logs em escala)
  - 2016: Predecessores do Temporal (Cadence, SWF)
  - 2019: Temporal open source
  - 2023: Agentes de longa duração entram em pauta
  - 2024: Durable execution para LLM agents amadurece
- **Confluência**: agentes longos + custo de recomputação + necessidade de resiliência
- Kreps *The Log* como fundamento conceitual
- CloudEvents (CNCF) como padrão emergente

**Diagrama**: Timeline horizontal com marcos (2011 → 2024)
**Animação**: Marcos aparecem sequencialmente da esquerda
**Imagem**: Ícones por marco (log, engrenagem, código, agente, durability)
**Tempo**: 1 min

**Rodape**: LLM = Large Language Model — Modelo de Linguagem de Grande Escala

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Event-driven não é novo — Kafka existe desde 2011. Mas a combinação com agentes de LLM é recente. Agentes executam por minutos ou horas (vs segundos das aplicações tradicionais), o custo de recomputação é alto (cada token custa), e a necessidade de HITL (esperar humano aprovar) exige pausas duráveis. Tudo isso convergiu em 2024.
💡 ANALOGIA: É como a invenção do avião. Os princípios (aerodinâmica) existiam há séculos, mas precisou do motor leve + materiais + controle de voo para decolar. Event-driven + agentes precisou do LLM barato + workflow engines maduras + casos de uso reais.
⚠️ ERROS COMUNS: Alunos acham que event-driven é "modinha". O conceito tem 15 anos; a aplicação a agentes é o que é novo.
➡️ TRANSIÇÃO: "Vamos entender os fundamentos do paradigma event-driven."

---

## SEÇÃO B — Por que Event-Driven (Slides 7-13 · 9 min)

---

### Slide 7 — [SEÇÃO] Por que Event-Driven

**Título**: Por que Event-Driven
**Objetivo**: Transição para o bloco de fundamentos.
**Conteúdo**: Número "1" grande + "Por que Event-Driven"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Fade in do número e título
**Imagem**: —
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Início do bloco de fundamentos. Antes de falar de Kafka, Temporal e ferramentas, precisamos entender o PORQUÊ. Por que event-driven? O que ele resolve? O que ele custa?
➡️ TRANSIÇÃO: "Comecemos pelo que estava antes — e por que quebra."

---

### Slide 8 — Limites da Orquestração Síncrona

**Título**: Limites da Orquestração Síncrona
**Objetivo**: Mostrar onde a orquestração síncrona quebra.
**Conteúdo**:
- **Acoplamento temporal**: caller e callee devem estar vivos ao mesmo tempo
- **Falta de resiliência**: falha no meio = perda de progresso
- **Difícil escalar**: bottleneck no orquestrador síncrono
- **Custo de recomputação**: cada retry recomeça do zero
- **Exemplo**: agente que processa 10 tools em série — se cai na tool 7, perde tudo

**Diagrama**: Cadeia síncrona com ponto de falha destacado (vermelho na posição 7)
**Animação**: Falha aparece em vermelho na posição 7; cadeia inteira fica vermelha
**Imagem**: Ícone de corrente com elo quebrado
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Orquestração síncrona funciona bem para tarefas curtas (segundos). Mas quando o pipeline é longo (minutos, horas), cada limite se manifesta. Acoplamento temporal significa que se o callee cai, o caller trava. Falta de resiliência significa que o progresso é volátil. Custo de recomputação significa que retries são caros.
💡 ANALOGIA: É como uma linha de montagem onde se uma estação para, toda a linha para. E se a peça cair no chão, você recomeça desde a matéria-prima.
❓ PERGUNTA PARA A TURMA: "Vocês têm algum pipeline síncrono hoje que já quebrou por essas razões?"
⚠️ ERROS COMUNS: Alunos acham que "retry simples" resolve. Retry sem durability recomeça do início. Retry sem idempotência duplica trabalho.
➡️ TRANSIÇÃO: "Qual é a alternativa? Vamos definir event-driven."

---

### Slide 9 — O que é Event-Driven

**Título**: O que é Event-Driven
**Objetivo**: Definir o paradigma event-driven de forma clara.
**Conteúdo**:
- Componentes se comunicam via **eventos** (mensagens assíncronas)
- **Produtor** publica evento → **broker** roteia → **consumidor** processa
- **Desacoplamento temporal**: produtor e consumidor não precisam coincidir
- **Desacoplamento espacial**: não precisam se conhecer
- **Evento** = fato que ocorreu (passado), não comando (futuro)
- "PedidoCriado" (evento) vs "CriarPedido" (comando)

**Diagrama**: `12-Diagrams/ETHAGT11/event-driven.mmd`
**Animação**: Produtor → broker → consumidor aparecem sequencialmente
**Imagem**: Diagrama de fluxo com producer (azul), broker (laranja), consumer (rosa)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A definição canônica de event-driven: componentes se comunicam via eventos assíncronos. A distinção crucial é: evento é um FATO que ocorreu (passado), não um comando (futuro). "PedidoCriado" é um evento — notifica que algo aconteceu. "CriarPedido" é um comando — instrui algo a fazer. Eventos são imutáveis; comandos podem falhar.
💡 ANALOGIA: É como um jornal. O jornal notifica "Choveu ontem" (evento). Um bilhete dizendo "Regue as plantas amanhã" é um comando. Eventos informam; comandos instruem.
❓ PERGUNDA PARA A TURMA: "Em seus sistemas, vocês usam eventos ou comandos para comunicação entre agentes?"
⚠️ ERROS COMUNS: Alunos modelam tudo como comandos. "AgenteB, processe o documento X" é comando. "DocumentoXRecebido" é evento. Eventos são mais desacoplados — múltiplos consumers podem reagir.
➡️ TRANSIÇÃO: "Vamos ver os benefícios concretos."

---

### Slide 10 — Benefícios: Desacoplamento, Escala, Resiliência

**Título**: Benefícios do Event-Driven
**Objetivo**: Listar os ganhos concretos do paradigma.
**Conteúdo**:
- **Desacoplamento**: componentes evoluem independentemente
- **Escala horizontal**: consumidores paralelos por partição
- **Resiliência**: broker persiste eventos; consumers recuperam de onde pararam
- **Replay**: reprocessar histórico de eventos (corrigir bugs retroativamente)
- **Backpressure natural**: consumer puxa no seu ritmo (não é empurrado)

**Diagrama**: 5 ícones com labels (`etho-success` verde)
**Animação**: Ícones surgem um a um (on click)
**Imagem**: Ícones: elos soltos, barras paralelas, escudo, replay, funil
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Os 5 benefícios são concretos. Desacoplamento: adicionar um novo consumer não exige mudar o produtor. Escala horizontal: adicionar consumers ao consumer group aumenta paralelismo. Resiliência: o broker persiste eventos — se o consumer cai, ele recupera do offset. Replay: voltar o offset e reprocessar (útil para corrigir bugs). Backpressure: o consumer puxa no seu ritmo, evitando sobrecarga.
💡 ANALOGIA: É como uma biblioteca. Desacoplamento: cada leitor lê independente. Escala: adicione mais leitores. Resiliência: o livro fica na prateleira até alguém pegar. Replay: releia um livro. Backpressure: cada leitor lê no seu ritmo.
⚠️ ERROS COMUNS: Alunos acham que replay é "recalcular tudo". Replay é reprocessar eventos — o input é o mesmo, mas a lógica do consumer mudou.
➡️ TRANSIÇÃO: "Mas event-driven não é grátis. Vamos ser honestos sobre o custo."

---

### Slide 11 — Trade-offs: Complexidade, Eventual Consistency, Debugging

**Título**: Trade-offs do Event-Driven
**Objetivo**: Ser honesto sobre o preço do paradigma.
**Conteúdo**:
- **Complexidade**: mais componentes móveis (broker, consumers, DLQ)
- **Eventual consistency**: estado converge apenas depois de processar eventos
- **Debugging distribuído**: trace espalhado por serviços
- **Ordering**: garantir ordem global é caro ou impossível
- "Event-driven não é grátis — é uma troca consciente"

**Diagrama**: Balança: benefícios (esquerda) vs custos (direita)
**Animação**: Balança inclina conforme itens são adicionados
**Imagem**: Ícone de balança
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Os 4 trade-offs são reais. Complexidade: você agora opera um broker, configura consumers, gerencia DLQ. Eventual consistency: o estado final só é garantido após todos os eventos serem processados — pode haver delay. Debugging: um bug pode estar em qualquer serviço do pipeline — precisa de distributed tracing. Ordering: ordenação global exige coordenação cara.
💡 ANALOGIA: É como trocar uma reunião presencial (síncrono, simples, todos presentes) por assíncrono via email (flexível, mas você perde a certeza de que todos leram na ordem).
❓ PERGUNTA PARA A TURMA: "Qual desses trade-offs mais preocupa vocês em produção?"
⚠️ ERROS COMUNS: Alunos adotam event-driven sem considerar o custo operacional. Broker caiu? Quem monitora? Consumer em deadlock? Quem debuga?
➡️ TRANSIÇÃO: "Vamos sistematizar: quando síncrono, quando assíncrono?"

---

### Slide 12 — Síncrono vs Assíncrono (Comparação)

**Título**: Síncrono vs Assíncrono
**Objetivo**: Sistematizar quando cada paradigma se aplica.
**Conteúdo**:

| Critério | Síncrono | Assíncrono (Event-Driven) |
|---|---|---|
| Latência | Baixa (ms) | Alta (segundos+) |
| Acoplamento | Alto | Baixo |
| Resiliência | Frágil | Resiliente |
| Escala | Vertical | Horizontal |
| Complexidade | Baixa | Alta |
| Consistência | Imediata | Eventual |

- **Híbrido**: síncrono para UX, assíncrono para processamento pesado
- **Pergunta**: *Suas tools de agente são síncronas ou assíncronas?*

**Diagrama**: 3 colunas comparativas (Síncrono / Assíncrono / Híbrido)
**Animação**: Colunas aparecem uma a uma
**Imagem**: Ícones por coluna
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A comparação mostra que nenhum paradigma é universalmente melhor. Síncrono para UX (usuário esperando resposta), baixa latência, simplicidade. Assíncrono para processamento pesado, resiliência, escala. Híbrido é o mais comum: API síncrona recebe request, dispara processamento assíncrono, retorna imediatamente; cliente consulta status depois.
💡 ANALOGIA: Síncrono é como um fast-food (você espera no balcão). Assíncrono é como um restaurante com garçom (você pede, faz outra coisa, a comida chega). Híbrido é como iFood (você pede, recebe número, consulta status).
❓ PERGUNTA PARA A TURMA: "Suas tools de agente hoje são síncronas ou assíncronas? Por quê?"
⚠️ ERROS COMUNS: Alunos tentam fazer tudo assíncrono. UX não pode ser assíncrona — usuário espera resposta. O truque é separar o que precisa ser síncrono (UX) do que pode ser assíncrono (processamento).
➡️ TRANSIÇÃO: "Vamos praticar a decisão."

---

### Slide 13 — Exercício Rápido: Síncrono ou Assíncrono?

**Título**: Exercício: Síncrono ou Assíncrono?
**Objetivo**: Praticar a decisão em cenários reais.
**Conteúdo**:
- 4 cenários curtos:
  1. "Responder pergunta do usuário em chat" → ?
  2. "Processar 10.000 documentos" → ?
  3. "Buscar em RAG e responder" → ?
  4. "Coordenar 3 agentes em pipeline longo" → ?
- Votação rápida (mãos levantadas)

**Diagrama**: 4 cards com cenários
**Animação**: Cards aparecem um a um; respostas reveladas após votação
**Imagem**: Cards coloridos
**Tempo**: 1.5 min

**Rodape**: RAG = Retrieval-Augmented Generation — Geracao Aumentada por Recuperacao

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Respostas: (1) Síncrono — usuário espera resposta em chat. (2) Assíncrono — processamento em massa, longa duração. (3) Síncrono com timeout — baixa latência, mas com fallback. (4) Assíncrono — coordenação complexa, longa duração. O ponto não é acertar — é justificar.
💡 ANALOGIA: É como decidir entre ligação (síncrono) e email (assíncrono) para cada situação.
❓ PERGUNTA PARA A TURMA: Votar em cada cenário. Anotar distribuição na lousa.
⚠️ ERROS COMUNS: Alunos respondem "assíncrono" para tudo. UX NÃO pode ser assíncrona — usuário não espera minutos por uma resposta de chat.
➡️ TRANSIÇÃO: "Com a decisão clara, vamos ao motor que faz event-driven acontecer: a mensageria."

---

## SEÇÃO C — Mensageria (Slides 14-27 · 15 min)

---

### Slide 14 — [SEÇÃO] Mensageria

**Título**: Mensageria: Kafka, RabbitMQ, NATS
**Objetivo**: Transição para o bloco de mensageria.
**Conteúdo**: "2 — Mensageria: Kafka, RabbitMQ, NATS"
**Diagrama**: Fundo `etho-primary`
**Animação**: Fade in do número e título
**Imagem**: —
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O coração do event-driven é a mensageria. Vamos cobrir os três brokers mais relevantes: Kafka (log de eventos em escala), RabbitMQ (routing rico), NATS (leveza e performance). Não vamos decorar APIs — vamos entender os modelos para saber escolher.
➡️ TRANSIÇÃO: "Comecemos pelo conceito fundacional de todos eles: o Log."

---

### Slide 15 — O Log como Abstração Central

**Título**: O Log como Abstração Central
**Objetivo**: Apresentar o conceito fundacional de Kafka.
**Conteúdo**:
- "O Log" (Kreps, LinkedIn) — append-only, ordenado, imutável
- **Tópico** = log particionado; cada partição é uma sequência ordenada
- **Consumer** mantém **offset** (posição no log)
- **Replay**: voltar o offset e reprocessar
- Fonte: Kreps, *The Log*

**Diagrama**: Log imutável com offsets (0, 1, 2, 3...) e consumers lendo em posições diferentes
**Animação**: Mensagens são appendadas no log; consumers avançam offset
**Imagem**: Representação visual de um log com setas de consumers
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Jay Kreps (co-criador do Kafka) escreveu "The Log" — um essay seminal. A ideia central: o log é a abstração mais poderosa em sistemas distribuídos. Append-only (só adiciona, nunca modifica), ordenado (ordem de chegada preservada), imutável (mensagens não mudam). Consumer mantém um offset (posição). Replay = voltar o offset.
💡 ANALOGIA: É como o diário de bordo de um navio. Cada entrada é adicionada no fim (append-only), na ordem (ordenado), e nunca é apagada (imutável). O capitão lê a partir de onde parou (offset).
❓ PERGUNTA PARA A TURMA: "Por que o log é imutável? Por que não modificar mensagens?"
⚠️ ERROS COMUNS: Alunos acham que log é "log de aplicação" (texto para debug). O Log de Kreps é uma estrutura de dados distribuída — fonte de verdade.
➡️ TRANSIÇÃO: "Kafka é a implementação mais famosa do Log. Vamos ver sua anatomia."

---

### Slide 16 — Kafka: Arquitetura (Topics, Partitions, Log)

**Título**: Kafka: Arquitetura
**Objetivo**: Mostrar a anatomia do Kafka.
**Conteúdo**:
- **Topic** → N **partitions** → cada partition é um log imutável
- **Producer** escreve em partition (por key ou round-robin)
- **Consumer Group**: um consumer por partition
- **Replicação**: leader + followers por partition
- **Retenção** por tempo ou tamanho

**Diagrama**: `12-Diagrams/ETHAGT11/event-driven.mmd` (parte Kafka)
**Animação**: Componentes surgem do tópico para fora (topic → partitions → consumers)
**Imagem**: Diagrama de arquitetura Kafka
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Kafka organiza mensagens em tópicos. Cada tópico é dividido em partições — cada partição é um log independente. Produtores escrevem escolhendo a partição (por chave ou round-robin). Consumers se organizam em grupos — cada partição é consumida por exatamente um consumer no grupo. Replicação garante durabilidade: cada partição tem um leader e followers.
💡 ANALOGIA: É como uma biblioteca com várias estantes (partições). Cada estante tem livros em ordem. Vários bibliotecários (consumers) podem ler estantes diferentes em paralelo, mas dois não leem a mesma estante simultaneamente.
⚠️ ERROS COMUNS: Alunos confundem partição com fila. Partição é um log (mensagens ficam); fila é consumida (mensagens somem).
➡️ TRANSIÇÃO: "Vamos aprofundar no particionamento — é onde a mágica do ordering acontece."

---

### Slide 17 — Kafka: Particionamento e Ordering

**Título**: Kafka: Particionamento e Ordering
**Objetivo**: Explicar o modelo de ordering do Kafka.
**Conteúdo**:
- Ordering garantido **dentro** de uma partição, não global
- **Key** = agente_id → mesmo agente → mesma partição → ordering preservado
- Sem key → round-robin → sem ordering garantido
- **Pergunta**: *Como garantir que mensagens do mesmo agente vão para a mesma partição?*
- **Resposta**: `hash(key) % num_partitions`

**Diagrama**: 3 partições com mensagens coloridas por agent_id (mesma cor = mesma partição)
**Animação**: Mensagens com mesma key caem na mesma partição (visual)
**Imagem**: Diagrama com chaves hasheadas para partições
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esta é a regra mais importante do Kafka: ordering é por partição, não global. Se você precisa que as mensagens do "agente 42" sejam processadas em ordem, use agent_id como key. Kafka garante que todas as mensagens com a mesma key vão para a mesma partição (via hash). Dentro da partição, a ordem é preservada.
💡 ANALOGIA: É como filas de banco. Múltiplos caixas (partições) atendem em paralelo. Se você quer que suas transações sejam processadas em ordem, você precisa ir sempre ao mesmo caixa (mesma key = mesma partição).
❓ PERGUNTA PARA A TURMA: "Ordering por partição — como garantir que mensagens do mesmo agente vão pra mesma partição?" (resposta: hash da key)
⚠️ ERROS COMUNS: Alunos esperam ordering global em Kafka. Não existe. Se você precisa de ordering global, tem 1 partição — e perde paralelismo. É um trade-off.
➡️ TRANSIÇÃO: "Vamos ver como escalar consumidores."

---

### Slide 18 — Kafka: Consumer Groups e Escala Horizontal

**Título**: Kafka: Consumer Groups e Escala Horizontal
**Objetivo**: Mostrar como Kafka escala consumidores.
**Conteúdo**:
- **Consumer Group**: conjunto de consumers que dividem as partições
- 1 consumer por partição dentro do grupo
- Adicionar consumers → **rebalanceamento** → mais paralelismo
- **Limite**: # consumers ≤ # partições
- **Offset commit**: at-least-once (commit após processar) vs at-most-once (commit antes)

**Diagrama**: 3 partições → 3 consumers em um group (setas de atribuição)
**Animação**: Consumers aparecem; setas de atribuição partition→consumer surgem
**Imagem**: Diagrama de consumer group
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Consumer Group é como Kafka escala horizontalmente. Um grupo de consumers divide as partições — cada partição vai para um consumer. Se você tem 3 partições e adiciona 4 consumers, o 4º fica ocioso (limite: 1 consumer por partição). Para escalar mais, adicione partições. O offset commit define a semântica: commit após processar = at-least-once (pode reprocessar); commit antes = at-most-once (pode perder).
💡 ANALOGIA: É como uma equipe de entregadores dividindo zonas da cidade. Cada zona (partição) é entregue por um entregador (consumer). Adicione mais zonas para contratar mais entregadores.
⚠️ ERROS COMUNS: Alunos adicionam consumers sem adicionar partições e não veem ganho. O limite é o número de partições.
➡️ TRANSIÇÃO: "Kafka é o log. Mas existem outros modelos. Vamos ao RabbitMQ."

---

### Slide 19 — RabbitMQ: Filas, Exchanges, Routing

**Título**: RabbitMQ: Filas, Exchanges, Routing
**Objetivo**: Apresentar o modelo AMQP do RabbitMQ.
**Conteúdo**:
- **Exchange** → **binding** → **queue**
- Tipos de exchange: **direct**, **topic**, **fanout**, **headers**
- **Routing rico**: mensagens vão para filas baseadas em routing key
- **ACK manual**: consumer ack após processar
- **Dead letter exchange** para mensagens que falham

**Diagrama**: Exchange → bindings → múltiplas queues → consumers
**Animação**: Mensagem roteada por routing key para queue correta
**Imagem**: Diagrama AMQP
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: RabbitMQ segue o modelo AMQP. A diferença vs Kafka: RabbitMQ é orientado a filas (mensagem é consumida e some), Kafka é orientado a log (mensagem fica até retenção expirar). RabbitMQ brilha em routing rico: exchanges decidem para quais filas a mensagem vai, baseado em routing key e tipo (direct, topic, fanout, headers). ACK manual garante que mensagem não é perdida se consumer falha.
💡 ANALOGIA: Kafka é um jornal (todo mundo lê a mesma edição, fica arquivada). RabbitMQ é uma central de taxistas (cada chamada vai para um taxista específico baseado em zona).
❓ PERGUNTA PARA A TURMA: "Em que cenário RabbitMQ é melhor que Kafka?"
⚠️ ERROS COMUNS: Alunos usam Kafka quando precisavam de RabbitMQ (routing complexo, request/reply). Kafka não é bom para routing dinâmico.
➡️ TRANSIÇÃO: "E para quem quer leveza extrema? NATS."

---

### Slide 20 — NATS: JetStream, Leveza, Performance

**Título**: NATS: JetStream, Leveza, Performance
**Objetivo**: Apresentar a alternativa leve.
**Conteúdo**:
- **NATS**: mensagem simples, baixíssima latência, single binary
- **JetStream**: persistência, streams, consumers duráveis
- Modelos: at-least-once, exactly-once (com dedup window)
- Ideal para **edge**, IoT, sistemas embarcados
- Comparação de throughput: NATS > RabbitMQ > Kafka (em mensagens pequenas)

**Diagrama**: Tabela de características NATS vs Kafka vs RabbitMQ (resumida)
**Animação**: Tabela aparece com wipe
**Imagem**: Logo NATS + tabela comparativa
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: NATS é o "canivete suíço" da mensageria. Single binary, baixíssima latência (sub-milissegundo), simples de operar. JetStream adiciona persistência (streams duráveis). É ideal para edge computing, IoT, sistemas embarcados. O trade-off: menos features que Kafka/RabbitMQ. Se você precisa de ecosystem massivo (Kafka Connect, KSQL), fique com Kafka. Se precisa de simplicidade e performance, NATS.
💡 ANALOGIA: Kafka é um caminhão (carrega muito, pesado). RabbitMQ é uma van (flexível). NATS é uma moto (rápido, leve, mas carrega menos).
⚠️ ERROS COMUNS: Alunos subestimam NATS por ser menos famoso. Em muitos casos, NATS resolve o problema com 1/10 da complexidade operacional do Kafka.
➡️ TRANSIÇÃO: "Vamos comparar os três lado a lado."

---

### Slide 21 — Comparação: Kafka vs RabbitMQ vs NATS

**Título**: Kafka vs RabbitMQ vs NATS
**Objetivo**: Sistematizar os trade-offs entre os três.
**Conteúdo**:

| Eixo | Kafka | RabbitMQ | NATS |
|---|---|---|---|
| Modelo | Log | Filas (AMQP) | Stream |
| Ordering | Por partição | Por fila | Por stream |
| Retenção | Configurável (dias) | ACK-based | Stream-based |
| Throughput | Altíssimo | Médio | Alto |
| Latência | Média | Baixa | Baixíssima |
| Complexidade | Alta | Média | Baixa |

**Diagrama**: Tabela comparativa colorida
**Animação**: Colunas aparecem uma a uma
**Imagem**: Logos dos três + tabela
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A tabela resume os trade-offs. Kafka ganha em throughput e retenção (log persistente). RabbitMQ ganha em routing e baixa latência. NATS ganha em simplicidade e latência mínima. A escolha depende do problema: volume extremo + replay = Kafka; routing complexo = RabbitMQ; simplicidade + edge = NATS.
💡 ANALOGIA: É como escolher veículo. Kafka = trem de carga (muito volume, infra pesada). RabbitMQ = táxi (flexível, bom routing). NATS = bicicleta (leve, rápido, simples).
⚠️ ERROS COMUNS: Alunos começam com Kafka "porque é o que a empresa usa", sem avaliar se precisam. Kafka é overkill para muitos casos.
➡️ TRANSIÇÃO: "Vamos dar critério prático de escolha."

---

### Slide 22 — Quando Usar Cada Um

**Título**: Quando Usar Cada Um
**Objetivo**: Dar critério prático de escolha.
**Conteúdo**:
- **Kafka**: volume altíssimo, replay necessário, log de eventos, event sourcing
- **RabbitMQ**: routing complexo, filas de trabalho, request/reply, integrações legadas
- **NATS**: baixa latência, edge, simplicidade operacional, mensagens pequenas
- **Regra**: comece com o mais simples que resolve; Kafka é overkill para muitos casos

**Diagrama**: Árvore de decisão simples
**Animação**: Ramos da árvore aparecem
**Imagem**: Fluxograma de decisão
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A regra de ouro: comece simples. Se RabbitMQ resolve, não use Kafka. Se NATS resolve, não use RabbitMQ. Kafka é a ferramenta mais poderosa, mas também a mais complexa de operar (ZooKeeper/KRaft, monitoramento de lag, retenção). A pergunta não é "qual é o melhor?" — é "qual resolve meu problema com menos complexidade?"
💡 ANALOGIA: É como escolher ferramenta. Não use um martelo pneumatizado para pregar um quadro. Use o martelo certo para o prego certo.
⚠️ ERROS COMUNS: Alunos sofrem de FOMO tecnológico — querem Kafka porque é "moderno". Moderno não significa adequado.
➡️ TRANSIÇÃO: "Com os brokers entendidos, vamos ver dois padrões importantes: CQRS e Saga."

---

### Slide 23 — Padrão: CQRS

**Título**: Padrão: CQRS
**Objetivo**: Introduzir CQRS no contexto de agentes.
**Conteúdo**:
- **Command Query Responsibility Segregation**
- **Write side** (commands) → eventos → **read side** (queries) → views materializadas
- Para agentes: comandos geram eventos; agentes de consulta leem views
- Fonte: Microsoft *Cloud Design Patterns*

**Diagrama**: Fluxo CQRS — command → event store → read model → query
**Animação**: Fluxo aparece da esquerda para direita
**Imagem**: Diagrama CQRS
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: CQRS separa escrita (commands) de leitura (queries). Em vez de um único modelo que faz tudo, você tem dois: o write side otimizado para consistência (eventos), e o read side otimizado para consulta (views materializadas). Para agentes: um agente que modifica estado publica eventos; outro agente que consulta lê views pré-computadas — mais rápido que consultar fonte original.
💡 ANALOGIA: É como uma biblioteca. O catalogador (write side) organiza os livros. Os índices (read side) são views otimizadas para busca. Separar permite otimizar cada lado.
⚠️ ERROS COMUNS: Alunos aplicam CQRS onde não precisam. CQRS adiciona complexidade — só use quando o read side tem perfis de acesso muito diferentes do write side.
➡️ TRANSIÇÃO: "Outro padrão essencial: Saga. Mas vamos só introduzir — aprofundamos na Seção F."

---

### Slide 24 — Padrão: Saga (Visão Geral)

**Título**: Padrão: Saga (Visão Geral)
**Objetivo**: Introduzir saga antes de aprofundar em resiliência.
**Conteúdo**:
- **Saga**: sequência de transações locais com compensação
- Se passo N falha, executam **compensações** dos passos 1..N-1
- Dois estilos: **orquestrada** (central) vs **coreografada** (eventos)
- Aprofundamento na Seção F (Slide 51)

**Diagrama**: `12-Diagrams/ETHAGT11/saga.mmd`
**Animação**: Passos executam → falha → compensações revertem
**Imagem**: Diagrama saga
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Saga resolve o problema de transações distribuídas. Em vez de uma transação global (2PC — caro, frágil), você divide em transações locais. Se uma falha, você executa compensações (ações reversas) nos passos anteriores. Não é rollback perfeito — é melhor esforço. Vamos aprofundar na Seção F com caso concreto de transferência bancária.
💡 ANALOGIA: É como planejar uma viagem. Se o voo cancela, você cancela hotel (compensação 1) e devolve o aluguel do carro (compensação 2). Não é "desfazer" — é reverter o efeito.
➡️ TRANSIÇÃO: "Antes da demo, um padrão de padronização de eventos."

---

### Slide 25 — CloudEvents: Padronização de Eventos

**Título**: CloudEvents: Padronização de Eventos
**Objetivo**: Apresentar o padrão CNCF para eventos.
**Conteúdo**:
- **CloudEvents**: spec CNCF para descrição de eventos
- Campos: `id`, `source`, `type`, `specversion`, `time`, `data`, `subject`
- **Interoperabilidade**: mesmo formato entre Kafka, RabbitMQ, NATS, HTTP
- Para agentes: tool outputs como CloudEvents padroniza observabilidade

**Diagrama**: Exemplo de JSON CloudEvent
**Animação**: Campos do JSON aparecem um a um
**Imagem**: JSON destacado com cores por campo
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: CloudEvents é um padrão CNCF para descrever eventos de forma uniforme. Em vez de cada sistema ter seu formato, todos seguem o mesmo schema. Para agentes: se cada tool output for um CloudEvent, você ganha interoperabilidade e observabilidade — todos os eventos têm os mesmos campos (id, source, type, time).
💡 ANALOGIA: É como o padrão de tomada elétrica. Antes, cada país tinha o seu. Com padronização, qualquer aparelho funciona em qualquer lugar (adaptador necessário, mas formato é previsível).
⚠️ ERROS COMUNS: Alunos acham que CloudEvents é "mais um formato". É UM formato — o padrão que unifica os outros.
➡️ TRANSIÇÃO: "Vamos ver tudo isso funcionando na DEMO."

---

### Slide 26 — DEMO: Agente com Kafka

**Título**: DEMO: Agente com Kafka
**Objetivo**: Demo ao vivo — dois agentes coordenados via tópicos Kafka.
**Conteúdo**:
- Referência: `05-Labs/ETHAGT11/Lab1-Agente-Kafka`
- Agente A publica "tarefa: pesquisar X" no tópico `agent-tasks`
- Agente B consome, processa, publica resultado no tópico `agent-results`
- Mostrar ordering por chave (mesmo agent_id = mesma partição)
- Simular falha de consumer e mostrar reprocessamento

**Diagrama**: Code block + terminal side-by-side
**Animação**: Highlight de linhas chave (producer, consumer, key)
**Imagem**: Terminal com logs de producer/consumer
**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Demo ao vivo. Agente A publica tarefas no tópico `agent-tasks` com key=agent_id. Agente B consome, processa (chama LLM), publica resultado no tópico `agent-results`. Destacar: (1) ordering por key — mensagens do mesmo agente na mesma partição; (2) resiliência — se matar o consumer B e reiniciar, ele recupera do último offset commitado.
💡 ANALOGIA: É como dois colegas de trabalho via Slack. Um posta tarefas no canal #tasks; o outro lê, faz, posta resultado em #results. Se o segundo cair e voltar, ele continua de onde parou.
❓ PERGUNTA PARA A TURMA: (deixar para o Slide 27)
⚠️ ERROS COMUNS: Se a demo falhar (Kafka indisponível), ter screenshots prontos. Não improvisar — ter plano B.
➡️ TRANSIÇÃO: "Pergunta sobre a demo."

---

### Slide 27 — Pergunta da DEMO

**Título**: Pergunta da DEMO
**Objetivo**: Engajar a turma com uma pergunta sobre a demo.
**Conteúdo**:
- "O que acontece se Agente B processar duas vezes a mesma mensagem?"
- "Como garantir que o resultado não seja duplicado?"
- Discussão em duplas (2 min)

**Diagrama**: Caixa de discussão
**Animação**: Perguntas aparecem uma a uma
**Imagem**: Ícone de discussão
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A resposta é: idempotência. Kafka é at-least-once — mensagens podem chegar mais de uma vez (se o consumer cai após processar mas antes de commitar o offset). Para garantir que o resultado não duplique, o consumer precisa ser idempotente — processar 2x = processar 1x. A solução é usar chaves de idempotência (veremos no Slide 49). Esta pergunta motiva toda a Seção F.
💡 ANALOGIA: É como um garçom que anota o pedido duas vezes por engano. Se a cozinha for idempotente (verifica se já recebeu), só faz um prato.
⚠️ ERROS COMUNS: Alunos acham que Kafka é exactly-once. Não é — é at-least-once por default. Exactly-once requer configuração especial e tem custo de performance.
➡️ TRANSIÇÃO: "Vamos mudar de foco: de brokers para workflow engines."

---

## SEÇÃO D — Orquestração de Workflows (Slides 28-36 · 10 min)

---

### Slide 28 — [SEÇÃO] Orquestração de Workflows

**Título**: Orquestração de Workflows
**Objetivo**: Transição para orquestração de workflows.
**Conteúdo**: "3 — Orquestração de Workflows: Temporal, Prefect, Airflow"
**Diagrama**: Fundo `etho-primary`
**Animação**: Fade in do número e título
**Imagem**: —
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vimos mensageria — como agentes se comunicam. Agora vamos ver workflow engines — como orquestrar a execução. A diferença: mensageria é infraestrutura de comunicação; workflow engine é coordenação de execução com estado durável.
➡️ TRANSIÇÃO: "Primeiro, uma distinção importante: workflow engine vs agente que decide."

---

### Slide 29 — Workflow Engine vs Agentes que Decidem

**Título**: Workflow Engine vs Agentes que Decidem
**Objetivo**: Clarificar que workflow engine e agentes são complementares.
**Conteúdo**:
- **Workflow engine**: passos predefinidos, determinísticos, duráveis
- **Agente que decide**: rota dinâmica, flexível, menos previsível
- **Híbrido**: agente decide dentro de activity; workflow garante durability
- **Pergunta**: *Você orquestra via código ou via agente supervisor?*

**Diagrama**: Espectro — workflow determinístico ←→ agente autônomo
**Animação**: Marcadores no espectro se movem
**Imagem**: Linha com extremos rotulados
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Não é "workflow OU agente" — é "workflow E agente". Workflow engine (Temporal) lida com a orquestração: sequência de passos, retries, durability, HITL. Agente (LLM) lida com decisões: qual tool chamar, como interpretar resultado, quando pedir ajuda humana. O padrão híbrido é o mais poderoso: agente dentro de uma activity do Temporal — você tem flexibilidade do agente E durability do workflow.
💡 ANALOGIA: Workflow é o trilho do trem (determinístico, durável). Agente é o maquinista (decide velocidade, para em emergência). Você precisa de ambos.
❓ PERGUNTA PARA A TURMA: "Você orquestra via código ou via agente supervisor?"
⚠️ ERROS COMUNS: Alunos tentam fazer o agente orquestrar tudo. Agente não é confiável para garantir durability — ele pode alucinar, esquecer passos. Workflow engine é determinístico.
➡️ TRANSIÇÃO: "Vamos ao Temporal — a workflow engine mais relevante para agentes."

---

### Slide 30 — Temporal: Conceitos (Workflow, Activity, Worker)

**Título**: Temporal: Conceitos
**Objetivo**: Apresentar os conceitos fundamentais do Temporal.
**Conteúdo**:
- **Workflow**: função que descreve a lógica (determinística, sem I/O direto)
- **Activity**: unidade de trabalho (chamada de API, tool, I/O)
- **Worker**: processo que executa workflows e activities
- **Temporal Server**: armazena estado e histórico de execução
- **Task Queue**: workflow/activity tasks esperando workers

**Diagrama**: Arquitetura Temporal — Client → Server → Task Queue → Worker
**Animação**: Componentes aparecem um a um
**Imagem**: Diagrama de arquitetura Temporal
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Temporal tem 5 conceitos-chave. Workflow é a função que descreve a lógica — é DETERMINÍSTICA (sem I/O, sem random, sem datetime.now). Activity é onde o trabalho real acontece (chamadas de API, tools, I/O). Worker é o processo que executa. Temporal Server é o cérebro — armazena histórico de cada execução. Task Queue é onde as tasks esperam um worker disponível.
💡 ANALOGIA: Workflow é a receita (passos determinísticos). Activity é a ação física (cortar, cozinhar — tem efeitos colaterais). Worker é o cozinheiro. Temporal Server é o gerente que anota tudo. Task Queue é a fila de pedidos.
⚠️ ERROS COMUNS: Alunos colocam I/O no workflow. Workflow é puro cálculo + chamadas de activities. I/O (HTTP, DB, filesystem) vai em activities SEMPRE.
➡️ TRANSIÇÃO: "O conceito mais poderoso do Temporal: durable execution."

---

### Slide 31 — Temporal: Durable Execution

**Título**: Temporal: Durable Execution
**Objetivo**: Explicar o conceito central de durable execution.
**Conteúdo**:
- **Estado da execução é persistido a cada step**
- Se o worker cai, outro worker retoma do último step completado
- **Não há perda de progresso** — o histórico é a fonte de verdade
- **Replay**: re-executar o workflow usando o histórico gravado
- Fonte: Temporal *Durable Execution* primer

**Diagrama**: `12-Diagrams/ETHAGT11/durable-execution.mmd`
**Animação**: Worker cai (X vermelho) → novo worker retoma do checkpoint
**Imagem**: Diagrama com checkpoint e recovery
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esta é a mágica do Temporal. Cada vez que o workflow chama uma activity, o resultado é persistido. Se o worker cai, outro worker pega o histórico, faz replay (re-executa o workflow usando os resultados gravados das activities — sem re-executar as activities de verdade), e continua do ponto onde parou. Zero perda de progresso.
💡 ANALOGIA: É como um videogame com auto-save a cada nível. Se o console desliga, você recomeça do último nível salvo — não do começo. Temporal é o auto-save para agentes.
⚠️ ERROS COMUNS: Alunos acham que "durable execution = database". Não é. É a capacidade de retomar execução de código do ponto exato onde parou — incluindo loops, variáveis, estado de stack.
➡️ TRANSIÇÃO: "E o melhor: o workflow é código Python/Go comum."

---

### Slide 32 — Temporal: Código como Workflow

**Título**: Temporal: Código como Workflow
**Objetivo**: Mostrar que o workflow é código Python/Go comum.
**Conteúdo**:
- Snippet: workflow como função async com `await activity(...)`
- **Determinismo**: sem `datetime.now()`, sem `random()`, sem I/O direto
- I/O vai em activities; workflow orquestra
- **Timers**: `await workflow.sleep(...)` (durable, sobrevive a restart)
- **Signals**: receber input externo durante execução

**Diagrama**: Code block com workflow + activity
**Animação**: Syntax highlight das linhas-chave
**Imagem**: Snippet Python
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O workflow é uma função Python comum. Você escreve `async def meu_workflow(...)` e dentro chama `await workflow.execute_activity(minha_activity, ...)`. O que muda: você NÃO pode usar `datetime.now()` (usa `workflow.now()`), `random()` (usa `workflow.random()`), ou `time.sleep()` (usa `workflow.sleep()`). Tudo que é não-determinístico ou I/O deve ir em activities.
💡 ANALOGIA: É como escrever uma receita. A receita (workflow) descreve passos. Mas a receita não pode dizer "espere até o relógio marcar 14h" (não-determinístico se você reassar a receita). Diz "asse por 30 minutos" (determinístico).
⚠️ ERROS COMUNS: Alunos usam `time.sleep()` no workflow. Isso trava o worker sem dar durabilidade. O correto é `workflow.sleep()` que é durable.
➡️ TRANSIÇÃO: "Temporal é poderoso, mas complexo. Vamos ver alternativas mais simples."

---

### Slide 33 — Prefect: Python Puro, Mais Simples

**Título**: Prefect: Python Puro, Mais Simples
**Objetivo**: Mostrar a alternativa mais simples.
**Conteúdo**:
- `@flow` e `@task` decorators
- Menos verboso que Temporal; integração natural com Python
- **Menos durável**: estado no Prefect server, não no código
- Bom para data pipelines e protótipos de agentes
- Snippet de código

**Diagrama**: Code block comparando com Temporal
**Animação**: Highlight dos decorators @flow, @task
**Imagem**: Snippet Prefect
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Prefect é a alternativa "Python-nativa". Você adiciona `@flow` numa função e `@task` nas sub-funções. Prefect rastreia execução, persiste estado, oferece retries. É MUITO mais simples que Temporal. O trade-off: durabilidade é menor — se o Prefect server cai, você pode perder estado. Temporal sobrevive a qualquer falha porque o histórico é a fonte de verdade.
💡 ANALOGIA: Prefect é como um Apple Watch — simples, funciona out-of-the-box. Temporal é como um equipamento médico profissional — mais potente, mas precisa de expertise.
⚠️ ERROS COMUNS: Alunos usam Prefect para casos que precisam de Temporal (long-running com HITL). Prefect é ótimo para protótipos; Temporal para produção crítica.
➡️ TRANSIÇÃO: "E o velho conhecido: Airflow."

---

### Slide 34 — Airflow: Agendamento vs Orquestração em Tempo Real

**Título**: Airflow: Agendamento vs Orquestração
**Objetivo**: Posicionar Airflow corretamente.
**Conteúdo**:
- **Airflow**: DAGs agendadas (batch, cron-like)
- **Não** é orquestração em tempo real nem durable execution
- Ótimo para **ETL** e pipelines de dados agendados
- Para agentes de longa duração com HITL: **Temporal é mais adequado**

**Diagrama**: Espectro: Airflow (batch/agendado) ←→ Temporal (real-time/durable)
**Animação**: Marcadores no espectro
**Imagem**: Logos Airflow e Temporal
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Airflow é excelente para o que foi feito: DAGs agendadas (toda meia-noite, rode este ETL). Mas NÃO é durable execution. Se um task do Airflow falha, ele retenta o task — mas não retoma execução parcial. E Airflow não tem HITL em tempo real (você não pode pausar um DAG esperando aprovação humana por dias). Para agentes de longa duração com HITL, Temporal é a escolha.
💡 ANALOGIA: Airflow é um despertador (dispara em horário agendado). Temporal é um assistente pessoal (executa quando precisa, pausa quando precisa, retoma quando pode).
⚠️ ERROS COMUNS: Equipes com Airflow tentam usá-lo para orquestração de agentes. Funciona para casos simples, mas quebra em long-running e HITL.
➡️ TRANSIÇÃO: "Vamos comparar os três."

---

### Slide 35 — Comparação: Temporal vs Prefect vs Airflow

**Título**: Temporal vs Prefect vs Airflow
**Objetivo**: Sistematizar os trade-offs.
**Conteúdo**:

| Eixo | Temporal | Prefect | Airflow |
|---|---|---|---|
| Durable execution | Máximo | Médio | Baixo |
| Complexidade | Média | Baixa | Média |
| HITL nativo | Sim | Limitado | Não |
| Timers duráveis | Sim | Não | Limitado |
| Replay / debug | Sim | Limitado | Não |
| Agendamento batch | Possível | Possível | Excelente |

**Diagrama**: Tabela comparativa colorida
**Animação**: Colunas aparecem uma a uma
**Imagem**: Tabela com indicadores (✓/✗/~)
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A tabela resume. Temporal ganha em durability, HITL e replay. Prefect ganha em simplicidade. Airflow ganha em agendamento batch. Para agentes de longa duração com HITL (o caso da nossa aula), Temporal é a escolha canônica. Para data pipelines agendados, Airflow. Para protótipos rápidos, Prefect.
💡 ANALOGIA: Temporal é um tanque (resistente, durável, complexo). Prefect é uma pickup (versátil, simples). Airflow é um ônibus (agenda rotas, bom em massa).
⚠️ ERROS COMUNS: Alunos escolhem ferramenta por familiaridade. "Já sei Airflow, vou usar para agentes." Pode funcionar, mas vai doer em long-running e HITL.
➡️ TRANSIÇÃO: "Decisão final: quando orquestrar via código vs via agente?"

---

### Slide 36 — Quando Orquestrar via Código vs via Agente Supervisor

**Título**: Código vs Agente Supervisor
**Objetivo**: Decisão arquitetural: workflow engine ou agente.
**Conteúdo**:
- **Workflow engine (Temporal)**: passos previsíveis, determinismo, auditoria
- **Agente supervisor**: rota dinâmica, decisões contextuais, flexibilidade
- **Híbrido**: agente dentro de activity Temporal — flexibilidade + durability
- **Regra**: orquestração determinística no workflow; decisões inteligentes no agente

**Diagrama**: Árvore de decisão
**Animação**: Ramos da árvore surgem
**Imagem**: Fluxograma de decisão
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A regra de ouro: orquestração (sequência de passos, retries, HITL) vai no workflow. Decisão inteligente (qual tool, como interpretar, quando escalar) vai no agente. O híbrido é o padrão de produção: workflow Temporal chama um agente como activity. O workflow garante durability; o agente garante flexibilidade.
💡 ANALOGIA: Workflow é o processo (checklist de voo). Agente é o piloto (toma decisões contextuais). Auditoria quer o checklist; flexibilidade quer o piloto. Você precisa dos dois.
⚠️ ERROS COMUNS: Alunos tentam fazer tudo no agente. Agente não é confiável para garantir durability e auditoria. Workflow engine sim.
➡️ TRANSIÇÃO: "Vamos aprofundar durable execution aplicada a agentes."

---

## SEÇÃO E — Durable Execution para Agentes (Slides 37-38 · início)

---

### Slide 37 — [SEÇÃO] Durable Execution para Agentes

**Título**: Durable Execution para Agentes
**Objetivo**: Transição para durable execution aplicado a agentes.
**Conteúdo**: "4 — Durable Execution para Agentes"
**Diagrama**: Fundo `etho-primary`
**Animação**: Fade in do número e título
**Imagem**: —
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esta seção é o coração da aula. Durable execution é o que permite que agentes sobrevivam a crashes, rodem por dias, e pausem para HITL. Vamos cobrir crashes, long-running, HITL via timers/signals, replays e a armadilha do non-determinism.
➡️ TRANSIÇÃO: "Comecemos pela sobrevivência a crashes."

---

### Slide 38 — Sobreviver a Crashes

**Título**: Sobreviver a Crashes
**Objetivo**: Mostrar como durable execution sobrevive a falhas.
**Conteúdo**:
- Estado persistido a cada step (não a cada minuto — a cada chamada)
- Kill do processo → novo worker pega o histórico → replay até o último step → continua
- Comparação: sem durability = recomeça do zero; com durability = retoma do checkpoint
- Para agentes: cada tool call é um activity → checkpoint automático

**Diagrama**: `12-Diagrams/ETHAGT11/durable-execution.mmd`
**Animação**: Crash → recovery com seta indicando ponto de retomada
**Imagem**: Diagrama com checkpoint e recovery
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A diferença entre "com durability" e "sem durability" é drástica. Sem: crash no ticket 5.000 = recomeça do ticket 1. Com: crash no ticket 5.000 = retoma do ticket 5.001. Cada activity é um checkpoint. Para agentes, isso significa que cada tool call (que é cara) é persistida — você nunca re-paga por uma tool que já executou.
💡 ANALOGIA: É como um jogo com save automático a cada ação. Sem save, se o console desliga, você recomeça o jogo inteiro. Com save, você perde no máximo a última ação.
❓ PERGUNTA PARA A TURMA: "Vocês já calcularam quanto custa um restart do zero em um pipeline longo?"
⚠️ ERROS COMUNS: Alunos acham que "checkpoint a cada step" é lento. Não é — persistir o resultado de uma activity é uma operação de DB, milissegundos. O custo de REPROCESSAR é ordens de magnitude maior.
➡️ TRANSIÇÃO: "Se sobrevivemos a crashes, podemos rodar por muito mais tempo."

---
