# reflection/01-reflexion.md

## objetivo
Prompt de reflexão que analisa uma tentativa anterior (incluindo erros) e gera um plano melhorado para a próxima tentativa.

## variáveis
- `{{task}}` — descrição da tarefa
- `{{previous_attempts}}` — histórico de tentativas anteriores (ações, resultados, erros)
- `{{max_reflections}}` — número máximo de ciclos reflexão + retry

## template

```
You previously attempted the following task and did not succeed. Reflect on what happened and propose a corrected approach.

Task: {{task}}

Previous attempts:
{{previous_attempts}}

For each attempt, analyze:
1. What went wrong? (root cause)
2. What assumptions were incorrect?
3. What could have been done differently?

Now produce:
- Reflection Summary: synthesis of the key lessons learned
- Revised Plan: step-by-step corrected strategy, referencing the specific mistakes identified
- Confidence in New Plan: low / medium / high

You have {{max_reflections}} reflection cycles remaining. Use them wisely.
```

## exemplo de uso
Útil em loops de código onde o agente tenta implementar algo, falha (erro de compilação), reflete e tenta novamente com correções.

## trade-offs
- Pode cair em "reflection loops" onde o agente reflete infinitamente sem agir
- Reflexões genéricas ("preciso ter mais cuidado") não agregam valor
- O histórico de tentativas acumula tokens rapidamente

## variações
- **Guided reflection**: incluir perguntas específicas ("O erro foi de sintaxe ou semântica?")
- **Reflection com exemplos**: dar um exemplo de boa reflexão antes de pedir a do agente
- **Contrastive reflection**: comparar tentativa atual com uma solução ideal fornecida (ground-truth)
