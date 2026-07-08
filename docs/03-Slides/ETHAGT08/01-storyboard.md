# ETHAGT08 — MCP — Model Context Protocol
## Storyboard da Apresentação

> **Universidade Etho · Especialização em Programação Agêntica**
> Fase C — Multi-Agentes, Ferramentas e Orquestração · 25 h
> Storyboard v1.0 · Julho 2026

---

## Metadados da Apresentação

| Campo | Valor |
|---|---|
| Código | ETHAGT08 |
| Título | MCP — Model Context Protocol (servers, clients, hosts, governança) |
| Duração estimada | 90 min (2 blocos de 45 min) |
| Total de slides | 70 |
| Público | Arquitetos, Engenheiros de Software, Engenheiros de IA, DevOps/SRE, Tech Leads |
| Pré-requisitos | ETHAGT02 |
| Competências | C1 (A), C2 (B), C3 (A), C5 (B), C6 (I) |
| Spec de referência | MCP Specification 2025-11-25 |
| Laboratórios | Lab 1 (4 h) — Primeiro MCP Server · Lab 2 (5 h) — Multi-server (arXiv + GitHub) |

---

## Mapa Visual da Apresentação

```
BLOCO 1 (45 min)                              BLOCO 2 (45 min)
┌──────────────────────────────┐              ┌──────────────────────────────┐
│ SEÇÃO A — Abertura (8 min)   │              │ SEÇÃO E — Clients/Hosts(10m) │
│  Capa · Objetivos · Agenda   │              │  Host · Client · Config JSON │
│  Motivação N×M · Contexto    │              │  Claude · VSCode · OpenCode  │
├──────────────────────────────┤              │  Agente custom · Multi-srv   │
│ SEÇÃO B — Arquitetura (10m)  │              ├──────────────────────────────┤
│  Host-Client-Server          │              │ SEÇÃO F — Governança (10 min)│
│  Transportes · Streamable HTTP│             │  Catálogo · Versionamento    │
│  Ciclo de vida · Ecossistema │              │  Permissões · SBOM · Auditoria│
├──────────────────────────────┤              ├──────────────────────────────┤
│ SEÇÃO C — Capabilities (12m) │              │ SEÇÃO G — Segurança (10 min) │
│  Tools · Resources · Prompts │              │  Boundary · Sandbox          │
│  Sampling · Roots/Notif/Subs │              │  Prompt injection · OAuth 2.1│
├──────────────────────────────┤              │  Rate limit · Casos reais    │
│ SEÇÃO D — Servers (15 min)   │              ├──────────────────────────────┤
│  FastMCP · Decorators        │              │ SEÇÃO H — Fechamento (15 min)│
│  Exemplos · TS SDK · Testes  │              │  Boas práticas · Anti-patterns│
│  Empacotamento · DEMO        │              │  Exercício · Resumo · Quiz   │
└──────────────────────────────┘              │  Projeto · Labs · Next · Q&A │
                                              └──────────────────────────────┘
```

---

## Storyboard Detalhado

### SEÇÃO A — Abertura (Slides 1-6 · 8 min)

---

#### Slide 1 — Capa
- **Tipo**: Capa
- **Objetivo**: Identificar a aula, professor e contexto
- **Conteúdo**:
  - ETHAGT08 — MCP — Model Context Protocol
  - Universidade Etho · Especialização em Programação Agêntica
  - Fase C — Multi-Agentes, Ferramentas e Orquestração
  - Professor · Data
  - Spec de referência: 2025-11-25
- **Diagrama**: Logo Etho + imagem de fundo (conectores USB-C / rede de nós)
- **Animação**: Fade in do título
- **Tempo**: 1 min

---

#### Slide 2 — Objetivos do Módulo
- **Tipo**: Conteúdo
- **Objetivo**: Deixar claro o que o aluno deve conseguir fazer ao final
- **Conteúdo**:
  - Objetivo geral: Dominar o Model Context Protocol — arquitetura, servers, clients, governança e segurança
  - 5 objetivos específicos (1 linha cada):
    1. Explicar a arquitetura MCP e seu papel como "USB-C da IA"
    2. Construir MCP servers (Python e/ou TS SDK) com tools, resources, prompts
    3. Integrar servers a hosts (Claude Desktop, VSCode, OpenCode, agentes custom)
    4. Aplicar governança: catálogo, permissões, versionamento, supply chain
    5. Avaliar riscos e mitigar (sandboxing, auditoria, OAuth)
- **Diagrama**: Ícones representando cada objetivo (plug, server, config, shield, lock)
- **Animação**: Aparecer objetivos um a um (on click)
- **Tempo**: 2 min

---

#### Slide 3 — Competências Desenvolvidas
- **Tipo**: Conteúdo
- **Objetivo**: Conectar a aula ao Framework Etho de competências
- **Conteúdo**:
  - Tabela: 5 competências com nível B/I/A
  - C1 Programação Agêntica → A
  - C2 Multi-Agent Systems → B
  - C3 MCP & Tool Use → A
  - C5 AgentOps & Avaliação → B
  - C6 Agent Security → I
  - Badge visual por competência
- **Diagrama**: Radar chart dos 5 pilares
- **Animação**: Radar aparece com wipe
- **Tempo**: 1 min

---

#### Slide 4 — Agenda
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar o roteiro da aula com tempos
- **Conteúdo**:
  - Bloco 1: Abertura → Arquitetura → Capabilities → Construindo Servers
  - Bloco 2: Clients/Hosts → Governança → Segurança → Fechamento
  - Tempos estimados por seção
  - 2 DEMOs marcadas no roteiro
- **Diagrama**: Timeline horizontal com 8 seções
- **Animação**: Timeline cresce da esquerda para direita
- **Tempo**: 1 min

---

#### Slide 5 — Motivação: O Problema N×M
- **Tipo**: Conteúdo
- **Objetivo**: Criar tensão — cada LLM precisa de adapter custom para cada sistema
- **Conteúdo**:
  - Cenário: 5 LLMs × 10 sistemas = 50 integrações customizadas
  - Mesmo sistema de arquivos precisa de adapter diferente para cada LLM
  - Custo de manutenção explode; fragmentação de ecossistema
  - Pergunta: *Quantas integrações diferentes vocês já fizeram para conectar LLMs a sistemas?*
