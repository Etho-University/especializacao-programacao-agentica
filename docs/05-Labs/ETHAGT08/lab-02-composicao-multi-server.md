# ETHAGT08 — Lab 2: Composição multi-server (arXiv + GitHub)

> Curso: MCP — Model Context Protocol · Carga: 25h · Pré-req: ETHAGT08 Lab 1

## Objetivo
Construir dois MCP servers distintos (arXiv e GitHub), compô-los em um único agente que usa tools de ambos simultaneamente, e aplicar governança básica (permissões, logs, versionamento).

## Preparação
- Ambiente: Python 3.11+, `pip install mcp httpx PyGithub`, `.env` com `GITHUB_TOKEN`
- Dados/recursos: acesso à API do arXiv e GitHub
- Leitura prévia: Apostila ETHAGT08, Unidade 4 (Clients e hosts) e Unidade 5 (Governança)

## Roteiro
### Passo 1 — Construir o arXiv MCP server
Crie `arxiv_server.py` com tools para buscar papers:

```python
from mcp.server.fastmcp import FastMCP
import httpx

mcp = FastMCP("arxiv-search")

@mcp.tool()
async def search_papers(query: str, max_results: int = 5) -> str:
    """Search arXiv for papers matching the query.
    Returns: title, authors, arXiv ID, abstract snippet.
    Example: search_papers(query='ReAct LLM agents', max_results=3)"""
    url = f"http://export.arxiv.org/api/query?search_query=all:{query}&max_results={max_results}"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
    # Parse XML e extrair campos
    return parse_arxiv_response(resp.text)

@mcp.tool()
async def get_paper(arxiv_id: str) -> str:
    """Get full metadata of a paper by its arXiv ID (e.g., '2210.03629')."""
    ...
```

**Checkpoint:** `search_papers("ReAct")` retorna papers reais do arXiv.

### Passo 2 — Construir o GitHub MCP server
Crie `github_server.py` com tools para repositórios:

```python
from github import Github
import os

mcp = FastMCP("github-tools")
gh = Github(os.environ["GITHUB_TOKEN"])

@mcp.tool()
def search_repos(query: str, language: str = "") -> str:
    """Search GitHub repositories.
    Example: search_repos(query='langgraph agent', language='Python')"""
    repos = gh.search_repositories(query=f"{query} language:{language}" if language else query)
    return json.dumps([{"full_name": r.full_name, "stars": r.stargazers_count,
                        "description": r.description} for r in repos[:10]])

@mcp.tool()
def get_readme(owner: str, repo: str) -> str:
    """Get the README content of a GitHub repository.
    Example: get_readme(owner='langchain-ai', repo='langgraph')"""
    repo = gh.get_repo(f"{owner}/{repo}")
    return repo.get_readme().decoded_content.decode()
```

**Checkpoint:** `search_repos("langgraph")` retorna repositórios reais.

### Passo 3 — Configurar composição multi-server
No agente custom (LangGraph ou OpenAI Agents SDK), configure ambos os servers:

```python
# config.json para o agente
{
  "mcpServers": {
    "arxiv": {"command": "python", "args": ["arxiv_server.py"]},
    "github": {"command": "python", "args": ["github_server.py"]}
  }
}
```

Ou configure no Claude Desktop para uso interativo.

**Checkpoint:** host reconhece ambos os servers e suas tools.

### Passo 4 — Agente que usa ambos
Crie um agente que combina fontes para responder perguntas de pesquisa:

```python
SYSTEM = """You have access to arXiv and GitHub tools.
Use arXiv to find relevant papers, and GitHub to find implementations.
When asked about a technique, provide both the paper reference and a repo example."""
```

**Checkpoint:** agente usa tools de ambos os servers em uma única conversa.

### Passo 5 — Teste de composição
Faça perguntas que exigem ambos os servers:

- "Encontre o paper original do ReAct e um repositório que o implementa"
- "Quais papers sobre GraphRAG existem e há implementações no GitHub?"
- "Busque o paper do DSPy e mostre o README do repo oficial"

**Checkpoint:** agente encadeia chamadas entre arXiv e GitHub corretamente.

### Passo 6 — Governança: permissões por server
Implemente controle de permissões — arXiv é read-only, GitHub pode ter write:

```python
SERVER_PERMISSIONS = {
    "arxiv": {"read": True, "write": False, "network": True},
    "github": {"read": True, "write": False, "network": True}  # write=False por segurança
}

def check_permission(server, action):
    allowed = SERVER_PERMISSIONS.get(server, {}).get(action, False)
    if not allowed:
        log_security(f"BLOCKED: {server}.{action}")
        raise PermissionError(f"Server '{server}' cannot {action}")
```

**Checkpoint:** tentativa de write no arXiv é bloqueada e logada.

### Passo 7 — Governança: auditoria
Registre todas as chamadas de tools em `audit_log.jsonl`:

```python
def log_tool_call(server, tool, args, result, user="agent"):
    entry = {"timestamp": datetime.now().isoformat(),
             "server": server, "tool": tool, "args": args,
             "result_size": len(str(result)), "user": user}
    with open("audit_log.jsonl", "a") as f:
        f.write(json.dumps(entry) + "\n")
```

**Checkpoint:** cada chamada de tool produz entrada de auditoria.

### Passo 8 — Versionamento dos servers
Adicione versionamento semântico e um health check:

```python
SERVER_VERSION = "1.0.0"

@mcp.tool()
def health_check() -> str:
    """Returns server version and status."""
    return json.dumps({"version": SERVER_VERSION, "status": "healthy",
                       "tools_count": len(mcp._tool_manager._tools)})
```

**Checkpoint:** health check retorna versão e número de tools disponíveis.

## Desafios extras
- Adicione um 3º server (ex.: Semantic Scholar, ou um DB interno) e teste composição tripla
- Implemente rate limiting por server
- Adicione um server destrutivo (criar issue no GitHub) com HITL
- Documente um threat model dos 2 servers em `threat_model.md`

## Entrega
- Repositório com `arxiv_server.py`, `github_server.py`, `agent.py`, `audit_log.jsonl`
- Commit no padrão `ETHAGT08: lab-2 compor servers arxiv github`

## Rubrica
Avaliado pela rubrica em `08-Assignments/ETHAGT08/assignment-01.md` (Pilar Comportamental 20%: colaboração em labs).
