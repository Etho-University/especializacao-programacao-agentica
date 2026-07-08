# Caso de Estudo — Assistentes empresariais em escala (Glean, Hebbia, Notion)

> ETHAGT14 · Operação de agentes sobre milhões de documentos para milhares de usuários.

## Contexto

Empresas como Glean (search empresarial), Hebbia (análise de documentos), Notion AI operam assistentes que servem milhares de usuários sobre corpora enormes. Os desafios de escala são universais e ilustrativos.

## Padrões observados

| Técnica | Impacto |
|---|---|
| **Adaptive RAG** | 70% das perguntas não precisam de retrieval → economia dramática |
| **Model routing** | 80% das perguntas fáceis → Haiku; 20% complexas → Sonnet |
| **Cache semântico** | 30-50% hit rate em perguntas repetidas |
| **Sharding por tenant** | Isolamento + localidade de cache |
| **FinOps dashboard** | Custo por usuário, alertas em outliers |

## Arquitetura típica

```
[user request]
   │
   ├── [cache check] ──hit──► return cached
   │
   ├── [routing: complexidade?]
   │     ├── fácil ──► Haiku
   │     └── difícil ──► Sonnet
   │
   ├── [Adaptive RAG: precisa recuperar?]
   │     ├── não ──► responder direto
   │     └── sim ──► retrieve híbrido
   │
   └── [response + log custo]

[sharding por tenant_id] em toda a stack
[FinOps dashboard] agregando métricas
```

## Resultados

- Viabiliza milhares de usuários simultâneos.
- Custo por usuário sustentável (<$10/mês typical).
- Latência p95 < 3s para maioria das queries.

## Lições

1. **Adaptive RAG** é o maior ganho único (skip retrieval quando não precisa).
2. **Model routing** economiza 5-10× sem perder qualidade percebida.
3. **Cache semântico** tem hit rate alto em enterprise (perguntas repetem).
4. **FinOps** é cultura, não ferramenta — medir desde o dia 1.
5. **Sharding por tenant** resolve isolamento e performance.

## Referências

- Glean engineering blog.
- Hebbia technical posts.
- Anthropic case studies.
