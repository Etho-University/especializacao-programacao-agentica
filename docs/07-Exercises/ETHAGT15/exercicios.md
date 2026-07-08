# ETHAGT15 — Lista de Exercícios

> Curso: Meta-Agentes & Sistemas Autoaprendentes. Fixação de conceitos. Use a apostila `04-Apostilas/ETHAGT15/apostila.md` como referência.

## Múltipla escolha

**1. Um "meta-agente" é definido como:**

a) Um modelo de embeddings
b) Um agente que opera sobre outros agentes — criando, otimizando ou evoluindo agentes especializados
c) Um vector database
d) Um protocolo de comunicação

**2. DSPy é uma framework que:**

a) Substitui LangGraph
b) Compila chamadas declarativas de LLM, otimizando prompts automaticamente
c) É um vector database
d) É um benchmark

**3. "Goal drift" em sistemas autoaprendentes significa:**

a) O agente fica mais rápido
b) Os objetivos do agente se desviam do objetivo original ao longo do tempo, por auto-modificação ou aprendizado
c) O agente para de funcionar
d) O custo diminui

**4. O padrão "meta-governor" serve para:**

a) Acelerar o agente
b) Supervisionar e vetar ações de meta-agentes que possam ser perigosas (segurança)
c) Indexar documentos
d) Fazer cache

## Verdadeiro ou Falso (justificado)

**1.** "Auto-aprendizado contínuo sempre melhora o desempenho do agente." — Justifique.

**2.** "Otimização automatizada de prompts (ex.: DSPy) é melhor que reescrita manual quando há um benchmark claro e automatizado." — Justifique.

**3.** "Recursão descontrolada em meta-agentes é um risco real que exige fences de segurança." — Justifique.

**4.** "Todo agente gerado por um meta-agente deve ser avaliado (eval) antes de deploy." — Justifique.

## Código curto

**1.** Escreva o pseudocódigo de um meta-agente que, dada uma tarefa, gera um prompt de agente especializado e o avalia em um benchmark.

**2.** Escreva um "veto" (policy) para um meta-governor que bloqueia agentes gerados que tentem modificar suas próprias instruções.

**3.** Escreva o pseudocódigo de uma strategy evolver: mantém N estratégias, testa todas, mantém as top-k, descarta as demais.

## Análise de trade-off

**1.** Compare otimização manual de prompts vs. automatizada (DSPy). Quando cada é preferível?

**2.** Compare auto-aprendizado contínuo vs. aprendizado supervisionado periódico. Riscos de cada?

**3.** Para um sistema que cria agentes especializados por domínio, quando confiança incremental (sandbox → produção) é necessária?

## Debug / diagnóstico

**1.** Um sistema com otimização automatizada de prompts via DSPy melhora no benchmark mas piora em produção. Diagnóstico provável.

**2.** Um meta-agente começa a gerar agentes cada vez mais complexos sem melhoria de desempenho. Diagnóstico e correção.
