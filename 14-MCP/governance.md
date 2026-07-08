# Governança MCP

> Catálogo, permissões, versionamento e supply chain.

## Catálogo de Servers

Manter um registro central (YAML/JSON) com:

```yaml
servers:
  arxiv:
    source: github:org/arxiv-mcp
    version: "1.2.0"
    tools: [search_papers, get_paper_details]
    auth: none
    approval: auto
  github:
    source: github:org/github-mcp
    version: "2.1.0"
    tools: [list_issues, create_pr, review_code]
    auth: oauth
    approval: manual (ações destrutivas)
```

## Permissões

- **auto**: tools read-only (search, read)
- **manual**: tools write (create, update, delete)
- **sempre_perguntar**: tools sensíveis (deploy, payment)
- **bloqueado**: tools proibidas

## Versionamento

- Servers versionados semanticamente
- Changelog obrigatório
- Breaking changes requerem approval manual

## Supply Chain

- **Auditoria**: logs de todas as tool calls
- **Verificação**: checksum dos servers instalados
- **Isolamento**: cada server roda em processo separado

## Referências
- OWASP Top 10 for LLM (2025): supply chain risks
- EU AI Act: transparência de ferramentas
