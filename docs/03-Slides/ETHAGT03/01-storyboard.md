# ETHAGT03 — Padrões de Workflow Agêntico
## Storyboard da Apresentação

> **Universidade Etho · Especialização em Programação Agêntica**
> Fase A — Fundamentos Agênticos · 30 h
> Storyboard v1.0 · Julho 2026

---

## Metadados da Apresentação

| Campo | Valor |
|---|---|
| Código | ETHAGT03 |
| Título | Padrões de Workflow Agêntico (os 5 da Anthropic + composições) |
| Duração estimada | 90 min (2 blocos de 45 min) |
| Total de slides | 63 |
| Público | Arquitetos, Engenheiros de Software, Engenheiros de IA, Cientistas de Dados, Tech Leads |
| Pré-requisitos | ETHAGT01 (recomendado ETHAGT02) |
| Competências | C1 (I), C2 (B), C3 (B), C5 (B) |

---

## Mapa Visual da Apresentação

```
BLOCO 1 (45 min)                              BLOCO 2 (45 min)
┌──────────────────────────────┐              ┌──────────────────────────────┐
│ SEÇÃO A — Abertura (6 min)   │              │ SEÇÃO F — Orchestrator-      │
│  Capa · Objetivos · Agenda   │              │  Workers (10 min)            │
│  Motivação                   │              │  Subtarefas dinâmicas · Code │
├──────────────────────────────┤              ├──────────────────────────────┤
│ SEÇÃO B — Por Que Workflows  │              │ SEÇÃO G — Evaluator-Optimizer│
│  (7 min)                     │              │  (10 min)                    │
│  Princípio · 5 padrões       │              │  Loop · Critérios · Converg. │
├──────────────────────────────┤              ├──────────────────────────────┤
│ SEÇÃO C — Prompt Chaining    │              │ SEÇÃO H — Composições (8 min)│
│  (8 min)                     │              │  Composição · Limites        │
│  Estrutura · Gates · Code    │              │  Trade-offs                  │
├──────────────────────────────┤              ├──────────────────────────────┤
│ SEÇÃO D — Routing (9 min)    │              │ SEÇÃO I — Fechamento (17 min)│
│  Classificação · Modelos     │              │  Caso · Resumo · Quiz        │
│  Code · Exercício            │              │  Exercício · Projeto · Q&A   │
├──────────────────────────────┤              └──────────────────────────────┘
│ SEÇÃO E — Parallelization    │
│  (15 min)                    │
│  Sectioning · Voting · Code  │
└──────────────────────────────┘
```

---

## Storyboard Detalhado

### SEÇÃO A — Abertura (Slides 1-5 · 6 min)

---

#### Slide 1 — Capa
- **Tipo**: Capa
- **Objetivo**: Identificar a aula, professor e contexto
- **Conteúdo**:
  - ETHAGT03 — Padrões de Workflow Agêntico
  - Os 5 padrões canônicos da Anthropic + composições
  - Universidade Etho · Especialização em Programação Agêntica
  - Fase A — Fundamentos Agênticos
  - Professor · Data
- **Diagrama**: Logo Etho + imagem de fundo abstrata (fluxos/conexões)
- **Animação**: Fade in do título
- **Tempo**: 1 min

---

#### Slide 2 — Objetivos do Módulo
- **Tipo**: Conteúdo
- **Objetivo**: Deixar claro o que o aluno deve conseguir fazer ao final
- **Conteúdo**:
  - Objetivo geral: Dominar os 5 padrões canônicos de workflow e suas composições
  - 5 objetivos específicos:
    1. Implementar os 5 workflows (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer)
    2. Identificar gates programáticos e onde inseri-los
    3. Combinar workflows em pipelines complexos
    4. Justificar workflow vs agente autônomo em cenário real
    5. Medir trade-offs de custo/latência/qualidade
- **Diagrama**: Ícones representando cada objetivo
- **Animação**: Aparecer objetivos um a um (on click)
- **Tempo**: 2 min

---

#### Slide 3 — Competências Desenvolvidas
- **Tipo**: Conteúdo
- **Objetivo**: Conectar a aula ao Framework Etho de competências
- **Conteúdo**:
  - Tabela: 4 competências com nível B/I/A
  - C1 Programação Agêntica → I
  - C2 Multi-Agent Systems → B
  - C3 MCP & Tool Use → B
  - C5 AgentOps & Avaliação → B
  - Badge visual por competência
- **Diagrama**: Radar chart dos 4 pilares
- **Animação**: Radar aparece com wipe
- **Tempo**: 1 min

---

#### Slide 4 — Agenda
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar o roteiro da aula com tempos
- **Conteúdo**:
  - Bloco 1: Abertura → Por Que Workflows → Prompt Chaining → Routing → Parallelization
  - Bloco 2: Orchestrator-Workers → Evaluator-Optimizer → Composições → Fechamento
  - Tempos estimados por seção
- **Diagrama**: Timeline horizontal com 9 seções
- **Animação**: Timeline cresce da esquerda para direita
- **Tempo**: 1 min

---

#### Slide 5 — Motivação: Comece Simples
- **Tipo**: Conteúdo
- **Objetivo**: Criar tensão — times pulam para agente autônomo e colhem complexidade desnecessária
- **Conteúdo**:
  - Problema: time usa agente autônomo onde um `if` bastava
  - Exemplo: chatbot de suporte com 3 etapas fixas (classificar → buscar → responder) — agente livre é overkill
  - Princípio de Anthropic: comece simples, só aumente com evidência
  - Custo de complexidade prematura: debugging difícil, custo imprevisível, latência alta
  - Pergunta: *Quantos de vocês já viram um projeto que usou agente onde um if bastava?*
- **Diagrama**: Comparação visual "agente caótico" vs "workflow estruturado"
- **Animação**: Split — lado esquerdo (caos), depois lado direito (ordem)
- **Tempo**: 1 min

---

### SEÇÃO B — Por Que Workflows Antes de Agentes (Slides 6-10 · 7 min)

---

