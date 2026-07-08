# ETHAGT04 — Lab 2: Reflexion com memória

> Curso: Reasoning & Planning · Carga: 30h · Pré-req: ETHAGT04 Lab 1

## Objetivo
Implementar um agente que usa o padrão Reflexion — auto-crítica após falha com memória de erros anteriores — e demonstrar melhoria de desempenho em um benchmark de raciocínio após múltiplas tentativas.

## Preparação
- Ambiente: Python 3.11+, `pip install openai`, `.env` com API key
- Dados/recursos: 10 problemas de raciocínio lógico/matemático (subconjunto de GSM8K ou custom) em `reasoning_problems.json`
- Leitura prévia: Apostila ETHAGT04, Unidade 4 (Reflexion)

## Roteiro
### Passo 1 — Definir o benchmark
Crie `reasoning_problems.json` com 10 problemas de raciocínio e suas respostas:

```json
[
  {"id": "R1", "question": "Um trem viaja a 60 km/h por 2.5 horas. Qual a distância?",
   "answer": "150", "category": "math"},
  {"id": "R2", "question": "Se todos os A são B, e alguns B são C, o que podemos concluir sobre A e C?",
   "answer": "nada definitivo", "category": "logic"}
]
```

**Checkpoint:** 10 problemas com respostas verificáveis em 2+ categorias.

### Passo 2 — Implementar o agente base (sem Reflexion)
Crie um agente que tenta resolver cada problema usando CoT:

```python
def solve_base(question):
    response = call_llm(f"""Solve this step by step.
    End with: FINAL ANSWER: <answer>
    Question: {question}""")
    return extract_answer(response)
```

**Checkpoint:** agente base roda nos 10 problemas e produz respostas.

### Passo 3 — Medir baseline
Rode o agente base nos 10 problemas e registre accuracy:

```python
baseline_correct = 0
for p in problems:
    answer = solve_base(p["question"])
    if check_answer(answer, p["answer"]):
        baseline_correct += 1
print(f"Baseline accuracy: {baseline_correct}/10")
```

**Checkpoint:** baseline accuracy registrado (ex.: 6/10).

### Passo 4 — Estrutura de memória Reflexion
Defina a estrutura de memória que acumula reflexões:

```python
@dataclass
class ReflectionMemory:
    reflections: list[str] = field(default_factory=list)

    def add(self, failure_analysis: str):
        self.reflections.append(failure_analysis)

    def context(self) -> str:
        if not self.reflections:
            return ""
        return "\n".join(f"- {r}" for r in self.reflections[-5:])
```

**Checkpoint:** `ReflectionMemory` funciona: `add()` e `context()` operacionais.

### Passo 5 — Implementar o loop Reflexion
Para cada problema, tente até 3 vezes. Após cada falha, gere uma reflexão:

```python
def solve_with_reflexion(question, correct_answer, memory: ReflectionMemory, max_attempts=3):
    for attempt in range(max_attempts):
        context = memory.context()
        prompt = f"""Solve step by step.
        {'Previous mistakes to avoid:\n' + context if context else ''}
        Question: {question}
        End with: FINAL ANSWER: <answer>"""
        answer = extract_answer(call_llm(prompt))
        if check_answer(answer, correct_answer):
            return answer, True, attempt + 1
        # Reflexionar sobre a falha
        reflection = call_llm(f"""Why was this answer wrong?
        Question: {question}
        Your answer: {answer}
        Correct: {correct_answer}
        Briefly explain the mistake.""")
        memory.add(reflection)
    return answer, False, max_attempts
```

**Checkpoint:** loop de até 3 tentativas com reflexão entre cada.

### Passo 6 — Experimento: aprendizado cross-problem
Rode os 10 problemas em sequência, mantendo a mesma `ReflectionMemory` para problemas da mesma categoria:

```python
results = []
for p in problems:
    memory = category_memories[p["category"]]
    answer, success, attempts_used = solve_with_reflexion(
        p["question"], p["answer"], memory)
    results.append({"id": p["id"], "success": success, "attempts": attempts_used})
```

**Checkpoint:** cada categoria tem sua própria memória acumulada.

### Passo 7 — Comparar baseline vs Reflexion
Compare accuracy e número de tentativas:

| Configuração | Accuracy (10) | Tentativas médias | Tokens médios |
|---|---|---|---|
| Baseline (sem Reflexion) | /10 | 1 | |
| Reflexion (até 3 tentativas) | /10 | | |

**Checkpoint:** tabela preenchida mostrando melhoria (ou não) da accuracy.

### Passo 8 — Análise de convergência
Analise: a memória ajuda em problemas posteriores da mesma categoria? O custo extra compensa?

```markdown
## Análise
- Acurácia passou de X/10 para Y/10 com Reflexion
- O ganho veio principalmente de [mesma tentativa | re-tentativas]
- A memória cross-problem ajudou nos últimos problemas da categoria "math"
- Custo aumentou N% mas accuracy melhorou M%
```

**Checkpoint:** análise documentada com conclusão sobre quando Reflexion vale a pena.

## Desafios extras
- Implemente Reflexion com memória persistente (SQLite) que sobrevive entre sessões
- Compare Reflexion com self-consistency (gerar 5 respostas e fazer maioria)
- Adicione um orçamento de tokens: se Reflexion exceder budget, abortar e usar baseline

## Entrega
- Repositório com `reflexion_agent.py`, `results.json`, `analysis.md`
- Commit no padrão `ETHAGT04: lab-2 implementar reflexion com memória`

## Rubrica
Avaliado pela rubrica em `08-Assignments/ETHAGT04/assignment-01.md` (Pilar Comportamental 20%: colaboração em labs).
