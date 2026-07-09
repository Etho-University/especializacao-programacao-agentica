---
password: Etho-Prof-2026
---
# ETHAGT08 — Prova do Módulo: MCP — Model Context Protocol

> Universidade Etho · Versão 1.0 · Julho 2026
> Duração: ~60 min · 10 questões · closed book · Pilar Técnico (40%)

Esta prova avalia o Model Context Protocol: arquitetura host/client/server, modelo de capabilities, construção de servers, governança de ecossistema e segurança.

---

## Parte 1 — Conceitos (Q1-4)

**1. (Múltipla escolha)** Quais são os três papéis da arquitetura MCP?
- (a) LLM · API · Database
- (b) Host · Client · Server
- (c) Producer · Consumer · Broker
- (d) Tool · Resource · Prompt

**2. (V/F justificado)** "MCP substitui o tool calling nativo do LLM (function calling)."

**3. (Múltipla escolha)** Qual capability do MCP é **server-initiated** (o servidor pede ao LLM do host para gerar)?
- (a) Tools
- (b) Resources
- (c) Prompts
- (d) Sampling

**4. (V/F justificado)** "Um resource (ex.: um arquivo ou row de DB) pode conter instruções maliciosas que, lidas pelo LLM, o manipulam — isso é prompt injection via resources."

---

## Parte 2 — Aplicação e trade-off (Q5-8)

**5. (Trade-off)** Diferencie os transportes stdio e Streamable HTTP. Dê um cenário para cada.

**6. (Análise de capabilities)** Diferencie Tools, Resources e Prompts em MCP. Dê um exemplo de quando usar cada.

**7. (Debug de governança)** Uma organização adotou MCP sem catálogo centralizado, sem permissões por servidor e sem versionamento. Liste 3 problemas concretos que surgirão em escala.

**8. (V/F justificado)** "Supply chain security em MCP servers inclui provenance, SBOM (Software Bill of Materials), scanning de vulnerabilidades e pinning de versões."

---

## Parte 3 — Projeto curto (Q9-10)

**9. (Projeto curto)** Escreva a config JSON para adicionar 2 servidores MCP (um Python local `etho-arxiv` e um `github` via `npx`) ao Claude Desktop / OpenCode.

**10. (Projeto curto)** Liste 5 riscos de segurança de um MCP server (Capítulo 7) e dê a mitigação canônica para cada um.

---

## Critérios de correção (resumo)

| Conceito | Questões | Peso |
|---|---|---|
| Arquitetura host/client/server | 1, 5 | 20% |
| Modelo de capabilities | 3, 6 | 20% |
| Governança | 7, 8 | 20% |
| Segurança | 4, 10 | 25% |
| Configuração & integração | 2, 9 | 15% |

**Conversão**: cada questão vale 10 pts; total 100 pts. Nota 1-5.
- 90+ pts: 5,0
- 75-89: 4,0
- 60-74: 3,0 (mínimo aprovação)
- <60: reprovação.

Gabarito comentado em [`gabarito.md`](gabarito.md).
