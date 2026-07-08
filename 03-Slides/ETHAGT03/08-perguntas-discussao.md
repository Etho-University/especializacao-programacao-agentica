# ETHAGT03 — Perguntas para Discussão

> Perguntas para estimular debate durante e após a aula.
> Organizadas por profundidade: rápida (1-2 min) → média (3-5 min) → profunda (10+ min).

---

## Perguntas Rápidas (1-2 min)

### Q1 — Comece Simples
"Em que nível da pirâmide de complexidade está o sistema de vocês hoje? E onde vocês acham que deveria estar?"
- **Objetivo**: Calibrar maturidade da turma e praticar auto-avaliação
- **Slide**: 7
- **Resposta esperada**: A maioria está em Nível 0-1 achando que está em Nível 3. O gap entre percepção e realidade é comum.

### Q2 — Padrão Mais Usado
"Qual dos 5 padrões vocês mais usam em produção hoje? E qual nunca usaram?"
- **Objetivo**: Mapear experiência prática
- **Slide**: 9
- **Ação**: Contar mãos levantadas por padrão. Geralmente routing e prompt chaining lideram; evaluator-optimizer é o menos usado.

### Q3 — Gates na Prática
"Vocês têm gates programáticos nos pipelines de vocês hoje? Ou tudo é LLM?"
- **Objetivo**: Mostrar que a maioria confia em LLM onde código seria melhor
- **Slide**: 13
- **Resposta esperada**: <30% tem gates estruturados. A maioria usa LLM para tudo.

### Q4 — Custo de Paralelismo
"Vocês medem custo por chamada LLM em produção? Sabem quanto custa cada paralelização?"
- **Objetivo**: Motivar observabilidade de custo
- **Slide**: 29
- **Resposta esperada**: <40% mede custo por chamada. Paralelização explode custo silenciosamente.

---

## Perguntas Médias (3-5 min)

### Q5 — Router Incerto
"Se o seu router está incerto entre duas categorias (40/60), o que você faz? Manda para a mais provável? Para a robusta? Re-classifica?"
- **Objetivo**: Pensar em estratégias de desempate em routing
- **Slide**: 21
- **Resposta esperada**: Depende do custo do erro. Se falso negativo é caro (difícil→fácil), manda para robusta. Se barato, manda para a mais provável. Re-classificar com prompt mais detalhado é opção, mas adiciona latência.

### Q6 — Voting para Corrigir Viés
"Você tem um modelo com viés conhecido (ex.: sempre prefere respostas longas). Voting ajuda?"
- **Objetivo**: Diferenciar variância de viés
- **Slide**: 26
- **Resposta esperada**: NÃO. Voting corrige variância (aleatoriedade), não viés (erro sistemático). Se todos os N modelos têm o mesmo viés, a maioria reforça. Para viés, calibre o prompt ou use rubric.

### Q7 — Quando Workflow Vira Agente
"Descrevam um sistema de vocês que começou como workflow e virou agente (ou deveria). O que mudou?"
- **Objetivo**: Aplicar a fronteira do Slide 49 a casos reais
- **Slide**: 49
- **Ação**: Deixar 1-2 alunos compartilharem. Sinal de transição: "depende do que acontecer no step anterior".

### Q8 — Custo do Evaluator-Optimizer
"Seu evaluator-optimizer roda 5 iterações em média. Cada iteração = generator + evaluator = 2 chamadas. Com 1000 usuários/dia, quantas chamadas/dia? E se você cortar para max 3 iters?"
- **Objetivo**: Praticar cálculo de custo de loops
- **Slide**: 44
- **Cálculo**: 5 iters × 2 chamadas × 1000 = 10.000 chamadas/dia. Cortando para 3: 6.000 chamadas/dia (40% redução). Em $0.01/chamada: $100/dia → $60/dia.

---

## Perguntas Profundas (10+ min)

### Q9 — Workflow ou Agente para Seu Sistema?
"Para o sistema de vocês hoje: qual dos 5 workflows seria mais adequado? Ou voces precisam de agente? Justifiquem com a tabela de trade-offs."
- **Objetivo**: Aplicar o framework de decisão ao caso real deles
- **Slide**: 51
- **Dica**: Usar a tabela de trade-offs (previsibilidade, flexibilidade, custo, latência) como framework para a resposta. A justificativa deve citar restrições reais (SLA, orçamento, criticidade).

### Q10 — Composição Ideal
"Se voces fossem redesenhar o pipeline de vocês com composição de workflows, como seria? Quais camadas? Por quê?"
- **Objetivo**: Pensar em composições reais
- **Slide**: 48
- **Estrutura esperada**: Routing (classificar) → [paralelização ou chaining] → evaluator (validar). A justificativa de cada camada é o que avalia competência.

### Q11 — O Maior Risco de Orchestrator-Workers
"Qual o maior risco de usar orchestrator-workers em produção?"
- **Objetivo**: Conscientização sobre armadilhas
- **Slide**: 34
- **Resposta esperada**: O orquestrador é um LLM — pode decompor mal. Se o plano é ruim, os workers executam mal e o reducer agrega mal. Falha em cascata. Mitigação: validar o plano (gate) antes de despachar para workers.

### Q12 — Evaluator Que Diverge
"Como você detecta que seu evaluator-optimizer está divergindo (piorando em vez de melhorando)? E como corrige?"
- **Objetivo**: Debug de loops de refinamento
- **Slide**: 44
- **Resposta esperada**: Sinais: score diminui entre iterações; delta negativo; feedback contraditório entre iterações. Correções: trocar evaluator por um mais forte; simplificar a rubric; reduzir max iters; adicionar delta estagnado como critério de parada.

---

## Perguntas Bônus (para alunos avançados)

### Q13 — ReWOO vs Orchestrator-Workers Reativo
"ReWOO faz o plano 'cego' (sem reagir a resultados intermediários) e paraleliza tudo. Orchestrator-Workers reativo reagiria. Qual é melhor e quando?"
- **Objetivo**: Aprofundar com papers
- **Resposta**: ReWOO é mais rápido (paralelismo total) mas menos adaptativo (se o plano está errado, não corrige). Reativo é mais adaptativo mas mais lento (serializa para reagir). ReWOO para tarefas bem-definidas; reativo para tarefas incertas.

### Q14 — Voting com Modelos Diferentes
"Em voting, você usa o MESMO modelo N vezes ou modelos DIFERENTES? Qual a vantagem de cada?"
- **Objetivo**: Pensar em diversidade de modelos
- **Resposta**: Mesmo modelo com temperatura variada: reduz variância aleatória, barato. Modelos diferentes (ex.: GPT + Claude + Gemini): reduz viés de modelo específico, mais caro mas mais robusto. A diversidade de modelos é análoga a "ensemble" em ML clássico.

### Q15 — Quando Compor Vira Dívida Técnica
"Você tem uma composição routing → parallelization → evaluator-optimizer. Quando essa composição vira dívida técnica em vez de vantagem?"
- **Objetivo**: Pensar sobre limites de composição
- **Resposta**: Quando: (1) cada camada adiciona latência sem agregar valor mensurável; (2) o custo total excede o de um agente autônomo equivalente; (3) o número de edge cases especiais cresce (sinais do Slide 50); (4) você não consegue mais explicar o fluxo para um novo engenheiro. Composição é poderosa, mas cada camada é complexidade.
