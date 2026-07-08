# ETHAGT03 — Slides Detalhados + Notas do Professor (Parte 2: Slides 33-63)

> Universidade Etho · Especialização em Programação Agêntica
> Cada slide contém: título, objetivo, conteúdo, notas do professor, diagrama, animação, imagem, tempo.

---

## SEÇÃO F — Orchestrator-Workers (Slides 33-39 · 10 min)

---

### Slide 33 — [SEÇÃO] Orchestrator-Workers

**Título**: 5 — Orchestrator-Workers: Delegação Dinâmica
**Objetivo**: Transição visual para o quarto padrão canônico.
**Conteúdo**: Número "5" grande + "Orchestrator-Workers: Delegação Dinâmica"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "5" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Início do quarto padrão. Este é o padrão mais confundido com parallelization. A distinção chave: subtarefas DINÂMICAS vs FIXAS.
➡️ TRANSIÇÃO: "Vamos fixar essa distinção."

---

### Slide 34 — Distinção Chave vs Parallelization: Subtarefas Dinâmicas

**Título**: Distinção Chave: Subtarefas Dinâmicas
**Objetivo**: Fixar a diferença crítica entre parallelization e orchestrator-workers.
**Conteúdo**:
- **Parallelization**: subtarefas são **conhecidas a priori** (fixas)
- **Orchestrator-Workers**: subtarefas são **dinâmicas** (definidas pelo orquestrador em runtime)
- O orquestrador é um LLM que olha a tarefa e decide QUEM chamar e COMO dividir
- Sem orquestrador = parallelization; com orquestrador = orchestrator-workers

**Diagrama**: Comparação lado a lado (parallelization fixa vs dinâmica)
**Animação**: Setas mostrando a diferença — fixas pré-desenhadas vs dinâmicas surgindo
**Imagem**: Lado esquerdo: 3 caixas fixas; lado direito: caixas emergindo do input
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esta é a distinção mais importante da aula. Em parallelization, VOCÊ (desenvolvedor) sabe de antemão quais são as subtarefas. Você escreve 3 funções e roda em paralelo. Em orchestrator-workers, as subtarefas NÃO são conhecidas — elas emergem do input. Um LLM (orquestrador) olha a tarefa e decide: "para esta tarefa, preciso de 3 workers; para aquela, preciso de 5". Essa é a diferença. Se as subtarefas são fixas, use parallelization (mais simples, barato, previsível). Se são dinâmicas, use orchestrator-workers.
💡 ANALOGIA: Parallelization é como uma receita de bolo — você sabe os passos antes de começar. Orchestrator-workers é como resolver um mistério — você descobre os passos conforme investiga.
❓ PERGUNTA PARA A TURMA: "Para gerar relatório com 3 fontes fixas, qual padrão?" (Parallelization — fontes são conhecidas)
⚠️ ERROS COMUNS: Alunos usam orchestrator-workers quando as subtarefas são fixas. Isso adiciona custo (LLM de planejamento) e latência (step extra) desnecessariamente.
➡️ TRANSIÇÃO: "Vamos entender o papel do orquestrador."

---

### Slide 35 — Orquestrador: Planejar + Sintetizar

**Título**: Orquestrador: Planejar + Sintetizar
**Objetivo**: Explicar o papel duplo do orquestrador.
**Conteúdo**:
- **Fase 1 — Planejar**: LLM decompõe a tarefa em subtarefas
- **Fase 2 — Delegar**: despacha cada subtarefa para um worker
- **Fase 3 — Sintetizar**: agrega resultados dos workers em resposta final
- O orquestrador NÃO executa subtarefas — ele **coordena**
- Workers podem ser LLMs com prompts/tools especializados

**Diagrama**: Ciclo: Planejar → Delegar → [Workers] → Sintetizar
**Animação**: Ciclo percorre as 3 fases
**Imagem**: Diagrama circular com 3 fases e workers no centro
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O orquestrador tem 3 responsabilidades. Primeiro, planejar: olha a tarefa e a decompõe em subtarefas. Segundo, delegar: despacha cada subtarefa para um worker. Terceiro, sintetizar: pega os resultados dos workers e agrega em uma resposta coerente. O orquestrador NÃO executa as subtarefas — só coordena. Os workers é que fazem o trabalho. Os workers podem ser LLMs com prompts especializados (ex.: um worker pesquisa, outro resume, outro valida). Esta separação é o que torna o padrão escalável.
💡 ANALOGIA: É como um maestro. O maestro não toca instrumentos — ele coordena. Olha a partitura (planejar), indica quem entra quando (delegar), e integra os sons em uma sinfonia (sintetizar). Os músicos (workers) tocam.
⚠️ ERROS COMUNS: Alunos fazem o orquestrador executar subtarefas. Isso quebra o padrão — o orquestrador deve ser puro planejamento e síntese.
➡️ TRANSIÇÃO: "Vamos ver a arquitetura de implementação."

---

### Slide 36 — Implementação: Task-Decomposition + Workers + Reducer

**Título**: Implementação: Decomposição + Workers + Reducer
**Objetivo**: Mostrar a arquitetura de implementação.
**Conteúdo**:
- **Componente 1**: Decompositor (LLM com prompt de planejamento)
- **Componente 2**: Workers (pool de LLMs com prompts especializados)
- **Componente 3**: Reducer/Sintetizador (LLM que agrega)
- **Estado**: lista de subtarefas + resultados parciais
- Conexão com papers: Plan-and-Solve (arXiv:2305.17126), ReWOO (arXiv:2305.04091)