- **Diagrama**: Grid N×M (LLMs de um lado, sistemas do outro, linhas cruzando)
- **Animação**: Linhas aparecem uma a uma até virar "cabelo de sogra"
- **Tempo**: 2 min

---

#### Slide 6 — Contexto: O Nascimento do MCP
- **Tipo**: Conteúdo
- **Objetivo**: Explicar a confluência histórica que motivou o MCP
- **Conteúdo**:
  - Linha do tempo: 2023 (tool calling nativo) → nov/2024 (Anthropic anuncia MCP) → 2025 (spec evolution, Streamable HTTP) → nov/2025 (spec 2025-11-25)
  - Confluência: tool calling maduro + necessidade de padrão + ecossistema fragmentado
  - Analogia: "USB-C da IA" — um conector para tudo
  - Adotantes: Anthropic, Block, Replit, Cloudflare, Zed, Microsoft (VSCode)
- **Diagrama**: Timeline horizontal com marcos
- **Animação**: Marcos aparecem sequencialmente
- **Tempo**: 1 min

---

### SEÇÃO B — Arquitetura MCP (Slides 7-13 · 10 min)

---

#### Slide 7 — [SEÇÃO] Por que MCP — O USB-C da IA
- **Tipo**: Seção
- **Objetivo**: Transição para o bloco de arquitetura
- **Conteúdo**: Número "1" grande + "Arquitetura MCP"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 8 — A Arquitetura Host-Client-Server
- **Tipo**: Diagrama
- **Objetivo**: Apresentar a decomposição canônica do MCP
- **Conteúdo**:
  - **Host**: aplicação que inicia a conexão (Claude Desktop, VSCode, OpenCode)
  - **Client**: instância por server, mantida pelo host (1:1 com server)
  - **Server**: processo que expõe capabilities (Filesystem, GitHub, Postgres)
  - Host pode instanciar múltiplos clients → múltiplos servers
  - LLM vive no host; server não tem acesso direto ao LLM (exceto via sampling)
- **Diagrama**: `12-Diagrams/ETHAGT08/host-client-server.mmd`
- **Animação**: Componentes surgem do centro (Host) para fora
- **Tempo**: 3 min

---

#### Slide 9 — Transportes: stdio, HTTP+SSE, Streamable HTTP
- **Tipo**: Comparação
- **Objetivo**: Mostrar os 3 transportes e quando usar cada
- **Conteúdo**:
  - **stdio**: processo local, stdin/stdout — simples, sem rede
  - **HTTP+SSE** (deprecated na spec 2025-11-25): HTTP POST + Server-Sent Events
  - **Streamable HTTP** (atual): single endpoint, POST para requests, opcional SSE stream
  - Tabela: latência, segurança, depuração, deploy
- **Diagrama**: 3 colunas comparativas com ícones de transporte
- **Animação**: Colunas aparecem uma a uma
- **Tempo**: 2 min

---

#### Slide 10 — Streamable HTTP em Detalhe (spec 2025-11-25)
- **Tipo**: Diagrama
- **Objetivo**: Aprofundar o transporte canônico atual
- **Conteúdo**:
  - Single endpoint: `POST /mcp`
  - Cliente envia JSON-RPC 2.0 sobre HTTP
  - Resposta pode ser: JSON direto (síncrono) ou SSE stream (para notificações/long-running)
  - Session management via header `Mcp-Session-Id`
  - Suporte a resumabilidade (stream replay via `Last-Event-ID`)
  - Vantagem sobre HTTP+SSE: um endpoint, não dois
- **Diagrama**: Diagrama de sequência cliente ↔ server
- **Animação**: Mensagens aparecem sequencialmente
- **Tempo**: 2 min

---

#### Slide 11 — O Ciclo de Vida de uma Conexão MCP
- **Tipo**: Diagrama
- **Objetivo**: Mostrar as fases de uma conexão MCP
- **Conteúdo**:
  - 1. **Initialize**: cliente envia `initialize` com protocolVersion + capabilities
  - 2. **Initialized**: cliente confirma com `notifications/initialized`
  - 3. **Operation**: tools/list, resources/list, prompts/list, tool calls, etc.
  - 4. **Shutdown**: cliente fecha conexão (stdio: fecha processo; HTTP: delete session)
  - Negociação de versão de protocolo (cliente pede, server responde com a versão suportada)
- **Diagrama**: Fluxograma de ciclo de vida
- **Animação**: Fases aparecem sequencialmente
- **Tempo**: 1.5 min

---

#### Slide 12 — Ecossistema MCP Atual
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar a maturidade do ecossistema
- **Conteúdo**:
  - Servers de referência: filesystem, git, github, postgres, google-drive, slack, brave-search
  - Hosts: Claude Desktop, VSCode (Copilot), OpenCode, Zed, Cursor, Windsurf
  - SDKs: Python (FastMCP), TypeScript, Go (comunitário), Rust (comunitário)
  - Remote servers: Cloudflare Workers MCP, Smithery, mcp.run
  - Catálogos: Awesome MCP Servers, modelcontextprotocol.io/servers
- **Diagrama**: Mind map com hubs (Hosts, Servers, SDKs, Infra)
- **Animação**: Ramos aparecem um a um
- **Tempo**: 1 min

---

#### Slide 13 — Pergunta: Onde o MCP se Encaixa na Sua Stack?
- **Tipo**: Exercício
- **Objetivo**: Engajar a turma a pensar na aplicabilidade
- **Conteúdo**:
  - "Qual sistema da sua empresa você transformaria em MCP server primeiro?"
  - "Quais dados você NÃO exporia via MCP server?"
  - Discussão em duplas (2 min)
- **Diagrama**: Caixa de discussão
- **Tempo**: 2 min

---

### SEÇÃO C — Modelo de Capabilities (Slides 14-20 · 12 min)

---

#### Slide 14 — [SEÇÃO] O Modelo de Capabilities
- **Tipo**: Seção
- **Objetivo**: Transição para o bloco de capabilities
- **Conteúdo**: "2 — O Modelo de Capabilities"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 15 — Visão Geral das Capabilities
- **Tipo**: Diagrama
- **Objetivo**: Apresentar as 4+ capabilities canônicas do MCP
- **Conteúdo**:
  - **Tools**: funções com JSON schema (host → server) — alinhado ao ETHAGT02
  - **Resources**: dados estruturados identificados por URI (host → server)
  - **Prompts**: templates reutilizáveis para o LLM (host → server)
  - **Sampling**: server pede ao LLM do host (server → host, server-initiated)
  - Extras: Roots, Notifications, Subscriptions, Elicitation
