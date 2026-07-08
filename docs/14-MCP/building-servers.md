# Construindo MCP Servers

> Guia prático: Python (FastMCP) e TypeScript SDK.

## Python com FastMCP

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("meu-server")

@mcp.tool()
def buscar(query: str) -> str:
    """Busca informação na base."""
    return f"Resultados para: {query}"

@mcp.resource("dados://{path}")
def ler_recurso(path: str) -> str:
    """Lê um resource por URI."""
    return f"Conteúdo de {path}"

mcp.run(transport="stdio")  # ou "sse" para Streamable HTTP
```

## TypeScript SDK

```typescript
import { Server } from "@modelcontextprotocol/sdk";

const server = new Server({ name: "meu-server", version: "1.0.0" }, {
    capabilities: { tools: {} }
});

server.setRequestHandler("tools/call", async (req) => {
    if (req.params.name === "buscar") {
        return { content: [{ type: "text", text: `Resultado: ${req.params.arguments.query}` }] };
    }
    throw new Error("Tool desconhecida");
});

server.listen({ transport: "stdio" });
```

## Princípios ACI (Agent-Computer Interface)

- Tool name: verbo + substantivo (`buscar_cliente`, não `executar`)
- Description: clara, sem jargão
- Parameters: tipos específicos, sem `any`
- Return: estruturado (JSON), não texto livre
- Error handling: mensagens legíveis para o agente

## Boas práticas

- **Idempotência** quando possível (tools de leitura)
- **Timeout** obrigatório em tools externas
- **Rate limiting** para evitar surpresas de custo
- **Versionamento** do catálogo de tools

## Referências
- FastMCP: [github.com/jlowin/fastmcp](https://github.com/jlowin/fastmcp)
- MCP SDK (Python): `pip install mcp`
- MCP SDK (TypeScript): `npm install @modelcontextprotocol/sdk`
