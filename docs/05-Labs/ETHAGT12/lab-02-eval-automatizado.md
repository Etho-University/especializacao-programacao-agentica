# ETHAGT12 — Lab 2: Eval automatizado

> Curso: AgentOps, Observabilidade & Avaliação · Carga: 30h · Pré-req: ETHAGT12 Lab 1

## Objetivo
Construir um pipeline de avaliação automatizada com golden cases e LLM-as-judge, detectar regressão após uma mudança de prompt, e produzir um eval report estruturado.

## Preparação
- Ambiente: Python 3.11+, `pip install openai pydantic`, `.env` com API key
- Dados/recursos: 20 golden cases em `golden_cases.json`
- Leitura prévia: Apostila ETHAGT12, Unidade 3 (Avaliação automatizada) e Unidade 6 (Reportando resultados)

## Roteiro
### Passo 1 — Construir golden cases
Crie 20 casos de teste com input, expected output e critério de sucesso:

```json
[
  {
    "id": "GC1",
    "input": "Quanto é 15% de 200?",
    "expected": "30",
    "criteria": "exact_match",
    "category": "math"
  },
  {
    "id": "GC2",
    "input": "Explique o que é um agent loop",
    "expected": "should mention Thought-Action-Observation pattern",
    "criteria": "llm_judge",
    "category": "concept",
    "judge_rubric": "Response must explain the Thought→Action→Observation cycle and mention LLM-driven control"
  }
]
```

**Checkpoint:** 20 golden cases com critérios mensuráveis (exact_match ou llm_judge).

### Passo 2 — Implementar o eval runner
Execute o agente em cada caso e avalie:

```python
def run_eval(agent, cases):
    results = []
    for case in cases:
        output = agent.run(case["input"])
        if case["criteria"] == "exact_match":
            passed = output.strip() == case["expected"].strip()
        elif case["criteria"] == "llm_judge":
            passed = llm_judge(case, output)
        results.append({
            "id": case["id"], "input": case["input"],
            "output": output, "expected": case["expected"],
            "passed": passed, "category": case["category"]
        })
    return results
```

**Checkpoint:** eval runner produz um resultado por caso com `passed: true/false`.

### Passo 3 — Implementar o LLM-as-judge
Crie um juiz LLM com rubrica estruturada:

```python
def llm_judge(case, output):
    prompt = f"""You are an impartial judge. Evaluate the response.
    Rubric: {case.get("judge_rubric", "Is the response correct and complete?")}
    Input: {case["input"]}
    Expected: {case["expected"]}
    Response: {output}
    Reply only: PASS or FAIL, followed by a one-sentence reason."""
    result = call_llm(prompt, model="gpt-4o", temperature=0)
    return result.strip().startswith("PASS")
```

**Checkpoint:** juiz LLM retorna PASS/FAIL com razão para 3 casos de teste.

### Passo 4 — Mitigar vieses do LLM-judge
Adicione técnicas anti-viés:
- Posição aleatória (não viciar por ordem)
- Múltiplos juízes e maioria
- Juiz cego (sem saber qual é a versão do agente)

```python
def robust_judge(case, output, n_judges=3):
    votes = [llm_judge(case, output) for _ in range(n_judges)]
    return sum(votes) > n_judges / 2  # maioria
```

**Checkpoint:** juiz com múltiplas rodadas reduz falsos positivos.

### Passo 5 — Estabelecer baseline
Rode o eval com o agente atual e registre baseline:

```python
baseline = run_eval(agent_v1, golden_cases)
baseline_accuracy = sum(r["passed"] for r in baseline) / len(baseline)
print(f"Baseline accuracy: {baseline_accuracy:.1%}")
```

| Categoria | Casos | Passou baseline |
|---|---|---|
| math | 5 | /5 |
| concept | 5 | /5 |
| tool_use | 5 | /5 |
| reasoning | 5 | /5 |

**Checkpoint:** baseline accuracy registrado por categoria.

### Passo 6 — Introduzir mudança e detectar regressão
Altere o prompt do agente (ex.: tornar mais conciso) e re-rode o eval:

```python
agent_v2 = Agent(system_prompt=NEW_PROMPT)  # prompt modificado
new_results = run_eval(agent_v2, golden_cases)
new_accuracy = sum(r["passed"] for r in new_results) / len(new_results)
```

Compare com baseline:

| Categoria | Baseline | v2 (novo prompt) | Delta |
|---|---|---|---|
| math | /5 | /5 | |
| concept | /5 | /5 | |
| tool_use | /5 | /5 | |
| **Total** | /20 | /20 | |

**Checkpoint:** regressão detectada se alguma categoria piorar.

### Passo 7 — Análise de falhas
Para cada caso que falhou na v2, categorize a falha:

```python
def categorize_failures(results):
    failures = [r for r in results if not r["passed"]]
    categories = Counter()
    for f in failures:
        if "wrong calculation" in f["output"].lower():
            categories["calculation_error"] += 1
        elif len(f["output"]) < 10:
            categories["too_short"] += 1
        else:
            categories["other"] += 1
    return categories
```

**Checkpoint:** falhas categorizadas em `failure_analysis.md`.

### Passo 8 — Produzir o eval report
Use o template `24-Templates/template-eval-report.md` para produzir o relatório:

```markdown
# Eval Report — ETHAGT12 Lab 2

## Sumário
- Baseline accuracy: X/20 (Y%)
- Nova versão: X/20 (Y%)
- Regressão detectada: [Sim/Não]

## Metodologia
- 20 golden cases
- LLM-as-judge com 3 juízes (maioria)
- Categorias: math, concept, tool_use, reasoning

## Resultados por categoria
[tabela]

## Análise de falhas
[categorias de falha]

## Recomendação
[Deploy v2 / Reverter / Investigar]
```

**Checkpoint:** eval report completo em `eval_report.md`.

## Desafios extras
- Adicione CI: rode o eval a cada commit via GitHub Actions
- Implemente partial credit (0.5 para resposta parcialmente correta)
- Compare 3 versões de prompt simultaneamente e escolha a melhor
- Adicione métricas de processo: número de steps, loops, tool misuse

## Entrega
- Repositório com `eval_runner.py`, `golden_cases.json`, `eval_report.md`, `failure_analysis.md`
- Commit no padrão `ETHAGT12: lab-2 construir pipeline de avaliação`

## Rubrica
Avaliado pela rubrica em `08-Assignments/ETHAGT12/assignment-01.md` (Pilar Comportamental 20%: colaboração em labs).
