---
password: Etho-Prof-2026
---
# ETHAGT15 — Prova do Módulo: Meta-Agentes & Sistemas Autoaprendentes

> Universidade Etho · Versão 1.0 · Julho 2026
> Duração: ~60 min · 10 questões · closed book · Pilar Técnico (40%)

Esta prova avalia a **fronteira dos meta-agentes** — agentes que criam, otimizam e evoluem outros agentes — com consciência dos riscos (recursão, goal drift, segurança).

---

## Parte 1 — Conceitos (Q1-4)

**1. (Múltipla escolha)** Um *meta-agente* é melhor definido como:
- (a) Um agente que só faz meta-comentários sobre outros.
- (b) Um agente que opera *sobre* agentes — gera, configura, otimiza ou evolui outros agentes.
- (c) Qualquer agente que use memória.

**2. (V/F justificado)** "Auto-aprendizado contínuo sempre melhora o sistema."

**3. (Múltipla escolha)** DSPy é uma ferramenta de:
- (a) Otimização automatizada de prompts (compilação declarativa de chamadas de LLM).
- (b) Orquestração de eventos (estilo Temporal).
- (c) Cache semântico de embeddings.

**4. (V/F justificado)** "Goal drift é quando o sistema otimiza para uma métrica que deriva do objetivo original."

---

## Parte 2 — Aplicação e trade-off (Q5-8)

**5. (Trade-off)** Dê 2 critérios para decidir quando **otimizar prompts automaticamente** (DSPy) vale a pena versus reescrevê-los manualmente.

**6. (Debug)** Um meta-agente gera agentes novos sem parar e o sistema degrada. Cite 2 riscos e 2 *fences* (guarda-corpos) estruturais.

**7. (Análise)** Por que um **meta-governor** (com poder de veto) é necessário em sistemas auto-evolutivos? O que falha sem ele?

**8. (Trade-off)** Estratégia *evolver* mantém memória de sucesso/falha. Dê 2 riscos de manter **tudo** e 1 estratégia de "esquecimento" saudável.

---

## Parte 3 — Projeto curto (Q9-10)

**9. (Projeto)** Escreva um "veto" (regra de segurança) para um meta-agente que proíbe auto-modificação do próprio código do meta-governor.

**10. (Projeto)** Descreva em 4 linhas o pipeline de um meta-agente que, dada uma tarefa, gera um agente especializado, o valida e só então faz deploy.

---

## Critérios de correção (resumo)

| Parte | Questões | Peso |
|---|---|---|
| Conceitos | 1, 2, 3, 4 | 40% |
| Aplicação/trade-off | 5, 6, 7, 8 | 40% |
| Projeto curto | 9,10 | 20% |

**Conversão**: cada questão vale 10 pts; total 100 pts → nota 1-5.
- 90+: 5,0 · 80-89: 4,5 · 70-79: 4,0 · 60-69: 3,5 · 50-59: 3,0 (mínimo) · <50: reprovação.

Gabarito comentado em [`gabarito.md`](gabarito.md).
