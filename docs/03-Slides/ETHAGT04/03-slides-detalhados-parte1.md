# ETHAGT04 — Slides Detalhados + Notas do Professor (Parte 1: Slides 1-45)

> Universidade Etho · Especialização em Programação Agêntica
> Cada slide contém: título, objetivo, conteúdo, notas do professor, diagrama, animação, imagem, tempo.

---

## SEÇÃO A — Abertura (Slides 1-7 · 8 min)

---

### Slide 1 — Capa

**Título**: ETHAGT04 — Reasoning & Planning
**Objetivo**: Identificar a aula, o professor e o contexto.
**Conteúdo**:
- ETHAGT04 — Reasoning & Planning (do CoT ao inference-time reasoning)
- Universidade Etho · Especialização em Programação Agêntica
- Fase B — Razão, Memória e Conhecimento · 30 h
- Professor · Data

**Diagrama**: Logo Etho + fundo abstrato (árvore de raciocínio)
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Bem-vindos ao ETHAGT04. Esta é a aula que separa quem entende agentes de quem entende agentes INTELIGENTES. Em ETHAGT01 vocês viram o ReAct — o padrão fundacional. Hoje vamos ver suas evoluções: como fazer um agente PLANEJAR antes de agir, como fazer ele EXPLORAR múltiplos caminhos (em vez de seguir um só), como fazer ele APRENDER com os próprios erros.
💡 ANALOGIA: ETHAGT01 foi aprender a andar. Hoje vocês vão aprender a correr, pular e escalar.
❓ PERGUNTA PARA A TURMA: "Quantos já viram um agente ficar preso em loop, repetindo a mesma ação?" (levantar mãos)
⚠️ ERROS COMUNS: Alunos chegam achando que "raciocínio" é só CoT. É muito mais — é um espectro.
➡️ TRANSIÇÃO: "Vamos definir o que vocês vão conseguir fazer."

---

### Slide 2 — Objetivos do Módulo

**Título**: Objetivos do Módulo
**Objetivo**: Deixar claro o que o aluno deve conseguir FAZER ao final.
**Conteúdo**:
- **Objetivo geral**: Dominar o espectro de estratégias de raciocínio e planejamento para agentes
- **Objetivos específicos**:
  1. Caracterizar planejamento antes vs durante a ação; linear vs em árvore
  2. Implementar: ReAct (revisão), Plan-and-Execute, ReWOO, ToT, LATS, Reflexion, Self-Discover
  3. Compreender quando usar reasoning model nativo vs padrão promptado
  4. Avaliar trade-offs: qualidade × custo × latência × robustez
  5. Lidar com falhas clássicas: plano rígido, re-planejamento ausente, loops

