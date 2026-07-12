# ETHAGT08 — Lab 1: Meu primeiro MCP server

> Curso: MCP — Model Context Protocol · Carga: 25h · Pré-req: ETHAGT02

## Objetivo
Construir um MCP server funcional usando o Python SDK (FastMCP) que expõe tools de consulta a um dataset, e conectá-lo a um host real (Claude Desktop ou OpenCode) para validar o protocolo end-to-end.

## Preparação
- Ambiente: Python 3.11+, `pip install mcp`, Claude Desktop (ou VSCode com MCP, ou OpenCode)
- Dados/recursos: dataset CSV/JSON (ex.: catálogo de cursos da Universidade Etho em [`cursos.json`](https://raw.githubusercontent.com/Etho-University/especializacao-programacao-agentica/main/05-Labs/ETHAGT08/cursos.json))
- Leitura prévia: Apostila ETHAGT08, Unidade 1 (Por que MCP), Unidade 2 (Capabilities) e Unidade 3 (Servers)

## Roteiro
### Passo 1 — Instalar o MCP Python SDK
```bash
pip install "mcp[cli]"
```

**Checkpoint:** `mcp --version` responde sem erro.

### Passo 2 — Criar o server com FastMCP
Crie `server.py` com o decorator `@mcp.tool()`:

```python
from mcp.server.fastmcp import FastMCP
import json

mcp = FastMCP("etho-courses")

with open("cursos.json", encoding="utf-8") as f:
    COURSES = json.load(f)

@mcp.tool()
def list_courses(area: str = "") -> str:
    """List all courses, optionally filtered by area (e.g., 'agentica', 'dados').
    Returns course codes and titles."""
    filtered = [c for c in COURSES if not area or area in c.get("area", "")]
    return json.dumps([{"code": c["code"], "title": c["title"]} for c in filtered],
                      ensure_ascii=False)

@mcp.tool()
def get_course_details(code: str) -> str:
    """Get full details of a course by its code (e.g., 'ETHAGT01').
    Returns: title, credits, syllabus, prerequisites."""
    course = next((c for c in COURSES if c["code"] == code.upper()), None)
    if not course:
        return f"Error: course '{code}' not found"
    return json.dumps(course, ensure_ascii=False)
```

**Checkpoint:** server define 2 tools com descrições e tipos.

### Passo 3 — Adicionar um resource
Exponha dados estruturados como resource:

```python
@mcp.resource("courses://catalog")
def get_catalog() -> str:
    """Full course catalog as JSON"""
    return json.dumps(COURSES, ensure_ascii=False)
```

**Checkpoint:** resource acessível via URI `courses://catalog`.

### Passo 4 — Adicionar um prompt template
Crie um prompt reutilizável:

```python
@mcp.prompt()
def course_summary(code: str) -> str:
    """Generate a summary prompt for a specific course"""
    return f"""Summarize the course {code} in 3 bullet points.
    Use the get_course_details tool to fetch the data first."""
```

**Checkpoint:** prompt template aceita parâmetro e retorna string formatada.

### Passo 5 — Testar o server localmente
Use o MCP Inspector para testar interativamente:

```bash
mcp dev server.py
```

Abra o Inspector no navegador, liste tools, chame `list_courses` e `get_course_details`.

**Checkpoint:** ambas as tools retornam dados corretos no Inspector.

### Passo 6 — Configurar no Claude Desktop
Adicione o server ao arquivo de configuração do Claude Desktop:

```json
{
  "mcpServers": {
    "etho-courses": {
      "command": "python",
      "args": ["C:\\caminho\\para\\server.py"]
    }
  }
}
```

Caminho do arquivo: `~/.config/claude-desktop/claude_desktop_config.json` (ou equivalente no Windows).

**Checkpoint:** Claude Desktop reinicia e mostra o server conectado.

### Passo 7 — Testar end-to-end
No Claude Desktop, faça perguntas que ativam as tools:

- "Quais cursos existem na área de programação agêntica?"
- "Me dê detalhes do curso ETHAGT08"
- "Faça um resumo do curso ETHAGT05"

**Checkpoint:** Claude usa as tools automaticamente e responde corretamente.

### Passo 8 — Adicionar logging e tratamento de erro
Robustez no server:

```python
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

@mcp.tool()
def search_courses(keyword: str) -> str:
    """Search courses by keyword in title or syllabus."""
    logging.info(f"search_courses called with: {keyword}")
    try:
        results = [c for c in COURSES if keyword.lower() in
                   (c["title"] + c.get("syllabus", "")).lower()]
        if not results:
            return f"No courses found for '{keyword}'"
        return json.dumps(results, ensure_ascii=False)
    except Exception as e:
        logging.error(f"search_courses failed: {e}")
        return f"Error: {e}"
```

**Checkpoint:** logs aparecem no terminal do server; erro tratado retorna mensagem útil.

## Desafios extras
- Adicione uma 4ª tool `get_prerequisites(code)` que retorna a árvore de pré-requisitos recursivamente
- Implemente o server em TypeScript SDK e compare a experiência
- Adicione sampling: o server pede ao LLM do host para classificar o nível de um curso
- Empacote o server como Docker container

## Entrega
- Repositório com `server.py`, `cursos.json`, `README.md` com instruções de setup
- Screenshot do Claude Desktop usando as tools
- Commit no padrão `ETHAGT08: lab-1 construir primeiro mcp server`

## Rubrica
Avaliado pela rubrica em `08-Assignments/ETHAGT08/assignment-01.md` (Pilar Comportamental 20%: colaboração em labs).
