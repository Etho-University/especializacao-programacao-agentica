# ETHAGT02 — Lista de Exercícios

> Curso: Tool Calling e Agent-Computer Interface (ACI). Fixação de conceitos. Use a apostila `04-Apostilas/ETHAGT02/apostila.md` como referência.

## Múltipla escolha

**1. Na engenharia de tools, o que é "poka-yoke"?**

a) Uma técnica de fine-tuning de LLMs
b) Um princípio de design à prova de erros (mistake-proofing) aplicado às descrições de tools
c) Um protocolo de comunicação entre agentes
d) Um método de compressão de JSON schema

**2. Qual é uma característica de uma tool destrutiva que exige HITL?**

a) É lenta de executar
b) Produz efeitos irreversíveis (delete, deploy, transfer, email)
c) Retorna dados estruturados
d) Consome muitos tokens

**3. O JSON Schema de uma tool atua como:**

a) Um template de prompt
b) Um contrato entre o LLM e o executor da função
c) Um log de auditoria
d) Um mecanismo de cache

**4. O anti-pattern "paths relativos" em tools causa qual problema?**

a) Aumento de custo de tokens
b) O modelo pode gerar paths que não correspondem ao sistema de arquivos real do ambiente
c) Incompatibilidade de encoding
d) Rate limit excedido

## Verdadeiro ou Falso (justificado)

**1.** "É melhor ter muitas tools especializadas (granularidade fina) do que poucas tools consolidadas." — Justifique.

**2.** "Timeouts e retries devem ser configurados em todas as tools que fazem chamadas de rede." — Justifique.

**3.** "Uma tool com idempotência garante que chamadas repetidas não causem efeitos colaterais duplicados." — Justifique.

**4.** "Erros de tool devem ser propagados ao modelo como mensagem útil, não como exceção silenciosa." — Justifique.

## Código curto

**1.** Escreva um JSON Schema (ou Pydantic model) para uma tool `send_email` com `to`, `subject`, `body` e `request_id` (idempotência), incluindo validação de formato de email.

**2.** Reescreva a descrição abaixo aplicando princípios de ACI (poka-yoke, exemplos, fronteiras):

```
search(q): searches stuff
```

**3.** Escreva um decorator Python `@hitl_confirm` que imprime a ação e exige confirmação do humano antes de executar a função.

## Análise de trade-off

**1.** Compare 1 tool com parâmetro `mode` (ex.: `mode: "draft" | "send"`) vs. 2 tools separadas (`draft_email` e `send_email`). Quando escolher cada?

**2.** Compare schema estrito (enums, patterns, required fields) vs. schema frouxo. Qual o custo/benefício de cada?

**3.** Quando uma tool com `request_id` (idempotência) é essencial vs. desnecessária?

## Debug / diagnóstico

**1.** Um agente chama a tool `get_user(id=123)` mas recebe `null`. Em vez de tratar o erro, o agente tenta `get_user(id=123)` novamente em loop. Diagnostique 2 causas prováveis e proponha correções.

**2.** Dado este schema, identifique 3 anti-patterns:
```json
{
  "name": "do_stuff",
  "parameters": { "type": "object" }
}
```
