# ETHAGT08 — Projeto do Módulo: MCP Server com Governança

> Curso: MCP — Model Context Protocol (servers, clients, hosts, governança) · Pilar: Técnico 40% + Prático 10% · Equipe: individual ou dupla

## Contexto / Cenário

A equipe de Platform Engineering de uma empresa de saúde digital precisa expor dados de sistemas internos (Confluence para documentação clínica, sistema de prontuários via API FHIR, Salesforce para dados de pacientes) para múltiplos agentes e hosts (Claude Desktop, VSCode, agentes custom em LangGraph). Hoje, cada agente integra com cada sistema via código ad-hoc — o pesadelo N×M. A direção adotou o Model Context Protocol como padrão e quer um MCP server de referência, com governança adequada: catálogo versionado, permissões por server/client, logs de auditoria, e um threat model que documente riscos de exfiltração e prompt injection via resources. O servidor deve ser *open-source-ready*: código limpo, testes, documentação e empacotamento.

## Objetivo

Projetar e construir um MCP server útil (ex.: Confluence Etho, SAP OData, Salesforce, ou sistema interno de domínio do aluno) exposto via Python SDK (FastMCP) ou TypeScript SDK, com ≥3 capabilities (tools, resources, prompts). Aplicar governança completa (catálogo, permissões, versionamento, auditoria) e produzir um threat model documentando riscos e mitigações.

## Requisitos

### Funcionais

1. MCP server com ≥3 tools (funções com schema), ≥1 resource (dados estruturados) e ≥1 prompt template reutilizável.
2. Integração com uma fonte de dados real ou mockada (API REST, DB, filesystem).
3. Server conectável a um host real (Claude Desktop, OpenCode, VSCode MCP) — demonstrado em pelo menos um host.
4. Composição multi-server: server funciona ao lado de outro MCP server no mesmo host.
5. Governança: catálogo interno (README/manifesto), versionamento semântico, permissões documentadas por tool/client.
6. Auditoria: logs estruturados de toda chamada (cliente, tool, input, output, timestamp).

### Não-funcionais

- Server empacotado e distribuível (Docker ou pip/npm package).
- Testes automatizados para tools (≥80% de cobertura das funções de tool).
- Sandboxing mínimo: server roda com credenciais limitadas (least privilege).
- Rate limiting configurável por tool.
- Documentação de onboarding: como adicionar o server a um host em <5 minutos.

## Entregáveis

- Código (repositório open-source-ready: README, LICENSE, testes, CI).
- Documentação de governança (catálogo, permissões, versionamento, processo de atualização).
- ADR de governança (decisões de boundaries de confiança, transportes, supply chain).
- Threat model (STRIDE ou equivalente) documentando riscos e mitigações.
- Demo: server rodando em um host real (Claude Desktop, OpenCode ou VSCode).

## Critérios de sucesso (mensuráveis)

- Server funcional com ≥3 tools, ≥1 resource e ≥1 prompt, conectável a um host real.
- Threat model documenta ≥8 riscos identificados com mitigações propostas (≥80% dos críticos mitigados).
- Testes automatizados passam em CI com cobertura ≥80% das funções de tool.
- Governança documentada: catálogo versionado, permissões explícitas, processo de auditoria.
- Onboarding reproduzível: avaliador consegue conectar o server a um host seguindo a documentação em <10 minutos.

## Competências avaliadas

- C1 Programação Agêntica — nível **A** (integração MCP em sistemas agênticos).
- C2 Multi-Agent Systems — nível **B** (composição multi-server).
- C3 MCP & Tool Use — nível **A** (construção de server, capabilities, transportes).
- C5 AgentOps & Avaliação — nível **B** (testes, CI, auditoria, observabilidade).
- C6 Agent Security — nível **I** (threat model, sandboxing, supply chain, rate limiting).

## Referências

- Apostila: `04-Apostilas/ETHAGT08/apostila.md`
- Rubrica técnica: `08-Assignments/ETHAGT08/assignment-01.md`