- **Diagrama**: `12-Diagrams/ETHAGT08/capabilities.mmd`
- **Animação**: Cada capability surge do centro
- **Tempo**: 2 min

---

#### Slide 16 — Tools: Funções com JSON Schema
- **Tipo**: Conteúdo
- **Objetivo**: Detalhar a capability mais usada
- **Conteúdo**:
  - Tool = nome + descrição + inputSchema (JSON Schema) + callback
  - Fluxo: LLM decide chamar → host executa via client → server processa → resultado volta ao LLM
  - Alinhado ao tool calling do ETHAGT02, mas padronizado pelo MCP
  - Exemplo de schema: `read_file(path: string)` com descrição rica
  - Diferença vs tool calling nativo: MCP padroniza o protocolo, não o modelo
- **Diagrama**: Fluxo: LLM → tool_call → client → server → result → LLM
- **Animação**: Fluxo step-by-step
- **Tempo**: 2 min

---

#### Slide 17 — Resources: Dados Estruturados
- **Tipo**: Conteúdo
- **Objetivo**: Diferenciar resources de tools
- **Conteúdo**:
  - Resource = URI + nome + descrição + mimeType + conteúdo (text ou blob)
  - Identificados por URI: `file:///path`, `postgres://table/row`, `github://issue/42`
  - Host pode listar (`resources/list`) e ler (`resources/read`)
  - Templates: `resource://users/{id}` — URI com variáveis
  - Casos: arquivos, linhas de DB, issues, imagens, configurações
  - Resource ≠ Tool: resource é dado (passivo), tool é ação (ativa)
- **Diagrama**: Comparação Resource (dado) vs Tool (ação)
- **Tempo**: 2 min

---

#### Slide 18 — Prompts: Templates Reutilizáveis
- **Tipo**: Conteúdo
- **Objetivo**: Explicar a terceira capability canônica
- **Conteúdo**:
  - Prompt = template nomeado com argumentos, servido pelo server
  - Host lista (`prompts/list`) e obtém (`prompts/get`)
  - Retorna mensagens estruturadas (user/assistant) com possível inclusão de resources
  - Casos: "code-review-prompt", "sql-optimizer-prompt", "incident-summary-prompt"
  - Server como guardião de prompts canônicos da organização
- **Diagrama**: Fluxo: host pede prompt → server retorna messages → host injeta no LLM
- **Tempo**: 1.5 min

---

#### Slide 19 — Sampling: Server-Initiated LLM Calls
- **Tipo**: Diagrama
- **Objetivo**: Explicar a capability que inverte a direção
- **Conteúdo**:
  - Server pede ao host para gerar texto via LLM (`sampling/createMessage`)
  - Fluxo: server → client → host → LLM → host → client → server
  - Casos: server precisa de sumarização, classificação, ou raciocínio sobre dados locais
  - Segurança: host deve pedir aprovação humana (HITL) antes de enviar
  - Server nunca tem acesso direto à API key do LLM
- **Diagrama**: Diagrama de sequência (server → host → LLM → host → server)
- **Animação**: Setas aparecem na direção inversa (destacando a inversão)
- **Tempo**: 2 min

---

#### Slide 20 — Roots, Notifications, Subscriptions, Elicitation
- **Tipo**: Conteúdo
- **Objetivo**: Cobrir capabilities complementares
- **Conteúdo**:
  - **Roots**: host indica ao server quais diretórios/URIs são permitidos (filesystem boundary)
  - **Notifications**: mensagens unidirecionais sem resposta (server → client ou client → server)
  - **Subscriptions**: client assina mudanças em resources (`resources/subscribe`)
  - **Elicitation** (spec 2025-11-25): server pede input ao usuário via host (formulário estruturado)
  - Pergunta: *Sampling: quando o server precisa gerar texto?*
- **Diagrama**: 4 ícones com labels e setas de direção
- **Tempo**: 2 min

---

### SEÇÃO D — Construindo Servers (Slides 21-30 · 15 min)

---

#### Slide 21 — [SEÇÃO] Construindo MCP Servers
- **Tipo**: Seção
- **Objetivo**: Transição para o bloco prático de servers
- **Conteúdo**: "3 — Construindo MCP Servers"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 22 — Python SDK: FastMCP
- **Tipo**: Código
- **Objetivo**: Apresentar o SDK Python canônico
- **Conteúdo**:
  - `FastMCP` — API de alto nível, inspirada no FastAPI
  - Instalação: `pip install mcp`
  - Server mínimo em 5 linhas:
    ```python
    from mcp.server.fastmcp import FastMCP
    mcp = FastMCP("meu-server")
    @mcp.tool()
    def hello(name: str) -> str:
        return f"Olá, {name}!"
    mcp.run()
    ```
  - Roda em stdio por padrão; HTTP via `mcp.run(transport="streamable-http")`
- **Diagrama**: Code block com syntax highlighting
- **Tempo**: 2 min

---

#### Slide 23 — Decorators: @tool, @resource, @prompt
- **Tipo**: Código
- **Objetivo**: Mostrar os 3 decorators canônicos
- **Conteúdo**:
  - `@mcp.tool()` — registra função como tool; docstring vira descrição; type hints viram schema
  - `@mcp.resource("uri://{path}")` — registra resource; suporta templates com variáveis
  - `@mcp.prompt()` — registra prompt template; argumentos viram parâmetros
  - Snippet mostrando os 3 decorators em um server
  - Type hints do Python → JSON Schema automaticamente
- **Diagrama**: 3 colunas, uma por decorator, com mini-snippet
- **Tempo**: 2 min

---

#### Slide 24 — Exemplo: Filesystem Server
- **Tipo**: Código
- **Objetivo**: Mostrar um server de referência
- **Conteúdo**:
  - Tools: `read_file`, `write_file`, `list_directory`, `search_files`
  - Resources: `file://{path}` com mimeType dinâmico
  - Roots: host define diretórios permitidos
  - Segurança: validação de path (resolver, não aceitar `..`)
  - Referência: `@modelcontextprotocol/server-filesystem` (TS) ou equivalente Python
