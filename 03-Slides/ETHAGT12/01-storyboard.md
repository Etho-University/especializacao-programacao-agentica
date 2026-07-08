# ETHAGT12 — AgentOps, Observabilidade & Avaliação
## Storyboard da Apresentação

> **Universidade Etho · Especialização em Programação Agêntica**
> Fase D — Produção, Governança e Fronteira · 30 h
> Storyboard v1.0 · Julho 2026

---

## Metadados da Apresentação

| Campo | Valor |
|---|---|
| Código | ETHAGT12 |
| Título | AgentOps, Observabilidade & Avaliação (LLMOps para agentes) |
| Duração estimada | 90 min (2 blocos de 45 min) |
| Total de slides | 78 |
| Público | Arquitetos, Engenheiros de Software, Engenheiros de IA, Platform Engineers, Tech Leads |
| Pré-requisitos | ETHAGT11 |
| Competências | C1 (A), C2 (B), C4 (B), C5 (A) |

---

## Mapa Visual da Apresentação

```
BLOCO 1 (45 min)                              BLOCO 2 (45 min)
┌──────────────────────────────┐              ┌──────────────────────────────┐
│ SEÇÃO A — Abertura (8 min)   │              │ SEÇÃO E — Benchmarks (14 min)│
│  Capa · Objetivos · Agenda   │              │  SWE-bench · GAIA · τ-bench  │
│  Motivação · Contexto        │              │  AgentBench · WebArena       │
├──────────────────────────────┤              │  Contaminação · Limites      │
│ SEÇÃO B — Por que difícil    │              ├──────────────────────────────┤
│  (10 min)                     │              │ SEÇÃO F — Melhoria & Report  │
│  Não-determinismo · Falácias │              │  (12 min)                     │
│  Custo de runs · Vibes-eval  │              │  CI · Shadow · Canary         │
├──────────────────────────────┤              │  Eval report · Análise falhas│
│ SEÇÃO C — Observabilidade    │              ├──────────────────────────────┤
│  (16 min)                     │              │ SEÇÃO G — Fechamento (12 min) │
│  Traces · Spans · OTel       │              │  Boas práticas · Anti-patterns│
│  LangSmith · Phoenix · DEMO  │              │  Caso de estudo · Resumo     │
├──────────────────────────────┤              │  Quiz · Projeto · Referências│
│ SEÇÃO D — Avaliação (18 min) │              │  Q&A                         │
│  LLM-as-judge · Golden cases │              └──────────────────────────────┘
│  Métricas · CI · DEMO        │
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
  - ETHAGT12 — AgentOps, Observabilidade & Avaliação
  - Universidade Etho · Especialização em Programação Agêntica
  - Fase D — Produção, Governança e Fronteira
  - Professor · Data
- **Diagrama**: Logo Etho + imagem de fundo abstrata (dashboards/grafos de traces)
- **Animação**: Fade in do título
- **Tempo**: 1 min

---

#### Slide 2 — Objetivos do Módulo
- **Tipo**: Conteúdo
- **Objetivo**: Deixar claro o que o aluno deve conseguir fazer ao final
- **Conteúdo**:
  - Objetivo geral: Estabelecer rigor experimental em sistemas de agentes — observar, medir, avaliar e iterar com confiança
  - 5 objetivos específicos (1 linha cada):
    1. Implementar observabilidade end-to-end (traces, spans, métricas)
    2. Construir pipelines de avaliação automatizada (LLM-as-judge, golden cases, regressão)
    3. Aplicar benchmarks canônicos (SWE-bench, GAIA, τ-bench, AgentBench, WebArena)
    4. Operar ciclos de melhoria contínua com dados
    5. Reportar resultados com rigor (eval report)
- **Diagrama**: Ícones representando cada objetivo
- **Animação**: Aparecer objetivos um a um (on click)
- **Tempo**: 2 min

---

#### Slide 3 — Competências Desenvolvidas
- **Tipo**: Conteúdo
- **Objetivo**: Conectar a aula ao Framework Etho de competências
- **Conteúdo**:
  - Tabela: 4 competências com nível B/I/A
  - C1 Programação Agêntica → **A**
  - C2 Multi-Agent Systems → B
  - C4 Agent Memory → B
  - C5 AgentOps & Avaliação → **A**
  - Badge visual por competência
- **Diagrama**: Radar chart dos 4 pilares
- **Animação**: Radar aparece com wipe
- **Tempo**: 1 min

---

#### Slide 4 — Agenda
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar o roteiro da aula com tempos
- **Conteúdo**:
  - Bloco 1: Abertura → Por que difícil → Observabilidade → Avaliação
  - Bloco 2: Benchmarks → Ciclo de melhoria → Fechamento
  - Tempos estimados por seção
- **Diagrama**: Timeline horizontal com 7 seções
- **Animação**: Timeline cresce da esquerda para direita
- **Tempo**: 1 min

---

#### Slide 5 — Motivação: 5/5 no Teste, 30% em Produção
- **Tipo**: Conteúdo
- **Objetivo**: Criar tensão — agentes não-determinísticos falham em casos que você não testou
- **Conteúdo**:
  - Cenário: agente funcionou 5/5 no teste manual, mas em produção acertou 30%
  - Sem métrica, você não sabia que estava falhando
  - "Parece que funciona" não é medida
  - Pergunta: *Como você sabe se seu agente está ficando melhor ou pior?*
- **Diagrama**: Gráfico de barras — "Teste manual: 100%" vs "Produção: 30%"
- **Animação**: Barras crescem lado a lado; a de produção para em 30%
- **Tempo**: 2 min

---

#### Slide 6 — Contexto: Por Que AgentOps Agora
- **Tipo**: Conteúdo
- **Objetivo**: Explicar a confluência que tornou AgentOps essencial
- **Conteúdo**:
  - Linha do tempo: 2022 (ChatGPT) → 2023 (primeiros agentes) → 2024 (SWE-bench, observabilidade) → 2025 (AgentOps como disciplina)
  - Confluência: agentes não-determinísticos + custo de runs + necessidade de iterar com confiança
  - LLMOps tradicional não cobre: tools, loops, estado, ambiente
  - Hamel Husain: "Evals for LLMs" como marco conceitual
- **Diagrama**: Timeline horizontal com marcos
- **Animação**: Marcos aparecem sequencialmente
- **Tempo**: 1 min

---

### SEÇÃO B — Por que Agentes São Difíceis de Avaliar (Slides 7-14 · 10 min)

---

#### Slide 7 — [SEÇÃO] Por que Agentes São Difíceis de Avaliar
- **Tipo**: Seção
- **Objetivo**: Transição para o bloco de fundamentos
- **Conteúdo**: Número "1" grande + "Por que Agentes São Difíceis de Avaliar"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 8 — Não-Determinismo em Agentes
- **Tipo**: Conteúdo
- **Objetivo**: Explicar por que a mesma entrada pode dar resultados diferentes
- **Conteúdo**:
  - LLMs são probabilísticos: mesma pergunta, respostas diferentes
  - Agentes amplificam: cada step tem não-determinismo que se acumula
  - Temperatura, sampling, tool choice podem variar
  - Implicação: avaliação única não é suficiente — precisamos de N runs
  - Pergunta: *Você já rodou o mesmo prompt duas vezes e teve resultados diferentes?*
- **Diagrama**: Árvore de possibilidades — 1 prompt → múltiplos caminhos
- **Animação**: Ramos da árvore aparecem um a um
- **Tempo**: 2 min

---

#### Slide 9 — Dependência de Ambiente
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar que agentes dependem de mundo externo mutável
- **Conteúdo**:
  - Tools chamam APIs que podem mudar de comportamento
  - RAG depende de base de conhecimento que evolui
  - Ambiente de execução (sistema de arquivos, web) muda entre runs
  - Exemplo: agente que usa API de cotação — resultado depende do momento
  - Implicação: avaliação precisa de ambiente controlado ou sandbox
- **Diagrama**: Agente cercado por fontes externas mutáveis (API, DB, Web, FS)
- **Tempo**: 1.5 min

---

#### Slide 10 — Custo de Runs
- **Tipo**: Conteúdo
- **Objetivo**: Explicar que avaliar agentes custa dinheiro real
- **Conteúdo**:
  - Cada run = tokens de entrada + tokens de saída × N steps
  - Agente complexo: 10-50 chamadas de LLM por tarefa
  - Avaliar 1000 casos × 50 chamadas × $0.01/chamada = $500
  - Benchmarks completos (SWE-bench): centenas de dólares por modelo
  - Estratégias: amostragem, subconjuntos, eval incremental
- **Diagrama**: Fórmula de custo cumulativo
- **Tempo**: 1.5 min

---

#### Slide 11 — Falácias Comuns de Avaliação
- **Tipo**: Conteúdo
- **Objetivo**: Desconstruir crenças perigosas sobre avaliação de agentes
- **Conteúdo**:
  - "Funcionou uma vez" → sobrevivência de amostra size=1
  - "Parece bom" → vibes-based eval, não escala
  - "O usuário não reclamou" → usuários desistem silenciosamente
  - "Passou no benchmark" → benchmark ≠ produção
  - "LLM disse que está correto" → LLM-as-judge sem calibração
  - Pergunta: *Qual dessas falácias você já cometeu?*
- **Diagrama**: 5 cards de falácia com ícone de "armadilha"
- **Animação**: Cards aparecem um a um com efeito de "queda"
- **Tempo**: 2 min

---

#### Slide 12 — Avaliação Contínua vs Pontual
- **Tipo**: Comparação
- **Objetivo**: Mostrar que avaliação não é evento, é processo
- **Conteúdo**:
  - Pontual: "rodamos eval antes do deploy" → estátua (congela no tempo)
  - Contínua: eval roda a cada mudança, em produção, com drift detection
  - Agentes mudam: prompt, tool, modelo, ambiente evoluem
  - Sem eval contínua: regressão passa despercebida por semanas
- **Diagrama**: Duas timelines — pontual (marcas isoladas) vs contínua (linha contínua)
- **Tempo**: 1 min

---

#### Slide 13 — Vibes-Based Eval: A Armadilha
- **Tipo**: Citação
- **Objetivo**: Fixar o anti-pattern mais comum
- **Conteúdo**:
  - "Se você não tem um conjunto de avaliação, você está fazendo vibes-based development." — Hamel Husain
  - Vibes = intuição, não medida
  - Intuição é útil para explorar, não para decidir deploy
  - Regra: todo deploy precisa de número, não de feeling
- **Diagrama**: Ícone de "vibes" (emoji/sentimento) vs ícone de "métrica" (gráfico)
- **Tempo**: 0.5 min

---

#### Slide 14 — Exercício: Identificando Falácias
- **Tipo**: Exercício
- **Objetivo**: Praticar o reconhecimento de falácias em cenários reais
- **Conteúdo**:
  - 4 afirmações curtas; alunos identificam a falácia
  - 1. "Testei com 3 exemplos e funcionou, pode ir para produção."
  - 2. "O benchmark mostra 80%, então o agente está bom."
  - 3. "O GPT-4 disse que a resposta está correta."
  - 4. "Ninguém reclamou desde o deploy."
  - Votação rápida (mãos levantadas)
- **Diagrama**: 4 cards com afirmações
- **Tempo**: 1 min

---

### SEÇÃO C — Observabilidade (Slides 15-27 · 16 min)

---

#### Slide 15 — [SEÇÃO] Observabilidade Desde o Dia 1
- **Tipo**: Seção
- **Objetivo**: Transição para o bloco de observabilidade
- **Conteúdo**: "2 — Observabilidade: Traces, Spans, Métricas"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 16 — Traces: O Que São
- **Tipo**: Diagrama
- **Objetivo**: Introduzir o conceito de trace como árvore de execução
- **Conteúdo**:
  - Trace = registro completo de uma execução de agente
  - Estrutura de árvore: root span → child spans → sub-spans
  - Cada span: nome, duração, input, output, atributos
  - Diferença de log: trace mostra relações e hierarquia
  - "Sem traces, você está debugando no escuro"
- **Diagrama**: Árvore de spans conceitual
- **Animação**: Spans surgem da raiz para as folhas
- **Tempo**: 2 min

---

#### Slide 17 — Anatomia de um Trace
- **Tipo**: Diagrama
- **Objetivo**: Mostrar a estrutura detalhada de um trace de agente
- **Conteúdo**:
  - Root span: tarefa completa (ex: "reservar voo")
  - Child spans: chamada LLM 1, tool call A, chamada LLM 2, tool call B
  - Sub-spans: API request dentro de tool call
  - Atributos por span: model, tokens, latency, tool name, args, result
  - Bags: contexto propagado entre spans (user_id, session_id)
- **Diagrama**: `12-Diagrams/ETHAGT12/trace-anatomy.mmd`
- **Animação**: Spans aparecem hierarquicamente (root → children → sub-spans)
- **Tempo**: 2 min

---

#### Slide 18 — OpenTelemetry para LLMs
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar o padrão de observabilidade para GenAI
- **Conteúdo**:
  - OpenTelemetry: padrão CNCF para observabilidade distribuída
  - GenAI semantic conventions: atributos padronizados para LLMs
    - `gen_ai.system`, `gen_ai.request.model`, `gen_ai.usage.prompt_tokens`
  - Vantagem: vendor-neutral — funciona com qualquer backend
  - Para agentes: traces cruzam LLM calls, tool calls, retrieval
- **Diagrama**: Exemplo de span com atributos GenAI
- **Tempo**: 2 min

---

#### Slide 19 — Tooling: LangSmith, Phoenix, Langfuse
- **Tipo**: Comparação
- **Objetivo**: Apresentar as ferramentas principais de observabilidade para agentes
- **Conteúdo**:
  - LangSmith: integrado ao LangChain/LangGraph; dashboard rico; comercial
  - Phoenix (Arize): open source; foco em LLM observability; eval integrado
  - Langfuse: open source self-hostable; traces + eval + prompts management
  - OpenLLMetry: instrumentação automática OpenTelemetry para LLMs
  - Critério de escolha: stack existente, self-host vs SaaS, custo
- **Diagrama**: Tabela comparativa (4 colunas)
- **Tempo**: 2 min

---

#### Slide 20 — Logs Estruturados vs Traces
- **Tipo**: Comparação
- **Objetivo**: Clarificar quando usar cada abordagem
- **Conteúdo**:
  - Logs estruturados: JSON com timestamp, step, thought, action, observation
  - Traces: árvore hierárquica com timing e relações
  - Logs: simples, barato, bom para debug rápido
  - Traces: rico, relacional, bom para análise e produção
  - Prática: comece com logs estruturados, evolua para traces
  - Complementares, não mutuamente exclusivos
- **Diagrama**: Comparação lado a lado
- **Tempo**: 1.5 min

---

#### Slide 21 — Custo de Observabilidade (Amostragem)
- **Tipo**: Conteúdo
- **Objetivo**: Explicar que observabilidade também custa
- **Conteúdo**:
  - Cada trace gera storage + processamento
  - Em alto volume: 100% de traces é caro
  - Amostragem: registrar apenas 1 em N traces
  - Estratégias: head-based (decide no início), tail-based (decide no fim)
  - Tail sampling: sempre logar traces com erro, amostrar sucesso
  - Regra: 100% em dev, amostrado em produção, 100% em erro
- **Diagrama**: Funil de amostragem
- **Tempo**: 1.5 min

---

#### Slide 22 — Dashboard Mínimo de Observabilidade
- **Tipo**: Diagrama
- **Objetivo**: Definir o que todo dashboard de agente deve ter
- **Conteúdo**:
  - Painel 1: Success rate por tarefa (últimas 24h)
  - Painel 2: Latência P50/P95/P99 por step
  - Painel 3: Custo por execução (tokens × preço)
  - Painel 4: Tool usage (qual tool, quantas vezes, sucesso/falha)
  - Painel 5: Erros agrupados por tipo
  - Painel 6: Distribuição de steps (agente fazendo muitos loops?)
- **Diagrama**: Mock de dashboard com 6 painéis
- **Tempo**: 1.5 min

---

#### Slide 23 — Métricas de Primeira Classe: Custo e Latência
- **Tipo**: Conteúdo
- **Objetivo**: Fixar que custo e latência são métricas, não detalhes
- **Conteúdo**:
  - Custo por execução: tokens in/out × preço por modelo
  - Latência cumulativa: serial = soma; paralelo = max
  - P95 e P99 importam mais que média (cauda longa)
  - Orçamento por execução: abortar se custo > limite
  - Em produção: alerta se custo médio sobe 20%
- **Diagrama**: Mini-gráfico de latência P50/P95/P99
- **Tempo**: 1 min

---

#### Slide 24 — DEMO: Traces Everywhere
- **Tipo**: Código
- **Objetivo**: Demo ao vivo — adicionar observabilidade a um agente existente
- **Conteúdo**:
  - Código do `05-Labs/ETHAGT12/Lab1-Traces-Everywhere`
  - Agente ReAct simples sem observabilidade
  - Adicionar LangSmith (ou Phoenix) com 3 linhas
  - Mostrar trace completo: pergunta → thought → tool call → observation → response
  - Dashboard: latência, custo por step, erros
  - Identificar gargalo no trace (tool call lenta)
- **Diagrama**: Code block + trace viewer side-by-side
- **Animação**: Highlight das linhas que adicionam observabilidade
- **Tempo**: 3 min

---

#### Slide 25 — Pergunta da DEMO
- **Tipo**: Exercício
- **Objetivo**: Engajar a turma com uma pergunta sobre a demo
- **Conteúdo**:
  - "O que o trace revelou que logs simples não mostrariam?"
  - "Qual step do agente é o gargalo de latência?"
  - "Como você decidiria se vale otimizar esse step?"
  - Discussão em duplas (2 min)
- **Diagrama**: Caixa de discussão
- **Tempo**: 2 min

---

#### Slide 26 — Exercício: Lendo um Trace
- **Tipo**: Exercício
- **Objetivo**: Praticar análise de trace para identificar problemas
- **Conteúdo**:
  - Mostrar um trace real com problema (agente em loop de 8 steps)
  - Em duplas: identificar onde o loop acontece
  - Propor 2 correções (max_steps? prompt? tool?)
  - 2 min discussão, 1 min compartilhar
- **Diagrama**: Trace de console com problema destacado
- **Tempo**: 3 min

---

#### Slide 27 — Pergunta: Observabilidade — Custo ou Investimento?
- **Tipo**: Exercício
- **Objetivo**: Refletir sobre o ROI de observabilidade
- **Conteúdo**:
  - "Observabilidade é custo operacional ou investimento estratégico?"
  - Argumento custo: storage, tooling, overhead de instrumentação
  - Argumento investimento: debugging mais rápido, regressão detectada, otimização guiada por dados
  - "Sem observabilidade, você não tem como melhorar o que não mede"
- **Tempo**: 1 min

---

### SEÇÃO D — Avaliação Automatizada (Slides 28-43 · 18 min)

---

#### Slide 28 — [SEÇÃO] Avaliação Automatizada
- **Tipo**: Seção
- **Objetivo**: Transição para o bloco de avaliação
- **Conteúdo**: "3 — Avaliação Automatizada: LLM-as-Judge, Golden Cases, Regressão"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 29 — Por que Avaliação Manual Não Escala
- **Tipo**: Conteúdo
- **Objetivo**: Justificar a necessidade de automação
- **Conteúdo**:
  - Manual: humano lê output e julga → lento, caro, inconsistente
  - Não escala: 1000 casos × 5 min/caso = 83 horas
  - Humano fica cansado: qualidade decai ao longo do dia
  - Não é reproduzível: mesmo humano julga diferente em outro dia
  - Solução: automação com LLM-as-judge + golden cases + métricas programáticas
- **Diagrama**: Escada de mão (manual, não escala) vs escada rolante (automatizada)
- **Tempo**: 1 min

---

#### Slide 30 — LLM-as-Judge: Conceito
- **Tipo**: Diagrama
- **Objetivo**: Apresentar o padrão de usar LLM para avaliar LLM
- **Conteúdo**:
  - LLM-as-judge: um LLM avalia a saída de outro LLM
  - Padrão: input + output + critério (rubrica) → judge → score + justificativa
  - Vantagem: escala, barato, reproduzível (com temperatura 0)
  - Quando usar: tarefas subjetivas (qualidade de resposta, completude)
  - Quando NÃO usar: tarefas com ground truth exato (use string match)
- **Diagrama**: Fluxo — agent output → judge prompt → judge LLM → score
- **Tempo**: 2 min

---

#### Slide 31 — LLM-as-Judge: Vieses
- **Tipo**: Conteúdo
- **Objetivo**: Ser honesto sobre as limitações do LLM-as-judge
- **Conteúdo**:
  - Positional bias: prefere primeira ou última opção
  - Sycophancy: concorda com o que o humano parece querer
  - Verbosity bias: prefere respostas mais longas
  - Self-preference: modelo prefere saídas do mesmo modelo
  - Knowledge bias: judge não sabe o que o agente deveria saber
  - Pergunta: *Qual desses vieses é mais perigoso para seu caso de uso?*
- **Diagrama**: 5 ícones de viés com labels
- **Tempo**: 2 min

---

#### Slide 32 — LLM-as-Judge: Mitigações
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar estratégias para reduzir vieses do judge
- **Conteúdo**:
  - Rubrica clara: critérios explícitos, não "avalie a qualidade"
  - Exemplos: few-shot com casos calibrados por humano
  - Múltiplos judges: 3+ modelos, média ou votação
  - Calibração: comparar judge com humano em subconjunto
  - Swap de posição: rodar A vs B e B vs A, média dos resultados
  - Cross-model: usar modelo diferente do agente como judge
- **Diagrama**: Checklist de mitigações
- **Tempo**: 2 min

---

#### Slide 33 — Golden Cases: O Que São
- **Tipo**: Conteúdo
- **Objetivo**: Introduzir o conceito de casos de teste para agentes
- **Conteúdo**:
  - Golden case = par (input, critério de sucesso)
  - Input: pergunta/tarefa para o agente
  - Critério: como saber se a resposta está correta
    - Exato: string match, regex, JSON schema
    - Subjetivo: rubrica para LLM-as-judge
    - Funcional: tool foi chamada? ação foi executada?
  - Conjunto crescente: cada bug encontrado vira golden case
- **Diagrama**: Cartão de golden case com campos
- **Tempo**: 1.5 min

---

#### Slide 34 — Escrevendo um Golden Case
- **Tipo**: Código
- **Objetivo**: Mostrar um golden case concreto em código
- **Conteúdo**:
  - Estrutura: id, input, expected_behavior, eval_fn, category
  - Exemplo:
    - id: "GC-042"
    - input: "Qual a capital da França?"
    - eval_fn: `assert "Paris" in response`
    - category: "factual"
  - Exemplo subjetivo:
    - input: "Resuma este artigo em 3 pontos"
    - eval_fn: LLM-as-judge com rubrica "3 pontos, fiel ao original"
  - Snippet de código em Python
- **Diagrama**: Code block com exemplo
- **Tempo**: 1.5 min

---

#### Slide 35 — Conjuntos de Regressão
- **Tipo**: Conteúdo
- **Objetivo**: Explicar como golden cases formam um conjunto de regressão
- **Conteúdo**:
  - Conjunto de regressão: N golden cases que rodam a cada mudança
  - Toda mudança de prompt, tool, ou modelo roda o conjunto
  - Se score cai: deploy bloqueado (CI gate)
  - Crescimento: conjunto começa com 10, cresce para 100+ com tempo
  - Categorização: factual, multi-step, tool-use, edge-case, error-handling
  - Manutenção: remover casos obsoletos, adicionar casos de bug
- **Diagrama**: Pipeline — mudança → roda regressão → score → gate
- **Tempo**: 1.5 min

---

#### Slide 36 — Métricas de Tarefa
- **Tipo**: Conteúdo
- **Objetivo**: Definir métricas que medem o resultado final
- **Conteúdo**:
  - Success rate: % de casos que passaram no critério
  - Partial credit: nem tudo ou nada (0.7 se 7 de 10 sub-tarefas corretas)
  - Custo por execução: tokens × preço
  - Latência P50/P95: tempo total da tarefa
  - Para benchmarks: score oficial (ex: SWE-bench usa % resolved)
- **Diagrama**: Tabela de métricas com fórmulas
- **Tempo**: 1.5 min

---

#### Slide 37 — Métricas de Processo
- **Tipo**: Conteúdo
- **Objetivo**: Definir métricas que medem como o agente chegou ao resultado
- **Conteúdo**:
  - Número de steps: quantas iterações do loop ReAct
  - Loops detectados: agente repetiu a mesma action?
  - Tool misuse rate: % de tool calls que falharam ou foram inúteis
  - Token efficiency: tokens usados / tokens necessários
  - Recovery rate: % de vezes que agente se recuperou de erro
  - Por que importa: processo explica sucesso ou fracasso
- **Diagrama**: Dashboard de processo
- **Tempo**: 1.5 min

---

#### Slide 38 — A/B Testing de Prompts e Tools
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar experimentação controlada para agentes
- **Conteúdo**:
  - A/B test: versão A (atual) vs versão B (nova) no mesmo conjunto
  - Variáveis: prompt, tool description, modelo, temperatura, max_steps
  - Uma variável por vez (ou design de experimentos)
  - Métricas: success rate, custo, latência, satisfação
  - Significância: N grande o suficiente (mínimo 30 casos por versão)
  - Pergunta: *Você mudaria o prompt sem A/B test?*
- **Diagrama**: Duas versões lado a lado, resultados comparados
- **Tempo**: 1 min

---

#### Slide 39 — Pipeline de Eval com CI
- **Tipo**: Diagrama
- **Objetivo**: Mostrar como eval se integra ao pipeline de deploy
- **Conteúdo**:
  - Mudança (prompt/tool/modelo) → CI roda eval
  - CI executa: golden cases + subconjunto de benchmark
  - LLM-as-judge avalia resultados
  - Compara com baseline: houve regressão?
  - Sim → bloquear deploy; Não → permitir deploy
  - Pipeline automatizado, não manual
- **Diagrama**: `12-Diagrams/ETHAGT12/eval-pipeline.mmd`
- **Animação**: Fluxo percorrido step-by-step
- **Tempo**: 2 min

---

#### Slide 40 — DEMO: Eval Automatizado
- **Tipo**: Código
- **Objetivo**: Demo ao vivo — construir pipeline de eval com LLM-as-judge
- **Conteúdo**:
  - Código do `05-Labs/ETHAGT12/Lab2-Eval-Automatizado`
  - Agente com 10 golden cases
  - Mudar prompt do agente
  - Rodar eval: score cai de 85% para 72%
  - Mostrar: quais casos regrediram? Por quê?
  - LLM-as-judge com rubrica para casos subjetivos
- **Diagrama**: Terminal + eval report side-by-side
- **Animação**: Highlight da regressão detectada
- **Tempo**: 3 min

---

#### Slide 41 — Pergunta da DEMO
- **Tipo**: Exercício
- **Objetivo**: Engajar com pergunta sobre regressão
- **Conteúdo**:
  - "A regressão é real ou o judge está errado?"
  - "Como distinguir bug do agente de viés do judge?"
  - "O que fazer: reverter o prompt ou corrigir os casos?"
  - Discussão aberta (2 min)
- **Diagrama**: Caixa de discussão
- **Tempo**: 2 min

---

#### Slide 42 — Exercício: Escrevendo um Golden Case
- **Tipo**: Exercício
- **Objetivo**: Praticar a escrita de casos de teste para agentes
- **Conteúdo**:
  - Cenário: agente de reserva de voo
  - Em duplas: escrever 2 golden cases com critério mensurável
  - Um caso factual (ex: "voo direto encontrado")
  - Um caso subjetivo (ex: "resposta clara e útil")
  - 3 min escrita, 2 min compartilhar
- **Diagrama**: Template de golden case para preencher
- **Tempo**: 3 min

---

#### Slide 43 — V/F: "LLM-as-Judge É Sempre Confiável"
- **Tipo**: Exercício
- **Objetivo**: Quebrar o mito da confiabilidade automática do judge
- **Conteúdo**:
  - Verdadeiro ou Falso: "LLM-as-judge é sempre confiável"
  - Resposta: **Falso**
  - LLM-as-judge tem vieses (positional, sycophancy, verbosity, self-preference)
  - Mitigações necessárias: rubrica, calibração, múltiplos judges
  - Sem calibração com humano, judge pode estar sistematicamente errado
- **Diagrama**: Card V/F com explicação
- **Tempo**: 1 min

---

### SEÇÃO E — Benchmarks Canônicos (Slides 44-54 · 14 min)

---

#### Slide 44 — [SEÇÃO] Benchmarks Canônicos
- **Tipo**: Seção
- **Objetivo**: Transição para o bloco de benchmarks
- **Conteúdo**: "4 — Benchmarks Canônicos: SWE-bench, GAIA, τ-bench"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 45 — Por que Benchmarks?
- **Tipo**: Conteúdo
- **Objetivo**: Justificar o uso de benchmarks padronizados
- **Conteúdo**:
  - Benchmark = conjunto padronizado de tarefas com critério objetivo
  - Permite comparar modelos e arquiteturas de forma justa
  - Reprodutível: mesma tarefa, mesmo critério, resultado comparável
  - Referência da comunidade: "meu agente faz X% no SWE-bench"
  - Limitação: benchmark ≠ produção (veremos)
  - Pergunta: *Você confia em um score de benchmark sem ter rodado?*
- **Diagrama**: Balança: benchmark (padronizado) vs eval custom (representativo)
- **Tempo**: 1.5 min

---

#### Slide 46 — Landscape de Benchmarks
- **Tipo**: Diagrama
- **Objetivo**: Visão geral dos benchmarks canônicos
- **Conteúdo**:
  - SWE-bench — código (resolver issues de GitHub)
  - GAIA — raciocínio geral multi-step
  - τ-bench — tool use em domínios (airline, retail)
  - WebArena — navegação web autônoma
  - AgentDojo — segurança (injeção em agentes)
  - τ²-bench — multi-agent tool use
- **Diagrama**: `12-Diagrams/ETHAGT12/benchmark-landscape.mmd`
- **Animação**: Cada benchmark aparece com click
- **Tempo**: 2 min

---

#### Slide 47 — SWE-bench / SWE-bench Verified
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar o benchmark de código mais influente
- **Conteúdo**:
  - SWE-bench: 2.294 issues reais de 12 repositórios Python open source
  - Tarefa: resolver issue → gerar patch → testes passam
  - SWE-bench Verified: subconjunto de 500 com validação humana
  - Claude 3.5 Sonnet: ~49% no Verified (dez/2024)
  - Por que importa: código é verificável (testes = ground truth)
  - Fonte: Jimenez et al., arXiv:2310.06770
- **Diagrama**: Fluxo — issue → agente → patch → testes → pass/fail
- **Tempo**: 2 min

---

#### Slide 48 — GAIA
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar o benchmark de raciocínio geral
- **Conteúdo**:
  - GAIA: 466 questões de raciocínio multi-step com tools
  - Níveis: Level 1 (simples) → Level 3 (complexo, dezenas de steps)
  - Requer: web search, file processing, reasoning, tool use
  - Human: ~92% no Level 1; GPT-4 + plugins: ~15%
  - Por que importa: testa capacidade geral de agente assistente
  - Fonte: Mialon et al., arXiv:2311.12983
- **Diagrama**: Exemplo de questão GAIA com steps esperados
- **Tempo**: 1.5 min

---

#### Slide 49 — τ-bench
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar o benchmark de tool use em domínios
- **Conteúdo**:
  - τ-bench: tool-agent-user interaction em domínios (airline, retail)
  - Agente simula atendente com acesso a APIs (policy, booking, etc.)
  - Avalia: success rate em tarefas com usuários simulados
  - Domínios: airline (policy-driven), retail (catalog-driven)
  - Por que importa: testa tool use realista com políticas
  - Fonte: Yao et al., arXiv:2404.44529
- **Diagrama**: Arquitetura τ-bench — user simulator ↔ agent ↔ tools
- **Tempo**: 1.5 min

---

#### Slide 50 — AgentBench e WebArena
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar benchmarks de panorama amplo e navegação web
- **Conteúdo**:
  - AgentBench: 8 ambientes (OS, DB, KG, web, card game, etc.)
  - Avalia capacidades diversas: reasoning, planning, tool use
  - WebArena: navegação web autônoma em sites simulados
  - Tarefas: "encontre o produto mais barato", "agende reunião"
  - VisualWebArena: adiciona compreensão visual
  - Fontes: Liu et al. (arXiv:2308.03688), Zhou et al. (arXiv:2307.13854)
- **Diagrama**: Grid dos ambientes do AgentBench
- **Tempo**: 1.5 min

---

#### Slide 51 — Como Rodar Localmente
- **Tipo**: Conteúdo
- **Objetivo**: Dar orientação prática de execução
- **Conteúdo**:
  - SWE-bench: Docker + eval harness (repositório GitHub)
  - GAIA: download do dataset + tools (web search, file tools)
  - τ-bench: pip install + simulate user
  - Custo: SWE-bench completo = $$ (muitas runs); subconjuntos = $$ controlável
  - Dica: comece com subconjunto (10-50 casos) para iterar rápido
  - Tempo: SWE-bench completo = horas; subconjunto = minutos
- **Diagrama**: Tabela de custo/tempo por benchmark
- **Tempo**: 1.5 min

---

#### Slide 52 — Limites e Contaminação
- **Tipo**: Conteúdo
- **Objetivo**: Ser honesto sobre os limites dos benchmarks
- **Conteúdo**:
  - Contaminação: dados de treino podem incluir o benchmark
  - Overfitting: otimizar para benchmark ≠ melhorar para produção
  - Coverage: benchmark cobre domínio específico, não seu caso de uso
  - Saturação: modelos melhores → benchmark fica fácil → perde poder discriminante
  - Detecção de contaminação: overlaps de n-gramas, memorização
  - Pergunta: *Um score alto em SWE-bench garante bom desempenho em produção?*
- **Diagrama**: Sinais de contaminação e overfitting
- **Tempo**: 2 min

---

#### Slide 53 — Exercício: Escolhendo um Benchmark
- **Tipo**: Exercício
- **Objetivo**: Praticar a seleção de benchmark adequado
- **Conteúdo**:
  - 4 cenários curtos; alunos escolhem o benchmark
  - 1. "Agente de coding que resolve issues" → SWE-bench
  - 2. "Assistente de pesquisa geral" → GAIA
  - 3. "Agente de atendimento com APIs" → τ-bench
  - 4. "Bot que navega e-commerce" → WebArena
  - Votação rápida (mãos levantadas)
- **Diagrama**: 4 cards com cenários
- **Tempo**: 1 min

---

#### Slide 54 — Pergunta: Benchmark vs Produção
- **Tipo**: Exercício
- **Objetivo**: Refletir sobre o gap entre benchmark e produção
- **Conteúdo**:
  - "Um score alto em benchmark garante bom desempenho em produção?"
  - Resposta: Não necessariamente
  - Benchmark é ambiente controlado; produção é mundo real
  - Combinar: benchmark (comparável) + eval custom (representativo)
  - "Benchmark diz o que é possível; eval custom diz o que é real"
- **Tempo**: 1 min

---

### SEÇÃO F — Ciclo de Melhoria & Reportando Resultados (Slides 55-64 · 12 min)

---

#### Slide 55 — [SEÇÃO] Ciclo de Melhoria Contínua
- **Tipo**: Seção
- **Objetivo**: Transição para o bloco de melhoria contínua
- **Conteúdo**: "5 — Ciclo de Melhoria Contínua e Reportando Resultados"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 56 — Dataset Crescente
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar o princípio de que eval é um ativo que cresce
- **Conteúdo**:
  - "Você não mediu se não mediu" — cada execução é dado
  - Produção gera casos: logs de conversas, feedback de usuário
  - Triagem: humano classifica (bom/ruim/edge case)
  - Bug encontrado → novo golden case (nunca mais regredir)
  - Crescimento: 10 → 50 → 200 → 1000+ casos ao longo de meses
  - Dataset é vantagem competitiva: seu concorrente não tem seus casos
- **Diagrama**: Funil — produção → triagem → golden cases → regressão
- **Tempo**: 1.5 min

---

#### Slide 57 — CI para Agentes (Testes de Regressão)
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar como eval se integra ao CI/CD
- **Conteúdo**:
  - Toda mudança (prompt, tool, modelo, config) dispara eval
  - CI roda: golden cases + subconjunto de benchmark
  - Gate: se regressão > threshold → bloquear merge
  - Threshold: 0% para casos críticos, 5% para casos não-críticos
  - Velocidade: CI eval precisa rodar em < 10 min (subconjunto)
  - Full eval: noturno ou pré-deploy
- **Diagrama**: Pipeline CI — PR → eval → gate → merge/deploy
- **Tempo**: 1.5 min

---

#### Slide 58 — Shadow Runs e Canary
- **Tipo**: Diagrama
- **Objetivo**: Apresentar estratégias de deploy seguro para agentes
- **Conteúdo**:
  - Shadow run: nova versão roda em paralelo sem afetar usuário
  - Compara outputs: versão atual vs versão nova
  - Canary: 5% → 25% → 50% → 100% do tráfego
  - Rollback automático: se métricas degradam, volta para versão anterior
  - Para agentes: shadow é ideal — sem risco para usuário
  - Diferença de tradicional: agente não-determinístico precisa de mais amostras
- **Diagrama**: Fluxo — shadow (paralelo) → canary (5%) → full (100%)
- **Tempo**: 1.5 min

---

#### Slide 59 — Feedback Humano Estruturado
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar como coletar feedback que vira dado de eval
- **Conteúdo**:
  - Thumbs up/down: simples, mas sem contexto
  - Feedback estruturado: categoria (errado/incompleto/lento/off-topic) + texto
  - Implicit feedback: usuário refez a pergunta? Abandonou?
  - Loop: feedback → triagem → golden case → regressão
  - Cuidado: feedback enviesado (só usuários frustrados respondem)
- **Diagrama**: Ciclo — usuário → feedback → triagem → golden case → melhoria
- **Tempo**: 1.5 min

---

#### Slide 60 — [SEÇÃO] Reportando Resultados
- **Tipo**: Seção
- **Objetivo**: Transição para reporte de resultados
- **Conteúdo**: "6 — Reportando Resultados com Rigor"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 61 — Eval Report (Template)
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar a estrutura de um eval report profissional
- **Conteúdo**:
  - Template: `24-Templates/template-eval-report.md`
  - Seções:
    1. Sumário executivo (1 parágrafo)
    2. Metodologia (dataset, métricas, N runs)
    3. Resultados (tabela: métrica × versão)
    4. Análise de falhas (categorização)
    5. Comparações (vs baseline, vs humano)
    6. Recomendações (deploy? corrigir? investigar?)
  - Princípio: reprodutível — outro engenheiro consegue rerodar
- **Diagrama**: Mock do template preenchido
- **Tempo**: 1.5 min

---

#### Slide 62 — Análise de Falhas (Categorização)
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar como categorizar falhas sistematicamente
- **Conteúdo**:
  - Categorias canônicas:
    1. Não entendeu a tarefa (interpretação errada)
    2. Tool errada (escolheu tool inadequada)
    3. Alucinação (inventou fato/tool/result)
    4. Loop infinito (não convergiu)
    5. Erro de tool (API falhou, formato errado)
    6. Incompleto (parou antes de terminar)
  - Por que categorizar: direciona onde investir esforço
  - Exemplo: 60% das falhas são "tool errada" → melhorar ACI
- **Diagrama**: Gráfico de pizza com categorias de falha
- **Tempo**: 1.5 min

---

#### Slide 63 — Comparações Honestas
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar princípios de comparação justa
- **Conteúdo**:
  - Sempre comparar vs baseline (versão anterior)
  - Comparar vs humano quando possível (ground truth)
  - Mesmas condições: mesmo dataset, mesmo ambiente, mesmo N
  - Reportar intervalo de confiança, não só média
  - Honestidade: reportar onde perdeu, não só onde ganhou
  - Pergunta: *O que é mais importante reportar para o CEO — accuracy ou custo por execução?*
- **Diagrama**: Tabela comparativa com baseline, versão nova, humano
- **Tempo**: 1.5 min

---

#### Slide 64 — Exercício: Detectando Regressão
- **Tipo**: Exercício
- **Objetivo**: Praticar análise de regressão em cenário real
- **Conteúdo**:
  - Cenário: time mudou o prompt e o eval score caiu de 85% para 72%
  - Em grupos: analisar causas possíveis
    - Viés do judge?
    - Mudança real no comportamento?
    - Casos que regrediram — padrão?
  - Propor: próximos passos (A/B test? rever casos? corrigir prompt?)
  - 3 min discussão, 2 min compartilhar
- **Diagrama**: Eval report parcial para analisar
- **Tempo**: 3 min

---

### SEÇÃO G — Fechamento (Slides 65-78 · 12 min)

---

#### Slide 65 — [SEÇÃO] Fechamento
- **Tipo**: Seção
- **Objetivo**: Transição para o fechamento
- **Conteúdo**: "7 — Fechamento: Boas Práticas, Caso de Estudo, Quiz"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 66 — Boas Práticas (DO)
- **Tipo**: Conteúdo
- **Objetivo**: Checklist de boas práticas de AgentOps
- **Conteúdo**:
  - Comece com logs estruturados desde a primeira linha de código
  - Adicione traces antes de adicionar features
  - Construa golden cases desde o dia 1 (comece com 10)
  - Rode eval a cada mudança (CI gate)
  - Use LLM-as-judge com calibração humana
  - Categorize falhas para direcionar esforço
  - Cresça o dataset continuamente (produção → casos)
  - Reporte com honestidade: inclua onde perdeu
- **Diagrama**: Checklist verde (etho-success)
- **Tempo**: 1 min

---

#### Slide 67 — Anti-Patterns (DON'T)
- **Tipo**: Conteúdo
- **Objetivo**: Checklist do que NÃO fazer em AgentOps
- **Conteúdo**:
  - Vibes-based eval ("parece bom")
  - Sem observabilidade em produção
  - Eval manual que não escala
  - LLM-as-judge sem calibração
  - Benchmark como única medida de qualidade
  - Deploy sem gate de regressão
  - Não categorizar falhas ("saber que falhou" sem "por quê")
  - Dataset estagnado (mesmos 10 casos para sempre)
  - Overfitting para benchmark
- **Diagrama**: Checklist vermelho (etho-danger)
- **Tempo**: 1 min

---

#### Slide 68 — Caso de Estudo: Anthropic Avaliando Claude em SWE-bench
- **Tipo**: Diagrama
- **Objetivo**: Mostrar todos os conceitos em um caso real
- **Conteúdo**:
  - Anthropic avaliando Claude 3.5 Sonnet em SWE-bench
  - Metodologia: SWE-bench Verified (500 casos, validação humana)
  - Resultado: ~49% resolved (dez/2024)
  - Processo de melhoria: iterar com traces + eval contínua
  - Análise de falhas: categorizou onde Claude falhava
  - Lição: melhoria guiada por dados, não por intuição
  - "Não há magia — é rigor experimental aplicado"
- **Diagrama**: Ciclo de melhoria da Anthropic — eval → trace → corrigir → re-eval
- **Tempo**: 2 min

---

#### Slide 69 — Resumo da Aula
- **Tipo**: Resumo
- **Objetivo**: Sintetizar os pontos-chave
- **Conteúdo**:
  - Agentes são difíceis de avaliar: não-determinismo, ambiente, custo
  - Observabilidade desde o dia 1: traces, spans, métricas
  - LLM-as-judge com calibração: escala, mas tem vieses
  - Golden cases + regressão: o CI gate de agentes
  - Benchmarks canônicos: SWE-bench, GAIA, τ-bench — comparável mas ≠ produção
  - Dataset crescente: sua vantagem competitiva
  - Eval report: rigor e honestidade
- **Diagrama**: 7 ícones com os pontos-chave
- **Tempo**: 1 min

---

#### Slide 70 — Checklist da Aula
- **Tipo**: Resumo
- **Objetivo**: Confirmar que todos os tópicos foram cobertos
- **Conteúdo**:
  - [ ] Explicou por que agentes são difíceis de avaliar
  - [ ] Implementou observabilidade com traces
  - [ ] Construiu pipeline de eval com LLM-as-judge
  - [ ] Descreveu benchmarks canônicos
  - [ ] Explicou CI para agentes e regressão
  - [ ] Apresentou estrutura de eval report
- **Diagrama**: Checklist visual
- **Tempo**: 0.5 min

---

#### Slide 71 — Quiz: Pergunta 1
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "Qual é a principal limitação do LLM-as-judge?"
  - A) É muito caro para usar
  - B) Não consegue avaliar texto
  - C) Tem vieses (positional, sycophancy, verbosity) que precisam de mitigação
  - D) Só funciona com GPT-4
  - Resposta: C
- **Tempo**: 1 min

---

#### Slide 72 — Quiz: Pergunta 2
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "O que é um golden case?"
  - A) Um caso de uso de sucesso para marketing
  - B) Um par (input, critério de sucesso) usado como teste de regressão
  - C) Um caso que sempre passa no eval
  - D) Um benchmark padronizado
  - Resposta: B
- **Tempo**: 1 min

---

#### Slide 73 — Quiz: Pergunta 3
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "O que o SWE-bench avalia?"
  - A) Navegação web autônoma
  - B) Atendimento ao cliente com tools
  - C) Resolução de issues reais de GitHub (código)
  - D) Raciocínio geral multi-step
  - Resposta: C
- **Tempo**: 1 min

---

#### Slide 74 — Quiz: Pergunta 4
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "Em um pipeline de CI para agentes, o que bloqueia o deploy?"
  - A) Latência acima de 1 segundo
  - B) Regressão no eval score (golden cases + benchmark subset)
  - C) Número de steps diferente da versão anterior
  - D) Custo acima de $0.01 por run
  - Resposta: B
- **Tempo**: 1 min

---

#### Slide 75 — Quiz: Pergunta 5
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "V/F: 'Bom score em benchmark garante bom desempenho em produção.'"
  - A) Verdadeiro — benchmarks são representativos
  - B) Falso — benchmark é ambiente controlado, produção é mundo real
  - C) Depende — só se o benchmark for do mesmo domínio
  - D) Verdadeiro — se passou em SWE-bench, está pronto
  - Resposta: B
- **Tempo**: 1 min

---

#### Slide 76 — Conexão com Próximos Módulos e Projeto
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar como ETHAGT12 conecta com o resto e apresentar projeto
- **Conteúdo**:
  - ETHAGT13 — Segurança & Governança: observabilidade como defesa
  - ETHAGT90 — Capstone: eval report completo
  - Projeto do módulo: avaliar um agente em subconjunto de τ-bench ou GAIA
    - Entrega: eval report + dataset + código de rerun + análise de falhas
    - Critério: eval reproduzível; ≥3 categorias de falha documentadas
  - Lab 1 (5h): "Traces Everywhere" — adicionar observabilidade a um agente
  - Lab 2 (5h): "Eval automatizado" — pipeline com LLM-as-judge + golden cases
- **Diagrama**: Mapa da especialização com ETHAGT12 destacado
- **Tempo**: 1.5 min

---

#### Slide 77 — Leitura Recomendada e Referências
- **Tipo**: Referências
- **Objetivo**: Indicar leitura obrigatória e complementar
- **Conteúdo**:
  - Obrigatório: Jimenez et al., *SWE-bench* (arXiv:2310.06770)
  - Obrigatório: Mialon et al., *GAIA* (arXiv:2311.12983)
  - Obrigatório: Yao et al., *τ-bench* (arXiv:2404.44529)
  - Recomendado: Hamel Husain, *Evals for LLMs*
  - Recomendado: Liu et al., *AgentBench* (arXiv:2308.03688)
  - Recomendado: Zhou et al., *WebArena* (arXiv:2307.13854)
  - Docs: LangSmith, Phoenix (Arize), Langfuse, OpenLLMetry, OpenTelemetry GenAI
- **Tempo**: 1 min

---

#### Slide 78 — Q&A / Encerramento
- **Tipo**: Capa
- **Objetivo**: Abrir para perguntas e encerrar
- **Conteúdo**:
  - "Perguntas?"
  - Contato do professor
  - "Na próxima aula: ETHAGT13 — Segurança & Governança de Agentes"
- **Diagrama**: Logo Etho + fundo etho-dark
- **Tempo**: 2 min

---

## Resumo do Storyboard

| Seção | Slides | Tempo | Conteúdo |
|---|---|---|---|
| A — Abertura | 1-6 | 8 min | Capa, objetivos, competências, agenda, motivação (5/5 vs 30%), contexto (por que AgentOps) |
| B — Por que difícil | 7-14 | 10 min | Não-determinismo, ambiente, custo, falácias, contínua vs pontual, vibes-eval, exercício |
| C — Observabilidade | 15-27 | 16 min | Traces, spans, OTel, tooling, logs vs traces, custo, dashboard, DEMO, exercício |
| D — Avaliação | 28-43 | 18 min | LLM-as-judge (vieses, mitigações), golden cases, regressão, métricas, CI, DEMO, exercício |
| E — Benchmarks | 44-54 | 14 min | SWE-bench, GAIA, τ-bench, AgentBench, WebArena, como rodar, limites, exercício |
| F — Melhoria & Report | 55-64 | 12 min | Dataset crescente, CI, shadow/canary, feedback, eval report, análise de falhas, exercício |
| G — Fechamento | 65-78 | 12 min | Boas práticas, anti-patterns, caso de estudo, resumo, quiz (5), conexão, projeto, referências, Q&A |
| **Total** | **78** | **90 min** | |

---

## Diagramas Necessários

| # | Slide | Diagrama | Tipo | Fonte |
|---|---|---|---|---|
| D1 | 5 | Teste manual vs produção (gráfico de barras) | Gráfico | Novo |
| D2 | 8 | Árvore de possibilidades (não-determinismo) | Árvore | Novo |
| D3 | 9 | Agente cercado por fontes mutáveis | Flowchart | Novo |
| D4 | 16 | Árvore de spans conceitual | Árvore | Novo |
| D5 | 17 | Anatomia de um trace (spans, atributos) | Flowchart | `12-Diagrams/ETHAGT12/trace-anatomy.mmd` |
| D6 | 18 | Span com atributos GenAI (OpenTelemetry) | Código | OpenTelemetry GenAI semconv |
| D7 | 19 | Comparação LangSmith vs Phoenix vs Langfuse vs OpenLLMetry | Tabela | Novo |
| D8 | 20 | Logs estruturados vs traces | Comparação | Novo |
| D9 | 21 | Funil de amostragem (head/tail) | Diagrama | Novo |
| D10 | 22 | Dashboard mínimo de observabilidade (6 painéis) | Mock | Novo |
| D11 | 23 | Latência P50/P95/P99 | Gráfico | Novo |
| D12 | 30 | Fluxo LLM-as-judge (output → judge → score) | Flowchart | Novo |
| D13 | 34 | Exemplo de golden case em código | Código | Novo |
| D14 | 39 | Pipeline de eval com CI | Flowchart | `12-Diagrams/ETHAGT12/eval-pipeline.mmd` |
| D15 | 46 | Landscape de benchmarks | Mind map | `12-Diagrams/ETHAGT12/benchmark-landscape.mmd` |
| D16 | 47 | Fluxo SWE-bench (issue → patch → testes) | Flowchart | Jimenez et al. |
| D17 | 49 | Arquitetura τ-bench (user simulator ↔ agent ↔ tools) | Flowchart | Yao et al. |
| D18 | 50 | Grid de ambientes AgentBench | Grid | Liu et al. |
| D19 | 58 | Shadow runs e canary (deploy progressivo) | Flowchart | Novo |
| D20 | 62 | Gráfico de pizza de categorias de falha | Gráfico | Novo |
| D21 | 68 | Ciclo de melhoria Anthropic SWE-bench | Ciclo | Novo |
| D22 | 76 | Mapa da especialização com ETHAGT12 | Mind map | Novo |

---

## Pontos de Engajamento

| # | Slide | Tipo | Interação | Tempo |
|---|---|---|---|---|
| E1 | 5 | Pergunta aberta | *Como você sabe se seu agente está ficando melhor ou pior?* | 1 min |
| E2 | 11 | Pergunta aberta | *Qual dessas falácias de avaliação você já cometeu?* | — |
| E3 | 14 | Exercício rápido | Votação: identificando falácias (4 afirmações) | 1 min |
| E4 | 24 | DEMO ao vivo | Traces Everywhere — adicionar observabilidade a um agente | 3 min |
| E5 | 25 | Discussão em duplas | *O que o trace revelou que logs não mostrariam?* | 2 min |
| E6 | 26 | Exercício em duplas | Lendo um trace: identificar loop e propor correções | 3 min |
| E7 | 27 | Pergunta provocativa | *Observabilidade é custo ou investimento?* | — |
| E8 | 31 | Pergunta conceitual | *Qual viés do LLM-as-judge é mais perigoso para seu caso?* | — |
| E9 | 40 | DEMO ao vivo | Eval automatizado — detectando regressão ao vivo | 3 min |
| E10 | 41 | Discussão aberta | *A regressão é real ou o judge está errado?* | 2 min |
| E11 | 42 | Exercício em duplas | Escrevendo golden cases com critério mensurável | 3 min |
| E12 | 43 | V/F | *LLM-as-judge é sempre confiável* | 1 min |
| E13 | 52 | Pergunta provocativa | *Score alto em benchmark garante produção?* | — |
| E14 | 54 | Discussão | *Benchmark vs produção — qual importa mais?* | 1 min |
| E15 | 63 | Pergunta aberta | *O que reportar para o CEO — accuracy ou custo?* | — |
| E16 | 64 | Exercício em grupos | Detectando regressão: análise de causas | 3 min |
| E17 | 71-75 | Quiz (5 perguntas) | Múltipla escolha com respostas | 5 min |

---

## Pendências de Produção

- [ ] Produzir 17 diagramas novos (D1, D2, D3, D4, D6, D7, D8, D9, D10, D11, D12, D13, D16, D17, D18, D19, D20, D21, D22)
- [ ] Screenshot de trace real no LangSmith/Phoenix (Slides 24, 26)
- [ ] Screenshot do código com syntax highlighting (Slides 24, 34, 40)
- [ ] Screenshot de eval report preenchido (Slide 61)
- [ ] Imagem de fundo para capa (Slide 1)
- [ ] Badge de competências (Slide 3)
- [ ] Timeline de marcos históricos (Slide 6)
- [ ] Preparar ambiente Docker Compose para DEMO de traces (Slide 24)
- [ ] Preparar conjunto de golden cases para DEMO de eval (Slide 40)
- [ ] Mock de dashboard de observabilidade (Slide 22)

---

> **Aguardando aprovação deste storyboard para gerar os slides detalhados com notas do professor.**
