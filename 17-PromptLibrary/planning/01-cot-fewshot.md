# planning/01-cot-fewshot.md

## objetivo
Prompt de Chain-of-Thought com exemplos few-shot para guiar o raciocínio passo a passo.

## variáveis
- `{{question}}` — pergunta ou problema a ser resolvido
- `{{examples}}` — 2-3 pares pergunta + raciocínio passo a passo + resposta final

## template

```
Solve the following problems step by step.

Examples:

{{examples}}

Now solve this new problem. Think step by step before giving the final answer.

Question: {{question}}

Reasoning:
```

## exemplo de uso
`{{question}}` = "João tem 3 maçãs, dá 2 para Maria e compra 5. Quantas tem agora?" — o modelo raciocina em passos aritméticos.

## trade-offs
- Exemplos consomem tokens e podem reduzir o limite útil de geração
- Exemplos mal escolhidos podem enviesar o raciocínio (contaminação)
- Funciona melhor com 2-4 exemplos; acima disso o ganho marginal é pequeno

## variações
- **Zero-shot CoT**: apenas "Let's think step by step" sem exemplos
- **CoT com verificação**: incluir passo de auto-checagem ao final
- **CoT com formatação rígida**: `Step 1: ... Step N: ... Answer: ...`
