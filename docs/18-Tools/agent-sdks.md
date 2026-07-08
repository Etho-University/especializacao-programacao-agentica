# Agent SDKs

| Framework | Licença | Modelo mental | Controle | Prod-ready |
|---|---|---|---|---|
| **LangGraph** | MIT | estado + grafo (nodes/edges) | alto (caixa branca) | sim |
| **OpenAI Agents SDK** | MIT | minimalista, agents + handoffs | médio | sim |
| **CrewAI** | MIT | role-based (crew com papéis) | médio | sim |
| **AutoGen** | MIT (Microsoft) | conversação multi-agente | médio | sim |
| **Agno** | MIT | performance-first | médio | sim |
| **PydanticAI** | MIT | typed, Pydantic-first | alto | sim |
| **Semantic Kernel** | MIT (Microsoft) | enterprise, plugins | médio | sim |
| **Google ADK** | Apache | Google ecosystem | médio | sim |
| **OpenAI Swarm** | MIT (experimental) | handoffs leves | baixo | experimental |
| **Strands** (AWS) | Apache | AWS ecosystem | médio | sim |

## Comparativo profundo

### LangGraph
- **Força**: explícito (grafo de estados), observável, persistente (checkpointer).
- **Quando escolher**: produção, sistemas complexos, quer controle total.
- **Quando evitar**: protótipos rápidos simples (overkill).

### OpenAI Agents SDK
- **Força**: minimalista, integração OpenAI nativa.
- **Quando escolher**: ecossistema OpenAI, simplicidade.
- **Quando evitar**: multi-provedor necessário; controle granular.

### CrewAI
- **Força**: role-based é intuitivo (designa papéis, objetivos, tools).
- **Quando escolher**: times não-técnicos concebem (papéis claros).
- **Quando evitar**: sistemas complexos com estado intricado.

### AutoGen
- **Força**: conversação multi-agente madura, GroupChat.
- **Quando escolher**: multi-agent conversacional.
- **Quando evitar**: workflows estruturados.

### PydanticAI
- **Força**: tipagem forte (Pydantic), structured outputs.
- **Quando escolher**: types importam, schemas complexos.
- **Quando evitar**: protótipo rápido sem tipo.

### Semantic Kernel / Google ADK / Strands
- **Força**: integração enterprise (Microsoft/Google/AWS).
- **Quando escolher**: já no ecossistema.
- **Quando evitar**: vendor lock-in não desejado.

## Princípio

Em produção, prefira frameworks **explícitos** (LangGraph, PydanticAI) sobre **mágicos** — debug é mais fácil. Use frameworks "mágicos" para protótipos.

## Referências

- Repos e docs oficiais de cada.
