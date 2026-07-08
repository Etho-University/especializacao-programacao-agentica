# `ETHAGT15` — Meta-Agentes & Sistemas Autoaprendentes

> Fase D · Carga 15 h · Versão 1.0 · Julho 2026

## 1. Identificação

| Campo | Valor |
|---|---|
| Código | `ETHAGT15` |
| Título | Meta-Agentes & Sistemas Autoaprendentes (agents that build agents) |
| Fase interna | D |
| Carga horária | 15 h |
| Pré-requisitos | `ETHAGT10` |
| Módulos que dependem deste | `ETHAGT16`, `ETHAGT90` |

## 2. Objetivos

**Objetivo geral**: Explorar a **fronteira dos meta-agentes** — agentes que criam, otimizam e evoluem outros agentes — com conscientização dos riscos.

**Objetivos específicos**:
1. Definir meta-agente, strategy evolver, meta-learning para agentes.
2. Implementar um sistema onde um agente gera/configura agentes especializados.
3. Aplicar otimização automatizada de prompts/tools.
4. Discutir auto-aprendizado contínuo com memória acumulada.
5. Identificar riscos (recursão descontrolada, drift, segurança) e mitigações.

## 3. Competências desenvolvidas

| Competência | Nível ao final |
|---|---|
| C1 Programação Agêntica | **A** |
| C2 Multi-Agent Systems | **A** |
| C3 MCP & Tool Use | B |
| C4 Agent Memory | **A** |
| C6 Agent Security | **I** |

## 4. Conteúdo programático

### Unidade 1 — O que é meta-agência (2 h)
- Agentes que operam sobre agentes
- Estratégias: synthesis, evolution, optimization
- Risco vs benefício

### Unidade 2 — Geração de agentes (3 h)
- Meta-agente que produz prompts/tools/agentes para tarefas específicas
- Templates e composição
- Validação do agente gerado (eval antes de deploy)

### Unidade 3 — Otimização automatizada (3 h)
- Otimização de prompts (DSPy, Atlas, Promptbreeder)
- Otimização de tools (reescrita de descrições)
- Otimização de topologia (qual worker agregar?)

### Unidade 4 — Auto-aprendizado contínuo (3 h)
- Memória de sucesso/falha
- Reflexion em nível de sistema
- Estratégia evolutiva (strategy evolver)
- Quando esquecer (drift)

### Unidade 5 — Riscos e governança (4 h)
- Recursão e loops de auto-modificação
- Drift de objetivos (goal drift)
- Segurança: meta-governor pattern, vetos
- Confiança incremental (sandbox antes de produção)

## 5. Bibliografia

### Fundamental
- Khattab, O. *DSPy: Compiling Declarative LLM Calls* (arXiv:2310.03714).
- Fernando, C. *Promptbreeder* (arXiv:2309.16797).
- Hu, S. *Meta-Prompting* (arXiv:2311.11402).

### Complementar
- *Voyager* (Wang) — agente que aprende skills no Minecraft.
- *Generative Agents* (Park).

## 6. Papers canônicos

- `arXiv:2310.03714` — DSPy
- `arXiv:2305.16291` — Voyager (auto-skills)
- `arXiv:2311.11402` — Meta-Prompting

## 7. Laboratórios

- **Lab 1** (4 h): "Agente que escreve agente". Construir meta-agente que, dada uma tarefa, produz um agente especializado e o avalia.

## 8. Projeto do módulo

**Descrição**: implementar um sistema onde prompts/tools são otimizados automaticamente (ex.: DSPy) e medir ganho em um benchmark.
**Entrega**: sistema + eval comparando antes/depois da otimização.
**Critério de sucesso**: ganho mensurável e reproduzível.

## 9. Exercícios

1. Quando otimizar prompts é melhor que reescrevê-los manualmente?
2. Defina goal drift e proponha uma detecção.
3. Por que meta-governor é necessário?
4. Escreva um "veto" para um meta-agente.
5. Verdadeiro/falso: "Auto-aprendizado contínuo sempre melhora."

## 10. Avaliação

| Pilar | Peso | Instrumento |
|---|---|---|
| Técnico | 40% | Projeto + análise crítica |
| Consultivo | 30% | Apresentação dos riscos/benefícios |
| Comportamental | 20% | Ética (code review focado em risco) |
| Prático | 10% | Demo: meta-agente em ação |

**Nota mínima**: 3,0.

## 11. Slides

- Slides: `03-Slides/ETHAGT15-slides.md` (~50 slides).

## 12. Leitura complementar

- DSPy docs; Voyager paper; Anthropic safety.

## 13. Ferramentas

- DSPy, Atlas, Promptbreeder refs, LangGraph.

## 14. Diagramas

- Diagramas: `12-Diagrams/ETHAGT15/` — meta-agent.mmd, evolution-loop.mmd, safety-fences.mmd.

## 15. Estudo de caso

- Voyager (auto-skills em ambiente fechado).

## 16. Ficha de pesquisa

- Ficha: `20-Research/ETHAGT15-pesquisa.md`.

---

*Mantido por: Universidade Etho · Versão 1.0 · Julho 2026*
