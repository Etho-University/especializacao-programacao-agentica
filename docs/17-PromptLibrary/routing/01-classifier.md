# routing/01-classifier.md

## objetivo
Prompt para classificar uma entrada em uma dentre N categorias pré-definidas, com fallback para "desconhecido".

## variáveis
- `{{categories}}` — lista de categorias com nome e breve descrição
- `{{input}}` — texto a ser classificado
- `{{output_format}}` — formato da saída (label, JSON, etc.)

## template

```
Classify the following input into one of the predefined categories.

Categories:
{{categories}}

Input:
{{input}}

Respond ONLY with a JSON object:
{
  "category": "<category_name>",
  "confidence": <0.0–1.0>,
  "reasoning": "<brief justification>",
  "fallback": <true|false>
}

If the input does not clearly match any category, set "category" to "unknown", "confidence" to a low value, and "fallback" to true.

Output format: {{output_format}}
```

## exemplo de uso
`{{categories}}` = `["bug", "feature_request", "question", "documentation"]`; classificar issue de GitHub automaticamente.

## trade-offs
- Categorias muito similares geram confusão e baixa confiança
- Categorias muito amplas (e.g., "outros") viram catch-all sem informação
- Dependente da qualidade das descrições; descrições vagas degradam a classificação

## variações
- **Hierarchical classifier**: duas etapas — primeiro domínio, depois subcategoria
- **Threshold routing**: se confiança < limiar, rotear para revisão humana
- **Multi-label classifier**: permitir que uma entrada pertença a múltiplas categorias simultaneamente
