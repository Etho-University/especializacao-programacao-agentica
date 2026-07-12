# ETHAGT90 — Marcos de Acompanhamento

> Cronograma de 8 semanas com **8 marcos (M1-M8)**. Cada marco é check-in com mentor; sem aprovação, não avança.

## Semana 1 — M1: Arquitetura aprovada

**Foco**: proposta + arquitetura + ADRs + C4.

**Entregas para o check-in**:
- [ ] Documento de proposta (1 página): objetivo, escopo, não-objetivos.
- [ ] ≥3 ADRs iniciais (topologia, transporte, memória).
- [ ] Diagramas C4 (Context, Container).
- [ ] Lista dos 3+ MCP servers planejados.

**Critério de aprovação do mentor**:
- Arquitetura cobre todos os requisitos do enunciado.
- ADRs são coerentes e discutem alternativas.
- Escopo é realista para 8 semanas.

## Semana 2 — M2: Infraestrutura base

**Foco**: MCP servers + memória multi-camada.

**Entregas**:
- [ ] 3 MCP servers customizados funcionando (cada com ≥2 tools).
- [ ] Catálogo de servers (YAML).
- [ ] Vector DB operacional (Qdrant ou equivalente).
- [ ] Postgres checkpointer configurado.
- [ ] Knowledge graph inicial (Neo4j) — schema.
- [ ] Docker Compose roda toda a infra.

**Critério**:
- Servers respondem a chamadas diretas (testar via MCP Inspector).
- Checkpointer persiste e retoma estado.
- Compose sobe sem erro.

## Semana 3 — M3: Pipeline end-to-end (happy path)

**Foco**: topologia multi-agente básica.

**Entregas**:
- [ ] Supervisor + workers implementados (LangGraph ou equivalente).
- [ ] Fluxo completo: pergunta → buscar → sintetizar → relatório básico.
- [ ] Relatório gerado para 1 pergunta de teste.

**Critério**:
- Fluxo completo roda sem erro para pelo menos 1 pergunta.
- Relatório tem estrutura mínima (intro, achados, conclusão).
- Ainda sem robustez — só happy path.

## Semana 4 — M4: Resiliência

**Foco**: event-driven + durable execution.

**Entregas**:
- [ ] Event bus (NATS/Kafka) integrado para paralelismo.
- [ ] Workflow engine (Temporal) para durable.
- [ ] Saga compensatória documentada.
- [ ] **Chaos test**: mate um worker no meio; sistema recupera.

**Critério**:
- Sistema sobrevive a ≥2 falhas injetadas.
- Saga documentada e demonstrada.
- HITL via interrupt funciona (pausa por "horas").

## Semana 5 — M5: Qualidade do relatório

**Foco**: RAG agêntico + KG + evaluator-optimizer.

**Entregas**:
- [ ] RAG agêntico (Adaptive ou superior) com re-ranking.
- [ ] Híbrido (vector + graph) integrado.
- [ ] Loop evaluator-optimizer funcional.
- [ ] Relatórios coerentes em ≥50% dos casos (em 10 testes).

**Critério**:
- 5/10 relatórios considerados coerentes por avaliação humana.
- Fontes citadas em ≥80% dos casos.
- Evaluator-optimizer melhora qualidade vs baseline.

## Semana 6 — M6: Segurança

**Foco**: guardrails + HITL + red team.

**Entregas**:
- [ ] Threat model (STRIDE) completo.
- [ ] Guardrails implementados (input/output filter, structured outputs).
- [ ] HITL obrigatório antes de publicar.
- [ ] Red team: ≥10 casos testados, ASR documentado.
- [ ] Policy-as-code (OPA) com ≥2 regras.

**Critério**:
- ASR < 30% nos vetores críticos.
- HITL funcional (pausa, humano aprova/edita, resume).
- Policies aplicadas em runtime.

## Semana 7 — M7: Observabilidade e avaliação

**Foco**: traces + eval + benchmark + eval report.

**Entregas**:
- [ ] Traces completos (Phoenix/LangSmith).
- [ ] Eval automatizado (LLM-as-judge + golden cases).
- [ ] Benchmark próprio: ≥30 perguntas curadas.
- [ ] **Eval report completo** (template).
- [ ] FinOps dashboard ou relatório.

**Critério**:
- Eval reproduzível (script de rerun + dataset).
- ≥3 categorias de falha documentadas com correção proposta.
- Custo e latência medidos (p50/p95).

## Semana 8 — M8: Pronto para defesa

**Foco**: hardening + documentação + ensaio.

**Entregas**:
- [ ] Documentação final completa (README + ADRs + threat model + privacy policy).
- [ ] Código limpo (sem TODOs críticos, sem bugs conhecidos).
- [ ] Apresentação de 25 min ensaiada.
- [ ] Material entregue ao painel (5 dias úteis antes).

**Critério**:
- Tudo rodando via `docker compose up`.
- Apresentação cobre: arquitetura, decisões, resultados, trade-offs, riscos.
- Demo ao vivo funciona sem ensaio (3 perguntas novas).

---

## Riscos comuns (e mitigações)

| Risco | Mitigação |
|---|---|
| Escopo ambicioso demais | Cortar features em M3 se atrasado; foco em integração |
| Custo de LLM explodindo | Model routing (Haiku para research simples) + cache |
| Bug crônico em componente | Isolar e simplificar; ADR documentando workaround |
| Red team encontra falha grave | Priorizar correção; se não corrigível, documentar em ADR de risco |
| Tempo insuficiente na semana 8 | Começar ensaio na semana 7 |

## Princípio

> **Melhor sistema incompleto mas robusto que sistema "completo" mas frágil.** Se tiver que cortar, corte features — não corte HITL, red team, ou eval.
