---
password: Etho-Prof-2026
---
# ETHAGT04 — Gabarito

> Restrito a mentores. Cada resposta justificada com referência à apostila.

## Múltipla escolha

1. **b)** — ReWOO planeja todas as etapas primeiro (plano "cego") e coleta evidências em paralelo, reduzindo os tokens de raciocínio intermediário que ReAct gasta a cada iteração do loop (Capítulo 2 — Plan-and-Execute e ReWOO).

2. **b)** — A memória de erros armazena reflexões sobre falhas anteriores (auto-crítica), permitindo que o agente evite repetir os mesmos erros em tentativas subsequentes (Capítulo 4 — Reflexion).

3. **a)** — ToT explora múltiplos caminhos de raciocínio em árvore, avaliando estados intermediários antes de prosseguir, ao contrário do CoT linear que segue um único caminho (Capítulo 3 — Tree of Thoughts e LATS).

4. **b)** — Reasoning models têm o raciocínio treinado/integrado (inference-time reasoning nativo), não adicionado via prompt. O modelo "pensa" internamente sem precisar de instruções CoT explícitas (Capítulo 6 — Inference-Time Reasoning nativo).

## Verdadeiro ou Falso (justificado)

1. **Falso.** Self-Discover é vantajoso quando o problema é tão novo que não há padrão pronto, permitindo que o agente compõe sua própria estratégia. Em problemas conhecidos, CoT ou padrões específicos podem ser mais eficientes e baratos (Capítulo 5 — Self-Discover).

2. **Verdadeiro.** ReWOO separa planejamento (uma chamada) de execução (paralela), evitando incluir thought/observation no contexto a cada passo do loop como ReAct faz, reduzindo tokens totais (Capítulo 2.3 — ReWOO).

3. **Verdadeiro.** LATS usa MCTS (Monte Carlo Tree Search) com LLM, permitindo backtracking — abandonar caminhos que o avaliador classifica como improdutivos e explorar alternativas (Capítulo 3.2 — LATS).

4. **Parcialmente verdadeiro.** Reasoning models reduzem ou eliminam a necessidade de CoT promptado para raciocínio interno, mas o design do agente muda (mais tools, orçamento de tokens maior, sem necessidade de instruir "pense passo a passo") (Capítulo 6.2).

## Código curto

1. **Memória de Reflexion:**
```python
def reflexion_agent(task, max_attempts=3):
    reflections = []  # memória de erros
    for attempt in range(max_attempts):
        prompt = f"Tarefa: {task}\nErros anteriores:\n{reflections}\nEvite repeti-los."
        result = llm_solve(prompt)
        if is_correct(result):
            return result
        critique = llm(f"Por que esta resposta falhou? {result}")
        reflections.append(critique)
    return result
```
Referência: Capítulo 4 (Reflexion).

2. **Plan-and-Execute:**
```python
def plan_and_execute(task):
    plan = llm(f"Crie um plano de passos para: {task}")  # planner
    steps = parse_steps(plan)
    results = []
    for step in steps:
        result = execute(step)              # executor
        results.append(result)
    return llm(f"Sintetize a resposta: {results}")  # síntese
```
Referência: Capítulo 2 (Plan-and-Execute).

3. **Orçamento de tokens:**
```python
def agent_with_budget(task, budget=10000):
    total = 0
    while total < budget:
        response = llm(task)
        total += count_tokens(response)
        if is_done(response):
            return response
    return "Budget exceeded"
```
Referência: Capítulo 7 (Orçamento de tokens/passos).

## Análise de trade-off

1. **ReAct vs. Plan-and-Execute:** ReAct é melhor para tarefas onde o próximo passo depende da observação do anterior (adaptabilidade). Plan-and-Execute é melhor quando a estrutura é previsível e o planejamento antecipado economiza tokens (Capítulo 2 e Lab 1).

2. **ToT vs. reasoning model nativo:** Reasoning models nativos (o1/o3) internalizam exploração de alternativas, substituindo ToT em muitos casos. ToT ainda é preferível quando é necessário controle explícito sobre a árvore de exploração, funções de avaliação customizadas, ou quando não se tem acesso a reasoning models (Capítulo 6.3).

3. **Estratégias por classe de problema:**
   - **Matemática:** Self-Consistency ou reasoning model nativo (múltiplas amostras + agregação reduz erro).
   - **Código:** ReAct ou Plan-and-Execute (necessita iteração com execução/teste).
   - **Decisão aberta:** Reflexion ou Self-Discover (aprendizado com falhas; composição de estratégia).
   Referência: Capítulos 1-7.

## Debug / diagnóstico

1. **Falta de re-planejamento:** O executor falha mas não sinaliza ao planner. Correção: ao detectar falha no passo, acionar re-planejamento supervisionado — o planner recebe os passos concluídos + o erro e gera um plano revisado para os passos restantes (Capítulo 2.4 e Capítulo 7.3).

2. **Diagnóstico:** A função de avaliação de estados não está discriminando entre caminhos (retorna scores iguais ou o seletor sempre pega o primeiro sem avaliação). Correção: implementar um avaliador que produz scores diferenciados com base em critérios claros, e usar seleção greedy ou MCTS adequada (Capítulo 3.2).
