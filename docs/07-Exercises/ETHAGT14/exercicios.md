# ETHAGT14 — Lista de Exercícios

> Curso: Escalabilidade & Sistemas Distribuídos de Agentes. Fixação de conceitos. Use a apostila `04-Apostilas/ETHAGT14/apostila.md` como referência.

## Múltipla escolha

**1. Em sistemas de agentes, o gargalo dominante de latência é tipicamente:**

a) O vector database
b) A chamada ao LLM
c) O logging
d) A rede interna

**2. Cache semântico difere do cache de prompt (exact match) porque:**

a) É mais lento
b) Usa similaridade de embedding para detectar queries semanticamente equivalentes, mesmo com wording diferente
c) Só funciona com modelos específicos
d) Não precisa de invalidação

**3. "Model routing" por complexidade significa:**

a) Usar sempre o modelo mais barato
b) Roteamento dinâmico entre modelos (ex.: Haiku para tarefas fáceis, Sonnet para difíceis) para otimizar custo/qualidade
c) Usar sempre o modelo mais potente
d) Roteamento geográfico

**4. Em FinOps de agentes, "orçamento por execução" significa:**

a) Limitar o custo total de uma única execução do agente (circuit breaker financeiro)
b) Pagar antecipadamente
c) Dividir custos entre clientes
d) Cachear respostas

## Verdadeiro ou Falso (justificado)

**1.** "Streaming reduz a latência total da resposta." — Justifique.

**2.** "Stateless workers são sempre preferíveis a stateful para escalabilidade." — Justifique.

**3.** "Cache semântico pode retornar respostas erradas se a similaridade de embedding enganar." — Justifique.

**4.** "Sharding por tenant isola dados e permite escala horizontal independente por cliente." — Justifique.

## Código curto

**1.** Escreva o pseudocódigo de um cache semântico: dada uma query, buscar por similaridade no cache; se hit (score > threshold), retornar cacheado.

**2.** Escreva o pseudocódigo de um orçamento por execução com circuit breaker: se custo acumulado > budget, parar e retornar erro.

**3.** Escreva o pseudocódigo de model routing: classificar complexidade → escolher modelo.

## Análise de trade-off

**1.** Compare cache de prompt (exact) vs. cache semântico. Quando o semântico falha?

**2.** Compare serverless vs. dedicado (Kubernetes) para hospedar agentes. Quando cada brilha?

**3.** Para reduzir custo em 40% sem perder qualidade, quais 3 otimizações você priorizaria?

## Debug / diagnóstico

**1.** Após adicionar cache semântico, usuários relatam respostas incorretas esporádicas. Diagnóstico e correção.

**2.** Um agente multi-tenant tem latência crescente conforme mais tenants são adicionados. Diagnóstico de gargalo e 2 soluções.
