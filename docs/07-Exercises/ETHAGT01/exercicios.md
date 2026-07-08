# ETHAGT01 — Lista de Exercícios

> Curso: Arquitetura Cognitiva de Agentes LLM. Fixação de conceitos. Use a apostila `04-Apostilas/ETHAGT01/apostila.md` como referência.

## Múltipla escolha

**1. Segundo a definição operacional adotada na apostila, qual é a unidade central de um agente?**

a) A função de custo do LLM
b) O agent loop: raciocinar → agir → observar → repetir
c) O prompt template
d) O vector database

**2. No bloco fundamental "Augmented LLM" de Anthropic, quais são as componentes?**

a) LLM + retrieval + tools + memory
b) LLM + fine-tuning + RAG + guardrails
c) LLM + chain-of-thought + embeddings + cache
d) LLM + agents + workflows + orchestration

**3. Na distinção canônica de Anthropic, a diferença entre workflow e agente é:**

a) Workflows usam modelos menores; agentes usam modelos maiores
b) Workflows têm caminhos de código predefinidos; agentes têm o LLM dirigindo o fluxo
c) Workflows são mais caros; agentes são mais baratos
d) Workflows não usam tools; agentes sempre usam tools

**4. Qual é uma limitação conhecida do padrão ReAct?**

a) Não consegue usar ferramentas
b) Pode entrar em loops, com custo crescente e alucinação em ação
c) Exige fine-tuning do modelo
d) Só funciona com modelos proprietários

## Verdadeiro ou Falso (justificado)

**1.** "Toda aplicação de LLM deveria ser um agente." — Justifique em 1-2 frases.

**2.** "No padrão ReAct, a observação do ambiente atua como mecanismo de grounding." — Justifique.

**3.** "Adicionar mais ferramentas a um agente sempre melhora seu desempenho." — Justifique.

**4.** "Observabilidade (logs estruturados, traces) é opcional na fase de protótipo e pode ser adicionada depois." — Justifique.

## Código curto

**1.** Escreva o esqueleto de um agent loop ReAct em Python puro (~10-15 linhas) que alterna entre `llm_generate()`, `execute_tool()` e `observe()`, com condição de parada.

**2.** Escreva um log estruturado (dict/JSON) para um único ciclo Thought → Action → Observation, incluindo timestamp e tipo de evento.

**3.** Escreva a descrição de uma tool `calculate(expression: str)` seguindo princípios de ACI (clareza, exemplos de formato, bordas).

## Análise de trade-off

**1.** Compare implementar um agente em Python puro vs. usar um framework (LangGraph). Quando escolher cada abordagem?

**2.** Compare responder diretamente a uma pergunta factual vs. recuperar de uma base local vs. usar uma tool de busca. Quais fatores o agente deve considerar ao decidir?

**3.** "Comece simples, só aumente a complexidade com evidência." — Por que essa é a recomendação de Anthropic? O que acontece se você violar esse princípio?

## Debug / diagnóstico

**1.** Dado o trace abaixo, identifique o problema e proponha 2 correções:

```
Thought: Preciso buscar o preço do produto
Action: search_price("laptop")
Observation: Preço não encontrado
Thought: Preciso buscar o preço do produto
Action: search_price("laptop")
Observation: Preço não encontrado
Thought: Preciso buscar o preço do produto
...
```

**2.** Um agente ReAct recebe a resposta correta de uma tool, mas a ignora e repete a mesma ação. Liste 2 hipóteses de causa raiz.