#### Slide 6 — [SEÇÃO] Por Que Workflows Antes de Agentes
- **Tipo**: Seção
- **Objetivo**: Transição para o bloco de fundamentos
- **Conteúdo**: Número "1" grande + "Por Que Workflows Antes de Agentes"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 7 — O Princípio de Anthropic: Comece Simples
- **Tipo**: Conteúdo
- **Objetivo**: Fixar o princípio norteador do módulo
- **Conteúdo**:
  - "Comece simples, só aumente complexidade com evidência" — Anthropic
  - Níveis de escalada:
    - Nível 0: Single LLM call + retrieval + examples
    - Nível 1: Workflow simples (prompt chaining)
    - Nível 2: Workflow complexo (orchestrator-workers)
    - Nível 3: Agente autônomo
    - Nível 4: Multi-agente
  - Regra: só suba um nível com evidência de que o anterior é insuficiente
- **Diagrama**: Pirâmide de níveis de complexidade
- **Animação**: Níveis aparecem de baixo para cima
- **Tempo**: 2 min

---

#### Slide 8 — Workflows vs Agentes (Recap de ETHAGT01)
- **Tipo**: Comparação
- **Objetivo**: Reativar o conhecimento de ETHAGT01 e preparar para os 5 padrões
- **Conteúdo**:
  - Workflows: LLMs e tools orquestrados via código predefinido → previsibilidade
  - Agentes: LLM direciona seu próprio processo e tool usage → flexibilidade
  - Workflows = controle do desenvolvedor; Agentes = controle do modelo
  - Este módulo: foco total em workflows (ETHAGT04 aprofunda agentes)
- **Diagrama**: `12-Diagrams/ETHAGT01/workflow-vs-agent.mmd` (referência)
- **Tempo**: 1.5 min

---

#### Slide 9 — Os 5 Workflows Canônicos (Panorama)
- **Tipo**: Diagrama
- **Objetivo**: Apresentar os 5 padrões que serão aprofundados na aula
- **Conteúdo**:
  1. Prompt Chaining — sequência de steps com gates
  2. Routing — classificação + dispatch
  3. Parallelization — sectioning / voting
  4. Orchestrator-Workers — delegação dinâmica
  5. Evaluator-Optimizer — loop de refinamento
  - Fonte: Anthropic, *Building Effective Agents* (2024)
- **Diagrama**: 5 mini-diagramas em grid 2x3 (com 1 célula vazia ou legenda)
- **Animação**: Cada workflow aparece com click
- **Tempo**: 2 min

---

#### Slide 10 — Mapa: Quando Cada Padrão Brilha
- **Tipo**: Comparação
- **Objetivo**: Dar um panorama rápido de quando usar cada padrão
- **Conteúdo**:
  - Prompt Chaining: tarefa linear com checkpoints de qualidade
  - Routing: categorias discretas com tratamento especializado
  - Parallelization: subtarefas independentes ou votação para robustez
  - Orchestrator-Workers: subtarefas dinâmicas não conhecidas a priori
  - Evaluator-Optimizer: feedback articulável e iterável melhora resultado
- **Diagrama**: Tabela 5×3 (padrão · quando usar · quando evitar)
- **Tempo**: 1 min

---

### SEÇÃO C — Prompt Chaining (Slides 11-16 · 8 min)

---

#### Slide 11 — [SEÇÃO] Prompt Chaining
- **Tipo**: Seção
- **Objetivo**: Transição para o primeiro padrão canônico
- **Conteúdo**: "2 — Prompt Chaining: Sequência com Gates"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 12 — Estrutura: LLM → Gate → LLM → …
- **Tipo**: Diagrama
- **Objetivo**: Apresentar a estrutura fundamental do prompt chaining
- **Conteúdo**:
  - Cadeia de chamadas LLM intercaladas com gates programáticos
  - Gate = código determinístico (não LLM) que decide se continua, roda de novo, ou para
  - Cada step tem prompt especializado e contexto focado
  - Saída de um step = entrada do próximo
- **Diagrama**: `12-Diagrams/ETHAGT03/prompt-chaining.mmd`
- **Animação**: Step a step, gates destacados em cor diferente
- **Tempo**: 2 min

---

#### Slide 13 — Onde Adicionar Gates
- **Tipo**: Conteúdo
- **Objetivo**: Ensinar a identificar pontos de gate na cadeia
- **Conteúdo**:
  - Validação estrutural: "a saída tem todos os campos obrigatórios?"
  - Classificação: "a resposta é do tipo esperado?"
  - Formatação: "está no formato JSON correto?"
  - Filtro de qualidade: "passou no check de segurança?"
  - Gates são código puro (if/else, regex, schema validation) — não LLM
  - Gate falhou? → retry com feedback, ou fallback, ou escalada
- **Diagrama**: Checklist de tipos de gate
- **Tempo**: 2 min

---

#### Slide 14 — Trade-off: Latência por Accuracy
- **Tipo**: Comparação
- **Objetivo**: Justificar quando o custo de latência serial vale a pena
- **Conteúdo**:
  - Latência = soma de todos os steps (serial)
  - Mas: cada step focado = melhor qualidade que uma chamada gigante
  - Gates reduzem retrabalho downstream (capturam erro cedo)
  - Quando vale: tarefas com critérios de qualidade verificáveis
  - Quando não vale: tarefas simples onde uma chamada basta
- **Diagrama**: Gráfico latência vs accuracy (curva de ganho marginal)
- **Tempo**: 1.5 min

---

#### Slide 15 — Exemplo + Código: Gerar → Revisar → Reescrever
- **Tipo**: Código
- **Objetivo**: Mostrar implementação concreta de prompt chaining
- **Conteúdo**:
  - Domínio: geração de resposta a ticket de suporte
  - Step 1: LLM gera rascunho
  - Gate 1: tem todos os campos? (schema validation)
  - Step 2: LLM revisa contra critérios
  - Gate 2: score ≥ threshold?
  - Step 3: LLM reescreve com feedback da revisão
  - Snippet em Python: função `chain()` com gates
