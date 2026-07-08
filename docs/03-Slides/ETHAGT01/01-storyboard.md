# ETHAGT01 — Arquitetura Cognitiva de Agentes LLM
## Storyboard da Apresentação

> **Universidade Etho · Especialização em Programação Agêntica**
> Fase A — Fundamentos Agênticos · 25 h
> Storyboard v1.0 · Julho 2026

---

## Metadados da Apresentação

| Campo | Valor |
|---|---|
| Código | ETHAGT01 |
| Título | Arquitetura Cognitiva de Agentes LLM |
| Duração estimada | 90 min (2 blocos de 45 min) |
| Total de slides | 62 |
| Público | Arquitetos, Engenheiros de Software, Engenheiros de IA, Cientistas de Dados, Tech Leads |
| Pré-requisitos | ETHDEV07, ETHML01, Python Intermediário |
| Competências | C1 (I), C3 (B), C4 (B), C5 (B) |

---

## Mapa Visual da Apresentação

```
BLOCO 1 (45 min)                              BLOCO 2 (45 min)
┌──────────────────────────────┐              ┌──────────────────────────────┐
│ SEÇÃO A — Abertura (8 min)   │              │ SEÇÃO D — Frameworks (15 min)│
│  Capa · Objetivos · Agenda   │              │  Python puro vs LangGraph vs │
│  Motivação · Contexto        │              │  OpenAI SDK · Comparação     │
├──────────────────────────────┤              ├──────────────────────────────┤
│ SEÇÃO B — Fundamentos (22 min)│             │ SEÇÃO E — Observabilidade (8m)│
│  Do LLM ao Agente            │              │  Traces · Logs · Custo       │
│  Augmented LLM               │              ├──────────────────────────────┤
│  Agent Loop (ReAct)          │              │ SEÇÃO F — Fechamento (12 min)│
│  DEMO: ReAct em 50 linhas    │              │  Boas práticas · Anti-patterns│
├──────────────────────────────┤              │  Exercício · Resumo          │
│ SEÇÃO C — Workflows (10 min) │              │  Quiz · Referências · Next   │
│  Workflows vs Agentes        │              │  Q&A                         │
│  5 padrões canônicos         │              └──────────────────────────────┘
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
  - ETHAGT01 — Arquitetura Cognitiva de Agentes LLM
  - Universidade Etho · Especialização em Programação Agêntica
  - Fase A — Fundamentos Agênticos
  - Professor · Data
- **Diagrama**: Logo Etho + imagem de fundo abstrata (circuitos/neural)
- **Animação**: Fade in do título
- **Tempo**: 1 min

---

#### Slide 2 — Objetivos do Módulo
- **Tipo**: Conteúdo
- **Objetivo**: Deixar claro o que o aluno deve conseguir fazer ao final
- **Conteúdo**:
  - Objetivo geral: Estabelecer o bloco fundamental — Augmented LLM em loop
  - 6 objetivos específicos (1 linha cada)
  - Diferença workflow vs agente
  - Raciocinar sobre arquitetura antes de framework
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
  - C3 MCP & Tool Use → B
  - C4 Agent Memory → B
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
  - Bloco 1: Abertura → Fundamentos → Workflows
  - Bloco 2: Frameworks → Observabilidade → Fechamento
  - Tempos estimados por seção
- **Diagrama**: Timeline horizontal com 6 seções
- **Animação**: Timeline cresce da esquerda para direita
- **Tempo**: 1 min

---

#### Slide 5 — Motivação: O Problema do Oráculo
- **Tipo**: Conteúdo
- **Objetivo**: Criar tensão — LLM puro falha em tarefas multi-step
- **Conteúdo**:
  - "LLM como oráculo": responde uma vez e acabou
  - Exemplo: "Reserve voo + hotel + carro para a conferência"
  - LLM puro: não pode agir, não pode verificar, não pode iterar
  - Pergunta: *Quantos já tentaram tarefa multi-step com ChatGPT e fracassaram?*
- **Diagrama**: Imagem de "oráculo" (mão de bola de cristal) → vs → fluxo multi-step
- **Animação**: Split — lado esquerdo (oráculo), depois lado direito (loop)
- **Tempo**: 2 min

---

#### Slide 6 — Contexto: Por Que Agora
- **Tipo**: Conteúdo
- **Objetivo**: Explicar a confluência histórica que tornou agentes viáveis
- **Conteúdo**:
  - Linha do tempo: 2020 (GPT-3) → 2022 (CoT) → 2023 (tool calling) → 2024 (agent frameworks)
  - Confluência: reasoning + tools + context window + cost reduction
  - Anthropic "Building Effective Agents" (dez/2024) como marco
  - arXiv:2601.12560 — survey de arquiteturas
- **Diagrama**: Timeline horizontal com marcos
- **Animação**: Marcos aparecem sequencialmente
- **Tempo**: 1 min

---

### SEÇÃO B — Fundamentos (Slides 7-22 · 22 min)

---

#### Slide 7 — [SEÇÃO] Do LLM ao Agente
- **Tipo**: Seção
- **Objetivo**: Transição para o bloco de fundamentos
- **Conteúdo**: Número "1" grande + "Do LLM ao Agente"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 8 — Definições: O Que É um Agente?
- **Tipo**: Comparação
- **Objetivo**: Mostrar que "agente" tem definições concorrentes
- **Conteúdo**:
  - Coluna 1: Definição ampla (autônomo, longo prazo, multi-tool)
  - Coluna 2: Definição restritiva (segue workflow predefinido)
  - Coluna 3: Recuo pragmático de Anthropic: "agentic systems" = workflows + agentes
  - Pergunta: *Qual definição sua equipe usa?*
- **Diagrama**: 3 colunas comparativas
- **Animação**: Colunas aparecem uma a uma
- **Tempo**: 2 min

---

#### Slide 9 — Taxonomia Unificada
- **Tipo**: Diagrama
- **Objetivo**: Apresentar a decomposição canônica de um agente
- **Conteúdo**:
  - 6 componentes: Perception · Brain · Planning · Action · Tool Use · Collaboration
  - Fonte: arXiv:2601.12560
  - Cada componente com 1 linha de descrição
- **Diagrama**: Hexágono com 6 componentes (mind map radial)
- **Animação**: Componentes aparecem um a um no hexágono
- **Tempo**: 3 min

---

#### Slide 10 — Transição: Geração Única → Controle Cognitivo
- **Tipo**: Comparação
- **Objetivo**: Mostrar a mudança de paradigma
- **Conteúdo**:
  - Antes: prompt → response (1 step)
  - Agora: prompt → plan → act → observe → adapt → ... → response (N steps)
  - Implicações: estado, memória, custo, latência, erro
- **Diagrama**: Comparação visual "1-step" vs "N-step loop"
- **Animação**: Setas mostrando a transição
- **Tempo**: 2 min

---

#### Slide 11 — [SEÇÃO] O Augmented LLM
- **Tipo**: Seção
- **Objetivo**: Transição para o bloco fundamental
- **Conteúdo**: "2 — O Augmented LLM: O Bloco Fundamental"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 12 — O Bloco Fundamental
- **Tipo**: Diagrama
- **Objetivo**: Apresentar o Augmented LLM como bloco base de tudo
- **Conteúdo**:
  - LLM + retrieval + tools + memory
  - O modelo gera suas próprias queries
  - O modelo escolhe e chama tools
  - O modelo decide o que reter
- **Diagrama**: `12-Diagrams/ETHAGT01/augmented-llm.mmd`
- **Animação**: Componentes surgem do centro (LLM) para fora
- **Tempo**: 3 min

---

#### Slide 13 — Retrieval In-Loop
- **Tipo**: Conteúdo
- **Objetivo**: Explicar que retrieval não é pipeline externo — é decisão do modelo
- **Conteúdo**:
  - RAG tradicional: query → retrieve → generate (fixo)
  - RAG agêntico: modelo decide SE e QUANDO recuperar
  - O modelo gera suas próprias search queries
  - Profundamento em ETHAGT06
- **Diagrama**: Comparação RAG fixo vs RAG agêntico
- **Animação**: Setas mostrando decisão do modelo
- **Tempo**: 2 min

---

#### Slide 14 — Tools como Extensão de Ação
- **Tipo**: Conteúdo
- **Objetivo**: Introduzir tool calling estruturado
- **Conteúdo**:
  - Tools = capacidades que o modelo não tem (API, DB, execução, busca)
  - Tool calling estruturado: JSON schema → função → resultado
  - Exemplo: calculator tool (snippet de código)
  - Aprofundamento em ETHAGT02 (ACI)
- **Diagrama**: Fluxo: LLM → tool_call JSON → execução → observation → LLM
- **Animação**: Fluxo step-by-step
- **Tempo**: 2 min

---

#### Slide 15 — Memory: Working vs Persistente
- **Tipo**: Comparação
- **Objetivo**: Panorama de memória (não aprofundar — ETHAGT05)
- **Conteúdo**:
  - Working memory = context window (efêmera, limitada)
  - Persistent memory = checkpointer (Postgres, Redis)
  - Tensão: mais memória = mais contexto = mais custo
  - Profundamento em ETHAGT05
- **Diagrama**: Duas caixas: "Context Window" (curto prazo) vs "Checkpointer" (longo prazo)
- **Tempo**: 2 min

---

#### Slide 16 — A Regra de Ouro: Interface Bem Documentada
- **Tipo**: Citação
- **Objetivo**: Fixar o princípio de ACI desde o início
- **Conteúdo**:
  - "Invista tanto esforço em ACI quanto em HCI" — Anthropic
  - Tool bem documentada > prompt melhor
  - Exemplo: path absoluto vs relativo (caso SWE-bench)
- **Diagrama**: Ícone de "regra de ouro"
- **Tempo**: 1 min

---

#### Slide 17 — [SEÇÃO] O Agent Loop: ReAct
- **Tipo**: Seção
- **Objetivo**: Transição para o padrão fundacional
- **Conteúdo**: "3 — O Agent Loop: ReAct"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 18 — ReAct: Thought → Action → Observation
- **Tipo**: Diagrama
- **Objetivo**: Apresentar o padrão fundacional de agentes
- **Conteúdo**:
  - Padrão: Thought → Action → Observation em loop
  - Fonte: Yao et al., ICLR 2023 (arXiv:2210.03629)
  - Por que funciona: força-grounding via observação do ambiente
  - max_steps como guardrail
- **Diagrama**: `12-Diagrams/ETHAGT01/agent-loop.mmd`
- **Animação**: Loop animado (Thought → Action → Observation → Thought)
- **Tempo**: 3 min

---

#### Slide 19 — Trace Real de um Agente ReAct
- **Tipo**: Código
- **Objetivo**: Mostrar a saída real de um agente em execução
- **Conteúdo**:
  - Console output com cores:
    - Thought: "Preciso saber a previsão do tempo no RJ"
    - Action: search("previsão tempo Rio de Janeiro")
    - Observation: "25°C, possibilidade de chuva"
    - Thought: "Agora posso responder"
    - Answer: "Leve guarda-chuva..."
- **Diagrama**: Print de console estilizado
- **Animação**: Linhas aparecem sequencialmente (simulando execução)
- **Tempo**: 2 min

---

#### Slide 20 — Limitações do ReAct
- **Tipo**: Conteúdo
- **Objetivo**: Ser honesto sobre os trade-offs
- **Conteúdo**:
  - Loops infinitos (sem max_steps)
  - Custo cumulativo (cada iteração = tokens)
  - Alucinação em ação (modelo chama tool inexistente)
  - Latência (múltiplas chamadas serial)
  - Erro composto (falha em step N propaga)
- **Diagrama**: 5 ícones de "perigo" com labels
- **Tempo**: 2 min

---

#### Slide 21 — DEMO: ReAct em 50 Linhas
- **Tipo**: Código
- **Objetivo**: Demo ao vivo — implementação mínima em Python puro
- **Conteúdo**:
  - Código do `19-Examples/ETHAGT01/exemplo-01-react-loop/main.py`
  - Tool: calculator
  - Loop principal: while not done → thought → action → observation
  - Mostrar trace no terminal
- **Diagrama**: Code block + terminal side-by-side
- **Animação**: Highlight de linhas chave
- **Tempo**: 5 min

---

#### Slide 22 — Pergunta da DEMO
- **Tipo**: Exercício
- **Objetivo**: Engajar a turma com uma pergunta sobre a demo
- **Conteúdo**:
  - "O que acontece se a tool retornar erro? Quem trata?"
  - "E se o modelo não chamar tool nenhuma?"
  - Discussão em duplas (2 min)
- **Diagrama**: Caixa de discussão
- **Tempo**: 2 min

---

### SEÇÃO C — Workflows vs Agentes (Slides 23-28 · 10 min)

---

#### Slide 23 — [SEÇÃO] Workflows vs Agentes
- **Tipo**: Seção
- **Objetivo**: Transição para a decisão arquitetural
- **Conteúdo**: "4 — Workflows vs Agentes"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 24 — A Distinção Canônica
- **Tipo**: Comparação
- **Objetivo**: Apresentar a distinção de Anthropic
- **Conteúdo**:
  - Workflows: LLMs e tools orquestrados via código predefinido → previsibilidade
  - Agentes: LLM direciona seu próprio processo e tool usage → flexibilidade
  - Fonte: Anthropic, Building Effective Agents (2024)
- **Diagrama**: `12-Diagrams/ETHAGT01/workflow-vs-agent.mmd`
- **Tempo**: 2 min

---

#### Slide 25 — Os 5 Workflows Canônicos (Panorama)
- **Tipo**: Diagrama
- **Objetivo**: Visão geral dos 5 padrões (aprofundamento em ETHAGT03)
- **Conteúdo**:
  1. Prompt Chaining — sequência de steps
  2. Routing — classificação + dispatch
  3. Parallelization — sectioning / voting
  4. Orchestrator-Workers — delegação dinâmica
  5. Evaluator-Optimizer — loop de refinamento
- **Diagrama**: 5 mini-diagramas em grid 2x3
- **Animação**: Cada workflow aparece com click
- **Tempo**: 3 min

---

#### Slide 26 — Árvore de Decisão: Workflow ou Agente?
- **Tipo**: Diagrama
- **Objetivo**: Dar um critério prático de decisão
- **Conteúdo**:
  - Consigo listar os passos? → Workflow
  - Nº de passos é imprevisível? → Agente
  - Posso confiar no modelo sem HITL? → Agente
  - Preciso de HITL forte? → Agente + checkpoints
- **Diagrama**: Fluxograma de decisão
- **Tempo**: 2 min

---

#### Slide 27 — A Escalada de Complexidade
- **Tipo**: Conteúdo
- **Objetivo**: Fixar o princípio "comece simples"
- **Conteúdo**:
  - Nível 0: Single LLM call + retrieval + examples
  - Nível 1: Workflow (prompt chaining)
  - Nível 2: Workflow complexo (orchestrator-workers)
  - Nível 3: Agente autônomo
  - Nível 4: Multi-agente
  - Regra: só suba com evidência de que o nível anterior é insuficiente
- **Diagrama**: Pirâmide de níveis
- **Animação**: Níveis aparecem de baixo para cima
- **Tempo**: 2 min

---

#### Slide 28 — Exercício Rápido: Workflow ou Agente?
- **Tipo**: Exercício
- **Objetivo**: Praticar a decisão em cenários reais
- **Conteúdo**:
  - 6 cenários curtos:
    1. "Traduzir documentação técnica" → Workflow (chaining)
    2. "Resolver issue de GitHub" → Agente
    3. "Classificar ticket de suporte" → Workflow (routing)
    4. "Pesquisar e sintetizar tema novo" → Agente
    5. "Revisar código em busca de bugs" → Workflow (parallelization)
    6. "Negociar contrato" → Agente + HITL
  - Votação rápida (maos levantadas)
- **Diagrama**: 6 cards com cenários
- **Tempo**: 2 min

---

### SEÇÃO D — Implementação: Frameworks (Slides 29-38 · 15 min)

---

#### Slide 29 — [SEÇÃO] Implementação: Do Zero vs Framework
- **Tipo**: Seção
- **Objetivo**: Transição para comparação de implementação
- **Conteúdo**: "5 — Implementação: Do Zero vs Framework"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 30 — Três Implementações do Mesmo Agente
- **Tipo**: Comparação
- **Objetivo**: Mostrar que o mesmo agente pode ser implementado de 3 formas
- **Conteúdo**:
  - Versão 1: Python puro + OpenAI SDK (~50 linhas)
  - Versão 2: LangGraph (~20 linhas)
  - Versão 3: OpenAI Agents SDK (~15 linhas)
  - Menos código ≠ melhor — depende do controle que você precisa
- **Diagrama**: 3 colunas com contagem de linhas
- **Tempo**: 2 min

---

#### Slide 31 — Python Puro: O Que Você Controla
- **Tipo**: Código
- **Objetivo**: Mostrar as vantagens do Python puro
- **Conteúdo**:
  - Controle total do prompt efetivo
  - Loop transparente (você vê cada step)
  - Estado explícito (você serializa)
  - Tools validadas por você
  - Snippet de código: o loop principal
- **Diagrama**: `12-Diagrams/ETHAGT01/framework-comparison.mmd` (lado esquerdo)
- **Tempo**: 3 min

---

#### Slide 32 — LangGraph: O Que Ele Abstrai
- **Tipo**: Código
- **Objetivo**: Mostrar o que o framework oferece
- **Conteúdo**:
  - StateGraph + nodes + edges
  - Checkpointer embutido
  - Tool wrapping automático
  - Snippet: create_react_agent(model, tools)
  - Mas: prompt efetivo é oculto, estado é opaco
- **Diagrama**: `12-Diagrams/ETHAGT01/framework-comparison.mmd` (lado direito)
- **Tempo**: 3 min

---

#### Slide 33 — OpenAI Agents SDK: A Camada Mais Alta
- **Tipo**: Código
- **Objetivo**: Mostrar a abstração mais alta
- **Conteúdo**:
  - Agent(model, tools, instructions) → run()
  - Mínimo código, máxima produtividade
  - Mas: menos controle, mais "caixa preta"
  - Snippet de código
- **Tempo**: 2 min

---

#### Slide 34 — Comparação Estrutural
- **Tipo**: Comparação
- **Objetivo**: Sistematizar os trade-offs
- **Conteúdo**:
  - Tabela: Python puro vs LangGraph vs OpenAI SDK
  - Eixos: controle do prompt, transparência do loop, estado, tools, curva de aprendizado, linhas de código, produção-ready
- **Diagrama**: Tabela comparativa colorida
- **Tempo**: 2 min

---

#### Slide 35 — Quando Reduzir Camadas de Abstração
- **Tipo**: Conteúdo
- **Objetivo**: Critério para decidir quando sair do framework
- **Conteúdo**:
  - Em produção: framework pode esconder bugs
  - Sinais de que você precisa reduzir:
    - "Não entendo por que o agente fez X"
    - Prompt efetivo é diferente do que você escreveu
    - Custo inesperado
    - Latência inexplicável
  - Regra: entenda o que está sob o hood
- **Diagrama**: Checklist de "sinais de alerta"
- **Tempo**: 2 min

---

#### Slide 36 — Pergunta: Framework ou Não?
- **Tipo**: Exercício
- **Objetivo**: Discussão sobre escolha de framework
- **Conteúdo**:
  - "Qual framework dá mais controle? E mais produtividade?"
  - "Em que cenário você NÃO usaria framework?"
  - Discussão aberta (3 min)
- **Tempo**: 3 min

---

### SEÇÃO E — Observabilidade (Slides 37-42 · 8 min)

---

#### Slide 37 — [SEÇÃO] Observabilidade Desde o Dia 1
- **Tipo**: Seção
- **Objetivo**: Transição para observabilidade
- **Conteúdo**: "6 — Observabilidade Desde o Dia 1"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 38 — Por Que Observabilidade desde o Início?
- **Tipo**: Conteúdo
- **Objetivo**: Justificar por que traces não são "nice to have"
- **Conteúdo**:
  - Sem traces: melhoria é adivinhação
  - Com traces: você vê o pensamento do agente
  - Em produção: debugging sem traces = impossível
  - Analogia: "logar é como ligar as luzes antes de procurar algo no escuro"
- **Diagrama**: Antes (escuro) vs Depois (iluminado)
- **Tempo**: 2 min

---

#### Slide 39 — Logging Estruturado
- **Tipo**: Código
- **Objetivo**: Mostrar o padrão mínimo de logging
- **Conteúdo**:
  - JSON estruturado: timestamp, step, thought, action, observation, cost, latency
  - Snippet de código: log_step()
  - Print → structured logs → LangSmith/Phoenix (futuro)
- **Diagrama**: Exemplo de JSON log
- **Tempo**: 2 min

---

#### Slide 40 — Traces: O Que São
- **Tipo**: Diagrama
- **Objetivo**: Introduzir o conceito de trace (aprofundamento em ETHAGT12)
- **Conteúdo**:
  - Trace = árvore de spans (cada step = span)
  - Span: nome, duração, input, output, metadata
  - Visualização: timeline de execução
  - Ferramentas: LangSmith, Phoenix, Langfuse
- **Diagrama**: Árvore de spans com timeline
- **Tempo**: 2 min

---

#### Slide 41 — Custo e Latência como Métricas de Primeira Classe
- **Tipo**: Conteúdo
- **Objetivo**: Fixar que custo e latência devem ser medidos desde o início
- **Conteúdo**:
  - Cada step tem custo (tokens in/out × preço)
  - Latência cumulativa (serial = soma)
  - Dashboard mínimo: step, tokens, custo, latência
  - Em produção: orçamento por execução
- **Diagrama**: Mini-dashboard com métricas
- **Tempo**: 1.5 min

---

### SEÇÃO F — Fechamento (Slides 43-62 · 12 min)

---

#### Slide 42 — [SEÇÃO] Boas Práticas e Anti-Patterns
- **Tipo**: Seção
- **Objetivo**: Transição para o fechamento
- **Conteúdo**: "7 — Boas Práticas e Anti-Patterns"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 43 — Boas Práticas (DO)
- **Tipo**: Conteúdo
- **Objetivo**: Checklist de boas práticas
- **Conteúdo**:
  - Comece simples (single LLM call antes de agente)
  - Documente tools como se fosse para um júnior
  - Defina max_steps desde o dia 1
  - Log estruturado desde a primeira linha
  - Sandbox para execução de tools
  - HITL em pontos críticos
  - Otimize o prompt efetivo, não apenas o prompt que você escreve
- **Diagrama**: Checklist verde (etho-success)
- **Tempo**: 2 min

---

#### Slide 44 — Anti-Patterns (DON'T)
- **Tipo**: Conteúdo
- **Objetivo**: Checklist do que NÃO fazer
- **Conteúdo**:
  - Começar com agente quando workflow basta
  - Adicionar complexidade sem evidência
  - Confiar no framework cegamente ("caixa preta")
  - Não definir max_steps (loop infinito)
  - Não logar (debug cego)
  - Tool mal documentada (ACI fraca)
  - Prompt gigante sem estrutura
  - Não testar em sandbox
- **Diagrama**: Checklist vermelho (etho-danger)
- **Tempo**: 2 min

---

#### Slide 45 — Caso de Estudo: Anthropic Coding Agent no SWE-bench
- **Tipo**: Diagrama
- **Objetivo**: Mostrar todos os conceitos em um caso real
- **Conteúdo**:
  - SWE-bench: resolver issues reais de GitHub
  - Arquitetura: Augmented LLM + loop + ACI + sandbox
  - Não há "magia" — é o que ETHAGT01 ensina
  - Claude 3.5 Sonnet: ~49% no SWE-bench Verified
  - Lição ACI: path absoluto vs relativo
- **Diagrama**: Arquitetura do coding agent
- **Tempo**: 3 min

---

#### Slide 46 — A Lição ACI do SWE-bench
- **Tipo**: Citação
- **Objetivo**: Fixar o princípio de ACI com o caso real
- **Conteúdo**:
  - "Após o agente sair do diretório raiz, começou a usar paths relativos errados.
    Em vez de mexer no prompt, mudaram a tool para exigir paths absolutos —
    e o erro desapareceu." — Schluntz, Anthropic
  - Tempo gasto em tools > tempo gasto no prompt principal
- **Diagrama**: Antes (path relativo, erro) → Depois (path absoluto, sucesso)
- **Tempo**: 1 min

---

#### Slide 47 — Exercício: Identificando um Loop Quebrado
- **Tipo**: Exercício
- **Objetivo**: Praticar debugging de agentes
- **Conteúdo**:
  - Mostrar um trace quebrado (agente em loop)
  - Em duplas: identificar onde o loop acontece
  - Propor 2 correções
  - 2 min discussão, 1 min compartilhar
- **Diagrama**: Trace de console com problema destacado
- **Tempo**: 3 min

---

#### Slide 48 — Resumo da Aula
- **Tipo**: Resumo
- **Objetivo**: Sintetizar os pontos-chave
- **Conteúdo**:
  - Augmented LLM = bloco fundamental (LLM + retrieval + tools + memory)
  - ReAct = padrão fundacional (Thought → Action → Observation)
  - Workflow vs Agente = decisão arquitetural (previsibilidade vs flexibilidade)
  - Comece simples, só aumente com evidência
  - ACI é onde mora a confiabilidade
  - Observabilidade desde o dia 1
- **Diagrama**: 6 ícones com os pontos-chave
- **Tempo**: 2 min

---

#### Slide 49 — Checklist da Aula
- **Tipo**: Resumo
- **Objetivo**: Confirmar que todos os tópicos foram cobertos
- **Conteúdo**:
  - [ ] Definiu agente vs workflow
  - [ ] Explicou Augmented LLM
  - [ ] Implementou ReAct do zero
  - [ ] Comparou 3 frameworks
  - [ ] Adicionou logging estruturado
  - [ ] Discutiu boas práticas e anti-patterns
- **Diagrama**: Checklist visual
- **Tempo**: 1 min

---

#### Slide 50 — Quiz: Pergunta 1
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "Qual é o bloco fundamental de qualquer sistema agêntico segundo Anthropic?"
  - A) Um framework como LangGraph
  - B) O Augmented LLM (LLM + retrieval + tools + memory)
  - C) Um prompt bem escrito
  - D) Um modelo grande o suficiente
  - Resposta: B
- **Tempo**: 1 min

---

#### Slide 51 — Quiz: Pergunta 2
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "Em ReAct, o que força o grounding do modelo?"
  - A) O prompt do sistema
  - B) A temperatura baixa
  - C) A Observation (resultado real da tool)
  - D) O max_steps
  - Resposta: C
- **Tempo**: 1 min

---

#### Slide 52 — Quiz: Pergunta 3
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "Quando você DEVERIA usar um agente em vez de um workflow?"
  - A) Quando a tarefa tem passos predefinidos
  - B) Quando você precisa de previsibilidade total
  - C) Quando os passos são imprevisíveis e exigem flexibilidade
  - D) Quando o custo precisa ser mínimo
  - Resposta: C
- **Tempo**: 1 min

---

#### Slide 53 — Quiz: Pergunta 4
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "O que é ACI?"
  - A) Agent Communication Interface
  - B) Agent-Computer Interface (design de tools)
  - C) Automated Code Injection
  - D) Agent Control Infrastructure
  - Resposta: B
- **Tempo**: 1 min

---

#### Slide 54 — Quiz: Pergunta 5
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "Qual é a PRIMEIRA coisa que você deve adicionar a um agente em produção?"
  - A) Um framework
  - B) Múltiplas tools
  - C) Observabilidade (logs estruturados + traces)
  - D) HITL
  - Resposta: C
- **Tempo**: 1 min

---

#### Slide 55 — Perguntas para Discussão
- **Tipo**: Exercício
- **Objetivo**: Estimular debate
- **Conteúdo**:
  1. "Toda aplicação de LLM deveria ser um agente?" (V/F justificado)
  2. "Em que cenário Python puro é melhor que LangGraph?"
  3. "Como você convenceria um PM de que workflow basta e agente é overkill?"
  4. "Qual o maior risco de começar com framework sem entender o básico?"
- **Tempo**: 2 min

---

#### Slide 56 — Conexão com Próximos Módulos
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar como ETHAGT01 conecta com o resto da especialização
- **Conteúdo**:
  - ETHAGT02 — Tool Calling e ACI (aprofunda ferramentas)
  - ETHAGT03 — Padrões de Workflow (os 5 padrões em detalhe)
  - ETHAGT04 — Reasoning & Planning (evolução do ReAct)
  - ETHAGT05 — Memória de Agentes (working vs persistente)
  - ETHAGT12 — AgentOps (observabilidade em profundidade)
- **Diagrama**: Mapa da especialização com ETHAGT01 no centro
- **Tempo**: 1 min

---

#### Slide 57 — Leitura Recomendada
- **Tipo**: Referências
- **Objetivo**: Indicar o que ler antes da próxima aula
- **Conteúdo**:
  - Obrigatório: Anthropic, *Building Effective Agents* (2024)
  - Obrigatório: Yao et al., *ReAct* (ICLR 2023, arXiv:2210.03629)
  - Recomendado: arXiv:2601.12560 (survey de arquiteturas)
  - Vídeo: Schluntz & Albert, *Building more effective AI agents* (YouTube)
- **Tempo**: 1 min

---

#### Slide 58 — Referências Completas
- **Tipo**: Referências
- **Objetivo**: Listar todas as fontes
- **Conteúdo**:
  1. Anthropic. *Building Effective Agents*. 2024. URL: anthropic.com/engineering/building-effective-agents
  2. Yao, S. et al. *ReAct: Synergizing Reasoning and Acting in Language Models*. ICLR 2023. arXiv:2210.03629
  3. Arunkumar V, Gangadharan G.R., Buyya R. *Agentic AI: Architectures, Taxonomies, and Evaluation*. arXiv:2601.12560, 2026
  4. Schick, T. et al. *Toolformer*. NeurIPS 2023. arXiv:2302.04761
  5. Jimenez, C. et al. *SWE-bench*. arXiv:2310.06770
  6. OpenAI. *Practical Guide to Building Agents*. 2024
  7. LangGraph docs: github.com/langchain-ai/langgraph
- **Tempo**: 0.5 min

---

#### Slide 59 — Projeto do Módulo
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar o projeto que os alunos devem entregar
- **Conteúdo**:
  - Implementar "research assistant" em 3 versões:
    1. Python puro
    2. LangGraph
    3. Framework à escolha (OpenAI SDK / CrewAI / PydanticAI)
  - O agente decide: responder direto, recuperar de base local, ou usar tool de busca
  - Entrega: repo + README comparativo + traces
  - Critério: justificar escolha com ≥3 critérios
- **Tempo**: 1 min

---

#### Slide 60 — Labs do Módulo
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar os laboratórios
- **Conteúdo**:
  - Lab 1 (4h): "ReAct em 50 linhas" — Python puro, tool de cálculo
  - Lab 2 (4h): "Augmented LLM" — adicionar retrieval + 2 tools
- **Tempo**: 0.5 min

---

#### Slide 61 — Próximos Passos
- **Tipo**: Conteúdo
- **Objetivo**: O que fazer antes da próxima aula
- **Conteúdo**:
  1. Ler: Anthropic *Building Effective Agents*
  2. Ler: ReAct paper (arXiv:2210.03629)
  3. Rodar: exemplo ReAct do repositório
  4. Iniciar: Lab 1
  5. Próxima aula: ETHAGT02 — Tool Calling e ACI
- **Tempo**: 1 min

---

#### Slide 62 — Q&A / Encerramento
- **Tipo**: Capa
- **Objetivo**: Abrir para perguntas e encerrar
- **Conteúdo**:
  - "Perguntas?"
  - Contato do professor
  - "Na próxima aula: ETHAGT02 — Tool Calling e ACI"
- **Diagrama**: Logo Etho + fundo etho-dark
- **Tempo**: 2 min

---

## Resumo do Storyboard

| Seção | Slides | Tempo | Conteúdo |
|---|---|---|---|
| A — Abertura | 1-6 | 8 min | Capa, objetivos, competências, agenda, motivação, contexto |
| B — Fundamentos | 7-22 | 22 min | Do LLM ao Agente, Augmented LLM, Agent Loop (ReAct), DEMO |
| C — Workflows | 23-28 | 10 min | Workflows vs Agentes, 5 padrões, árvore de decisão, exercício |
| D — Frameworks | 29-36 | 15 min | Python puro, LangGraph, OpenAI SDK, comparação, discussão |
| E — Observabilidade | 37-41 | 8 min | Logging, traces, custo, latência |
| F — Fechamento | 42-62 | 12 min | Boas práticas, anti-patterns, caso de estudo, exercício, resumo, quiz, referências, próximos passos, Q&A |
| **Total** | **62** | **90 min** | |

---

## Diagramas Necessários

| # | Slide | Diagrama | Tipo | Fonte |
|---|---|---|---|---|
| D1 | 9 | Taxonomia unificada (6 componentes) | Mind map radial | arXiv:2601.12560 |
| D2 | 12 | Augmented LLM | Flowchart | `12-Diagrams/ETHAGT01/augmented-llm.mmd` |
| D3 | 13 | RAG fixo vs RAG agêntico | Comparação | Novo |
| D4 | 14 | Fluxo de tool calling | Sequência | Novo |
| D5 | 15 | Working vs Persistente memory | Comparação | Novo |
| D6 | 18 | Agent Loop (ReAct) | Flowchart | `12-Diagrams/ETHAGT01/agent-loop.mmd` |
| D7 | 24 | Workflow vs Agente | Fluxograma | `12-Diagrams/ETHAGT01/workflow-vs-agent.mmd` |
| D8 | 25 | 5 workflows canônicos | Grid 2x3 | Anthropic |
| D9 | 26 | Árvore de decisão | Fluxograma | Novo |
| D10 | 27 | Pirâmide de complexidade | Pirâmide | Novo |
| D11 | 30 | Comparação 3 implementações | 3 colunas | Novo |
| D12 | 31 | Framework comparison | Flowchart | `12-Diagrams/ETHAGT01/framework-comparison.mmd` |
| D13 | 40 | Trace tree (spans) | Árvore | Novo |
| D14 | 45 | Arquitetura coding agent SWE-bench | Flowchart | `09-CaseStudies/01-anthropic-swe-bench-coding-agent.md` |
| D15 | 56 | Mapa da especialização | Mind map | Novo |

---

## Pendências de Produção

- [ ] Produzir 8 diagramas novos (D3, D4, D5, D9, D10, D11, D13, D15)
- [ ] Screenshot do trace real do exemplo ReAct (Slide 19)
- [ ] Screenshot do código com syntax highlighting (Slides 21, 31, 32, 33)
- [ ] Imagem de fundo para capa (Slide 1)
- [ ] Badge de competências (Slide 3)
- [ ] Timeline de marcos históricos (Slide 6)

---

> **Aguardando aprovação deste storyboard para gerar os slides detalhados com notas do professor.**
