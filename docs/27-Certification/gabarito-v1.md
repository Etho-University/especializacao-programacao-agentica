# Exame V1 — Gabarito (restrito a avaliadores)

> Use em conjunto com [`exame-v1.md`](exame-v1.md). Para questões abertas, critérios de correção.

## Múltipla escolha

| Q | Resposta | Justificativa |
|---|---|---|
| 1 | **(b)** | Distinção canônica Anthropic: workflow = código predefinido; agente = LLM dirige. |
| 2 | **(b)** | Augmented LLM = LLM + retrieval + tools + memory (Anthropic). |
| 3 | **(b)** | ReAct: Thought → Action → Observation em loop (Yao et al.). |
| 4 | **(b)** | ToT explora múltiplos caminhos em árvore com avaliação e backtracking; CoT é linear único. |
| 5 | **(b)** | ACI :: HCI; invista na interface das tools tanto quanto na humana. |
| 6 | **(b)** | Host, client, server (Anthropic MCP). |
| 7 | **(c)** | Streamable HTTP substituiu HTTP+SSE em março/2025. |
| 8 | **(b)** | CRAG avalia relevância; se irrelevante/ambíguo, busca web. |
| 9 | **(c)** | GraphRAG brilha em multi-hop e panorâmicas (global search). |
| 10 | **(b)** | Checkpointer persiste estado; permite interromper e retomar. |
| 11 | **(b)** | Adiciona nível quando >10 workers diretos ou sub-domínios separáveis. |
| 12 | **(b)** | Saga = transações distribuídas com compensação. |
| 13 | **(b)** | Vieses: position, length, self-preference, authority. |
| 14 | **(b)** | Indireto: injeção em dados recuperados. |
| 15 | **(b)** | Meta-governor aplica policies e veto sobre mudanças propostas. |

## Verdadeiro/Falso justificado

| Q | V/F | Justificativa esperada (mínimo) |
|---|---|---|
| 16 | **Falso** | Maioria se resolve com workflow ou chamada única; agente adiciona custo/risco. Só quando flexibilidade é necessária. |
| 17 | **Falso** | ReAct reduz (grounding por passo) mas não elimina; alucinação em ação persiste. |
| 18 | **Falso** | MCP **padroniza** a interface; usa tool calling nativo do provedor. |
| 19 | **Verdadeiro** | Princípio Anthropic: comece simples; só complexidade com evidência. |
| 20 | **Falso** | Modelos maiores são mais capazes — inclusive de seguir instruções maliciosas complexas. |
| 21 | **Falso** | Em perguntas únicas ou dados voláteis, hit rate baixo; custo sem benefício. |
| 22 | **Falso** | Podem polarizar, echo chamber, divergir. |
| 23 | **Verdadeiro** | Reflexion acumula reflexões verbais de tentativas falhas; usa nas seguintes. |

## Análise de trade-off (critérios)

| Q | Critério de nota 5 |
|---|---|
| 24 | Workflow (routing) — categorias claras; justifica com ≥3 critérios (previsibilidade, custo, debug). |
| 25 | Subtarefas **dinâmicas** (dependem da issue); orchestrator decide; parallelization é predefinido. |
| 26 | Vector para similaridade semântica (FAQ); KG para relações multi-hop; **híbrido** quando perfil misto. |
| 27 | Routing por complexidade: 80% fáceis → Haiku; 20% difíceis → Sonnet. Economia 5-10×. |
| 28 | Actor: isolamento, concorrência, distribuído; Blackboard: desacoplado, flexível, mas alto custo tokens. |

## Análise de arquitetura (rubrica)

- **Q29**: nota 5 = identifica topologia correta, ≥2 pontos únicos de falha, melhoria acionável.
- **Q30**: nota 5 = localiza loop, causa raiz, **2** correções distintas (uma prompt, uma código).

## Práticas (rubrica)

- **Q31**: nota 5 = identifica bug em 3/3 + correção correta + explica.
- **Q32**: nota 5 = schema Pydantic + descrição rica (exemplos, edge cases) + HITL onde perigoso.
- **Q33**: nota 5 = prompt com critério de parada explícito + trata edge cases.
- **Q34**: nota 5 = pipeline com golden cases + LLM-as-judge calibrado + métricas 4 dimensões.
- **Q35**: nota 5 = ADR com contexto, decisão, alternativas, consequências — formato correto.

## Conversão para nota 1-5

- ≥90% acertos: 5,0
- 80-89%: 4,5
- 70-79%: 4,0
- 60-69%: 3,0 (abaixo do mínimo para certificação)
- <60%: reprova

**Nota mínima para certificação**: 4,0 (70% acertos).