**Diagrama**: `12-Diagrams/ETHAGT03/orchestrator-workers.mmd`
**Animação**: Decompose → Workers disparam → Reducer agrega
**Imagem**: Flowchart com 3 componentes destacados
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A implementação tem 3 componentes. O decompositor é um LLM com um prompt de planejamento ("dada esta tarefa, liste as subtarefas necessárias"). Os workers são um pool de LLMs — cada um pode ter um prompt especializado (pesquisar, resumir, validar). O reducer é um LLM que agrega os resultados em uma resposta coerente. O estado (lista de subtarefas + resultados) é passado entre componentes. A conexão com a literatura: Plan-and-Solve (2023) mostrou que separar planejamento de execução melhora qualidade. ReWOO (2023) mostrou que um plano "cego" (sem reagir a resultados intermediários) permite paralelismo total de evidências. LLMCompiler (2023) formalizou a paralelização estruturada.
💡 ANALOGIA: É como uma empresa de consultoria. O sócio sênior (decompositor) divide o projeto em tarefas. Os consultores (workers) executam. O sócio (reducer) integra em um relatório final.
⚠️ ERROS COMUNS: Alunos não persistem o estado entre fases. Sem estado, o reducer não tem acesso aos resultados dos workers.
➡️ TRANSIÇÃO: "Vamos ver casos de uso reais."

---

### Slide 37 — Casos de Uso

**Título**: Casos de Uso
**Objetivo**: Mostrar cenários reais onde o padrão brilha.
**Conteúdo**:
- **Coding em múltiplos arquivos**: orquestrador decide quais arquivos criar/modificar
- **Search em múltiplas fontes**: orquestrador decide quais fontes consultar
- **Relatório multi-fonte**: orquestrador divide por tópico, workers pesquisam, reducer sintetiza
- Sinal de que este padrão é adequado: *"não sei quantos steps vou precisar"*

**Diagrama**: 3 mini-casos em cards
**Animação**: Cards aparecem um a um
**Imagem**: 3 cards com ícones (código, busca, relatório)
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Três casos clássicos. Primeiro, coding em múltiplos arquivos: dado um issue ("adicione login com Google"), o orquestrador decide quais arquivos criar/modificar (auth.py, config.py, tests/test_auth.py). Cada worker edita um arquivo. O reducer integra. Segundo, search em múltiplas fontes: dado uma pergunta, o orquestrador decide quais fontes consultar (web, KB, tickets anteriores). Terceiro, relatório multi-fonte: o orquestrador divide por tópico, workers pesquisam cada tópico, reducer sintetiza. O sinal comum: você NÃO sabe de antemão quantos steps ou quais workers vai precisar.
💡 ANALOGIA: É como um general em campanha. Ele não sabe de antemão quantas batalhas vai lutar — decide conforme o terreno e o inimigo. Cada batalha (worker) é diferente. No fim, integra as vitórias em uma campanha (reducer).
❓ PERGUNTA PARA A TURMA: "Pensem em um sistema de vocês: ele precisa de subtarefas fixas ou dinâmicas?" (deixar pensar)
⚠️ ERROS COMUNS: Alunos usam orchestrator-workers para problemas com passos fixos. Se você sabe os passos, parallelization é mais simples e barato.
➡️ TRANSIÇÃO: "Vamos ver código."

---

### Slide 38 — Código: Orchestrator-Workers

**Título**: Código: Orchestrator-Workers
**Objetivo**: Mostrar implementação concreta.
**Conteúdo**:
- Função `orchestrate(task)`:
  1. LLM planeja → lista de subtarefas
  2. `asyncio.gather()` despacha para workers
  3. LLM sintetiza resultados
- Snippet em Python
- Diferença do código de parallelization: o step de planejamento

```python
async def orchestrate(task):
    plan = await planner_llm("Decomponha em subtarefas", task)
    subtasks = plan["subtasks"]
    results = await asyncio.gather(
        *[worker(sub) for sub in subtasks]
    )
    return await synthesizer_llm("Integre os resultados", task, results)
```

**Diagrama**: Code block com 3 fases destacadas
**Animação**: Highlight de planner, gather, synthesizer
**Imagem**: Screenshot do VS Code
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Comparem com o código de parallelization (Slide 30). A diferença é o primeiro e o último passo. Em parallelization, as subtarefas são hardcoded. Aqui, o planner LLM as gera dinamicamente. Depois, o padrão é o mesmo: gather para paralelizar. Mas há um último passo extra: o synthesizer integra os resultados em uma resposta coerente. Esse step de síntese é crítico — sem ele, você tem N resultados soltos, não uma resposta.
💡 ANALOGIA: É como um diretor de filme. O roteiro (planner) diz quantas cenas e quais. Os operadores de câmera (workers) filmam cada cena em paralelo. O editor (synthesizer) monta o filme final.
⚠️ ERROS COMUNS: Alunos pulam o synthesizer. Resultado: N respostas fragmentadas em vez de uma resposta integrada.
➡️ TRANSIÇÃO: "Vamos quebrar um mito."

---

### Slide 39 — Exercício: V/F "Orchestrator-Workers É Sempre Melhor"

**Título**: Exercício — V/F: Orchestrator-Workers É Sempre Melhor
**Objetivo**: Quebrar o mito de que padrões mais complexos são sempre melhores.
**Conteúdo**:
- Verdadeiro ou Falso: *"Orchestrator-workers é sempre melhor que parallelization."*
- **Resposta**: Falso
- Por quê: se as subtarefas são fixas e conhecidas, parallelization é mais simples, barato e previsível
- Orchestrator-workers adiciona custo (LLM de planejamento) e latência (step extra)
- **Regra**: só use orchestrator-workers quando as subtarefas são genuinamente dinâmicas

**Diagrama**: V/F com explicação
**Animação**: "Falso" aparece em `etho-danger`, depois explicação
**Imagem**: Ícone de Falso com explicação
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esta é uma armadilha clássica de "mais complexo = melhor". Falso. Orchestrator-workers adiciona custo (uma chamada LLM extra para planejar) e latência (o step de planejamento é serial). Se as subtarefas são fixas e conhecidas, parallelization é mais simples, mais barato, mais previsível. A regra de ouro: só use orchestrator-workers quando genuinamente não sabe as subtarefas de antemão. Se sabe, use parallelization.
💡 ANALOGIA: É como escolher entre receita e improvisação. Se você tem a receita (subtarefas fixas), siga-a — é mais rápido e previsível. Improvisar (orchestrator) só quando não tem receita.
❓ PERGUNTA PARA A TURMA: "Votem: V ou F?" (a maioria acerta, mas alguns hesitam)
⚠️ ERROS COMUNS: Alunos usam orchestrator-workers por "parecer avançado". Complexidade sem necessidade é débito técnico.
➡️ TRANSIÇÃO: "Vamos ao quinto e último padrão: evaluator-optimizer."

