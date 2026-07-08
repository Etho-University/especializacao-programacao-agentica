from mcp.server.fastmcp import FastMCP

mcp = FastMCP("etho-example-server")

@mcp.tool()
def calculate(expression: str) -> str:
    """Avalia uma expressão matemática simples. Ex.: '2 + 2', '123 * 456'"""
    allowed = set("0123456789+-*/.() ")
    if not all(c in allowed for c in expression):
        return "Erro: caracteres não permitidos"
    try:
        return str(eval(expression, {"__builtins__": {}}, {}))
    except Exception as e:
        return f"Erro: {e}"

@mcp.tool()
def search_kb(query: str, top_k: int = 3) -> list:
    """Simula busca em base de conhecimento. Retorna documentos relevantes."""
    kb = [
        {"id": 1, "title": "Augmented LLM", "content": "LLM + retrieval + tools + memory"},
        {"id": 2, "title": "ReAct Loop", "content": "Thought → Action → Observation"},
        {"id": 3, "title": "MCP Protocol", "content": "Model Context Protocol para ferramentas"},
        {"id": 4, "title": "Agent Memory", "content": "4 camadas: working, episodic, semantic, procedural"},
        {"id": 5, "title": "Multi-Agent Topologies", "content": "Supervisor, Hierarchical, Swarm, Event-Driven"},
    ]
    results = [d for d in kb if query.lower() in d["title"].lower() or query.lower() in d["content"].lower()]
    return results[:top_k]

if __name__ == "__main__":
    mcp.run(transport="stdio")
