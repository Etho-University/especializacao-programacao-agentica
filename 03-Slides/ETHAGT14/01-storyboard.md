# ETHAGT14 — Escalabilidade & Sistemas Distribuídos de Agentes
## Storyboard da Apresentação

> **Universidade Etho · Especialização em Programação Agêntica**
> Fase D — Sistemas Distribuídos · 30 h
> Storyboard v1.0 · Julho 2026

---

## Metadados da Apresentação

| Campo | Valor |
|---|---|
| Código | ETHAGT14 |
| Título | Escalabilidade & Sistemas Distribuídos de Agentes |
| Duração estimada | 90 min (2 blocos de 45 min) |
| Total de slides | 75 |
| Público | Arquitetos, Engenheiros de Software, Engenheiros de IA, SREs, Tech Leads |
| Pré-requisitos | ETHAGT11 |
| Competências | C1 (A), C2 (A), C3 (B), C4 (A), C5 (A) |

---

## Mapa Visual da Apresentação

```
BLOCO 1 (45 min)                              BLOCO 2 (45 min)
┌──────────────────────────────┐              ┌──────────────────────────────┐
│ SEÇÃO A — Abertura (8 min)   │              │ SEÇÃO D — Routing (12 min)   │
│  Capa · Objetivos · Agenda   │              │  Haiku/Sonnet/Opus · Batching│
│  Motivação · Contexto        │              │  Speculative · Streaming     │
├──────────────────────────────┤              ├──────────────────────────────┤
│ SEÇÃO B — Gargalos (10 min)  │              │ SEÇÃO E — Distribuição (10m) │
│  Latência · Custo · Rate     │              │  Stateless · Sharding · Replica│
│  Estado · Bottleneck diagram │              │  Consensus · Multi-region    │
├──────────────────────────────┤              ├──────────────────────────────┤
│ SEÇÃO C — Caching (17 min)   │              │ SEÇÃO F — Infra (5 min)      │
│  Exact · Semântico · Embeds  │              │  K8s · Serverless · GPU      │
│  Tools · Invalidação · DEMO  │              ├──────────────────────────────┤
│                              │              │ SEÇÃO G — FinOps (8 min)     │
│                              │              │  Orçamento · Trade-offs · CB │
│                              │              ├──────────────────────────────┤
│                              │              │ SEÇÃO H — Fechamento (10 min)│
│                              │              │  Boas práticas · Quiz · Refs │
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
  - ETHAGT14 — Escalabilidade & Sistemas Distribuídos de Agentes
  - Universidade Etho · Especialização em Programação Agêntica
  - Fase D — Sistemas Distribuídos
  - Professor · Data
- **Diagrama**: Logo Etho + imagem de fundo abstrata (rede de nós/servidores)
- **Animação**: Fade in do título
- **Tempo**: 1 min

---

#### Slide 2 — Objetivos do Módulo
- **Tipo**: Conteúdo
- **Objetivo**: Deixar claro o que o aluno deve conseguir fazer ao final
- **Conteúdo**:
  - Objetivo geral: Levar sistemas de agentes a escala de produção, dominando distribuição, custo, latência, caching e FinOps
  - 5 objetivos específicos (1 linha cada):
    1. Identificar gargalos em sistemas multi-agente
    2. Aplicar caching (semântico, de prompts, de embeddings)
    3. Distribuir agentes (sharding, replica, partitioning)
    4. Otimizar custo e latência (model routing, batching, speculative)
    5. Operar FinOps de agentes (orçamento, observabilidade de custo)
- **Diagrama**: Ícones representando cada objetivo
- **Animação**: Aparecer objetivos um a um (on click)
- **Tempo**: 2 min

---

#### Slide 3 — Competências Desenvolvidas
- **Tipo**: Conteúdo
- **Objetivo**: Conectar a aula ao Framework Etho de competências
- **Conteúdo**:
  - Tabela: 5 competências com nível B/I/A
  - C1 Programação Agêntica → A
  - C2 Multi-Agent Systems → A
  - C3 MCP & Tool Use → B
  - C4 Agent Memory → A
  - C5 AgentOps & Avaliação → A
  - Badge visual por competência
- **Diagrama**: Radar chart dos 5 pilares
- **Animação**: Radar aparece com wipe
- **Tempo**: 1 min

---

#### Slide 4 — Agenda
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar o roteiro da aula com tempos
- **Conteúdo**:
  - Bloco 1: Abertura → Gargalos → Caching
  - Bloco 2: Routing → Distribuição → Infra → FinOps → Fechamento
  - Tempos estimados por seção
- **Diagrama**: Timeline horizontal com 8 seções
- **Animação**: Timeline cresce da esquerda para direita
- **Tempo**: 1 min

---

#### Slide 5 — Motivação: O Custo da Escala
- **Tipo**: Conteúdo
- **Objetivo**: Criar tensão — o que funciona para 1 usuário quebra em 10.000
- **Conteúdo**:
  - Agente que funciona para 1 usuário custa R$0,50/consulta
  - Para 10.000 usuários simultâneos: latência de 30s, custo mensal de R$50k
  - Sem otimização: escala linear = explosão de custo
  - Pergunta: *Qual o maior custo oculto que vocês já viram em sistemas de LLM?*
- **Diagrama**: Gráfico de custo crescente exponencial vs linear otimizado
- **Animação**: Curva de custo sobe dramáticamente, depois curva otimizada achata
- **Tempo**: 2 min

---

#### Slide 6 — Contexto: Por Que Escalabilidade Agora
- **Tipo**: Conteúdo
- **Objetivo**: Explicar por que escalabilidade de agentes é um problema novo e urgente
- **Conteúdo**:
  - Agentes = múltiplas chamadas de LLM por execução (vs 1 chamada em chat simples)
  - Contexto cresce dentro de uma sessão (KV cache, janela grande)
  - APIs de LLM impõem rate limits (RPM/TPM)
  - Estado de sessão precisa ser distribuído entre réplicas
  - Confluência: frameworks maduros + demanda de produção + pressão de custo
- **Diagrama**: Timeline horizontal: 2023 (protótipos) → 2024 (frameworks) → 2025 (produção) → 2026 (escala)
- **Animação**: Marcos aparecem sequencialmente
- **Tempo**: 1 min

---

### SEÇÃO B — Gargalos de Escala (Slides 7-14 · 10 min)

---

#### Slide 7 — [SEÇÃO] Onde Agentes Esbarram em Escala
- **Tipo**: Seção
- **Objetivo**: Transição para o bloco de gargalos
- **Conteúdo**: Número "1" grande + "Onde Agentes Esbarram em Escala"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 8 — Latência de LLM como Gargalo Dominante
- **Tipo**: Conteúdo
- **Objetivo**: Explicar que a latência do LLM domina o tempo total
- **Conteúdo**:
  - TTFT (Time To First Token) — latência antes da primeira resposta
  - TPOT (Time Per Output Token) — taxa de geração
  - Em um loop ReAct de 5 steps: 5 × (TTFT + TPOT × tokens) = latência cumulativa
  - Latência serial: cada step depende do anterior
  - Comparação: chat simples (~2s) vs agente multi-step (~15-30s)
- **Diagrama**: Bar chart comparando latência por tipo de chamada
- **Animação**: Barras crescem mostrando latência acumulada
- **Tempo**: 2 min

---

#### Slide 9 — Custo Crescendo com Contexto
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar que o custo não é linear — cresce com a janela de contexto
- **Conteúdo**:
  - Cada step do agente envia TODO o histórico anterior
  - Step 1: 1k tokens · Step 5: 15k tokens · Step 10: 40k tokens
  - Custo de input tokens cresce quadraticamente com profundidade do loop
  - KV cache (provider-side) reduz custo mas não elimina
  - Implicação: agente profundo = custo explosivo
- **Diagrama**: Gráfico de custo por step (crescimento quadrático)
- **Animação**: Steps aparecem um a um, barras de custo crescem
- **Tempo**: 1.5 min

---

#### Slide 10 — Concorrência e Rate Limits
- **Tipo**: Conteúdo
- **Objetivo**: Explicar como rate limits impedem escala
- **Conteúdo**:
  - APIs de LLM limitam RPM (requests per minute) e TPM (tokens per minute)
  - Anthropic Claude: tiers com limites crescentes
  - 1.000 usuários simultâneos × 5 steps = 5.000 RPM necessários
  - Sem gestão: 429 Too Many Requests → falhas em cascata
  - Estratégias: filas, backoff exponencial, multi-provider
- **Diagrama**: Diagrama de filas com rate limiter
- **Animação**: Requests chegam, rate limiter deixa passar N/min, resto fila
- **Tempo**: 1.5 min

---

#### Slide 11 — Estado Distribuído
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar o desafio de manter estado entre réplicas
- **Conteúdo**:
  - Agente stateful: sessão, memória, contexto acumulado
  - Com múltiplas réplicas: usuário pode cair em réplica diferente
  - Opções: sticky sessions, estado externo (Redis/Postgres), stateless + checkpoint
  - Tensão: stateless é mais fácil de escalar, mas agentes são inerentemente stateful
  - Aprofundamento em ETHAGT05 (Memória de Agentes)
- **Diagrama**: 3 réplicas com estado compartilhado via Redis
- **Tempo**: 1.5 min

---

#### Slide 12 — Anatomia de um Gargalo
- **Tipo**: Diagrama
- **Objetivo**: Visualizar onde o tempo e o custo se acumulam em um agente
- **Conteúdo**:
  - request → chamada LLM (latência: 2s) → tool calls (latência: 0.5s) → contexto cresce (custo: $$) → loop?
  - Cada componente é um potencial gargalo
  - Latência total = soma serial de todos os steps
  - Custo total = soma de tokens × preço por step
- **Diagrama**: `12-Diagrams/ETHAGT14/bottleneck-analysis.mmd`
- **Animação**: Fluxo percorre o diagrama step-by-step, destacando gargalos em vermelho
- **Tempo**: 2 min

---

#### Slide 13 — Métricas-Chave de Escalabilidade
- **Tipo**: Conteúdo
- **Objetivo**: Definir as métricas que devem ser medidas desde o dia 1
- **Conteúdo**:
  - Latência: TTFT, TPOT, p50/p95/p99 de tempo total
  - Custo: $ por execução, $ por usuário, $ por tenant
  - Throughput: requisições concorrentes, tokens/min
  - Taxa de erro: 429s, timeouts, falhas de tool
  - Cache hit rate: % de requisições servidas do cache
  - Dashboard mínimo: latência, custo, throughput, cache hit, erros
- **Diagrama**: Mini-dashboard com 5 gauges
- **Tempo**: 1 min

---

#### Slide 14 — Pergunta: O Maior Custo Oculto
- **Tipo**: Exercício
- **Objetivo**: Engajar a turma com uma pergunta sobre custos reais
- **Conteúdo**:
  - "Qual o maior custo oculto que vocês já viram em sistemas de LLM?"
  - Opções: contexto crescente? tools? retries? logs? infra?
  - Discussão aberta (3 min)
  - Resposta típica: contexto crescente + retries silenciosos
- **Diagrama**: Caixa de discussão
- **Tempo**: 2 min

---

### SEÇÃO C — Caching (Slides 15-29 · 17 min)

---

#### Slide 15 — [SEÇÃO] Caching: A Primeira Linha de Defesa
- **Tipo**: Seção
- **Objetivo**: Transição para o bloco de caching
- **Conteúdo**: "2 — Caching: A Primeira Linha de Defesa"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 16 — Por Que Caching?
- **Tipo**: Conteúdo
- **Objetivo**: Justificar por que caching é a otimização de maior impacto
- **Conteúdo**:
  - Caching elimina chamadas de LLM redundantes
  - Impacto: reduz custo E latência simultaneamente
  - Cache hit = resposta instantânea + custo zero
  - Em sistemas reais: 30-60% das queries são repetidas ou similares
  - Analogia: "Cache é o único caso onde você ganha algo por nada"
- **Diagrama**: Antes (todas as queries batem no LLM) vs Depois (cache filtra repetições)
- **Animação**: Queries repetidas sendo interceptadas pelo cache
- **Tempo**: 1.5 min

---

#### Slide 17 — Cache de Prompts / Exact Match
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar a forma mais simples de caching
- **Conteúdo**:
  - Mesmo prompt (exato) → mesma resposta
  - Implementação: hash do prompt → lookup em Redis/dict
  - Prompt caching nativo (Anthropic, OpenAI): cache de prefixo no provider
  - Vantagem: trivial de implementar
  - Limitação: só funciona para prompts idênticos (case-sensitive, whitespace-sensitive)
- **Diagrama**: Fluxo: prompt → hash → cache hit? → resposta / LLM
- **Tempo**: 2 min

---

#### Slide 18 — Cache Semântico: Conceito
- **Tipo**: Diagrama
- **Objetivo**: Introduzir o conceito de cache semântico
- **Conteúdo**:
  - Perguntas semanticamente similares → mesma resposta
  - "Qual a capital do Brasil?" ≈ "Capital do Brasil?" ≈ "Brasil capital?"
  - Implementação: embedding da query → busca por similaridade → threshold
  - Se similaridade > threshold: retorna resposta cacheada
  - Se não: chama LLM, armazena resultado
- **Diagrama**: Fluxo: query → embedding → busca vetorial → hit/miss
- **Animação**: Query entra, embedding gerado, comparado com vetores no cache
- **Tempo**: 2 min

---

#### Slide 19 — Cache Semântico: Implementação
- **Tipo**: Código
- **Objetivo**: Mostrar código real de cache semântico
- **Conteúdo**:
  - Snippet: função `semantic_cache(query, threshold=0.92)`
  - Passo 1: embed(query) com modelo leve (e.g., text-embedding-3-small)
  - Passo 2: vector_search no Redis/ChromaDB com top_k=1
  - Passo 3: se similarity > threshold → return cached response
  - Passo 4: senão → llm(query) → store {embedding, query, response}
  - Custo do embedding é ~1000x menor que custo do LLM
- **Diagrama**: Code block + fluxo lado a lado
- **Animação**: Highlight de linhas chave
- **Tempo**: 2 min

---

#### Slide 20 — Threshold de Similaridade
- **Tipo**: Comparação
- **Objetivo**: Discutir o trade-off central do cache semântico
- **Conteúdo**:
  - Threshold alto (0.95): poucos falsos positivos, mas baixa hit rate
  - Threshold baixo (0.80): alta hit rate, mas falsos positivos (resposta errada)
  - Falso positivo = resposta semanticamente próxima mas factualmente errada
  - Exemplo: "Preço do iPhone 15" vs "Preço do iPhone 14" — similares mas diferentes
  - Recomendação: começar com 0.92, ajustar com base em eval
- **Diagrama**: Gráfico de trade-off: threshold vs hit rate vs erro
- **Animação**: Curva se move mostrando o trade-off
- **Tempo**: 1.5 min

---

#### Slide 21 — Cache de Embeddings
- **Tipo**: Conteúdo
- **Objetivo**: Explicar como evitar re-embedding desnecessário
- **Conteúdo**:
  - Embedding de um texto é determinístico (mesmo modelo → mesmo vetor)
  - Re-embeddo mesmo documento a cada query? Desperdício
  - Solução: cache de embeddings (hash do texto → vetor)
  - Útil em RAG: documentos indexados não precisam re-embedding
  - TTL: invalidar quando o modelo de embedding muda
- **Diagrama**: Fluxo: texto → hash → cache hit? → vetor / embed()
- **Tempo**: 1 min

---

#### Slide 22 — Cache de Tool Results
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar que resultados de tools também podem ser cacheados
- **Conteúdo**:
  - Tools idempotentes (GET, search, lookup) → resultado não muda frequentemente
  - Exemplo: `get_weather("Rio de Janeiro")` — cache por 30 min
  - Exemplo: `search_docs("API reference")` — cache por 24h
  - TTL por tool: weather=30min, docs=24h, price=5min
  - Cuidado: tools não-idempotentes (POST, mutate) NÃO devem ser cacheadas
- **Diagrama**: Tabela de tools com TTL recomendado
- **Tempo**: 1.5 min

---

#### Slide 23 — Invalidação e Consistência
- **Tipo**: Conteúdo
- **Objetivo**: Discutir os desafios de manter o cache correto
- **Conteúdo**:
  - Cache stale = resposta desatualizada
  - Estratégias de invalidação:
    - TTL (time-to-live) — simples mas impreciso
    - Event-driven — invalidar quando fonte muda
    - Versionada — chave inclui versão da fonte
  - Consistência eventual: cache pode divergir da fonte por um tempo
  - Em agentes: contexto muda a cada step → cache deve ser por step
- **Diagrama**: Timeline mostrando TTL vs event-driven
- **Tempo**: 1.5 min

---

#### Slide 24 — Cache Poisoning e Mitigação
- **Tipo**: Conteúdo
- **Objetivo**: Alertar sobre riscos de segurança do caching
- **Conteúdo**:
  - Cache poisoning: usuário malicioso injeta resposta errada no cache
  - Cenário: query maliciosa → resposta manipulada → cacheada → servida a outros
  - Mitigação: separar cache por tenant/usuário
  - Mitigação: não cachear respostas de usuários não confiáveis
  - Mitigação: validar resposta antes de cachear
- **Diagrama**: Fluxo de ataque vs fluxo protegido
- **Tempo**: 1 min

---

#### Slide 25 — Estratégia de Camadas (L1/L2)
- **Tipo**: Diagrama
- **Objetivo**: Apresentar uma arquitetura de cache em camadas
- **Conteúdo**:
  - L1: Cache local em memória (ms, por instância)
  - L2: Cache compartilhado em Redis (ms, por cluster)
  - L3: Prompt caching do provider (Anthropic/OpenAI)
  - Fluxo: L1 → L2 → L3 → LLM
  - Cada camada adiciona latência incremental mas reduz custo
- **Diagrama**: Arquitetura em camadas L1 → L2 → L3 → LLM
- **Animação**: Request desce pelas camadas, para no primeiro hit
- **Tempo**: 1 min

---

#### Slide 26 — DEMO: Cache Semântico em Ação
- **Tipo**: Código
- **Objetivo**: Demo ao vivo — adicionar cache semântico a um agente
- **Conteúdo**:
  - Código do `05-Labs/ETHAGT14/Lab1-Cache-Semantico`
  - Primeira chamada → LLM (lenta, cara) → armazena no cache
  - Segunda chamada (pergunta similar) → cache hit (rápida, barata)
  - Medir redução de custo/latência em 10 perguntas
  - Mostrar before/after no terminal
- **Diagrama**: Code block + terminal side-by-side
- **Animação**: Highlight de linhas chave; terminal mostra tempo/custo
- **Tempo**: 4 min

---

#### Slide 27 — Medindo o Impacto (Antes/Depois)
- **Tipo**: Conteúdo
- **Objetivo**: Quantificar o ganho do caching
- **Conteúdo**:
  - Antes: 10 queries × R$0,05 = R$0,50 · Latência média: 3s
  - Depois: 4 queries × R$0,05 + 6 cache hits × R$0,001 = R$0,21 · Latência média: 1.2s
  - Redução de custo: 58%
  - Redução de latência: 60%
  - Cache hit rate: 60%
  - Métrica-chave: cache hit rate deve ser monitorada continuamente
- **Diagrama**: Bar chart antes vs depois (custo e latência)
- **Tempo**: 1 min

---

#### Slide 28 — Pergunta da DEMO
- **Tipo**: Exercício
- **Objetivo**: Engajar a turma com uma pergunta sobre a demo
- **Conteúdo**:
  - "O que acontece se o threshold for muito baixo?"
  - "E se o usuário fizer uma pergunta factual que mudou (ex: 'quem é o presidente')?"
  - "Como detectar que o cache está stale?"
  - Discussão em duplas (2 min)
- **Diagrama**: Caixa de discussão
- **Tempo**: 1 min

---

#### Slide 29 — Exercício: Quando Cache Semântico Falha
- **Tipo**: Exercício
- **Objetivo**: Praticar identificação de cenários onde cache semântico é problemático
- **Conteúdo**:
  - 5 cenários curtos — em quais cache semântico falha?
    1. "Preço das ações da Apple hoje" → Falha (temporal)
    2. "Qual a capital da França?" → Funciona (estável)
    3. "Resuma o último email recebido" → Falha (contextual)
    4. "Como fazer um loop em Python?" → Funciona (estável)
    5. "Qual a previsão do tempo amanhã?" → Falha (temporal)
  - Votação rápida (mãos levantadas)
  - Lição: cache semântico funciona para conhecimento estável, falha para temporal/contextual
- **Diagrama**: 5 cards com cenários
- **Tempo**: 2 min

---

### SEÇÃO D — Model Routing e Otimização (Slides 30-39 · 12 min)

---

#### Slide 30 — [SEÇÃO] Model Routing e Otimização
- **Tipo**: Seção
- **Objetivo**: Transição para otimização de chamadas
- **Conteúdo**: "3 — Model Routing e Otimização"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 31 — Roteamento por Complexidade
- **Tipo**: Comparação
- **Objetivo**: Apresentar o conceito de rotear requisições por complexidade
- **Conteúdo**:
  - Nem toda query precisa do modelo mais caro
  - Haiku ($0.25/M): classificação, extração, Q&A simples
  - Sonnet ($3/M): raciocínio moderado, tool use, análise
  - Opus ($15/M): raciocínio complexo, multi-step, crítico
  - Roteamento automático: classifier → modelo apropriado
  - Economia: 70% das queries podem usar Haiku
- **Diagrama**: Funil: queries → classifier → 3 modelos
- **Animação**: Queries descem pelo funil para o modelo certo
- **Tempo**: 2 min

---

#### Slide 32 — Como Medir Complexidade Antes de Chamar
- **Tipo**: Conteúdo
- **Objetivo**: Discutir como classificar complexidade sem gastar tokens
- **Conteúdo**:
  - Heurísticas baratas: tamanho do input, nº de tools disponíveis, palavra-chave
  - Classifier leve (Haiku/tiny model): "esta query é simples ou complexa?"
  - Histórico: queries similares já classificadas (cache de roteamento)
  - Cascata: tentar Haiku primeiro, escalar para Sonnet se falhar
  - Trade-off: classifier errado = resposta ruim ou custo desnecessário
- **Diagrama**: Fluxo: query → heurística/classifier → modelo
- **Tempo**: 1.5 min

---

#### Slide 33 — Batching de Requests
- **Tipo**: Conteúdo
- **Objetivo**: Explicar como agrupar requisições reduz custo e latência
- **Conteúdo**:
  - N requisições independentes → 1 chamada de API com N prompts
  - Batch de embeddings: 100 textos em 1 chamada
  - Batch de classificações: 10 queries em 1 prompt
  - Reduz: nº de requests (rate limit), overhead de rede, custo de TTFT
  - Limitação: só funciona para requisições independentes (não em loop serial)
- **Diagrama**: Antes (10 requests serial) vs Depois (1 batch)
- **Tempo**: 1.5 min

---

#### Slide 34 — Speculative Decoding / Prediction
- **Tipo**: Conteúdo
- **Objetivo**: Introduzir speculative decoding como técnica de redução de latência
- **Conteúdo**:
  - Modelo pequeno (draft) gera rascunho rápido
  - Modelo grande (target) verifica rascunho em paralelo
  - Se rascunho estiver certo: enorme economia de latência
  - Se errado: target corrige (pequeno overhead)
  - Em agentes: prever próxima action do agente com modelo leve
  - Fonte: arXiv:2211.17192
- **Diagrama**: Fluxo: draft model → target model → aceita/rejeita
- **Tempo**: 1.5 min

---

#### Slide 35 — Streaming para Latência Percebida
- **Tipo**: Conteúdo
- **Objetivo**: Explicar como streaming melhora experiência sem reduzir latência total
- **Conteúdo**:
  - Sem streaming: usuário espera 10s, recebe tudo de uma vez
  - Com streaming: usuário vê tokens em ~0.5s, recebe gradualmente
  - Latência total é a mesma, mas latência PERCEBIDA cai drasticamente
  - Em agentes: streamar thought/answer, não tool calls
  - V/F: "Streaming reduz latência total." → FALSO (reduz percebida, não real)
- **Diagrama**: Comparação visual: barra cheia vs barra preenchendo gradualmente
- **Tempo**: 1.5 min

---

#### Slide 36 — Distilação e Fine-Tuning (Panorama)
- **Tipo**: Conteúdo
- **Objetivo**: Panorama de otimizações mais profundas
- **Conteúdo**:
  - Distilação: treinar modelo menor com saídas de modelo maior
  - Fine-tuning: especializar modelo para domínio (reduz prompt size)
  - Quando vale: volume alto (>100k requests/mês), domínio estável
  - Quando NÃO vale: volume baixo, domínio muda frequentemente
  - Aprofundamento: ETHAGT08 (Fine-tuning) e ETHAGT15 (DSPy)
- **Diagrama**: Árvore de decisão: vale fine-tuning?
- **Tempo**: 1.5 min

---

#### Slide 37 — Matriz de Otimização
- **Tipo**: Comparação
- **Objetivo**: Sistematizar as técnicas de otimização
- **Conteúdo**:
  - Tabela: técnica × impacto (custo/latência/qualidade) × esforço × risco
  - Caching: alto impacto custo/latência, baixo esforço, baixo risco
  - Routing: médio impacto custo, médio esforço, médio risco
  - Batching: médio impacto latência, baixo esforço, baixo risco
  - Speculative: alto impacto latência, alto esforço, alto risco
  - Fine-tuning: alto impacto custo, alto esforço, alto risco
- **Diagrama**: Matriz 2x2 (impacto vs esforço)
- **Tempo**: 1 min

---

#### Slide 38 — Pergunta: Como Decidir?
- **Tipo**: Exercício
- **Objetivo**: Discussão sobre priorização de otimizações
- **Conteúdo**:
  - "Se você tivesse 1 semana para otimizar um agente em produção, por onde começaria?"
  - Resposta esperada: caching primeiro (maior ROI, menor esforço)
  - "Em que cenário routing é melhor que caching?"
  - Discussão aberta (2 min)
- **Tempo**: 2 min

---

#### Slide 39 — Exercício Rápido: Qual Modelo para Qual Tarefa
- **Tipo**: Exercício
- **Objetivo**: Praticar roteamento por complexidade
- **Conteúdo**:
  - 6 tarefas — qual modelo (Haiku/Sonnet/Opus)?
    1. "Classificar este ticket como bug/feature/question" → Haiku
    2. "Resolver este bug complexo de concorrência" → Opus
    3. "Resumir este documento de 5 páginas" → Haiku
    4. "Planejar arquitetura de sistema multi-agente" → Opus
    5. "Extrair entidades deste email" → Haiku
    6. "Decidir qual tool chamar e por quê" → Sonnet
  - Votação rápida
- **Diagrama**: 6 cards com tarefas
- **Tempo**: 2 min

---

### SEÇÃO E — Distribuição (Slides 40-48 · 10 min)

---

#### Slide 40 — [SEÇÃO] Distribuição de Agentes
- **Tipo**: Seção
- **Objetivo**: Transição para distribuição horizontal
- **Conteúdo**: "4 — Distribuição de Agentes"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 41 — Stateless vs Stateful Workers
- **Tipo**: Comparação
- **Objetivo**: Apresentar a distinção fundamental para distribuição
- **Conteúdo**:
  - Stateless: cada request é independente, sem sessão — escala trivialmente
  - Stateful: mantém sessão/contexto entre chamadas — necessário para agentes
  - Agentes são inerentemente stateful (loop, memória, contexto)
  - Solução híbrida: worker stateless + estado externo (Redis/Postgres checkpoint)
  - Tensão: stateless é mais fácil de escalar, mas agentes precisam de estado
- **Diagrama**: Comparação: stateless (qualquer réplica) vs stateful (sticky session)
- **Tempo**: 2 min

---

#### Slide 42 — Sharding por Usuário/Sessão/Domínio
- **Tipo**: Conteúdo
- **Objetivo**: Explicar sharding como estratégia de particionamento
- **Conteúdo**:
  - Sharding: dividir carga por chave (tenant_id, user_id, domínio)
  - Shard 1: tenants A, B · Shard 2: tenants C, D · Shard 3: tenant "hot" Z
  - Cada shard tem DB isolado → isolamento de dados e custo
  - Hot shard: tenant muito ativo recebe shard dedicado
  - Vantagem: isolamento, custo rastreável, sem contenção
  - Desafio: rebalanceamento quando shards desequilibram
- **Diagrama**: `12-Diagrams/ETHAGT14/sharding.mmd`
- **Animação**: Requests chegam, router distribui por shards
- **Tempo**: 2 min

---

#### Slide 43 — Replica e Balanceamento de Carga
- **Tipo**: Conteúdo
- **Objetivo**: Explicar como réplicas aumentam throughput
- **Conteúdo**:
  - Réplica = cópia idêntica do worker para atender mais requisições
  - Load balancer distribui requisições entre réplicas
  - Com N réplicas: throughput × N (se stateless)
  - Com stateful: sticky sessions ou estado externo
  - Health checks: réplica doente é removida do pool
  - Auto-scaling: adiciona/remove réplicas com base na carga
- **Diagrama**: Load balancer → N réplicas → DB compartilhado
- **Tempo**: 1.5 min

---

#### Slide 44 — Estratégias de Balanceamento
- **Tipo**: Comparação
- **Objetivo**: Apresentar algoritmos de load balancing
- **Conteúdo**:
  - Round-robin: distribuição circular, simples
  - Least-connections: envia para réplica com menos conexões ativas
  - Weighted: réplicas mais potentes recebem mais carga
  - Latency-based: envia para réplica com menor latência
  - Hash-based (consistent hashing): mesmo tenant → mesma réplica
  - Para agentes: least-connections ou consistent hashing (preserva sessão)
- **Diagrama**: 4 mini-diagramas das estratégias
- **Tempo**: 1 min

---

#### Slide 45 — Coordenação: Consensus e Leader Election
- **Tipo**: Conteúdo
- **Objetivo**: Introduzir coordenação distribuída
- **Conteúdo**:
  - Quando múltiplos workers precisam concordar: consensus
  - Raft/Paxos: algoritmos de consenso distribuído
  - Leader election: um worker é "líder", outros são "followers"
  - Casos de uso em agentes:
    - Orquestrador principal (leader) → workers (followers)
    - Distribuição de tarefas entre agentes
    - Locks distribuídos (apenas um agente edita recurso por vez)
  - Ferramentas: etcd, ZooKeeper, Redis Redlock
- **Diagrama**: Cluster com leader e followers
- **Tempo**: 1.5 min

---

#### Slide 46 — Multi-Region e Autoscaling
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar escala geográfica e automática
- **Conteúdo**:
  - Multi-region: reduzir latência para usuários globais
  - Latência inter-região: ~50-100ms (vs <5ms intra-região)
  - Desafio: replicação de estado entre regiões
  - Autoscaling: HPA (Horizontal Pod Autoscaler) no Kubernetes
  - KEDA: autoscaling baseado em eventos (fila, métricas custom)
  - Escala para zero: serverless quando não há tráfego
  - Métricas de escala: CPU, memória, tamanho de fila, latência
- **Diagrama**: Mapa global com 3 regiões + autoscaling arrows
- **Tempo**: 1.5 min

---

#### Slide 47 — Pergunta: Stateless é Sempre Preferível?
- **Tipo**: Exercício
- **Objetivo**: Discussão sobre o trade-off stateless vs stateful
- **Conteúdo**:
  - "Stateless é sempre preferível? Justifique."
  - Casos onde stateful é necessário:
    - Sessões longas com contexto acumulado
    - WebSockets / streaming
    - Estado em memória para baixa latência
  - "Como você tornaria um agente stateful mais 'stateless-friendly'?"
  - Resposta: checkpoint externo + restore on-demand
  - Discussão aberta (2 min)
- **Tempo**: 2 min

---

### SEÇÃO F — Infraestrutura (Slides 49-54 · 5 min)

---

#### Slide 48 — [SEÇÃO] Infraestrutura para Agentes
- **Tipo**: Seção
- **Objetivo**: Transição para infraestrutura
- **Conteúdo**: "5 — Infraestrutura para Agentes"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 49 — Kubernetes para Agentes
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar K8s como plataforma de orquestração para agentes
- **Conteúdo**:
  - Pods: unidade mínima (1 agente worker por pod)
  - Deployments: réplicas + rolling updates
  - HPA: autoscaling horizontal baseado em CPU/métricas
  - Services: load balancing interno
  - Ingress: entrada de tráfego externo
  - ConfigMaps/Secrets: configuração e secrets
  - Vantagem: padronização, portabilidade entre clouds
- **Diagrama**: Arquitetura K8s: Ingress → Service → Pods → DB
- **Tempo**: 1 min

---

#### Slide 50 — Serverless vs Dedicado
- **Tipo**: Comparação
- **Objetivo**: Comparar os dois modelos de deploy
- **Conteúdo**:
  - Serverless (AWS Lambda, Cloud Run):
    - Escala para zero, paga por execução
    - Cold start: 1-5s de latência inicial
    - Ideal: tráfego esporádico, baixo volume
  - Dedicado (EC2, ECS, EKS):
    - Sempre ativo, sem cold start
    - Custo fixo, independente de uso
    - Ideal: tráfego constante, alto volume
  - Para agentes: dedicado é geralmente melhor (cold start quebra UX)
- **Diagrama**: Tabela comparativa: serverless vs dedicado
- **Tempo**: 1 min

---

#### Slide 51 — GPUs para Inferência Local
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar inferência local como alternativa
- **Conteúdo**:
  - vLLM, TGI (Text Generation Inference): servidores de inferência otimizados
  - Modelos open-source: Llama, Mistral, Qwen
  - Vantagem: custo fixo, sem rate limit, baixa latência
  - Desafio: custo de GPU ($1-8/hora), manutenção, qualidade vs Claude/GPT
  - Quando vale: alto volume, privacidade, latência crítica
  - Quando não vale: baixo volume, qualidade prioritária
- **Diagrama**: Decisão: API vs self-hosted
- **Tempo**: 1 min

---

#### Slide 52 — Service Mesh
- **Tipo**: Conteúdo
- **Objetivo**: Introduzir service mesh para comunicação entre agentes
- **Conteúdo**:
  - Múltiplos agentes = múltiplos serviços comunicando entre si
  - Service mesh (Istio, Linkerd): camada de comunicação transparente
  - Features: mTLS, retries, circuit breakers, observabilidade
  - Traffic splitting: canary deployments (10% tráfego nova versão)
  - Para agentes: tracing distribuído entre chamadas de agentes
- **Diagrama**: Service mesh com sidecar proxies
- **Tempo**: 1 min

---

#### Slide 53 — Custo de Infra Total
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar que LLM não é o único custo
- **Conteúdo**:
  - Custos escondidos:
    - Memória: Redis para cache/estado (~$50-500/mês)
    - Rede: transferência entre regiões (~$50-200/mês)
    - Storage: vetores, logs, traces (~$20-200/mês)
    - Compute: K8s nodes, GPUs (~$200-2000/mês)
    - Observabilidade: Datadog, LangSmith (~$50-300/mês)
  - Regra: custo de LLM é ~60-70% do total, infra é 30-40%
  - Não ignore infra ao calcular TCO
- **Diagrama**: Pie chart: LLM 65%, Compute 15%, Memória 10%, Outros 10%
- **Tempo**: 1 min

---

### SEÇÃO G — FinOps de Agentes (Slides 55-63 · 8 min)

---

#### Slide 54 — [SEÇÃO] FinOps de Agentes
- **Tipo**: Seção
- **Objetivo**: Transição para FinOps
- **Conteúdo**: "6 — FinOps de Agentes"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 55 — Orçamento por Execução/Usuário/Tenant
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar orçamento como guardrail fundamental
- **Conteúdo**:
  - Orçamento por execução: máximo de $X por run do agente
  - Orçamento por usuário: máximo de $Y/mês por usuário
  - Orçamento por tenant: máximo de $Z/mês por empresa/cliente
  - Implementação: contador de custo acumulado → circuit breaker
  - Sem orçamento: um usuário pode gerar $1000 em uma noite
  - Com orçamento: agente para e avisa quando limite é atingido
- **Diagrama**: 3 níveis de orçamento (execução → usuário → tenant)
- **Tempo**: 1.5 min

---

#### Slide 56 — Medição Granular de Custo
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar como medir custo em nível de step/tool
- **Conteúdo**:
  - Por step: cada iteração do loop ReAct tem custo próprio
  - Por tool: qual tool gera mais tokens de contexto?
  - Por token: input vs output (preços diferentes)
  - Por modelo: se há routing, custo varia por modelo
  - Tagging: cada execução carrega tags (usuário, tenant, categoria, feature)
  - Dashboard: custo por feature, por tenant, por modelo, por tool
- **Diagrama**: Hierarquia de custo: execução → step → tool → tokens
- **Tempo**: 1 min

---

#### Slide 57 — Trade-offs: Custo × Latência × Qualidade
- **Tipo**: Diagrama
- **Objetivo**: Visualizar o triângulo de trade-offs
- **Conteúdo**:
  - Os 3 eixos estão em tensão:
    - Reduzir custo → pode aumentar latência ou reduzir qualidade
    - Reduzir latência → pode aumentar custo ou reduzir qualidade
    - Aumentar qualidade → pode aumentar custo e latência
  - Não existe otimização gratuita (pick two)
  - Exemplo: Haiku é barato e rápido, mas menos capaz
  - Exemplo: Opus é capaz, mas caro e lento
  - Decisão: qual eixo é mais importante para seu caso de uso?
- **Diagrama**: Triângulo com Custo, Latência, Qualidade nos vértices
- **Animação**: Vértices se destacam um a um
- **Tempo**: 1.5 min

---

#### Slide 58 — Fluxo FinOps
- **Tipo**: Diagrama
- **Objetivo**: Visualizar o ciclo de FinOps de agentes
- **Conteúdo**:
  - execução → medir custo granular → tag (usuário/tenant/categoria) → dashboard
  - dashboard → alerta: custo > orçamento? → sim: circuit breaker / não: ok
  - dashboard → otimização contínua (routing, cache)
  - Loop fechado: medir → alertar → otimizar → medir
- **Diagrama**: `12-Diagrams/ETHAGT14/finops-flow.mmd`
- **Animação**: Fluxo percorre o diagrama, circuit breaker aciona em vermelho
- **Tempo**: 1 min

---

#### Slide 59 — Dashboards de Custo Contínuo
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar como visualizar e otimizar custo continuamente
- **Conteúdo**:
  - Dashboard mínimo (Grafana):
    - Custo por dia/semana/mês
    - Custo por feature (qual funcionalidade consome mais)
    - Custo por tenant (qual cliente consome mais)
    - Cache hit rate (efetividade do cache)
    - Top 10 execuções mais caras
  - Alertas: custo diário > threshold → Slack/email
  - Otimização contínua: identificar anomalias e agir
- **Diagrama**: Mockup de dashboard Grafana
- **Tempo**: 1 min

---

#### Slide 60 — Pricing para Clientes
- **Tipo**: Conteúdo
- **Objetivo**: Discutir como precificar um produto agêntico
- **Conteúdo**:
  - Modelo per-call: cobrar por execução do agente (transparência)
  - Modelo por tokens: repassar custo de tokens + margem
  - Modelo assinatura: valor fixo mensal com limite (previsibilidade)
  - Modelo freemium: tier gratuito limitado + tier pago
  - Modelo por valor: cobrar por outcome (resolvido, não resolvido)
  - Pergunta: *Você cobraria por chamada de API ou assinatura mensal?*
  - Tensão: custo é variável, pricing precisa ser previsível para o cliente
- **Diagrama**: Tabela comparativa de modelos de pricing
- **Tempo**: 1 min

---

#### Slide 61 — Circuit Breaker de Custo
- **Tipo**: Código
- **Objetivo**: Mostrar implementação de circuit breaker de custo
- **Conteúdo**:
  - Snippet: `CostCircuitBreaker(budget=0.10)` antes de cada chamada de LLM
  - Antes de chamar LLM: `breaker.check(estimated_cost)` → raise se exceder
  - Após chamada: `breaker.add(actual_cost)` → atualiza contador
  - Exceção amigável: "Orçamento de R$0,10 excedido para esta execução"
  - Log + alerta para monitoramento
  - Padrão: fail-safe (bloqueia em caso de dúvida)
- **Diagrama**: Code block com syntax highlighting
- **Tempo**: 1 min

---

#### Slide 62 — Exercício: Orçamento com Circuit Breaker
- **Tipo**: Exercício
- **Objetivo**: Praticar implementação de circuit breaker
- **Conteúdo**:
  - Cenário: sistema multi-tenant com orçamento de R$100/usuário/mês
  - Em duplas: escrever lógica de circuit breaker que bloqueia execuções se custo mensal exceder
  - Incluir: alerta, log, exceção amigável
  - Bônus: o que acontece se o orçamento for compartilhado entre features?
  - 3 min código, 2 min compartilhar abordagens
- **Diagrama**: Caixa de exercício com template de código
- **Tempo**: 4 min

---

### SEÇÃO H — Fechamento (Slides 64-75 · 12 min)

---

#### Slide 63 — [SEÇÃO] Boas Práticas e Anti-Patterns
- **Tipo**: Seção
- **Objetivo**: Transição para o fechamento
- **Conteúdo**: "7 — Boas Práticas e Anti-Patterns"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 64 — Boas Práticas (DO)
- **Tipo**: Conteúdo
- **Objetivo**: Checklist de boas práticas de escalabilidade
- **Conteúdo**:
  - Comece por caching (maior ROI, menor esforço)
  - Meça custo desde a primeira linha de código
  - Defina orçamento por execução desde o dia 1
  - Use routing para separar queries simples de complexas
  - Faça checkpoint do estado externamente (stateless-friendly)
  - Monitore cache hit rate continuamente
  - Use autoscaling com métricas de negócio (fila, latência), não só CPU
  - Teste sob carga antes de ir para produção
- **Diagrama**: Checklist verde (etho-success)
- **Tempo**: 2 min

---

#### Slide 65 — Anti-Patterns (DON'T)
- **Tipo**: Conteúdo
- **Objetivo**: Checklist do que NÃO fazer
- **Conteúdo**:
  - Não medir custo (surpresa no fim do mês)
  - Não definir orçamento (usuário gera $1000 em uma noite)
  - Usar sempre o modelo mais caro (desperdício)
  - Não cachear (todas as queries batem no LLM)
  - Manter estado em memória sem checkpoint (perda em restart)
  - Ignorar rate limits (429 em cascata)
  - Não monitorar cache hit rate (cache ineficaz sem saber)
  - Otimizar antes de medir (premature optimization)
- **Diagrama**: Checklist vermelho (etho-danger)
- **Tempo**: 2 min

---

#### Slide 66 — Caso de Estudo: Assistente de Empresa em Escala
- **Tipo**: Diagrama
- **Objetivo**: Mostrar todos os conceitos em um caso real
- **Conteúdo**:
  - Cenário: assistente corporativo para 5.000 funcionários
  - Antes: 1 agente por usuário, sem cache, sempre Sonnet
    - Custo: R$15k/mês · Latência p95: 12s · Taxa de erro: 5%
  - Depois: cache semântico + routing + sharding por departamento + FinOps
    - Custo: R$4k/mês (−73%) · Latência p95: 4s (−67%) · Taxa de erro: 1%
  - Otimizações aplicadas: cache (40%), routing (20%), batching (10%), infra (3%)
  - Lição: escalabilidade é combinação de técnicas, não uma bala de prata
- **Diagrama**: Arquitetura antes vs depois
- **Tempo**: 2 min

---

#### Slide 67 — Resumo da Aula
- **Tipo**: Resumo
- **Objetivo**: Sintetizar os pontos-chave
- **Conteúdo**:
  - Gargalos: latência de LLM, custo de contexto, rate limits, estado distribuído
  - Caching = primeira linha de defesa (exact, semântico, embeddings, tools)
  - Routing = separar simples de complexo (Haiku/Sonnet/Opus)
  - Distribuição = stateless + checkpoint, sharding por tenant, replica + balanceamento
  - Infra = K8s + autoscaling + service mesh
  - FinOps = orçamento, medição granular, circuit breaker, trade-offs
  - Projeto: otimizar custo/latência ≥40% sem perder qualidade
- **Diagrama**: 7 ícones com os pontos-chave
- **Tempo**: 2 min

---

#### Slide 68 — Checklist da Aula
- **Tipo**: Resumo
- **Objetivo**: Confirmar que todos os tópicos foram cobertos
- **Conteúdo**:
  - [ ] Identificou gargalos de escala
  - [ ] Implementou cache semântico
  - [ ] Configurou model routing
  - [ ] Distribuiu agentes com sharding
  - [ ] Configurou FinOps com circuit breaker
  - [ ] Discutiu trade-offs custo × latência × qualidade
- **Diagrama**: Checklist visual
- **Tempo**: 1 min

---

#### Slide 69 — Quiz: Pergunta 1
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "Qual é a PRIMEIRA otimização que você deve aplicar a um agente em produção?"
  - A) Fine-tuning do modelo
  - B) Caching (semântico + exact match)
  - C) Multi-region deployment
  - D) Speculative decoding
  - Resposta: B (maior ROI, menor esforço)
- **Tempo**: 1 min

---

#### Slide 70 — Quiz: Pergunta 2
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "Cache semântico com threshold muito baixo (ex: 0.75) causa qual problema?"
  - A) Aumenta latência
  - B) Falsos positivos (resposta errada servida como correta)
  - C) Rate limit excedido
  - D) Aumenta custo de embedding
  - Resposta: B
- **Tempo**: 1 min

---

#### Slide 71 — Quiz: Pergunta 3
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "Streaming reduz a latência TOTAL de uma resposta?"
  - A) Sim, significativamente
  - B) Sim, marginalmente
  - C) Não, reduz apenas a latência PERCEBIDA
  - D) Não, aumenta a latência total
  - Resposta: C
- **Tempo**: 1 min

---

#### Slide 72 — Perguntas para Discussão
- **Tipo**: Exercício
- **Objetivo**: Estimular debate
- **Conteúdo**:
  1. "Em que cenário cache semântico é mais perigoso que útil?"
  2. "Stateless é sempre preferível? Justifique com um contra-exemplo."
  3. "Como você convenceria um CTO a investir em FinOps antes de escalar?"
  4. "Qual o maior risco de autoscaling baseado apenas em CPU?"
- **Tempo**: 2 min

---

#### Slide 73 — Conexão com Próximos Módulos
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar como ETHAGT14 conecta com o resto da especialização
- **Conteúdo**:
  - ETHAGT15 — Meta-Agentes: auto-aprendizado que pode otimizar custos
  - ETHAGT90 — Capstone: otimização de custo em sistema real
  - ETHAGT12 — AgentOps: observabilidade em profundidade (traces, eval)
  - ETHAGT05 — Memória de Agentes: estado distribuído em detalhe
- **Diagrama**: Mapa da especialização com ETHAGT14 destacado
- **Tempo**: 1 min

---

#### Slide 74 — Referências e Leitura Recomendada
- **Tipo**: Referências
- **Objetivo**: Indicar o que ler antes da próxima aula
- **Conteúdo**:
  - Obrigatório: Kleppmann, M. *Designing Data-Intensive Applications*
  - Obrigatório: FinOps Foundation, *FinOps for ML/AI*
  - Recomendado: *Speculative Decoding* (arXiv:2211.17192)
  - Recomendado: vLLM docs (serving LLMs)
  - Recomendado: Richards & Ford, *Fundamentals of Software Architecture*
  - Docs: LiteLLM (roteamento e custo), OpenTelemetry, Grafana
  - Projeto: otimizar custo/latência ≥40% com ADR + FinOps dashboard
  - Labs: Lab 1 (Cache Semântico, 4h), Lab 2 (Sharding por Tenant, 5h)
- **Tempo**: 1 min

---

#### Slide 75 — Q&A / Encerramento
- **Tipo**: Capa
- **Objetivo**: Abrir para perguntas e encerrar
- **Conteúdo**:
  - "Perguntas?"
  - Contato do professor
  - "Na próxima aula: ETHAGT15 — Meta-Agentes & Sistemas Autoaprendentes"
- **Diagrama**: Logo Etho + fundo etho-dark
- **Tempo**: 2 min

---

## Resumo do Storyboard

| Seção | Slides | Tempo | Conteúdo |
|---|---|---|---|
| A — Abertura | 1-6 | 8 min | Capa, objetivos, competências, agenda, motivação, contexto |
| B — Gargalos | 7-14 | 10 min | Latência, custo, rate limits, estado, bottleneck, métricas |
| C — Caching | 15-29 | 17 min | Exact, semântico, embeddings, tools, invalidação, DEMO, exercício |
| D — Routing | 30-39 | 12 min | Complexidade, batching, speculative, streaming, distilação, exercício |
| E — Distribuição | 40-47 | 10 min | Stateless, sharding, replica, balanceamento, consensus, multi-region |
| F — Infraestrutura | 49-53 | 5 min | K8s, serverless, GPUs, service mesh, custo total |
| G — FinOps | 55-62 | 8 min | Orçamento, medição, trade-offs, dashboards, pricing, circuit breaker |
| H — Fechamento | 64-75 | 12 min | Boas práticas, anti-patterns, caso, resumo, quiz, discussão, referências, Q&A |
| **Total** | **75** | **90 min** | |

---

## Diagramas Necessários

| # | Slide | Diagrama | Tipo | Fonte |
|---|---|---|---|---|
| D1 | 5 | Custo crescente exponencial vs otimizado | Gráfico | Novo |
| D2 | 8 | Latência por tipo de chamada (bar chart) | Bar chart | Novo |
| D3 | 9 | Custo por step (crescimento quadrático) | Gráfico | Novo |
| D4 | 10 | Rate limiter com filas | Flowchart | Novo |
| D5 | 11 | Réplicas com estado compartilhado (Redis) | Arquitetura | Novo |
| D6 | 12 | Anatomia de um gargalo | Flowchart | `12-Diagrams/ETHAGT14/bottleneck-analysis.mmd` |
| D7 | 16 | Antes vs depois do caching | Comparação | Novo |
| D8 | 18 | Cache semântico: conceito | Flowchart | Novo |
| D9 | 19 | Cache semântico: implementação | Código + fluxo | Novo |
| D10 | 20 | Threshold vs hit rate vs erro | Gráfico de trade-off | Novo |
| D11 | 25 | Cache em camadas L1/L2/L3 | Arquitetura | Novo |
| D12 | 31 | Funil de routing (Haiku/Sonnet/Opus) | Funil | Novo |
| D13 | 34 | Speculative decoding | Sequência | Novo |
| D14 | 35 | Streaming vs não-streaming | Comparação | Novo |
| D15 | 37 | Matriz de otimização (impacto vs esforço) | Matriz 2x2 | Novo |
| D16 | 41 | Stateless vs stateful workers | Comparação | Novo |
| D17 | 42 | Sharding por tenant | Flowchart | `12-Diagrams/ETHAGT14/sharding.mmd` |
| D18 | 44 | Estratégias de balanceamento | Grid 2x2 | Novo |
| D19 | 45 | Cluster com leader e followers | Arquitetura | Novo |
| D20 | 46 | Mapa multi-region + autoscaling | Mapa | Novo |
| D21 | 49 | Arquitetura K8s para agentes | Arquitetura | Novo |
| D22 | 53 | Pie chart de custo total | Pie chart | Novo |
| D23 | 57 | Triângulo custo × latência × qualidade | Triângulo | Novo |
| D24 | 58 | Fluxo FinOps | Flowchart | `12-Diagrams/ETHAGT14/finops-flow.mmd` |
| D25 | 59 | Mockup de dashboard Grafana | Dashboard | Novo |
| D26 | 66 | Arquitetura antes vs depois (caso de estudo) | Comparação | Novo |
| D27 | 73 | Mapa da especialização | Mind map | Novo |

---

## Pendências de Produção

- [ ] Produzir 24 diagramas novos (D1-D5, D7-D16, D18-D23, D25-D27)
- [ ] Screenshot do terminal com before/after do cache (Slide 26)
- [ ] Screenshot do código com syntax highlighting (Slides 19, 26, 61)
- [ ] Imagem de fundo para capa (Slide 1)
- [ ] Badge de competências (Slide 3)
- [ ] Mockup de dashboard Grafana (Slide 59)
- [ ] Mapa multi-region (Slide 46)
- [ ] Template de exercício para circuit breaker (Slide 62)

---

> **Aguardando aprovação deste storyboard para gerar os slides detalhados com notas do professor.**
