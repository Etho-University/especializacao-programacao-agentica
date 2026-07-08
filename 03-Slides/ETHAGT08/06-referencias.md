# ETHAGT08 — Referências

> Todas as fontes utilizadas na preparação e apresentação da aula.

---

## Canônicas (fundação do curso)

### 1. Anthropic — Introducing the Model Context Protocol
- **Data**: novembro 2024
- **URL**: https://www.anthropic.com/news/model-context-protocol
- **Resumo**: Anúncio oficial do MCP como padrão aberto. Estabelece o problema N×M, a proposta host-client-server, e o ecossistema inicial. Base direta das Seções A e B da aula.
- **Importância**: Canônica
- **Slides que referenciam**: 1, 5, 6, 12, 58

### 2. Model Context Protocol Specification (2025-11-25)
- **URL**: https://modelcontextprotocol.io/specification/2025-11-25
- **Resumo**: Especificação oficial do protocolo MCP. Define JSON-RPC 2.0, capabilities (tools, resources, prompts, sampling, roots), transportes (stdio, Streamable HTTP), lifecycle, e OAuth 2.1. Base técnica de toda a aula.
- **Importância**: Canônica
- **Slides que referenciam**: 8, 9, 10, 11, 15, 16, 17, 18, 19, 20, 51

### 3. MCP Architecture
- **URL**: https://modelcontextprotocol.io/docs/learn/architecture
- **Resumo**: Documentação oficial sobre a arquitetura host-client-server. Explica papéis, transportes, e ciclo de vida. Base da Seção B.
- **Importância**: Canônica
- **Slides que referenciam**: 7, 8, 32

---

## Importantes (complementam e aprofundam)

### 4. MCP Python SDK (FastMCP)
- **URL**: https://github.com/modelcontextprotocol/python-sdk
- **Resumo**: SDK Python oficial. API `FastMCP` inspirada no FastAPI. Decorators `@tool`, `@resource`, `@prompt`. Referência direta para os exemplos de código da Seção D.
- **Importância**: Importante
- **Slides que referenciam**: 22, 23, 24, 29, 36

### 5. MCP TypeScript SDK
- **URL**: https://github.com/modelcontextprotocol/typescript-sdk
- **Resumo**: SDK TypeScript oficial. API `McpServer`. Mesmo runtime de VSCode, Cursor, OpenCode. Referência para o Slide 26.
- **Importância**: Importante
- **Slides que referenciam**: 26

### 6. Cloudflare — Remote MCP servers (2025)
- **URL**: https://developers.cloudflare.com/agents/guides/remote-mcp-server/
- **Resumo**: Guia da Cloudflare para deploy de MCP servers em Workers. Caso real de remote MCP com OAuth 2.1. Base para discussão de remote servers (Slides 9, 12, 28).
- **Importância**: Importante
- **Slides que referenciam**: 9, 12, 28, 51

### 7. Auth0 — Streamable HTTP Analysis (2025)
- **URL**: https://auth0.com/blog/using-streamable-http-with-mcp/
- **Resumo**: Análise técnica da transição de HTTP+SSE para Streamable HTTP em março/2025. Detalha single endpoint, session management, resumabilidade. Base do Slide 10.
- **Importância**: Importante
- **Slides que referenciam**: 9, 10

### 8. MCP Inspector
- **URL**: https://github.com/modelcontextprotocol/inspector
- **Resumo**: CLI interativo para testar MCP servers. Lista tools, executa chamadas, valida schemas. Ferramenta canônica de teste. Base do Slide 27.
- **Importância**: Importante
- **Slides que referenciam**: 27

### 9. langchain-mcp-adapters
- **URL**: https://github.com/langchain-ai/langchain-mcp-adapters
- **Resumo**: Biblioteca para carregar tools de servers MCP como `BaseTool` do LangChain. Habilita agentes custom como hosts MCP. Base do Slide 36.
- **Importância**: Importante
- **Slides que referenciam**: 36

### 10. Block — MCP in Production
- **Data**: 2025
- **Resumo**: Apresentações e posts da Block sobre arquitetura interna de MCP servers para dev tools. Caso real de governança enterprise. Base do Slide 58.
- **Importância**: Importante
- **Slides que referenciam**: 58

---

## Complementares (leitura opcional)

### 11. Awesome MCP Servers
- **URL**: https://github.com/punkpeye/awesome-mcp-servers
- **Resumo**: Catálogo comunitário de MCP servers. Referência para descoberta de servers existentes.
- **Importância**: Complementar
- **Slides que referenciam**: 12, 28, 40

