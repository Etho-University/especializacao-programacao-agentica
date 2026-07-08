# ETHAGT08 — Lista de Exercícios

> Curso: MCP — Model Context Protocol. Fixação de conceitos. Use a apostila `04-Apostilas/ETHAGT08/apostila.md` como referência.

## Múltipla escolha

**1. Na arquitetura MCP, qual é o papel do "host"?**

a) Servidor de embeddings
b) A aplicação que o usuário usa (ex.: Claude Desktop, VSCode) e que instancia clients MCP
c) Um modelo de linguagem
d) Um vector database

**2. Qual é a diferença entre Tools, Resources e Prompts em MCP?**

a) São três nomes para a mesma coisa
b) Tools são funções com schema; Resources são dados estruturados; Prompts são templates reutilizáveis
c) Tools são para leitura; Resources para escrita; Prompts para cache
d) Tools são server-side; Resources são client-side; Prompts são host-side

**3. O mecanismo de "sampling" em MCP permite que:**

a) O servidor cacheie respostas
b) O servidor solicite inferência do LLM do host (server-initiated)
c) O cliente faça fine-tuning
d) O host restrinja tools

**4. Qual transporte NÃO é suportado nativamente por MCP?**

a) stdio
b) HTTP+SSE
c) Streamable HTTP
d) gRPC bidirecional com protobuf obrigatório

## Verdadeiro ou Falso (justificado)

**1.** "MCP substitui o tool calling nativo do LLM." — Justifique.

**2.** "Um MCP server é uma boundary de confiança — deve ser tratado com sandboxing e auditoria." — Justifique.

**3.** "Versionamento semântico de MCP servers é importante para não quebrar agentes em produção." — Justifique.

**4.** "Prompt injection via resources (documentos maliciosos em um MCP server) é um vetor de ataque real." — Justifique.

## Código curto

**1.** Escreva a config JSON para adicionar um MCP server ao Claude Desktop (server em Python via stdio, comando `python server.py`).

**2.** Escreva o esqueleto de um MCP server com `FastMCP` (Python SDK) que expõe uma tool `get_weather(city: str) -> str`.

**3.** Escreva o pseudocódigo de um mecanismo de rate limiting para um MCP server (máximo N chamadas por minuto por client).

## Análise de trade-off

**1.** Compare transporte stdio vs. HTTP+SSE para MCP servers. Quando escolher cada?

**2.** Compare um agente usando tools nativas (definidas no código) vs. tools via MCP server. Quando MCP vale a pena?

**3.** Compare supply chain security via SBOM/provenance vs. allowlist manual de servers. O que cada oferece?

## Debug / diagnóstico

**1.** Um MCP server conecta ao Claude Desktop mas as tools não aparecem. Liste 3 causas prováveis.

**2.** Um MCP server de filesystem expõe paths arbitrários — um documento malicioso instrui o modelo a ler `/etc/passwd`. Diagnóstico do risco e 2 mitigações.