- **Diagrama**: Code block + fluxo lado a lado
- **Animação**: Highlight de linhas chave (gates destacados)
- **Tempo**: 1.5 min

---

#### Slide 16 — Exercício: Gate Útil em Tradução
- **Tipo**: Exercício
- **Objetivo**: Praticar identificação de gates em outro domínio
- **Conteúdo**:
  - Cenário: prompt chaining para tradução técnica (EN → PT-BR)
  - Pergunta: *Descreva um gate programático útil entre o step de tradução e o step de revisão.*
  - Dica: pense em verificação estrutural, não semântica
  - Discussão em duplas (2 min)
- **Diagrama**: Caixa de discussão
- **Tempo**: 1.5 min

---

### SEÇÃO D — Routing (Slides 17-23 · 9 min)

---

#### Slide 17 — [SEÇÃO] Routing
- **Tipo**: Seção
- **Objetivo**: Transição para o segundo padrão canônico
- **Conteúdo**: "3 — Routing: Classificação e Dispatch"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 18 — Classificação como Etapa Separada
- **Tipo**: Conteúdo
- **Objetivo**: Explicar o principio fundamental do routing
- **Conteúdo**:
  - Router = LLM (ou código) que classifica a entrada em categorias
  - Cada categoria tem seu próprio tratamento especializado
  - Separação de concerns: classificar é mais barato que resolver
  - Router pode ser modelo menor (Haiku) — classify é tarefa simples
- **Diagrama**: Funil: input → router → N caminhos especializados
- **Tempo**: 1.5 min

---

#### Slide 19 — Routing por Modelo
- **Tipo**: Comparação
- **Objetivo**: Mostrar routing por capacidade/custo do modelo
- **Conteúdo**:
  - Haiku para tarefas fáceis (classificação, resumo simples) — barato e rápido
  - Sonnet para tarefas difíceis (raciocínio, código complexo) — caro mas capaz
  - Economia: 80% dos tickets são fáceis → Haiku → custo total cai
  - Risco: classificação errada envia tarefa difícil para modelo fraco
- **Diagrama**: `12-Diagrams/ETHAGT03/routing.mmd`
- **Animação**: Input entra no router, seta se divide em Haiku/Sonnet
- **Tempo**: 2 min

---

#### Slide 20 — Routing por Prompt/Tools Especializados
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar que routing não é só por modelo, mas por prompt e tools
- **Conteúdo**:
  - Mesmo modelo, diferentes system prompts especializados
  - Exemplo: ticket de billing → prompt com tools de fatura; ticket técnico → prompt com tools de docs
  - Vantagem: cada path tem contexto focado (menos tokens, melhor qualidade)
  - O router decide qual conjunto de tools/prompt carregar
- **Diagrama**: Router → 3 paths com diferentes toolsets
- **Tempo**: 1.5 min

---

#### Slide 21 — Avaliando a Qualidade do Classificador
- **Tipo**: Conteúdo
- **Objetivo**: Ensinar a medir se o router está funcionando
- **Conteúdo**:
  - O router é um classificador → métricas de classificação
  - Matriz de confusão: quais categorias confunde?
  - Precision/Recall por categoria
  - Erro mais caro: falso negativo (tarefa difícil → modelo fraco)
  - Estratégia: quando incerto, enviar para path robusto (Sonnet)
- **Diagrama**: Matriz de confusão 3×3 com exemplo
- **Tempo**: 1.5 min

---

#### Slide 22 — Código: Routing com Classifier
- **Tipo**: Código
- **Objetivo**: Mostrar implementação concreta de routing
- **Conteúdo**:
  - Função `route(input)` → classificação → dispatch
  - Router: LLM com output estruturado (JSON schema com categoria)
  - Switch/case para cada categoria → prompt + modelo + tools
  - Fallback: categoria "unknown" → path robusto
  - Snippet em Python
- **Diagrama**: Code block com fluxo
- **Tempo**: 1 min

---

#### Slide 23 — Exercício: O Que Medir no Router?
- **Tipo**: Exercício
- **Objetivo**: Engajar a turma com pergunta sobre avaliação do router
- **Conteúdo**:
  - "Como saber se o roteador está errando? O que medir?"
  - "Qual métrica é mais importante: precision ou recall? Depende do quê?"
  - "Se o router envia 10% dos fáceis para o path difícil, isso é problema?"
  - Discussão em duplas (2 min), 1 min compartilhar
- **Diagrama**: Caixa de discussão
- **Tempo**: 1.5 min

---

### SEÇÃO E — Parallelization (Slides 24-32 · 15 min)

---

#### Slide 24 — [SEÇÃO] Parallelization
- **Tipo**: Seção
- **Objetivo**: Transição para o terceiro padrão canônico
- **Conteúdo**: "4 — Parallelization: Sectioning e Voting"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 25 — Sectioning: Subtarefas Independentes em Paralelo
- **Tipo**: Diagrama
- **Objetivo**: Apresentar o padrão de dividir em subtarefas paralelas
- **Conteúdo**:
  - Tarefa dividida em N subtarefas independentes
  - Cada subtarefa roda em paralelo (chamadas LLM simultâneas)
  - Resultados são agregados por um reducer/sintetizador
  - Exemplo: revisar código → rodar linter + testes + typecheck em paralelo
  - Ganho: latência = max(subtasks) vs sum(subtasks)
- **Diagrama**: `12-Diagrams/ETHAGT03/parallelization.mmd` (lado sectioning)
- **Animação: Subtarefas disparam em paralelo, resultados convergem
- **Tempo**: 2 min

---

#### Slide 26 — Voting: Mesma Tarefa N Vezes
- **Tipo**: Diagrama
- **Objetivo**: Apresentar o padrão de votação para robustez
- **Conteúdo**:
  - Mesma tarefa executada N vezes (com temperatura/variação)
  - Agregação por maioria (classificação) ou seleção (geração)
  - Quando usar: classificação ambígua, geração de código crítico, decisões de segurança
  - Custo: N× o custo base — mas com N modelos menores pode ser mais barato que 1 grande