- **Diagrama**: Arquitetura do filesystem server
- **Tempo**: 2 min

---

#### Slide 25 — Exemplo: GitHub Server
- **Tipo**: Código
- **Objetivo**: Mostrar um server que integra API externa
- **Conteúdo**:
  - Tools: `create_issue`, `list_prs`, `merge_pr`, `search_code`
  - Resources: `github://repo/{owner}/{repo}/issue/{number}`
  - Prompts: `pr-review-prompt(number)` — template de code review
  - Autenticação: token via env var (`GITHUB_TOKEN`)
  - Paginação e rate limiting do GitHub API
- **Diagrama**: Fluxo: LLM → tool → GitHub API → resultado
- **Tempo**: 1.5 min

---

#### Slide 26 — TypeScript SDK
- **Tipo**: Código
- **Objetivo**: Mostrar a alternativa TS para devs Node.js
- **Conteúdo**:
  - `@modelcontextprotocol/sdk` — SDK oficial TypeScript
  - API: `McpServer` + `server.tool()`, `server.resource()`, `server.prompt()`
  - Vantagem: mesmo runtime de VSCode, Cursor, OpenCode
  - Snippet equivalente ao FastMCP em TS
  - Quando escolher TS: ecossistema Node, deploy em edge (Cloudflare Workers)
- **Tempo**: 1.5 min

---

#### Slide 27 — Testes de Server (MCP Inspector)
- **Tipo**: Demo / Ferramenta
- **Objetivo**: Mostrar como testar servers sem um host completo
- **Conteúdo**:
  - `mcp inspector` — CLI interativo que conecta a qualquer server
  - Lista tools, resources, prompts; executa tool calls manualmente
  - Inspeção de schema, validação de responses
  - Debug de transportes (stdio, HTTP)
  - CI: testes automatizados com cliente MCP de teste
- **Diagrama**: Screenshot do MCP Inspector
- **Tempo**: 1.5 min

---

#### Slide 28 — Empacotamento e Distribuição
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar como distribuir um MCP server
- **Conteúdo**:
  - Python: pacote pip (`pip install meu-mcp-server`), entrypoint `meu-server`
  - TypeScript: pacote npm, binário `npx meu-mcp-server`
  - Docker: container com server HTTP (remote MCP)
  - Remote servers: deploy em Cloudflare Workers, Vercel, fly.io
  - Registro: publicar em catálogos (Awesome MCP, modelcontextprotocol.io)
  - Versionamento semântico (semver) — quebra de schema = major bump
- **Diagrama**: Pipeline: código → pacote → registro → host
- **Tempo**: 1.5 min

---

#### Slide 29 — DEMO: Meu Primeiro MCP Server
- **Tipo**: Código
- **Objetivo**: Demo ao vivo — construir server que expõe tools de consulta a dataset
- **Conteúdo**:
  - Código do `05-Labs/ETHAGT08/Lab1-Primeiro-MCP-Server`
  - Passo 1: criar server com FastMCP + 3 tools (query, stats, search)
  - Passo 2: rodar em stdio
  - Passo 3: configurar no OpenCode (ou Claude Desktop)
  - Passo 4: mostrar LLM chamando tool via host
  - Passo 5: adicionar resource (arquivo de config do dataset)
- **Diagrama**: Code block + terminal side-by-side
- **Animação**: Highlight de linhas chave
- **Tempo**: 5 min

---

#### Slide 30 — Pergunta da DEMO
- **Tipo**: Exercício
- **Objetivo**: Engajar a turma com uma pergunta sobre a demo
- **Conteúdo**:
  - "O que acontece se a tool retornar erro? Como o LLM reage?"
  - "E se o LLM chamar uma tool que não existe?"
  - "Resource vs Tool: quando usar cada para o mesmo dado?"
  - Discussão em duplas (2 min)
- **Diagrama**: Caixa de discussão
- **Tempo**: 2 min

---

### SEÇÃO E — Clients e Hosts (Slides 31-38 · 10 min)

---

#### Slide 31 — [SEÇÃO] Clients e Hosts
- **Tipo**: Seção
- **Objetivo**: Transição para o bloco de integração
- **Conteúdo**: "4 — Clients e Hosts"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 32 — Como um Host Instancia Clients
- **Tipo**: Diagrama
- **Objetivo**: Mostrar o mecanismo interno de um host
- **Conteúdo**:
  - Host lê config de servers (JSON)
  - Para cada server configurado → cria 1 client → 1 conexão
  - Client faz handshake (initialize → initialized)
  - Host agrega capabilities de todos os servers
  - LLM vê tools de todos os servers como um conjunto unificado
  - Host roteia tool_call para o client/server correto
- **Diagrama**: Flowchart: config → N clients → N servers → agregação
- **Animação**: Clients surgem um a um
- **Tempo**: 2 min

---

#### Slide 33 — Claude Desktop: Config JSON
- **Tipo**: Código
- **Objetivo**: Mostrar o formato de config do host de referência
- **Conteúdo**:
  - Arquivo: `claude_desktop_config.json` (macOS/Linux/Windows)
  - Estrutura: `mcpServers` com nome → command + args + env
  - Exemplo:
    ```json
    {
      "mcpServers": {
        "filesystem": {
          "command": "npx",
          "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/me/projects"]
        }
      }
    }
    ```
  - Suporte a stdio (local) e HTTP (remote)
- **Diagrama**: JSON block com syntax highlighting
- **Tempo**: 2 min

---

#### Slide 34 — VSCode MCP
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar integração no editor mais usado
- **Conteúdo**:
  - VSCode (Copilot Chat) suporta MCP servers nativamente
  - Config via `.vscode/mcp.json` ou settings workspace
  - Servers aparecem como tools no Copilot Chat
  - Suporte a stdio e HTTP
  - Debug: output panel mostra logs do server
- **Diagrama**: Screenshot do VSCode com MCP config
- **Tempo**: 1 min

---

#### Slide 35 — OpenCode: Config MCP
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar integração com a ferramenta usada na especialização
- **Conteúdo**:
  - OpenCode: `opencode.json` com seção `mcp`
  - Suporte a múltiplos servers (stdio e HTTP)
  - Servers como tools do agente OpenCode
  - Vantagem: mesmo runtime que os exemplos do curso
  - Exemplo de config com 2 servers
