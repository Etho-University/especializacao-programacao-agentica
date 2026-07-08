# Construindo MCP Clients

> Como conectar agents a MCP servers.

## Python: Client Mínimo

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    params = StdioServerParameters(command="python", args=["server.py"])
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.call_tool("buscar", {"query": "agentes"})
            print(result.content)

asyncio.run(main())
```

## Integração com Agentes (LangChain/LangGraph)

```python
from langchain_mcp.adapters import load_mcp_tools

# Carrega tools de um MCP server automaticamente
tools = await load_mcp_tools("path/to/server.py")
agent = create_react_agent(model, tools)
```

## Conexão Remota

```python
# Streamable HTTP client
from mcp.client.http import http_client

async with http_client("https://mcp-exemplo.com") as session:
    tools = await session.list_tools()
    result = await session.call_tool(tools[0].name, {"arg": "valor"})
```

## Descoberta Dinâmica

O client pode perguntar ao server suas capacidades:

```python
server_info = await session.initialize()
capabilities = server_info.capabilities
tools = await session.list_tools()
resources = await session.list_resources()
```

## Referências
- MCP Client SDK: `pip install mcp`
- LangChain MCP Adapter: `pip install langchain-mcp`
