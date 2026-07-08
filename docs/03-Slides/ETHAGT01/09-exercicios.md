# ETHAGT01 — Exercícios

> Exercícios para aula e para casa.
> Organizados por tipo: em aula, individual, em duplas, projeto.

---

## Exercícios em Aula

### E1 — Workflow ou Agente? (Votação Rápida)
**Slide**: 28
**Tempo**: 2 min
**Formato**: Individual, votação de mão levantada

**Enunciado**: Para cada cenário abaixo, vote: Workflow (W) ou Agente (A)?

1. Traduzir documentação técnica EN→PT
2. Resolver issue de GitHub arbitrário
3. Classificar ticket de suporte por tipo
4. Pesquisar e sintetizar tema novo
5. Revisar código em busca de bugs
6. Negociar contrato com fornecedor

**Gabarito**:
1. W (prompt chaining: traduzir → revisar → ajustar termos)
2. A (passos imprevisíveis, depende da issue)
3. W (routing puro)
4. A (busca iterativa, queries adaptativas)
5. W (parallelization/voting — múltiplos revisores)
6. A + HITL (alta stakes, humano aprova cada step)

---

### E2 — O Que Acontece Se...? (Discussão em Duplas)
**Slide**: 22
**Tempo**: 2 min
**Formato**: Duplas, 2 min discussão + 1 min compartilhar

**Enunciado**: Após a demo do ReAct em 50 linhas, discutam em duplas:

1. O que acontece se a tool retornar erro? Quem trata?
2. E se o modelo não chamar tool nenhuma?
3. E se o modelo chamar uma tool que não existe?

**Gabarito**:
1. Se não houver try/except, a exceção quebra o loop. Solução: capturar erro e retornar como Observation estruturada (`{"error": "...", "suggestion": "..."}`).
2. O código entra no `if not msg.tool_calls` e imprime a resposta final — mesmo que não seja correta.
3. `calculator(**args)` falha com KeyError. Sem validação de tool name, o loop quebra.

---

### E3 — Debug de Trace Quebrado (Duplas)
**Slide**: 47
**Tempo**: 3 min
**Formato**: Duplas, 2 min discussão + 1 min compartilhar

**Enunciado**: Analise o seguinte trace de um agente ReAct:

```
[STEP 0] Thought: "Vou buscar o preço do produto X"
         Action: search_price("Produto X")
         Observation: "Produto X: R$ 99,90"

[STEP 1] Thought: "Vou buscar o preço do produto X"
         Action: search_price("Produto X")
         Observation: "Produto X: R$ 99,90"

[STEP 2] Thought: "Vou buscar o preço do produto X"
         Action: search_price("Produto X")
         Observation: "Produto X: R$ 99,90"

[STEP 3] Thought: "Vou buscar o preço do produto X"
         Action: search_price("Produto X")
         Observation: "Produto X: R$ 99,90"

[STEP 4] Thought: "Vou buscar o preço do produto X"
         Action: search_price("Produto X")
         Observation: "Produto X: R$ 99,90"

[STEP 5] max_steps reached. Abortando.
```

**Perguntas**:
1. Identifique onde o loop acontece e por quê.
2. Proponha 2 correções diferentes.

**Gabarito**:
- **Problema**: O agente repete a mesma action sem processar a Observation. Possíveis causas: (a) prompt não instrui a usar informações já obtidas; (b) contexto não inclui observations anteriores; (c) modelo fraco.
- **Correção 1 (prompt)**: Adicionar ao system prompt: "Antes de buscar, verifique se você já tem a informação nas observações anteriores."
- **Correção 2 (código)**: Adicionar detecção de repetição: se `action == action_anterior` por 3x, forçar resposta final.
- **Correção 3 (context)**: Garantir que `messages` inclui todas as observations anteriores.

---

## Exercícios Individuais (para casa)

### E4 — Defina Workflow vs Agente
**Tempo estimado**: 10 min
**Formato**: Individual, escrito

**Enunciado**: Em suas palavras, defina a diferença entre workflow e agente em 2-3 frases. Use um exemplo de cada.

**Critério de avaliação**:
- Define workflow como "passos predefinidos via código" ✅
- Define agente como "modelo controla o fluxo" ✅
- Exemplo de workflow é realista ✅
- Exemplo de agente é realista ✅

---

### E5 — Descrição de Tool com ACI
**Tempo estimado**: 15 min
**Formato**: Individual, código

**Enunciado**: Escreva a descrição de uma tool seguindo princípios ACI. A tool deve:
- Ter nome descritivo
- Ter descrição clara (como docstring para júnior)
- Ter parâmetros com tipos e descrições
- Incluir exemplo de uso
- Aplicar poka-yoke (dificultar erro)

