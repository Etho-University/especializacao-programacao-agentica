# extraction/01-structured-json.md

## objetivo
Prompt para extrair informações de texto não-estruturado e devolver em formato JSON seguindo um schema definido.

## variáveis
- `{{text}}` — texto de origem (email, log, documento)
- `{{json_schema}}` — schema JSON com tipos e descrições dos campos
- `{{strict_mode}}` — se true, valores ausentes viram null (não omitidos)

## template

```
Extract structured data from the following text according to the JSON schema below.

Text:
{{text}}

JSON Schema:
{{json_schema}}

Rules:
- Extract values exactly as they appear; do not paraphrase or infer.
- If a value is not found in the text, set it to null (do not omit the key).
- Do not add fields that are not in the schema.
- Preserve original formatting for dates, currencies, and numbers.
- If the text is ambiguous, include a "_notes" key with your uncertainty.

Respond ONLY with valid JSON.
```

## exemplo de uso
Extrair de um email de confirmação de pedido: `{"order_id": "ABC-123", "total": 299.90, "items": [...], "date": "2025-11-20"}`.

## trade-offs
- Schema muito complexo (aninhado profundo) reduz acurácia
- Campos opcionais vs obrigatórios: null vs ausência é uma escolha de design que afeta parsers downstream
- Textos muito longos podem fazer o modelo perder campos no meio

## variações
- **JSON com extração multivalorada**: arrays de objetos quando há múltiplas ocorrências (ex.: todos os produtos em um email)
- **Incremental JSON**: extrair campos em múltiplas chamadas quando o schema é muito grande
- **JSON + raw fallback**: incluir campo `raw_unknown` com texto não extraído para auditoria
