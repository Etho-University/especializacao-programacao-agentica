---
tags:
  - ETHAGT08
  - syllabus
  - mcp
  - protocolo
---

# `ETHAGT08` — MCP — Model Context Protocol

> Fase C · Carga 25 h · Versão 1.0 · Julho 2026

## 1. Identificação

| Campo | Valor |
|---|---|
| Código | `ETHAGT08` |
| Título | MCP — Model Context Protocol (servers, clients, hosts, governança) |
| Fase interna | C — Multi-Agentes, Ferramentas e Orquestração |
| Carga horária | 25 h |
| Pré-requisitos | `ETHAGT02` |
| Módulos que dependem deste | `ETHAGT13`, `ETHAGT90` |

## 2. Objetivos

**Objetivo geral**: Dominar o **Model Context Protocol** — arquitetura client-server-host, construção de servers, integração com clients/hosts, governança de ecossistema e segurança.

**Objetivos específicos**:
1. Explicar a arquitetura MCP e seu papel como "USB-C da IA".
2. Construir MCP servers (Python e/ou TS SDK) com tools, resources, prompts.
3. Integrar servers a hosts (Claude Desktop, VSCode, OpenCode, agentes custom).
4. Aplicar governança: catálogo, permissões, versionamento, supply chain.
5. Avaliar riscos e mitigar (sandboxing, auditoria).

## 3. Competências desenvolvidas

| Competência | Nível ao final |
|---|---|
| C1 Programação Agêntica | **A** |
| C2 Multi-Agent Systems | B |
| C3 MCP & Tool Use | **A** |
| C5 AgentOps & Avaliação | B |
| C6 Agent Security | **I** |

## 4. Conteúdo programático

### Unidade 1 — Por que MCP (3 h)
- O problema: N×M integrações LLM ↔ sistemas
- A proposta: padrão aberto (Anthropic, nov/2024)
- Arquitetura: host (Claude, VSCode) · client (por host) · server (dados/tools)
- Transportes: stdio, HTTP+SSE, streamable HTTP
- Ecossistema atual

### Unidade 2 — O modelo de capabilities (4 h)
- **Tools**: funções com schema (alinhado ao `ETHAGT02`)
- **Resources**: dados estruturados (arquivos, DB rows)
- **Prompts**: templates reutilizáveis
- **Sampling**: server pede ao LLM do host (server-initiated)
- Roots, notifications, subscriptions

### Unidade 3 — Construindo servers (5 h)
- Python SDK: `FastMCP`, decorators
- TypeScript SDK
- Exemplos: filesystem, GitHub, Postgres, HTTP
- Testes de server
- Empacotamento e distribuição

### Unidade 4 — Clients e hosts (4 h)
- Como um host instancia clients
- Claude Desktop config; VSCode MCP; OpenCode
- Integrar em agente custom (LangGraph, OpenAI Agents SDK)
- Multi-server composition

### Unidade 5 — Governança de ecossistema (5 h)
- Catálogo interno de servers
- Versionamento (semântico) e compatibilidade
- Permissões por server/client
- Supply chain security: provenance, dependências,SBOM
- Auditoria e logs

### Unidade 6 — Segurança e produção (4 h)
- Server como boundary de confiança
- Sandboxing de servers
- Prompt injection via resources
- Rate limiting, quotas
- Casos reais: exfiltração, tool misuse

## 5. Bibliografia

### Fundamental
- Anthropic. *Introducing the Model Context Protocol* (nov/2024).
- *Model Context Protocol Specification* (modelcontextprotocol.io).
- MCP SDKs (Python, TypeScript) — documentação e código.

### Complementar
- *Awesome MCP Servers* (catálogo comunitário).
- Cloudflare *Remote MCP servers*.

## 6. Papers / docs canônicos

- Especificação MCP oficial (versão atual)
- Anthropic announcement blog (nov/2024)
- Databricks, Google Cloud — guias sobre MCP (2025)

## 7. Laboratórios

- **Lab 1** (4 h): "Meu primeiro MCP server". Construir um server expõe tools de consulta a um dataset; conectar ao Claude Desktop / OpenCode.
- **Lab 2** (5 h): "MCP server para arXiv + GitHub". Composição multi-server em um agente.

## 8. Projeto do módulo

**Descrição**: projetar e construir um **MCP server útil** (ex.: Confluence Etho, SAP OData, Salesforce) com governança (permissões, logs, versionamento).
**Entrega**: server open-source-ready + docs + ADR de governança + threat model.
**Critério de sucesso**: server funcional com ≥3 tools; threat model documenta riscos e mitigações.

## 9. Exercícios

1. Diferencie tool, resource e prompt em MCP.
2. Quando usar sampling (server-initiated)?
3. Escreva a config JSON para adicionar um server ao Claude Desktop.
4. Liste 5 riscos de segurança de um MCP server.
5. Verdadeiro/falso: "MCP substitui o tool calling nativo do LLM."

## 10. Avaliação

| Pilar | Peso | Instrumento |
|---|---|---|
| Técnico | 40% | Server + threat model |
| Consultivo | 30% | Apresentação do server como produto |
| Comportamental | 20% | Code review |
| Prático | 10% | Demo: server rodando em host real |

**Nota mínima**: 3,0.

## 11. Slides

- Slides: `03-Slides/ETHAGT08-slides.md` (~70 slides).

## 12. Leitura complementar

- Anthropic *MCP*; especificação; Cloudflare remote MCP.

## 13. Ferramentas

- Python/TS MCP SDK, Claude Desktop, VSCode MCP, OpenCode, Docker.

## 14. Diagramas

- Diagramas: `12-Diagrams/ETHAGT08/` — host-client-server.mmd, capabilities.mmd, governance.mmd.

## 15. Estudo de caso

- ecossistema MCP em produção (Anthropic, Block, Replit).

## 16. Ficha de pesquisa

- Ficha: `20-Research/ETHAGT08-pesquisa.md`.

---

*Mantido por: Universidade Etho · Versão 1.0 · Julho 2026*
