# ETHAGT12 — Avaliação do Módulo

> Curso: AgentOps, Observabilidade & Avaliação (LLMOps para agentes) · Nota mínima de aprovação: 3,0

## Composição da nota (4 pilares)

| Pilar | Peso | Instrumento |
|---|---|---|
| Técnico | 40% | Eval report completo + pipeline de avaliação automatizada |
| Consultivo | 30% | Apresentação dos resultados para "diretoria" |
| Comportamental | 20% | Code review |
| Prático | 10% | Demo: regressão detectada ao vivo |

**Nota final** = Σ(pilar × peso).

---

## Rubrica — Pilar Técnico (40%)

O projeto exige avaliar um agente (de módulos anteriores) em um subconjunto de τ-bench ou GAIA, produzindo um eval report completo e reproduzível, com ≥3 categorias de falha documentadas e correção proposta para cada uma.

| Critério | Peso | 1 (muito abaixo) | 3 (esperado) | 5 (referência) |
|---|---|---|---|---|
| Correção técnica | 25% | Pipeline de eval não roda; sem dataset | Pipeline de eval funcional (LLM-as-judge + golden cases); eval reproduzível via rerun | Pipeline completo + casos de borda (viés de judge, contaminação, nondeterminismo) tratados com mitigações |
| Qualidade arquitetural | 25% | Eval acoplado ao agente; sem separação | Separação razoável (dataset · pipeline · report); CI-ready | Padrões claros (golden cases parametrizados, regression suite), benchmark reutilizável, ADR de estratégia de eval |
| Profundidade | 20% | Superficial; métricas sem contexto | Métricas corretas (success rate, partial credit, custo/latência, tool misuse); ≥3 categorias de falha | Discute trade-offs (LLM-as-judge vs humano, SWE-bench vs custom), analisa vieses, compara com baseline/humano honestamente |
| Produção-ready | 15% | Sem Docker nem dataset versionado | Docker + dataset versionado; eval report com template oficial | Docker + CI pipeline (testes de regressão a cada mudança) + eval report completo (template `24-Templates/`) |
| Avaliação/observabilidade | 15% | Sem observabilidade | Traces instrumentados (LangSmith/Phoenix); dashboard de métricas | Observabilidade end-to-end (traces/spans GenAI), shadow runs/canary, análise de falhas categorizada e priorizada |

**Eval report** (parte do Pilar Técnico): relatório completo usando `24-Templates/template-eval-report.md` com metodologia, dataset, métricas, ≥3 categorias de falha analisadas, comparações honestas e correções propostas. Peso: 50% do pilar técnico.

---

## Critérios dos demais pilares

- **Consultivo (30%):** Apresentação dos resultados para "diretoria" (banca simulada como stakeholders não-técnicos).
  - *1:* Apresenta métricas sem contexto nem recomendações.
  - *3:* Comunica resultados com clareza, destaca riscos e recomenda ações.
  - *5:* Traduz métricas em decisões de produto, articula limites do eval, propõe roadmap de melhoria.

- **Comportamental (20%):** Code review do pipeline de eval de um colega.
  - *1:* Comentários ausentes ou genéricos.
  - *3:* ≥5 observações sobre robustez do LLM-as-judge, golden cases e reprodutibilidade.
  - *5:* Identifica vieses de judge, sugere mitigações, avalia representatividade do dataset.

- **Prático (10%):** Demo: regressão detectada ao vivo após mudança de prompt/tool.
  - *1:* Não consegue detectar regressão.
  - *3:* Pipeline detecta regressão após mudança, mostrando o delta.
  - *5:* Mostra CI bloqueando regressão, categoriza a falha, propõe correção em tempo real.

---

## Regras

- Entrega: repositório Git com pipeline, dataset, eval report (`./docs/eval-report.md`) e código de rerun.
- **Integridade acadêmica:** métricas devem ser reais e reproduzíveis. Fabricação de resultados ou inflação de scores resulta em nota 1,0 e processo disciplinar.
- Atraso: -0,5 ponto por dia útil, até 3 dias.