**Exemplo de resposta**:
```python
{
    "type": "function",
    "function": {
        "name": "search_product",
        "description": "Busca um produto pelo nome exato ou parcial no catálogo. Retorna preço, disponibilidade e SKU. Use esta tool quando o usuário perguntar sobre preço, estoque ou detalhes de um produto específico. NÃO use para listar todos os produtos — use list_products para isso.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Nome do produto ou parte do nome. Exemplo: 'iPhone 15' ou 'notebook Dell'"
                },
                "category": {
                    "type": "string",
                    "enum": ["electronics", "clothing", "food", "books"],
                    "description": "Categoria para filtrar. Opcional — omita se não souber a categoria."
                }
            },
            "required": ["query"]
        }
    }
}
```

**Poka-yokes aplicados**:
- `category` é enum (não pode errar)
- Descrição diz quando USAR e quando NÃO USAR
- Exemplo de query incluído na descrição do parâmetro

---

### E6 — Verdadeiro/Falso Justificado
**Tempo estimado**: 10 min
**Formato**: Individual, escrito

**Enunciado**: Responda V ou F e justifique em 2-3 frases:

1. "Toda aplicação de LLM deveria ser um agente."
2. "LangGraph é sempre melhor que Python puro porque tem menos código."
3. "O Thought no ReAct é opcional — o modelo pode ir direto para Action."
4. "Se a context window for grande o suficiente, não precisamos de persistent memory."
5. "max_steps é uma otimização, não uma necessidade."

**Gabarito**:
1. **F** — A Anthropic recomenda começar simples. 90% dos casos = single LLM call + retrieval. Agente só quando flexibilidade é necessária.
2. **F** — Depende do contexto. Em produção com auditoria, Python puro dá mais controle e transparência. Menos código ≠ melhor.
3. **F** — O Thought força reasoning explícito. Sem ele, o modelo pula para ação sem planejar, aumentando erros.
4. **F** — Context window maior reduz summarization mas não resolve: custo cresce, qualidade cai (lost in the middle), e memória persistente é entre sessões.
5. **F** — max_steps é guardrail de segurança. Sem ele, o agente pode entrar em loop infinito e gastar orçamento ilimitado.

---

### E7 — Trade-offs de Custo
**Tempo estimado**: 15 min
**Formato**: Individual, cálculo

**Enunciado**: Liste 3 trade-offs de custo/latência ao adicionar retrieval em loop a um agente. Para cada um, dê um número concreto.

**Exemplo de resposta**:

1. **Custo por step**: Cada retrieval adiciona ~500 tokens de contexto. A $0.15/1M tokens (gpt-4o-mini input), 10 steps = $0.00075 extra. Em 10k execuções/dia = $7.50/dia extra = $225/mês extra.
2. **Latência por step**: Cada retrieval adiciona ~200ms (query + embedding + search). 10 steps com retrieval = +2s de latência total. Se latência alvo é <5s, retrieval consome 40% do orçamento.
3. **Context growth**: Cada retrieval adiciona resultado ao contexto. Step 1: 2k tokens. Step 10: 7k tokens (acumulando). Custo cresce quadraticamente, não linearmente.

---

## Projeto do Módulo

### P1 — Research Assistant em 3 Versões
**Prazo**: 2 semanas
**Formato**: Individual
**Carga**: ~8h

**Descrição**: Implementar um agente "research assistant" que, dada uma pergunta factual, decide entre:
- (a) responder direto
- (b) recuperar de uma base local (vector store)
- (c) usar uma tool de busca (simulada ou real)

**Entrega**: 3 versões do mesmo agente:
1. **Python puro** + OpenAI/Anthropic SDK
2. **LangGraph**
3. Um terceiro framework à escolha (OpenAI Agents SDK, CrewAI, PydanticAI)

**Entregáveis**:
- Repositório Git com as 3 versões
- README comparativo (mínimo 3 critérios: controle, transparência, esforço)
- Traces de execução mostrando o loop ReAct em ação
- Pelo menos 3 perguntas-teste executadas em cada versão

**Critério de sucesso**:
- Agente funcional nas 3 versões
- Comparação justifica escolha com ≥3 critérios
- Traces demonstram o loop
- README é claro e estruturado

**Avaliação** (rubrica de 4 pilares):

| Pilar | Peso | Critério |
|---|---|---|
| Técnico | 40% | Código funcional, traces, qualidade da implementação |
| Consultivo | 30% | README comparativo — clareza da justificativa |
| Comportamental | 20% | Code review de um colega |
| Prático | 10% | Demo ao vivo: agente respondendo a 3 perguntas |

**Nota mínima de aprovação**: 3.0
