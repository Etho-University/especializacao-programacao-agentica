# 14 — MCP (Model Context Protocol)

Material dedicado ao **Model Context Protocol**. O curso `ETHAGT08` aprofunda este diretório; aqui fica o **guia de referência** para consulta contínua.

## Conteúdo

### Fundamentos
- [`intro.md`](intro.md) — o que é, por que existe, arquitetura host/client/server
- [`specification.md`](specification.md) — resumo da spec oficial (2025-11-25) + mudanças recentes
- [`transports.md`](transports.md) — stdio vs Streamable HTTP (comparação profunda)

### Construindo
- [`building-servers.md`](building-servers.md) — guia de construção (Python FastMCP + TS SDK)
- [`building-clients.md`](building-clients.md) — hosts e integração em agentes custom
- [`examples/`](examples) — servers de referência: filesystem, GitHub, arXiv, Confluence Etho

### Produção
- [`governance.md`](governance.md) — catálogo, permissões, versionamento, supply chain
- [`security.md`](security.md) — riscos, mitigações, red team
- [`oauth.md`](oauth.md) — auth em remote MCP (OAuth 2.1)

## Status

- Conteúdo canônico: `04-Apostilas/ETHAGT08/apostila.md` (8 capítulos profundos).
- ✅ Guia completo: intro, spec, transports, building-servers, building-clients, governance, security, oauth.
- 🔄 `examples/`: server mínimo em FastMCP (ver `19-Examples/ETHAGT08/exemplo-03-mcp-server/`).

## Referência canônica

- [modelcontextprotocol.io](https://modelcontextprotocol.io)
- [Anthropic MCP announcement](https://www.anthropic.com/news/model-context-protocol) (nov/2024)
- Spec version: `2025-11-25` (última consulta: Julho 2026)
