---
password: Etho-Prof-2026
---
# ETHAGT10 — Gabarito

> Restrito a mentores. Cada resposta justificada com referência à apostila.

## Múltipla escolha

1. **b)** — Na topologia Supervisor (LangGraph), o supervisor é um roteador com tool calls que decide qual worker acionar com base na tarefa (Capítulo 2 — Supervisor e Hierarchical).

2. **b)** — Orchestrator-Workers ou Hierarchical é mais adequada quando as subtarefas são dinâmicas e não podem ser pré-determinadas, pois o orquestrador LLM as define em runtime (Capítulo 2 e 4).

3. **b)** — No Swarm (OpenAI), a coordenação é descentralizada via handoffs entre agentes leves que transferem controle e contexto sem um supervisor central (Capítulo 3 — Swarm e handoffs).

4. **b)** — Hierarchical é melhor que flat quando há múltiplos níveis de especialização que justificam uma árvore (supervisor → workers → sub-workers). Com poucos agentes, flat é mais simples e suficiente (Capítulo 2.3).

## Verdadeiro ou Falso (justificado)

1. **Falso.** Mesh (peer-to-peer flat) escala em termos de N agentes, mas a complexidade de coordenação cresce quadraticamente (O(N²) interações). Não é sempre a mais escalável — para alta escala, hierarchical ou event-driven costumam ser melhores (Capítulo 6 e exercícios do syllabus).

2. **Verdadeiro.** Recursive (meta-agents que criam agentes) adiciona complexidade, risco de recursão descontrolada e custo. Sem necessidade genuína de auto-geração, é over-engineering (Capítulo 6.2 — Recursive).

3. **Verdadeiro.** O supervisor é um ponto central de decisão; se todas as tarefas passam por ele, ele se torna bottleneck de latência e custo. Hierarchical mitiga dividindo em sub-supervisores (Capítulo 2.4 — Casos de falha).

4. **Verdadeiro.** A escolha de topologia tem impacto arquitetural profundo (custo, latência, flexibilidade, complexidade). Um ADR documenta o contexto, a decisão e a justificativa para futura referência (Capítulo 7 — Escolha e ADR).

## Código curto

1. **ADR de topologia:**
```markdown
# ADR-001: Topologia Multi-Agente

## Contexto
[Descrição do problema e requisitos]

## Decisão
Escolhemos [topologia X].

## Justificativa
[Motivos: consistência, latência, custo, flexibilidade]

## Trade-offs
[O que ganhamos e o que perdemos vs. alternativas]
```
Referência: Capítulo 7 (ADR de topologia).

2. **Supervisor com 2 workers:**
```python
def supervisor(task):
    task_type = classify(task)
    if task_type == "type_a":
        return worker_a(task)
    else:
        return worker_b(task)
```
Referência: Capítulo 2 (Supervisor pattern).

3. **Swarm com handoff:**
```python
def agent_general(query):
    if is_specialist_needed(query):
        return handoff(agent_specialist, context=query)
    return respond(query)
```
Referência: Capítulo 3 (Swarm e handoffs).

## Análise de trade-off

1. **Hierarchical vs. Swarm (revisão de PR):** Hierarchical com supervisor que delega a especialistas (frontend, backend, security) é preferível — o supervisor orquestra, cada especialista revisa sua área, e o supervisor sintetiza. Swarm seria menos controlável para uma tarefa que requer cobertura estruturada (Capítulo 2 e 3).

2. **Supervisor vs. Blackboard:** Supervisor é melhor quando o fluxo é estruturado e sequencial (decisão centralizada). Blackboard é melhor quando especialistas contribuem incrementalmente para um problema dinâmico sem ordem fixa (Capítulo 3 vs. 2).

3. **Topologias por cenário:**
   - **Atendimento (5 departamentos):** Supervisor com routing por departamento.
   - **Pesquisa científica colaborativa:** Blackboard ou Hierarchical com especialistas.
   - **Pipeline ETL fixo:** Pipeline fixo (workflow, não multi-agente).
   Referência: Capítulos 1-7.

## Debug / diagnóstico

1. **Diagnóstico:** O roteamento do supervisor nunca classifica tarefas para aquele worker — pode ser bug no classificador, no prompt do supervisor, ou o worker não está registrado. **Correção:** revisar o prompt/rota do supervisor e adicionar logs de decisão de routing (Capítulo 2.4).

2. **Diagnóstico:** O handoff não transfere contexto adequadamente — cada agente reinicia sem histórico. **Correção:** garantir que o handoff inclua todo o contexto acumulado (mensagens anteriores, estado) na transferência (Capítulo 3.2 — Limites).
