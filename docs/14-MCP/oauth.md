# Autenticação MCP (OAuth 2.1)

> Auth em remote MCP servers.

## Como funciona

Remote MCP usa **OAuth 2.1** com Authorization Code + PKCE para autenticação:

1. Client solicita tool que requer auth
2. Host redireciona para autorização (browser)
3. Usuário autoriza
4. Client recebe token e anexa às requisições

## Exemplo

```python
from mcp.auth import OAuthHandler

auth = OAuthHandler(
    client_id="meu-client",
    authorization_url="https://auth.exemplo.com/authorize",
    token_url="https://auth.exemplo.com/token",
    scopes=["tools:read"]
)

async with http_client("https://mcp.exemplo.com", auth=auth) as session:
    result = await session.call_tool("dados_sensiveis", {})
```

## Token Management

- Access token: curta duração (15 min)
- Refresh token: longa duração (7-30 dias)
- PKCE: obrigatório para public clients
- Revogação: possível via endpoint

## Provedores suportados

- GitHub OAuth Apps
- Google OAuth 2.0
- Auth0
- Custom OAuth server

## Referências
- OAuth 2.1 (RFC 6749, RFC 7636)
- MCP Auth spec: [spec/modelcontextprotocol.io](https://modelcontextprotocol.io/specification/auth)
