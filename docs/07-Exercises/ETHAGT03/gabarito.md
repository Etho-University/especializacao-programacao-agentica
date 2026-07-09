---
password: Etho-Prof-2026
---
# ETHAGT03 — Gabarito

> Restrito a mentores. Cada resposta justificada com referência à apostila.

## Múltipla escolha

1. **b)** — Um gate programático é um checkpoint determinístico (código, não LLM) entre etapas LLM que valida, classifica ou filtra antes de prosseguir (Capítulo 2 — Prompt Chaining).

2. **b)** — Em Parallelization as subtarefas são pré-definidas (estáticas); em Orchestrator-Workers, o orquestrador (LLM) determina dinamicamente as subtarefas com base no problema (Capítulo 5 — Orchestrator-Workers).

3. **b)** — A condição de parada típica combina: score atingir threshold, máximo de iterações, ou delta estagnado (sem melhoria entre iterações) (Capítulo 6 — Evaluator-Optimizer).

4. **b)** — Routing por modelo usa a complexidade da tarefa para escolher entre modelo rápido (Haiku, para fácil) e modelo potente (Sonnet, para difícil) (Capítulo 3 — Routing).

## Verdadeiro ou Falso (justificado)

1. **Falso.** Orchestrator-Workers adiciona custo e latência (o orquestrador é uma chamada LLM extra). Parallelization é mais barato e previsível quando as subtarefas são conhecidas a priori. Orchestrator-Workers só supera quando as subtarefas são dinâmicas e não podem ser pré-determinadas (Capítulo 5.1).

2. **Verdadeiro.** Voting reduz variabilidade ao agregar múltiplas execuções da mesma tarefa. Quando há alta variabilidade, voting aumenta confiança. Sectioning é melhor quando há subtarefas genuinamente independentes (Capítulo 4.2).

3. **Verdadeiro.** Um gate pode ser código puro — ex.: verificar se o texto está no idioma esperado via biblioteca de detecção, sem LLM. Gates determinísticos são preferidos por custo e previsibilidade (Capítulo 2.2).

4. **Falso.** Composições de workflows continuam sendo workflows enquanto o fluxo de controle é predefinido em código. Só vira agente quando o LLM passa a dirigir dinamicamente o fluxo (Capítulo 7 — Composições e limites).

## Código curto

1. **Prompt Chaining com gate:**
```python
def translate_chain(text, target_lang):
    draft = llm(f"Translate to {target_lang}: {text}")
    detected = detect_language(draft)           # gate programático
    if detected != target_lang:
        return llm(f"Fix this translation to {target_lang}: {draft}")
    return llm(f"Review and polish: {draft}")    # etapa de revisão
```
Referência: Capítulo 2 (Prompt Chaining).

2. **Evaluator-Optimizer:**
```python
def evaluator_optimizer(task, threshold=0.85, max_iters=5):
    output = llm(task)
    for i in range(max_iters):
        score = evaluate(output, task)
        if score >= threshold:
            return output
        output = llm(f"Improve based on feedback (score={score}): {output}")
    return output  # best effort
```
Referência: Capítulo 6 (Evaluator-Optimizer).

3. **Voting:**
```python
def voting_classify(text, n=3):
    votes = [llm_classify(text) for _ in range(n)]
    return max(set(votes), key=votes.count)  # maioria
```
Referência: Capítulo 4.2 (Voting).

## Análise de trade-off

1. **Prompt Chaining vs. Routing:** Prompt Chaining é melhor quando o processo é linear e previsível (etapas fixas). Routing é melhor quando diferentes tipos de ticket exigem tratamento diferente — um classificador inicial encaminha ao ramo adequado. Routing adiciona custo de classificação mas melhora qualidade em domínios heterogêneos (Capítulos 2 e 3).

2. **Sectioning vs. Voting:** Sectioning executa subtarefas independentes em paralelo (ex.: extrair 3 aspectos de um documento) — custo N×1, sem redundância. Voting executa a mesma tarefa N vezes e agrega — custo N×1 mas com redundância para reduzir variância. Sectioning brilha com tarefas decomponíveis; Voting brilha com tarefas de alta incerteza (Capítulo 4).

3. **Workflow composto para síntese:** Routing → Orchestrator-Workers → Evaluator-Optimizer. Routing classifica o tipo de pergunta; Orchestrator-Workers decompõe em subtarefas de busca (múltiplas fontes dinamicamente); Evaluator-Optimizer refina o relatório até atender critérios de qualidade (Capítulo 7).

## Debug / diagnóstico

1. **Causas de não convergência:**
   - **Critério de avaliação ambíguo:** o evaluator não tem critérios mensuráveis claros. Correção: definir rubrica estruturada.
   - **Feedback não acionável:** o evaluator diz "melhore" sem orientação específica. Correção: exigir feedback articulável.
   - **Threshold inalcançável:** score alvo é irrealista. Correção: revisar threshold ou adicionar delta estagnado como condição de parada.
   Referência: Capítulo 6 (Evaluator-Optimizer).

2. **Reducer com erro intermitente:** O reducer deve ter tolerância a falhas — aceitar resultados parciais (2 de 3 workers), logar o erro, e opcionalmente acionar retry do worker falho. Não deve quebrar o pipeline inteiro por um worker (Capítulo 4.3 — Erros comuns).
