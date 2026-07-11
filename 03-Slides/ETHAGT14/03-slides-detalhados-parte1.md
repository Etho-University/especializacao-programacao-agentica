# ETHAGT14 — Slides Detalhados + Notas do Professor (Parte 1: Slides 1-40)

> Universidade Etho · Especialização em Programação Agêntica
> Cada slide contém: título, objetivo, conteúdo, notas do professor, diagrama, animação, imagem, tempo.

---

## SEÇÃO A — Abertura (Slides 1-6 · 8 min)

---

### Slide 1 — Capa

**Título**: ETHAGT14 — Escalabilidade & Sistemas Distribuídos de Agentes
**Objetivo**: Identificar a aula, o professor e o contexto dentro da especialização.
**Conteúdo**:
- ETHAGT14 — Escalabilidade & Sistemas Distribuídos de Agentes
- Universidade Etho · Especialização em Programação Agêntica
- Fase D — Sistemas Distribuídos · 30 h
- Professor · Data

**Diagrama**: Logo Etho (canto sup. esquerdo) + imagem de fundo abstrata (rede de nós/servidores)
**Animação**: Fade in do título (300ms)
**Imagem**: Fundo `etho-dark` (#0F1E2D) com pattern sutil de nós e arestas conectando servidores
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Bem-vindos. Chegamos à Fase D — onde protótipos viram produção. Um agente que funciona para 1 usuário não é um sistema escalável. Hoje vamos transformar conhecimento de protótipo em engenharia de escala: caching, roteamento, distribuição, FinOps. Se vocês entenderem estes conceitos, conseguem operar um sistema agêntico para milhares de usuários sem surpresas no fim do mês.
💡 ANALOGIA: É a diferença entre cozinhar para a família (protótipo) e abrir um restaurante (escala). Os ingredientes são os mesmos, mas a engenharia é completamente diferente.
❓ PERGUNTA PARA A TURMA: "Quantos de vocês já colocaram um agente em produção para mais de 100 usuários?" (levantar mãos — calibrar)
⚠️ ERROS COMUNS: Alunos chegam achando que "escala = mais servidores". Não é. Escala é reduzir custo, latência e contenção sistemicamente.
➡️ TRANSIÇÃO: "Vamos começar definindo o que vocês vão conseguir fazer ao final."

---

### Slide 2 — Objetivos do Módulo

**Título**: Objetivos do Módulo
**Objetivo**: Deixar claro o que o aluno deve conseguir FAZER ao final da aula.
**Conteúdo**:
- **Objetivo geral**: Levar sistemas de agentes a escala de produção, dominando distribuição, custo, latência, caching e FinOps
- **Objetivos específicos**:
  1. Identificar gargalos em sistemas multi-agente (LLM, tools, memória, rede)
  2. Aplicar caching (semântico, de prompts, de embeddings)
  3. Distribuir agentes (sharding, replica, partitioning)
  4. Otimizar custo e latência (model routing, batching, speculative)
  5. Operar FinOps de agentes (orçamento, observabilidade de custo)

**Diagrama**: 5 ícones representando cada objetivo (funil, cache, shards, rota, gráfico de custo)
**Animação**: Objetivos aparecem um a um (on click)
**Imagem**: Ícones minimalistas em `etho-accent` (#E85D2F)
**Tempo**: 2 min

**Rodape**: FinOps = Financial Operations — gestao financeira de custo de agentes  ·  LLM = Large Language Model — Modelo de Linguagem de Grande Escala

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Cada objetivo é mensurável. Não é "entender" — é "identificar", "aplicar", "distribuir", "otimizar", "operar". Se ao final da aula vocês não conseguem fazer essas cinco coisas, eu falhei como professor. O projeto do módulo — otimizar custo/latência em ≥40% sem perder qualidade — é a prova real de que internalizaram.
💡 ANALOGIA: É como checklist de mergulho. Não dá para mergulhar sem verificar oxigênio, profundímetro e companheiro. Em escala, nosso checklist é estas 5 otimizações.
❓ PERGUNTA PARA A TURMA: "Qual desses objetivos vocês acham mais urgente no trabalho de vocês?" (deixar responder — costuma dividir entre caching e FinOps)
⚠️ ERROS COMUNS: Alunos priorizam distribuição (sharding) antes de caching. Ordem errada: caching primeiro (maior ROI), depois routing, depois distribuição.
➡️ TRANSIÇÃO: "Vamos ver onde esta aula toca no Framework Etho."

---

### Slide 3 — Competências Desenvolvidas

**Título**: Competências Desenvolvidas
**Objetivo**: Conectar a aula ao Framework Etho de competências.
**Conteúdo**:

| Competência | Nível ao final | Próximo nível em |
|---|---|---|
| C1 Programação Agêntica | **A** (Avançado) | ETHAGT90 Capstone |
| C2 Multi-Agent Systems | **A** (Avançado) | ETHAGT90 Capstone |
| C3 MCP & Tool Use | **B** (Básico) | aprofundamento individual |
| C4 Agent Memory | **A** (Avançado) | ETHAGT05, ETHAGT90 |
| C5 AgentOps & Avaliação | **A** (Avançado) | ETHAGT12, ETHAGT90 |

**Diagrama**: Radar chart com 5 eixos mostrando nível B/A
**Animação**: Radar aparece com wipe (left-to-right, 500ms)
**Imagem**: Badge visual por competência (círculos coloridos)
**Tempo**: 1 min

**Rodape**: AgentOps = Agent Operations — operacao e monitoramento de agentes em producao  ·  MCP = Model Context Protocol — Protocolo de Contexto de Modelo

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Este é um módulo terminal — quatro das cinco competências atingem Avançado. "Avançado" significa que vocês conseguem arquitetar, defender e operar sistemas em produção, não apenas implementar. C4 (Memória) aqui ganha dimensão distribuída: checkpointer, estado entre réplicas, consistência. C3 fica em Básico porque não aprofundamos ACI — foco é escala, não design de tools.
💡 ANALOGIA: Vocês estão saindo do estágio de piloto comercial e entrando em comandante de linha aérea. Mais responsabilidade, mais trade-offs, mais stakeholders.
⚠️ ERROS COMUNS: Alunos subestimam C4 aqui. Acham que memória é só "lembrar conversas". Em escala, memória distribuída é o calcanhar de Aquiles.
➡️ TRANSIÇÃO: "Vamos ver como esta aula está estruturada."

---

### Slide 4 — Agenda

**Título**: Agenda da Aula
**Objetivo**: Mostrar o roteiro da aula com tempos estimados.
**Conteúdo**:
- **Bloco 1 (45 min)**:
  - Abertura (8 min) — objetivos, custo da escala, contexto
  - Gargalos (10 min) — latência, custo, rate limits, estado
  - Caching (22 min) — exact, semântico, embeddings, tools, DEMO
  - Intervalo (5 min)
- **Bloco 2 (45 min)**:
  - Routing & Otimização (12 min) — Haiku/Sonnet, batching, speculative
  - Distribuição (10 min) — stateless, sharding, replica, consensus
  - Infra (5 min) — K8s, serverless, GPU, service mesh
  - FinOps (8 min) — orçamento, trade-offs, circuit breaker
  - Fechamento (10 min) — boas práticas, caso, quiz, Q&A

**Diagrama**: Timeline horizontal com 8 seções coloridas
**Animação**: Timeline cresce da esquerda para direita (500ms)
**Imagem**: Ícones de relógio por seção
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O Bloco 1 é sobre diagnóstico e tratamento de gargalos — caching é a estrela. O Bloco 2 é sobre arquitetura e operação: distribuição, infra e FinOps. Há 1 DEMO ao vivo (Slide 26) e 3 exercícios rápidos. O quiz final tem 3 perguntas.
💡 ANALOGIA: É como uma consulta médica — primeiro o diagnóstico (gargalos), depois o tratamento (caching, routing), depois o plano de saúde contínuo (FinOps).
⚠️ ERROS COMUNS: Alunos chegam atrasados e perdem a motivação (Slide 5). Avisar que o Slide 5 estabelece a urgência de toda a aula.
➡️ TRANSIÇÃO: "Por que estamos aqui? Porque escala custa caro."

---

### Slide 5 — Motivação: O Custo da Escala

**Título**: O Custo da Escala
**Objetivo**: Criar tensão cognitiva — o que funciona para 1 usuário quebra em 10.000.
**Conteúdo**:
- **Cenário**: agente que funciona para 1 usuário custa R$0,50/consulta
- **Para 10.000 usuários simultâneos**:
  - Latência explode: 2s → 30s (rate limit, contenção)
  - Custo mensal: R$50k (linear = explosão)
  - Estado distribuído entre réplicas: race conditions
- **Sem otimização**: escala linear = explosão de custo
- **Pergunta**: *Qual o maior custo oculto que vocês já viram em sistemas de LLM?*

**Diagrama**: Gráfico de custo crescente exponencial vs linear otimizado
**Animação**: Curva de custo sobe dramáticamente; depois curva otimizada achata
**Imagem**: Eixo Y em escala log, anotação "Zona de Dor" no topo
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Escala linear é o pesadelo. Cada usuário novo multiplica custo, latência e complexidade. Um agente que custa R$0,50 por consulta, em 10k usuários fazendo 10 consultas/dia, gera R$1,5M/mês. Sem caching, routing e FinOps, a empresa quebra em 30 dias. A boa notícia: caching + routing + batching tipicamente cortam 60-80% do custo. É isto que vamos aprender.
💡 ANALOGIA: É como um restaurante. Servir 10 clientes é fácil. Servir 1.000 no mesmo horário sem planejamento = filas, cozinha trava, ingredientes acabam, reviews ruins. Escala exige engenharia.
❓ PERGUNTA PARA A TURMA: "Qual o maior custo oculto que vocês já viram em sistemas de LLM?" (deixar 2-3 alunos responderem — costuma aparecer: contexto crescente, retries silenciosos, logs)
⚠️ ERROS COMUNS: Alunos acham que custo de LLM é só "preço da API". Esquecem infra (Redis, K8s, observabilidade) — 30-40% do total.
➡️ TRANSIÇÃO: "Mas por que só agora escala é urgente?"

---

### Slide 6 — Contexto: Por Que Escalabilidade Agora

**Título**: Por Que Escalabilidade Agora
**Objetivo**: Explicar a confluência que tornou escala de agentes urgente em 2026.
**Conteúdo**:
- **Agentes ≠ chat simples**: múltiplas chamadas de LLM por execução
- **Contexto cresce dentro de uma sessão** (KV cache, janela grande)
- **APIs impõem rate limits** (RPM/TPM) — sem gestão, 429 em cascata
- **Estado de sessão precisa ser distribuído** entre réplicas
- **Confluência**: frameworks maduros + demanda de produção + pressão de custo
- **Timeline**: 2023 (protótipos) → 2024 (frameworks) → 2025 (produção) → 2026 (escala)

**Diagrama**: Timeline horizontal com marcos
**Animação**: Marcos aparecem sequencialmente
**Imagem**: Eixo temporal com logos de frameworks/empresas
**Tempo**: 1 min

**Rodape**: KV = Key-Value — chave-valor

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Em 2023 todo mundo estava fazendo protótipos. Em 2024 surgiram LangGraph, CrewAI, OpenAI SDK. Em 2025 começamos a ver sistemas em produção. Em 2026 a pergunta virou "como escalo sem quebrar o caixa?". A urgência é real: empresas estão gastando 6 dígitos/mês com LLM e percebendo que sem engenharia de escala, não dá para sustentar.
💡 ANALOGIA: É como a transição da web em 1999. Primeiro vieram os sites (protótipos). Depois veio a pergunta: como servir 1 milhão de usuários? Nasceu a engenharia de escalabilidade web. Estamos no mesmo momento com agentes.
⚠️ ERROS COMUNS: Alunos acham que "escala é problema do DevOps". Não — escala começa no design do agente (caching, routing, loops curtos). É engenharia agêntica.
➡️ TRANSIÇÃO: "Vamos diagnosticar onde agentes esbarram em escala."

---

## SEÇÃO B — Gargalos de Escala (Slides 7-14 · 10 min)

---

### Slide 7 — [SEÇÃO] Onde Agentes Esbarram em Escala

**Título**: 1 — Onde Agentes Esbarram em Escala
**Objetivo**: Transição para o bloco de gargalos.
**Conteúdo**: Número "1" grande + "Onde Agentes Esbarram em Escala"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Número aparece com zoom
**Imagem**: Padrão abstrato de funil/gargalo
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Antes de otimizar, precisamos diagnosticar. Os próximos 8 slides identificam os 5 gargalos principais em sistemas multi-agente. Prestem atenção: cada gargalo tem uma técnica de mitigação que veremos nas próximas seções.
➡️ TRANSIÇÃO: "O primeiro gargalo — e o mais dominante — é a latência do LLM."

---

### Slide 8 — Latência de LLM como Gargalo Dominante

**Título**: Latência de LLM: O Gargalo Dominante
**Objetivo**: Explicar que a latência do LLM domina o tempo total de execução.
**Conteúdo**:
- **TTFT** (Time To First Token) — latência antes da primeira resposta (~0.3-1s)
- **TPOT** (Time Per Output Token) — taxa de geração (~30-80ms/token)
- **Em loop ReAct de 5 steps**: 5 × (TTFT + TPOT × tokens) = latência cumulativa
- **Latência serial**: cada step depende do anterior
- **Comparação**:
  - Chat simples: ~2s
  - Agente multi-step: ~15-30s
  - Agente profundo (10 steps): ~60s+

**Diagrama**: Bar chart comparando latência por tipo de chamada
**Animação**: Barras crescem mostrando latência acumulada
**Imagem**: Eixo Y em segundos, 4 barras (chat, 3-step, 5-step, 10-step)
**Tempo**: 2 min

**Rodape**: ReAct = Reasoning and Acting — padrao de loop Thought / Action / Observation

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O LLM é um gargalo serial. Cada chamada leva segundos, e em um loop ReAct as chamadas são sequenciais. Um agente de 5 steps com 2s por step = 10s mínimo, sem contar tool calls. Em 1.000 usuários simultâneos, sem paralelização, a fila cresce indefinidamente. As técnicas que veremos — streaming, batching, speculative decoding — atacam este gargalo.
💡 ANALOGIA: É como um restaurante com 1 cozinheiro. Cada prato leva 10 min. Mesas chegam a 10 min de espera. Adicionar cozinheiro (réplica) ou pré-preparar ingredientes (caching) reduz a espera.
❓ PERGUNTA PARA A TURMA: "Qual a latência p95 do agente mais crítico de vocês?" (deixar responder — costuma ser surpreendentemente alta)
⚠️ ERROS COMUNS: Confundir TTFT com latência total. TTFT é só o tempo até o primeiro token; latência total é TTFT + TPOT × tokens.
➡️ TRANSIÇÃO: "Mas latência não é o único problema. Custo cresce ainda mais rápido."

---

### Slide 9 — Custo Crescendo com Contexto

**Título**: Custo: Crescimento Quadrático
**Objetivo**: Mostrar que o custo não é linear — cresce com a janela de contexto.
**Conteúdo**:
- Cada step do agente envia TODO o histórico anterior
- **Step 1**: 1k tokens · **Step 5**: 15k tokens · **Step 10**: 40k tokens
- **Custo de input tokens cresce quadraticamente** com profundidade do loop
- KV cache (provider-side) reduz custo mas não elimina
- **Implicação**: agente profundo = custo explosivo
- Exemplo: 10-step loop × 5k tokens/step = ~250k tokens consumidos

**Diagrama**: Gráfico de custo por step (crescimento quadrático)
**Animação**: Steps aparecem um a um, barras de custo crescem
**Imagem**: Eixo X (steps), Eixo Y (tokens acumulados), curva quadrática
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Aqui está o custo oculto que mais surpreende. Em um loop ReAct, cada step reenvia todo o histórico. Não é 5 × 1k = 5k tokens — é 1k + 2k + 3k + ... = soma triangular ≈ n²/2. Para 10 steps, são ~50 × tokens-por-step. Em produção, isso multiplica custo rapidamente. Prompt caching do provider ajuda (cacheia prefixo), mas a parte nova ainda é cobrada.
💡 ANALOGIA: É como uma reunião onde cada novo participante precisa ouvir todo o histórico. 10 participantes = você repete a história 10 vezes. Custo de comunicação cresce quadraticamente.
⚠️ ERROS COMUNS: Alunos calculam custo como "steps × tokens-por-step". Errado — é soma triangular. Use a fórmula real no orçamento.
➡️ TRANSIÇÃO: "E quando mil usuários fazem isso ao mesmo tempo? Rate limits."

---

### Slide 10 — Concorrência e Rate Limits

**Título**: Concorrência e Rate Limits
**Objetivo**: Explicar como rate limits impedem escala horizontal.
**Conteúdo**:
- APIs de LLM limitam **RPM** (requests per minute) e **TPM** (tokens per minute)
- Anthropic Claude / OpenAI: tiers com limites crescentes
- **1.000 usuários simultâneos × 5 steps = 5.000 RPM necessários**
- Sem gestão: **429 Too Many Requests** → falhas em cascata
- **Estratégias**:
  - Filas com prioridade
  - Backoff exponencial (jitter)
  - Multi-provider (failover)
  - Batching de requests

**Diagrama**: Diagrama de filas com rate limiter
**Animação**: Requests chegam, rate limiter deixa passar N/min, resto fila
**Imagem**: Token bucket visual
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Rate limit é o teto duro. Por mais que você tenha orçamento, a API te limita por minuto. Sem gestão, 1.000 usuários simultâneos = desastre. A boa notícia: estratégias como backoff exponencial com jitter, filas com prioridade e multi-provider resolvem a maioria dos casos. O que vocês NÃO devem fazer é retry imediato — só piora o congestionamento.
💡 ANALOGIA: É como uma porta giratória. Por mais que a fila esteja ansiosa, só passa N pessoas por minuto. Empurrar mais gente não acelera — trava tudo.
❓ PERGUNTA PARA A TURMA: "Vocês já tomaram 429 em produção?" (levantar mãos)
⚠️ ERROS COMUNS: Retry sem backoff = tempestade de retries. Sempre use backoff exponencial com jitter aleatório.
➡️ TRANSIÇÃO: "Mas mesmo com rate limit sob controle, há outro problema: estado."

---

### Slide 11 — Estado Distribuído

**Título**: Estado Distribuído
**Objetivo**: Mostrar o desafio de manter estado entre réplicas.
**Conteúdo**:
- **Agente stateful**: sessão, memória, contexto acumulado
- Com múltiplas réplicas: usuário pode cair em réplica diferente
- **Opções**:
  - Sticky sessions (simples mas frágil)
  - Estado externo (Redis/Postgres checkpoint)
  - Stateless + checkpoint restore on-demand
- **Tensão**: stateless é mais fácil de escalar, mas agentes são inerentemente stateful
- Aprofundamento em ETHAGT05 (Memória de Agentes)

**Diagrama**: 3 réplicas com estado compartilhado via Redis
**Animação**: Request cai em réplica diferente, busca estado no Redis
**Imagem**: 3 pods + Redis central
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Agentes têm estado: o histórico da conversa, memória, contexto. Em uma única instância, isso morre em memória. Mas com múltiplas réplicas, o usuário pode cair em réplica diferente a cada request. Solução: externalizar o estado. Redis ou Postgres como checkpointer. Quando a request chega, restaura o estado, processa, salva novamente. Isto transforma um agente stateful em "stateless-friendly".
💡 ANALOGIA: É como um hotel. Se você troca de quarto a cada dia, precisa guardar suas coisas no cofre da recepção (Redis). Cada quarto (réplica) é stateless; o cofre central guarda o estado.
⚠️ ERROS COMUNS: Manter estado em memória sem checkpoint. Quando a réplica reinicia (deploy, crash), o usuário perde tudo.
➡️ TRANSIÇÃO: "Vamos visualizar todos esses gargalos juntos."

---

### Slide 12 — Anatomia de um Gargalo

**Título**: Anatomia de um Gargalo
**Objetivo**: Visualizar onde tempo e custo se acumulam em um agente.
**Conteúdo**:
- **request → chamada LLM (latência: 2s) → tool calls (latência: 0.5s) → contexto cresce (custo: $$) → loop?**
- Cada componente é um potencial gargalo
- **Latência total** = soma serial de todos os steps
- **Custo total** = soma de tokens × preço por step
- Mitigação: atacar o maior gargalo primeiro (maior ROI)

**Diagrama**: `12-Diagrams/ETHAGT14/bottleneck-analysis.mmd`
**Animação**: Fluxo percorre o diagrama step-by-step, destacando gargalos em vermelho
**Imagem**: Diagrama Mermaid renderizado
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Este é o diagrama-chave da aula. Cada nó é um gargalo potencial. A LLM é o gargalo dominante (latência + custo). Tool calls somam latência adicional. O crescimento de contexto multiplica custo. O loop multiplica tudo. Para otimizar, atacar o nó vermelho de maior impacto primeiro — geralmente caching na chamada LLM.
💡 ANALOGIA: É como analisar uma via expressa. Cada semáforo, cada obra, cada pedágio é um gargalo. Otimizar um semáforo não adianta se o pedágio é o gargalo real. Measure first, optimize second.
❓ PERGUNTA PARA A TURMA: "No sistema de vocês, qual nó é o mais vermelho?"
➡️ TRANSIÇÃO: "Para otimizar, precisamos medir. Quais métricas?"

---

### Slide 13 — Métricas-Chave de Escalabilidade

**Título**: Métricas-Chave de Escalabilidade
**Objetivo**: Definir as métricas que devem ser medidas desde o dia 1.
**Conteúdo**:
- **Latência**: TTFT, TPOT, p50/p95/p99 de tempo total
- **Custo**: $ por execução, $ por usuário, $ por tenant
- **Throughput**: requisições concorrentes, tokens/min
- **Taxa de erro**: 429s, timeouts, falhas de tool
- **Cache hit rate**: % de requisições servidas do cache
- **Dashboard mínimo**: latência, custo, throughput, cache hit, erros

**Diagrama**: Mini-dashboard com 5 gauges
**Animação**: Gauges se preenchem
**Imagem**: 5 cards lado a lado simulando Grafana
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: "Mediocrity is the enemy of scale." Sem métricas, vocês estão otimizando no escuro. Estas 5 dimensões formam o dashboard mínimo. Importante: sempre olhar p95 e p99, não só média. p99 revela os outliers (usuários esperando 30s) que destroem UX. Custo deve ser por execução (granular), não só mensal agregado.
💡 ANALOGIA: É como o painel de um carro. Não basta saber a velocidade média — você precisa de combustível, temperatura, RPM. Em agentes: latência, custo, throughput, erros, cache hit.
⚠️ ERROS COMUNS: Otimizar antes de medir. "Premature optimization is the root of all evil" — Knuth. Meçam primeiro, otimizem o gargalo real depois.
➡️ TRANSIÇÃO: "Pergunta rápida para a turma."

---

### Slide 14 — Pergunta: O Maior Custo Oculto

**Título**: Pergunta para a Turma
**Objetivo**: Engajar a turma com uma pergunta sobre custos reais.
**Conteúdo**:
- "Qual o maior custo oculto que vocês já viram em sistemas de LLM?"
- Opções:
  - Contexto crescente
  - Retries silenciosos
  - Tools (APIs externas)
  - Logs/traces
  - Infra (Redis, K8s, observabilidade)
- **Discussão aberta (3 min)**
- **Resposta típica**: contexto crescente + retries silenciosos

**Diagrama**: Caixa de discussão amarela
**Animação**: Opções aparecem uma a uma
**Imagem**: Ícone de balão de conversa
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Deixar a turma falar. Respostas comuns: contexto crescente (mais tokens), retries silenciosos (loop de retries sem log), tools que chamam APIs pagas, logs verbosos, observabilidade cara (Datadog). A lição: custo de LLM é só 60-70% do total. Os 30-40% restantes são "custos invisíveis" que ninguém mede até o fim do mês.
❓ PERGUNTA PARA A TURMA: deixar 3-4 alunos compartilharem
⚠️ ERROS COMUNS: Calcular TCO esquecendo observabilidade e rede. Always calcule total cost, não só custo de API.
➡️ TRANSIÇÃO: "Agora que diagnosticamos, vamos ao tratamento. Começamos pela primeira linha de defesa: caching."

---

## SEÇÃO C — Caching (Slides 15-29 · 17 min)

---

### Slide 15 — [SEÇÃO] Caching: A Primeira Linha de Defesa

**Título**: 2 — Caching: A Primeira Linha de Defesa
**Objetivo**: Transição para o bloco de caching.
**Conteúdo**: "2 — Caching: A Primeira Linha de Defesa"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Número aparece com zoom
**Imagem**: Padrão abstrato de cache/escudo
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Caching é a otimização de maior ROI. Custo baixo, impacto alto, risco baixo. Se só vão implementar uma técnica da aula, implementem caching. Os próximos 15 slides detalham 5 tipos de cache, estratégias de camadas, invalidação e a DEMO ao vivo.
➡️ TRANSIÇÃO: "Por que caching é tão impactante?"

---

### Slide 16 — Por Que Caching?

**Título**: Por Que Caching?
**Objetivo**: Justificar por que caching é a otimização de maior impacto.
**Conteúdo**:
- Caching elimina chamadas de LLM redundantes
- **Impacto**: reduz custo E latência simultaneamente
- **Cache hit = resposta instantânea + custo zero**
- Em sistemas reais: **30-60% das queries são repetidas ou similares**
- Analogia: "Cache é o único caso onde você ganha algo por nada"

**Diagrama**: Antes (todas as queries batem no LLM) vs Depois (cache filtra repetições)
**Animação**: Queries repetidas sendo interceptadas pelo cache
**Imagem**: Comparação visual, 2 colunas
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O dado-chave: 30-60% das queries em produção são repetidas ou semanticamente similares. Em sistemas de suporte, FAQs, documentação — esse número sobe para 70-80%. Cache hit nessas queries = custo zero, latência ~50ms (vs 2-3s do LLM). É a única otimização que reduz custo E latência simultaneamente.
💡 ANALOGIA: É como uma biblioteca. Sem cache, toda pergunta vai ao arquivo morto (LLM). Com cache, perguntas frequentes ficam no balcão (instantâneo). O bibliotecário só vai ao arquivo morto quando necessário.
⚠️ ERROS COMUNS: Achar que cache é só "memória". Cache é estratégia: o que cachear, por quanto tempo, como invalidar. Errar qualquer um dos três = dados errados.
➡️ TRANSIÇÃO: "Vamos do mais simples ao mais sofisticado."

---

### Slide 17 — Cache de Prompts / Exact Match

**Título**: Cache de Prompts / Exact Match
**Objetivo**: Apresentar a forma mais simples de caching.
**Conteúdo**:
- Mesmo prompt (exato) → mesma resposta
- **Implementação**: hash do prompt → lookup em Redis/dict
- **Prompt caching nativo** (Anthropic, OpenAI): cache de prefixo no provider
- **Vantagem**: trivial de implementar
- **Limitação**: só funciona para prompts idênticos (case-sensitive, whitespace-sensitive)

**Diagrama**: Fluxo: prompt → hash → cache hit? → resposta / LLM
**Animação**: Hash é calculado, lookup no Redis
**Imagem**: Fluxo esquemático simples
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Exact match é o cache mais simples. Hash (SHA-256) do prompt = chave. Se a chave existe no Redis, retorna. Senão, chama LLM, armazena. Prompt caching do provider é uma versão otimizada: eles cacham o prefixo do prompt (system prompt + tools) para reduzir custo de processamento — útil para agentes que sempre enviam o mesmo system prompt.
💡 ANALOGIA: É como reconhecer um cliente pelo nome exato. "João da Silva" é cache hit. "João Silva" é miss (sem o "da"). Sensível a detalhes.
❓ PERGUNTA PARA A TURMA: "Em qual caso exact match falha?" (qualquer variação: typos, espaços, ordem)
⚠️ ERROS COMUNS: Esquecer de normalizar o prompt antes de hashear (lowercase, trim, ordem canônica). Sem normalização, cache hit rate despenca.
➡️ TRANSIÇÃO: "E se perguntas forem semanticamente iguais mas com palavras diferentes?"

---

### Slide 18 — Cache Semântico: Conceito

**Título**: Cache Semântico: Conceito
**Objetivo**: Introduzir o conceito de cache semântico.
**Conteúdo**:
- Perguntas semanticamente similares → mesma resposta
- **"Qual a capital do Brasil?"** ≈ **"Capital do Brasil?"** ≈ **"Brasil capital?"**
- **Implementação**: embedding da query → busca por similaridade → threshold
- Se similaridade > threshold: retorna resposta cacheada
- Se não: chama LLM, armazena resultado

**Diagrama**: Fluxo: query → embedding → busca vetorial → hit/miss
**Animação**: Query entra, embedding gerado, comparado com vetores no cache
**Imagem**: Vetores 2D com cluster de queries similares
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Cache semântico é onde a mágica acontece. Em vez de comparar strings, comparamos SIGNIFICADO. Embeddings convertem a query em um vetor; busca vetorial encontra a query mais similar já cacheada. Se similaridade > threshold (e.g., 0.92), é hit. Isto captura variações linguísticas, typos, sinônimos. Hit rate tipicamente dobra vs exact match.
💡 ANALOGIA: É como um balconista experiente. Ele entende que "qual a capital do Brasil", "capital brasileira" e "Brasil, capital?" são a mesma pergunta, mesmo com palavras diferentes. Cache semântico faz isso com vetores.
⚠️ ERROS COMUNS: Usar embedding caro (e.g., text-embedding-3-large) para cache. Use modelo leve (text-embedding-3-small, ~1000x mais barato que o LLM).
➡️ TRANSIÇÃO: "Como implementar isso?"

---

### Slide 19 — Cache Semântico: Implementação

**Título**: Cache Semântico: Implementação
**Objetivo**: Mostrar código real de cache semântico.
**Conteúdo**:
- Snippet: função `semantic_cache(query, threshold=0.92)`
- **Passo 1**: embed(query) com modelo leve (e.g., text-embedding-3-small)
- **Passo 2**: vector_search no Redis/ChromaDB com top_k=1
- **Passo 3**: se similarity > threshold → return cached response
- **Passo 4**: senão → llm(query) → store {embedding, query, response}
- **Custo do embedding é ~1000x menor que custo do LLM**

**Diagrama**: Code block + fluxo lado a lado
**Animação**: Highlight de linhas chave
**Imagem**: Código Python com syntax highlighting
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A implementação é direta. Importante: o embedding é ~1000x mais barato que a chamada de LLM. Então mesmo se cache hit rate for 20%, já vale a pena. O threshold é o parâmetro crítico — veremos no próximo slide. Para armazenamento, Redis com vector search ou ChromaDB/Qdrant funcionam bem. TTL deve ser configurado para evitar cache stale.
💡 ANALOGIA: É como o sistema de sugestão do Google. Ele calcula um "embedding" da sua query parcial e busca queries similares já buscadas. Retorna sugestões instantaneamente.
⚠️ ERROS COMUNS: Esquecer TTL. Sem TTL, o cache acumula queries obsoletas ("preço do iPhone 14" servido em 2026). Sempre configurar TTL por tipo de query.
➡️ TRANSIÇÃO: "Mas como escolher o threshold? É um trade-off."

---

### Slide 20 — Threshold de Similaridade

**Título**: Threshold de Similaridade
**Objetivo**: Discutir o trade-off central do cache semântico.
**Conteúdo**:
- **Threshold alto (0.95)**: poucos falsos positivos, mas baixa hit rate
- **Threshold baixo (0.80)**: alta hit rate, mas falsos positivos (resposta errada)
- **Falso positivo** = resposta semanticamente próxima mas factualmente errada
- **Exemplo problemático**: "Preço do iPhone 15" vs "Preço do iPhone 14" — similares mas diferentes
- **Recomendação**: começar com 0.92, ajustar com base em eval

**Diagrama**: Gráfico de trade-off: threshold vs hit rate vs erro
**Animação**: Curva se move mostrando o trade-off
**Imagem**: Curva com eixos threshold (X), hit rate/erro (Y)
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O threshold é o parâmetro mais delicado. Alto (0.95) = só captura queries quase idênticas = hit rate baixo. Baixo (0.80) = captura tudo, inclusive o que não deveria = falsos positivos. Falso positivo em cache semântico é grave: você serve resposta errada como se fosse certa. O exemplo clássico é "preço do iPhone 15" vs "preço do iPhone 14" — semanticamente próximos (0.89), factualmente diferentes. Por isso, recomendo começar conservador (0.92) e ajustar com eval.
💡 ANALOGIA: É como um controle de fronteira. Muito rigoroso (0.95) = poucos entram. Muito frouxo (0.80) = entra gente errada. O ponto ótimo depende do contexto.
❓ PERGUNTA PARA A TURMA (duplas, 2 min): "Em que tipo de sistema você usaria threshold baixo? E alto?" (baixo: FAQs gerais; alto: dados sensíveis/numéricos)
⚠️ ERROS COMUNS: Configurar threshold uma vez e nunca revisar. Threshold ótimo muda conforme o cache enche e o domínio evolui.
➡️ TRANSIÇÃO: "Outro cache importante: embeddings."

---

### Slide 21 — Cache de Embeddings

**Título**: Cache de Embeddings
**Objetivo**: Explicar como evitar re-embedding desnecessário.
**Conteúdo**:
- Embedding de um texto é determinístico (mesmo modelo → mesmo vetor)
- Re-embeddo mesmo documento a cada query? **Desperdício**
- **Solução**: cache de embeddings (hash do texto → vetor)
- Útil em RAG: documentos indexados não precisam re-embedding
- **TTL**: invalidar quando o modelo de embedding muda

**Diagrama**: Fluxo: texto → hash → cache hit? → vetor / embed()
**Animação**: Hash do texto, lookup no cache de embeddings
**Imagem**: Pipeline RAG com cache de embeddings destacado
**Tempo**: 1 min

**Rodape**: RAG = Retrieval-Augmented Generation — Geracao Aumentada por Recuperacao  ·  TTL = Time To Live — tempo de validade

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Embeddings são determinísticos — mesmo texto + mesmo modelo = mesmo vetor. Re-embeddar documentos em cada query é puro desperdício. Solução: cachear embeddings por hash do texto. Em sistemas RAG com milhões de documentos indexados, isso economiza muita computação. Cuidado: invalidar o cache quando o modelo de embedding muda (e.g., text-embedding-3-small → text-embedding-3-large) — vetores incompatíveis.
💡 ANALOGIA: É como uma biblioteca que re-cataloga o mesmo livro toda vez que alguém pergunta por ele. Bobo. Cataloga uma vez, consulta muitas.
⚠️ ERROS COMUNS: Trocar modelo de embedding sem invalidar cache. Vetores incompatíveis = busca vetorial retorna lixo.
➡️ TRANSIÇÃO: "E os resultados de tools? Também podem ser cacheados."

---

### Slide 22 — Cache de Tool Results

**Título**: Cache de Tool Results
**Objetivo**: Mostrar que resultados de tools também podem ser cacheados.
**Conteúdo**:
- Tools idempotentes (GET, search, lookup) → resultado não muda frequentemente
- **Exemplos**:
  - `get_weather("Rio de Janeiro")` — cache por 30 min
  - `search_docs("API reference")` — cache por 24h
  - `get_price("AAPL")` — cache por 5 min
- **TTL por tool**: weather=30min, docs=24h, price=5min
- **Cuidado**: tools não-idempotentes (POST, mutate) NÃO devem ser cacheadas

**Diagrama**: Tabela de tools com TTL recomendado
**Animação**: Linhas da tabela aparecem uma a uma
**Imagem**: Tabela colorida com colunas tool/TTL/idempotência
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Tool results são um cache subaproveitado. Se o agente chama `search_docs("como configurar Redis")` e a doc não muda, pode cachear por horas. Isto reduz latência do agente (tool call → cache hit instantâneo) e custo de API externa. Mas atenção: só cachear tools idempotentes (GET, search). Tools que mutam estado (POST, PUT, DELETE) nunca devem ser cacheadas — causaria bugs sutis.
💡 ANALOGIA: É como o cache do navegador. Imagens e CSS ficam em cache (estáticos). Mas POST de formulário nunca é cacheado (muta estado).
❓ PERGUNTA PARA A TURMA: "Quais tools de vocês são idempotentes e cacheáveis?"
⚠️ ERROS COMUNS: Cachear tool de "enviar email". Disaster. SEMPRE verificar idempotência antes de cachear.
➡️ TRANSIÇÃO: "Cache tem um inimigo: tempo. Como manter correto?"

---

### Slide 23 — Invalidação e Consistência

**Título**: Invalidação e Consistência
**Objetivo**: Discutir os desafios de manter o cache correto.
**Conteúdo**:
- **Cache stale = resposta desatualizada**
- **Estratégias de invalidação**:
  - **TTL** (time-to-live) — simples mas impreciso
  - **Event-driven** — invalidar quando fonte muda
  - **Versionada** — chave inclui versão da fonte
- **Consistência eventual**: cache pode divergir da fonte por um tempo
- **Em agentes**: contexto muda a cada step → cache deve ser por step

**Diagrama**: Timeline mostrando TTL vs event-driven
**Animação**: TTL expira, event-driven invalida imediatamente
**Imagem**: Comparação de 2 estratégias lado a lado
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: "There are only two hard things in Computer Science: cache invalidation and naming things." A frase é clássica porque é verdadeira. TTL é simples mas impreciso — pode servir dado obsoleto por minutos. Event-driven é preciso mas complexo — precisa de notificação da fonte. Em agentes, há uma complicação adicional: o contexto muda a cada step do loop. Por isso, cache deve ser por step (não global). Combinar estratégias (TTL + event-driven) é geralmente o ideal.
💡 ANALOGIA: É como um cardápio de restaurante. TTL = cardápio impresso semanalmente (pode estar desatualizado). Event-driven = garçom pergunta a cozinha antes de anotar (preciso mas lento).
⚠️ ERROS COMUNS: Cachear resposta sem invalidar quando a fonte muda. Cliente recebe preço antigo, perde dinheiro, processa.
➡️ TRANSIÇÃO: "E se alguém injetar dados errados no cache?"

---

### Slide 24 — Cache Poisoning e Mitigação

**Título**: Cache Poisoning e Mitigação
**Objetivo**: Alertar sobre riscos de segurança do caching.
**Conteúdo**:
- **Cache poisoning**: usuário malicioso injeta resposta errada no cache
- **Cenário**: query maliciosa → resposta manipulada → cacheada → servida a outros
- **Mitigações**:
  - Separar cache por tenant/usuário
  - Não cachear respostas de usuários não confiáveis
  - Validar resposta antes de cachear
  - Rate limit por tenant para evitar flood de cache

**Diagrama**: Fluxo de ataque vs fluxo protegido
**Animação**: Ataque é bloqueado pela mitigação
**Imagem**: Comparação de 2 cenários
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Cache poisoning é um risco real e subestimado. Imaginem um sistema multi-tenant onde o cache é compartilhado. Um tenant malicioso envia uma query esperada ("capital do Brasil") mas manipula o contexto para o LLM responder "São Paulo" (errado). Essa resposta errada é cacheada. Todos os outros tenants agora recebem "São Paulo". Mitigação: separar cache por tenant OU validar respostas antes de cachear. Para cache semântico, requisitos de confiança são essenciais.
💡 ANALOGIA: É como alguém colocar uma placa falsa em um museu ("Mona Lisa — pintada em 1990"). Outros visitantes leem e acreditam. Solução: placas só podem ser colocadas por curadores aprovados.
⚠️ ERROS COMUNS: Cache compartilhado entre tiers gratuito e pago. Tier gratuito malicioso pode envenenar cache do tier pago.
➡️ TRANSIÇÃO: "Vamos arquitetar múltiplos caches em camadas."

---

### Slide 25 — Estratégia de Camadas (L1/L2/L3)

**Título**: Estratégia de Camadas (L1/L2/L3)
**Objetivo**: Apresentar uma arquitetura de cache em camadas.
**Conteúdo**:
- **L1**: Cache local em memória (ms, por instância)
- **L2**: Cache compartilhado em Redis (ms, por cluster)
- **L3**: Prompt caching do provider (Anthropic/OpenAI)
- **Fluxo**: L1 → L2 → L3 → LLM
- Cada camada adiciona latência incremental mas reduz custo

**Diagrama**: Arquitetura em camadas L1 → L2 → L3 → LLM
**Animação**: Request desce pelas camadas, para no primeiro hit
**Imagem**: Pirâmide de 4 níveis
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Camadas combinam velocidade e cobertura. L1 (memória da instância) é a mais rápida mas só serve aquela instância. L2 (Redis) é compartilhada entre réplicas. L3 (prompt caching do provider) cachear o prefixo no lado do LLM. A request desce pelas camadas; para no primeiro hit. Cada camada adiciona ~1-5ms de latência incremental mas reduz chamadas ao LLM drasticamente.
💡 ANALOGIA: É como memória de computador. L1 = registrador (instantâneo), L2 = RAM (rápido), L3 = SSD (ok), LLM = busca na internet (lenta). Cada nível é mais lento mas maior.
➡️ TRANSIÇÃO: "Agora vamos ver isso em ação. DEMO."

---

### Slide 26 — DEMO: Cache Semântico em Ação

**Título**: DEMO — Cache Semântico em Ação
**Objetivo**: Demo ao vivo — adicionar cache semântico a um agente.
**Conteúdo**:
- Código do `05-Labs/ETHAGT14/Lab1-Cache-Semantico`
- **Primeira chamada** → LLM (lenta, cara) → armazena no cache
- **Segunda chamada** (pergunta similar) → cache hit (rápida, barata)
- Medir redução de custo/latência em 10 perguntas
- Mostrar before/after no terminal

**Diagrama**: Code block + terminal side-by-side
**Animação**: Highlight de linhas chave; terminal mostra tempo/custo
**Imagem**: Terminal com before/after em verde
**Tempo**: 4 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Hora da demo. Eu vou executar o agente duas vezes. Primeira: sem cache. Cada query demora ~2-3s e custa ~R$0,05. Segunda: com cache semântico. Primeira query ainda vai ao LLM (miss), mas queries similares subsequentes são cache hits (~50ms, custo ~R$0,001). No final, mostro o before/after no terminal: 10 queries sem cache vs 10 com cache. Hit rate de ~60%, redução de custo de ~60%, redução de latência de ~60%. Isso é o poder do caching.
💡 ANALOGIA: É como ligar o ar-condicionado pela primeira vez vs deixá-lo ligado. O primeiro ciclo gasta energia para atingir a temperatura. Depois, ele só mantém (baixo custo).
❓ PERGUNTA PARA A TURMA: "Se a API falhar durante a demo, qual o plano B?" (screenshot pré-gravado)
⚠️ ERROS COMUNS: Demo falha por rate limit. Sempre pré-popular o cache para mostrar o hit path primeiro (mais robusto).
➡️ TRANSIÇÃO: "Vamos quantificar o ganho."

---

### Slide 27 — Medindo o Impacto (Antes/Depois)

**Título**: Medindo o Impacto
**Objetivo**: Quantificar o ganho do caching.
**Conteúdo**:
- **Antes**: 10 queries × R$0,05 = R$0,50 · Latência média: 3s
- **Depois**: 4 queries × R$0,05 + 6 cache hits × R$0,001 = R$0,21 · Latência média: 1.2s
- **Redução de custo: 58%**
- **Redução de latência: 60%**
- **Cache hit rate: 60%**
- **Métrica-chave**: cache hit rate deve ser monitorada continuamente

**Diagrama**: Bar chart antes vs depois (custo e latência)
**Animação**: Barras encolhem dramaticamente
**Imagem**: 2 barras antes/dupla, 2 barras depois/reduzidas
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Os números falam por si. 58% de redução de custo, 60% de latência, com cache hit rate de 60%. Em produção, esses números tipicamente variam de 30-70% dependendo do domínio. FAQs e documentação técnica: até 80%. Sistemas com queries altamente personalizadas: 20-30%. Importante: monitorem cache hit rate continuamente — se cair, investiguem (cache stale? queries mudaram? threshold errado?).
💡 ANALOGIA: É como medir a economia de combustível após ajustar o motor. Você precisa do número antes e depois para justificar o investimento.
⚠️ ERROS COMUNS: Medir uma vez e assumir que fica estável. Cache hit rate varia com a base de usuários, mudanças de produto e sazonalidade.
➡️ TRANSIÇÃO: "Pergunta rápida sobre a demo."

---

### Slide 28 — Pergunta da DEMO

**Título**: Pergunta da DEMO
**Objetivo**: Engajar a turma com uma pergunta sobre a demo.
**Conteúdo**:
- "O que acontece se o threshold for muito baixo?"
- "E se o usuário fizer uma pergunta factual que mudou (ex: 'quem é o presidente')?"
- "Como detectar que o cache está stale?"
- **Discussão em duplas (2 min)**

**Diagrama**: Caixa de discussão
**Animação**: Perguntas aparecem uma a uma
**Imagem**: Ícone de duplas conversando
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Deixar a turma discutir em duplas por 2 min. Respostas esperadas: (1) Threshold baixo = falsos positivos (resposta errada servida como certa); (2) Perguntas factuais que mudaram = cache stale, daí a importância do TTL por categoria; (3) Detectar cache stale = A/B testing, feedback do usuário, monitorar queda de qualidade. Lição: cache semântico não é "set and forget" — precisa de governança contínua.
❓ PERGUNTA PARA A TURMA: deixar 2-3 duplas compartilharem
➡️ TRANSIÇÃO: "Exercício rápido: quando cache semântico falha?"

---

### Slide 29 — Exercício: Quando Cache Semântico Falha

**Título**: Exercício — Quando Cache Semântico Falha
**Objetivo**: Praticar identificação de cenários onde cache semântico é problemático.
**Conteúdo**:
- 5 cenários curtos — em quais cache semântico falha?
  1. "Preço das ações da Apple hoje" → Falha (temporal)
  2. "Qual a capital da França?" → Funciona (estável)
  3. "Resuma o último email recebido" → Falha (contextual)
  4. "Como fazer um loop em Python?" → Funciona (estável)
  5. "Qual a previsão do tempo amanhã?" → Falha (temporal)
- **Votação rápida (mãos levantadas)**
- **Lição**: cache semântico funciona para conhecimento estável, falha para temporal/contextual

**Diagrama**: 5 cards com cenários
**Animação**: Cards aparecem um a um, depois resposta revelada
**Imagem**: Cards coloridos (verde=ok, vermelho=falha)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Exercício de votação rápida. Levantar mãos para cada cenário: "Quem acha que cache semântico FALHA aqui?" Respostas: 1 falha (preço muda), 2 ok (estável), 3 falha (depende do email), 4 ok (estável), 5 falha (previsão muda). Lição geral: cache semântico funciona para conhecimento ESTÁVEL (geografia, programação, conceitos). Falha para TEMPORAL (preço, previsão, notícia) ou CONTEXTUAL (último email, histórico pessoal). Para esses, usar TTL curto ou não cachear.
💡 ANALOGIA: É como uma enciclopédia. Excelente para "capital da França" (não muda). Péssima para "preço da Apple hoje" (muda a cada segundo).
⚠️ ERROS COMUNS: Aplicar cache semântico sem categorizar queries. Configure TTL por categoria temporal: estável (infinito), diário (24h), real-time (5min).
➡️ TRANSIÇÃO: "Intervalo. Voltamos com routing e otimização."

---

## SEÇÃO D — Model Routing & Otimização (Slides 30-39 · 12 min)

---

### Slide 30 — [SEÇÃO] Model Routing & Otimização

**Título**: 3 — Model Routing & Otimização
**Objetivo**: Transição para otimização de chamadas.
**Conteúdo**: "3 — Model Routing & Otimização"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Número aparece com zoom
**Imagem**: Padrão abstrato de roteamento
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Depois do caching, a segunda maior otimização é model routing: nem toda query precisa do modelo mais caro. Veremos Haiku/Sonnet/Opus, batching, speculative decoding, streaming, e a matriz de esforço vs impacto. Ao final, vocês terão um framework para decidir qual técnica aplicar primeiro.
➡️ TRANSIÇÃO: "A ideia central: rotear por complexidade."

---

### Slide 30A — Roteamento por Complexidade

**Título**: Roteamento por Complexidade
**Objetivo**: Apresentar o conceito de rotear requisições por complexidade.
**Conteúdo**:
- Nem toda query precisa do modelo mais caro
- **Haiku ($0.25/M)**: classificação, extração, Q&A simples
- **Sonnet ($3/M)**: raciocínio moderado, tool use, análise
- **Opus ($15/M)**: raciocínio complexo, multi-step, crítico
- **Roteamento automático**: classifier → modelo apropriado
- **Economia**: 70% das queries podem usar Haiku

**Diagrama**: Funil: queries → classifier → 3 modelos
**Animação**: Queries descem pelo funil para o modelo certo
**Imagem**: Funil com 3 saídas coloridas
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O insight: 70% das queries em sistemas reais são "simples" (classificação, extração, Q&A factual). Essas podem ir para Haiku a $0.25/M, em vez de Opus a $15/M — 60x mais barato. Um classifier leve decide: "esta query é simples, moderada ou complexa?" Redireciona para o modelo apropriado. Em produção, isto reduz custo médio em 40-60% sem perda de qualidade mensurável.
💡 ANALOGIA: É como um pronto-socorro. Triagem decide quem vai para enfermeiro (Haiku), médico geral (Sonnet) ou especialista (Opus). Nem todo paciente precisa do especialista.
⚠️ ERROS COMUNS: Usar Opus para tudo. É o erro mais comum e mais caro. Medir: qual % das suas queries é realmente complexa?
➡️ TRANSIÇÃO: "Mas como classificar complexidade SEM gastar tokens?"

---

### Slide 31 — Como Medir Complexidade Antes de Chamar

**Título**: Como Medir Complexidade
**Objetivo**: Discutir como classificar complexidade sem gastar tokens.
**Conteúdo**:
- **Heurísticas baratas**: tamanho do input, nº de tools disponíveis, palavra-chave
- **Classifier leve** (Haiku/tiny model): "esta query é simples ou complexa?"
- **Histórico**: queries similares já classificadas (cache de roteamento)
- **Cascata**: tentar Haiku primeiro, escalar para Sonnet se falhar
- **Trade-off**: classifier errado = resposta ruim ou custo desnecessário

**Diagrama**: Fluxo: query → heurística/classifier → modelo
**Animação**: Query passa por heurística, é classificada
**Imagem**: Árvore de decisão com 2 níveis
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O classifier não pode custar mais que a economia. Heurísticas baratas (tamanho do input, palavras-chave) são de graça. Um classifier Haiku ($0.25/M) é quase grátis. A cascata é elegante: tenta Haiku primeiro. Se ele retornar baixa confiança (e.g., "não sei"), escala para Sonnet. Isto captura o melhor dos dois mundos: barato para simples, capaz para complexas.
💡 ANALOGIA: É como resolver um problema matemático. Tente a fórmula simples primeiro. Se não funcionar, chame o professor. Não comece chamando o professor para tudo.
❓ PERGUNTA PARA A TURMA: "Que heurística você usaria para classificar queries de vocês?"
⚠️ ERROS COMUNS: Classifier muito complexo (custa caro) ou muito simples (erra muito). Teste diferentes abordagens com eval.
➡️ TRANSIÇÃO: "Outra otimização: batching."

---

### Slide 32 — Batching de Requests

**Título**: Batching de Requests
**Objetivo**: Explicar como agrupar requisições reduz custo e latência.
**Conteúdo**:
- N requisições independentes → 1 chamada de API com N prompts
- **Batch de embeddings**: 100 textos em 1 chamada
- **Batch de classificações**: 10 queries em 1 prompt
- **Reduz**: nº de requests (rate limit), overhead de rede, custo de TTFT
- **Limitação**: só funciona para requisições independentes (não em loop serial)

**Diagrama**: Antes (10 requests serial) vs Depois (1 batch)
**Animação**: 10 barras colapsam em 1
**Imagem**: Comparação visual antes/depois
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Batching é velho conhecido de sistemas distribuídos. Em agentes, há dois usos: (1) embeddings — em vez de embeddar 100 textos em 100 chamadas, faça 1 chamada com 100 textos; (2) classificações — em vez de classificar 10 tickets em 10 chamadas, faça 1 prompt com 10 tickets. Isto reduz latência (menos round-trips), custo (menos overhead) e respeita rate limit (menos requests). Mas atenção: batching só funciona para requisições INDEPENDENTES. Em loop serial, cada step depende do anterior — não dá para batchear.
💡 ANALOGIA: É como ir ao mercado. Em vez de 10 viagens para comprar 1 item cada, faça 1 viagem com 10 itens. Economiza tempo, gasolina e esforço.
⚠️ ERROS COMUNS: Tentar batchear steps de um loop ReAct. Não funciona — cada step depende do anterior.
➡️ TRANSIÇÃO: "Para reduzir latência real: speculative decoding."

---

### Slide 33 — Speculative Decoding / Prediction

**Título**: Speculative Decoding
**Objetivo**: Introduzir speculative decoding como técnica de redução de latência.
**Conteúdo**:
- **Modelo pequeno (draft)** gera rascunho rápido
- **Modelo grande (target)** verifica rascunho em paralelo
- Se rascunho estiver certo: **enorme economia de latência**
- Se errado: target corrige (pequeno overhead)
- Em agentes: prever próxima action do agente com modelo leve
- **Fonte**: arXiv:2211.17192

**Diagrama**: Fluxo: draft model → target model → aceita/rejeita
**Animação**: Draft gera tokens, target verifica em paralelo
**Imagem**: 2 modelos lado a lado, setas de aceitação/rejeição
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Speculative decoding é uma das otimizações mais elegantes. A ideia: um modelo pequeno (draft, rápido) gera K tokens. O modelo grande (target, lento) verifica esses K tokens em paralelo. Se todos estiverem corretos, economizou muito tempo. Se alguns errados, o target corrige a partir do primeiro erro. Em média, latência cai 2-3x. Para agentes, há uma variação: prever a próxima action com modelo leve, e só confirmar com modelo pesado.
💡 ANALOGIA: É como um estagiário que escreve o rascunho, e o sênior só revisa. Se o rascunho estiver bom, o sênior aprova rápido. Se não, reescreve a parte errada.
⚠️ ERROS COMUNS: Achar que speculative decoding é simples de implementar. Exige infraestrutura especializada (vLLM, TGI). Não tente fazer do zero.
➡️ TRANSIÇÃO: "Já streaming é mais simples e impacta UX."

---

### Slide 34 — Streaming para Latência Percebida

**Título**: Streaming para Latência Percebida
**Objetivo**: Explicar como streaming melhora experiência sem reduzir latência total.
**Conteúdo**:
- **Sem streaming**: usuário espera 10s, recebe tudo de uma vez
- **Com streaming**: usuário vê tokens em ~0.5s, recebe gradualmente
- **Latência total é a mesma**, mas latência PERCEBIDA cai drasticamente
- Em agentes: streamar thought/answer, não tool calls
- **V/F**: "Streaming reduz latência total." → **FALSO** (reduz percebida, não real)

**Diagrama**: Comparação visual: barra cheia vs barra preenchendo gradualmente
**Animação**: Barra esquerda fica vazia por 10s, depois cheia; barra direita preenche gradualmente
**Imagem**: 2 timelines lado a lado
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esta é uma pegadinha clássica. Streaming NÃO reduz latência total — o LLM ainda gera os mesmos tokens no mesmo tempo. Mas reduz a latência PERCEBIDA: o usuário vê algo acontecendo em 500ms em vez de 10s. Psicologicamente, espera-se muito mais por algo em movimento do que por uma tela vazia. Em agentes, streamar a resposta final (thought + answer) melhora UX drasticamente. Não streamar tool calls (são internas, não para o usuário).
💡 ANALOGIA: É como um carregamento de página. Barra vazia por 5s parece eterno. Barra preenchendo gradualmente parece rápida. Mesmo tempo total.
❓ PERGUNTA PARA A TURMA: "Vocês streamam respostas em produção?" (levantar mãos)
⚠️ ERROS COMUNS: Implementar streaming mas não para tool calls intermedíárias. Usuário fica esperando sem feedback.
➡️ TRANSIÇÃO: "Panorama: distilação e fine-tuning."

---

### Slide 35 — Distilação e Fine-Tuning (Panorama)

**Título**: Distilação e Fine-Tuning
**Objetivo**: Panorama de otimizações mais profundas.
**Conteúdo**:
- **Distilação**: treinar modelo menor com saídas de modelo maior
- **Fine-tuning**: especializar modelo para domínio (reduz prompt size)
- **Quando vale**: volume alto (>100k requests/mês), domínio estável
- **Quando NÃO vale**: volume baixo, domínio muda frequentemente
- Aprofundamento: ETHAGT08 (Fine-tuning) e ETHAGT15 (DSPy)

**Diagrama**: Árvore de decisão: vale fine-tuning?
**Animação**: Árvore se ramifica com critérios
**Imagem**: Fluxograma com nós de decisão
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Distilação e fine-tuning são otimizações profundas. Distilação: treine um modelo pequeno com saídas de um grande. Resultado: modelo pequeno que se aproxima da qualidade do grande, com custo muito menor. Fine-tuning: especialize um modelo para seu domínio, reduzindo o tamanho do prompt necessário (system prompt fixo vira conhecimento interno). Ambos valem a pena quando: volume alto (>100k requests/mês, para amortizar o custo de treino) E domínio estável (não muda toda semana).
💡 ANALOGIA: Distilar é como um aprendiz que copia o mestre até aprender. Fine-tuning é como um médico generalista que se especializa em cardiologia — precisa de menos contexto para diagnosticar problemas cardíacos.
⚠️ ERROS COMUNS: Fine-tunar com volume baixo. O custo de treino (GPU + dados + eval) supera a economia. Regra: pelo menos 100k requests/mês para justificar.
➡️ TRANSIÇÃO: "Vamos sistematizar tudo numa matriz."

---

### Slide 36 — Matriz de Otimização

**Título**: Matriz de Otimização
**Objetivo**: Sistematizar as técnicas de otimização.
**Conteúdo**:
- Tabela: técnica × impacto (custo/latência/qualidade) × esforço × risco
  - **Caching**: alto impacto custo/latência, baixo esforço, baixo risco
  - **Routing**: médio impacto custo, médio esforço, médio risco
  - **Batching**: médio impacto latência, baixo esforço, baixo risco
  - **Speculative**: alto impacto latência, alto esforço, alto risco
  - **Fine-tuning**: alto impacto custo, alto esforço, alto risco

**Diagrama**: Matriz 2x2 (impacto vs esforço)
**Animação**: Pontos aparecem na matriz
**Imagem**: Quadrante com 5 técnicas posicionadas
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A matriz ajuda a priorizar. Canto superior esquerdo (alto impacto, baixo esforço): caching — comece aqui. Routing e batching são médio impacto, baixo esforço: implemente em seguida. Speculative e fine-tuning são alto impacto mas alto esforço/risco: só depois de esgotar as anteriores. A regra: comece barato e de baixo risco, escale para caro/risco conforme ROI justifique.
💡 ANALOGIA: É como investir. Comece com ETFs (caching — barato, seguro, bom retorno). Depois ações individuais (routing). Depois derivativos (speculative — só para experientes).
⚠️ ERROS COMUNS: Pular caching e ir direto para fine-tuning. É como pular ETFs e ir para derivativos — desperdício de risco.
➡️ TRANSIÇÃO: "Pergunta para reflexão."

---

### Slide 37 — Pergunta: Como Decidir?

**Título**: Pergunta — Como Decidir?
**Objetivo**: Discussão sobre priorização de otimizações.
**Conteúdo**:
- "Se você tivesse 1 semana para otimizar um agente em produção, por onde começaria?"
- **Resposta esperada**: caching primeiro (maior ROI, menor esforço)
- "Em que cenário routing é melhor que caching?"
- **Discussão aberta (2 min)**

**Diagrama**: Caixa de discussão
**Animação**: Pergunta aparece
**Imagem**: Ícone de brainstorm
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Pergunta de reflexão. Resposta esperada: caching primeiro (maior ROI, menor esforço, menor risco). Em 1 semana, dá para implementar cache semântico, medir hit rate e ajustar threshold. Routing é segunda prioridade. Batching terceira. Speculative e fine-tuning exigem mais de 1 semana. Em que cenário routing é melhor que caching? Quando as queries são majoritariamente únicas (baixa repetição) mas há clara separação de complexidade.
❓ PERGUNTA PARA A TURMA: deixar 2-3 alunos compartilharem suas prioridades
➡️ TRANSIÇÃO: "Exercício rápido de routing."

---

### Slide 38 — Exercício Rápido: Qual Modelo para Qual Tarefa

**Título**: Exercício — Routing por Complexidade
**Objetivo**: Praticar roteamento por complexidade.
**Conteúdo**:
- 6 tarefas — qual modelo (Haiku/Sonnet/Opus)?
  1. "Classificar este ticket como bug/feature/question" → Haiku
  2. "Resolver este bug complexo de concorrência" → Opus
  3. "Resumir este documento de 5 páginas" → Haiku
  4. "Planejar arquitetura de sistema multi-agente" → Opus
  5. "Extrair entidades deste email" → Haiku
  6. "Decidir qual tool chamar e por quê" → Sonnet
- **Votação rápida**

**Diagrama**: 6 cards com tarefas
**Animação**: Cards aparecem, depois resposta revelada
**Imagem**: Cards coloridos por modelo
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Votação rápida. Respostas: 1 Haiku (classificação direta), 2 Opus (raciocínio profundo sobre concorrência), 3 Haiku (sumarização), 4 Opus (arquitetura complexa), 5 Haiku (extração estruturada), 6 Sonnet (decisão com tools). Lição: a maioria das tarefas é Haiku. Use Opus com parcimônia. O gasto médio cai drasticamente quando você para de usar Opus para tudo.
❓ PERGUNTA PARA A TURMA: votação de mãos levantadas para cada tarefa
⚠️ ERROS COMUNS: Usar Opus para tudo por "medo de errar". Meça: qual % das respostas Haiku é rejeitada pelo usuário? Geralmente baixo.
➡️ TRANSIÇÃO: "Vamos para distribuição."

---

### Slide 39 — Resumo da Seção D

**Título**: Resumo — Routing & Otimização
**Objetivo**: Sintetizar as técnicas de otimização.
**Conteúdo**:
- **Routing**: Haiku para 70% das queries → reduz custo 40-60%
- **Batching**: agrupar requests independentes → reduz latência e rate limit
- **Speculative**: draft + target → reduz latência 2-3x
- **Streaming**: reduz latência percebida (não real)
- **Fine-tuning/Distilação**: alto esforço, alto ganho, só para volume alto
- **Ordem de implementação**: caching → routing → batching → speculative → fine-tuning

**Diagrama**: Pipeline de otimização em sequência
**Animação**: Etapas aparecem em sequência
**Imagem**: Timeline horizontal com 5 etapas
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Recapitulando. A ordem de implementação é crucial: caching primeiro (maior ROI), depois routing, depois batching. Speculative e fine-tuning só depois de esgotar as anteriores. Esta ordem maximiza redução de custo/latência com mínimo esforço. Não pule etapas.
➡️ TRANSIÇÃO: "Agora vamos além de otimizar chamadas. Vamos DISTRIBUIR agentes."
