# ETHAGT06 — Avaliação do Módulo

> Curso: RAG Agêntico (Adaptive · Corrective · Self-RAG · Agentic) · Nota mínima de aprovação: 3,0

## Composição da nota (4 pilares)

| Pilar | Peso | Instrumento |
|---|---|---|
| Técnico | 40% | Projeto (sistema RAG de produção) + eval report (Ragas) |
| Consultivo | 30% | Apresentação dos resultados para "cliente" |
| Comportamental | 20% | Code review |
| Prático | 10% | Demo: agente respondendo com fontes citadas |

**Nota final** = Σ(pilar × peso).

---

## Rubrica — Pilar Técnico (40%)

O projeto exige construir um sistema RAG de produção sobre um corpus técnico (ex.: documentação Etho) com pipeline agêntico (Adaptive/CRAG/Self-RAG/Agentic), eval automatizado (Ragas) e relatório de qualidade. Meta: faithfulness ≥ 0.85 e context recall ≥ 0.80.

| Critério | Peso | 1 (muito abaixo) | 3 (esperado) | 5 (referência) |
|---|---|---|---|---|
| Correção técnica | 25% | RAG ingênuo sem componente agêntico; faithfulness < 0.70 | Pipeline agêntico funcional (≥1 padrão); faithfulness ≥ 0.85 e context recall ≥ 0.80 | Agentic RAG multi-hop + casos de borda (doc irrelevante, fallback web, CRAG trigger correto) com métricas mantidas |
| Qualidade arquitetural | 25% | Chunking hardcoded; sem separação retrieval/generation | Separação razoável; re-ranking e query rewriting presentes | Pipeline modular (chunking + retrieval + rerank + generation intercambiáveis), ADR justifica padrão agêntico escolhido |
| Profundidade | 20% | Superficial; não diferencia os 4 padrões | Compara Adaptive vs CRAG vs Self-RAG; justifica escolha | Discute trade-offs (latência vs qualidade, quando CRAG busca na web), compara chunking strategies, analisa falhas |
| Produção-ready | 15% | Só roda em notebook; sem Docker | Docker (vector store + app); eval report com template oficial | Docker + dataset de holdout + eval reproduzível (rerun) + relatório de iteração de qualidade |
| Avaliação/observabilidade | 15% | Sem eval automatizado | Eval report com Ragas (faithfulness, relevance, context precision/recall) | Eval automatizado no CI, análise de falhas categorizada, A/B testing de prompts/chunking documentado |

**Eval report** (parte do Pilar Técnico): relatório completo usando `24-Templates/template-eval-report.md` com métricas, dataset, análise de falhas e correções propostas. Peso: 50% do pilar técnico.

---

## Critérios dos demais pilares

- **Consultivo (30%):** Apresentação dos resultados para "cliente" (banca simulada como stakeholder de produto).
  - *1:* Apresenta sem dados; não justifica o pipeline.
  - *3:* Apresenta métricas (faithfulness, recall) e justifica o padrão agêntico escolhido.
  - *5:* Usa dados para mostrar ganho vs RAG ingênuo, articula limites, propõe roadmap de melhoria.

- **Comportamental (20%):** Code review do pipeline de um colega.
  - *1:* Comentários ausentes ou genéricos.
  - *3:* ≥5 observações sobre chunking, retrieval e tratamento de docs irrelevantes.
  - *5:* Sugere estratégias de re-ranking, identifica viés de LLM-as-judge, propõe melhoria de query rewriting.

- **Prático (10%):** Demo: agente respondendo com fontes citadas em tempo real.
  - *1:* Agente não cita fontes ou responde incorretamente.
  - *3:* Agente responde corretamente com fontes e métricas aceitáveis.
  - *5:* Mostra CRAG fallback em ação, re-ranking visível, lida com pergunta fora do domínio.

---

## Regras

- Entrega: repositório Git com sistema, eval report (`./docs/eval-report.md`), ADR e dataset de teste.
- **Integridade acadêmica:** métricas de eval devem ser reais e reproduzíveis (script de rerun incluído). Fabricação de métricas resulta em nota 1,0.
- Atraso: -0,5 ponto por dia útil, até 3 dias.
