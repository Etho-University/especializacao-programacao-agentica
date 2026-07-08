# routing/02-rag-need.md

## objetivo
Prompt decisório que avalia se uma consulta precisa de recuperação externa (RAG) ou pode ser respondida apenas com conhecimento interno do modelo.

## variáveis
- `{{query}}` — pergunta do usuário
- `{{knowledge_cutoff}}` — data de corte do conhecimento do modelo
- `{{rag_threshold}}` — nível de confiança mínimo para decidir "retrieve"

## template

```
Determine whether the following query requires external information retrieval (RAG) or can be answered from internal knowledge.

Query: {{query}}
Internal knowledge cutoff: {{knowledge_cutoff}}

Analyze:
1. Is the query time-sensitive (e.g., "latest", "today", "2025") beyond the cutoff?
2. Does it refer to specific documents, APIs, or data not available in training?
3. Is it about a niche or private domain unlikely to be in training data?
4. Can the question be answered with general knowledge?

Output JSON:
{
  "needs_retrieval": true/false,
  "confidence": <0.0–1.0>,
  "reason": "<short justification>",
  "rag_query_hint": "<optional: a rewritten query optimized for retrieval>"
}

If confidence < {{rag_threshold}}, default to needs_retrieval: true.
```

## exemplo de uso
Query = "Qual foi o revenue da OpenAI em 2025?" → needs_retrieval: true (dado pós-cutoff e não público internamente).

## trade-offs
- Falso negativo: modelo acha que sabe mas está desatualizado — gera alucinação
- Falso positivo: recupera documentos desnecessariamente, aumentando latência e custo
- A qualidade do reranker downstream é crítica para este prompt funcionar em cascata

## variações
- **RAG routing com contexto**: incluir histórico da conversa para decisão mais informada
- **Domain-specific threshold**: limiares diferentes por domínio (e.g., 0.6 para tech geral, 0.9 para medicina)
- **Hybrid approach**: sempre recuperar snippets curtos, mas só passar para o gerador se needs_retrieval=true
