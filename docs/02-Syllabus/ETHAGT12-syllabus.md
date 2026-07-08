# `ETHAGT12` — AgentOps, Observabilidade & Avaliação

> Fase D · Carga 30 h · Versão 1.0 · Julho 2026

## 1. Identificação

| Campo | Valor |
|---|---|
| Código | `ETHAGT12` |
| Título | AgentOps, Observabilidade & Avaliação (LLMOps para agentes) |
| Fase interna | D — Produção, Governança e Fronteira |
| Carga horária | 30 h |
| Pré-requisitos | `ETHAGT11` |
| Módulos que dependem deste | `ETHAGT13`, `ETHAGT90` |

## 2. Objetivos

**Objetivo geral**: Estabelecer **rigor experimental** em sistemas de agentes — observar (traces), medir (métricas), avaliar (evals e benchmarks) e iterar com confiança.

**Objetivos específicos**:
1. Implementar observabilidade end-to-end (traces, spans, métricas).
2. Construir pipelines de avaliação automatizada (LLM-as-judge, golden cases, regressão).
3. Aplicar benchmarks canônicos (SWE-bench, GAIA, τ-bench, AgentBench, WebArena).
4. Operar ciclos de melhoria contínua com dados.
5. Reportar resultados com rigor (eval report).

## 3. Competências desenvolvidas

| Competência | Nível ao final |
|---|---|
| C1 Programação Agêntica | **A** |
| C2 Multi-Agent Systems | B |
| C4 Agent Memory | B |
| C5 AgentOps & Avaliação | **A** |

## 4. Conteúdo programático

### Unidade 1 — Por que agentes são difíceis de avaliar (3 h)
- Não-determinismo; dependência de ambiente; custo de runs
- Falácias: "parece bom", "funcionou uma vez"
- Avaliação contínua vs pontual

### Unidade 2 — Observabilidade (5 h)
- Traces, spans, bags (contexto)
- OpenTelemetry para LLMs (GenAI semantic conventions)
- Tooling: LangSmith, Phoenix (Arize), Langfuse, OpenLLMetry
- Logs estruturados vs traces
- Custo de observabilidade

### Unidade 3 — Avaliação automatizada (6 h)
- LLM-as-judge: quando confiável, vieses, mitigações
- Golden cases e conjuntos de regressão
- Métricas de tarefa: success rate, partial credit, custo/latência
- Métricas de processo: steps, loops, tool misuse
- A/B testing de prompts/tools

### Unidade 4 — Benchmarks canônicos (5 h)
- **SWE-bench / SWE-bench Verified**: código
- **GAIA**: raciocínio geral multi-step
- **τ-bench**: tool use em domínios (airline, retail)
- **AgentBench**: panorama amplo
- **WebArena / VisualWebArena**: navegação web
- Como rodar, limites, contaminação

### Unidade 5 — Ciclo de melhoria (5 h)
- Dataset crescente (você não mediu se não mediu)
- CI para agentes (testes de regressão a cada mudança)
- Shadow runs, canary
- Feedback humano estruturado

### Unidade 6 — Reportando resultados (6 h)
- Eval report (template `24-Templates/template-eval-report.md`)
- Análise de falhas (categorização)
- Comparações honestas (vs baseline, vs humano)
- Comunicação para stakeholders

## 5. Bibliografia

### Fundamental
- Jimenez, C. *SWE-bench: Can Language Models Resolve Real-World GitHub Issues?* (arXiv:2310.06770).
- Mialon, G. *GAIA: a benchmark for General AI Assistants* (arXiv:2311.12983).
- Yao, S. *τ-bench: A Benchmark for Tool-Agent-User Interaction* (arXiv:2404.44529).

### Complementar
- Liu, X. *AgentBench* (arXiv:2308.03688).
- Zhou, S. *WebArena* (arXiv:2307.13854).
- LangSmith / Phoenix / Langfuse docs.

## 6. Papers canônicos

- `arXiv:2310.06770` — SWE-bench
- `arXiv:2311.12983` — GAIA
- `arXiv:2404.44529` — τ-bench
- `arXiv:2308.03688` — AgentBench

## 7. Laboratórios

- **Lab 1** (5 h): "Traces everywhere". Adicionar observabilidade (LangSmith ou Phoenix) a um agente existente; criar um dashboard.
- **Lab 2** (5 h): "Eval automatizado". Construir pipeline de avaliação com LLM-as-judge + golden cases; detectar regressão após mudança de prompt.

## 8. Projeto do módulo

**Descrição**: avaliar um agente (construído em módulos anteriores) em um subconjunto de τ-bench ou GAIA; produzir eval report completo.
**Entrega**: eval report (template) + dataset + código de rerun + análise de falhas.
**Critério de sucesso**: eval reproduzível; ≥3 categorias de falha documentadas com correção proposta.

## 9. Exercícios

1. Quais vieses do LLM-as-judge? Como mitigar?
2. Quando usar SWE-bench vs um benchmark custom?
3. Escreva um golden case com critério de sucesso mensurável.
4. Como detectar contaminação de benchmark?
5. Verdadeiro/falso: "Bom score em benchmark garante bom desempenho em produção."

## 10. Avaliação

| Pilar | Peso | Instrumento |
|---|---|---|
| Técnico | 40% | Eval report + pipeline |
| Consultivo | 30% | Apresentação dos resultados para "diretoria" |
| Comportamental | 20% | Code review |
| Prático | 10% | Demo: regressão detectada |

**Nota mínima**: 3,0.

## 11. Slides

- Slides: `03-Slides/ETHAGT12-slides.md` (~90 slides).

## 12. Leitura complementar

- *Evals for LLMs* (Hamel Husain); Eugene Yan blog.

## 13. Ferramentas

- LangSmith, Phoenix, Langfuse, OpenLLMetry, OpenTelemetry, Ragas, DeepEval.

## 14. Diagramas

- Diagramas: `12-Diagrams/ETHAGT12/` — trace-anatomy.mmd, eval-pipeline.mmd, benchmark-landscape.mmd.

## 15. Estudo de caso

- Anthropic avaliando Claude em SWE-bench.

## 16. Ficha de pesquisa

- Ficha: `20-Research/ETHAGT12-pesquisa.md`.

---

*Mantido por: Universidade Etho · Versão 1.0 · Julho 2026*
