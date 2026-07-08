# Catálogo de Arquiteturas (12 Topologias)

> v1: catálogo consolidado das 12 topologias de referência para sistemas multi-agente. Cada topologia: **Estrutura** · **Quando usar** · **Quando evitar** · **Trade-offs** · **Referências**. Aprofundamento em `ETHAGT10`. Fichas individuais disponíveis em `01-single-agent.md` a `12-hybrid.md` neste mesmo diretório.

---

## 1. Single Agent
- **Estrutura**: 1 agente ReAct + tools.
- **Quando usar**: baseline; subtarefas únicas; protótipo.
- **Quando evitar**: especialização múltipla necessária; escala.
- **Trade-offs**: simples, barato, limitado.
- **Refs**: ETHAGT01.

## 2. Supervisor
- **Estrutura**: supervisor central + workers especializados, decisão via tool calls.
- **Quando usar**: sub-especializações claras; controle centralizado; ≤10 workers.
- **Quando evitar**: muitos workers; concorrência alta; trabalho criativo.
- **Trade-offs**: controle alto; supervisor é gargalo; custo médio.
- **Refs**: LangGraph *Supervisor* pattern; ETHAGT10.

## 3. Hierarchical
- **Estrutura**: árvore de supervisores (top → sub → workers).
- **Quando usar**: muitos workers (>10); sub-domínios separáveis; isolamento.
- **Quando evitar**: sistemas pequenos (não justifica complexidade).
- **Trade-offs**: escala bem; latência média-alta; complexidade de debug.
- **Refs**: MetaGPT; LangGraph `hierarchical_agent_teams`.

## 4. Blackboard
- **Estrutura**: espaço compartilhado onde agentes leem/escrevem incrementalmente.
- **Quando usar**: problema dinâmico; especialistas contribuem pouco a pouco; baixo acoplamento.
- **Quando evitar**: poucos agentes com papéis claros (mensagens diretas mais simples).
- **Trade-offs**: flexível; custo de tokens alto (todos veem tudo).
- **Refs**: ETHAGT09; clássico de IA.

## 5. Actor Model
- **Estrutura**: agentes = atores com estado privado + mailboxes; comunicação async.
- **Quando usar**: distribuído; alta concorrência; tolerância a falhas.
- **Quando evitar**: poucos agentes locais (overkill).
- **Trade-offs**: escala; isolamento; complexidade de raciocínio.
- **Refs**: Hewitt 1973; Akka; Erlang.

## 6. Pipeline
- **Estrutura**: agentes em sequência fixa, cada um uma etapa.
- **Quando usar**: etapas bem definidas; baixa variabilidade; latência previsível.
- **Quando evitar**: etapas dinâmicas; necessita branching.
- **Trade-offs**: simples; previsível; rígido.
- **Refs**: prompt chaining generalizado.

## 7. Event-Driven
- **Estrutura**: agentes reagem a eventos via mensageria (Kafka/NATS).
- **Quando usar**: desacoplamento; escala; workflows longos; HITL assíncrono.
- **Quando evitar**: tarefas síncronas simples; baixa latência crítica.
- **Trade-offs**: escala; resiliência; complexidade de debug.
- **Refs**: ETHAGT11.

## 8. Swarm
- **Estrutura**: agentes leves com handoffs; sem autoridade central.
- **Quando usar**: fluxo conversacional; especialistas claros; baixa latência.
- **Quando evitar**: workflow rígido; muitos agentes sobrepostos.
- **Trade-offs**: leve; flexível; coordenação difícil.
- **Refs**: OpenAI Swarm; ETHAGT09.

## 9. Tree of Agents
- **Estrutura**: árvore de exploração com backtracking (LATS aplicado).
- **Quando usar**: problemas difíceis com múltiplos caminhos; vale explorar.
- **Quando evitar**: problemas simples; custo sensível.
- **Trade-offs**: poderoso; caro; complexo.
- **Refs**: LATS (arXiv:2310.01757); ETHAGT04.

## 10. Recursive
- **Estrutura**: meta-agentes criam sub-agentes em recursão.
- **Quando usar**: problemas muito abertos onde estrutura emerge; meta-programming.
- **Quando evitar**: sem orçamento claro; sem validação de sub-agentes.
- **Trade-offs**: adaptativo; risco de explosão; difícil de governar.
- **Refs**: ETHAGT15; Voyager.

## 11. Agent Mesh
- **Estrutura**: peer-to-peer flat; todos falam com todos.
- **Quando usar**: poucos agentes altamente colaborativos; exploração.
- **Quando evitar**: muitos agentes (N² conexões); previsibilidade necessária.
- **Trade-offs**: flexibilidade máxima; custo e complexidade altos.
- **Refs**: raro em LLM; comum em sistemas distribuídos clássicos.

## 12. Hybrid
- **Estrutura**: composição realista das anteriores (ex.: supervisor + event-driven + pipeline).
- **Quando usar**: produção real (quase sempre híbrido).
- **Quando evitar**: protótipos (comece simples).
- **Trade-offs**: otimizado para o caso; complexidade máxima; ADR necessário.
- **Refs**: casos de produção (Anthropic, Block).

---

## Mapa de decisão rápido

```
Poucos agentes, papéis claros?
  ├─ Sim, etapas fixas ───────────► Pipeline
  ├─ Sim, decisão central ────────► Supervisor
  ├─ Sim, fluxo conversacional ───► Swarm
  └─ Sim, contribuição incremental ► Blackboard

Muitos agentes?
  ├─ Sub-domínios separáveis ─────► Hierarchical
  ├─ Distribuído/concorrente ─────► Actor Model / Event-Driven
  └─ Exploratório ────────────────► Tree of Agents

Problema muito aberto?
  └─ Estrutura emerge ────────────► Recursive / Mesh

Produção real?
  └─ Híbrido (com ADR)
```

## Princípios transversais

1. **Comece simples** (supervisor ou pipeline).
2. **Evolua com base em evidência** (gargalo identificado).
3. **ADR sempre** para mudança de topologia.
4. **Topologia não é estática** — sistemas maduros evoluem.

## Próximos passos

Sprint futuro: dividir cada topologia em arquivo próprio (`<nome>.md`) com exemplo runnable + métricas empíricas + anti-patterns detalhados.
