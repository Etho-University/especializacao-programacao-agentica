# Catálogo de Padrões de Agentes (v1)

> 23 padrões de projeto para sistemas de agentes LLM. Inspirado no espírito de *Design Patterns* (GoF), adaptado para Agentic AI. v1: catálogo consolidado. Fichas individuais disponíveis em `01-supervisor.md` a `23-tool-agent.md` neste mesmo diretório.
> Cada padrão segue: **Intenção** · **Estrutura** · **Quando usar** · **Anti-patterns** · **Custo** · **Referências**.

---

## Categoria A — Padrões de Orquestração (delegação e roteamento)

### 1. Supervisor
- **Intenção**: orquestrar workers especializados atuando como roteador via tool calls; o supervisor decide qual worker chamar a cada passo.
- **Estrutura**: `supervisor` LLM com tools = `call_worker(name, task)`. Workers são LLMs especializados.
- **Quando usar**: tarefas com sub-especializações claras; quer controle centralizado.
- **Anti-patterns**: supervisor gargalo (todos os pedidos passam por ele); workers redundantes.
- **Custo**: 1 chamada supervisor + 1 worker por passo.
- **Refs**: LangGraph *Multi-Agent Supervisor* pattern.

### 2. Orchestrator
- **Intenção**: decompor dinamicamente a tarefa em subtarefas e delegar a workers, sintetizando resultados.
- **Estrutura**: `orchestrator` gera plano → `workers` executam → `synthesizer` integra.
- **Quando usar**: subtarefas **não são previsíveis**; problema aberto.
- **Anti-patterns**: workers duplicando trabalho; synthesis só concatenando.
- **Custo**: N+2 chamadas (orchestrator + N workers + synth).
- **Refs**: Anthropic *Orchestrator-Workers* workflow.

### 3. Coordinator
- **Intenção**: mediar comunicação entre agentes sem decidir o conteúdo; gerencia sessão, handoffs, estado compartilhado.
- **Estrutura**: `coordinator` roteia mensagens, mantém state, não gera conteúdo.
- **Quando usar**: muitos agentes precisam coordenar; quer desacoplar remetente/destinatário.
- **Anti-patterns**: coordinator virando supervisor (decidindo conteúdo).
- **Custo**: baixo (gerenciamento, não geração).
- **Refs**: padrões de middleware; actor model.

### 4. Router
- **Intenção**: classificar input e direcionar para handler especializado.
- **Estrutura**: `classifier` → ramo A/B/C.
- **Quando usar**: categorias distintas com tratamentos próprios.
- **Anti-patterns**: categorias ambíguas; sem fallback.
- **Custo**: 1 classificação + 1 handler.
- **Refs**: Anthropic *Routing* workflow.

---

## Categoria B — Padrões de Planejamento e Execução

### 5. Planner
- **Intenção**: decompor objetivo em sequência de passos executáveis.
- **Estrutura**: `planner(goal) → [step1, step2, ...]`. Pode ser replanner se necessário.
- **Quando usar**: problema decompõe-se naturalmente; vale planejar antes.
- **Anti-patterns**: plano rígido sem re-planejamento; plano muito granular.
- **Custo**: 1 chamada (barato).
- **Refs**: Plan-and-Solve (arXiv:2305.04091); LangGraph `plan-and-execute`.

### 6. Executor
- **Intenção**: operar passos do plano, chamando tools conforme necessário.
- **Estrutura**: loop sobre passos; cada passo vira chamada LLM/tool.
- **Quando usar**: sempre (parceiro do Planner).
- **Anti-patterns**: executor que re-planeja implicitamente (vira agente).
- **Custo**: N chamadas (uma por passo).
- **Refs**: idem Planner.

### 7. Scheduler
- **Intenção**: agendar e priorizar tarefas em sistemas com múltiplas demandas.
- **Estrutura**: fila de tarefas com prioridade; scheduler decide ordem.
- **Quando usar**: muitos pedidos concorrentes; ordem importa.
- **Anti-patterns**: FIFO cego (sem prioridade); starvation.
- **Custo**: baixo (decisão, não execução).
- **Refs**: sistemas operacionais; filas de produção.

