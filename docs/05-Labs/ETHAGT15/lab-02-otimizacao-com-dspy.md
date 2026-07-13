# ETHAGT15 — Lab 2: Otimização automatizada com DSPy

> Curso: Meta-Agentes & Sistemas Autoaprendentes · Carga: 15h · Pré-req: ETHAGT15 Lab 1

## Objetivo
Usar DSPy para otimizar automaticamente os prompts e tools de um agente, medir o ganho de desempenho comparando antes vs depois da otimização, e refletir sobre os trade-offs de auto-otimização.

## Preparação
- Ambiente: Python 3.11+, `pip install dspy-ai openai`, `.env` com API key
- Dados/recursos: dataset de treino (20 exemplos) e teste (10 exemplos) em [`train.json`](https://raw.githubusercontent.com/Etho-University/especializacao-programacao-agentica/main/05-Labs/ETHAGT15/train.json) e [`test.json`](https://raw.githubusercontent.com/Etho-University/especializacao-programacao-agentica/main/05-Labs/ETHAGT15/test.json)
- Leitura prévia: Apostila ETHAGT15, Unidade 3 (Otimização automatizada) e Unidade 4 (Auto-aprendizado)

## Roteiro
### Passo 1 — Instalar e configurar DSPy
```python
import dspy

lm = dspy.LM("openai/gpt-4o-mini", api_key=os.environ["OPENAI_API_KEY"])
dspy.configure(lm=lm)
```

**Checkpoint:** DSPy configurado e conectado ao LLM.

### Passo 2 — Definir a assinatura do módulo
Modele a tarefa como uma assinatura DSPy:

```python
class AnswerQuestion(dspy.Signature):
    """Answer a question accurately and concisely."""
    question: str = dspy.InputField(desc="The user's question")
    context: str = dspy.InputField(desc="Retrieved context, if any")
    answer: str = dspy.OutputField(desc="Clear, accurate answer")
```

**Checkpoint:** assinatura define input e output com descrições.

### Passo 3 — Construir o módulo baseline
Crie um módulo simples com prompt não-otimizado:

```python
class SimpleQA(dspy.Module):
    def __init__(self):
        super().__init__()
        self.generate = dspy.ChainOfThought(AnswerQuestion)

    def forward(self, question, context=""):
        return self.generate(question=question, context=context)
```

**Checkpoint:** módulo baseline executa e produz respostas.

### Passo 4 — Preparar dados de treino e teste
Carregue exemplos no formato DSPy:

```python
from dspy import Example

train_data = [
    Example(question=d["question"], context=d.get("context", ""),
            answer=d["answer"]).with_inputs("question", "context")
    for d in load_json("train.json")
]
test_data = [
    Example(question=d["question"], context=d.get("context", ""),
            answer=d["answer"]).with_inputs("question", "context")
    for d in load_json("test.json")
]
```

**Checkpoint:** 20 exemplos de treino e 10 de teste carregados.

### Passo 5 — Definir a métrica de avaliação
Crie uma métrica customizada:

```python
def answer_quality_metric(example, prediction, trace=None):
    """LLM-as-judge: rate answer quality 1-5."""
    prompt = f"""Rate this answer 1-5:
    Question: {example.question}
    Expected: {example.answer}
    Got: {prediction.answer}
    Reply with just a number."""
    score = int(dspy.LM("openai/gpt-4o-mini")(prompt)[0].strip())
    return score / 5.0  # normalizar para 0-1
```

**Checkpoint:** métrica retorna score entre 0 e 1.

### Passo 6 — Medir baseline
Avalie o módulo sem otimização:

```python
from dspy import Evaluate

evaluator = Evaluate(devset=test_data, metric=answer_quality_metric, num_threads=4)
baseline_score = evaluator(SimpleQA())
print(f"Baseline score: {baseline_score:.2f}")
```

**Checkpoint:** baseline score registrado.

### Passo 7 — Otimizar com BootstrapFewShot
Aplique o otimizador automático:

```python
from dspy.teleprompt import BootstrapFewShot

optimizer = BootstrapFewShot(
    metric=answer_quality_metric,
    max_bootstrapped_demos=4,
    max_labeled_demos=4
)

optimized = optimizer.compile(SimpleQA(), trainset=train_data)
optimized_score = evaluator(optimized)
print(f"Optimized score: {optimized_score:.2f}")
```

**Checkpoint:** módulo otimizado produzido e avaliado.

### Passo 8 — Comparar antes vs depois
Produza a tabela comparativa:

```python
print(f"Baseline:  {baseline_score:.2f}")
print(f"Optimized: {optimized_score:.2f}")
print(f"Improvement: +{(optimized_score - baseline_score)*100:.1f}%")
```

| Configuração | Score (10 testes) | Tokens médios | Latência média |
|---|---|---|---|
| Baseline (sem otimização) | | | |
| Otimizado (BootstrapFewShot) | | | |

**Checkpoint:** tabela preenchida com ganho mensurável.

### Passo 9 — Inspecionar o que mudou
DSPy permite ver os exemplos/few-shot que o otimizador adicionou:

```python
print("Optimized demos:")
for demo in optimized.demos:
    print(f"  Q: {demo.question[:50]}... → A: {demo.answer[:50]}...")
```

**Checkpoint:** demos selecionados pelo otimizador documentados.

## Desafios extras
- Experimente um otimizador mais poderoso: `BootstrapFewShotWithRandomSearch` ou `MIPRO`
- Otimize também a escolha de tools (não só o prompt)
- Compare otimização com BootstrapFewShot vs otimização com `COPRO` (CoordinatePromptOptimizer)
- Adicione auto-aprendizado contínuo: rodar otimização semanal com novos dados

## Entrega
- Repositório com `dspy_optimize.py`, `train.json`, `test.json`, `optimization_report.md`
- Commit no padrão `ETHAGT15: lab-2 otimizar agente com dspy`

## Rubrica
Avaliado pela rubrica em `08-Assignments/ETHAGT15/assignment-01.md` (Pilar Comportamental 20%: colaboração em labs).
