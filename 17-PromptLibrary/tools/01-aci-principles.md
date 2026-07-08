# tools/01-aci-principles.md

## objetivo
Prompt de referência para descrever ferramentas (tools) seguindo os princípios ACI (Agent-Computer Interface): nome claro, assinatura precisa, descrição do comportamento e restrições.

## variáveis
- `{{tool_name}}` — nome da ferramenta
- `{{parameters}}` — descrição dos parâmetros (nome, tipo, obrigatório, descrição)
- `{{returns}}` — descrição do retorno (tipo, estrutura)
- `{{side_effects}}` — efeitos colaterais (se houver: mutate DB, send email, etc.)

## template

```
When defining a tool for an agent, use the ACI format below.

Tool Name: {{tool_name}}

Parameters:
{{parameters}}

Returns:
{{returns}}

Side Effects:
{{side_effects}}

ACI Principles applied:
1. **Name**: action-oriented verb + noun (e.g., search_users, send_invoice)
2. **Parameters**: typed, with clear defaults and validation constraints
3. **Returns**: structured and consistent across calls
4. **Error handling**: documented failure modes
5. **Cost**: approximate latency and token cost if significant

Example tool definition:

Tool: get_weather
Description: Returns current weather for a given city.
Parameters:
  - city (string, required): City name, e.g. "São Paulo"
  - units (string, optional): "celsius" or "fahrenheit", default "celsius"
Returns: { "temperature": float, "humidity": int, "condition": string }
Errors: 404 if city not found; 429 if rate limited
```

## exemplo de uso
Usado antes de gerar o JSON de tool definitions para OpenAI function calling ou Anthropic tool use, garantindo que cada ferramenta siga o padrão ACI.

## trade-offs
- Definições muito detalhadas consomem tokens no system prompt
- Parâmetros opcionais demais geram chamadas ambíguas
- ACI promove clareza, mas não substitui testes com o agente (golden trajectories)

## variações
- **ACI with examples**: incluir 1-2 exemplos de chamada bem-sucedida para cada tool
- **ACI with rejection policy**: explicitar em que casos a tool deve retornar erro (e não ser chamada)
- **Grouped ACI**: agrupar tools relacionadas em um bloco para reduzir repetição de contexto
