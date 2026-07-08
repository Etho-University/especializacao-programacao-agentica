# ETHAGT04 — Reasoning & Planning — Slides

> Apresentação para aula síncrona · ~50 min · 14 slides

## Estrutura da aula
- Abertura (5 min): gancho/motivação
- Teoria (25 min): conceitos principais com diagramas de referência
- Demonstração (10 min): código ao vivo ou walkthrough de lab
- Exercício (5 min): questão rápida ou discussão
- Fechamento (5 min): conexão com próximo módulo, leitura recomendada

## Slides

### Slide 1 — Título
- ETHAGT04 — Reasoning & Planning (do CoT ao inference-time reasoning)
- Professor, data, Universität Etho
- Pré-requisito: ETHAGT03
- ~1 min

### Slide 2 — Agenda
1. Tipologia do raciocínio (CoT, antes/durante, linear/árvore/grafo)
2. Plan-and-Execute e ReWOO
3. Tree of Thoughts e LATS
4. Reflexion
5. Self-Discover
6. Inference-Time Reasoning nativo
7. Falhas, loops e orçamento
- ~1 min

### Slide 3 — Gancho / Motivação
- Problema: ReAct simples não resolve problemas que exigem exploração ou backtracking
- Exemplo: "Planeje uma viagem de 7 dias com orçamento de R$5000" — agente linear entra em loop ou faz plano ruim
- A solução: raciocínio estruturado (árvore, reflexão, planejamento explícito)
- Pergunta: *Quando um passo errado no meio inviabiliza todo o plano?*
- ~3 min

### Slide 4 — Tipologia do Raciocínio
- CoT (zero-shot, few-shot, self-consistency)
- Raciocínio antes (Plan-and-Execute) vs durante (ReAct) a ação
- Linear vs árvore (ToT) vs grafo (LATS)
- O casamento reasoning + tools
- Pergunta: *Self-consistency: quantas amostras são suficientes?*
- ~4 min

### Slide 5 — Plan-and-Execute e ReWOO
- Planner gera plano completo; executor opera sequencialmente
- ReWOO: plano "cego" + evidências paralelas; redução de tokens
- Vantagens: eficiência, paralelismo
- Desvantagens: rigidez, não re-planeja
- Diagrama: `12-Diagrams/ETHAGT04/plan-execute.mmd`
- Discussão: *Quando o plano inicial é tão bom que não precisa re-planejar?*
- ~4 min

### Slide 6 — Tree of Thoughts e LATS
- Exploração em árvore com avaliação de estados (ToT)
- LATS: MCTS + LLM; backtracking e busca
- Custo vs qualidade: quando vale
- Casos: raciocínio matemático, planejamento de código
- Diagrama: `12-Diagrams/ETHAGT04/tot-search-tree.mmd`
- Pergunta: *Qual o custo adicional de ToT vs ReAct? Vale a pena?*
- ~4 min

### Slide 7 — Reflexion
- Auto-crítica após falha; memória de erros anteriores
- Reflexion vs Reflection pattern simples (diferença sutil mas importante)
- Convergência: limite de tentativas para evitar loop
- Diagrama: `12-Diagrams/ETHAGT04/reflexion-loop.mmd`
- Exemplo: agente que erra cálculo, reflete "errei porque usei fórmula errada", e corrige
- ~4 min

### Slide 8 — Self-Discover
- O agente compõe sua própria estratégia de raciocínio
- Primitivas (REACT, CoT, etc.) como building blocks selecionáveis
- Quando o problema é tão novo que não há padrão pronto
- Caso: problemas de pesquisa onde a estratégia ótima é desconhecida
- ~3 min

### Slide 9 — DEMO: Plan-and-Execute vs ReAct
- Código ao vivo: mesma tarefa multi-step nos dois padrões
- Mostrar trace do ReAct (passo a passo, re-planejando)
- Mostrar trace do Plan-and-Execute (plano inicial + execução)
- Comparar: tokens gastos, acertos, tempo
- Referência: `05-Labs/ETHAGT04/Lab1-Plan-vs-ReAct`
- Pergunta: *Qual padrão vocês usariam para uma tarefa de 20 passos?*
- ~5 min

### Slide 10 — Inference-Time Reasoning Nativo
- Modelos treinados para pensar: o1, o3, Claude com extended thinking
- O que muda no design do agente: sem CoT promptado, mais tools, orçamento de tokens
- Quando escolher reasoning model vs prompting
- Custo e latência: estratégias de mitigação
- Pergunta: *O reasoning nativo substitui Tree of Thoughts? Em quais casos?*
- ~3 min

### Slide 11 — Falhas, Loops e Orçamento
- Detecção e quebra de loops (monitorar repetição de ações)
- Orçamento de tokens/passos (max steps, max tokens)
- Re-planejamento supervisionado (HITL no plano)
- Avaliação comparativa
- ~3 min

### Slide 12 — Exercício: Qual Estratégia para Cada Problema?
- 5 classes de problema projetadas:
  1. Problema matemático multi-step (ex: provar teorema)
  2. Busca em árvore de decisões (ex: jogo da velha)
  3. Correção de código com feedback do compilador
  4. Pergunta com múltiplas fontes conflitantes
  5. Tarefa criativa (ex: escrever um conto)
- Em duplas: indicar estratégia + justificar 2 linhas
- ~4 min

### Slide 13 — Conexão com Próximo Módulo
- ETHAGT05 — Memória de Agentes: estende Reflexion com memória persistente
- ETHAGT06 — RAG Agêntico: raciocínio + recuperação combinados
- Leitura: Yao et al. *Tree of Thoughts* (arXiv:2305.10601)
- Paper: Shinn et al. *Reflexion* (arXiv:2303.11366)
- ~2 min

### Slide 14 — Referências
- Yao, S. *Tree of Thoughts* (arXiv:2305.10601)
- Shinn, N. *Reflexion* (arXiv:2303.11366)
- Wang, X. *Self-Consistency* (arXiv:2203.11171)
- OpenAI. *Learning to Reason with LLMs* (o1 launch paper)
- Zhou, A. *ReWOO* (arXiv:2305.18323)
- Zhou, A. *LATS* (arXiv:2310.01757)
- ~1 min
