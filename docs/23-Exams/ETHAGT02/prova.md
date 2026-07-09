---
password: Etho-Prof-2026
---
# ETHAGT02 — Prova do Módulo: Tool Calling e Agent-Computer Interface (ACI)

> Universidade Etho · Versão 1.0 · Julho 2026
> Duração: ~60 min · 10 questões · closed book · Pilar Técnico (40%)

Esta prova avalia o design de ferramentas para agentes: o mecanismo de tool calling, os princípios de ACI, engenharia de schemas, ferramentas perigosas com HITL e avaliação via workbench.

---

## Parte 1 — Conceitos (Q1-4)

**1. (Múltipla escolha)** Qual é a principal vantagem do function calling nativo sobre o modo prompt-based (parsing de texto)?
- (a) É mais barato em tokens
- (b) Elimina o problema de parsing, pois a saída é estruturada
- (c) Permite usar modelos menores
- (d) Reduz a latência

**2. (V/F justificado)** "O custo de uma ferramenta no catálogo se limita à chamada quando ela é invocada."

**3. (Múltipla escolha)** Segundo a matriz de risco de Anthropic, qual quadrante exige **obrigatoriamente** Human-in-the-Loop (HITL)?
- (a) Baixo impacto + reversível
- (b) Alto impacto + reversível
- (c) Irreversível + alto impacto
- (d) Baixo impacto + irreversível

**4. (V/F justificado)** "Se o modelo usa uma ferramenta errada ou passa argumentos errados, a reação correta do engenheiro de ACI é culpar o modelo e tentar outro LLM."

---

## Parte 2 — Aplicação e trade-off (Q5-8)

**5. (Análise de schema)** Avalie o seguinte schema de tool e liste 3 anti-patterns:
```json
{
  "name": "search",
  "description": "Consulta pedidos.",
  "parameters": {
    "type": "object",
    "properties": { "q": {"type": "string"} }
  }
}
```

**6. (Trade-off)** Você tem 3 ferramentas: `search_orders_by_id`, `search_orders_by_date`, `search_orders_by_customer`. Elas compartilham ~80% da lógica. O que fazer e por quê?

**7. (Debug de tool)** Um agente de suporte chama a tool `edit_file(path, content)` e escreve no arquivo errado. O agente interpretou `src/app.py` como path relativo ao diretório que *achava* ser o atual. Qual é a correção canônica (caso real da Anthropic)?

**8. (V/F justificado)** "Uma ferramenta de leitura pura (ex.: `get_order`) precisa obrigatoriamente de idempotency key."

---

## Parte 3 — Projeto curto (Q9-10)

**9. (Projeto curto)** Escreva a descrição ACI de qualidade para uma tool `get_order_status` que atualmente tem a descrição vaga `"Consulta pedidos."`. Siga: (a) o que faz, (b) quando usar, (c) quando NÃO usar, (d) o que retorna.

**10. (Projeto curto)** Escreva o esqueleto de uma tool `charge_customer` idempotente, com `idempotency_key`, tratamento de erro que devolve uma mensagem útil e `hint` acionável ao modelo no caso de `InsufficientFunds`.

---

## Critérios de correção (resumo)

| Conceito | Questões | Peso |
|---|---|---|
| Tool calling & mecanismo | 1, 2 | 20% |
| ACI & princípios de design | 4, 5, 9 | 25% |
| Engenharia de tools & erros | 6, 7, 8 | 25% |
| HITL & risco | 3, 10 | 20% |
| Idempotência | 10 | 10% |

**Conversão**: cada questão vale 10 pts; total 100 pts. Nota 1-5.
- 90+ pts: 5,0
- 75-89: 4,0
- 60-74: 3,0 (mínimo aprovação)
- <60: reprovação.

Gabarito comentado em [`gabarito.md`](gabarito.md).
