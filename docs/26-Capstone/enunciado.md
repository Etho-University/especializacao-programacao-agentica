# ETHAGT90 — Capstone: Enunciado Detalhado

> Especialização em Programação Agêntica · Universidade Etho
> Capstone · Carga 60 h · Versão 1.0 · Julho 2026

Este é o enunciado completo do projeto final. O README em [`26-Capstone/README.md`](README.md) é uma visão geral; aqui está a especificação detalhada — **o contrato entre aluno e painel de avaliação**.

---

## 1. Contexto e motivação

Você percorreu 16 módulos cobrindo fundamentos, razão/memória/conhecimento, multi-agentes/ferramentas/orquestração, e produção/fronteira. O Capstone é a **prova de integração**: construir uma plataforma realista que exercite **todos** os conceitos.

O cenário escolhido é uma **Plataforma de Pesquisa Autônoma (AutoResearch)** — um sistema multi-agente que conduz pesquisa técnica de ponta a ponta, do planejamento à publicação. É o caso mais desafiador coberto na fronteira (ETHAGT16), e integra naturalmente todas as competências da Especialização.

## 2. Objetivo

Construir, documentar, avaliar e defender uma **plataforma de pesquisa autônoma** que:

- Recebe uma **pergunta de pesquisa técnica** em linguagem natural.
- Conduz o ciclo completo: **planejar → buscar → recuperar → sintetizar → criticar → revisar → publicar**.
- Produz um **relatório técnico** (5-10 páginas) com fontes verificáveis, comparações e recomendação fundamentada.
- Opera com **rigor de produção**: observabilidade, segurança, HITL, FinOps.

## 3. Requisitos obrigatórios (contrato)

Cada requisito mapeia competências dos módulos anteriores. **Todos** devem estar presentes.

### 3.1 Arquitetura (C1, C2) — ETHAGT01, 03, 10
- Topologia **Hierarchical** + **Orchestrator-Workers** + **Evaluator-Optimizer**.
- Pelo menos **3 ADRs** documentando decisões arquiteturais não-triviais.
- Diagramas **C4** (Context, Container, Component) em `12-Diagrams/ETHAGT90/`.

### 3.2 Ferramentas e MCP (C3) — ETHAGT02, 08
- Pelo menos **3 MCP servers customizados** (ex.: arXiv MCP, GitHub MCP, Confluence Etho MCP).
- Cada server com **≥2 tools** com ACI bem desenhada.
- **Catálogo de servers** (YAML) com governança documentada.
- **Threat model** do ecossistema MCP.

### 3.3 Memória (C4) — ETHAGT05, 07
- **Multi-camada**:
  - Working (context window gerenciado).
  - Episódica (vector store com timestamps).
  - Semântica (knowledge graph ou Postgres relacional).
  - Procedural (skills reutilizáveis — templates de seção de relatório, estratégias de busca).
- **Checkpointer** persistente (Postgres).
- **Política de privacidade/evicção** documentada.

### 3.4 RAG (C1, C4) — ETHAGT06, 07
- Pipeline **agêntico** (não ingênuo): Adaptive RAG ou superior.
- **Re-ranking** aplicado.
- **Híbrido** (vector + BM25 ou vector + graph).

### 3.5 Orquestração (C1, C2) — ETHAGT11
- **Event-driven** para paralelismo (NATS ou Kafka).
- **Durable execution** (Temporal ou equivalente) para sobreviver a crashes.
- Pelo menos **1 saga compensatória** documentada.

### 3.6 Segurança e governança (C6) — ETHAGT13
- **Threat model** completo (STRIDE).
- **Guardrails** (input filter, output filter, structured outputs).
- **HITL obrigatório** antes de "publicar" o relatório (humano revisa).
- **Red team** executado (≥10 casos) com ASR documentado.
- **Policy-as-code** (OPA ou equivalente) para pelo menos 2 regras.

### 3.7 Observabilidade e avaliação (C5) — ETHAGT12
- **Traces** completos (LangSmith/Phoenix/Langfuse).
- **Eval automatizado**: LLM-as-judge com rubrica + golden cases.
- **Benchmark próprio**: ≥30 perguntas de pesquisa curadas.
- **Eval report** completo (template `24-Templates/template-eval-report.md`).
- Métricas de **qualidade + eficiência + robustez + segurança**.

### 3.8 Produção (C1, C5) — ETHAGT14
- **Docker Compose** para rodar tudo localmente.
- **README** reprodutível (como rodar, testar, avaliar).
- **Métricas exportadas** (custo, latência, success rate).
- **FinOps dashboard** ou relatório.

