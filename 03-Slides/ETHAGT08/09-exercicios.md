# ETHAGT08 — Exercícios

> Exercícios para aula e para casa.
> Organizados por tipo: em aula, individual, em duplas, projeto.

---

## Exercícios em Aula

### E1 — Onde o MCP se Encaixa? (Discussão em Duplas)
**Slide**: 13
**Tempo**: 2 min
**Formato**: Duplas, 2 min discussão + 1 min compartilhar

**Enunciado**: Em duplas, discutam:

1. Qual sistema da sua empresa você transformaria em MCP server primeiro?
2. Quais dados você NÃO exporia via MCP server?

**Gabarito**:
1. Respostas variam — aceitar qualquer sistema com API estável e valor para agentes (Salesforce, SAP, Confluence, Jira, DB interno).
2. Dados sensíveis: dados de RH (salários, avaliações), dados de saúde (LGPD), chaves de API, dados pessoais identificáveis sem anonimização, dados financeiros detalhados.

---

### E2 — O Que Acontece Se...? (Discussão em Duplas)
**Slide**: 30
**Tempo**: 2 min
**Formato**: Duplas, 2 min discussão + 1 min compartilhar

**Enunciado**: Após a DEMO do primeiro server, discutam em duplas:

1. O que acontece se a tool retornar erro? Como o LLM reage?
2. E se o LLM chamar uma tool que não existe?
3. Resource vs Tool: quando usar cada para o mesmo dado?

**Gabarito**:
1. O erro vira uma Observation estruturada para o LLM. O LLM decide: tentar de outra forma, pedir ajuda ao usuário, ou reportar falha. Erro bem-formado inclui `{"error": "...", "suggestion": "..."}`.
2. O host retorna `method not found` ou `tool not found`. O LLM vê o erro e evita repetir — geralmente pede esclarecimento ao usuário.
3. Resource para leitura passiva (ler config, ler issue do GitHub). Tool para ação (salvar config, criar issue). Mesmo dado pode ser exposto como ambos: resource para ler, tool para modificar.

---

### E3 — Mitigando Path Traversal (Individual + Share)
**Slide**: 54
**Tempo**: 3 min
**Formato**: Individual (2 min) + share (1 min)

**Enunciado**: Cenário: um MCP server de arquivos permite ler qualquer path (sem validação). Como você mitigaria path traversal?

**Estratégias esperadas**:
1. **Roots** — host define boundary de diretórios permitidos; server só acessa dentro delas.
2. **Path validation** — resolve o path (elimina `..`), check se resultado está dentro das roots.
3. **Sandbox FS** — container Docker com mount read-only; tmpfs para escrita temporária.
4. **Allowlist de extensões** — só `.txt`, `.md`, `.json`, `.yaml`; bloqueia `.env`, `.key`, `.pem`.

**Critério de avaliação**:
- Lista pelo menos 2 estratégias ✅
- Menciona combinação de camadas (defense in depth) ✅
- Reconhece que path validation sozinha é insuficiente ✅

---

### E4 — Config e Segurança (Individual + Share)
**Slide**: 59
**Tempo**: 5 min
**Formato**: Individual (3 min) + share (2 min)

**Enunciado**: Cenário: adicionar um MCP server de banco de dados ao Claude Desktop.

**Tarefa 1**: Escreva a config JSON para `claude_desktop_config.json`.

**Tarefa 2**: Liste 3 riscos de segurança e proponha mitigação para cada.

**Gabarito — Tarefa 1**:
```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-postgres",
        "postgresql://localhost/mydb"
      ],
      "env": {
        "PGPASSWORD": "${PG_PASSWORD}"
      }
    }
  }
}
```

**Gabarito — Tarefa 2** (exemplos válidos):

| Risco | Mitigação |
|---|---|
| SQL injection via tool args | Parameterized queries; validação de schema de args |
| Vazamento de dados sensíveis via resources | ACL por tabela; anonimização; HITL para tabelas sensíveis |
| Custo de tokens com query gigante | Limit de rows retornado; paginação obrigatória |
| Escrita acidental (DROP, DELETE) | Modo read-only por padrão; HITL para tools de escrita |
| Vazamento de credenciais no log | Não logar args com secrets; redação automática |

**Critério de avaliação**:
- JSON syntax válido ✅
- Usa env var para senha (não hardcode) ✅
- Lista 3 riscos específicos (não genéricos) ✅
- Mitigação é concreta e técnica ✅

---

## Exercícios Individuais (para casa)

### E5 — Diferencie Tool, Resource e Prompt
**Tempo estimado**: 10 min
**Formato**: Individual, escrito

**Enunciado**: Em suas palavras, defina tool, resource e prompt em MCP. Dê um exemplo de cada.

