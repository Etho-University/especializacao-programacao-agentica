# ETHAGT03 — Padrões de Workflow Agêntico — Slides

> Apresentação para aula síncrona · ~50 min · 14 slides

## Estrutura da aula
- Abertura (5 min): gancho/motivação
- Teoria (25 min): conceitos principais com diagramas de referência
- Demonstração (10 min): código ao vivo ou walkthrough de lab
- Exercício (5 min): questão rápida ou discussão
- Fechamento (5 min): conexão com próximo módulo, leitura recomendada

## Slides

### Slide 1 — Título
- ETHAGT03 — Padrões de Workflow Agêntico (os 5 da Anthropic + composições)
- Professor, data, Universität Etho
- Pré-requisitos: ETHAGT01 (recomendado ETHAGT02)
- ~1 min

### Slide 2 — Agenda
1. Por que workflows antes de agentes
2. Prompt Chaining
3. Routing
4. Parallelization (Sectioning + Voting)
5. Orchestrator-Workers
6. Evaluator-Optimizer
7. Composições e limites
- ~1 min

### Slide 3 — Gancho / Motivação
- Problema: time pula direto para agente autônomo e colhe complexidade desnecessária
- Exemplo: chatbot de suporte que precisa de 3 etapas fixas (classificar → buscar → responder) — um agente livre é overkill
- Princípio de Anthropic: comece simples, só aumente com evidência
- Pergunta: *Quantos de vocês já viram um projeto que usou agente onde um if bastava?*
- ~3 min

### Slide 4 — Prompt Chaining
- Estrutura: LLM → gate → LLM → ...
- Onde adicionar gates (validação, classificação, formatação)
- Quando trade-off de latência por accuracy vale
- Exemplo: gerar rascunho → revisar (gate: tem todos os campos?) → reescrever
- Diagrama: `12-Diagrams/ETHAGT03/prompt-chaining.mmd`
- ~4 min

### Slide 5 — Routing
- Classificação como etapa separada
- Routing por modelo: Haiku para fácil, Sonnet para difícil
- Routing por prompt/tools especializados
- Avaliando a qualidade do classificador (matriz de confusão)
- Diagrama: `12-Diagrams/ETHAGT03/routing.mmd`
- Pergunta: *Como saber se o roteador está errando? O que medir?*
- ~3 min

### Slide 6 — Parallelization: Sectioning
- Subtarefas independentes em paralelo
- Exemplo: revisar código → rodar linter + testes + typecheck em paralelo
- Ganho: latência = max(subtasks) vs sum(subtasks)
- Erro comum: dependências ocultas entre "subtarefas independentes"
- Diagrama: `12-Diagrams/ETHAGT03/parallelization-sectioning.mmd`
- ~3 min

### Slide 7 — Parallelization: Voting
- Mesma tarefa N vezes, agregação por maioria
- Quando usar: classificação, geração de código crítico
- Guardrails em paralelo: modelo responde + modelo filtra
- Custo: N× o custo base
- Diagrama: `12-Diagrams/ETHAGT03/parallelization-voting.mmd`
- Pergunta: *N=3 ou N=5? Qual o trade-off?*
- ~3 min

### Slide 8 — Orchestrator-Workers
- Distinção chave vs parallelization: subtarefas são **dinâmicas**
- Orquestrador como LLM que planeja + sintetiza
- Implementação: task-decomposition + workers + reducer
- Casos: coding em múltiplos arquivos, search em múltiplas fontes
- Diagrama: `12-Diagrams/ETHAGT03/orchestrator-workers.mmd`
- ~4 min

### Slide 9 — DEMO: Os 5 Workflows em 1 Domínio
- Código ao vivo: mesmo ticket de suporte implementado nos 5 padrões
- Prompt Chaining: classificar → buscar → responder
- Routing: simples vai direto, complexo vai para analista
- Parallelization: buscar FAQ + documentação + histórico em paralelo
- Orchestrator-Workers: orquestrador delega sub-perguntas
- Evaluator-Optimizer: gerar → avaliar cobertura → refinar
- Referência: `05-Labs/ETHAGT03/Lab1-Os-5-em-1-dia`
- Medir custo/latência de cada ao vivo
- ~6 min

### Slide 10 — Evaluator-Optimizer
- Loop: gerar → avaliar → refinar até critério
- Quando tem valor: feedback humano articulável; LLM consegue avaliar
- Critérios claros e mensuráveis
- Convergência: parar por score, max iters, ou delta estagnado
- Diagrama: `12-Diagrams/ETHAGT03/evaluator-optimizer.mmd`
- ~3 min

### Slide 11 — Composições e Limites
- Composições típicas: routing → parallelization → evaluator-optimizer
- Quando combinar vira agente (e como saber)
- Sinais de que você está forçando workflow em problema que pede agente
- Discussão: *O que diferencia um workflow composto de um agente? A linha é tênue.*
- ~3 min

### Slide 12 — Exercício: Escolha o Workflow
- 5 cenários impressos (ou projetados):
  1. Tradução com revisão de qualidade
  2. Análise de sentimentos de 10.000 tweets
  3. Geração de relatório com múltiplas fontes
  4. Chatbot de FAQ simples
  5. Correção de redação com feedback
- Em grupos: indicar workflow + justificar
- 3 min discussão, 2 min compartilhar
- ~5 min

### Slide 13 — Conexão com Próximo Módulo
- ETHAGT04 — Reasoning & Planning: quando workflow não basta, entra raciocínio avançado
- ETHAGT09 — Multi-Agente: workflows como fundação de orquestração
- Leitura: Anthropic *Building Effective Agents* (seção principal)
- Paper: arXiv:2601.12560 (taxonomia)
- ~2 min

### Slide 14 — Referências
- Anthropic. *Building Effective Agents*. 2024
- LangGraph examples: plan-and-execute, llm-compiler, multi-agent
- Schluntz, E. & Albert, A. *Building more effective AI agents* (YouTube)
- Coinbase, Intercom case studies
- ~1 min