---

## SEÇÃO G — Evaluator-Optimizer (Slides 40-46 · 10 min)

---

### Slide 40 — [SEÇÃO] Evaluator-Optimizer

**Título**: 6 — Evaluator-Optimizer: Loop de Refinamento
**Objetivo**: Transição visual para o quinto padrão canônico.
**Conteúdo**: Número "6" grande + "Evaluator-Optimizer: Loop de Refinamento"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "6" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Início do quinto e último padrão. Evaluator-optimizer é um loop: gerar, avaliar, refinar, repetir até satisfazer critério.
➡️ TRANSIÇÃO: "Vamos ver o loop."

---

### Slide 41 — O Loop: Gerar → Avaliar → Refinar

**Título**: O Loop: Gerar → Avaliar → Refinar
**Objetivo**: Apresentar a estrutura fundamental do evaluator-optimizer.
**Conteúdo**:
- **Step 1**: LLM gera saída (generator)
- **Step 2**: LLM (ou código) avalia saída contra critérios (evaluator)
- **Step 3**: Se abaixo do critério → LLM refina com feedback (optimizer)
- Loop até critério de parada
- Diferença de ReAct: aqui o loop é gerar-avaliar-refinar, não pensar-agir-observar

**Diagrama**: `12-Diagrams/ETHAGT03/evaluator-optimizer.mmd`
**Animação**: Loop animado (Gerar → Avaliar → Refinar → Gerar...)
**Imagem**: Flowchart com loop circular destacado
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A estrutura é um loop. O generator produz uma primeira versão. O evaluator avalia contra critérios objetivos. Se passou, entrega. Se não passou, o optimizer refina com o feedback do evaluator. Repete até satisfazer o critério de parada. A diferença de ReAct (ETHAGT01): ReAct é pensar-agir-observer no ambiente. Aqui é gerar-avaliar-refinar contra critério interno. Não há ambiente externo — o feedback vem do próprio LLM avaliador. Isso é poderoso quando bem calibrado e perigoso quando mal calibrado.
💡 ANALOGIA: É como um escritor com um editor. O escritor (generator) escreve um rascunho. O editor (evaluator) avalia contra critérios (estrutura, clareza, tom). Se insuficiente, o escritor revisa com o feedback. Repetem até o editor aprovar.
⚠️ ERROS COMUNS: Alunos confundem evaluator-optimizer com ReAct. ReAct age no ambiente; evaluator-optimizer avalia contra critério interno. Diferentes propósitos.
➡️ TRANSIÇÃO: "Mas quando esse padrão vale a pena?"

---

### Slide 42 — Quando Tem Valor

**Título**: Quando Tem Valor
**Objetivo**: Ensinar a identificar quando este padrão é adequado.
**Conteúdo**:
- **Condição 1**: feedback é articulável (LLM consegue explicar o que está errado)
- **Condição 2**: LLM consegue avaliar (existe critério objetivo ou near-objetivo)
- **Condição 3**: iteração melhora resultado (nem sempre — às vezes o modelo trava)
- Quando NÃO usar: se o evaluator não é melhor que o generator, o loop não converge
- Exemplo que funciona: tradução literária (feedback sobre tom, ritmo, fidelidade)
- Exemplo que não funciona: "seja mais criativo" (feedback não-articulável)

**Diagrama**: Checklist de 3 condições
**Animação**: Cada condição aparece com check verde ou X vermelho
**Imagem**: Checklist com 3 itens
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Três condições devem ser verdadeiras. Primeiro, o feedback deve ser articulável: o evaluator consegue explicar O QUE está errado ("a tradução perde o ritmo na 3ª estrofe"), não só QUE está errado ("não gostei"). Segundo, o LLM consegue avaliar: existe um critério objetivo (a resposta cita 3 fontes? tem menos de 500 palavras?). Terceiro, a iteração melhora o resultado: às vezes o modelo trava e refinar piora. Se o evaluator é FRACO (não consegue avaliar melhor que o generator), o loop diverge — cada iteração piora.
💡 ANALOGIA: É como aprender piano com professor. Se o professor diz "toque com mais sentimento" (não-articulável), você não melhora. Se diz "diminua o tempo na 3ª compasso" (articulável), você melhora. O evaluator precisa ser o bom professor.
⚠️ ERROS COMUNS: Alunos usam evaluator-optimizer com feedback vago ("melhore a resposta"). Sem feedback articulável, o loop não converge.
➡️ TRANSIÇÃO: "Vamos estruturar critérios."

---

### Slide 43 — Critérios Claros e Mensuráveis

**Título**: Critérios Claros e Mensuráveis
**Objetivo**: Mostrar como estruturar critérios de avaliação.
**Conteúdo**:
- Critério vago: "a resposta é boa" → não converge
- Critério claro: "a resposta cita ≥3 fontes, tem ≤500 palavras, e inclui uma recomendação"
- **Rubric estruturada**: dimensão → escala → descrição por nível
- LLM-as-judge com rubric > LLM-as-judge sem rubric
- Exemplo de rubric para tradução: fidelidade (1-5), fluência (1-5), terminologia (1-5)

