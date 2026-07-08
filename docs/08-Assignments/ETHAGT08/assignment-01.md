# ETHAGT08 — Avaliação do Módulo

> Curso: MCP — Model Context Protocol (servers, clients, hosts, governança) · Nota mínima de aprovação: 3,0

## Composição da nota (4 pilares)

| Pilar | Peso | Instrumento |
|---|---|---|
| Técnico | 40% | MCP server funcional + threat model |
| Consultivo | 30% | Apresentação do server como produto |
| Comportamental | 20% | Code review |
| Prático | 10% | Demo: server rodando em host real (Claude Desktop/OpenCode/VSCode) |

**Nota final** = Σ(pilar × peso).

---

## Rubrica — Pilar Técnico (40%)

O projeto exige projetar e construir um MCP server útil (ex.: Confluence Etho, SAP OData, Salesforce) com ≥3 tools/resources/prompts e governança (permissões, logs, versionamento), além de um threat model documentando riscos e mitigações.

| Critério | Peso | 1 (muito abaixo) | 3 (esperado) | 5 (referência) |
|---|---|---|---|---|
| Correção técnica | 25% | Server não funciona ou não segue a especificação MCP | Server funcional com ≥3 tools; conecta a um host real; capabilities (tools/resources/prompts) corretas | ≥3 tools + resources + prompts + sampling (se aplicável); casos de borda (timeout, client desconecta, tool com erro) tratados |
| Qualidade arquitetural | 25% | Sem separação; server monolítico; sem governança | Separação razoável de capabilities; config de permissões básica | Arquitetura limpa (capabilities modularizadas), versionamento semântico, supply chain security (SBOM, provenance), ADR de governança |
| Profundidade | 20% | Superficial; não entende host/client/server | Diferencia tool/resource/prompt/sampling; justifica transporte (stdio vs HTTP+SSE) | Discute trade-offs (MCP vs tool calling nativo, quando sampling vale), governança de ecossistema (catálogo, auditoria) |
| Produção-ready | 15% | Server não empacotado; sem docs | Server empacotado; docs de instalação; conecta a Claude Desktop/OpenCode | Docker + testes de server + docs open-source-ready + config JSON exemplo + distribuição (pip/npm) |
| Avaliação/observabilidade | 15% | Sem threat model nem logs | Threat model com ≥5 riscos identificados; logs de auditoria | Threat model completo (STRIDE), sandboxing de server, rate limiting, análise de prompt injection via resources |

**Threat model** (parte do Pilar Técnico): documento estruturado modelando ameaças ao server (superfícies de ataque, vetores de prompt injection via resources, exfiltração) com mitigações. Peso: 40% do pilar técnico.

---

## Critérios dos demais pilares

- **Consultivo (30%):** Apresentação do server como produto para um "cliente" (banca).
  - *1:* Apresenta sem justificar valor nem governança.
  - *3:* Demonstra valor do server, explica capabilities e governança básica.
  - *5:* Articula o problema N×M que MCP resolve, mostra governança (permissões, auditoria), posiciona no ecossistema.

- **Comportamental (20%):** Code review do MCP server de um colega.
  - *1:* Comentários ausentes ou genéricos.
  - *3:* ≥5 observações sobre aderência à especificação, tratamento de erro e segurança.
  - *5:* Identifica riscos de segurança (prompt injection via resources), sugere sandboxing, avalia governança.

- **Prático (10%):** Demo: server rodando em host real (Claude Desktop, OpenCode ou VSCode).
  - *1:* Server não conecta ao host na demo.
  - *3:* Server conecta, responde a ≥2 tools, logs visíveis.
  - *5:* Mostra composição multi-server, rate limiting em ação, HITL para tool destrutiva.

---

## Regras

- Entrega: repositório Git com server, docs, ADR de governança (`./docs/adr-001-governance.md`) e threat model (`./docs/threat-model.md`).
- **Integridade acadêmica:** o server deve ser autoral. Uso de SDKs oficiais é esperado; cópia de servers públicos sem atribuição é plágio (nota 1,0).
- Atraso: -0,5 ponto por dia útil, até 3 dias.