- **Diagrama**: `12-Diagrams/ETHAGT03/parallelization.mmd` (lado voting)
- **Tempo**: 2 min

---

#### Slide 27 — Guardrails em Paralelo
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar um padrão híbrido de parallelization para segurança
- **Conteúdo**:
  - Modelo A: gera a resposta principal
  - Modelo B (paralelo): filtra/modera a resposta
  - Se B sinaliza problema → bloqueia ou regenera
  - Latência quase zero adicionada (roda em paralelo)
  - Exemplo: resposta de suporte + verificação de PII em paralelo
- **Diagrama**: Duas lanes paralelas: gerar + filtrar
- **Tempo**: 2 min

---

#### Slide 28 — LLM-as-Judge em Paralelo
- **Tipo**: Conteúdo
- **Objetivo**: Conectar parallelization com avaliação (ponte para evaluator-optimizer)
- **Conteúdo**:
  - N julgamentos paralelos de uma saída (mesma tarefa de avaliação)
  - Votação reduz variância do juiz
  - Usado em pipelines de qualidade antes de entregar ao usuário
  - Cuidado: viés do juiz é sistemático (votação não resolve viés, só variância)
- **Diagrama**: Saída → N juízes em paralelo → agregação de scores
- **Tempo**: 1.5 min

---

#### Slide 29 — Erros Comuns: Dependências Ocultas, Custo Explodindo
- **Tipo**: Conteúdo
- **Objetivo**: Alertar sobre armadilhas típicas de parallelization
- **Conteúdo**:
  - Dependência oculta: "subtarefas independentes" que não são (ex.: step 2 precisa de output de step 1)
  - Custo explodindo: N=5 voting em pipeline de 10 steps = 50 chamadas
  - Reducer mal feito: síntese perde informação crítica
  - Timeout não tratado: uma subtarefa lenta atrasa todo o pipeline
  - Mitigação: medir custo/latência de cada subtarefa desde o início
- **Diagrama**: 4 ícones de "perigo" com labels
- **Tempo**: 2 min

---

#### Slide 30 — Código: Parallelization (Sectioning + Voting)
- **Tipo**: Código
- **Objetivo**: Mostrar implementação concreta de ambos os modos
- **Conteúdo**:
  - Sectioning: `asyncio.gather()` com N chamadas especializadas
  - Voting: `asyncio.gather()` com N chamadas idênticas (temp variada)
  - Reducer: função que agrega resultados
  - Snippet em Python com asyncio
  - Métricas: medir custo e latência de cada modo
- **Diagrama**: Code block com asyncio
- **Animação**: Highlight de gather() e reducer
- **Tempo**: 2 min

---

#### Slide 31 — DEMO: Latência = max vs sum
- **Tipo**: Código
- **Objetivo**: Demo ao vivo mostrando o ganho de latência do paralelismo
- **Conteúdo**:
  - Mesma tarefa: rodar 3 subtarefas
  - Versão serial: sum(3 chamadas) → ~9s
  - Versão paralela: max(3 chamadas) → ~3s
  - Mostrar timer no terminal
  - Mostrar custo: igual nos dois casos (mesmas chamadas)
  - Lição: paralelismo não reduz custo, reduz latência
- **Diagrama**: Terminal com timer lado a lado (serial vs paralelo)
- **Animação**: Barras de tempo crescendo em paralelo
- **Tempo**: 2 min

---

#### Slide 32 — Exercício: Voting vs Sectioning
- **Tipo**: Exercício
- **Objetivo**: Praticar a decisão entre os dois modos de parallelization
- **Conteúdo**:
  - Pergunta: *Quando voting é preferível a sectioning?*
  - 3 cenários rápidos — voting ou sectioning?
    1. Traduzir 3 páginas independentes
    2. Decidir se um email é phishing
    3. Gerar 3 alternativas de copy para anúncio
  - Votação rápida (mãos levantadas)
  - Respostas: 1=sectioning, 2=voting, 3=sectioning (mas usa voting para escolher a melhor)
- **Diagrama**: 3 cards com cenários
- **Tempo**: 1.5 min

---

### SEÇÃO F — Orchestrator-Workers (Slides 33-39 · 10 min)

---

#### Slide 33 — [SEÇÃO] Orchestrator-Workers
- **Tipo**: Seção
- **Objetivo**: Transição para o quarto padrão canônico
- **Conteúdo**: "5 — Orchestrator-Workers: Delegação Dinâmica"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 34 — Distinção Chave vs Parallelization: Subtarefas Dinâmicas
- **Tipo**: Comparação
- **Objetivo**: Fixar a diferença crítica entre parallelization e orchestrator-workers
- **Conteúdo**:
  - Parallelization: subtarefas são **conhecidas a priori** (fixas)
  - Orchestrator-Workers: subtarefas são **dinâmicas** (definidas pelo orquestrador em runtime)
  - O orquestrador é um LLM que olha a tarefa e decide QUEM chamar e COMO dividir
  - Sem orquestrador = parallelization; com orquestrador = orchestrator-workers
- **Diagrama**: Comparação lado a lado (parallelization fixa vs dinâmica)
- **Animação**: Setas mostrando a diferença
- **Tempo**: 2 min

---

#### Slide 35 — Orquestrador: Planejar + Sintetizar
- **Tipo**: Conteúdo
- **Objetivo**: Explicar o papel duplo do orquestrador
- **Conteúdo**:
  - Fase 1 — Planejar: LLM decompõe a tarefa em subtarefas
  - Fase 2 — Delegar: despacha cada subtarefa para um worker
  - Fase 3 — Sintetizar: agrega resultados dos workers em resposta final
  - O orquestrador NÃO executa subtarefas — ele coordena
  - Workers podem ser LLMs com prompts/tools especializados
- **Diagrama**: Ciclo: Planejar → Delegar → [Workers] → Sintetizar
- **Tempo**: 2 min

---

