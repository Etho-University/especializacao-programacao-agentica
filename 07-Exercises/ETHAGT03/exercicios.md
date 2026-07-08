# ETHAGT03 — Lista de Exercícios

> Curso: Padrões de Workflow Agêntico. Fixação de conceitos. Use a apostila `04-Apostilas/ETHAGT03/apostila.md` como referência.

## Múltipla escolha

**1. No padrão Prompt Chaining, o que é um "gate programático"?**

a) Um modelo de ML separado que valida a saída
b) Um checkpoint determinístico (código) entre etapas LLM que valida, classifica ou filtra antes de prosseguir
c) Um tipo de tool
d) Um mecanismo de cache

**2. Qual é a diferença fundamental entre Parallelization e Orchestrator-Workers?**

a) Parallelization usa mais modelos; Orchestrator-Workers usa menos
b) Em Parallelization as subtarefas são pré-definidas; em Orchestrator-Workers são determinadas dinamicamente pelo LLM
c) Parallelization é síncrono; Orchestrator-Workers é assíncrono
d) Não há diferença

**3. No padrão Evaluator-Optimizer, a condição de parada típica é:**

a) Sempre executar exatamente 3 iterações
b) Parar por score atingido, máximo de iterações, ou delta estagnado
c) Parar quando o usuário intervir
d) Nunca parar (loop infinito)

**4. Em Routing por modelo, o critério típico de decisão é:**

a) O tamanho do prompt
b) A complexidade da tarefa (modelo rápido para fácil, modelo potente para difícil)
c) O número de tools disponíveis
d) O custo do token

## Verdadeiro ou Falso (justificado)

**1.** "Orchestrator-workers é sempre melhor que parallelization." — Justifique.

**2.** "Voting (executar a mesma tarefa N vezes e agregar) é preferível a Sectioning quando há alta variabilidade nas respostas." — Justifique.

**3.** "Um gate programático em prompt chaining pode ser uma simples validação de formato (não-LLM)." — Justifique.

**4.** "Combinar workflows (ex.: routing → parallelization → evaluator-optimizer) sempre vira um agente." — Justifique.

## Código curto

**1.** Escreva o pseudocódigo de um workflow Prompt Chaining com gate para tradução: traduzir → gate (validar idioma detectado) → revisar.

**2.** Escreva o pseudocódigo de um Evaluator-Optimizer com condição de parada (score ≥ threshold OU max_iters).

**3.** Escreva o pseudocódigo de um Voting com N=3 e agregação por maioria (para classificação).

## Análise de trade-off

**1.** Compare Prompt Chaining vs. Routing para responder tickets de suporte. Quando escolher cada?

**2.** Compare Sectioning vs. Voting em termos de custo e qualidade. Quando cada brilha?

**3.** Para um cenário de "síntese de relatório a partir de múltiplas fontes", qual workflow composto você escolheria? Justifique.

## Debug / diagnóstico

**1.** Um workflow evaluator-optimizer roda 20 iterações sem convergir. Liste 3 hipóteses de causa e correções.

**2.** Em um parallelization sectioning, um dos 3 workers retorna erro intermitente. Como o reducer deve lidar com isso sem quebrar o pipeline inteiro?
