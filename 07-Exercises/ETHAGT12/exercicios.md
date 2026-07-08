# ETHAGT12 — Lista de Exercícios

> Curso: AgentOps, Observabilidade & Avaliação. Fixação de conceitos. Use a apostila `04-Apostilas/ETHAGT12/apostila.md` como referência.

## Múltipla escolha

**1. No contexto de observabilidade de agentes, um "span" representa:**

a) Um tipo de vector database
b) Uma unidade de trabalho dentro de um trace (ex.: uma chamada de LLM, uma tool)
c) Um log de erro
d) Um benchmark

**2. Qual é um viés comum do LLM-as-judge?**

a) Preferir respostas mais longas (verbosity bias)
b) Preferir respostas em inglês
c) Preferir respostas curtas
d) Todas as anteriores são vieses possíveis

**3. O benchmark τ-bench (tau-bench) avalia:**

a) Geração de código
b) Tool-agent-user interaction em domínios (airline, retail)
c) Navegação web
d) Raciocínio matemático

**4. "Golden cases" em um pipeline de avaliação são:**

a) Casos de teste de produção
b) Casos de teste com resposta esperada conhecida, usados para detectar regressão
c) Cases de prompt injection
d) Logs de traces

## Verdadeiro ou Falso (justificado)

**1.** "Bom score em benchmark garante bom desempenho em produção." — Justifique.

**2.** "Contaminação de benchmark (dados de teste no treino) infla resultados artificialmente." — Justifique.

**3.** "LLM-as-judge deve sempre ser calibrado contra avaliação humana para verificar confiabilidade." — Justifique.

**4.** "Observabilidade tem custo — traces e logs consomem armazenamento e processamento." — Justifique.

## Código curto

**1.** Escreva um "golden case" (JSON) com pergunta, resposta esperada, e critério de sucesso mensurável.

**2.** Escreva o pseudocódigo de um pipeline de avaliação: rodar agente em N golden cases → calcular success rate → comparar com baseline.

**3.** Escreva o pseudocódigo de um LLM-as-judge: dado output e critérios, retorna score 0-1 com justificativa.

## Análise de trade-off

**1.** Compare SWE-bench vs. benchmark custom. Quando usar cada?

**2.** Compare observabilidade via traces (LangSmith/Phoenix) vs. logs estruturados simples. Quando o overhead de traces vale a pena?

**3.** Compare success rate (binário) vs. partial credit. Quando partial credit é mais informativo?

## Debug / diagnóstico

**1.** Após mudar o system prompt, o success rate caiu de 85% para 70%. Como investigar quais casos regrediram e por quê?

**2.** Um LLM-as-judge concorda com humanos em 95% dos casos fáceis mas só em 40% dos difíceis. Diagnóstico e correção.