#### Slide 36 — Implementação: Task-Decomposition + Workers + Reducer
- **Tipo**: Diagrama
- **Objetivo**: Mostrar a arquitetura de implementação
- **Conteúdo**:
  - Componente 1: Decompositor (LLM com prompt de planejamento)
  - Componente 2: Workers (pool de LLMs com prompts especializados)
  - Componente 3: Reducer/Sintetizador (LLM que agrega)
  - Estado: lista de subtarefas + resultados parciais
  - Conexão com papers: Plan-and-Solve (arXiv:2305.17126), ReWOO (arXiv:2305.04091)
- **Diagrama**: `12-Diagrams/ETHAGT03/orchestrator-workers.mmd`
- **Animação**: Decompose → Workers disparam → Reducer agrega
- **Tempo**: 2 min

---

#### Slide 37 — Casos de Uso
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar cenários reais onde o padrão brilha
- **Conteúdo**:
  - Coding em múltiplos arquivos: orquestrador decide quais arquivos criar/modificar
  - Search em múltiplas fontes: orquestrador decide quais fontes consultar
  - Relatório multi-fonte: orquestrador divide por tópico, workers pesquisam, reducer sintetiza
  - Sinal de que este padrão é adequado: "não sei quantos steps vou precisar"
- **Diagrama**: 3 mini-casos em cards
- **Tempo**: 1.5 min

---

#### Slide 38 — Código: Orchestrator-Workers
- **Tipo**: Código
- **Objetivo**: Mostrar implementação concreta
- **Conteúdo**:
  - Função `orchestrate(task)`:
    1. LLM planeja → lista de subtarefas
    2. `asyncio.gather()` despacha para workers
    3. LLM sintetiza resultados
  - Snippet em Python
  - Diferença do código de parallelization: o step de planejamento
- **Diagrama**: Code block com 3 fases destacadas
- **Tempo**: 1.5 min

---

#### Slide 39 — Exercício: V/F "Orchestrator-Workers É Sempre Melhor"
- **Tipo**: Exercício
- **Objetivo**: Quebrar o mito de que padrões mais complexos são sempre melhores
- **Conteúdo**:
  - Verdadeiro ou Falso: "Orchestrator-workers é sempre melhor que parallelization."
  - Resposta: Falso
  - Por quê: se as subtarefas são fixas e conhecidas, parallelization é mais simples, barato e previsível
  - Orchestrator-workers adiciona custo (LLM de planejamento) e latência (step extra)
  - Regra: só use orchestrator-workers quando as subtarefas são genuinamente dinâmicas
- **Diagrama**: V/F com explicação
- **Tempo**: 1 min

---

### SEÇÃO G — Evaluator-Optimizer (Slides 40-46 · 10 min)

---

#### Slide 40 — [SEÇÃO] Evaluator-Optimizer
- **Tipo**: Seção
- **Objetivo**: Transição para o quinto padrão canônico
- **Conteúdo**: "6 — Evaluator-Optimizer: Loop de Refinamento"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 41 — O Loop: Gerar → Avaliar → Refinar
- **Tipo**: Diagrama
- **Objetivo**: Apresentar a estrutura fundamental do evaluator-optimizer
- **Conteúdo**:
  - Step 1: LLM gera saída (generator)
  - Step 2: LLM (ou código) avalia saída contra critérios (evaluator)
  - Step 3: Se abaixo do critério → LLM refina com feedback (optimizer)
  - Loop até critério de parada
  - Diferença de ReAct: aqui o loop é gerar-avaliar-refinar, não pensar-agir-observar
- **Diagrama**: `12-Diagrams/ETHAGT03/evaluator-optimizer.mmd`
- **Animação**: Loop animado (Gerar → Avaliar → Refinar → Gerar...)
- **Tempo**: 2 min

---

#### Slide 42 — Quando Tem Valor
- **Tipo**: Conteúdo
- **Objetivo**: Ensinar a identificar quando este padrão é adequado
- **Conteúdo**:
  - Condição 1: feedback é articulável (LLM consegue explicar o que está errado)
  - Condição 2: LLM consegue avaliar (existe critério objetivo ou near-objetivo)
  - Condição 3: iteração melhora resultado (nem sempre — às vezes o modelo trava)
  - Quando NÃO usar: se o evaluator não é melhor que o generator, o loop não converge
  - Exemplo que funciona: tradução literária (feedback sobre tom, ritmo, fidelidade)
  - Exemplo que não funciona: "seja mais criativo" (feedback não-articulável)
- **Diagrama**: Checklist de 3 condições
- **Tempo**: 2 min

---

#### Slide 43 — Critérios Claros e Mensuráveis
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar como estruturar critérios de avaliação
- **Conteúdo**:
  - Critério vago: "a resposta é boa" → não converge
  - Critério claro: "a resposta cita ≥3 fontes, tem ≤500 palavras, e inclui uma recomendação"
  - Rubric estruturada: dimensão → escala → descrição por nível
  - LLM-as-judge com rubric > LLM-as-judge sem rubric
  - Exemplo de rubric para tradução: fidelidade (1-5), fluência (1-5), terminologia (1-5)
- **Diagrama**: Tabela de rubric exemplo
- **Tempo**: 2 min

---

#### Slide 44 — Convergência: Parar por Score, Max Iters, ou Delta Estagnado
- **Tipo**: Conteúdo
- **Objetivo**: Ensinar a definir critérios de parada do loop
- **Conteúdo**:
  - Critério 1 — Score: parar quando score ≥ threshold (ex.: 4.5/5)
  - Critério 2 — Max iters: parar após N iterações (ex.: 5) — orçamento
  - Critério 3 — Delta estagnado: parar se score não melhora por 2 iterações consecutivas
  - Sempre usar ≥2 critérios (score OU max iters, no mínimo)
  - Custo: cada iteração = generator + evaluator = 2× chamadas
- **Diagrama**: Gráfico de convergência (score vs iteração) com 3 linhas de parada
- **Tempo**: 2 min

---

#### Slide 45 — Código: Evaluator-Optimizer
- **Tipo**: Código
- **Objetivo**: Mostrar implementação concreta do loop
- **Conteúdo**:
  - Função `evaluate_optimize(task, max_iters, threshold)`:
    1. Generator: LLM gera saída
    2. Evaluator: LLM avalia com rubric → score + feedback
    3. Condição de parada: score ≥ threshold OU iter ≥ max_iters OU delta < epsilon
    4. Optimizer: LLM refina com feedback
  - Snippet em Python
