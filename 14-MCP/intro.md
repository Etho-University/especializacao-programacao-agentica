# MCP — Introdução

## O que é

O **Model Context Protocol** (MCP) é um **padrão aberto** anunciado pela Anthropic em novembro de 2024 para conectar LLMs a fontes de dados e ferramentas de forma padronizada. Freqüentemente chamado de "USB-C da IA".

## O problema que resolve

Antes do MCP, integrar N LLMs a M sistemas exigia **N×M integrações custom**. Cada provedor (OpenAI, Anthropic, Google) tinha seu formato; cada sistema precisava de conector por provedor.

MCP propõe uma camada padrão: servers expõem capacidades; clients consomem; hosts gerenciam. **N+M em vez de N×M.**

## Arquitetura: 3 papéis

| Papel | Função | Exemplos |
|---|---|---|
| **Host** | abriga o LLM, instancia clients | Claude Desktop, VSCode, OpenCode, Cursor |
| **Client** | 1 por server; ponte dentro do host | (transparente) |
| **Server** | processo independente que expõe capacidades | github-mcp, filesystem-mcp |

```
HOST (Claude Desktop)
├── Client A ─► Server A (GitHub)
└── Client B ─► Server B (Postgres)
```

## Capacidades

- **Tools**: ações com schema (o tipo mais comum).
- **Resources**: dados por URI (leitura).
- **Prompts**: templates reutilizáveis.
- **Sampling**: server-initiated LLM call (controle invertido).

## Por que importa

1. **Padronização** reduz N×M para N+M.
2. **Descoberta dinâmica**: host pergunta ao server suas capacidades.
3. **Isolamento**: server é processo separado (falha isolada).
4. **Multi-host**: um server serve múltiplos hosts.
5. **Ecossistema**: milhares de servers públicos; adoção por Claude, OpenAI, Google, Block, Replit, etc.

## Adoção (desde nov/2024)

Suporte nativo em: Claude Desktop / Claude Code, VSCode (via extensão), Cursor, OpenCode, Zed. OpenAI e Google adicionaram suporte em 2025.

## Próximos passos

- [`specification.md`](specification.md): detalhes técnicos.
- [`building-servers.md`](building-servers.md): construir seu primeiro server.
- Curso `ETHAGT08`: aprofundamento completo.
