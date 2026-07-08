# Workflow: Prompt Chaining

## Intenção
Decompor uma tarefa em **sequência fixa** de chamadas LLM, cada uma processando a saída da anterior. Gates programáticos podem interromper/redirecionar entre etapas.

## Estrutura
```
[LLM 1] → gate → [LLM 2] → gate → [LLM 3] → saída
```

## Quando usar
- Tarefa decompõe-se naturalmente em **subtarefas fixas**.
- Aceita **trocar latência por accuracy** (cada chamada mais fácil).
- Há critérios claros para gates.

## Quando evitar
- Subtarefas não são previsíveis.
- Não há gates válidos (sem critério objetivo).
- 1 chamada resolve.

## Exemplos
- Marketing: gerar copy PT → traduzir EN → revisar tom.
- Documento: outline → validar → escrever.
- Código: função → testes → validar.

## Gates (código, não LLM)
- Validar formato da saída.
- Verificar palavras proibidas.
- Classificar e redirecionar.
- Parar se score baixo.

## Anti-patterns
- Encadear sem gates ("vai que vai").
- Sem critério (quando 1 chamada bastava).
- Gates que chamam LLM desnecessariamente.

## Custo
N chamadas LLM × tokens acumulados. Mais barato que agente iterativo, mais caro que 1 chamada.

## Referências
- Anthropic *Building Effective Agents* (2024).