**Diagrama**: Tabela de rubric exemplo
**Animação**: Rubric preenche linha por linha
**Imagem**: Tabela 3×5 com níveis coloridos
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A qualidade do evaluator-optimizer depende da qualidade dos critérios. Critério vago ("seja bom") não converge — o evaluator não sabe o que medir. Critério claro (cite 3 fontes, <500 palavras, inclua recomendação) é verificável. A melhor estrutura é uma rubric: dimensões (fidelidade, fluência, terminologia), escala (1-5), descrição por nível (nível 5 = "tradução preserva tom e ritmo; nível 1 = "tradução literal perde nuance"). LLM-as-judge com rubric é significativamente mais consistente que sem rubric. A rubric transforma subjetividade em estrutura.
💡 ANALOGIA: É como a rubric de correção de redação do ENEM. Sem rubric, cada corretor dá nota diferente. Com rubric (competências 1-5, níveis 0-200), a correção é mais consistente.
⚠️ ERROS COMUNS: Alunos usam critérios sem escala. "Bom/médio/ruim" é frágil. Sempre dar escala numérica (1-5) e descrição por nível.
➡️ TRANSIÇÃO: "Mas quando parar o loop?"

---

### Slide 44 — Convergência: Parar por Score, Max Iters, ou Delta Estagnado

**Título**: Convergência: Critérios de Parada
**Objetivo**: Ensinar a definir critérios de parada do loop.
**Conteúdo**:
- **Critério 1 — Score**: parar quando score ≥ threshold (ex.: 4.5/5)
- **Critério 2 — Max iters**: parar após N iterações (ex.: 5) — orçamento
- **Critério 3 — Delta estagnado**: parar se score não melhora por 2 iterações consecutivas
- Sempre usar ≥2 critérios (score OU max iters, no mínimo)
- Custo: cada iteração = generator + evaluator = 2× chamadas

**Diagrama**: Gráfico de convergência (score vs iteração) com 3 linhas de parada
**Animação**: Curva de score cresce e atinge platô; linhas de parada aparecem
**Imagem**: Gráfico com eixos "iteração" e "score"
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Três critérios de parada. Score: para quando atinge o threshold (4.5/5) — qualidade desejada. Max iters: para após N iterações (5) — orçamento. Delta estagnado: para se o score não melhora por 2 iterações — evita gastar orçamento em platô. Sempre use pelo menos 2: score OU max iters. Sem max iters, o loop pode rodar indefinidamente (custo explode). Sem score, o loop para por orçamento mas talvez antes da qualidade ideal. O delta estagnado é bônus: detecta que o modelo "travou" e para cedo. Custo: cada iteração são 2 chamadas (generator + evaluator).
💡 ANALOGIA: É como treinar para uma maratona. Score = correr 42km (meta). Max iters = treinar 12 semanas (orçamento de tempo). Delta estagnado = se o tempo não melhora por 2 semanas, pare de forçar (platô).
⚠️ ERROS COMUNS: Alunos usam só score. Sem max iters, o loop explode em custo. Sempre combinar critérios.
➡️ TRANSIÇÃO: "Vamos ver código."

---

### Slide 45 — Código: Evaluator-Optimizer

**Título**: Código: Evaluator-Optimizer
**Objetivo**: Mostrar implementação concreta do loop.
**Conteúdo**:
- Função `evaluate_optimize(task, max_iters, threshold)`:
  1. Generator: LLM gera saída
  2. Evaluator: LLM avalia com rubric → score + feedback
  3. Condição de parada: score ≥ threshold OU iter ≥ max_iters OU delta < epsilon
  4. Optimizer: LLM refina com feedback
- Snippet em Python

```python
def evaluate_optimize(task, max_iters=5, threshold=4.5):
    output = generator(task)
    prev_score = 0
    for i in range(max_iters):
        result = evaluator(output, rubric=RUBRIC)
        if result["score"] >= threshold:
            return output
        if abs(result["score"] - prev_score) < 0.1:
            return output
        output = optimizer(task, output, result["feedback"])
        prev_score = result["score"]
    return output
```

**Diagrama**: Code block com loop destacado
**Animação**: Highlight das condições de parada
**Imagem**: Screenshot do VS Code
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vejam as 3 condições de parada no código. Primeira: score ≥ threshold (qualidade). Segunda: iter ≥ max_iters (orçamento). Terceira: delta < 0.1 (estagnação — score não melhora). O optimizer recebe o output atual e o feedback do evaluator, e produz uma versão melhorada. O loop é claro e defensável. Em produção, loguem cada iteração (score, feedback) para debugar convergência.
💡 ANALOGIA: É como o ciclo de code review. Você envia PR (generator). Revisor avalia (evaluator). Se rejeita com comentários, você revisa (optimizer). Repete até aprovar ou atingir limite de revisões.
⚠️ ERROS COMUNS: Alunos não logam o histórico de scores. Sem log, você não sabe se o loop está convergindo ou divergindo.
➡️ TRANSIÇÃO: "Vamos praticar."

---

### Slide 46 — Exercício: Condição de Parada para Tradução Literária

**Título**: Exercício — Condição de Parada para Tradução Literária
**Objetivo**: Praticar definição de critérios de parada em domínio real.
**Conteúdo**:
- Cenário: evaluator-optimizer para tradução de um poema (EN → PT-BR)
- Pergunta: *Escreva a condição de parada. Quais critérios? Qual threshold? Quantas iterações máximas?*
- Dica: tradução literária é subjetiva — como evitar loop infinito?
- Discussão em duplas (2 min), 1 min compartilhar

**Diagrama**: Caixa de discussão (`etho-warning`)
**Animação**: Caixa aparece com fade
**Imagem**: Ícone de pena e livro
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Deixem a turma pensar em duplas. O desafio é: tradução literária é subjetiva. Como definir threshold? Resposta esperada: usar rubric com múltiplas dimensões (fidelidade, fluência, ritmo, tom) cada uma 1-5. Threshold = média ≥ 4.0 (não 5 — perfeição é inatingível). Max iters = 3-4 (literário não melhora indefinidamente; depois de 3 iterações, o modelo trava). Delta estagnado = se média não melhora por 1 iteração, parar. A chave é aceitar que "bom o suficiente" é o objetivo, não "perfeito".
💡 ANALOGIA: É como polir uma escultura. As primeiras passadas dão forma (score sobe rápido). As últimas passadas mal mudam (platô). Saber parar é arte.
❓ PERGUNTA PARA A TURMA: "Compartilhem 2 respostas." (resposta-chave: threshold 4.0 não 5.0; max 3-4 iters)
⚠️ ERROS COMUNS: Alunos setam threshold=5.0 (perfeição). O loop nunca converge — perde orçamento.
➡️ TRANSIÇÃO: "Agora vamos compor os padrões."

---

## SEÇÃO H — Composições e Limites (Slides 47-51 · 8 min)

---

### Slide 47 — [SEÇÃO] Composições e Limites

**Título**: 7 — Composições e Limites
**Objetivo**: Transição visual para composição de padrões.
**Conteúdo**: Número "7" grande + "Composições e Limites"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "7" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Início do bloco de composições. Na prática, raramente usamos um padrão isolado. Combinamos. Mas a composição tem limites — e a fronteira entre workflow composto e agente é tênue.
➡️ TRANSIÇÃO: "Vamos ver a composição típica."

---

### Slide 48 — Composição Típica: Routing → Parallelization → Evaluator-Optimizer

**Título**: Composição Típica: Routing → Parallelization → Evaluator-Optimizer
**Objetivo**: Mostrar como os 5 padrões se combinam em pipelines reais.
**Conteúdo**:
- **Camada 1 — Routing**: classifica a entrada (ex.: tipo de ticket)
- **Camada 2 — Parallelization**: despacha subtarefas em paralelo (ex.: buscar FAQ + docs + histórico)
- **Camada 3 — Evaluator-Optimizer**: avalia a resposta antes de entregar
- Cada camada resolve um problema diferente
- Outras composições: prompt chaining + evaluator-optimizer; routing + orchestrator-workers

**Diagrama**: `12-Diagrams/ETHAGT03/composition-routing-parallel-evaluator.mmd`
**Animação**: Camadas surgem sequencialmente de cima para baixo
**Imagem**: Flowchart com 3 camadas coloridas
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esta é a composição mais comum em produção. Camada 1 (routing): classifica o input — técnico, billing, geral. Camada 2 (parallelization): para tickets técnicos, despacha 3 workers em paralelo (KB, web, tickets anteriores). Camada 3 (evaluator-optimizer): avalia a resposta sintetizada antes de entregar ao usuário. Cada camada resolve um problema: routing = custo (modelo certo); parallelization = latência (subtarefas em paralelo); evaluator-optimizer = qualidade (validação final). Outras composições: prompt chaining + evaluator (cadeia com loop de refinamento no final); routing + orchestrator-workers (roteia para um orchestrator quando a categoria é complexa).
💡 ANALOGIA: É como um restaurante com 3 estações. Hostess (routing) direciona para a mesa certa. Garçom (parallelization) pede entradas, pratos e bebidas em parânelo. Chef (evaluator-optimizer) prova cada prato antes de servir.
⚠️ ERROS COMUNS: Alunos compõem sem justificar. Cada camada adiciona custo e latência. Só componha se cada camada agrega valor mensurável.
➡️ TRANSIÇÃO: "Mas quando a composição vira agente?"

---

### Slide 49 — Quando Combinar Vira Agente

**Título**: Quando Combinar Vira Agente
**Objetivo**: Discutir a fronteira tênue entre workflow composto e agente.
**Conteúdo**:
- **Workflow composto**: camadas fixas, ordem predefinida, gates determinísticos
- **Agente**: o próprio LLM decide a ordem, se itera, se busca mais informação
- A linha é tênue: se o workflow tem routing + loops + branches condicionais suficientes...
- Sinal de transição: quando o workflow precisa de um "meta-step" que decide qual caminho seguir dinamicamente
- Isso é o que ETHAGT04 (Reasoning & Planning) aprofunda

**Diagrama**: Espectro: workflow puro ←→ workflow composto ←→ agente
**Animação**: Espectro preenche da esquerda
**Imagem**: Gradiente de workflow (azul) para agente (laranja)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A fronteira entre workflow composto e agente é tênue. Workflow composto: você define as camadas, a ordem, os gates. Agente: o LLM decide. Mas e quando o workflow tem routing dinâmico + loops condicionais + branches? Em algum ponto, o workflow composto SE TORNA um agente. O sinal de transição é: quando você precisa de um "meta-step" que olha o estado e decide QUAL camada executar a seguir. Isso é essencialmente o que um agente faz. A Anthropic reconhece: a distinção é mais de grau que de tipo. ETHAGT04 aprofunda reasoning e planning — a ponte entre workflow e agente.
💡 ANALOGIA: É como a diferença entre uma receita detalhada (workflow) e cozinhar "no feeling" (agente). No meio, há receitas com variações ("se o molho ficar grosso, adicione água") — isso já é semi-agêntico.
❓ PERGUNTA PARA A TURMA: "O que diferencia um workflow composto de um agente para vocês?" (debate aberto)
⚠️ ERROS COMUNS: Alunos acham que workflow composto = agente. Não. Enquanto o caminho é predefinido (mesmo com condicionais), é workflow. Quando o LLM decide o caminho, é agente.
➡️ TRANSIÇÃO: "Como saber se você está forçando workflow?"

---

### Slide 50 — Sinais de Que Você Está Forçando Workflow

**Título**: Sinais de Que Você Está Forçando Workflow
**Objetivo**: Dar checklist de quando o problema pede agente, não workflow.
**Conteúdo**:
- Você está adicionando gates cada vez mais complexos para cobrir casos especiais
- O número de branches no routing cresce sem parar
- Você precisa de "loops dentro de loops" para cobrir edge cases
- O evaluator precisa de contexto que o generator não teve acesso
- Você descreve o workflow e ouve: "depende do que acontecer no step anterior"

**Diagrama**: Checklist de "sinais de alerta" (`etho-danger`)
**Animação**: Cada sinal aparece em vermelho
**Imagem**: Ícones de alerta por sinal
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Cinco sinais de que o problema pede agente, não workflow. Primeiro: seus gates ficam tão complexos que são quase LLMs disfarçados de código. Segundo: o routing tem 20 categorias e cresce toda semana. Terceiro: você aninha loops (loop dentro de loop) para cobrir edge cases. Quarto: o evaluator precisa de contexto que o generator não teve — o que significa que o workflow está particionado artificialmente. Quinto: quando você descreve o fluxo, a frase mais comum é "depende do que acontecer no step anterior". Esses são sinais de que o problema é inerentemente dinâmico e pede agente.
💡 ANALOGIA: É como tentar dirigir um carro só com marchas pré-programadas. Funciona em estrada reta. Mas em trânsito caótico, você precisa de um motorista que decide — um agente.
⚠️ ERROS COMUNS: Alunos insistem em workflow por "previsibilidade" mesmo quando o problema é inerentemente dinâmico. Previsibilidade em problema dinâmico = ilusão.
➡️ TRANSIÇÃO: "Vamos consolidar os trade-offs."

---

### Slide 51 — Trade-offs Consolidados

**Título**: Trade-offs Consolidados
**Objetivo**: Sistematizar os trade-offs de todos os 5 padrões.
**Conteúdo**:

| Padrão | Previsibilidade | Flexibilidade | Custo | Latência |
|---|---|---|---|---|
| Prompt Chaining | Alta | Baixa | Médio | Alta (serial) |
| Routing | Alta | Média | Baixo | Baixa |
| Parallelization | Alta | Média | Alto (N×) | Baixa (max) |
| Orchestrator-Workers | Média | Alta | Alto | Média |
| Evaluator-Optimizer | Alta | Média | Alto (loop) | Alta |

**Diagrama**: Tabela 5×4 colorida por intensidade
**Animação**: Colunas preenchem com cores (verde=baixo, amarelo=médio, vermelho=alto)
**Imagem**: Tabela heatmap
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esta é a tabela mais importante do módulo. Cinco padrões em 4 eixos. Prompt chaining: previsível mas lento (serial). Routing: barato e rápido, mas flexibilidade média. Parallelization: rápido (latência = max) mas caro (N× custo). Orchestrator-workers: flexível mas menos previsível (orquestrador é LLM). Evaluator-optimizer: previsível mas caro (loop) e lento. A escolha depende das restrições do problema: se custo é prioridade, routing. Se latência, parallelization. Se flexibilidade, orchestrator-workers. Se qualidade, evaluator-optimizer. Se linearidade, prompt chaining.
💡 ANALOGIA: É como escolher transporte. Bicicleta (routing — barato, rápido, distâncias curtas). Carro (parallelization — flexível, mas combustível). Táxi (orchestrator — flexível mas caro). Avião (evaluator — rápido entre cidades mas caro). Trem (prompt chaining — rota fixa, previsível).
⚠️ ERROS COMUNS: Alunos escolhem pelo padrão "favorito". A escolha deve ser pelas restrições do problema, não pela preferência.
➡️ TRANSIÇÃO: "Vamos ao fechamento."

---

## SEÇÃO I — Fechamento (Slides 52-63 · 17 min)

---

### Slide 52 — [SEÇÃO] Fechamento

**Título**: 8 — Fechamento
**Objetivo**: Transição visual para o fechamento.
**Conteúdo**: Número "8" grande + "Fechamento"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "8" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Início do fechamento. Vamos ver um caso real, resumir, fazer quiz, exercício final, apresentar projeto e Q&A.
➡️ TRANSIÇÃO: "Vamos começar com um caso real."

---

### Slide 53 — Caso de Estudo: Coinbase / Intercom

**Título**: Caso de Estudo: Coinbase / Intercom
**Objetivo**: Mostrar os 5 padrões em um caso real de produção.
**Conteúdo**:
- Coinbase / Intercom: workflows agênticos em suporte ao cliente
- Arquitetura típica: routing (classificar ticket) → parallelization (buscar fontes) → evaluator-optimizer (validar resposta)
- Resultados: redução de tempo de resposta, escalabilidade, custo controlado
- Lição: workflow composto > agente autônomo para suporte (previsibilidade importa)
- Referência: `09-CaseStudies/`

**Diagrama**: Arquitetura do caso real
**Animação**: Arquitetura constrói camada por camada
**Imagem**: Flowchart da arquitetura Coinbase/Intercom
**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A Coinbase e a Intercom usam workflows agênticos para suporte ao cliente. A arquitetura típica é a composição que vimos no Slide 48: routing classifica o ticket, parallelization busca fontes (KB, docs, tickets anteriores), evaluator-optimizer valida a resposta. Por que workflow e não agente autônomo? Porque suporte ao cliente exige previsibilidade. Cada resposta precisa ser consistente, auditável e dentro de SLA. Um agente autônomo poderia resolver, mas com custo imprevisível e latência variável. A lição: em produção, workflow composto é geralmente melhor que agente autônomo quando previsibilidade importa.
💡 ANALOGIA: É como um call center estruturado (workflow) vs um consultor freelancer (agente). O call center é previsível, escalável, auditável. O freelancer é flexível mas imprevisível. Em suporte em escala, call center vence.
⚠️ ERROS COMUNS: Alunos acham que casos de produção usam agente autônomo. A maioria usa workflow composto. Agente é para problemas abertos.
➡️ TRANSIÇÃO: "Vamos resumir a aula."

---

### Slide 54 — Resumo da Aula

**Título**: Resumo da Aula
**Objetivo**: Sintetizar os pontos-chave.
**Conteúdo**:
- 5 padrões canônicos: prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer
- **Gates programáticos** = controle determinístico em workflows
- **Parallelization**: sectioning (independentes) vs voting (robustez)
- **Orchestrator-Workers**: subtarefas dinâmicas (vs fixas em parallelization)
- **Evaluator-Optimizer**: loop com critérios claros e convergência mensurável
- **Composição** = realidade; mas quando workflow vira agente, mude de módulo
- **Comece simples**, só aumente com evidência

**Diagrama**: 7 ícones com os pontos-chave
**Animação**: Ícones aparecem um a um
**Imagem**: 7 ícones em `etho-accent`
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Resumo dos 7 pontos-chave. 1. Os 5 padrões são a caixa de ferramentas. 2. Gates são o controle determinístico — código, não LLM. 3. Parallelization tem 2 modos: sectioning para independentes, voting para robustez. 4. Orchestrator-workers é para subtarefas DINÂMICAS (a distinção crítica). 5. Evaluator-optimizer precisa de critérios claros e condições de parada. 6. Na prática, componha — mas saiba quando vira agente. 7. Comece simples, só escale com evidência. Se lembrarem destes 7 pontos, a aula cumpriu seu objetivo.
💡 ANALOGIA: É como o decálogo do engenheiro de workflows. Sete mandamentos.
➡️ TRANSIÇÃO: "Vamos confirmar que cobrimos tudo."

---

### Slide 55 — Checklist da Aula

**Título**: Checklist da Aula
**Objetivo**: Confirmar que todos os tópicos foram cobertos.
**Conteúdo**:
- [ ] Explicou o princípio "comece simples"
- [ ] Detalhou os 5 padrões canônicos com diagramas
- [ ] Mostrou código de cada padrão
- [ ] Discutiu gates programáticos
- [ ] Comparou parallelization vs orchestrator-workers
- [ ] Apresentou critérios de convergência do evaluator-optimizer
- [ ] Discutiu composições e quando workflow vira agente

**Diagrama**: Checklist visual
**Animação**: Itens recebem check verde um a um
**Imagem**: Lista com caixas de seleção
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Checklist final. Se algum item ficou sem check, vale a pena revisitar. Em 90 minutos, nem sempre dá para aprofundar tudo. Os itens não-cobertos viram leitura recomendada ou tópico de Q&A.
➡️ TRANSIÇÃO: "Vamos ao quiz."

---

### Slide 56 — Quiz: Pergunta 1

**Título**: Quiz — Pergunta 1
**Objetivo**: Verificar compreensão.
**Conteúdo**:
- *"Qual é a diferença fundamental entre parallelization e orchestrator-workers?"*
- A) Orchestrator-workers é mais rápido
- B) Parallelization usa modelos menores
- C) Em orchestrator-workers, as subtarefas são dinâmicas (definidas em runtime)
- D) Parallelization não tem reducer
- **Resposta**: C