- **Diagrama**: Code block com loop destacado
- **Tempo**: 1 min

---

#### Slide 46 — Exercício: Condição de Parada para Tradução Literária
- **Tipo**: Exercício
- **Objetivo**: Praticar definição de critérios de parada em domínio real
- **Conteúdo**:
  - Cenário: evaluator-optimizer para tradução de um poema (EN → PT-BR)
  - Pergunta: *Escreva a condição de parada. Quais critérios? Qual threshold? Quantas iterações máximas?*
  - Dica: tradução literária é subjetiva — como evitar loop infinito?
  - Discussão em duplas (2 min), 1 min compartilhar
- **Diagrama**: Caixa de discussão
- **Tempo**: 1.5 min

---

### SEÇÃO H — Composições e Limites (Slides 47-51 · 8 min)

---

#### Slide 47 — [SEÇÃO] Composições e Limites
- **Tipo**: Seção
- **Objetivo**: Transição para composição de padrões
- **Conteúdo**: "7 — Composições e Limites"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 48 — Composição Típica: Routing → Parallelization → Evaluator-Optimizer
- **Tipo**: Diagrama
- **Objetivo**: Mostrar como os 5 padrões se combinam em pipelines reais
- **Conteúdo**:
  - Camada 1 — Routing: classifica a entrada (ex.: tipo de ticket)
  - Camada 2 — Parallelization: despacha subtarefas em paralelo (ex.: buscar FAQ + docs + histórico)
  - Camada 3 — Evaluator-Optimizer: avalia a resposta antes de entregar
  - Cada camada resolve um problema diferente
  - Outras composições: prompt chaining + evaluator-optimizer; routing + orchestrator-workers
- **Diagrama**: `12-Diagrams/ETHAGT03/composition-routing-parallel-evaluator.mmd`
- **Animação: Camadas surgem sequencialmente de cima para baixo
- **Tempo**: 2 min

---

#### Slide 49 — Quando Combinar Vira Agente
- **Tipo**: Conteúdo
- **Objetivo**: Discutir a fronteira tênue entre workflow composto e agente
- **Conteúdo**:
  - Workflow composto: camadas fixas, ordem predefinida, gates determinísticos
  - Agente: o próprio LLM decide a ordem, se itera, se busca mais informação
  - A linha é tênue: se o workflow tem routing + loops + branches condicionais suficientes...
  - Sinal de transição: quando o workflow precisa de um "meta-step" que decide qual caminho seguir dinamicamente
  - Isso é o que ETHAGT04 (Reasoning & Planning) aprofunda
- **Diagrama**: Espectro: workflow puro ←→ workflow composto ←→ agente
- **Tempo**: 2 min

---

#### Slide 50 — Sinais de Que Você Está Forçando Workflow
- **Tipo**: Conteúdo
- **Objetivo**: Dar checklist de quando o problema pede agente, não workflow
- **Conteúdo**:
  - Você está adicionando gates cada vez mais complexos para cobrir casos especiais
  - O número de branches no routing cresce sem parar
  - Você precisa de "loops dentro de loops" para cobrir edge cases
  - O evaluator precisa de contexto que o generator não teve acesso
  - Você descreve o workflow e ouve: "depende do que acontecer no step anterior"
- **Diagrama**: Checklist de "sinais de alerta" (etho-danger)
- **Tempo**: 2 min

---

#### Slide 51 — Trade-offs Consolidados
- **Tipo**: Comparação
- **Objetivo**: Sistematizar os trade-offs de todos os 5 padrões
- **Conteúdo**:
  - Tabela: 5 padrões × 4 eixos (previsibilidade, flexibilidade, custo, latência)
  - Prompt Chaining: previsibilidade alta, flexibilidade baixa, custo médio, latência alta (serial)
  - Routing: previsibilidade alta, flexibilidade média, custo baixo, latência baixa
  - Parallelization: previsibilidade alta, flexibilidade média, custo alto (N×), latência baixa (max)
  - Orchestrator-Workers: previsibilidade média, flexibilidade alta, custo alto, latência média
  - Evaluator-Optimizer: previsibilidade alta, flexibilidade média, custo alto (loop), latência alta
- **Diagrama**: Tabela 5×4 colorida por intensidade
- **Tempo**: 1.5 min

---

### SEÇÃO I — Fechamento (Slides 52-63 · 17 min)

---

#### Slide 52 — [SEÇÃO] Fechamento
- **Tipo**: Seção
- **Objetivo**: Transição para o fechamento
- **Conteúdo**: "8 — Fechamento"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 53 — Caso de Estudo: Coinbase / Intercom
- **Tipo**: Diagrama
- **Objetivo**: Mostrar os 5 padrões em um caso real de produção
- **Conteúdo**:
  - Coinbase / Intercom: workflows agênticos em suporte ao cliente
  - Arquitetura típica: routing (classificar ticket) → parallelization (buscar fontes) → evaluator-optimizer (validar resposta)
  - Resultados: redução de tempo de resposta, escalabilidade, custo controlado
  - Lição: workflow composto > agente autônomo para suporte (previsibilidade importa)
  - Referência: `09-CaseStudies/`
- **Diagrama**: Arquitetura do caso real
- **Tempo**: 3 min

---

#### Slide 54 — Resumo da Aula
- **Tipo**: Resumo
- **Objetivo**: Sintetizar os pontos-chave
- **Conteúdo**:
  - 5 padrões canônicos: prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer
  - Gates programáticos = controle determinístico em workflows
  - Parallelization: sectioning (independentes) vs voting (robustez)
  - Orchestrator-Workers: subtarefas dinâmicas (vs fixas em parallelization)
  - Evaluator-Optimizer: loop com critérios claros e convergência mensurável
  - Composição = realidade; mas quando workflow vira agente, mude de módulo
  - Comece simples, só aumente com evidência