- **Tempo**: 1 min

---

#### Slide 36 — Integrar em Agente Custom (LangGraph, OpenAI Agents SDK)
- **Tipo**: Código
- **Objetivo**: Mostrar que MCP não é só para hosts pronto — pode ser embedding
- **Conteúdo**:
  - LangGraph: `langchain-mcp-adapters` — carrega tools de server MCP como `BaseTool`
  - OpenAI Agents SDK: MCP server como tool source
  - Padrão: agente custom = host leve
  - Snippet: carregar tools de server MCP e injetar em agente LangGraph
  - Vantagem: reusar servers MCP sem acoplar a um host específico
- **Diagrama**: Arquitetura: agente custom → MCP client → server
- **Tempo**: 2 min

---

#### Slide 37 — Multi-Server Composition
- **Tipo**: Diagrama
- **Objetivo**: Mostrar o cenário real de múltiplos servers
- **Conteúdo**:
  - Host com 5 servers: filesystem, github, postgres, slack, brave-search
  - LLM vê todas as tools agregadas (pode haver nome colision → namespacing)
  - Host roteia chamadas; server não sabe dos outros
  - Composição: LLM pode encadear tools de servers diferentes
  - Desafio: contexto explode (muitas tools = tokens)
- **Diagrama**: 1 host → 5 clients → 5 servers, com LLM no topo
- **Tempo**: 1 min

---

#### Slide 38 — Pergunta: Como o LLM Escolhe Entre N Servers?
- **Tipo**: Exercício
- **Objetivo**: Provocar reflexão sobre escalabilidade de tools
- **Conteúdo**:
  - "Com 50 tools de 5 servers, como o LLM escolhe a certa?"
  - "O que acontece quando tools têm nomes/funcionalidades sobrepostas?"
  - Estratégias: descrições ricas, namespacing, tool filtering dinâmico
  - Discussão aberta (2 min)
- **Tempo**: 2 min

---

### SEÇÃO F — Governança de Ecossistema (Slides 39-46 · 10 min)

---

#### Slide 39 — [SEÇÃO] Governança de Ecossistema
- **Tipo**: Seção
- **Objetivo**: Transição para o bloco de governança
- **Conteúdo**: "5 — Governança de Ecossistema"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 40 — Catálogo Interno de Servers
- **Tipo**: Conteúdo
- **Objetivo**: Justificar a necessidade de um registro central
- **Conteúdo**:
  - Problema: times criam servers MCP ad hoc — caos sem catálogo
  - Catálogo interno: registro, descoberta, documentação
  - Metadados: nome, descrição, owner, versão, tools, dependencies
  - Analogia: "catálogo de servers = npm registry interno"
  - Ferramentas: registry custom, Smithery (SaaS), mcp.run
- **Diagrama**: Arquitetura do catálogo (registry → descoberta → hosts)
- **Tempo**: 2 min

---

#### Slide 41 — Versionamento Semântico e Compatibilidade
- **Tipo**: Conteúdo
- **Objetivo**: Estabelecer regras de evolução de servers
- **Conteúdo**:
  - SemVer: MAJOR.MINOR.PATCH
  - Quebra de schema de tool = MAJOR bump (tool removida ou schema incompatível)
  - Nova tool ou novo campo opcional = MINOR
  - Bug fix = PATCH
  - Negociação de versão de protocolo no `initialize`
  - Janela de deprecação: avisar antes de remover
- **Diagrama**: Timeline de versões com flags breaking/non-breaking
- **Tempo**: 1.5 min

---

#### Slide 42 — Permissões por Server/Client
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar o modelo de controle de acesso
- **Conteúdo**:
  - Per-server: quais hosts/clients podem conectar
  - Per-tool: quais tools são expostas para qual client (allowlist)
  - Per-resource: ACL por URI
  - Config declarativa: `allow`, `deny`, `ask` (HITL)
  - Exemplo: server de DB → `read` para todos, `write` só para dev senior
- **Diagrama**: Matriz server × client × tool com checkmarks
- **Tempo**: 1.5 min

---

#### Slide 43 — Supply Chain Security: Provenance, SBOM
- **Tipo**: Conteúdo
- **Objetivo**: Aplicar supply chain security a MCP servers
- **Conteúdo**:
  - Provenance: de onde veio o server? (registry, commit hash, build signature)
  - SBOM (Software Bill of Materials): lista de dependências transitivas
  - Verificação: assinatura do pacote, hash, reproducible build
  - Risco: server malicioso no catálogo = backdoor para todos os hosts
  - Prática: pin de versão, audit de deps, scan de vulnerabilities (Snyk, Dependabot)
- **Diagrama**: Pipeline: source → build → sign → registry → verify → deploy
- **Tempo**: 2 min

---

#### Slide 44 — Auditoria e Logs
- **Tipo**: Diagrama
- **Objetivo**: Mostrar o modelo de observabilidade de chamadas MCP
- **Conteúdo**:
  - Log de cada chamada: timestamp, server, tool, args, result, caller, duração
  - Host-side log: quem chamou, quando, com qual contexto
  - Server-side log: o que executou, com quais permissões
  - Centralização: logs → SIEM (Splunk, ELK, Datadog)
  - Alertas: chamada a tool sensível, erro repetido, volume anômalo
- **Diagrama**: `12-Diagrams/ETHAGT08/governance.mmd`
- **Tempo**: 1.5 min

---

#### Slide 45 — ADR de Governança
- **Tipo**: Conteúdo
- **Objetivo**: Conectar governança a prática de ADRs
- **Conteúdo**:
  - ADR (Architecture Decision Record) para cada server de produção
  - Template: contexto, decisão, consequences, owner, review date
  - Questões: por que este server? quais tools? quem é owner? ciclo de deprecação?
  - Exemplo: ADR-012 — "Adoção do server-postgres com read-only"
- **Diagrama**: Template de ADR
- **Tempo**: 1 min

---

#### Slide 46 — Pergunta: Quem é "Dono" dos Servers?
- **Tipo**: Exercício
- **Objetivo**: Provocar reflexão sobre ownership organizacional
- **Conteúdo**:
  - "Servers de infra (filesystem, DB) — dono: platform team?"
  - "Servers de domínio (Salesforce, SAP) — dono: biz team?"
  - "Quem aprova a criação de um novo server?"
  - Discussão aberta (2 min)