**Diagrama**: 4 opções com radio buttons
**Animação**: Resposta aparece após votação
**Imagem**: Card de quiz
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A resposta é C. A distinção fundamental é: parallelization tem subtarefas FIXAS (você sabe quais são); orchestrator-workers tem subtarefas DINÂMICAS (o orquestrador define em runtime). As outras opções são incorretas: A é falso (orchestrator é geralmente mais lento por ter step de planejamento); B é falso (ambos podem usar qualquer modelo); D é falso (ambos têm reducer).
➡️ TRANSIÇÃO: "Próxima pergunta."

---

### Slide 57 — Quiz: Pergunta 2

**Título**: Quiz — Pergunta 2
**Objetivo**: Verificar compreensão.
**Conteúdo**:
- *"O que é um gate em prompt chaining?"*
- A) Um modelo LLM que decide se continua
- B) Um checkpoint programático (código) que valida a saída antes do próximo step
- C) Um tipo de prompt especial
- D) Um framework de orquestração
- **Resposta**: B

**Diagrama**: 4 opções com radio buttons
**Animação**: Resposta aparece após votação
**Imagem**: Card de quiz
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A resposta é B. Gate é CÓDIGO (determinístico), não LLM. Se fosse LLM, seria evaluator-optimizer. Gate valida estruturalmente (schema, formato, regras) antes do próximo step. A é a armadilha clássica — alunos confundem gate com evaluator.
➡️ TRANSIÇÃO: "Próxima."

