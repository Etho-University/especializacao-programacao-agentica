# reflection/03-evaluator-optimizer.md

## objetivo
Prompt para um avaliador que dá feedback detalhado para um gerador, permitindo iterações de melhoria (loop evaluator-optimizer).

## variáveis
- `{{task}}` — descrição da tarefa
- `{{generation}}` — última versão gerada pelo otimizador
- `{{iteration}}` — número da iteração atual
- `{{max_iterations}}` — máximo de iterações permitidas

## template

```
You are the Evaluator in an evaluator-optimizer loop. Assess the latest generation and provide actionable feedback for improvement.

Task: {{task}}

Generation (iteration {{iteration}} of {{max_iterations}}):
{{generation}}

Evaluate on these dimensions:
1. Correctness — Does it accurately address the task?
2. Completeness — Are all aspects covered?
3. Clarity — Is it easy to understand?
4. Efficiency — Could it be simpler or faster?

For each dimension:
- Score (1–5)
- Specific evidence from the generation
- Concrete suggestion for improvement

Finally, state:
- Verdict: Pass (all scores >= 4) or Revise
- If Revise, what is the single most important change to make?
```

## exemplo de uso
Loop de geração de query SQL: o gerador produz uma query, o evaluator aponta erro de JOIN, gerador corrige, evaluator aprova.

## trade-offs
- Loop pode convergir lentamente se o evaluator for inconsistente
- Feedback muito vago ("improve clarity") não ajuda o gerador
- Atinge melhores resultados que single-shot, mas com custo multiplicado por iterações

## variações
- **Multi-evaluator**: dois ou mais evaluators com perspectivas diferentes (e.g., funcional + estilo)
- **Structured scores**: usar schema JSON para o feedback, facilitando parse e condicionamento do otimizador
- **Early stopping**: interromper o loop se a melhoria entre iterações for abaixo de um limiar
