# `ETHAGT90` — Capstone: Plataforma de Pesquisa Autônoma

> Especialização em Programação Agêntica · Universidade Etho
> Capstone · Carga 60 h · Versão 1.0 · Julho 2026

## 1. Identificação

| Campo | Valor |
|---|---|
| Código | `ETHAGT90` |
| Título | Capstone — Plataforma de Pesquisa Autônoma (AutoResearch) |
| Fase interna | Capstone (pós-Fase D) |
| Fase Etho | Especialização (Fase 4) |
| Carga horária | 60 h |
| Pré-requisitos | **Todos os 16 módulos** (`ETHAGT01`-`ETHAGT16`) aprovados |
| Módulos que dependem deste | — (certificação) |

## 2. Objetivos

**Objetivo geral**: Integrar, em uma plataforma realista, **todos os conceitos da Especialização**, demonstrando domínio de arquitetura, implementação, produção, segurança e avaliação de um sistema de agentes autônomos.

**Objetivos específicos**:
1. Projetar uma arquitetura multi-agente justificada por ADR.
2. Implementar topologia Hierarchical + Orchestrator-Workers + Evaluator-Optimizer.
3. Construir MCP servers customizados.
4. Arquitetar memória multi-camada (vector + grafo + relacional).
5. Operar com event-driven + durable execution.
6. Aplicar guardrails, HITL e red team.
7. Produzir observabilidade e eval report com benchmark próprio.
8. Defender perante painel de especialistas.

## 3. Competências desenvolvidas (todas em nível A)

| Competência | Nível ao final |
|---|---|
| C1 Programação Agêntica | **A** |
| C2 Multi-Agent Systems | **A** |
| C3 MCP & Tool Use | **A** |
| C4 Agent Memory | **A** |
| C5 AgentOps & Avaliação | **A** |
| C6 Agent Security | **A** |

## 4. Cenário — Plataforma de Pesquisa Autônoma (AutoResearch)

Um sistema multi-agente que, dada uma **pergunta de pesquisa técnica**, executa:

```
Planejar → Buscar (web, GitHub, arXiv, Confluence, Jira)
   → Recuperar (RAG agêntico + KG)
   → Sintetizar
   → Criticar (evaluator-optimizer)
   → Revisar (HITL opcional)
   → Publicar relatório técnico com fontes e avaliações
```

### Exemplo de pergunta
*"Quais são os padrões arquiteturais emergentes para sistemas multi-agente em produção, e quais trade-offs cada um apresenta?"*

O sistema deve produzir um relatório de 5-10 páginas com referências, comparações, e uma recomendação fundamentada.

## 5. Requisitos obrigatórios

### 5.1 Arquitetura (C1, C2)
- Topologia **Hierarchical** (supervisor geral) + **Orchestrator-Workers** (para sub-tarefas de busca) + **Evaluator-Optimizer** (loop de síntese/crítica)
- ADRs para cada decisão não-trivial (≥3 ADRs)
- Diagramas C4 (Context, Container, Component)

### 5.2 Ferramentas e MCP (C3)
- ≥ **3 MCP servers customizados** (ex.: arXiv MCP, GitHub MCP, Confluence MCP)
- Governança: catálogo, permissões, logs, versionamento
- ADR de governança

### 5.3 Memória (C4)
- **Multi-camada**: working (context window) + episódica (vector) + semântica (KG) + procedural (skills)
- Checkpointer persistente (Postgres)
- Política de privacidade/evicção documentada

### 5.4 Orquestração (C1, C2)
- Event-driven para paralelismo (NATS ou Kafka)
- Durable execution (Temporal ou equivalente) para sobreviver a crashes
- ≥1 saga compensatória

### 5.5 Segurança (C6)
- Threat model documentado
- Guardrails (input/output filtering, structured outputs)
- HITL obrigatório em checkpoints críticos (ex.: antes de publicar)
- Red team executado (≥10 casos)