### 8. Recovery Agent
- **Intenção**: recuperar de falhas durante execução (timeouts, erros, loops).
- **Estrutura**: detecta anomalia → aplica estratégia (retry, fallback, re-planejamento).
- **Quando usar**: produção; agentes de longa duração; ambientes instáveis.
- **Anti-patterns**: retry cego infinito; sem classificação de erro.
- **Custo**: variável; deve ter orçamento próprio.
- **Refs**: padrões de resiliência (circuit breaker, saga).

---

## Categoria C — Padrões de Avaliação e Melhoria

### 9. Critic
- **Intenção**: avaliar saída de outro agente em loop; núcleo do evaluator-optimizer.
- **Estrutura**: gerador → `critic` → feedback → gerador refina.
- **Quando usar**: feedback humano articulável; LLM consegue avaliar.
- **Anti-patterns**: critic genérico; sem critério de parada.
- **Custo**: 2× chamadas por iteração.
- **Refs**: Anthropic *Evaluator-Optimizer*; Reflexion.

### 10. Evaluator
- **Intenção**: medir qualidade contra critérios objetivos (não necessariamente em loop).
- **Estrutura**: `evaluator(output, criteria) → score + breakdown`.
- **Quando usar**: eval automatizado; CI para agentes.
- **Anti-patterns**: evaluator subjetivo; sem calibração.
- **Custo**: 1 chamada por avaliação.
- **Refs**: LLM-as-judge; Ragas.

### 11. Reviewer
- **Intenção**: revisar/critica iterativamente com foco em melhoria incremental.
- **Estrutura**: gerar → `reviewer` sugere melhorias → revisar → (até satisfazer).
- **Quando usar**: qualidade é crítica; múltiplas iterações valem.
- **Anti-patterns**: reviewer que sempre aprova; sem fim.
- **Custo**: N× chamadas.
- **Refs**: Reflexion; padrões de editing humano adaptados.

### 12. Reflection Agent
- **Intenção**: auto-crítica; o agente avalia sua própria saída e aprende.
- **Estrutura**: agente → `reflection` (auto-avaliação) → memória → próxima tentativa.
- **Quando usar**: sinal de falha; múltiplas tentativas; aprender com erros.
- **Anti-patterns**: reflexão genérica; sem uso efetivo da memória.
- **Custo**: 1 chamada extra por tentativa.
- **Refs**: Shinn et al. *Reflexion* (arXiv:2303.11366).

---

## Categoria D — Padrões de Informação e Memória

### 13. Researcher
- **Intenção**: buscar e recuperar informação de múltiplas fontes.
- **Estrutura**: `researcher(query)` → retrieve → filtrar → sintetizar.
- **Quando usar**: tarefas que exigem informação externa.
- **Anti-patterns**: retrieve sem filter; fonte única.
- **Custo**: N retrieves + 1 síntese.
- **Refs**: Agentic RAG.

### 14. Retrieval Agent
- **Intenção**: especialista em RAG — decide o quê/quando recuperar, refina queries.
- **Estrutura**: loop com tools `search_kb`, `search_web`, `lookup_entity`.
- **Quando usar**: RAG agêntico multi-hop.
- **Anti-patterns**: parar cedo demais; sem re-ranking.
- **Custo**: variável (N hops).
- **Refs**: Adaptive/CRAG/Self-RAG.

### 15. Memory Manager
- **Intenção**: gerenciar memória do sistema — o que armazenar, recalls, eviction.
- **Estrutura**: hooks para armazenar eventos, recuperar relevantes, aplicar política.
- **Quando usar**: agentes de longo prazo.
- **Anti-patterns**: armazenar tudo (custo); sem eviction.
- **Custo**: baixo (gerenciamento).
- **Refs**: MemGPT; Generative Agents.

### 16. Observer
- **Intenção**: observar execução e emitir eventos/métricas; não interfere no fluxo.
- **Estrutura**: hooks que registram traces, métricas, alertas.
- **Quando usar**: produção; observabilidade.
- **Anti-patterns**: observador que altera comportamento (efeito observador).
- **Custo**: mínimo.
- **Refs**: OpenTelemetry; observabilidade.

---

## Categoria E — Padrões de Governança e Segurança

### 17. Guardian
- **Intenção**: aplicar guardrails e exercer veto sobre ações perigosas.
- **Estrutura**: `guardian(proposed_action)` → aprova/rejeita/edita.
- **Quando usar**: ações destrutivas; ambientes adversariais.
- **Anti-patterns**: guardian leniente; sem log de veto.
- **Custo**: 1 chamada por ação sensível.
- **Refs**: Constitutional AI; NeMo Guardrails.

