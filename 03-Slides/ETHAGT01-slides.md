# ETHAGT01 — Arquitetura Cognitiva de Agentes LLM — Slides

> Apresentação para aula síncrona · ~50 min · 14 slides

## Estrutura da aula
- Abertura (5 min): gancho/motivação
- Teoria (25 min): conceitos principais com diagramas de referência
- Demonstração (10 min): código ao vivo ou walkthrough de lab
- Exercício (5 min): questão rápida ou discussão
- Fechamento (5 min): conexão com próximo módulo, leitura recomendada

## Slides

### Slide 1 — Título
- ETHAGT01 — Arquitetura Cognitiva de Agentes LLM
- Professor, data, Universität Etho
- Contexto: Fase A — Fundamentos Agênticos
- ~1 min

### Slide 2 — Agenda
1. Do LLM ao agente: o que muda
2. Augmented LLM: o bloco fundamental
3. O Agent Loop: ReAct
4. Workflows vs Agentes
5. Implementação: do zero vs framework
6. Observabilidade desde o dia 1
- ~1 min

### Slide 3 — Gancho / Motivação
- Problema: "LLM como oráculo" responde uma vez e acabou — falha em tarefas multi-step
- Exemplo concreto: "Reserve um voo, hotel e carro para a conferência" — LLM sozinho erra porque não pode agir
- Pergunta à turma: *Quantos de vocês já tentaram fazer uma tarefa multi-step com ChatGPT puro e fracassaram?*
- A solução: LLM como controlador cognitivo em loop
- Diagrama: `12-Diagrams/ETHAGT01/agent-loop.mmd`
- ~3 min

### Slide 4 — Do LLM ao Agente
- Transição: geração única → controle cognitivo de longo prazo
- Definições concorrentes de "agente" e o recuo pragmático de Anthropic
- Taxonomia unificada: Perception · Brain · Planning · Action · Tool Use · Collaboration (arXiv:2601.12560)
- Por que agora: confluência de reasoning, tools, context
- Pergunta: *Qual dessas capacidades você acha que foi o gatilho mais recente?*
- ~4 min

### Slide 5 — O Augmented LLM
- Bloco fundamental: LLM + retrieval + tools + memory
- Diagrama: `12-Diagrams/ETHAGT01/augmented-llm.mmd`
- Retrieval in-loop: o modelo gera suas próprias queries
- Tools como extensão de ação; tool calling estruturado
- Memory: working (context window) vs persistente — panorama
- Interface bem documentada: a regra de ouro
- ~4 min

### Slide 6 — O Agent Loop: ReAct
- Padrão fundacional: Thought → Action → Observation em loop
- Por que funciona: força-grounding via observação do ambiente
- Diagrama: `12-Diagrams/ETHAGT01/agent-loop.mmd`
- Exemplo de trace real (print de console): Thought → Action: search("previsão do tempo RJ") → Observation: "25°C, chuva" → Thought → Action: decide responder
- Limitações: loops infinitos, custo, alucinação em ação
- ~4 min

### Slide 7 — DEMO: ReAct em 50 Linhas
- Código ao vivo: implementação mínima em Python puro (sem SDK)
- Tool de cálculo como exemplo
- Loop principal: while not done: thought → action → observation
- Mostrar trace no terminal
- Referência: `05-Labs/ETHAGT01/Lab1-ReAct-50-linhas`
- Pergunta: *O que acontece se a tool retornar erro? Quem trata?*
- ~5 min

### Slide 8 — Workflows vs Agentes
- Distinção canônica de Anthropic: workflows = previsibilidade, agentes = flexibilidade
- Os 5 workflows (visão geral; aprofundamento em ETHAGT03): prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer
- Diagrama: `12-Diagrams/ETHAGT01/workflow-vs-agent.mmd`
- Critério de decisão: comece simples, só aumente com evidência
- Exercício rápido: *Dê 3 exemplos de problemas que pedem workflow vs 3 que pedem agente*
- ~4 min

### Slide 9 — Implementação: do zero vs framework
- ReAct em Python puro (revisão com tool real de API)
- Mesmo agente em LangGraph
- Mesmo agente em OpenAI Agents SDK
- Diagrama: `12-Diagrams/ETHAGT01/framework-comparison.mmd`
- O que cada framework abstrai vs o que esconde
- Quando reduzir camadas de abstração em produção
- Pergunta: *Qual framework vocês acham que dá mais controle? E mais produtividade?*
- ~4 min

### Slide 10 — Observabilidade Desde o Dia 1
- Logging estruturado: thought/action/observation com timestamps
- Traces: introdução ao conceito (aprofundamento em ETHAGT12)
- Custo e latência como métricas de primeira classe
- Tooling mínimo: print → structured logs → LangSmith/Phoenix (futuro)
- Exemplo de log estruturado em JSON
- ~3 min

### Slide 11 — Exercício: Identificando um Loop
- Mostrar um trace quebrado (agente entrou em loop)
- Em duplas: identificar onde o loop acontece e propor 2 correções
- 2 min discussão, 1 min compartilhar
- Resposta esperada: falta de condição de parada, observação mal formatada
- ~3 min

### Slide 12 — Conexão com Próximo Módulo
- ETHAGT02 — Tool Calling e ACI: aprofunda ferramentas com design de qualidade
- ETHAGT03 — Padrões de Workflow: os 5 padrões em detalhe
- Leitura recomendada: Anthropic *Building Effective Agents* (2024)
- Paper: Yao et al. *ReAct* (ICLR 2023)
- ~2 min

### Slide 13 — Referências
- Anthropic. *Building Effective Agents*. 2024
- Yao, S. et al. *ReAct: Synergizing Reasoning and Acting in Language Models*. ICLR 2023
- Arunkumar V. et al. *Agentic AI: Architectures, Taxonomies, and Evaluation*. arXiv:2601.12560, 2026
- LangGraph docs: examples/react-agent-from-scratch
- ~1 min

### Slide 14 — Q&A
- Perguntas abertas
- Preview do projeto do módulo: research assistant em 3 versões
