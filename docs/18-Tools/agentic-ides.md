# Agentic IDEs

| Ferramenta | Licença | Modelo mental | Quando escolher | Quando evitar |
|---|---|---|---|---|
| **OpenCode** | open source | CLI agnóstico com MCP | automação terminal, pipelines | GUI rica necessária |
| **Claude Code** | comercial (Anthropic) | CLI integrado ao Claude | coding agent Claude | não-Claude |
| **Cursor** | comercial | IDE com AI nativa | desenvolvimento com AI assistente | custo alto em volume |
| **VSCode + MCP** | open + plugins | IDE extensível via MCP | times que já usam VSCode | setup mais complexo |
| **Zed** | open source | editor performático com AI | performance + AI | ecossistema menor |

## Comparativo

- **Autonomia**: Cursor > Claude Code > VSCode+MCP > OpenCode (depende do uso).
- **Custo**: OpenCode/VSCode (open) < Cursor (assinatura) < Claude Code (API).
- **Extensibilidade via MCP**: todos suportam; OpenCode e VSCode são mais flexíveis.
- **Internacionalização**: todos em EN; UI não localizada.

## Quando usar qual

- **Dev solo, custo consciente**: OpenCode ou VSCode+MCP.
- **Time que adota Cursor**: Cursor.
- **Coding agent robusto (Claude)**: Claude Code.
- **Automação CI/CD**: OpenCode (headless).

## Referências

- Sites oficiais e repositórios GitHub de cada.
