# ETHAGT04 — Lab 1: Plan-and-Execute vs ReAct

> Curso: Reasoning & Planning · Carga: 30h · Pré-req: ETHAGT03

## Objetivo
Implementar a mesma tarefa complexa multi-step usando dois padrões de raciocínio distintos (Plan-and-Execute e ReAct), medir e comparar custo, latência, qualidade e robustez.

## Preparação
- Ambiente: Python 3.11+, `pip install openai`, `.env` com API key
- Dados/recursos: conjunto de 5 problemas multi-step do tipo GAIA-lite (fornecidos em `problems.json`)
- Leitura prévia: Apostila ETHAGT04, Unidade 2 (Plan-and-Execute e ReWOO) e Unidade 1 (tipologia)

## Roteiro
### Passo 1 — Definir os problemas de teste
Crie `problems.json` com 5 problemas multi-step que exigem planejamento:

```json
[
  {"id": "P1", "question": "Quantos anos o autor de '1984' tinha quando publicou o livro?",
   "requires": ["search_orwell_birth", "search_1984_date", "calculate_age"]},
  {"id": "P2", "question": "Qual a diferença de população entre as 2 maiores cidades do Brasil?",
   "requires": ["search_cities", "search_populations", "calculate_diff"]}
]
```

**Checkpoint:** 5 problemas com resposta verificável e passos necessários documentados.

### Passo 2 — Implementar o agente ReAct
Use o agent loop do ETHAGT01 Lab 1, adaptado com tools `search`, `calculate` e `answer`:

```python
REACT_SYSTEM = """Use Thought/Action/Observation loop.
Available tools: search[query], calculate[expression], answer[result]
Think step by step before each action."""
```

**Checkpoint:** agente ReAct resolve P1 corretamente usando search + calculate.

### Passo 3 — Implementar o agente Plan-and-Execute
Implemente um *planner* que gera o plano completo primeiro, e um *executor* que executa cada passo:

```python
def plan_and_execute(question):
    plan = call_llm(f"""Create a step-by-step plan to answer this question.
    Output as JSON list of steps with tool calls:
    Question: {question}""")
    steps = json.loads(plan)
    results = {}
    for i, step in enumerate(steps):
        results[f"step_{i}"] = execute_step(step, results)
    final = call_llm(f"""Based on these results, answer the question.
    Results: {results}\nQuestion: {question}""")
    return final
```

**Checkpoint:** planner gera plano em JSON e executor resolve cada passo.

### Passo 4 — Implementar ReWOO (variação de plan-and-execute)
Adicione a variante ReWOO onde o plano é "cego" (sem observar resultados intermediários):

```python
def rewoo(question):
    plan = call_llm(f"""Create a plan using placeholders like #E1, #E2.
    Example: #E1 = search[author birth], #E2 = calculate[#E1 - 1984]
    Question: {question}""")
    # Executar evidências em paralelo, substituindo placeholders
    ...
```

**Checkpoint:** ReWOO executa evidências em paralelo e substitui placeholders.

### Passo 5 — Instrumentação de medição
Crie um harness que mede para cada problema e cada padrão:

```python
@dataclass
class RunResult:
    problem_id: str
    pattern: str  # react | plan_execute | rewoo
    correct: bool
    total_tokens: int
    latency_s: float
    n_steps: int
    cost_usd: float
```

**Checkpoint:** harness roda 1 problema × 3 padrões e retorna 3 `RunResult`.

### Passo 6 — Executar benchmark
Rode os 3 padrões nos 5 problemas (15 execuções no total) e registre:

```python
for problem in problems:
    for pattern in [react_agent, plan_and_execute, rewoo]:
        result = run_with_metrics(pattern, problem)
        results.append(result)
```

**Checkpoint:** 15 resultados registrados em `benchmark.json`.

### Passo 7 — Análise comparativa
Produza uma tabela comparativa e gráficos:

| Padrão | Accuracy (5) | Tokens médios | Latência média | Steps médios |
|---|---|---|---|---|
| ReAct | /5 | | | |
| Plan-and-Execute | /5 | | | |
| ReWOO | /5 | | | |

**Checkpoint:** tabela preenchida em `comparison.md` com discussão.

### Passo 8 — Análise de robustez
Teste um cenário de falha: injete um erro em uma tool (ex.: search retorna vazio) e observe como cada padrão reage. ReAct deve adaptar; Plan-and-Execute pode falhar.

**Checkpoint:** comportamento de cada padrão sob falha documentado.

## Desafios extras
- Implemente re-planejamento no Plan-and-Execute: se um passo falha, gerar novo plano
- Adicione Tree of Thoughts como 4º padrão e compare
- Meça quality/cost ratio (accuracy por dólar gasto) para cada padrão

## Entrega
- Repositório com `agents.py` (3 padrões), `benchmark.json`, `comparison.md`
- Commit no padrão `ETHAGT04: lab-1 comparar plan-execute vs react`

## Rubrica
Avaliado pela rubrica em `08-Assignments/ETHAGT04/assignment-01.md` (Pilar Comportamental 20%: colaboração em labs).
