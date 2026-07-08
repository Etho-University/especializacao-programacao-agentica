# planning/03-self-consistency.md

## objetivo
Prompt que instrui o modelo a gerar múltiplos raciocínios independentes e depois consolidar por votação (self-consistency).

## variáveis
- `{{question}}` — pergunta a ser respondida
- `{{num_samples}}` — número de cadeias de raciocínio a gerar (default: 3–5)
- `{{aggregation_method}}` — método de consolidação (majority vote / weighted vote)

## template

```
You will answer the following question {{num_samples}} times, each time with an independent chain of thought. Be diverse in your reasoning approaches.

Question: {{question}}

After generating {{num_samples}} distinct reasoning chains, aggregate them using {{aggregation_method}} and produce:

- Final Answer: the answer that appears most consistently across samples
- Confidence: low / medium / high based on agreement among samples
- Dissenting Views: summarize any minority reasoning paths

Do not simply repeat the same reasoning. Vary assumptions, angles, or examples between samples.

Sample 1 Reasoning:
```

## exemplo de uso
Pergunta matemática que admite múltiplas abordagens (e.g., "Qual a probabilidade de tirar dois 6 em 3 dados?") — amostra 3 raciocínios e vota na resposta mais frequente.

## trade-offs
- Custo de tokens multiplicado por `{{num_samples}}`
- Amostras muito similares não agregam valor
- Melhor em problemas factuais e de raciocínio lógico; pior em tarefas criativas ou subjetivas

## variações
- **Weighted consistency**: ponderar cada amostra por um score de confiança
- **Self-consistency com critic**: cada amostra é seguida de autoavaliação antes da votação
- **Sample-then-refine**: após a votação, refinar a resposta final com base nos dissensos