---

### Slide 58 — Quiz: Pergunta 3

**Título**: Quiz — Pergunta 3
**Objetivo**: Verificar compreensão.
**Conteúdo**:
- *"Quando o evaluator-optimizer NÃO vale a pena?"*
- A) Quando o feedback é articulável e o LLM consegue avaliar
- B) Quando o evaluator não é melhor que o generator
- C) Quando há orçamento para múltiplas iterações
- D) Quando a tarefa tem critérios objetivos
- **Resposta**: B

**Diagrama**: 4 opções com radio buttons
**Animação**: Resposta aparece após votação
**Imagem**: Card de quiz
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A resposta é B. Se o evaluator não é melhor que o generator, o loop diverge — cada iteração piora em vez de melhorar. As outras opções são quando VALE a pena: A (feedback articulável), C (orçamento), D (critérios objetivos).
➡️ TRANSIÇÃO: "Última pergunta do quiz."

---

### Slide 59 — Quiz: Pergunta 4

**Título**: Quiz — Pergunta 4
**Objetivo**: Verificar compreensão.
**Conteúdo**:
- *"Em routing por modelo, qual é o erro mais caro?"*
- A) Enviar tarefa fácil para modelo forte (Sonnet)
- B) Enviar tarefa difícil para modelo fraco (Haiku)
- C) Usar o mesmo modelo para todas as categorias
- D) Ter apenas 2 categorias
- **Resposta**: B