- **Diagrama**: 7 ícones com os pontos-chave
- **Tempo**: 2 min

---

#### Slide 55 — Checklist da Aula
- **Tipo**: Resumo
- **Objetivo**: Confirmar que todos os tópicos foram cobertos
- **Conteúdo**:
  - [ ] Explicou o princípio "comece simples"
  - [ ] Detalhou os 5 padrões canônicos com diagramas
  - [ ] Mostrou código de cada padrão
  - [ ] Discutiu gates programáticos
  - [ ] Comparou parallelization vs orchestrator-workers
  - [ ] Apresentou critérios de convergência do evaluator-optimizer
  - [ ] Discutiu composições e quando workflow vira agente
- **Diagrama**: Checklist visual
- **Tempo**: 1 min

---

#### Slide 56 — Quiz: Pergunta 1
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "Qual é a diferença fundamental entre parallelization e orchestrator-workers?"
  - A) Orchestrator-workers é mais rápido
  - B) Parallelization usa modelos menores
  - C) Em orchestrator-workers, as subtarefas são dinâmicas (definidas em runtime)
  - D) Parallelization não tem reducer
  - Resposta: C
- **Tempo**: 1 min

---

#### Slide 57 — Quiz: Pergunta 2
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "O que é um gate em prompt chaining?"
  - A) Um modelo LLM que decide se continua
  - B) Um checkpoint programático (código) que valida a saída antes do próximo step
  - C) Um tipo de prompt especial
  - D) Um framework de orquestração
  - Resposta: B
- **Tempo**: 1 min

---

#### Slide 58 — Quiz: Pergunta 3
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "Quando o evaluator-optimizer NÃO vale a pena?"
  - A) Quando o feedback é articulável e o LLM consegue avaliar
  - B) Quando o evaluator não é melhor que o generator
  - C) Quando há orçamento para múltiplas iterações
  - D) Quando a tarefa tem critérios objetivos
  - Resposta: B
- **Tempo**: 1 min

---

#### Slide 59 — Quiz: Pergunta 4
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "Em routing por modelo, qual é o erro mais caro?"
  - A) Enviar tarefa fácil para modelo forte (Sonnet)
  - B) Enviar tarefa difícil para modelo fraco (Haiku)
  - C) Usar o mesmo modelo para todas as categorias
  - D) Ter apenas 2 categorias
  - Resposta: B
- **Tempo**: 1 min

---

#### Slide 60 — Exercício: Escolha o Workflow (5 Cenários)
- **Tipo**: Exercício
- **Objetivo**: Praticar a decisão de padrão em cenários reais
- **Conteúdo**:
  - 5 cenários:
    1. Tradução com revisão de qualidade → Prompt Chaining + Evaluator-Optimizer
    2. Análise de sentimentos de 10.000 tweets → Routing (por idioma) + Parallelization (sectioning)
    3. Geração de relatório com múltiplas fontes → Orchestrator-Workers
    4. Chatbot de FAQ simples → Routing
    5. Correção de redação com feedback → Evaluator-Optimizer
  - Em grupos: indicar workflow + justificar
  - 3 min discussão, 2 min compartilhar
- **Diagrama**: 5 cards com cenários
- **Tempo**: 3 min

---

#### Slide 61 — Projeto do Módulo + Labs
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar o projeto e laboratórios
- **Conteúdo**:
  - Projeto: síntese de relatório a partir de múltiplas fontes
    - Projetar e implementar workflow composto
    - Comparar 2 abordagens (ex.: prompt chaining vs orchestrator-workers)
    - Entrega: código + benchmark + ADR justificando escolha
    - Critério: ADR coerente; medições em ≥20 casos
  - Lab 1 (5h): "Os 5 em 1 dia" — versões mínimas dos 5 workflows em domínio comum
  - Lab 2 (5h): "Composição" — routing → parallelization (3 workers) → evaluator-optimizer
- **Tempo**: 2 min

---

#### Slide 62 — Conexão com Próximos Módulos + Referências
- **Tipo**: Referências
- **Objetivo**: Mostrar conexões e indicar leitura
- **Conteúdo**:
  - ETHAGT04 — Reasoning & Planning: quando workflow não basta, entra raciocínio avançado
  - ETHAGT09 — Multi-Agente: workflows como fundação de orquestração multi-agente
  - ETHAGT10 — Orquestração: composições em escala
  - Leitura obrigatória: Anthropic, *Building Effective Agents* (2024)
  - Papers: arXiv:2305.17126 (Plan-and-Solve), arXiv:2305.04091 (ReWOO), arXiv:2310.01757 (LLMCompiler)
  - Vídeo: Schluntz & Albert, *Building more effective AI agents* (YouTube)
- **Diagrama**: Mapa da especialização com ETHAGT03 destacado
- **Tempo**: 1.5 min

---

#### Slide 63 — Q&A / Encerramento
- **Tipo**: Capa
- **Objetivo**: Abrir para perguntas e encerrar
- **Conteúdo**:
  - "Perguntas?"
  - Contato do professor
  - "Na próxima aula: ETHAGT04 — Reasoning & Planning"
- **Diagrama**: Logo Etho + fundo etho-dark
- **Tempo**: 2 min

---

## Resumo do Storyboard

| Seção | Slides | Tempo | Conteúdo |
|---|---|---|---|
| A — Abertura | 1-5 | 6 min | Capa, objetivos, competências, agenda, motivação |
| B — Por Que Workflows | 6-10 | 7 min | Princípio de Anthropic, workflows vs agentes, 5 padrões, quando usar |
| C — Prompt Chaining | 11-16 | 8 min | Estrutura, gates, trade-off latência/accuracy, código, exercício |
| D — Routing | 17-23 | 9 min | Classificação, routing por modelo/prompt/tools, avaliação, código, exercício |
| E — Parallelization | 24-32 | 15 min | Sectioning, voting, guardrails, erros comuns, código, DEMO, exercício |
| F — Orchestrator-Workers | 33-39 | 10 min | Distinção vs parallelization, implementação, casos, código, exercício |
| G — Evaluator-Optimizer | 40-46 | 10 min | Loop, quando tem valor, critérios, convergência, código, exercício |
| H — Composições e Limites | 47-51 | 8 min | Composição típica, quando vira agente, sinais de alerta, trade-offs |
| I — Fechamento | 52-63 | 17 min | Caso de estudo, resumo, checklist, quiz, exercício, projeto, labs, referências, Q&A |
| **Total** | **63** | **90 min** | |

