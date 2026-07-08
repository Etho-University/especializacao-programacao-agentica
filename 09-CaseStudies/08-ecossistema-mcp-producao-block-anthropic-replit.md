# Caso de Estudo — Ecossistema MCP em produção (Block, Anthropic, Replit)

> ETHAGT08 · Adoção real do MCP como padrão corporativo.

## Contexto

Desde o lançamento do MCP (nov/2024), várias empresas adotaram-no internamente como padrão de integração entre LLMs e sistemas corporativos. Block (Square), Anthropic e Replit publicaram relatos de uso.

## Padrão arquitetural típico

```
desenvolvedor / agente interno
   │
   ▼
[HOST corporativo (Claude Desktop, IDE custom)]
   │
   ├── client ─► [server: CRM interno]      (tools: get_customer, update_lead)
   ├── client ─► [server: code repos]       (tools: search_code, get_repo)
   ├── client ─► [server: docs (Confluence)](resources: docs por URI)
   ├── client ─► [server: métricas]         (tools: query_metrics)
   └── ... (20-50 servers)
   │
   ▼
[Catálogo interno + OAuth corporativo + auditoria]
```

## Práticas observadas

1. **Catálogo centralizado**: cada server tem owner, versão, SLA.
2. **Auth integrada**: OAuth 2.1 com SSO corporativo; sem credenciais hardcoded.
3. **Governança de plataforma**: time dedicado revisa novos servers (segurança, qualidade).
4. **Sandboxing**: servers rodam em containers isolados com mínimo privilégio.
5. **Auditoria**: logs centralizados de todas as tool calls para forense/compliance.

## Benefícios relatados

- Desenvolvedores dão a qualquer LLM acesso a sistemas internos **sem escrever conectores custom**.
- Padronização reduz N×M para N+M.
- Auditoria centralizada viabiliza compliance.
- Novos LLMs (de qualquer provedor) ganham acesso instantaneamente ao ecossistema.

## Lições

1. **MCP é infraestrutura**, não feature — tratar como produto interno.
2. **Governança desde o início** — adicionar depois é doloroso.
3. **Sandboxing não opcional** — servers são código arbitrário.
4. **OAuth > API keys** em escala corporativa.

## Referências

- Anthropic. *Introducing the Model Context Protocol*. nov/2024.
- Block engineering blog (relatos de adoção MCP).
- Cloudflare *Remote MCP servers* (2025).