**Diagrama**: 4 opções com radio buttons
**Animação**: Resposta aparece após votação
**Imagem**: Card de quiz
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A resposta é B. Enviar tarefa difícil para modelo fraco gera resposta RUIM (prejudica qualidade). A é apenas ineficiência (custo extra, mas resposta boa). O erro mais caro em routing é o falso negativo: classificar difícil como fácil.
➡️ TRANSIÇÃO: "Vamos ao exercício final."

---

### Slide 60 — Exercício: Escolha o Workflow (5 Cenários)

**Título**: Exercício — Escolha o Workflow
**Objetivo**: Praticar a decisão de padrão em cenários reais.
**Conteúdo**:
- 5 cenários:
  1. Tradução com revisão de qualidade → Prompt Chaining + Evaluator-Optimizer
  2. Análise de sentimentos de 10.000 tweets → Routing (por idioma) + Parallelization (sectioning)
  3. Geração de relatório com múltiplas fontes → Orchestrator-Workers
  4. Chatbot de FAQ simples → Routing
  5. Correção de redação com feedback → Evaluator-Optimizer
- Em grupos: indicar workflow + justificar
- 3 min discussão, 2 min compartilhar

**Diagrama**: 5 cards com cenários
**Animação**: Cards aparecem um a um
**Imagem**: 5 cards coloridos
**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Este é o exercício de consolidação. Cada cenário tem um workflow mais adequado. 1: tradução com revisão = prompt chaining (traduzir → gate → revisar) + evaluator-optimizer (refina até critério). 2: 10.000 tweets = routing (por idioma) + parallelization sectioning (cada tweet em paralelo). 3: relatório multi-fonte = orchestrator-workers (fontes dinâmicas). 4: FAQ simples = routing (classifica pergunta, despacha para handler). 5: correção com feedback = evaluator-optimizer (gera, avalia contra rubric, refina). A chave é a JUSTIFICATIVA — por que este padrão e não outro?
💡 ANALOGIA: É como um diagnóstico médico. Cada sintoma (cenário) pede um tratamento (workflow) diferente. O bom médico justifica.
❓ PERGUNTA PARA A TURMA: "Compartilhem 2 grupos com justificativas." (avaliar profundidade da justificativa)
⚠️ ERROS COMUNS: Alunos escolhem orchestrator-workers para tudo ("parece avançado"). A justificativa deve ser baseada nas restrições do problema.
➡️ TRANSIÇÃO: "Vamos ao projeto."

