# summarization/01-conversation-summary.md

## objetivo
Prompt para sumarizar um histórico de conversa (chat) mantendo as decisões, perguntas-chave e respostas.

## variáveis
- `{{conversation}}` — transcript da conversa (role + message)
- `{{max_summary_length}}` — tamanho máximo em tokens ou sentenças
- `{{focus}}` — foco da sumarização (ex.: decisões, dúvidas, ações pendentes)

## template

```
Summarize the following conversation, focusing on {{focus}}.

Conversation:
{{conversation}}

Produce a summary with these sections:

**Context**: 1-2 sentences describing what the conversation is about.
**Key Decisions**: bullet list of decisions made.
**Open Questions**: any unresolved questions or pending items.
**Action Items**: tasks assigned, with owner if identifiable.

Constraints:
- Total summary must not exceed {{max_summary_length}} sentences.
- Use direct language, avoid meta-commentary ("the user asked...").
- Preserve factual accuracy; do not add information not present.

Summary:
```

## exemplo de uso
Resumir um atendimento de suporte de 30 mensagens em 5 sentenças, destacando o problema reportado e a solução acordada.

## trade-offs
- Perde nuance emocional e tom da conversa
- Foco muito restrito pode ignorar informações periféricas importantes
- Conversas longas exigem sumarização incremental (janela deslizante) ou perde-se o início

## variações
- **Turn-by-turn compression**: comprimir cada fala individualmente antes de sumarizar o todo
- **Hierarchical conversation summary**: primeiro sumarizar segmentos, depois sumarizar as sumarizações
- **Structured conversation summary**: formato tabular com speaker, tópico, decisão por bloco
