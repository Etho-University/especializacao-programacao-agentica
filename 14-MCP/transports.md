# MCP — Transports

## Dois transportes oficiais

### 1. stdio (local)

- Server roda como **subprocesso** do host.
- Comunicação via **stdin/stdout** (JSON-RPC).
- Env vars passadas pelo host.

**Vantagens**: simples, sem rede, seguro (isolado por processo), ideal para dev/local.

**Desvantagens**: só local; servidor precisa rodar na máquina do usuário.

**Config no host**:
```json
{
  "mcpServers": {
    "meu-server": {
      "command": "python",
      "args": ["/caminho/server.py"],
      "env": { "API_KEY": "..." }
    }
  }
}
```

### 2. Streamable HTTP (remoto)

Introduzido em março/2025, **substituiu HTTP+SSE**. Server é processo independente acessível via HTTP.

- **POST** para enviar mensagens ao server.
- **GET** (opcional) abre stream SSE para receber updates do server em tempo real.
- Stateless por default (state na URL/session token).

**Vantagens**: deploy remoto (cloud, edge); multi-cliente; autenticável (OAuth); escalável.

**Desvantagens**: complexidade de deploy; latência de rede; exige TLS.

**Deploy típico**: Cloudflare Workers, Fly.io, AWS Lambda, qualquer HTTP server.

## Por que HTTP+SSE foi substituído

O transporte HTTP+SSE original mantinha **conexões SSE de longa duração** com estado, o que era problemático para:

- **Autenticação**: conexões longas com tokens expirando.
- **Load balancing**: conexões pegadas a um servidor.
- **Serverless**: plataformas com timeout em conexões longas.
- **Reconexão**: lógica complexa para recuperar estado.

Streamable HTTP usa requests isolados (stateless), simplificando tudo isso.

## Escolha

| Cenário | Transporte |
|---|---|
| Dev local, dados locais | **stdio** |
| Server acessa serviços locais (filesystem, Docker socket) | **stdio** |
| Server compartilhado entre usuários | **Streamable HTTP** |
| Server em cloud/edge | **Streamable HTTP** |
| Server precisa de auth corporativa | **Streamable HTTP** + OAuth |

## Exemplo: rodar ambos

Servers podem suportar **ambos** transports (escolha em runtime). FastMCP suporta:

```python
mcp.run(transport="stdio")  # ou "streamable-http"
```

## Referências

- <https://modelcontextprotocol.io/specification/2025-11-25/basic/transports>
- Auth0 blog (maio/2025).
- Cloudflare *Remote MCP* (2025).
