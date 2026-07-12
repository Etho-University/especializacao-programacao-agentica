# ETHAGT08 — Slides Detalhados + Notas do Professor (Parte 1: Slides 1-35)

> Universidade Etho · Especialização em Programação Agêntica
> Cada slide contém: título, objetivo, conteúdo, notas do professor, diagrama, animação, imagem, tempo.

---

## SEÇÃO A — Abertura (Slides 1-6 · 8 min)

---

### Slide 1 — Capa

**Título**: ETHAGT08 — MCP — Model Context Protocol
**Objetivo**: Identificar a aula, o professor e o contexto dentro da especialização.
**Conteúdo**:
- ETHAGT08 — MCP — Model Context Protocol
- Universidade Etho · Especialização em Programação Agêntica
- Fase C — Multi-Agentes, Ferramentas e Orquestração · 25 h
- Professor · Data
- Spec de referência: 2025-11-25

**Diagrama**: Logo Etho (canto sup. esquerdo) + imagem de fundo (conectores USB-C / rede de nós)
**Animação**: Fade in do título (300ms)
**Imagem**: Fundo `etho-dark` (#0F1E2D) com pattern de conectores USB-C e nós interligados
**Tempo**: 1 min

**Rodape**: MCP = Model Context Protocol — Protocolo de Contexto de Modelo

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Bem-vindos. Esta aula é sobre o **Model Context Protocol** — o "USB-C da IA". O MCP é o padrão aberto anunciado pela Anthropic em novembro de 2024 para padronizar a conexão entre LLMs e sistemas. Hoje vamos do porquê até governança e segurança em produção. Se você dominar este módulo, consegue projetar, construir e operar MCP servers em qualquer organização.
💡 ANALOGIA: É como o USB-C. Antes do USB-C, cada celular tinha um carregador diferente. O MCP é o USB-C dos agentes: um conector padrão para qualquer sistema.
❓ PERGUNTA PARA A TURMA: "Quem aqui já ouviu falar do MCP? Quem já usou um server MCP em produção?" (levantar mãos — calibrar nível da turma)
⚠️ ERROS COMUNS: Alunos chegam achando que MCP é "mais um framework de agentes". Não é — é um protocolo, como HTTP. Frameworks implementam; MCP é a camada de padronização.
➡️ TRANSIÇÃO: "Vamos começar definindo o que vocês vão conseguir fazer ao final desta aula."

---

### Slide 2 — Objetivos do Módulo

**Título**: Objetivos do Módulo
**Objetivo**: Deixar claro o que o aluno deve conseguir FAZER ao final da aula.
**Conteúdo**:
- **Objetivo geral**: Dominar o Model Context Protocol — arquitetura, servers, clients, governança e segurança
- **Objetivos específicos**:
  1. Explicar a arquitetura MCP e seu papel como "USB-C da IA"
  2. Construir MCP servers (Python e/ou TS SDK) com tools, resources, prompts
  3. Integrar servers a hosts (Claude Desktop, VSCode, OpenCode, agentes custom)
  4. Aplicar governança: catálogo, permissões, versionamento, supply chain
  5. Avaliar riscos e mitigar (sandboxing, auditoria, OAuth)

**Diagrama**: 5 ícones representando cada objetivo (plug, server, config, shield, lock)
**Animação**: Objetivos aparecem um a um (on click)
**Imagem**: Ícones minimalistas em `etho-accent` (#E85D2F)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Cada objetivo é mensurável. Não é "entender" — é "explicar", "construir", "integrar", "aplicar", "avaliar". Vamos revisar estes objetivos no Slide 60 (resumo) e no Slide 61 (checklist) para confirmar que entregamos tudo.
💡 ANALOGIA: É como um checklist de pré-voo do piloto. Hoje, nosso checklist é estes 5 objetivos. Ao final da aula, vocês devem marcar cada um.
❓ PERGUNTA PARA A TURMA: "Qual desses objetivos vocês acham mais desafiador?" (deixar responder — costuma ser #4 governança ou #5 segurança)
⚠️ ERROS COMUNS: Alunos acham que MCP é só construir servers (objetivo #2). Governança e segurança (#4, #5) são o que distingue "server de brincadeira" de "server de produção".
➡️ TRANSIÇÃO: "Antes de saber o que vamos fazer, vamos saber onde estamos no mapa de competências."

---

### Slide 3 — Competências Desenvolvidas

**Título**: Competências Desenvolvidas
**Objetivo**: Conectar a aula ao Framework Etho de competências.
**Conteúdo**:

| Competência | Nível ao final | Próximo nível em |
|---|---|---|
| C1 Programação Agêntica | **A** (Avançado) | ETHAGT90 Capstone |
| C2 Multi-Agent Systems | **B** (Básico) | ETHAGT09-10 |
| C3 MCP & Tool Use | **A** (Avançado) | — |
| C5 AgentOps & Avaliação | **B** (Básico) | ETHAGT12 |
| C6 Agent Security | **I** (Intermediário) | ETHAGT13 |

**Diagrama**: Radar chart com 5 eixos mostrando nível B/I/A
**Animação**: Radar aparece com wipe (left-to-right, 500ms)
**Imagem**: Badge visual por competência (círculos coloridos)
**Tempo**: 1 min

**Rodape**: AgentOps = Agent Operations — operacao e monitoramento de agentes em producao

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Este módulo atinge nível **Avançado** em duas competências: C1 (Programação Agêntica) e C3 (MCP & Tool Use). C1-A significa que você constrói agentes em produção com justificativa arquitetural completa. C3-A significa que você projeta, construiu e governa servers MCP. C6 (Agent Security) sobe para Intermediário — você consegue ameaçar e mitigar servers; o aprofundamento vem em ETHAGT13.
💡 ANALOGIA: É como tirar carteira de motorista. C1-B era "carteira provisória". C1-A é "carteira definitiva". Vocês saem prontos para "dirigir sozinhos".
⚠️ ERROS COMUNS: Alunos acham que "Avançado" significa "especialista mundial". Não — significa que você opera com autonomia em produção. Especialista mundial é papel de PhD em pesquisa.
➡️ TRANSIÇÃO: "Vamos ver como esta aula está estruturada para entregar essas competências."

---

### Slide 4 — Agenda

**Título**: Agenda da Aula
**Objetivo**: Mostrar o roteiro da aula com tempos estimados.
**Conteúdo**:
- **Bloco 1 (45 min)**:
  - Abertura (8 min) — objetivos, motivação, contexto histórico
  - Arquitetura MCP (10 min) — host-client-server, transportes, ciclo de vida
  - Modelo de Capabilities (12 min) — tools, resources, prompts, sampling
  - Construindo Servers (15 min) — FastMCP, decorators, DEMO
  - Intervalo (5 min)
- **Bloco 2 (45 min)**:
  - Clients e Hosts (10 min) — Claude Desktop, VSCode, OpenCode, multi-server
  - Governança (10 min) — catálogo, versionamento, permissões, SBOM
  - Segurança (10 min) — sandbox, prompt injection, OAuth 2.1
  - Fechamento (15 min) — boas práticas, casos reais, quiz, projeto, Q&A

**Diagrama**: Timeline horizontal com 8 seções coloridas
**Animação**: Timeline cresce da esquerda para direita (500ms)
**Imagem**: Ícones de relógio por seção + 2 marcadores DEMO
**Tempo**: 1 min

**Rodape**: SBOM = Software Bill of Materials — lista de componentes de software

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A aula tem dois blocos. O primeiro é a base teórica + a primeira DEMO (construir um server ao vivo). O segundo é o "como operar em produção": clients, governança, segurança. Há um intervalo de 5 min. O quiz final tem 5 perguntas — individual e serve para auto-avaliação.
💡 ANALOGIA: Bloco 1 = "como funciona o motor". Bloco 2 = "como dirigir com segurança". Os dois juntos = piloto completo.
⚠️ ERROS COMUNS: Alunos querem pular para o código (Seção D) sem entender a arquitetura (Seção B). Reforçar: sem arquitetura, código vira cópia sem entendimento.
➡️ TRANSIÇÃO: "Vamos começar pelo porquê. Por que precisamos de um protocolo novo?"

---

### Slide 5 — Motivação: O Problema N×M

**Título**: O Problema N×M
**Objetivo**: Criar tensão cognitiva — cada LLM precisa de adapter custom para cada sistema.
**Conteúdo**:
- **Cenário**: 5 LLMs (Claude, GPT, Gemini, Llama, Mistral) × 10 sistemas = **50 integrações customizadas**
- Mesmo filesystem precisa de adapter diferente para cada LLM
- Custo de manutenção explode; fragmentação de ecossistema
- Cada provedor reinventa a roda; nenhum interoperável
- **Pergunta**: *Quantas integrações diferentes vocês já fizeram para conectar LLMs a sistemas?*

**Diagrama**: Grid N×M (LLMs à esquerda, sistemas à direita, linhas cruzando em "cabelo de sogra")
**Animação**: Linhas aparecem uma a uma até virar caos visual
**Imagem**: Grid N×M com 5×10 = 50 linhas
**Tempo**: 2 min

**Rodape**: LLM = Large Language Model — Modelo de Linguagem de Grande Escala

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Antes do MCP, integrar N LLMs a M sistemas exigia N×M integrações custom. Se você tem 5 LLMs e 10 sistemas, são 50 conectores para escrever e manter. Cada provedor (OpenAI, Anthropic, Google) tinha seu formato. Cada sistema precisava de conector por provedor. É insustentável. O MCP propõe N+M: cada LLM implementa 1 client; cada sistema implementa 1 server. Total = N+M, não N×M.
💡 ANALOGIA: É como antes do USB. Cada celular tinha um carregador único. Quando você viajava, levava uma sacola de cabos. O USB-C resolveu isso: um cabo para tudo. O MCP é o USB-C da IA.
❓ PERGUNTA PARA A TURMA: "Quantas integrações diferentes vocês já fizeram para conectar LLMs a sistemas?" (levantar mãos — geralmente 3-5 por pessoa)
⚠️ ERROS COMUNS: Alunos acham que "só usamos um LLM, então N×M não é problema". Mas mesmo com 1 LLM, você reescreve para cada sistema. E quando troca de LLM, refaz tudo.
➡️ TRANSIÇÃO: "Essa fragmentação não é eterna. Vamos ver quando e por que isso mudou."

---

### Slide 6 — Contexto: O Nascimento do MCP

**Título**: O Nascimento do MCP
**Objetivo**: Explicar a confluência histórica que motivou o MCP.
**Conteúdo**:
- **Linha do tempo**:
  - 2023: tool calling nativo (OpenAI, Anthropic)
  - Nov/2024: Anthropic anuncia MCP — padrão aberto
  - Mar/2025: Streamable HTTP substitui HTTP+SSE
  - Nov/2025: spec 2025-11-25 (atual)
  - 2026: adoção massiva por OpenAI, Google, Block, Replit, Cloudflare
- **Confluência**: tool calling maduro + necessidade de padrão + ecossistema fragmentado
- **Analogia**: "USB-C da IA" — um conector para tudo
- **Adotantes**: Anthropic, Block, Replit, Cloudflare, Zed, Microsoft (VSCode)

**Diagrama**: Timeline horizontal com marcos + logo dos adotantes
**Animação**: Marcos aparecem sequencialmente (on click)
**Imagem**: Convergência de rios em um lago
**Tempo**: 1 min

**Rodape**: SSE = Server-Sent Events — eventos enviados pelo servidor

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O MCP não surgiu do nada. Ele é a confluência de três coisas: (1) tool calling amadureceu (function calling nativo em 2023); (2) cada provedor inventava seu formato de tools (fragmentação); (3) a Anthropic decidiu abrir o padrão em vez de fechar. O resultado é um protocolo aberto que OpenAI, Google, Block e Replit adotaram. Hoje (2026), é o padrão de facto para integração de LLMs.
💡 ANALOGIA: É como a invenção do container de carga. Antes, cada navio carregava de jeito diferente. O container padrão mudou o comércio mundial. O MCP é o container padrão da IA.
❓ PERGUNTA PARA A TURMA: "Qual desses marcos vocês acham que foi mais decisivo?" (Resposta costuma ser nov/2024 — anúncio da Anthropic abriu o protocolo)
⚠️ ERROS COMUNS: Alunos acham que MCP é proprietário da Anthropic. É aberto (spec pública, SDKs open source, governance multiempresa).
➡️ TRANSIÇÃO: "Agora que sabemos por que estamos aqui, vamos à arquitetura."

---

## SEÇÃO B — Arquitetura MCP (Slides 7-13 · 10 min)

---

### Slide 7 — [SEÇÃO] Por que MCP — O USB-C da IA

**Título**: 1 — Arquitetura MCP
**Objetivo**: Transição visual para o bloco de arquitetura.
**Conteúdo**: Número "1" grande + "Arquitetura MCP"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "1" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Início do bloco de arquitetura. Vamos responder: como o MCP é decomposto? Quem são os papéis? Como eles se comunicam? E qual é o ciclo de vida de uma conexão?
➡️ TRANSIÇÃO: "Primeiro: a decomposição canônica do MCP."

---

### Slide 8 — A Arquitetura Host-Client-Server

**Título**: A Arquitetura Host-Client-Server
**Objetivo**: Apresentar a decomposição canônica do MCP.
**Conteúdo**:
- **Host**: aplicação que abriga o LLM e inicia a conexão (Claude Desktop, VSCode, OpenCode)
- **Client**: instância por server, mantida pelo host (1:1 com server)
- **Server**: processo independente que expõe capabilities (Filesystem, GitHub, Postgres)
- Host pode instanciar múltiplos clients → múltiplos servers
- **LLM vive no host**; server não tem acesso direto ao LLM (exceto via sampling)

**Diagrama**: `12-Diagrams/ETHAGT08/host-client-server.mmd` (Host com LLM + 2 clients → 2 servers → APIs externas)
**Animação**: Componentes surgem do centro (Host) para fora
**Imagem**: Diagrama mermaid renderizado
**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A decomposição canônica do MCP tem três papéis. O **host** é a aplicação que abriga o LLM e inicia tudo — Claude Desktop, VSCode, OpenCode. O **client** é uma instância interna do host, uma por server. O **server** é o processo independente que expõe capabilities — filesystem, github, postgres. Importante: o LLM vive no host. O server não tem acesso direto ao LLM. Isso é proposital — isola responsabilidades e segurança.
💡 ANALOGIA: Host é o gerente de um escritório. Client é o assistente que faz a ligação. Server é o departamento externo (RH, financeiro) que responde. O gerente (LLM) nunca liga direto para o departamento — sempre via assistente (client).
❓ PERGUNTA PARA A TURMA: "Por que o server não tem acesso direto ao LLM?" (Resposta: segurança e isolamento. Se o server pudesse chamar o LLM direto, qualquer server malicioso poderia gastar tokens.)
⚠️ ERROS COMUNS: Alunos confundem client com host. Client NÃO é uma aplicação separada — é uma instância interna do host. Não existe "baixar um MCP client". Você usa o client embutido no Claude Desktop, VSCode, etc.
➡️ TRANSIÇÃO: "Como essas 3 peças se comunicam? Via transportes."

---

### Slide 9 — Transportes: stdio, HTTP+SSE, Streamable HTTP

**Título**: Transportes MCP
**Objetivo**: Mostrar os 3 transportes e quando usar cada.
**Conteúdo**:

| Transporte | Uso | Latência | Segurança | Deploy |
|---|---|---|---|---|
| **stdio** | Local (subprocesso) | Baixa | Processo isolado | Mesma máquina |
| **HTTP+SSE** *(deprecated)* | Remoto (até mar/2025) | Média | TLS obrigatório | Servidor HTTP |
| **Streamable HTTP** *(atual)* | Remoto (canônico) | Média-baixa | TLS + OAuth 2.1 | Cloud / edge |

- **stdio**: stdin/stdout do processo — simples, sem rede
- **HTTP+SSE**: HTTP POST + Server-Sent Events (deprecated na spec 2025-11-25)
- **Streamable HTTP**: single endpoint, POST para requests, SSE opcional para streaming

**Diagrama**: 3 colunas comparativas com ícones de transporte (terminal, HTTP, nuvem)
**Animação**: Colunas aparecem uma a uma
**Imagem**: Ícones de terminal, HTTP, nuvem com setas
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: MCP tem três transportes. **stdio** é o mais simples — o host lança o server como subprocesso e troca mensagens via stdin/stdout. É local, rápido, sem rede. **HTTP+SSE** era o transporte remoto até março/2025, mas foi deprecated porque tinha dois endpoints. **Streamable HTTP** é o atual — single endpoint `POST /mcp`, com SSE opcional para streaming. A spec 2025-11-25 mantém Streamable HTTP como o canônico para remote.
💡 ANALOGIA: stdio é como conversar cara a cara. HTTP+SSE era como telefonar com duas linhas. Streamable HTTP é como WhatsApp — uma conversa, mensagens e áudio no mesmo canal.
❓ PERGUNTA PARA A TURMA: "Qual transporte vocês usariam para um server interno de DB?" (Resposta: stdio, se o host está na mesma máquina do DB; Streamable HTTP se o host é remoto)
⚠️ ERROS COMUNS: Alunos ainda veem tutoriais antigos usando HTTP+SSE. Reforçar: está deprecated desde mar/2025. Usem Streamable HTTP para remote.
➡️ TRANSIÇÃO: "Vamos aprofundar no Streamable HTTP, que é o canônico atual."

---

### Slide 10 — Streamable HTTP em Detalhe (spec 2025-11-25)

**Título**: Streamable HTTP em Detalhe
**Objetivo**: Aprofundar o transporte canônico atual.
**Conteúdo**:
- **Single endpoint**: `POST /mcp`
- Cliente envia **JSON-RPC 2.0** sobre HTTP
- Resposta pode ser:
  - JSON direto (síncrono) — para requests rápidas
  - **SSE stream** — para notificações / long-running
- **Session management**: header `Mcp-Session-Id`
- **Resumabilidade**: stream replay via `Last-Event-ID`
- Vantagem sobre HTTP+SSE: um endpoint, não dois

**Diagrama**: Diagrama de sequência cliente ↔ server (POST inicial → resposta JSON ou SSE)
**Animação**: Mensagens aparecem sequencialmente
**Imagem**: Diagrama de sequência UML estilizado
**Tempo**: 2 min

**Rodape**: JSON-RPC = JSON Remote Procedure Call — protocolo de RPC sobre JSON

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Streamable HTTP é elegante. Um endpoint só: `POST /mcp`. Você envia JSON-RPC 2.0 sobre HTTP. A resposta pode vir de duas formas: JSON direto (síncrono, para requests rápidas) ou SSE stream (para notificações e operações longas). O session management usa o header `Mcp-Session-Id`. Suporta resumabilidade — se a conexão cair, você pode retomar o stream via `Last-Event-ID`. A vantagem sobre HTTP+SSE é estrutural: um endpoint, não dois.
💡 ANALOGIA: HTTP+SSE era como pedir pizza por telefone e receber por delivery separado. Streamable HTTP é como pedir no app — você pede e acompanha no mesmo lugar.
⚠️ ERROS COMUNS: Alunos acham que Streamable HTTP é "só HTTP". Não — pode ter SSE embutido para streaming. É um híbrido inteligente.
➡️ TRANSIÇÃO: "Agora que vimos os transportes, vejamos o ciclo de vida de uma conexão."

---

### Slide 11 — O Ciclo de Vida de uma Conexão MCP

**Título**: Ciclo de Vida de uma Conexão MCP
**Objetivo**: Mostrar as fases de uma conexão MCP.
**Conteúdo**:
- 1. **Initialize**: cliente envia `initialize` com `protocolVersion` + `capabilities`
- 2. **Initialized**: cliente confirma com `notifications/initialized`
- 3. **Operation**: `tools/list`, `resources/list`, `prompts/list`, `tool calls`, etc.
- 4. **Shutdown**: cliente fecha conexão (stdio: mata processo; HTTP: DELETE session)
- **Negociação de versão**: cliente pede uma versão; server responde com a suportada

**Diagrama**: Fluxograma de ciclo de vida (Initialize → Initialized → Operation → Shutdown)
**Animação**: Fases aparecem sequencialmente
**Imagem**: Diagrama de estados com 4 fases
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Toda conexão MCP tem 4 fases. **Initialize**: o cliente envia `initialize` dizendo qual versão de protocolo quer e quais capabilities suporta. O server responde com a versão suportada e suas capabilities. **Initialized**: o cliente confirma com `notifications/initialized` — a conexão está pronta. **Operation**: troca de mensagens — listar tools, chamar tools, ler resources, etc. **Shutdown**: o cliente fecha. Em stdio, mata o processo. Em HTTP, faz DELETE da sessão. Importante: há negociação de versão. Se o cliente pede 2025-11-25 mas o server só suporta 2025-06-18, o server responde com a versão suportada.
💡 ANALOGIA: É como um aperto de mão formal. "Olá, sou a versão X, suporto Y." "Prazer, sou versão Z, suporto W." "Confirmado, vamos conversar."
⚠️ ERROS COMUNS: Alunos acham que podem chamar `tools/call` direto. Não — precisa fazer o handshake `initialize` → `initialized` primeiro.
➡️ TRANSIÇÃO: "Quem já implementa esse protocolo? O ecossistema."

---

### Slide 12 — Ecossistema MCP Atual

**Título**: Ecossistema MCP Atual
**Objetivo**: Mostrar a maturidade do ecossistema.
**Conteúdo**:
- **Servers de referência**: filesystem, git, github, postgres, google-drive, slack, brave-search
- **Hosts**: Claude Desktop, VSCode (Copilot), OpenCode, Zed, Cursor, Windsurf
- **SDKs**: Python (FastMCP), TypeScript, Go (comunitário), Rust (comunitário)
- **Remote servers**: Cloudflare Workers MCP, Smithery, mcp.run
- **Catálogos**: Awesome MCP Servers, modelcontextprotocol.io/servers
- **Adoção enterprise**: Block, Replit, Anthropic, Microsoft, Google, OpenAI (2025+)

**Diagrama**: Mind map com 4 hubs (Hosts, Servers, SDKs, Infra)
**Animação**: Ramos aparecem um a um
**Imagem**: Mind map radial com logos
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O ecossistema MCP é maduro. Há servers de referência da própria Anthropic (filesystem, github, postgres). Há hosts que suportam nativamente: Claude Desktop, VSCode, Cursor, OpenCode, Zed, Windsurf. Há SDKs oficiais em Python (FastMCP) e TypeScript, mais comunitários em Go e Rust. Há plataformas de remote MCP: Cloudflare Workers, Smithery, mcp.run. E adoção enterprise: Block, Replit, Microsoft, Google, OpenAI adicionaram suporte em 2025. Não é mais "tech nova" — é padrão de facto.
💡 ANALOGIA: É como o ecossistema npm em 2015. Já tem volume, mas ainda maturando governança. Onde estamos com MCP hoje.
⚠️ ERROS COMUNS: Alunos acham que só Claude usa MCP. Reforçar: OpenAI, Google, Block, Replit, Microsoft todos adotaram em 2025.
➡️ TRANSIÇÃO: "Vamos estressar isso com uma pergunta prática."

---

### Slide 13 — Pergunta: Onde o MCP se Encaixa na Sua Stack?

**Título**: Onde o MCP se Encaixa na Sua Stack?
**Objetivo**: Engajar a turma a pensar na aplicabilidade.
**Conteúdo**:
- "Qual sistema da sua empresa você transformaria em MCP server primeiro?"
- "Quais dados você NÃO exporia via MCP server?"
- Discussão em duplas (2 min)

**Diagrama**: Caixa de discussão com ícone de chat
**Animação**: Perguntas aparecem uma a uma
**Imagem**: Ícone de balão de conversa em `etho-accent`
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Pausa para reflexão. Cada dupla discute 2 min: qual sistema viraria server primeiro, e quais dados jamais exporiam. A ideia é trazer o MCP para a realidade deles. Costumam sugerir: Salesforce, SAP, Confluence, Jira. E para "não expor": dados de RH sensíveis, dados de saúde (LGPD), chaves de API.
❓ PERGUNTA PARA A TURMA: "Qual sistema da sua empresa você transformaria em MCP server primeiro?" (deixar 2-3 duplas compartilharem)
💡 ANALOGIA: É como escolher o primeiro microsserviço para extrair de um monolito. Comece pelo de maior valor e menor risco.
⚠️ ERROS COMUNS: Alunos querem expor TUDO via MCP. Reforçar: comece pequeno, com dados read-only, e expanda com governança.
➡️ TRANSIÇÃO: "Agora que sabemos onde aplicar, vamos ao modelo de capabilities."

---

## SEÇÃO C — Modelo de Capabilities (Slides 14-20 · 12 min)

---

### Slide 14 — [SEÇÃO] O Modelo de Capabilities

**Título**: 2 — O Modelo de Capabilities
**Objetivo**: Transição visual para o bloco de capabilities.
**Conteúdo**: "2 — O Modelo de Capabilities"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "2" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Início do bloco de capabilities. O MCP não é só "chamar funções". É um modelo rico com 4 capabilities canônicas + complementares. Vamos ver cada uma.
➡️ TRANSIÇÃO: "Visão geral primeiro."

---

### Slide 15 — Visão Geral das Capabilities

**Título**: Visão Geral das Capabilities
**Objetivo**: Apresentar as 4+ capabilities canônicas do MCP.
**Conteúdo**:
- **Tools**: funções com JSON schema (host → server) — alinhado ao ETHAGT02
- **Resources**: dados estruturados identificados por URI (host → server)
- **Prompts**: templates reutilizáveis para o LLM (host → server)
- **Sampling**: server pede ao LLM do host (server → host, **server-initiated**)
- **Extras**: Roots, Notifications, Subscriptions, Elicitation

**Diagrama**: `12-Diagrams/ETHAGT08/capabilities.mmd` (Server com Tools/Resources/Prompts/Sampling; Client; LLM)
**Animação**: Cada capability surge do centro
**Imagem**: Diagrama mermaid renderizado
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O MCP tem 4 capabilities canônicas. **Tools** são funções com JSON schema — o tipo mais usado, alinhado ao tool calling do ETHAGT02. **Resources** são dados estruturados identificados por URI — leitura passiva. **Prompts** são templates reutilizáveis que o server serve. **Sampling** é especial — inverte a direção: o server pede ao LLM do host para gerar texto. Há também capabilities extras: Roots (sandboxing de paths), Notifications, Subscriptions, Elicitation (server pede input ao usuário).
💡 ANALOGIA: Tools = mãos (ação). Resources = olhos (leitura). Prompts = voz (template pronto). Sampling = pedir para o cérebro (host LLM) pensar. Cada capability tem um papel.
❓ PERGUNTA PARA A TURMA: "Qual capability vocês acham que é mais usada em produção?" (Resposta: Tools, disparado. É o 80%.)
⚠️ ERROS COMUNS: Alunos confundem Resources com Tools. Resources = dado (passivo). Tools = ação (ativa). Vamos aprofundar isso no Slide 17.
➡️ TRANSIÇÃO: "Vamos detalhar cada uma, começando pela mais usada: Tools."

---

### Slide 16 — Tools: Funções com JSON Schema

**Título**: Tools — Funções com JSON Schema
**Objetivo**: Detalhar a capability mais usada.
**Conteúdo**:
- **Tool** = nome + descrição + `inputSchema` (JSON Schema) + callback
- **Fluxo**: LLM decide chamar → host executa via client → server processa → resultado volta ao LLM
- Alinhado ao tool calling do ETHAGT02, mas **padronizado** pelo MCP
- Exemplo de schema: `read_file(path: string)` com descrição rica
- **Diferença vs tool calling nativo**: MCP padroniza o **protocolo**, não o modelo

**Diagrama**: Fluxo: LLM → tool_call → client → server → result → LLM (sequência)
**Animação**: Fluxo step-by-step
**Imagem**: Diagrama de sequência
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Tools é a capability mais usada. Uma tool MCP tem: nome, descrição, `inputSchema` (JSON Schema), e um callback. O fluxo é: o LLM no host decide chamar → o host executa via client → o server processa → o resultado volta ao LLM. Isso é idêntico ao tool calling do ETHAGT02, mas padronizado pelo MCP. A diferença é sutil: MCP não substitui o tool calling nativo — padroniza o **protocolo** de comunicação host↔server. O modelo continua usando tool calling; MCP só padroniza como o host descobre e chama as tools.
💡 ANALOGIA: É como REST vs gRPC. Ambos chamam funções remotas. MCP é o "REST padronizado" para tools de LLM.
⚠️ ERROS COMUNS: Alunos acham que MCP "substitui" o tool calling. Falso. MCP padroniza a comunicação; o modelo ainda faz tool calling nativo. (Isso cai no quiz!)
➡️ TRANSIÇÃO: "Agora a capability que mais confunde: Resources."

---

### Slide 17 — Resources: Dados Estruturados

**Título**: Resources — Dados Estruturados
**Objetivo**: Diferenciar resources de tools.
**Conteúdo**:
- **Resource** = URI + nome + descrição + `mimeType` + conteúdo (text ou blob)
- Identificados por URI: `file:///path`, `postgres://table/row`, `github://issue/42`
- Host pode listar (`resources/list`) e ler (`resources/read`)
- **Templates**: `resource://users/{id}` — URI com variáveis
- Casos: arquivos, linhas de DB, issues, imagens, configurações
- **Resource ≠ Tool**: resource é **dado** (passivo), tool é **ação** (ativa)

**Diagrama**: Comparação Resource (dado, ícone olho) vs Tool (ação, ícone mão)
**Animação**: Lado a lado aparece
**Imagem**: Dois ícones: olho (ler) vs mão (fazer)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Resources é a capability que mais confunde. Um resource é um **dado** identificado por URI — como um arquivo, uma linha de DB, uma issue do GitHub. Tem nome, descrição, mimeType e conteúdo. O host pode listar (`resources/list`) e ler (`resources/read`). Suporta templates: `resource://users/{id}` permite instanciar com variáveis. A distinção crítica: **Resource é dado passivo; Tool é ação ativa**. Um resource `github://issue/42` te dá o conteúdo da issue. Uma tool `create_issue()` cria uma nova. Não confunda.
💡 ANALOGIA: Resource é como um arquivo no disco — você lê, mas não altera (só leitura via MCP). Tool é como um botão — você aperta e algo acontece.
❓ PERGUNTA PARA A TURMA: "Para ler um arquivo de config, você usa tool ou resource?" (Resposta: resource — é leitura passiva de dado)
⚠️ ERROS COMUNS: Alunos expõem tudo como tool. Antipattern: `read_file()` como tool. Use resource para leitura, tool para ação.
➡️ TRANSIÇÃO: "A terceira capability: Prompts."

---

### Slide 18 — Prompts: Templates Reutilizáveis

**Título**: Prompts — Templates Reutilizáveis
**Objetivo**: Explicar a terceira capability canônica.
**Conteúdo**:
- **Prompt** = template nomeado com argumentos, servido pelo server
- Host lista (`prompts/list`) e obtém (`prompts/get`)
- Retorna mensagens estruturadas (user/assistant) com possível embedding de resources
- Casos: `code-review-prompt`, `sql-optimizer-prompt`, `incident-summary-prompt`
- **Server como guardião de prompts canônicos** da organização

**Diagrama**: Fluxo: host pede prompt → server retorna messages → host injeta no LLM
**Animação**: Fluxo step-by-step
**Imagem**: Ícone de template / formulário
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Prompts é a terceira capability. Um prompt MCP é um template nomeado com argumentos, servido pelo server. O host lista (`prompts/list`) e obtém (`prompts/get`). Retorna mensagens estruturadas — user/assistant — com possível embedding de resources. Casos: `code-review-prompt(number)`, `sql-optimizer-prompt(query)`, `incident-summary-prompt(id)`. O valor organizacional: o server vira **guardião de prompts canônicos**. Em vez de cada dev inventar seu prompt de code review, o server serve o oficial.
💡 ANALOGIA: É como ter um template de email corporativo. Em vez de cada um escrever do zero, você puxa o template oficial. O server MCP é a "biblioteca de templates" da IA.
⚠️ ERROS COMUNS: Alunos acham que prompts MCP são "prompts do usuário". Não — são templates servidos pelo server, com versionamento e governança.
➡️ TRANSIÇÃO: "Agora a capability especial: Sampling."

---

### Slide 19 — Sampling: Server-Initiated LLM Calls

**Título**: Sampling — Server-Initiated LLM Calls
**Objetivo**: Explicar a capability que inverte a direção.
**Conteúdo**:
- Server pede ao host para gerar texto via LLM (`sampling/createMessage`)
- **Fluxo**: server → client → host → LLM → host → client → server
- Casos: server precisa de sumarização, classificação, ou raciocínio sobre dados locais
- **Segurança**: host deve pedir aprovação humana (HITL) antes de enviar
- Server **nunca** tem acesso direto à API key do LLM

**Diagrama**: Diagrama de sequência (server → host → LLM → host → server)
**Animação**: Setas aparecem na direção inversa (destacando a inversão)
**Imagem**: Diagrama de sequência com setas invertidas
**Tempo**: 2 min

**Rodape**: HITL = Human-in-the-Loop — Humano no Ciclo

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Sampling é especial — inverte a direção. Em tools, o host chama o server. Em sampling, o **server** pede ao **host** para gerar texto via LLM. O fluxo: server → client → host → LLM → host → client → server. Por que isso? Pense num server que processa muitos dados locais e precisa sumarizar. Em vez de enviar todos os dados para o LLM (caro, inseguro), o server pede ao host: "gere um resumo deste texto". O host decide se aprova (HITL), chama o LLM, devolve o resultado. **Crítico**: o server nunca tem acesso direto à API key do LLM. Tudo passa pelo host, que controla.
💡 ANALOGIA: É como um estagiário (server) que precisa de um parecer do diretor (LLM). O estagiário não vai direto ao diretor — pede ao gerente (host), que aprova e repassa. O estagiário nunca tem o telefone do diretor.
⚠️ ERROS COMUNS: Alunos acham que sampling é "o server chamar o LLM direto". NÃO. O server pede ao host, que decide. Sempre HITL para sampling em produção.
➡️ TRANSIÇÃO: "E as capabilities complementares? Vamos rápido."

---

### Slide 20 — Roots, Notifications, Subscriptions, Elicitation

**Título**: Roots, Notifications, Subscriptions, Elicitation
**Objetivo**: Cobrir capabilities complementares.
**Conteúdo**:
- **Roots**: host indica ao server quais diretórios/URIs são permitidos (filesystem boundary)
- **Notifications**: mensagens unidirecionais sem resposta (server → client ou client → server)
- **Subscriptions**: client assina mudanças em resources (`resources/subscribe`)
- **Elicitation** (spec 2025-11-25): server pede input ao usuário via host (formulário estruturado)
- **Pergunta**: *Sampling: quando o server precisa gerar texto?*

**Diagrama**: 4 ícones com labels e setas de direção
**Animação**: Ícones aparecem um a um
**Imagem**: 4 ícones: pasta (roots), sino (notifications), olho (subscriptions), formulário (elicitation)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Quatro capabilities complementares. **Roots**: o host diz ao server quais diretórios ou URIs ele pode acessar — boundary de segurança. **Notifications**: mensagens unidirecionais sem resposta esperada — server avisa "terminei", client avisa "mudei config". **Subscriptions**: o client assina mudanças em resources — quando um arquivo muda, o server notifica. **Elicitation** (nova na spec 2025-11-25): o server pede input estruturado ao usuário via host — tipo um formulário. Útil para confirmation de ações sensíveis.
💡 ANALOGIA: Roots = "você só pode mexer nesta gaveta". Notifications = "avisa quando terminar". Subscriptions = "avisem quando o arquivo mudar". Elicitation = "pergunta ao usuário antes de fazer".
❓ PERGUNTA PARA A TURMA: "Sampling: quando o server precisa gerar texto?" (Resposta: quando processa dados locais e precisa de raciocínio LLM sem expor tudo — sumarização, classificação)
⚠️ ERROS COMUNS: Alunos acham que Roots é "permissão de tool". Não — é boundary de filesystem/URI, aplicado a resources.
➡️ TRANSIÇÃO: "Agora a parte que vocês mais querem: construir servers."

---

## SEÇÃO D — Construindo Servers (Slides 21-30 · 15 min)

---

### Slide 21 — [SEÇÃO] Construindo MCP Servers

**Título**: 3 — Construindo MCP Servers
**Objetivo**: Transição visual para o bloco prático de servers.
**Conteúdo**: "3 — Construindo MCP Servers"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "3" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Início do bloco prático. Vamos do código ao deploy. Python primeiro (FastMCP), depois TypeScript. Exemplos reais (filesystem, github). Testes, empacotamento. E a DEMO ao vivo.
➡️ TRANSIÇÃO: "Começando pelo Python: FastMCP."

---

### Slide 22 — Python SDK: FastMCP

**Título**: Python SDK — FastMCP
**Objetivo**: Apresentar o SDK Python canônico.
**Conteúdo**:
- `FastMCP` — API de alto nível, inspirada no FastAPI
- **Instalação**: `pip install mcp`
- Server mínimo em 5 linhas:

```python
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("meu-server")

@mcp.tool()
def hello(name: str) -> str:
    return f"Olá, {name}!"

mcp.run()
```

- Roda em **stdio** por padrão; HTTP via `mcp.run(transport="streamable-http")`

**Diagrama**: Code block com syntax highlighting
**Animação**: Linhas aparecem sequencialmente
**Imagem**: Screenshot do código em VSCode dark theme
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: FastMCP é o SDK Python canônico. Inspirado no FastAPI — mesma ergonomia. Instalação: `pip install mcp`. Server mínimo em 5 linhas: import, instanciar, decorar função com `@mcp.tool()`, chamar `mcp.run()`. Por padrão roda em stdio (local). Para HTTP, passe `transport="streamable-http"`. A mágica: o decorator converte type hints em JSON Schema automaticamente. A docstring vira a descrição da tool.
💡 ANALOGIA: FastMCP é para MCP o que FastAPI é para HTTP. Decorator → endpoint. Type hints → schema. Docstring → documentação.
⚠️ ERROS COMUNS: Alunos esquecem de chamar `mcp.run()`. Sem isso, o server não sobe.
➡️ TRANSIÇÃO: "Vamos ver os 3 decorators canônicos."

---

### Slide 23 — Decorators: @tool, @resource, @prompt

**Título**: Decorators — @tool, @resource, @prompt
**Objetivo**: Mostrar os 3 decorators canônicos.
**Conteúdo**:
- `@mcp.tool()` — registra função como tool; docstring vira descrição; type hints viram schema
- `@mcp.resource("uri://{path}")` — registra resource; suporta templates com variáveis
- `@mcp.prompt()` — registra prompt template; argumentos viram parâmetros
- Type hints do Python → JSON Schema automaticamente

```python
@mcp.tool()
def read_config(path: str) -> str:
    """Lê arquivo de configuração."""
    return open(path).read()

@mcp.resource("config://app/{env}")
def get_config(env: str) -> str:
    """Configuração por ambiente."""
    return load_config(env)

@mcp.prompt()
def code_review(code: str) -> str:
    """Template de code review."""
    return f"Revise este código:\n{code}"
```

**Diagrama**: 3 colunas, uma por decorator, com mini-snippet
**Animação**: Colunas aparecem uma a uma
**Imagem**: 3 ícones: ferramenta (tool), arquivo (resource), template (prompt)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Três decorators canônicos. `@mcp.tool()` registra uma função como tool. A docstring vira a descrição da tool. Os type hints viram o JSON Schema automaticamente. `@mcp.resource("uri://{path}")` registra um resource — suporta templates com variáveis (`config://app/{env}`). `@mcp.prompt()` registra um prompt template — os argumentos viram parâmetros. A mágica do Python: type hints viram JSON Schema. Você não escreve schema manualmente — o decorator infere.
💡 ANALOGIA: É como OpenAPI/Swagger automático. Você anota a função; o schema é gerado.
⚠️ ERROS COMUNS: Alunos esquecem a docstring. Sem docstring, a tool fica sem descrição — o LLM não sabe quando usá-la. ACI do ETHAGT02: descrição rica é crítica.
➡️ TRANSIÇÃO: "Exemplos reais: filesystem e github."

---

### Slide 24 — Exemplo: Filesystem Server

**Título**: Exemplo — Filesystem Server
**Objetivo**: Mostrar um server de referência.
**Conteúdo**:
- **Tools**: `read_file`, `write_file`, `list_directory`, `search_files`
- **Resources**: `file://{path}` com mimeType dinâmico
- **Roots**: host define diretórios permitidos
- **Segurança**: validação de path (resolve, não aceitar `..`)
- Referência: `@modelcontextprotocol/server-filesystem` (TS) ou equivalente Python

**Diagrama**: Arquitetura do filesystem server (host → roots → server → FS)
**Animação**: Camadas aparecem
**Imagem**: Ícone de pasta com cadeado
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Filesystem é o server de referência mais clássico. Tools: `read_file`, `write_file`, `list_directory`, `search_files`. Resources: `file://{path}` com mimeType dinâmico (text, image, binary). Roots: o host define quais diretórios o server pode acessar — sandboxing fundamental. Segurança: validação de path. NUNCA aceitar `..` sem resolver — path traversal é o ataque mais comum. Referência oficial: `@modelcontextprotocol/server-filesystem` em TypeScript, ou equivalente em Python.
💡 ANALOGIA: É como um bibliotecário. Ele só te dá livros da seção permitida (roots). Ele valida que você não está pedindo "sai da biblioteca e pega do outro prédio" (path traversal).
⚠️ ERROS COMUNS: Alunos implementam `read_file(path)` sem validar. Vulnerabilidade clássica. Sempre: resolve path, check se está dentro das roots.
➡️ TRANSIÇÃO: "Outro exemplo: integração com API externa."

---

### Slide 25 — Exemplo: GitHub Server

**Título**: Exemplo — GitHub Server
**Objetivo**: Mostrar um server que integra API externa.
**Conteúdo**:
- **Tools**: `create_issue`, `list_prs`, `merge_pr`, `search_code`
- **Resources**: `github://repo/{owner}/{repo}/issue/{number}`
- **Prompts**: `pr-review-prompt(number)` — template de code review
- **Autenticação**: token via env var (`GITHUB_TOKEN`)
- Paginação e rate limiting do GitHub API

**Diagrama**: Fluxo: LLM → tool → GitHub API → resultado
**Animação**: Fluxo step-by-step
**Imagem**: Logo GitHub + ícone de API
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: GitHub é outro server de referência. Tools: `create_issue`, `list_prs`, `merge_pr`, `search_code`. Resources: `github://repo/{owner}/{repo}/issue/{number}` — você lê uma issue como resource. Prompts: `pr-review-prompt(number)` — template de code review oficial da organização. Autenticação: token via env var (`GITHUB_TOKEN`). Cuidados: paginação (GitHub retorna 30 por página) e rate limiting (5000 req/h autenticado). Esse server mostra como integrar APIs externas no padrão MCP.
💡 ANALOGIA: É como ter um assistente que fala a "língua do GitHub". Você pede "cria issue"; ele traduz para a API do GitHub; retorna o resultado padronizado.
⚠️ ERROS COMUNS: Alunos expõem token no código. NUNCA. Sempre env var ou secret manager.
➡️ TRANSIÇÃO: "Alternativa para devs Node: TypeScript SDK."

---

### Slide 26 — TypeScript SDK

**Título**: TypeScript SDK
**Objetivo**: Mostrar a alternativa TS para devs Node.js.
**Conteúdo**:
- `@modelcontextprotocol/sdk` — SDK oficial TypeScript
- API: `McpServer` + `server.tool()`, `server.resource()`, `server.prompt()`
- **Vantagem**: mesmo runtime de VSCode, Cursor, OpenCode
- Quando escolher TS: ecossistema Node, deploy em edge (Cloudflare Workers)

```typescript
import { McpServer } from "@modelcontextprotocol/sdk";

const server = new McpServer({ name: "meu-server", version: "1.0.0" });

server.tool("hello", { name: "string" }, async ({ name }) => ({
  content: [{ type: "text", text: `Olá, ${name}!` }]
}));

server.run({ transport: "stdio" });
```

**Diagrama**: Snippet TS lado a lado com Python
**Animação**: Linhas aparecem
**Imagem**: Logo TypeScript + Node.js
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: TypeScript SDK é a alternativa para devs Node. Pacote: `@modelcontextprotocol/sdk`. API: `McpServer` + `server.tool()`, `server.resource()`, `server.prompt()`. A vantagem: mesmo runtime de VSCode, Cursor, OpenCode (todos Electron/Node). Escolha TS quando: ecossistema Node, deploy em edge (Cloudflare Workers), ou integração com código TS existente.
💡 ANALOGIA: FastMCP é Python-first. SDK TS é Node-first. Mesma funcionalidade, ergonomia de cada linguagem.
⚠️ ERROS COMUNS: Alunos tentam misturar Python e TS no mesmo server. Não — escolha um SDK por server.
➡️ TRANSIÇÃO: "Como testar um server? MCP Inspector."

---

### Slide 27 — Testes de Server (MCP Inspector)

**Título**: Testes de Server — MCP Inspector
**Objetivo**: Mostrar como testar servers sem um host completo.
**Conteúdo**:
- `mcp inspector` — CLI interativo que conecta a qualquer server
- Lista tools, resources, prompts; executa tool calls manualmente
- Inspeção de schema, validação de responses
- Debug de transportes (stdio, HTTP)
- **CI**: testes automatizados com cliente MCP de teste

**Diagrama**: Screenshot do MCP Inspector (UI com lista de tools à esquerda)
**Animação**: Highlight dos elementos da UI
**Imagem**: Screenshot real do MCP Inspector
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: MCP Inspector é a ferramenta canônica de testes. CLI interativo que conecta a qualquer server. Lista tools, resources, prompts. Executa tool calls manualmente (você preenche os args, ele chama). Inspeciona schema, valida responses. Debug de transportes — funciona com stdio e HTTP. Para CI: você escreve testes automatizados usando um cliente MCP de teste (a SDK fornece). Isso é essencial — server sem teste é server não-production-ready.
💡 ANALOGIA: É como o Postman para APIs REST. Você testa sem precisar construir o frontend inteiro.
⚠️ ERROS COMUNS: Alunos testam só rodando no Claude Desktop. Ineficiente — Inspector é muito mais rápido para iterar.
➡️ TRANSIÇÃO: "Depois de testar, como distribuir."

---

### Slide 28 — Empacotamento e Distribuição

**Título**: Empacotamento e Distribuição
**Objetivo**: Mostrar como distribuir um MCP server.
**Conteúdo**:
- **Python**: pacote pip (`pip install meu-mcp-server`), entrypoint `meu-server`
- **TypeScript**: pacote npm, binário `npx meu-mcp-server`
- **Docker**: container com server HTTP (remote MCP)
- **Remote servers**: deploy em Cloudflare Workers, Vercel, fly.io
- **Registro**: publicar em catálogos (Awesome MCP, modelcontextprotocol.io)
- **Versionamento semântico** (semver) — quebra de schema = major bump

**Diagrama**: Pipeline: código → pacote → registro → host
**Animação**: Pipeline cresce da esquerda
**Imagem**: Ícones: código → caixa → registry → servidor
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Distribuir um MCP server é como distribuir qualquer pacote. Python: empacote como pip, com entrypoint. TS: empacote como npm, com binário `npx`. Para remote: container Docker com server HTTP, deploy em Cloudflare Workers, Vercel, fly.io. Registre em catálogos: Awesome MCP Servers, modelcontextprotocol.io/servers. Versionamento: semver estrito. Quebra de schema de tool = major bump. Nova tool = minor. Bug fix = patch.
💡 ANALOGIA: É como publicar uma biblioteca npm ou pip. Mesma mecânica, novo protocolo.
⚠️ ERROS COMUNS: Alunos publicam sem versionar ou pinam em `latest`. Antipattern grave em produção.
➡️ TRANSIÇÃO: "Agora a DEMO ao vivo."

---

### Slide 29 — DEMO: Meu Primeiro MCP Server

**Título**: DEMO — Meu Primeiro MCP Server
**Objetivo**: Demo ao vivo — construir server que expõe tools de consulta a dataset.
**Conteúdo**:
- Código do `05-Labs/ETHAGT08/Lab1-Primeiro-MCP-Server`
- **Passo 1**: criar server com FastMCP + 3 tools (query, stats, search)
- **Passo 2**: rodar em stdio
- **Passo 3**: configurar no OpenCode (ou Claude Desktop)
- **Passo 4**: mostrar LLM chamando tool via host
- **Passo 5**: adicionar resource (arquivo de config do dataset)

**Diagrama**: Code block + terminal side-by-side
**Animação**: Highlight de linhas chave
**Imagem**: Split screen — VSCode + terminal
**Tempo**: 5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: DEMO ao vivo. Vou construir um server em 5 passos. Passo 1: criar server FastMCP com 3 tools (query, stats, search sobre um dataset CSV). Passo 2: rodar em stdio. Passo 3: configurar no OpenCode (mostrar `opencode.json` com seção `mcp`). Passo 4: no chat do OpenCode, perguntar algo que dispara a tool — mostrar o LLM chamando. Passo 5: adicionar um resource (arquivo de config do dataset) e mostrar o LLM lendo. Total: ~5 min. Se algo quebrar, tenho screenshot do trace completo.
💡 ANALOGIA: É como a primeira vez que você conectou um backend a um frontend. A mágica do "funcionou" — mas padronizada.
⚠️ ERROS COMUNS: Se a API do LLM falhar, mostrar screenshot. Não improvisar — ter plano B pronto.
➡️ TRANSIÇÃO: "Vamos refletir sobre a DEMO."

---

### Slide 30 — Pergunta da DEMO

**Título**: Pergunta da DEMO
**Objetivo**: Engajar a turma com uma pergunta sobre a demo.
**Conteúdo**:
- "O que acontece se a tool retornar erro? Como o LLM reage?"
- "E se o LLM chamar uma tool que não existe?"
- "Resource vs Tool: quando usar cada para o mesmo dado?"
- Discussão em duplas (2 min)

**Diagrama**: Caixa de discussão com ícone de interrogação
**Animação**: Perguntas aparecem uma a uma
**Imagem**: Ícone de balão de conversa em `etho-accent`
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Pausa para refletir sobre a DEMO. Em duplas, 2 min. As três perguntas são clássicas de error handling. (1) Se a tool retorna erro, o LLM vê o erro como Observation e decide o que fazer — geralmente tenta alternativas ou pede ajuda ao usuário. (2) Se o LLM chama tool inexistente, o host retorna erro de "tool not found" — o LLM corrige. (3) Resource para leitura passiva, tool para ação — mesma regra do Slide 17.
❓ PERGUNTA PARA A TURMA: "O que acontece se a tool retornar erro? Como o LLM reage?" (deixar 2 duplas compartilharem)
⚠️ ERROS COMUNS: Alunos acham que erro quebra o agente. Não — erros são Observations. O LLM lida com eles.
➡️ TRANSIÇÃO: "Intervalo. Voltamos para clients e hosts."

---

## SEÇÃO E — Clients e Hosts (Slides 31-38 · 10 min)

---

### Slide 31 — [SEÇÃO] Clients e Hosts

**Título**: 4 — Clients e Hosts
**Objetivo**: Transição visual para o bloco de integração.
**Conteúdo**: "4 — Clients e Hosts"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "4" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Início do Bloco 2. Vimos como construir servers. Agora: como hosts consomem servers. Claude Desktop, VSCode, OpenCode, agente custom.
➡️ TRANSIÇÃO: "Começando pelo mecanismo interno."

---

### Slide 32 — Como um Host Instancia Clients

**Título**: Como um Host Instancia Clients
**Objetivo**: Mostrar o mecanismo interno de um host.
**Conteúdo**:
- Host lê config de servers (JSON)
- Para cada server configurado → cria 1 client → 1 conexão
- Client faz handshake (initialize → initialized)
- Host agrega capabilities de todos os servers
- **LLM vê tools de todos os servers como um conjunto unificado**
- Host roteia tool_call para o client/server correto

**Diagrama**: Flowchart: config → N clients → N servers → agregação no LLM
**Animação**: Clients surgem um a um
**Imagem**: Diagrama com 1 host, 3 clients, 3 servers
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Mecanismo interno do host. O host lê um arquivo de config JSON que lista os servers. Para cada server na config, o host cria 1 client → 1 conexão. Cada client faz o handshake (initialize → initialized). O host então agrega as capabilities de todos os servers. Para o LLM, todas as tools aparecem como um conjunto unificado — ele não sabe (nem precisa saber) qual server hospeda qual tool. Quando o LLM chama uma tool, o host roteia para o client/server correto.
💡 ANALOGIA: É como um tradutor simultâneo em reunião multilíngue. O host é o tradutor. Cada server é um idioma. O LLM (ouvinte) recebe tudo traduzido para uma língua só.
⚠️ ERROS COMUNS: Alunos acham que o LLM precisa saber qual server chamar. Não — o host roteia. O LLM só vê "tools".
➡️ TRANSIÇÃO: "Vejam a config do host de referência."

---

### Slide 33 — Claude Desktop: Config JSON

**Título**: Claude Desktop — Config JSON
**Objetivo**: Mostrar o formato de config do host de referência.
**Conteúdo**:
- Arquivo: `claude_desktop_config.json` (macOS/Linux/Windows)
- Estrutura: `mcpServers` com nome → `command` + `args` + `env`
- Exemplo:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/me/projects"],
      "env": {}
    }
  }
}
```

- Suporte a stdio (local) e HTTP (remote)

**Diagrama**: JSON block com syntax highlighting
**Animação**: Campos aparecem
**Imagem**: Screenshot do arquivo JSON em editor
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Claude Desktop é o host de referência da Anthropic. A config fica em `claude_desktop_config.json`. Estrutura: objeto `mcpServers` onde cada chave é o nome do server, e o valor tem `command`, `args`, e `env`. No exemplo: server "filesystem" usando `npx` para rodar `@modelcontextprotocol/server-filesystem` com path `/Users/me/projects`. Suporta stdio (local, como acima) e HTTP (remote). Para remote, a estrutura muda para `url` em vez de `command`.
💡 ANALOGIA: É como configurar extensões do VSCode. Um JSON, uma entrada por extensão, restart e pronto.
⚠️ ERROS COMUNS: Alunos erram o path do arquivo. Cada OS tem um local: macOS (`~/Library/Application Support/Claude/`), Windows (`%APPDATA%\Claude\`), Linux (`~/.config/Claude/`).
➡️ TRANSIÇÃO: "Outro host popular: VSCode."

---

### Slide 34 — VSCode MCP

**Título**: VSCode MCP
**Objetivo**: Mostrar integração no editor mais usado.
**Conteúdo**:
- VSCode (Copilot Chat) suporta MCP servers nativamente
- Config via `.vscode/mcp.json` ou settings workspace
- Servers aparecem como **tools no Copilot Chat**
- Suporte a stdio e HTTP
- **Debug**: output panel mostra logs do server

**Diagrama**: Screenshot do VSCode com MCP config + Copilot Chat usando tool
**Animação**: Highlight dos elementos
**Imagem**: Screenshot real do VSCode
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: VSCode suporta MCP nativamente desde 2025. Config via `.vscode/mcp.json` no workspace ou settings globais. Os servers aparecem como tools no Copilot Chat — você pergunta algo, o Copilot decide chamar a tool, executa, responde. Suporte a stdio e HTTP. Debug: o output panel mostra logs do server, essencial para troubleshooting.
💡 ANALOGIA: É como ter o Claude Desktop embutido no seu editor. Sem trocar de janela.
⚠️ ERROS COMUNS: Alunos esquecem de restartar o VSCode após mudar a config. Sem restart, não pega.
➡️ TRANSIÇÃO: "E a ferramenta que usamos no curso: OpenCode."

---

### Slide 35 — OpenCode: Config MCP

**Título**: OpenCode — Config MCP
**Objetivo**: Mostrar integração com a ferramenta usada na especialização.
**Conteúdo**:
- OpenCode: `opencode.json` com seção `mcp`
- Suporte a múltiplos servers (stdio e HTTP)
- Servers como **tools do agente OpenCode**
- **Vantagem**: mesmo runtime que os exemplos do curso
- Exemplo de config com 2 servers

**Diagrama**: Screenshot do `opencode.json` com seção `mcp`
**Animação**: Highlight da seção mcp
**Imagem**: Screenshot do OpenCode
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: OpenCode é a ferramenta que usamos no curso. Configura MCP no `opencode.json` com seção `mcp`. Suporta múltiplos servers — stdio e HTTP. Os servers viram tools do agente OpenCode. A vantagem: mesmo runtime que os exemplos do curso, então vocês podem reproduzir tudo localmente. Exemplo: configurar filesystem + github, e o agente OpenCode tem acesso a ambos.
💡 ANALOGIA: É como o `.vscode/extensions.json`, mas para MCP servers.
➡️ TRANSIÇÃO: "E se eu quiser meu próprio host? Agente custom."

---

### Slide 36 — Integrar em Agente Custom (LangGraph, OpenAI Agents SDK)

**Título**: Integrar em Agente Custom
**Objetivo**: Mostrar que MCP não é só para hosts pronto — pode ser embedding.
**Conteúdo**:
- **LangGraph**: `langchain-mcp-adapters` — carrega tools de server MCP como `BaseTool`
- **OpenAI Agents SDK**: MCP server como tool source
- **Padrão**: agente custom = host leve
- Snippet: carregar tools de server MCP e injetar em agente LangGraph
- **Vantagem**: reusar servers MCP sem acoplar a um host específico

```python
from langchain_mcp_adapters import load_mcp_tools

tools = await load_mcp_tools(server_connection)
agent = create_react_agent(llm, tools)
```

**Diagrama**: Arquitetura: agente custom → MCP client → server
**Animação**: Fluxo aparece
**Imagem**: Ícone de agente + MCP client + server
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: MCP não é só para hosts prontos (Claude, VSCode). Você pode embutir MCP no seu próprio agente. LangGraph: use `langchain-mcp-adapters` para carregar tools de um server MCP como `BaseTool` do LangChain. OpenAI Agents SDK: MCP server como tool source. O padrão: seu agente custom vira um "host leve" — instancia clients, agrega tools, roteia chamadas. Vantagem: reusar servers MCP (filesystem, github) sem acoplar a um host específico.
💡 ANALOGIA: É como escrever seu próprio navegador em vez de usar Chrome. Você controla tudo, mas herda os padrões (HTTP, HTML). Com MCP, você herda o protocolo.
⚠️ ERROS COMUNS: Alunos reimplementam o protocolo MCP no agente. Não — use as SDKs. Elas já fazem o handshake, o roteamento, etc.
➡️ TRANSIÇÃO: "Cenário real: múltiplos servers."

---

<details>
<summary>Continua na Parte 2 (Slides 37-70)</summary>

Ver arquivo `03-slides-detalhados-parte2.md`.
</details>

---

> **Mantido por**: Universidade Etho · Versão 1.0 · Julho 2026
> **Spec de referência**: MCP Specification 2025-11-25 (modelcontextprotocol.io)