---

### Slide 61 — Projeto do Módulo + Labs

**Título**: Projeto do Módulo + Labs
**Objetivo**: Apresentar o projeto e laboratórios.
**Conteúdo**:
- **Projeto**: síntese de relatório a partir de múltiplas fontes
  - Projetar e implementar workflow composto
  - Comparar 2 abordagens (ex.: prompt chaining vs orchestrator-workers)
  - Entrega: código + benchmark + ADR justificando escolha
  - Critério: ADR coerente; medições em ≥20 casos
- **Lab 1 (5h)**: "Os 5 em 1 dia" — versões mínimas dos 5 workflows em domínio comum
- **Lab 2 (5h)**: "Composição" — routing → parallelization (3 workers) → evaluator-optimizer

**Diagrama**: Cards do projeto e labs
**Animação**: Cards aparecem em sequência
**Imagem**: 3 cards (projeto + 2 labs)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O projeto é a entrega principal. Vocês recebem uma tarefa de síntese de relatório (múltiplas fontes). Projetam o workflow mais adequado. Implementam. Mas o coração do projeto é a COMPARAÇÃO: implementem 2 abordagens (ex.: prompt chaining vs orchestrator-workers), meçam em ≥20 casos, e escrevam um ADR (Architecture Decision Record) justificando a escolha. O ADR é o que vale — código que funciona é pré-requisito, mas a JUSTIFICATIVA é o que avalia competência. Os labs são preparatórios: Lab 1 implementa os 5 workflows isoladamente; Lab 2 compõe.
💡 ANALOGIA: É como uma defesa de tese. O código é a tese (precisa existir). O ADR é a defesa (precisa convencer).
⚠️ ERROS COMUNS: Alunos focam só no código. O ADR é 40% da nota. Sem medições (≥20 casos), o ADR é opinião, não engenharia.
➡️ TRANSIÇÃO: "Vamos ver conexões e referências."

---

### Slide 62 — Conexão com Próximos Módulos + Referências

**Título**: Conexão com Próximos Módulos + Referências
**Objetivo**: Mostrar conexões e indicar leitura.
**Conteúdo**:
- **ETHAGT04** — Reasoning & Planning: quando workflow não basta, entra raciocínio avançado
- **ETHAGT09** — Multi-Agente: workflows como fundação de orquestração multi-agente
- **ETHAGT10** — Orquestração: composições em escala
- Leitura obrigatória: Anthropic, *Building Effective Agents* (2024)
- Papers: arXiv:2305.17126 (Plan-and-Solve), arXiv:2305.04091 (ReWOO), arXiv:2310.01757 (LLMCompiler)
- Vídeo: Schluntz & Albert, *Building more effective AI agents* (YouTube)

**Diagrama**: Mapa da especialização com ETHAGT03 destacado
**Animação**: ETHAGT03 pulsa, conexões para ETHAGT04/09/10 se acendem
**Imagem**: Mind map da especialização
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: ETHAGT03 é fundação para 3 módulos. ETHAGT04 aprofunda reasoning e planning — quando workflow não basta e você precisa de agente com reflexão. ETHAGT09 expande para multi-agente — orchestrator-workers é proto-multi-agente. ETHAGT10 formaliza orquestração em escala. Leitura obrigatória: Anthropic Building Effective Agents (a fonte dos 5 padrões). Papers: Plan-and-Solve (decomposição), ReWOO (plano cego + paralelismo), LLMCompiler (paralelização estruturada). Vídeo: Schluntz e Albert apresentando ao vivo.
➡️ TRANSIÇÃO: "Vamos ao Q&A."

---

### Slide 63 — Q&A / Encerramento

**Título**: Perguntas?
**Objetivo**: Abrir para perguntas e encerrar.
**Conteúdo**:
- "Perguntas?"
- Contato do professor
- "Na próxima aula: ETHAGT04 — Reasoning & Planning"

**Diagrama**: Logo Etho + fundo `etho-dark`
**Animação**: Fade in
**Imagem**: Logo Etho centralizado
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Abrir para Q&A. Se não houver perguntas: "Qual parte foi menos clara?" Mensagem final: "Os 5 padrões são a caixa de ferramentas. A escolha certa é o que diferencia engenharia de tentativa-e-erro. Pratiquem no Lab 1 — implementar os 5 em um dia é a melhor forma de fixar."
➡️ TRANSIÇÃO: Fim da aula.

---
