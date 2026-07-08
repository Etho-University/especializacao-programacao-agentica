# ETHAGT08 — MCP — Model Context Protocol — Slides

> Apresentação para aula síncrona · ~50 min · 13 slides

## Estrutura da aula
- Abertura (5 min): gancho/motivação
- Teoria (25 min): conceitos principais com diagramas de referência
- Demonstração (10 min): código ao vivo ou walkthrough de lab
- Exercício (5 min): questão rápida ou discussão
- Fechamento (5 min): conexão com próximo módulo, leitura recomendada

## Slides

### Slide 1 — Título
- ETHAGT08 — MCP — Model Context Protocol (servers, clients, hosts, governança)
- Professor, data, Universität Etho
- Pré-requisito: ETHAGT02
- ~1 min

### Slide 2 — Agenda
1. Por que MCP (o problema N×M)
2. Modelo de capabilities (tools, resources, prompts, sampling)
3. Construindo servers (SDK Python/TS)
4. Clients e hosts
5. Governança de ecossistema
6. Segurança e produção
- ~1 min

### Slide 3 — Gancho / Motivação
- Problema: N LLMs × M sistemas = N×M integrações customizadas
- Exemplo: mesmo sistema de arquivos precisa de adapter diferente para cada LLM
- A proposta: padrão aberto como "USB-C da IA" (Anthropic, nov/2024)
- Arquitetura: host · client · server
- Pergunta: *Quantas integrações diferentes vocês já fizeram para conectar LLMs a sistemas?*
- ~3 min

### Slide 4 — Arquitetura MCP
- Host (Claude Desktop, VSCode, OpenCode) — aplicação que inicia a conexão
- Client (por instância de host) — mantém conexão com o server
- Server (Filesystem, GitHub, Postgres) — expõe capabilities
- Transportes: stdio, HTTP+SSE, streamable HTTP
- Diagrama: `12-Diagrams/ETHAGT08/host-client-server.mmd`
- ~4 min

### Slide 5 — Modelo de Capabilities
- **Tools**: funções com JSON schema (alinhado ao ETHAGT02)
- **Resources**: dados estruturados (arquivos, DB rows, imagens)
- **Prompts**: templates reutilizáveis para o LLM
- **Sampling**: server pede ao LLM do host (server-initiated)
- Roots, notifications, subscriptions
- Diagrama: `12-Diagrams/ETHAGT08/capabilities.mmd`
- Pergunta: *Sampling: quando o server precisa gerar texto?*
- ~4 min

### Slide 6 — Construindo MCP Servers
- Python SDK: `FastMCP`, decorators (`@server.tool()`, `@server.resource()`)
- TypeScript SDK
- Exemplos práticos: filesystem (ler/escrever arquivos), GitHub (issues/PRs), Postgres (consultas)
- Testes de server (MCP inspector)
- Empacotamento e distribuição (pip, npm, container)
- ~4 min

### Slide 7 — DEMO: Meu Primeiro MCP Server
- Código ao vivo: construir server que expõe tools de consulta a dataset local
- Conectar ao OpenCode (ou Claude Desktop)
- Mostrar tool sendo chamada pelo LLM
- Adicionar resource (arquivo de configuração)
- Referência: `05-Labs/ETHAGT08/Lab1-Primeiro-MCP-Server`
- ~5 min

### Slide 8 — Clients e Hosts
- Como um host instancia clients (config JSON)
- Claude Desktop config: `mcpServers` no JSON
- VSCode MCP: extensões e settings
- OpenCode: `opencode.json` MCP configuration
- Integrar em agente custom (LangGraph, OpenAI Agents SDK)
- Pergunta: *Multi-server composition: um host com 5 servers — como o LLM escolhe?*
- ~4 min

### Slide 9 — Governança de Ecossistema
- Catálogo interno de servers (registro, descoberta)
- Versionamento semântico e compatibilidade
- Permissões por server/client (allowlists)
- Supply chain security: provenance, dependências, SBOM
- Auditoria e logs de chamadas MCP
- Diagrama: `12-Diagrams/ETHAGT08/governance.mmd`
- ~4 min

### Slide 10 — Segurança e Produção
- Server como boundary de confiança
- Sandboxing de servers (containers, permissões de SO)
- Prompt injection via resources (dados maliciosos no server)
- Rate limiting, quotas por usuário
- Casos reais: exfiltração de dados, tool misuse
- Pergunta: *Se um MCP server de arquivos permite ler qualquer path, como mitigar?*
- ~4 min

### Slide 11 — Exercício: Config e Segurança
- Cenário: adicionar um MCP server de banco de dados a um host
- Escrever a config JSON para Claude Desktop
- Listar 3 riscos de segurança e propor mitigação
- 3 min individual, 2 min compartilhar
- ~5 min

### Slide 12 — Conexão com Próximo Módulo
- ETHAGT13 — Segurança & Governança: aprofunda threat modeling e defesa
- ETHAGT90 — Capstone: projeto integrador com MCP
- Leitura: *Model Context Protocol Specification* (modelcontextprotocol.io)
- Anthropic *Introducing the Model Context Protocol* (nov/2024)
- ~2 min

### Slide 13 — Referências
- Anthropic. *Introducing the Model Context Protocol* (nov/2024)
- *Model Context Protocol Specification* (modelcontextprotocol.io)
- MCP SDKs (Python, TypeScript) — docs e código
- *Awesome MCP Servers* (catálogo comunitário)
- Cloudflare *Remote MCP servers*
- ~1 min
