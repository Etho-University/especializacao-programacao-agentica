# Exame de Certificação — Versão 1 (modelo)

> Especialização em Programação Agêntica · Universidade Etho
> Duração: 3 horas · Nota mínima: 4,0

---

## PARTE 1 — Conceitual (30 questões, 90 min)

### Múltipla escolha (15 × 2 min)

**1.** Segundo Anthropic (*Building Effective Agents*), a distinção canônica entre workflow e agente é:
- (a) Workflow usa tools; agente não.
- (b) Workflow orquestra LLMs por código predefinido; agente deixa o LLM dirigir o processo.
- (c) Workflow é mais barato; agente é mais caro.
- (d) Workflow é síncrono; agente é assíncrono.

**2.** O Augmented LLM (bloco fundamental de Anthropic) é:
- (a) LLM + fine-tuning.
- (b) LLM + retrieval + tools + memory.
- (c) LLM com contexto longo.
- (d) LLM com reasoning nativo.

**3.** ReAct (Yao et al.) intercala qual sequência de passos?
- (a) Plan → Execute → Observe
- (b) Thought → Action → Observation
- (c) Query → Retrieve → Generate
- (d) Generate → Evaluate → Refine

**4.** Em Tree of Thoughts (ToT), o que diferencia de CoT?
- (a) ToT usa mais tokens.
- (b) ToT explora múltiplos caminhos em árvore com avaliação e backtracking.
- (c) ToT é mais rápido.
- (d) ToT só funciona com modelos reasoning.

**5.** O princípio ACI de Anthropic defende que:
- (a) Tools devem ter schema JSON.
- (b) A descrição das tools merece tanto esforço quanto HCI.
- (c) Tools devem ser idempotentes.
- (d) Tools devem ter HITL.

**6.** MCP (Model Context Protocol) define três papéis:
- (a) Cliente, servidor, provedor.
- (b) Host, client, server.
- (c) Agente, tool, recurso.
- (d) Producer, consumer, broker.

**7.** Qual transporte MCP substituiu HTTP+SSE em março/2025?
- (a) gRPC.
- (b) WebSocket.
- (c) Streamable HTTP.
- (d) stdio remoto.

**8.** Corrective RAG (CRAG) decide buscar na web quando:
- (a) Sempre.
- (b) Quando os docs recuperados são avaliados como irrelevantes/ambíguos.
- (c) Quando o modelo é pequeno.
- (d) Quando há cache miss.

**9.** GraphRAG (Microsoft) supera vector RAG principalmente em:
- (a) Latência.
- (b) Custo.
- (c) Perguntas multi-hop e panorâmicas.
- (d) Simplicidade.

**10.** Checkpointer (LangGraph) permite:
- (a) Cache de prompts.
- (b) Persistência de estado; interromper e retomar execução.
- (c) Compartilhar memória entre agentes.
- (d) Rate limiting.

**11.** Em topologia hierarchical, quando adicionar um nível?
- (a) Nunca.
- (b) Quando o supervisor tem >10 workers diretos ou há sub-domínios separáveis.
- (c) Sempre que possível.
- (d) Quando custo é alto.

**12.** Saga pattern é usado para:
- (a) Paralelizar chamadas LLM.
- (b) Transações distribuídas com compensação.
- (c) Cache de resultados.
- (d) Observabilidade.

**13.** LLM-as-judge tem viés de:
- (a) Apenas position bias.
- (b) Position, length, self-preference, authority.
- (c) Não tem vieses.
- (d) Apenas viés de idioma.

**14.** Prompt injection indireto ocorre quando:
- (a) Usuário digita a injeção.
- (b) Injeção está em dados recuperados (RAG, web, MCP resources).
- (c) Modelo é grande demais.
- (d) Sem HITL.

**15.** Meta-governor em sistemas auto-evolutivos serve para:
- (a) Otimizar prompts.
- (b) Aplicar policies e veto sobre mudanças propostas por meta-agentes.
- (c) Aumentar contexto.
- (d) Substituir HITL.

### Verdadeiro/Falso justificado (8 × 3 min)

**16.** V/F: "Toda aplicação de LLM deveria ser implementada como agente autônomo."

**17.** V/F: "ReAct elimina completamente a alucinação."

**18.** V/F: "MCP substitui o tool calling nativo do LLM."

**19.** V/F: "Em produção, é melhor começar com workflow e só ir para agente quando necessário."

**20.** V/F: "Modelos maiores são sempre mais seguros contra prompt injection."

**21.** V/F: "Cache semântico é sempre benéfico."

**22.** V/F: "Sociedades de agentes sempre convergem para consenso."

**23.** V/F: "Reflexion usa memória cross-tentativa para aprender com falhas."

### Análise de trade-off (5 × 4 min)

**24.** Para um sistema de classificação de tickets com 4 categorias bem definidas, defenda workflow vs agente.

**25.** Para um coding agent que edita múltiplos arquivos, por que orchestrator-workers sobre parallelization?

**26.** Para memória de agente pessoal de longo prazo, vector DB vs knowledge graph: qual e quando?

**27.** Para 80% de perguntas fáceis + 20% difíceis, qual estratégia de model routing?

**28.** Para um sistema multi-agente distribuído, actor model vs blackboard: trade-offs?

### Análise de arquitetura (2 × 8 min)

**29.** Dado o diagrama (anexo A), identifique: (a) topologia, (b) pontos únicos de falha, (c) uma melhoria.

**30.** Dado um trace (anexo B) onde o agente entrou em loop: (a) onde, (b) por quê, (c) proponha 2 correções.

---

## PARTE 2 — Prática (10 questões, 90 min, com código/repo)

**31. Debug de agente (3 × 8 min)**: dado trace com problema (3 traces fornecidos), identificar e escrever correção.

**32. Design de tool/ACI (2 × 6 min)**: escrever schema + descrição para: (a) `transfer_money`, (b) `search_documents`.

**33. Design de prompt (2 × 6 min)**: escrever prompt para: (a) evaluator-optimizer de tradução literária, (b) planner multi-step.

**34. Eval design (2 × 8 min)**: dado cenário (assistente de suporte), projetar: (a) pipeline de eval, (b) golden cases.

**35. ADR (1 × 15 min)**: dado requisito ("sistema deve sobreviver a quedas de LLM provider"), escrever ADR.

---

## Critérios de correção

| Conceito avaliado | Questões |
|---|---|
| Fundamentos (Augmented LLM, ReAct, workflow vs agente) | 1, 2, 3, 16, 17, 19 |
| Reasoning patterns | 4, 23 |
| ACI e tools | 5, 32 |
| MCP | 6, 7, 18 |
| RAG e memória | 8, 9, 10, 26 |
| Topologias multi-agente | 11, 28, 29 |
| Orquestração | 12 |
| Avaliação | 13, 34 |
| Segurança | 14, 20 |
| Meta-agentes e fronteira | 15, 22 |
| Otimização | 21, 27 |
| Prática | 30, 31, 33, 35 |

Gabarito em [`gabarito-v1.md`](gabarito-v1.md).