**Critério de avaliação**:
- Define tool como "função com schema, executada pelo server, retorna resultado" ✅
- Define resource como "dado identificado por URI, leitura passiva" ✅
- Define prompt como "template nomeado com argumentos, servido pelo server" ✅
- Exemplos são realistas e distintos ✅

**Exemplo de resposta**:
- **Tool**: `create_issue(repo, title, body)` — cria issue no GitHub; ação com efeito colateral.
- **Resource**: `github://repo/owner/name/issue/42` — URI que retorna o conteúdo da issue 42; leitura.
- **Prompt**: `pr-review-prompt(pr_number)` — template de prompt para code review; injetado no LLM.

---

### E6 — Quando Usar Sampling?
**Tempo estimado**: 10 min
**Formato**: Individual, escrito

**Enunciado**: Responda:

1. Quando um server deveria usar sampling (server-initiated LLM call)?
2. Por que o server nunca tem acesso direto à API key do LLM?
3. Por que HITL é recomendado para sampling em produção?

**Gabarito**:
1. Quando o server processa dados locais e precisa de raciocínio LLM sem expor tudo ao host diretamente. Exemplos: sumarização de documento grande, classificação de tickets, raciocínio sobre dados sensíveis. Server envia dados ao LLM via host, não direto.
2. Para manter controle com o host. Se o server tivesse acesso direto à API key, qualquer server malicioso poderia: (a) gastar tokens ilimitadamente; (b) exfiltrar dados via prompts maliciosos; (c) burlar rate limits e auditoria do host.
3. HITL protege contra: (a) server malicioso que usa sampling para exfiltrar dados (pede ao LLM para sumarizar dados sensíveis e enviar a endpoint externo); (b) custos inesperados; (c) raciocínio indesejado. Sem HITL, sampling é vetor de ataque grave.

---

### E7 — Config JSON para Claude Desktop
**Tempo estimado**: 15 min
**Formato**: Individual, código

**Enunciado**: Escreva a config JSON para adicionar DOIS servers ao Claude Desktop:
1. Um server de filesystem (TypeScript) com acesso a `/Users/aluno/projects`
2. Um server custom seu (Python, FastMCP) rodando via `python -m meu_server`