### 12. Smithery
- **URL**: https://smithery.ai
- **Resumo**: Plataforma SaaS para registry e deploy de MCP servers. Alternativa a registry custom.
- **Importância**: Complementar
- **Slides que referenciam**: 12, 28, 40

### 13. mcp.run
- **URL**: https://mcp.run
- **Resumo**: Plataforma para rodar MCP servers remotamente. Caso de remote MCP gerenciado.
- **Importância**: Complementar
- **Slides que referenciam**: 12, 28

### 14. Google Cloud — Guides on MCP (2025)
- **Resumo**: Guias da Google Cloud sobre integração de MCP em Vertex AI. Confirma adoção multi-cloud.
- **Importância**: Complementar
- **Slides que referenciam**: 6, 12

### 15. Databricks — Guides on MCP (2025)
- **Resumo**: Guias da Databricks sobre uso de MCP para data tools. Caso enterprise de data lake.
- **Importância**: Complementar
- **Slides que referenciam**: 6

### 16. Replit — Agents with MCP
- **Data**: 2025
- **Resumo**: Posts da Replit sobre agentes que usam MCP para integração com serviços cloud. Caso real de multi-server composition.
- **Importância**: Complementar
- **Slides que referenciam**: 58

### 17. OWASP — Top 10 for LLM Applications
- **URL**: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- **Resumo**: Lista de riscos de segurança em aplicações LLM, incluindo prompt injection. Base conceitual para a Seção G.
- **Importância**: Complementar
- **Slides que referenciam**: 50, 53

### 18. OAuth 2.1 Draft
- **URL**: https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/
- **Resumo**: Draft do OAuth 2.1 (consolida best practices do OAuth 2.0). PKCE obrigatório. Base do Slide 51.
- **Importância**: Complementar
- **Slides que referenciam**: 51

---

## Documentação de Hosts

### 19. Claude Desktop — MCP Config
- **URL**: https://modelcontextprotocol.io/docs/quickstart/user
- **Resumo**: Documentação oficial sobre configuração de MCP servers no Claude Desktop. Base do Slide 33.
- **Importância**: Importante
- **Slides que referenciam**: 33

### 20. VSCode MCP
- **URL**: https://code.visualstudio.com/docs
- **Resumo**: Documentação do suporte MCP nativo no VSCode (Copilot Chat).
- **Importância**: Importante
- **Slides que referenciam**: 34

### 21. OpenCode MCP
- **Resumo**: Documentação do OpenCode sobre configuração de MCP servers. Mesma ferramenta usada no curso.
- **Importância**: Importante
- **Slides que referenciam**: 35

### 22. Cursor / Zed / Windsurf MCP
- **Resumo**: Documentação de suporte MCP em outros editores. Confirma adoção ampla.
- **Importância**: Complementar
- **Slides que referenciam**: 12, 34

---

## Documentação de Servers de Referência

### 23. @modelcontextprotocol/server-filesystem
- **URL**: https://github.com/modelcontextprotocol/servers
- **Resumo**: Server de filesystem de referência (TypeScript). Tools: read_file, write_file, list_directory, search_files. Base do Slide 24.
- **Importância**: Importante
- **Slides que referenciam**: 24, 33

### 24. @modelcontextprotocol/server-github
- **URL**: https://github.com/modelcontextprotocol/servers
- **Resumo**: Server de GitHub de referência. Tools: create_issue, list_prs, merge_pr, search_code. Base do Slide 25.
- **Importância**: Importante
- **Slides que referenciam**: 25

### 25. @modelcontextprotocol/server-postgres
- **URL**: https://github.com/modelcontextprotocol/servers
- **Resumo**: Server de Postgres de referência. Exemplo de integração com DB. Base do Slide 59.
- **Importância**: Complementar
- **Slides que referenciam**: 59

---

## Conexão com ETHAGT02

### 26. Anthropic — Writing Effective Tools for AI Agents
- **Data**: 2025
- **URL**: https://www.anthropic.com/engineering/writing-tools-for-agents
- **Resumo**: Guia de design de tools (ACI). Princípios aplicam diretamente ao design de tools MCP. Reforça a conexão entre tool calling nativo e MCP.
- **Importância**: Importante
- **Slides que referenciam**: 16, 23, 38, 56

---

## Ficha de Pesquisa

- **Arquivo**: `20-Research/ETHAGT08-pesquisa.md`
- **Última consulta**: Julho 2026 (spec 2025-11-25)
- **Revalidação**: Janeiro 2027 (spec MCP evolui — sempre verificar modelcontextprotocol.io/specification)

---

> **Mantido por**: Universidade Etho · Versão 1.0 · Julho 2026
> **Spec de referência**: MCP Specification 2025-11-25 (modelcontextprotocol.io)