- **Tempo**: 2 min

---

### SEÇÃO G — Segurança e Produção (Slides 47-54 · 10 min)

---

#### Slide 47 — [SEÇÃO] Segurança e Produção
- **Tipo**: Seção
- **Objetivo**: Transição para o bloco de segurança
- **Conteúdo**: "6 — Segurança e Produção"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 48 — Server como Boundary de Confiança
- **Tipo**: Conteúdo
- **Objetivo**: Estabelecer o modelo de ameaça fundamental
- **Conteúdo**:
  - Server executa código arbitrário com acesso a dados/APIs
  - Server é um boundary: o que ele retorna vai para o LLM → vai para o contexto
  - 3 níveis de confiança: trusted (interno), semi-trusted (terceiro), untrusted (comunitário)
  - Pergunta: "Você confiaria neste server com acesso ao seu filesystem?"
  - Princípio: treat server output as untrusted data (não como instrução)
- **Diagrama**: 3 níveis de confiança com cores (verde/amarelo/vermelho)
- **Tempo**: 2 min

---

#### Slide 49 — Sandboxing de Servers
- **Tipo**: Diagrama
- **Objetivo**: Mostrar técnicas de isolamento
- **Conteúdo**:
  - Container Docker: isolamento de processo, filesystem, rede
  - OS-level: seccomp, AppArmor, SELinux
  - Linguagem: sandbox de Python (RestrictedPython), WASM
  - Network egress: bloquear saída não autorizada (server não deve chamar internet)
  - Filesystem: mount read-only, tmpfs para escrita
  - Roots do MCP: host define boundary de URIs
- **Diagrama**: Camadas de sandbox (container → OS → rede → FS)
- **Tempo**: 1.5 min

---

#### Slide 50 — Prompt Injection via Resources
- **Tipo**: Diagrama
- **Objetivo**: Mostrar o vetor de ataque mais comum em MCP
- **Conteúdo**:
  - Cenário: resource contém texto malicioso ("ignore instruções anteriores e...")
  - LLM lê resource como parte do contexto → pode seguir a instrução injetada
  - Server expõe dado não confiável (ex.: issue de GitHub, email, página web)
  - Mitigação: marcar resources como `untrusted`, sanitização, HITL para ações sensíveis
  - Caso real: server de web-search retorna página com prompt injection
- **Diagrama**: Sequência: resource malicioso → LLM lê → ação indesejada
- **Tempo**: 2 min

---

#### Slide 51 — OAuth 2.1 para Streamable HTTP
- **Tipo**: Diagrama
- **Objetivo**: Explicar o modelo de autenticação para remote servers
- **Conteúdo**:
  - Spec 2025-11-25: remote servers (Streamable HTTP) devem usar OAuth 2.1
  - Fluxo: host atua como OAuth client → Authorization Server → Resource Server (MCP server)
  - Token: Bearer token no header `Authorization`
  - PKCE obrigatório (Proof Key for Code Exchange)
  - Server pode exigir scopes específicos por tool
  - Dynamic Client Registration: server pode registrar clientes dinamicamente
- **Diagrama**: Diagrama de sequência OAuth 2.1 (host → auth server → MCP server)
- **Tempo**: 2 min

---

#### Slide 52 — Rate Limiting e Quotas
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar defesas contra abuso
- **Conteúdo**:
  - Rate limiting por client/user (requests/min)
  - Quotas por tool (ex.: `write_file` max 100/dia)
  - Token budget: limitar tokens consumidos por sessão
  - Backpressure: server pode retornar HTTP 429
  - Circuit breaker: se server falhar N vezes, host desabilita temporariamente
- **Diagrama**: Pipeline com rate limiter + quota + circuit breaker
- **Tempo**: 1 min

---

#### Slide 53 — Casos Reais: Exfiltração e Tool Misuse
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar ataques reais documentados
- **Conteúdo**:
  - Caso 1: server malicioso exfiltra dados via sampling (pede ao LLM para sumarizar dados sensíveis e enviar para endpoint externo)
  - Caso 2: prompt injection via resource faz LLM chamar tool de delete
  - Caso 3: tool confusion — nomes similares fazem LLM chamar tool errada
  - Caso 4: token exaustion — server retorna resource gigante para encher contexto
  - Lição: defense in depth (sandbox + permissões + auditoria + HITL)
- **Diagrama**: 4 cards com caso + mititaçãoção
- **Tempo**: 1.5 min

---

#### Slide 54 — Pergunta: Mitigando Path Traversal
- **Tipo**: Exercício
- **Objetivo**: Praticar mitigação de um risco concreto
- **Conteúdo**:
  - "Se um MCP server de arquivos permite ler qualquer path, como mitigar?"
  - Estratégias: roots, path validation (resolve + check prefix), sandbox FS, allowlist de extensões
  - 2 min individual, 1 min compartilhar
- **Diagrama**: Caixa de discussão com dica visual (cadeado + path)
- **Tempo**: 3 min

---

### SEÇÃO H — Fechamento (Slides 55-70 · 15 min)

---

#### Slide 55 — [SEÇÃO] Boas Práticas e Anti-Patterns
- **Tipo**: Seção
- **Objetivo**: Transição para o fechamento
- **Conteúdo**: "7 — Boas Práticas e Anti-Patterns"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 56 — Boas Práticas (DO)
- **Tipo**: Conteúdo
- **Objetivo**: Checklist de boas práticas
- **Conteúdo**:
  - Descreva tools com o cuidado de uma API pública (ACI do ETHAGT02)
  - Use type hints / JSON Schema explícito
  - Sandbox todo server de terceiro
  - Log estruturado de toda chamada MCP
  - Versionamento semver desde o primeiro release
  - HITL para tools destrutivas (delete, write, send)
  - Pin de versão de servers em produção
  - Catálogo + ADR para todo server de produção
- **Diagrama**: Checklist verde (etho-success)
- **Tempo**: 2 min

---