---

## Diagramas Necessários

| # | Slide | Diagrama | Tipo | Fonte | Status |
|---|---|---|---|---|---|
| D1 | 7 | Pirâmide de níveis de complexidade | Pirâmide | Novo | A produzir |
| D2 | 8 | Workflow vs Agente (recap) | Fluxograma | `12-Diagrams/ETHAGT01/workflow-vs-agent.mmd` | Pronto |
| D3 | 9 | 5 workflows canônicos (grid) | Grid 2x3 | Anthropic | A produzir |
| D4 | 10 | Tabela "quando cada padrão brilha" | Tabela 5×3 | Novo | A produzir |
| D5 | 12 | Prompt Chaining | Flowchart | `12-Diagrams/ETHAGT03/prompt-chaining.mmd` | Pronto |
| D6 | 13 | Checklist de tipos de gate | Checklist | Novo | A produzir |
| D7 | 14 | Gráfico latência vs accuracy | Gráfico | Novo | A produzir |
| D8 | 18 | Funil de routing | Funil | Novo | A produzir |
| D9 | 19 | Routing | Flowchart | `12-Diagrams/ETHAGT03/routing.mmd` | Pronto |
| D10 | 20 | Router com diferentes toolsets | Flowchart | Novo | A produzir |
| D11 | 21 | Matriz de confusão 3×3 | Matriz | Novo | A produzir |
| D12 | 25 | Parallelization — Sectioning | Flowchart | `12-Diagrams/ETHAGT03/parallelization.mmd` | Pronto |
| D13 | 26 | Parallelization — Voting | Flowchart | `12-Diagrams/ETHAGT03/parallelization.mmd` | Pronto |
| D14 | 27 | Guardrails em paralelo (2 lanes) | Comparação | Novo | A produzir |
| D15 | 28 | LLM-as-Judge em paralelo | Flowchart | Novo | A produzir |
| D16 | 29 | Erros comuns (4 ícones) | Ícones | Novo | A produzir |
| D17 | 34 | Parallelization fixa vs dinâmica | Comparação | Novo | A produzir |
| D18 | 35 | Ciclo Planejar → Delegar → Sintetizar | Ciclo | Novo | A produzir |
| D19 | 36 | Orchestrator-Workers | Flowchart | `12-Diagrams/ETHAGT03/orchestrator-workers.mmd` | Pronto |
| D20 | 37 | 3 casos de uso em cards | Cards | Novo | A produzir |
| D21 | 41 | Evaluator-Optimizer | Flowchart | `12-Diagrams/ETHAGT03/evaluator-optimizer.mmd` | Pronto |
| D22 | 42 | Checklist de 3 condições | Checklist | Novo | A produzir |
| D23 | 43 | Rubric de tradução (tabela) | Tabela | Novo | A produzir |
| D24 | 44 | Gráfico de convergência | Gráfico | Novo | A produzir |
| D25 | 48 | Composição routing → parallel → evaluator | Flowchart | `12-Diagrams/ETHAGT03/composition-routing-parallel-evaluator.mmd` | Pronto |
| D26 | 49 | Espectro workflow ↔ agente | Espectro | Novo | A produzir |
| D27 | 50 | Sinais de alerta (checklist danger) | Checklist | Novo | A produzir |
| D28 | 51 | Trade-offs consolidados (tabela 5×4) | Tabela | Novo | A produzir |
| D29 | 53 | Arquitetura caso Coinbase/Intercom | Flowchart | `09-CaseStudies/` | A produzir |
| D30 | 62 | Mapa da especialização | Mind map | Novo | A produzir |

---

## Pontos de Engajamento

| Slide | Tipo | Interação |
|---|---|---|
| 5 | Pergunta | "Quantos já viram projeto que usou agente onde um if bastava?" — votação por mão levantada |
| 16 | Exercício | Descrever gate programático útil em tradução — discussão em duplas (2 min) |
| 23 | Exercício | "Como saber se o roteador está errando? O que medir?" — discussão em duplas (2 min) |
| 31 | DEMO | Latência = max vs sum ao vivo com timer no terminal |
| 32 | Exercício | Voting vs sectioning em 3 cenários — votação rápida por mão levantada |
| 39 | Exercício | V/F "Orchestrator-workers é sempre melhor" — votação + explicação |
| 46 | Exercício | Condição de parada para tradução literária — discussão em duplas (2 min) |
| 49 | Discussão | "O que diferencia um workflow composto de um agente?" — debate aberto |
| 56-59 | Quiz | 4 perguntas de múltipla escolha — votação individual |
| 60 | Exercício | 5 cenários: indicar workflow + justificar — grupos (3 min discussão, 2 min compartilhar) |
| 63 | Q&A | Perguntas abertas da turma |

---

## Pendências de Produção

- [ ] Produzir 23 diagramas novos (D1, D3, D4, D6, D7, D8, D10, D11, D14, D15, D16, D17, D18, D20, D22, D23, D24, D26, D27, D28, D29, D30 + D2 reutilizado de ETHAGT01)
- [ ] Screenshot do código com syntax highlighting (Slides 15, 22, 30, 38, 45)
- [ ] Screenshot do DEMO de latência serial vs paralelo (Slide 31)
- [ ] Imagem de fundo para capa (Slide 1)
- [ ] Badge de competências (Slide 3)
- [ ] Tabela de trade-offs consolidados colorida por intensidade (Slide 51)
- [ ] Material do caso de estudo Coinbase/Intercom (Slide 53)
- [ ] Cards impressos dos 5 cenários do exercício final (Slide 60)

---

> **Aguardando aprovação deste storyboard para gerar os slides detalhados com notas do professor.**
