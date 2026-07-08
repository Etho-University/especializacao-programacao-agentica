# MCP — Especificação (resumo)

> Última versão consultada: **2025-11-25**. Sempre verifique <https://modelcontextprotocol.io/specification> para a versão atual.

## Visão geral

MCP é um protocolo **JSON-RPC 2.0** com capabilities negociadas. Comunicação é estruturada em mensagens tipadas.

## Lifecycle de uma conexão

```
1. Initialize: client e server trocam capabilities suportadas
2. Initialized: conexão pronta
3. (Operações: list tools, call tool, read resource, etc.)
4. Shutdown
```

## Capabilities (negociação)

Cada lado declara o que suporta:

- **Server**: `tools`, `resources`, `prompts`, `logging`, `sampling`.
- **Client**: `sampling` (aceita pedidos do server), `roots` (declara acessos).

## Mensagens principais

### Tools
- `tools/list` — lista tools disponíveis.
- `tools/call` — chama uma tool com args; retorna resultado (texto, imagem, resource).

### Resources
- `resources/list` — lista resources.
- `resources/read` — lê conteúdo por URI.
- `resources/subscribe` — assina mudanças.

### Prompts
- `prompts/list` — lista prompts.
- `prompts/get` — resolve um prompt com args.

### Sampling
- `sampling/createMessage` — server pede ao client/host para chamar o LLM.

### Roots
- Client declara diretórios/arquivos permitidos ao server (sandboxing).

### Logging
- Server emite logs estruturados ao client.

## Transports

- **stdio** (local): subprocesso, stdin/stdout.
- **Streamable HTTP** (remoto, desde março/2025): substituiu HTTP+SSE. POST para mensagens; SSE opcional para streaming.

## Autenticação (remote)

- **OAuth 2.1** é o padrão para remote MCP.
- Scopes por capability.

## Versionamento

- Spec versionada (data-based: `2025-11-25`, `2025-06-18`, `2025-03-26`).
- Breaking changes sinalizados.

## Mudanças recentes (2025)

- **Mar/2025**: Streamable HTTP substitui HTTP+SSE.
- **Maio/2025**: spec oficializada a transição.
- Suporte crescente a remote MCP (Cloudflare, etc.).

## Referências

- <https://modelcontextprotocol.io/specification/2025-11-25>
- Auth0 *Streamable HTTP* analysis (2025).
