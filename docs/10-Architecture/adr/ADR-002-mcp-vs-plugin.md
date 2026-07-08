# ADR-002: Adoção de MCP (Model Context Protocol) vs Plugin Proprietário

> **Status**: Aceito · **Data**: Julho 2026 · **Autor**: [Nome]

## Contexto
Sistema precisa integrar 5+ fontes externas (arXiv, GitHub, Confluence, banco interno, search web). Decidir entre protocolo aberto ou interface proprietária.

## Decisão
Adotar **MCP** (Model Context Protocol, spec 2025-11-25) com servers customizados em FastMCP.

## Alternativas consideradas
- **Plugin proprietário**: rejeitado porque cada integração exigiria adapter próprio, sem reuso entre agentes.
- **Function calling direto**: rejeitado porque não há descoberta nem govemança padronizada.
- **A2A**: inadequado (A2A é para agente-agente, não agente-ferramenta).

## Consequências
- **Positivas**: protocolo aberto; servidores reutilizáveis; descoberta automática; ecossistema crescente.
- **Negativas**: maturidade media do ecossistema (2026); performance de transporte (Streamable HTTP).
- **Mitigação**: cache de respostas para tools read-heavy.

## Referências
- MCP Spec: `14-MCP/02-spec.md`
- ETHAGT08 — MCP & Tool Use