### 18. Meta-Governor
- **Intenção**: definir e revisar políticas que governam outros agentes (incl. guardians).
- **Estrutura**: `meta-governor` edita políticas com base em incidentes e métricas.
- **Quando usar**: sistemas auto-evolutivos; grandes fleets de agentes.
- **Anti-patterns**: meta-governor sem supervisão humana (risco de drift).
- **Custo**: baixo (decisões raras, impacto alto).
- **Refs**: Constitutional AI; meta-learning.

---

## Categoria F — Padrões de Meta-Agência e Evolução

### 19. Strategy Evolver
- **Intenção**: evoluir estratégias/prompts/topologias ao longo do tempo com base em performance.
- **Estrutura**: loop: medir performance → gerar variação → avaliar → promover/rejeitar.
- **Quando usar**: sistemas de longa duração; otimização contínua.
- **Anti-patterns**: evoluir sem eval rigoroso; deriva de objetivos.
- **Custo**: alto (muitas execuções para avaliar).
- **Refs**: DSPy; Promptbreeder; Voyager.

### 20. Learning Agent
- **Intenção**: aprender com experiências passadas; acumular skills.
- **Estrutura**: experiência → extrair skill/insight → armazenar → reusar.
- **Quando usar**: tarefas recorrentes; vale acumular conhecimento procedural.
- **Anti-patterns**: aprender coisas erradas; sem validação.
- **Custo**: variável.
- **Refs**: Voyager (auto-skills).

### 21. Simulation Agent
- **Intenção**: simular cenários para testar/avaliar antes de produção.
- **Estrutura**: simular N cenários → coletar métricas → recomendar.
- **Quando usar**: testes de robustez; "what-if" em fleet.
- **Anti-patterns**: simulação sem realismo.
- **Custo**: N× execuções simuladas.
- **Refs**: AgentVerse; sandboxes.

### 22. Negotiation Agent
- **Intenção**: negociar entre partes (agentes, recursos) para chegar a acordo.
- **Estrutura**: proposta → contraproposta → (loop) → acordo ou impasse.
- **Quando usar**: multi-agent com objetivos conflitantes.
- **Anti-patterns**: sem critério de parada; deadlock.
- **Custo**: N× chamadas.
- **Refs**: CAMEL; teoria de negociação.

### 23. Tool Agent
- **Intenção**: encapsular um domínio de ferramentas (ex.: "SAP agent", "GitHub agent").
- **Estrutura**: agente especializado num conjunto coeso de tools de um domínio.
- **Quando usar**: domínio com muitas tools relacionadas; quer isolamento.
- **Anti-patterns**: tool agent fazendo tudo (vira god object).
- **Custo**: igual a agente normal.
- **Refs**: MCP servers como "tool agents" bem definidos.

---

## Mapa de uso (resumo)

| Preciso de… | Padrões candidatos |
|---|---|
| Orquestrar workers | Supervisor, Orchestrator, Coordinator |
| Rotear por categoria | Router |
| Planejar e executar | Planner, Executor, Scheduler |
| Avaliar e melhorar | Critic, Evaluator, Reviewer, Reflection |
| Recuperar informação | Researcher, Retrieval Agent |
| Gerenciar memória | Memory Manager, Observer |
| Garantir segurança | Guardian, Meta-Governor |
| Evoluir o sistema | Strategy Evolver, Learning Agent |
| Testar/simular | Simulation Agent |
| Negociar entre agentes | Negotiation Agent |
| Encapsular domínio | Tool Agent |
| Recuperar de falhas | Recovery Agent |

## Princípios transversais

1. **Composição**: padrões combinam; raramente há só um.
2. **Custo sempre**: cada padrão tem custo; justifique com valor.
3. **Anti-patterns importam**: conhecer o que **não** fazer é metade do design.
4. **Evolução**: padrões novos surgem; este catálogo é vivo.

## Status

- ✅ Padrões divididos em arquivos próprios (`01-supervisor.md` a `23-tool-agent.md`)
- 🔄 Exemplos de código runnable em desenvolvimento (`19-Examples/`)
- ⏳ Métricas empíricas de quando cada padrão ajuda (próxima versão)