**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Cada objetivo é mensurável. O mais importante é #4 — trade-offs. Não existe "melhor técnica de raciocínio". Existe a técnica certa para o problema certo. Se ao final da aula vocês sabem escolher, a aula funcionou.
💡 ANALOGIA: É como ter uma caixa de ferramentas com 7 ferramentas. Não usar sempre a mesma — saber qual serve para cada problema.
❓ PERGUNTA: "Qual objetivo vocês acham mais desafiador?" (geralmente #2 ou #4)
➡️ TRANSIÇÃO: "Competências."

---

### Slide 3 — Competências Desenvolvidas

**Título**: Competências Desenvolvidas
**Objetivo**: Conectar a aula ao Framework Etho.
**Conteúdo**:

| Competência | Nível ao final |
|---|---|
| C1 Programação Agêntica | **I** |
| C2 Multi-Agent Systems | **B** |
| C4 Agent Memory | **B** |
| C5 AgentOps & Avaliação | **B** |

**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: C1 atinge Intermediário. C2 entra em Básico porque LATS e Reflexion já tocam em multi-step coordination. C4 (memória) é tocado por Reflexion, que usa memória de erros. C5 é tocado pelos benchmarks que vamos discutir (GSM8K, GAIA).
➡️ TRANSIÇÃO: "Agenda."

---

### Slide 4 — Agenda

**Título**: Agenda da Aula
**Conteúdo**:
- **Bloco 1 (60 min)**: Abertura, Tipologia, Plan-and-Execute, ToT/LATS, Intervalo
- **Bloco 2 (60 min)**: Reflexion, Self-Discover, Reasoning Nativo, Falhas/Orçamento, Fechamento

**Tempo**: 1 min

---

### Slide 5 — Motivação: Quando ReAct Não Basta

**Título**: Quando ReAct Não Basta
**Objetivo**: Criar tensão cognitiva — ReAct linear falha em problemas que exigem exploração.
**Conteúdo**:
- **Cenário**: "Planeje uma viagem de 7 dias com orçamento de R$5000"
- **ReAct puro**:
  - Passo 1: buscar voos → R$3000 (sobe de 50% do orçamento)
  - Passo 2: buscar hotel → R$2000 (sobe de 80%)
  - Passo 3: atividades → não cabe mais. Loop.
  - Sem backtracking: não pode voltar e escolher voos mais baratos
- **O problema**: um passo errado no meio inviabiliza todo o plano
- **Solução**: raciocínio estruturado — planejar antes, explorar caminhos, refletir sobre erros

**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: ReAct é excelente para tarefas onde cada passo é independente. Mas quando os passos DEPENDEM uns dos outros e uma escolha ruim no início compromete tudo, ReAct não consegue voltar. É como entrar num beco sem saída e não poder dar ré.
💡 ANALOGIA: É como um xadrez. Se você joga move-by-move sem pensar adiante (ReAct), perde. Um mestre pensa vários lances à frente (ToT), aprende com jogos anteriores (Reflexion), e tem uma estratégia (Plan-and-Execute).
❓ PERGUNTA: "Quando um passo errado no meio inviabiliza todo o plano? Vocês já viram isso?"
⚠️ ERROS COMUNS: Alunos acham que "mais max_steps" resolve. Não resolve — o agente continua indo na direção errada, só que por mais tempo.
➡️ TRANSIÇÃO: "Vamos ver o espectro de soluções."

---

### Slide 6 — Contexto: O Espectro do Raciocínio

**Título**: O Espectro do Raciocínio
**Objetivo**: Mostrar o panorama de estratégias que serão cobertas.
**Conteúdo**:
- **Linha do tempo**:
  - 2022: Chain-of-Thought (Wei et al.)
  - Mar/2023: ReAct (Yao et al.) — raciocínio durante a ação
  - Mai/2023: Tree of Thoughts (Yao et al.) — busca em árvore
  - Mar/2023: Reflexion (Shinn et al.) — auto-crítica com memória
  - 2024: LATS (Zhou et al.) — MCTS + LLM
  - Fev/2024: Self-Discover — composição de estratégia
  - Set/2024: OpenAI o1 — reasoning nativo via RL

**Diagrama**: `12-Diagrams/ETHAGT04/reasoning-spectrum.mmd`
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Cada técnica resolve uma limitação da anterior. CoT adiciona raciocínio. ReAct adiciona ação. ToT adiciona exploração. LATS adiciona busca sistemática. Reflexion adiciona aprendizado. Self-Discover adiciona meta-raciocínio. o1 traz o raciocínio para dentro do modelo.
➡️ TRANSIÇÃO: "Vamos começar pela fundação: CoT."

---

### Slide 7 — [SEÇÃO] Tipologia do Raciocínio

**Título**: 1 — Tipologia do Raciocínio
**Tipo**: Seção
**Tempo**: 0.5 min

---

## SEÇÃO B — Tipologia do Raciocínio (Slides 8-18 · 14 min)

---

### Slide 8 — Chain-of-Thought: A Fundação

**Título**: Chain-of-Thought (CoT)
**Objetivo**: Apresentar a base de todo raciocínio em LLMs.
**Conteúdo**:
- **CoT zero-shot**: "Let's think step by step" — uma frase mágica
- **CoT few-shot**: exemplos de raciocínio passo-a-passo no prompt
- **Por que funciona**: LLMs geram melhor quando "pensam em voz alta"
- **Fonte**: Wei et al., NeurIPS 2022 (arXiv:2201.11903)

**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: CoT é a técnica mais simples e mais poderosa de raciocínio. A ideia é não pedir a resposta direta — pedir que o modelo MOSTRE o raciocínio. "Let's think step by step" adiciona até 20 pontos em benchmarks matemáticos. Por quê? Porque o LLM não "pensa e depois responde" — ele pensa ATRAVÉS da geração. Cada token gerado é parte do raciocínio.
💡 ANALOGIA: É como pedir para um aluno não só dar a resposta, mas mostrar o cálculo. Ao escrever o cálculo, ele se corrige no meio.
⚠️ ERROS COMUNS: Alunos acham que CoT é "adicionar prompt". É, mas o efeito é estrutural — muda a distribuição de geração.
➡️ TRANSIÇÃO: "E se amostrarmos múltiplas vezes?"

---

### Slide 9 — Self-Consistency

**Título**: Self-Consistency
**Objetivo**: Mostrar que múltiplas amostras + votação melhoram a precisão.
**Conteúdo**:
- **Ideia**: gerar N raciocínios independentes (temperatura > 0)
- **Votação**: escolher a resposta mais frequente (majority vote)
- **Custo**: N× mais caro que CoT simples
- **Fonte**: Wang et al., 2022 (arXiv:2203.11171)

**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Self-consistency explora o fato de que LLMs podem chegar à mesma resposta por caminhos diferentes. Se 7 de 10 raciocínios dão "42" e 3 dão "38", você escolhe "42". O custo é N× maior mas a confiabilidade aumenta. Quantas amostras? Tipicamente 5-20. Mais que 20 tem retorno marginal.
💡 ANALOGIA: É como perguntar a 10 pessoas qual é a capital da Austrália. Se 9 dizem "Canberra" e 1 diz "Sydney", você confia na maioria.
➡️ TRANSIÇÃO: "CoT raciocina. Mas raciocina ANTES ou DURANTE a ação?"

---

### Slide 10 — Antes vs Durante a Ação

**Título**: Raciocínio Antes vs Durante a Ação
**Objetivo**: Distinguir duas famílias fundamentais de planejamento.
**Conteúdo**:
- **Durante (ReAct)**: pensa → age → observa → pensa → age → ...
  - Adaptativo, flexível
  - Mas: pode se perder, re-escolhe a cada passo
- **Antes (Plan-and-Execute)**: planeja tudo → executa
  - Eficiente, estruturado
  - Mas: rígido, não adapta se algo inesperado acontece

**Diagrama**: Comparação lado a lado
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esta é a distinção mais importante da aula. ReAct raciocina DURANTE — a cada passo, reconsidera. Plan-and-Execute raciocina ANTES — gera um plano completo, depois executa cegamente. Cada um tem vantagens. ReAct é flexível mas caro (reescolhe a cada passo). Plan-and-Execute é eficiente mas rígido (se o plano falha, precisa replanejar).
💡 ANALOGIA: ReAct é como dirigir olhando pelo espelho a cada segundo. Plan-and-Execute é como programar o GPS no início — eficiente, mas se uma rua fecha, precisa recalcular.
➡️ TRANSIÇÃO: "E estruturalmente, como é o raciocínio?"

---

### Slide 11 — Linear vs Árvore vs Grafo

**Título**: Linear vs Árvore vs Grafo
**Objetivo**: Mostrar as três estruturas de raciocínio.
**Conteúdo**:
- **Linear (ReAct)**: Thought → Action → Observation → Thought → ...
  - Um caminho, sem bifurcação
- **Árvore (ToT)**: gerar múltiplos candidatos → avaliar → explorar o melhor
  - Backtracking possível
- **Grafo/LATS**: MCTS — seleção, expansão, avaliação, backpropagation
  - Busca sistemática com memória de estados

**Diagrama**: Comparação visual das 3 estruturas
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A evolução do raciocínio é estrutural. ReAct é linear — um caminho só. ToT é uma árvore — explora múltiplos ramos e pode voltar (backtrack). LATS é um grafo (MCTS) — busca sistemática com memória, avaliação de estados e backpropagation de valor. Cada nível adiciona poder mas também custo.
➡️ TRANSIÇÃO: "E como raciocínio se une com tools?"

---

### Slide 12 — Reasoning + Tools

**Título**: Reasoning + Tools
**Objetivo**: Mostrar que raciocínio e tool use não são separados.
**Conteúdo**:
- ReAct já une reasoning + acting
- ToT pode usar tools em cada ramo da árvore
- Reflexion usa tools, reflete, ajusta o uso de tools
- Reasoning nativo (o1) também chama tools entre "pensamentos"

**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Uma confusão comum é achar que "raciocínio" e "tools" são separados. Não são. Em todas as técnicas avançadas, o raciocínio guia QUANDO e QUAIS tools chamar. ToT pode ramificar a árvore chamando diferentes tools. Reflexion reflete sobre POR QUE uma tool falhou.
➡️ TRANSIÇÃO: "Vamos à primeira técnica: Plan-and-Execute."

---

### Slide 13 — [SEÇÃO] Plan-and-Execute e ReWOO

**Tipo**: Seção
**Tempo**: 0.5 min

---

## SEÇÃO C — Plan-and-Execute e ReWOO (Slides 19-30 · 16 min)

---

### Slide 14 — Plan-and-Execute: Arquitetura

**Título**: Plan-and-Execute
**Objetivo**: Apresentar a arquitetura Planner → Executor.
**Conteúdo**:
- **Planner**: LLM gera lista de passos (sem executar)
  - Ex: ["1. Buscar voos SP→RJ", "2. Buscar hotéis RJ", "3. Calcular total", "4. Verificar orçamento"]
- **Executor**: executa cada passo (pode ser ReAct por passo)
- **Replanner** (opcional): se um passo falha, re-planeja o restante
- **Fonte**: LangGraph plan-and-execute template

**Diagrama**: `12-Diagrams/ETHAGT04/plan-execute.mmd`
**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Plan-and-Execute separa duas preocupações: planejamento e execução. O Planner não executa nada — só decomponhe a tarefa em passos. O Executor pega cada passo e executa (pode usar ReAct internamente). O Replanner é o opcional que torna o sistema adaptativo: se o passo 2 falha, ele re-planeja os passos 3+.
💡 ANALOGIA: É como um arquiteto (Planner) que desenha a planta e um pedreiro (Executor) que constrói. Se o pedreiro encontra uma tubulação não mapeada, o arquiteto redesenha (Replanner).
❓ PERGUNTA: "Para que tipo de tarefa Plan-and-Execute é melhor que ReAct?"
⚠️ ERROS COMUNS: Alunos implementam Plan-and-Execute sem Replanner. O plano é rígido e falha ao primeiro obstáculo.
➡️ TRANSIÇÃO: "Existe uma variação mais eficiente: ReWOO."

---

### Slide 15 — ReWOO: Reasoning WithOut Observation

**Título**: ReWOO
**Objetivo**: Mostrar como ReWOO reduz custo paralelizando evidências.
**Conteúdo**:
- **Ideia**: Planner gera plano "cego" (sem ver observações)
- **Paralelização**: todas as tools são chamadas em paralelo
- **Solver**: combina as evidências para a resposta final
- **Vantagem**: 1 chamada de raciocínio (Planner) + N chamadas de tool paralelas + 1 chamada (Solver)
- **Fonte**: Xu et al., 2023 (arXiv:2305.18323)

**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: ReWOO é elegante. Em vez de intercalar raciocínio e execução (como ReAct), ele separa totalmente. O Planner diz "preciso saber X, Y e Z" — sem esperar pelas respostas. As três tools rodam em paralelo. O Solver combina tudo. Isso reduz chamadas de LLM e permite paralelismo.
💡 ANALOGIA: É como enviar três pesquisadores simultaneamente para buscar informações diferentes, em vez de mandar um de cada vez esperando voltar.
⚠️ ERROS COMUNS: ReWOO não funciona bem quando a tool B depende do resultado da tool A. Se a segunda busca precisa do resultado da primeira, não pode paralelizar.
➡️ TRANSIÇÃO: "Vamos comparar os três."

---

### Slide 16 — Trade-offs: ReAct vs Plan-Execute vs ReWOO

**Título**: Comparação das 3 Abordagens
**Objetivo**: Sistematizar trade-offs.
**Conteúdo**:

| Critério | ReAct | Plan-and-Execute | ReWOO |
|---|---|---|---|
| Flexibilidade | ✅ Alta | ⚠️ Média | ❌ Baixa |
| Eficiência (tokens) | ❌ Baixa | ⚠️ Média | ✅ Alta |
| Latência | ❌ Serial | ⚠️ Serial | ✅ Paralelo |
| Re-planejamento | ✅ Nativo | ⚠️ Opcional | ❌ Não |
| Complexidade | ✅ Simples | ⚠️ Média | ⚠️ Média |

**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Não há vencedor. ReAct ganha em flexibilidade. ReWOO ganha em eficiência. Plan-and-Execute é meio-termo. A escolha depende do problema. Tarefas sequenciais dependentes → ReAct. Tarefas paralelizáveis com informação independente → ReWOO. Tarefas estruturadas com possibilidade de falha → Plan-and-Execute com Replanner.
❓ PERGUNTA: "Para o sistema de vocês, qual seria a melhor?"
➡️ TRANSIÇÃO: "E quando o plano falha?"

---

### Slide 17 — Quando Re-planejar

**Título**: Quando Re-planejar
**Objetivo**: Dar critérios para detectar falha de plano.
**Conteúdo**:
- **Sinais de falha**:
  - Tool retorna erro ou resultado inesperado
  - Resultado contradiz premissa do plano
  - Orçamento estourando (custo, tempo)
  - Loop detectado (mesma ação repetida)
- **Estratégias**:
  - Re-planejamento automático (LLM re-gera plano restante)
  - HITL: humano aprova ou ajusta o plano
  - Fallback: plano simplificado pré-definido

**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Re-planejamento é o que torna Plan-and-Execute adaptativo. Sem ele, o plano é rígido. A questão é QUANDO disparar o replanner. Sinais objetivos: erro de tool, timeout, custo excedido. Sinais subjetivos: resultado "estranho" — mais difícil de detectar. Em produção, HITL no replanejamento é essencial para tarefas de alto risco.
➡️ TRANSIÇÃO: "Vamos subir de nível: Tree of Thoughts."

---

### Slide 18 — Intervalo

**Título**: Intervalo (5 min)
**Tempo**: 5 min

---

## SEÇÃO D — Tree of Thoughts e LATS (Slides 31-45 · 18 min)

---

### Slide 19 — [SEÇÃO] Tree of Thoughts e LATS

**Tipo**: Seção
**Tempo**: 0.5 min

---

### Slide 20 — Tree of Thoughts: Busca em Árvore

**Título**: Tree of Thoughts (ToT)
**Objetivo**: Apresentar busca em árvore como evolução do raciocínio linear.
**Conteúdo**:
- **Decompor**: quebrar problema em sub-problemas
- **Gerar candidatos**: para cada estado, gerar múltiplos "pensamentos" candidatos
- **Avaliar**: LLM avalia cada candidato (viable/not viable, ou score 1-10)
- **Buscar**: BFS ou DFS através dos estados avaliados
- **Backtracking**: se um ramo leva a beco sem saída, voltar e tentar outro
- **Fonte**: Yao et al., NeurIPS 2023 (arXiv:2305.10601)

**Diagrama**: `12-Diagrams/ETHAGT04/tot-search-tree.mmd`
**Tempo**: 4 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: ToT é a generalização de CoT para uma árvore. Em vez de um caminho linear de pensamentos, você explora múltiplos caminhos. Em cada nó da árvore, o LLM gera vários candidatos. Um avaliador (também LLM) pontua cada candidato. Você explora os melhores, e se chegar a um beco sem saída, volta (backtrack). É poderoso mas caro — cada nó da árvore é uma chamada de LLM.
💡 ANALOGIA: É como um xadrez. Você não joga uma sequência só — você considera várias jogadas, avalia qual é a melhor, e se uma linha não funciona, volta e tenta outra.
❓ PERGUNTA: "Em que tipo de problema ToT vale o custo?" (Resposta: problemas com espaço de busca grande e função de avaliação clara)
⚠️ ERROS COMUNS: Usar ToT para problemas simples onde CoT bastaria. ToT é 5-10x mais caro.
➡️ TRANSIÇÃO: "LATS leva isso adiante com MCTS."

---

### Slide 21 — LATS: Language Agent Tree Search

**Título**: LATS
**Objetivo**: Mostrar como LATS combina MCTS com LLMs.
**Conteúdo**:
- **Base**: Monte Carlo Tree Search (MCTS) — algoritmo de AlphaGo
- **4 fases do MCTS**:
  1. **Seleção**: escolher nó via UCT (explora vs explora)
  2. **Expansão**: gerar nova ação (LLM)
  3. **Simulação**: executar e avaliar (LLM + environment)
  4. **Backpropagation**: propagar valor para os nós ancestrais
- **Vantagem**: busca sistemática com memória de estados visitados
- **Fonte**: Zhou et al., 2024 (arXiv:2310.01757)

**Tempo**: 4 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: LATS é o estado da arte em busca agêntica. Ele pega o MCTS — o algoritmo que deu ao AlphaGo a capacidade de planejar — e adapta para LLMs. Em vez de simular partidas inteiras (como no Go), LATS usa o LLM para gerar ações e avaliar estados. A grande inovação é a backpropagation: o valor de um estado é propagado para seus ancestrais, permitindo que o agente APRENDA durante a busca qual caminho é mais promissor.
💡 ANALOGIA: É como um explorador que marca em um mapa quais trilhas já testou e qual foi o resultado. Cada nova exploração usa esse conhecimento para escolher melhor.
⚠️ ERROS COMUNS: Alunos confundem LATS com ToT. ToT é busca em árvore simples (BFS/DFS). LATS é MCTS — com UCT, backpropagation e valor acumulado.
➡️ TRANSIÇÃO: "Mas isso tem um custo."

---

### Slide 22 — Custo vs Qualidade

**Título**: Custo vs Qualidade
**Objetivo**: Ser honesto sobre o trade-off.
**Conteúdo**:
- **ReAct**: 1 caminho × N passos = ~N chamadas
- **ToT**: árvore de profundidade D com branching B = ~B^D chamadas
- **LATS**: M+s iterações × simulações = ~(M+s)×k chamadas
- **Exemplo numérico**: problema com D=3, B=3 → ToT = 27 nós. LATS com 5 simulações = ~15+ nós.
- **Quando vale**: problema difícil (GSM8K hard, GAIA, SWE-bench) onde acertar vale mais que economizar

**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: ToT e LATS são caros. ToT com branching factor 3 e profundidade 3 = 27 chamadas de LLM. LATS com 5 iterações e 3 simulações cada = 15+ chamadas. Em produção, isso pode significar $0.50-$1.00 por execução. Vale quando o problema é difícil o suficiente para justificar. Não vale para "qual é a capital da França".
💡 ANALOGIA: É como cirurgia vs consulta. Cirurgia custa 100x mais que consulta, mas você não faz cirurgia para tratar um resfriado.
➡️ TRANSIÇÃO: "Vamos ver na prática."

---

### Slide 23 — DEMO: ToT em Ação

**Título**: DEMO: ToT
**Objetivo**: Demo ao vivo de ToT resolvendo um problema.
**Conteúdo**:
- Problema: jogo dos 24 (24-game) ou raciocínio matemático
- Mostrar: geração de candidatos, avaliação, backtracking
- Trace com árvore visual

**Tempo**: 5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Demo ao vivo. Vou rodar ToT em um problema matemático. Prestem atenção em três coisas: (1) como o LLM gera múltiplos candidatos em cada nó; (2) como o avaliador pontua cada um; (3) como o backtracking acontece quando um ramo falha. Se a API falhar, tenho screenshot do trace.
➡️ TRANSIÇÃO: "Vamos ao intervalo e voltamos com Reflexion."

---

### Slide 24 — [SEÇÃO] Reflexion

**Tipo**: Seção
**Tempo**: 0.5 min

---

*(Continua na Parte 2 — Slides 46-90)*
