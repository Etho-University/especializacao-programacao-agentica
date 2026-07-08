# Caso de Estudo — RAG em assistentes enterprise

> ETHAGT06 · Aplicações reais de RAG agêntico em produção.

## Contexto

Empresas como Notion, Glean, Hebbia e várias outras construíram assistentes empresariais baseados em RAG sobre documentos internos. Os desafios são universais e ilustrativos.

## Desafios típicos (e como RAG agêntico resolve)

| Desafio | RAG ingênuo | RAG agêntico |
|---|---|---|
| Documentos de diferentes fontes (Notion, Drive, Slack) | Pipeline único não funciona | Routing por fonte + fusão |
| Permissões (usuário só vê o que pode) | Ignora | Filter por ACL antes de gerar |
| Perguntas multi-hop ("quem aprovou o orçamento do projeto X?") | Falha | Agentic RAG encadeia buscas |
| Docs desatualizados | Responde errado | CRAG com fallback web/humano |
| Volume (milhões de docs) | Custo alto | Adaptive RAG pula retrieval quando não precisa |

## Padrão arquitetural típico

```
pergunta do usuário
   │
   ├── [ACL filter: quais docs o usuário pode ver?]
   ▼
[Adaptive RAG: precisa recuperar?]
   │
   ▼
[Retrieve híbrido: vector + BM25, multi-fonte]
   │
   ▼
[Re-rank com modelo especializado]
   │
   ▼
[Agentic loop: precisa de mais? refina query?]
   │
   ▼
[Generate com citações]
   │
   ▼
[Faithfulness check antes de responder]
```

## Lições

1. **Permissões/ACL** são frequentemente esquecidas e críticas em enterprise.
2. **Citação obrigatória**: respostas sem fonte em enterprise não são confiáveis.
3. **Multi-fonte** é a regra, não exceção.
4. **Faithfulness check** antes de responder reduz drasticamente alucinação em produção.

## Referências

- Glean, Hebbia — blogs técnicos sobre RAG empresarial.
- Anthropic *Contextual Retrieval* (2024) — técnicas de qualidade.