#### Slide 57 — Anti-Patterns (DON'T)
- **Tipo**: Conteúdo
- **Objetivo**: Checklist do que NÃO fazer
- **Conteúdo**:
  - Confiar em server de terceiro sem sandbox
  - Expor tool sem descrição ou schema
  - Não versionar (pin em `latest`)
  - Não logar chamadas MCP
  - Misturar dados não confiáveis (resources) como instruções
  - Permitir path arbitrário sem validação
  - Remote server sem OAuth/TLS
  - Server com access excessivo (princípio do menor privilégio violado)
- **Diagrama**: Checklist vermelho (etho-danger)
- **Tempo**: 2 min

---

#### Slide 58 — Caso de Estudo: MCP em Produção (Anthropic, Block, Replit)
- **Tipo**: Diagrama
- **Objetivo**: Mostrar todos os conceitos em casos reais
- **Conteúdo**:
  - **Anthropic**: Claude Desktop com servers de referência (filesystem, github, etc.)
  - **Block**: arquitetura interna de servers MCP para dev tools
  - **Replit**: agentes com MCP para integração com serviços cloud
  - Padrão comum: catálogo interno + sandbox + auditoria
  - Não há "magia" — é o que ETHAGT08 ensina
- **Diagrama**: 3 colunas (uma por empresa) com arquitetura resumida
- **Tempo**: 2 min

---

#### Slide 59 — Exercício: Config e Segurança
- **Tipo**: Exercício
- **Objetivo**: Praticar config + threat model
- **Conteúdo**:
  - Cenário: adicionar um MCP server de banco de dados a um host
  - Tarefa 1: escrever a config JSON para Claude Desktop
  - Tarefa 2: listar 3 riscos de segurança e propor mitigação
  - 3 min individual, 2 min compartilhar
- **Diagrama**: Template de resposta (config + tabela de riscos)
- **Tempo**: 5 min

---

#### Slide 60 — Resumo da Aula
- **Tipo**: Resumo
- **Objetivo**: Sintetizar os pontos-chave
- **Conteúdo**:
  - MCP = padrão aberto que resolve o problema N×M ("USB-C da IA")
  - Arquitetura: host → client → server; transportes: stdio, Streamable HTTP
  - Capabilities: tools, resources, prompts, sampling (+ roots, notifications, elicitation)
  - Servers: FastMCP (Python) / TS SDK; decorators @tool, @resource, @prompt
  - Hosts: Claude Desktop, VSCode, OpenCode, agente custom
  - Governança: catálogo, semver, permissões, SBOM, auditoria, ADR
  - Segurança: sandbox, prompt injection, OAuth 2.1, rate limiting, defense in depth
- **Diagrama**: 7 ícones com os pontos-chave
- **Tempo**: 2 min

---

#### Slide 61 — Checklist da Aula
- **Tipo**: Resumo
- **Objetivo**: Confirmar que todos os tópicos foram cobertos
- **Conteúdo**:
  - [ ] Explicou arquitetura host-client-server
  - [ ] Diferenciou tools, resources, prompts, sampling
  - [ ] Construiu server com FastMCP (DEMO)
  - [ ] Mostrou config de host (Claude Desktop / OpenCode)
  - [ ] Discutiu governança (catálogo, versionamento, permissões)
  - [ ] Abordou segurança (sandbox, injection, OAuth)
- **Diagrama**: Checklist visual
- **Tempo**: 1 min

---

#### Slide 62 — Quiz: Pergunta 1
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "Qual é o problema que o MCP resolve?"
  - A) Falta de modelos grandes o suficiente
  - B) A explosão N×M de integrações LLM ↔ sistemas
  - C) Ausência de frameworks de agentes
  - D) Custo de tokens
  - Resposta: B
- **Tempo**: 1 min

---

#### Slide 63 — Quiz: Pergunta 2
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "Qual capability permite que um server peça ao LLM do host para gerar texto?"
  - A) Tools
  - B) Resources
  - C) Prompts
  - D) Sampling
  - Resposta: D
- **Tempo**: 1 min

---

#### Slide 64 — Quiz: Pergunta 3
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "Qual transporte é o canônico para remote servers na spec 2025-11-25?"
  - A) stdio
  - B) HTTP+SSE (deprecated)
  - C) Streamable HTTP
  - D) WebSocket
  - Resposta: C
- **Tempo**: 1 min

---

#### Slide 65 — Quiz: Pergunta 4
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "Qual é o maior risco de security ao usar resources de fontes não confiáveis?"
  - A) Rate limiting
  - B) Prompt injection
  - C) Incompatibilidade de schema
  - D) Latência alta
  - Resposta: B
- **Tempo**: 1 min

---

#### Slide 66 — Quiz: Pergunta 5
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "Verdadeiro ou falso: MCP substitui o tool calling nativo do LLM."
  - A) Verdadeiro
  - B) Falso — MCP padroniza o protocolo de comunicação, não substitui o tool calling do modelo
  - Resposta: B
- **Tempo**: 1 min

---

#### Slide 67 — Projeto do Módulo
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar o projeto que os alunos devem entregar
- **Conteúdo**:
  - Projetar e construir um MCP server útil (ex.: Confluence Etho, SAP OData, Salesforce)
  - Com governança: permissões, logs, versionamento
  - Entrega: server open-source-ready + docs + ADR de governança + threat model
  - Critério de sucesso: server funcional com ≥3 tools; threat model documenta riscos e mitigações
- **Tempo**: 1 min

---

#### Slide 68 — Labs do Módulo
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar os laboratórios
- **Conteúdo**:
  - Lab 1 (4 h): "Meu primeiro MCP server" — construir server com tools de consulta a dataset; conectar ao Claude Desktop / OpenCode
  - Lab 2 (5 h): "MCP server para arXiv + GitHub" — composição multi-server em um agente
- **Tempo**: 1 min

---

#### Slide 69 — Conexão com Próximos Módulos / Leitura Recomendada
- **Tipo**: Referências
- **Objetivo**: Conectar com o resto da especialização e indicar leitura
- **Conteúdo**:
  - ETHAGT13 — Segurança & Governança: aprofunda threat modeling e defesa
  - ETHAGT90 — Capstone: projeto integrador com MCP
  - Obrigatório: *Model Context Protocol Specification* (modelcontextprotocol.io)
  - Obrigatório: Anthropic, *Introducing the Model Context Protocol* (nov/2024)
  - Recomendado: Cloudflare *Remote MCP servers*
  - Recomendado: *Awesome MCP Servers* (catálogo comunitário)