### 5.6 Observabilidade & Avaliação (C5)
- Traces completos (LangSmith/Phoenix/Langfuse)
- Eval automatizado (LLM-as-judge + golden cases)
- **Benchmark próprio** com ≥30 perguntas de pesquisa
- **Eval report completo** (template `24-Templates/template-eval-report.md`)

### 5.7 Produção (C1, C5)
- Docker / Docker Compose
- README reprodutível
- Métricas exportadas (custo, latência, success rate)

## 6. Cronograma sugerido (8 semanas)

| Semana | Foco |
|---|---|
| 1 | Proposta + arquitetura + ADRs + diagramas C4 |
| 2 | MCP servers + memória multi-camada |
| 3 | Topologia multi-agente (supervisor + workers) |
| 4 | Event-driven + durable execution |
| 5 | RAG agêntico + KG + evaluator-optimizer |
| 6 | Segurança + guardrails + HITL + red team |
| 7 | Observabilidade + eval + benchmark + eval report |
| 8 | Hardening + documentação + ensaio de defesa |

## 7. Entregáveis

1. **Código** (repositório Git com Docker Compose)
2. **Documentação**: README + ≥3 ADRs + diagramas C4 + threat model
3. **Eval report** completo (resultados em benchmark próprio)
4. **Apresentação** (25 min) + **defesa Q&A** (20 min) para painel ≥3 especialistas

## 8. Avaliação (4 pilares)

| Pilar | Peso | Instrumento | Critério |
|---|---|---|---|
| Técnico | 40% | Código + ADRs + eval report | ≥ 4,0 |
| Consultivo | 30% | Apresentação + defesa para painel | ≥ 4,0 |
| Comportamental | 20% | Code review, colaboração, ética | ≥ 4,0 |
| Prático | 10% | Demo ao vivo: 3 perguntas de pesquisa | ≥ 4,0 |

**Atenção**: capstone exige nota ≥ **4,0** em **todos** os pilares (não média). Ver `24-Templates/template-rubrica-avaliacao.md`.

## 9. Critérios de sucesso (mensuráveis)

- Success rate no benchmark próprio ≥ 60%
- Relatório coerente (avaliado por humanos/painel) em ≥ 70% dos casos
- Custo por pesquisa ≤ $X (definido no ADR de FinOps)
- Latência p95 ≤ Y minutos (definido no ADR)
- ≥ 80% dos vetores críticos de red team mitigados

## 10. Painel de avaliação

- ≥3 especialistas em Agentic AI (interno Etho ou convidados)
- Código + docs entregues **5 dias úteis antes** da defesa
- Defesa ao vivo (presencial ou video)
- Deliberação imediata após Q&A

## 11. Slides de apoio

`03-Slides/ETHAGT90/README.md` — guia para construção dos ~30 slides de defesa.

## 12. Leitura complementar

Todos os papers dos módulos anteriores; *AI Scientist* (Sakana).

## 13. Ferramentas

Tudo o que foi usado nos módulos (Python, LangGraph/OpenAI SDK, MCP, Postgres, Redis, Qdrant, Neo4j, Kafka/NATS, Temporal, LangSmith/Phoenix, Docker).

## 14. Diagramas

`12-Diagrams/ETHAGT90/` — visão C4 completa + fluxo de pesquisa + topologia.

## 15. Estudo de caso

Inspiração em *AI Scientist* (Sakana) e *Deep Research* (OpenAI/Anthropic) — adaptado para o contexto Etho.

## 16. Ficha de pesquisa

`20-Research/ETHAGT90-pesquisa.md` — fontes para a arquitetura.

## 17. Conexão com a certificação

Aprovação neste capstone (≥4,0 em todos os pilares) é **pré-requisito** da certificação "Especialista em Programação Agêntica" da Universidade Etho. Ver `27-Certification/`.

---

*Mantido por: Escola de Tecnologia — Universidade Etho · Versão 1.0 · Julho 2026*
