---
password: Etho-Prof-2026
---
# ETHAGT08 — Gabarito

> Restrito a mentores. Cada resposta justificada com referência à apostila.

## Múltipla escolha

1. **b)** — O host é a aplicação que o usuário usa (ex.: Claude Desktop, VSCode, OpenCode) e que instancia um ou mais clients MCP para se conectar a servers (Capítulo 1 — Por que MCP, arquitetura host/client/server).

2. **b)** — Tools são funções com schema JSON (executam ações); Resources são dados estruturados (arquivos, DB rows — leitura); Prompts são templates reutilizáveis de interação (Capítulo 2 — O modelo de capabilities).

3. **b)** — Sampling permite que o servidor solicite inferência do LLM do host (server-initiated), invertendo a direção habitual da comunicação (Capítulo 2.4 — Sampling).

4. **d)** — gRPC bidirecional com protobuf obrigatório não é um transporte nativo de MCP. Os transportes suportados são stdio, HTTP+SSE e streamable HTTP (Capítulo 1.4 — Transportes).

## Verdadeiro ou Falso (justificado)

1. **Falso.** MCP não substitui o tool calling nativo — é um protocolo padronizado para expor tools, resources e prompts a hosts/clients. O host repassa as tools MCP ao LLM usando o mecanismo de tool calling nativo do modelo (Capítulo 1 e exercícios do syllabus).

2. **Verdadeiro.** Um MCP server é uma boundary de confiança que executa código e acessa dados. Deve ser tratado com sandboxing, rate limiting e auditoria de logs, especialmente servers de terceiros (Capítulo 6 — Segurança e produção).

3. **Verdadeiro.** Mudanças breaking em tools/schemas de um MCP server podem quebrar agentes em produção que dependem da interface anterior. Versionamento semântico comunica compatibilidade (Capítulo 5.2 — Versionamento).

4. **Verdadeiro.** Documentos maliciosos em Resources podem conter instruções de prompt injection indireto. Quando o host lê o resource e o injeta no contexto do LLM, as instruções maliciosas são executadas (Capítulo 6.3 — Prompt injection via resources).

## Código curto

1. **Config JSON para Claude Desktop:**
```json
{
  "mcpServers": {
    "my-server": {
      "command": "python",
      "args": ["server.py"]
    }
  }
}
```
Referência: Capítulo 4 (Clients e hosts, Claude Desktop config).

2. **MCP server com FastMCP:**
```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather-server")

@mcp.tool()
def get_weather(city: str) -> str:
    """Retorna o clima atual de uma cidade."""
    return fetch_weather(city)

if __name__ == "__main__":
    mcp.run(transport="stdio")
```
Referência: Capítulo 3 (Construindo servers, Python SDK).

3. **Rate limiting:**
```python
from collections import defaultdict
from time import time

calls = defaultdict(list)

def rate_limit(client_id, max_per_min=60):
    now = time()
    calls[client_id] = [t for t in calls[client_id] if now - t < 60]
    if len(calls[client_id]) >= max_per_min:
        raise Exception("Rate limit exceeded")
    calls[client_id].append(now)
```
Referência: Capítulo 6 (Rate limiting, quotas).

## Análise de trade-off

1. **stdio vs. HTTP+SSE:** stdio é mais simples (sem rede), ideal para servers locais acoplados ao host. HTTP+SSE permite servers remotos, compartilhados entre múltiplos hosts e escaláveis. stdio para desenvolvimento/local; HTTP+SSE para produção distribuída (Capítulo 1.4).

2. **Tools nativas vs. MCP:** Tools nativas são mais rápidas (sem overhead de protocolo) e integradas ao código do agente. MCP vale a pena quando há múltiplos hosts/agentes que precisam das mesmas tools, quando servers são mantidos por equipes separadas, ou quando se quer reusar servers da comunidade (Capítulo 1 e 4).

3. **SBOM/provenance vs. allowlist:** SBOM/provenance oferece rastreabilidade automatizada de dependências e vulnerabilidades conhecidas, mas não bloqueia execução. Allowlist manual é mais simples e determinístico (só servers aprovados rodam), mas não detecta vulnerabilidades dentro dos servers aprovados. Ideal: combinar ambos (Capítulo 5.4 — Supply chain security).

## Debug / diagnóstico

1. **Causas de tools não aparecerem:**
   - **Erro de inicialização do server:** O processo falha ao iniciar (erro de import, path errado). Verificar logs do host.
   - **Schema inválido:** As tools têm schema malformado e o host as rejeita. Validar JSON Schema.
   - **Transporte incorreto:** Server espera stdio mas host configura HTTP, ou vice-versa.
   Referência: Capítulo 3 e 4.

2. **Risco:** Path traversal — o server permite ler qualquer path no filesystem. **Mitrações:** (1) Restringir a um diretório base (allowlist de paths); (2) Sanitizar/validar paths antes de acessar (Capítulo 6 — Segurança).