**Exemplo de resposta**:
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/aluno/projects"
      ],
      "env": {}
    },
    "meu-server": {
      "command": "python",
      "args": ["-m", "meu_server"],
      "env": {
        "PYTHONPATH": "/Users/aluno/dev/meu_server"
      }
    }
  }
}
```

**Critério de avaliação**:
- JSON syntax válido ✅
- Dois servers com nomes distintos ✅
- Args corretos para cada server ✅
- Uso de env vars quando apropriado ✅

---

### E8 — Liste 5 Riscos de Segurança
**Tempo estimado**: 10 min
**Formato**: Individual, escrito

**Enunciado**: Liste 5 riscos de segurança distintos de um MCP server em produção. Para cada, dê uma mitigação concreta.

**Gabarito** (exemplos válidos):

| # | Risco | Mitigação |
|---|---|---|
| 1 | Path traversal via tool de arquivo | Roots + path validation (resolve + check prefix) + sandbox FS |
| 2 | Prompt injection via resource não confiável | Marcar resource como untrusted; HITL para ações destrutivas |
| 3 | Exfiltração via sampling | HITL obrigatório em todo sampling; budget de tokens |
| 4 | Server malicioso no catálogo (supply chain) | SBOM; assinatura de pacote; audit de deps; reproducible build |
| 5 | Remote server sem autenticação | OAuth 2.1 obrigatório; TLS; scopes por tool |
| 6 | Tool confusion (nomes sobrepostos) | Namespacing; descrições ricas (ACI) |
| 7 | Token exhaustion (resource gigante) | Limit de tamanho de resource; paginação |
| 8 | Credenciais vazadas em log | Redação automática de secrets; não logar args sensíveis |

**Critério de avaliação**:
- Lista exatamente 5 riscos distintos ✅
- Cada mitigação é técnica e concreta ✅
- Reconhece defense in depth (combinação de camadas) ✅

---

### E9 — Verdadeiro/Falso Justificado
**Tempo estimado**: 10 min
**Formato**: Individual, escrito

**Enunciado**: Responda V ou F e justifique em 2-3 frases:

1. "MCP substitui o tool calling nativo do LLM."
2. "HTTP+SSE é o transporte canônico para remote servers na spec 2025-11-25."
3. "Resources são ideais para representar ações com efeito colateral."
4. "Server MCP tem acesso direto à API key do LLM do host."
5. "OAuth 2.1 é opcional para remote MCP servers."

**Gabarito**:
1. **F** — MCP padroniza o protocolo de comunicação host↔server. O modelo continua usando tool calling nativo. MCP é a camada de padronização.
2. **F** — HTTP+SSE está deprecated desde março/2025. Streamable HTTP é o canônico na spec 2025-11-25.
3. **F** — Resources são para dados passivos (leitura). Ações com efeito colateral são Tools.
4. **F** — Server nunca tem acesso direto à API key. Toda chamada ao LLM passa pelo host (via sampling), que controla.
5. **F** — OAuth 2.1 é mandatório para remote servers na spec 2025-11-25. PKCE obrigatório.

---

### E10 — Trade-offs de Multi-Server
**Tempo estimado**: 15 min
**Formato**: Individual, escrito

**Enunciado**: Liste 3 trade-offs ao compor múltiplos servers MCP em um host. Para cada, dê um número ou exemplo concreto.

**Exemplo de resposta**:

1. **Explosão de contexto**: Cada server adiciona tools cujos schemas vão ao contexto. 5 servers × 10 tools × ~100 tokens/schema = 5000 tokens só de schemas. Em uma sessão longa, isso comprime o espaço para dados reais.
2. **Roteamento e ambiguidade**: Com 50 tools agregadas, o LLM pode escolher a errada. Ex.: `read_file` (filesystem) vs `read_config` (custom) — sem namespacing, o LLM pode confundir. Mitigação: prefixar (`fs_read_file`, `cfg_read_config`).
3. **Falha em cascata**: Se um server cai, o host deve isolá-lo (circuit breaker). Sem circuit breaker, chamadas a tools do server caído geram timeouts que travam o agente. Ex.: server de slack cai, todas as tools de slack retornam timeout por 30s — degrada UX.

---

## Projeto do Módulo

### P1 — MCP Server Útil com Governança
**Prazo**: 2 semanas
**Formato**: Individual ou dupla
**Carga**: ~10h

**Descrição**: Projetar e construir um **MCP server útil** (ex.: Confluence Etho, SAP OData, Salesforce, Jira, ServiceNow) com governança completa.

**Entregáveis**:
1. **Server funcional** (Python FastMCP ou TypeScript SDK) com:
   - Mínimo 3 tools com schemas explícitos e descrições ricas (ACI)
   - Pelo menos 1 resource identificado por URI
   - Pelo menos 1 prompt template
   - Suporte a stdio e/ou Streamable HTTP
2. **Documentação** (README):
   - Visão geral do server
   - Lista de tools/resources/prompts com schemas
   - Exemplo de config para Claude Desktop / OpenCode
   - Instruções de instalação e uso
3. **ADR de Governança** (Architecture Decision Record):
   - Contexto: por que este server? Qual problema resolve?
   - Decisão: quais tools? Quais permissões? Qual owner?
   - Consequences: impactos positivos e negativos
   - Review date: quando revisitar
4. **Threat Model**:
   - Lista de riscos identificados (mínimo 5)
   - Mitigação para cada risco
   - Diagrama de fluxo de dados com boundaries de confiança

**Critério de sucesso**:
- Server funcional com ≥3 tools demonstráveis ✅
- Resource e prompt implementados ✅
- Documentação clara e completa ✅
- ADR segue template e justifica decisão ✅
- Threat model documenta ≥5 riscos com mitigações concretas ✅

**Avaliação** (rubrica de 4 pilares):

| Pilar | Peso | Critério |
|---|---|---|
| Técnico | 40% | Server funcional, código limpo, schemas corretos, threat model técnico |
| Consultivo | 30% | README + ADR — clareza da justificativa e apresentação como produto |
| Comportamental | 20% | Code review de um colega (outro server) |
| Prático | 10% | Demo ao vivo: server rodando em host real (Claude Desktop / OpenCode) |

**Nota mínima de aprovação**: 3.0

---

## Laboratórios

### Lab 1 — Primeiro MCP Server (4 h)
**Descrição**: Construir um server com FastMCP que expõe tools de consulta a um dataset (CSV). Conectar ao Claude Desktop ou OpenCode e demonstrar chamadas de tool.

**Entregáveis**:
- Código do server (`server.py`)
- Config JSON para o host
- Screenshot do LLM chamando uma tool

### Lab 2 — Multi-Server Composition (5 h)
**Descrição**: Construir dois servers MCP (arXiv + GitHub) e compô-los em um agente único. Demonstrar encadeamento de tools entre servers.

**Entregáveis**:
- Código dos dois servers
- Config JSON com ambos
- Demo de encadeamento (ex.: buscar paper no arXiv, criar issue no GitHub com resumo)

---

> **Mantido por**: Universidade Etho · Versão 1.0 · Julho 2026
> **Spec de referência**: MCP Specification 2025-11-25 (modelcontextprotocol.io)