## 4. Exemplo de pergunta de pesquisa

> *"Quais são os padrões arquiteturais emergentes para sistemas multi-agente em produção, e quais trade-offs cada um apresenta?"*

O sistema deve produzir um relatório que:
- Cite **≥10 fontes** (papers, docs, repositórios).
- Compare **≥3 abordagens** (topologias, frameworks, técnicas).
- Apresente **trade-offs** explícitos (custo, latência, robustez, etc.).
- Termine com **recomendação fundamentada** para um cenário específico.

## 5. Cronograma sugerido (8 semanas)

| Semana | Foco | Marco |
|---|---|---|
| 1 | Proposta + arquitetura + ADRs + C4 | M1: ADRs + diagramas aprovados pelo mentor |
| 2 | MCP servers + memória multi-camada | M2: 3 servers + memória funcionando |
| 3 | Topologia multi-agente (supervisor + workers) | M3: pipeline end-to-end "happy path" |
| 4 | Event-driven + durable execution | M4: sobrevive a crash injetado |
| 5 | RAG agêntico + KG + evaluator-optimizer | M5: relatórios coerentes em ≥50% dos casos |
| 6 | Segurança + guardrails + HITL + red team | M6: ASR < 30% nos vetores críticos |
| 7 | Observabilidade + eval + benchmark + eval report | M7: eval report completo |
| 8 | Hardening + documentação + ensaio de defesa | M8: pronto para defesa |

Cada marco (M1-M8) é **check-in com mentor** — sem aprovação, não avança.

## 6. Entregáveis

1. **Código** (repositório Git com Docker Compose).
2. **Documentação**:
   - `README.md` (como rodar).
   - `docs/adr/` — ≥3 ADRs.
   - `docs/architecture/` — diagramas C4.
   - `docs/threat-model.md`.
   - `docs/privacy-policy.md` (memória).
3. **Eval report** completo (template `24-Templates/template-eval-report.md`).
4. **Benchmark dataset** (≥30 perguntas + respostas ideais).
5. **Apresentação** (25 min) + **defesa Q&A** (20 min) para painel ≥3 especialistas.
6. **Demo ao vivo**: 3 perguntas executadas na hora.

## 7. Critérios de sucesso (mensuráveis)

| Métrica | Meta |
|---|---|
| Success rate no benchmark próprio | ≥ 60% |
| Relatório coerente (avaliado por painel) | ≥ 70% dos casos |
| Custo por pesquisa | ≤ definido no ADR de FinOps (ex.: $2) |
| Latência p95 | ≤ definido no ADR (ex.: 5 min) |
| Vetores críticos de red team mitigados | ≥ 80% |
| Fontes citadas e verificáveis | ≥ 10 por relatório |

## 8. Avaliação (4 pilares, nota ≥ 4,0 em **todos**)

| Pilar | Peso | Instrumento | Nota mínima |
|---|---|---|---|
| Técnico | 40% | Código + ADRs + eval report | **4,0** |
| Consultivo | 30% | Apresentação + defesa para painel | **4,0** |
| Comportamental | 20% | Code review, colaboração, ética | **4,0** |
| Prático | 10% | Demo ao vivo (3 perguntas) | **4,0** |

**Atenção**: o Capstone exige **≥ 4,0 em todos os pilares individualmente** (não média). Falhar num pilar reprova o capstone.

## 9. Painel de avaliação

- **≥ 3 especialistas** em Agentic AI (internos Etho ou convidados externos).
- Código + docs entregues **5 dias úteis antes** da defesa.
- Defesa ao vivo (presencial ou video).
- **Deliberação imediata** após Q&A.

## 10. O que NÃO fazer

- Não copiar exemplos sem entender (você terá de explicar tudo no Q&A).
- Não deixar bugs "quase funcionando" — success rate é medido em execução real.
- Não pular HITL ou red team — são pré-requisitos, não opcionais.
- Não inflar métricas — painel vai questionar; honestidade é critério.

## 11. Conexão com certificação

Aprovação neste capstone (≥4,0 em todos os pilares) é **pré-requisito** da certificação "Especialista em Programação Agêntica" da Universidade Etho. Ver [`27-Certification/`](../27-Certification/).

---

*Relacionado: [`architecture-reference.md`](architecture-reference.md) · [`milestones.md`](milestones.md) · [`defense-guide.md`](defense-guide.md) · [`rubric.md`](rubric.md)*
