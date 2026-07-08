# ETHAGT03 — Quiz Final

> Quiz individual, sem consulta, 4 perguntas de múltipla escolha.
> Tempo estimado: 4 min
> **Critério**: ≥3 acertos = compreensão básica atingida.

---

## Pergunta 1

Qual é a diferença fundamental entre parallelization e orchestrator-workers?

- A) Orchestrator-workers é mais rápido porque paraleliza tudo
- B) Parallelization usa modelos menores e orchestrator usa modelos maiores
- C) Em orchestrator-workers, as subtarefas são dinâmicas (definidas em runtime pelo orquestrador)
- D) Parallelization não tem reducer/sintetizador

<details>
<summary>Resposta</summary>

**C) Em orchestrator-workers, as subtarefas são dinâmicas**

A distinção crítica: em parallelization, as subtarefas são fixas e conhecidas a priori (você escreve N funções). Em orchestrator-workers, as subtarefas emergem do input — um LLM orquestrador olha a tarefa e decide quantos workers e quais. Se as subtarefas são fixas, parallelization é mais simples, barato e previsível. A é falso (orchestrator é geralmente mais lento por ter step de planejamento serial). B é falso (ambos podem usar qualquer modelo). D é falso (ambos têm reducer).
</details>

---

## Pergunta 2

O que é um gate em prompt chaining?

- A) Um modelo LLM que decide se a cadeia deve continuar
- B) Um checkpoint programático (código determinístico) que valida a saída antes do próximo step
- C) Um tipo especial de prompt que bloqueia entradas inválidas
- D) Um framework de orquestração para encadear LLMs

<details>
<summary>Resposta</summary>

**B) Um checkpoint programático (código determinístico)**

Gate é CÓDIGO PURO (if/else, regex, schema validation), não LLM. Sua função é validar estruturalmente a saída de um step antes de passar para o próximo. Se fosse LLM, seria evaluator-optimizer (loop gerar-avaliar-refinar), não prompt chaining (cadeia com checkpoints). A é a armadilha clássica — alunos confundem gate com evaluator. A determinidade é o ponto: gates são previsíveis, LLMs não.
</details>

---

## Pergunta 3

Quando o evaluator-optimizer NÃO vale a pena?

- A) Quando o feedback é articulável e o LLM consegue avaliar
- B) Quando o evaluator não é melhor que o generator
- C) Quando há orçamento para múltiplas iterações
- D) Quando a tarefa tem critérios objetivos e mensuráveis

<details>
<summary>Resposta</summary>

**B) Quando o evaluator não é melhor que o generator**

Se o evaluator é mais fraco que o generator, o feedback é pior que a saída original. O loop diverge — cada iteração piora em vez de melhorar. As outras opções descrevem situações em que o evaluator-optimizer VALE a pena: A (feedback articulável), C (orçamento disponível), D (critérios objetivos). A regra: só use evaluator-optimizer quando (1) o feedback é articulável, (2) o LLM consegue avaliar, e (3) o evaluator é melhor que o generator.
</details>

---

## Pergunta 4

Em routing por modelo (Haiku para fácil, Sonnet para difícil), qual é o erro mais caro?

- A) Enviar tarefa fácil para modelo forte (Sonnet) — desperdiça capacidade
- B) Enviar tarefa difícil para modelo fraco (Haiku) — gera resposta ruim
- C) Usar o mesmo modelo para todas as categorias — perde a vantagem do routing
- D) Ter apenas 2 categorias em vez de 5 — granularidade insuficiente

<details>
<summary>Resposta</summary>

**B) Enviar tarefa difícil para modelo fraco (Haiku)**

O erro mais caro em routing por modelo é o falso negativo: classificar uma tarefa difícil como fácil e enviá-la para Haiku. Resultado: resposta ruim para o usuário. A (fácil→difícil) é apenas ineficiência — custa mais (Sonnet é caro) mas a resposta é boa. B (difícil→fácil) prejudica qualidade, que é geralmente mais caro em sistemas de produção (churn, reclamações, perda de confiança). A mitigação: quando o router está incerto, despachar para o path robusto (Sonnet).
</details>

---

## Pergunta Bônus (não conta para nota)

Qual destes NÃO é um sinal de que você está forçando workflow em um problema que pede agente?

- A) O número de branches no routing cresce sem parar
- B) Você adiciona gates cada vez mais complexos para cobrir edge cases
- C) O workflow tem exatamente 3 steps lineares e funciona bem
- D) Você precisa de "loops dentro de loops" para cobrir casos especiais

<details>
<summary>Resposta</summary>

**C) O workflow tem exatamente 3 steps lineares e funciona bem**

Se o workflow tem poucos steps, é linear, e funciona bem, isso é um SINAL DE SUCESSO — o problema pede workflow, não agente. Os outros (A, B, D) são sinais de alerta de que a complexidade do problema está excedendo a capacidade do workflow e um agente seria mais adequado. A regra: comece simples (workflow). Só migre para agente quando os sinais de alerta aparecem com evidência.
</details>

---

## Resultado

| Acertos | Avaliação |
|---|---|
| 4/4 | Excelente — compreensão completa dos 5 padrões |
| 3/4 | Bom — compreensão sólida, revisar 1 ponto |
| 2/4 | Suficiente — revisar 2 pontos (provavelmente gates e routing) |
| 1/4 | Insuficiente — reler Anthropic Building Effective Agents |
| 0/4 | Crítico — agendar horário com professor |