- **Diagrama**: Mapa da especialização com ETHAGT08 no centro
- **Tempo**: 1 min

---

#### Slide 70 — Q&A / Encerramento
- **Tipo**: Capa
- **Objetivo**: Abrir para perguntas e encerrar
- **Conteúdo**:
  - "Perguntas?"
  - Contato do professor
  - "Na próxima aula: ETHAGT13 — Segurança & Governança"
- **Diagrama**: Logo Etho + fundo etho-dark
- **Tempo**: 2 min

---

## Resumo do Storyboard

| Seção | Slides | Tempo | Conteúdo |
|---|---|---|---|
| A — Abertura | 1-6 | 8 min | Capa, objetivos, competências, agenda, motivação N×M, contexto histórico |
| B — Arquitetura MCP | 7-13 | 10 min | Host-client-server, transportes, Streamable HTTP, ciclo de vida, ecossistema |
| C — Capabilities | 14-20 | 12 min | Tools, resources, prompts, sampling, roots/notifications/elicitation |
| D — Servers | 21-30 | 15 min | FastMCP, decorators, exemplos (filesystem, GitHub), TS SDK, testes, empacotamento, DEMO |
| E — Clients/Hosts | 31-38 | 10 min | Host instancia clients, Claude Desktop, VSCode, OpenCode, agente custom, multi-server |
| F — Governança | 39-46 | 10 min | Catálogo, versionamento, permissões, SBOM, auditoria, ADR |
| G — Segurança | 47-54 | 10 min | Boundary, sandbox, prompt injection, OAuth 2.1, rate limiting, casos reais |
| H — Fechamento | 55-70 | 15 min | Boas práticas, anti-patterns, caso de estudo, exercício, resumo, quiz, projeto, labs, next, Q&A |
| **Total** | **70** | **90 min** | |

---

## Diagramas Necessários

| # | Slide | Diagrama | Tipo | Fonte |
|---|---|---|---|---|
| D1 | 8 | Host-Client-Server | Flowchart | `12-Diagrams/ETHAGT08/host-client-server.mmd` |
| D2 | 9 | Transportes (stdio, HTTP+SSE, Streamable HTTP) | Comparação | Novo |
| D3 | 10 | Streamable HTTP lifecycle | Sequência | Novo |
| D4 | 11 | Ciclo de vida de conexão MCP | Flowchart | Novo |
| D5 | 12 | Ecossistema MCP atual | Mind map | Novo |
| D6 | 15 | Capabilities overview | Flowchart | `12-Diagrams/ETHAGT08/capabilities.mmd` |
| D7 | 16 | Fluxo de tool calling MCP | Sequência | Novo |
| D8 | 17 | Resource vs Tool (dado vs ação) | Comparação | Novo |
| D9 | 19 | Sampling (server-initiated) | Sequência | Novo |
| D10 | 22 | FastMCP server mínimo | Código | Novo |
| D11 | 24 | Filesystem server architecture | Flowchart | Novo |
| D12 | 25 | GitHub server fluxo | Sequência | Novo |
| D13 | 29 | DEMO server (código + terminal) | Código | Novo |
| D14 | 32 | Host instancia N clients | Flowchart | Novo |
| D15 | 37 | Multi-server composition (1 host → 5 servers) | Flowchart | Novo |
| D16 | 40 | Catálogo interno (registry → descoberta) | Flowchart | Novo |
| D17 | 44 | Governança (auditoria + logs) | Flowchart | `12-Diagrams/ETHAGT08/governance.mmd` |
| D18 | 49 | Camadas de sandbox | Flowchart | Novo |
| D19 | 50 | Prompt injection via resources | Sequência | Novo |
| D20 | 51 | OAuth 2.1 flow (host → auth server → MCP server) | Sequência | Novo |
| D21 | 53 | Casos reais de ataque (4 cards) | Comparação | Novo |
| D22 | 58 | MCP em produção (Anthropic, Block, Replit) | 3 colunas | Novo |
| D23 | 69 | Mapa da especialização | Mind map | Novo |

---

## Pontos de Engajamento

| # | Slide | Tipo | Pergunta / Atividade | Tempo |
|---|---|---|---|---|
| E1 | 5 | Votação | "Quantas integrações diferentes vocês já fizeram para conectar LLMs a sistemas?" | 1 min |
| E2 | 13 | Discussão em duplas | "Qual sistema da sua empresa você transformaria em MCP server primeiro?" | 2 min |
| E3 | 20 | Pergunta retórica | "Sampling: quando o server precisa gerar texto?" | 1 min |
| E4 | 30 | Discussão em duplas | "O que acontece se a tool retornar erro? Como o LLM reage?" | 2 min |
| E5 | 38 | Discussão aberta | "Com 50 tools de 5 servers, como o LLM escolhe a certa?" | 2 min |
| E6 | 46 | Discussão aberta | "Quem é dono dos servers? Platform team ou biz team?" | 2 min |
| E7 | 54 | Exercício individual + share | "Se um MCP server de arquivos permite ler qualquer path, como mitigar?" | 3 min |
| E8 | 59 | Exercício individual + share | "Escrever config JSON + listar 3 riscos de segurança de um server de DB" | 5 min |
| E9 | 62-66 | Quiz (5 perguntas) | Verificação de compreensão (multipla escolha + V/F) | 5 min |

---

## Pendências de Produção

- [ ] Produzir 20 diagramas novos (D2-D5, D7-D16, D18-D23)
- [ ] Screenshot do MCP Inspector (Slide 27)
- [ ] Screenshot do VSCode com MCP config (Slide 34)
- [ ] Screenshot do OpenCode com MCP config (Slide 35)
- [ ] Screenshot do código DEMO com syntax highlighting (Slides 22, 23, 24, 29, 36)
- [ ] Screenshot do trace real de tool call via MCP (Slide 29)
- [ ] Imagem de fundo para capa (Slide 1) — conectores USB-C / rede de nós
- [ ] Badge de competências (Slide 3)
- [ ] Timeline de marcos históricos do MCP (Slide 6)
- [ ] Template de ADR (Slide 45)
- [ ] Verificar 3 diagramas existentes (host-client-server.mmd, capabilities.mmd, governance.mmd) quanto à spec 2025-11-25

---

> **Aguardando aprovação deste storyboard para gerar os slides detalhados com notas do professor.**
