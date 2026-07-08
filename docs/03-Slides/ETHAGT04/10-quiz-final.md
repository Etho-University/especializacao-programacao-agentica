# ETHAGT04 — Quiz Final

> Quiz individual, sem consulta, 5 perguntas de múltipla escolha.
> Tempo estimado: 5 min
**Critério**: ≥3 acertos = compreensão básica atingida.

---

## Pergunta 1

Qual é a diferença fundamental entre Chain-of-Thought (CoT) e Tree of Thoughts (ToT)?

- A) CoT usa prompt; ToT usa fine-tuning
- B) CoT é linear (uma cadeia); ToT é uma árvore com ramificação, avaliação e poda
- C) CoT funciona com qualquer modelo; ToT só com GPT-4
- D) ToT é sempre mais barato que CoT

<details>
<summary>Resposta</summary>

**B) CoT é linear; ToT é uma árvore com ramificação, avaliação e poda**

CoT gera uma única cadeia de pensamento (linear, sem backtracking). ToT generaliza para uma árvore: cada nó é um "estado de pensamento", o modelo avalia múltiplos estados, explora os promissores e poda os fracos. Isso permite voltar e tentar outro caminho — impossível no CoT linear.

</details>

---

## Pergunta 2

Por que ReWOO reduz custo em comparação com ReAct?

- A) ReWOO usa modelos menores
- B) ReWOO não reenvia o contexto acumulado a cada chamada de tool
- C) ReWOO não usa tools
- D) ReWOO usa cache de respostas

<details>
<summary>Resposta</summary>

**B) ReWOO não reenvia o contexto acumulado a cada chamada de tool**

Em ReAct, cada chamada de LLM recebe TODO o histórico (todas as thoughts, actions e observations anteriores). O input cresce linearmente com os steps. ReWOO separa planejamento de execução: o planner gera um plano com variáveis de evidência (#E1, #E2...) uma vez, os workers executam em paralelo (cada um recebe só sua sub-tarefa), e o solver substitui as variáveis no final. Sem reenvio de histórico acumulado.

</details>

---

## Pergunta 3

O que diferencia Reflexion de um simples "reflection pattern" (criticar e reescrever)?

- A) Reflexion usa um modelo diferente para criticar
- B) Reflexion mantém memória episódica de reflexões entre tentativas, acumulando aprendizado
- C) Reflexion é mais rápido
- D) Reflexion só funciona com GPT-4

<details>
<summary>Resposta</summary>

**B) Reflexion mantém memória episódica de reflexões entre tentativas**

Um reflection pattern simples critica e reescreve na mesma sessão (uma rodada de gerar → criticar → reescrever). Reflexion é iterativo e com memória: a cada tentativa falha, o agente gera uma reflexão verbal sobre o erro, armazena na memória episódica, e a próxima tentativa recebe TODAS as reflexões anteriores. É "reinforcement learning verbal" — aprende com falhas acumuladas.

</details>

---

## Pergunta 4

Quando um modelo de reasoning nativo (o1, o3, Claude com extended thinking) NÃO substitui Tree of Thoughts?

- A) Nunca — reasoning nativo sempre substitui ToT
- B) Quando se precisa de transparência/auditorabilidade do processo de raciocínio
- C) Quando o problema é muito simples
- D) Quando se usa LangGraph

<details>
<summary>Resposta</summary>

**B) Quando se precisa de transparência/auditorabilidade do processo de raciocínio**

Reasoning models nativos raciocinam internamente (hidden chain of thought) — você vê o resultado, mas não o processo detalhado de busca. ToT deixa a árvore de busca explícita e observável: você vê quais caminhos foram explorados, quais foram podados e por quê. Para compliance, debug e auditoria, essa transparência é insubstituível. ToT também vale quando é preciso integrar tools durante a busca (cada nó pode chamar uma tool).

</details>

---

## Pergunta 5

Qual é o trade-off principal ao usar Self-Consistency com N=20 amostras?

- A) Maior latência — as 20 amostras são sequenciais
- B) Maior custo (20 chamadas) e latência, em troca de maior robustez estatística
- C) Menor accuracy — muitas amostras confundem o modelo
- D) Self-Consistency não funciona com N > 5

<details>
<summary>Resposta</summary>

**B) Maior custo (20 chamadas) e latência, em troca de maior robustez estatística**

Self-Consistency amostra N cadeias de pensamento (com temperatura > 0) e faz votação da maioria. Mais amostras = maior robustez (a resposta consensual é mais confiável). Mas o custo escala linearmente (N chamadas) e a latência também (a menos que sejam paralelizáveis). N=20 custa 20x mais que CoT simples. O ganho de accuracy tem retornos decrescentes: saltar de N=5 para N=20 pode dar +2-3% de accuracy por um custo 4x maior.

</details>

---

## Pergunta Bônus (não conta para nota)

Qual destas técnicas compõe sua PRÓPRIA estratégia de raciocínio a partir de primitivas (CoT, decomposição, analogia)?

- A) Reflexion
- B) ReWOO
- C) Self-Discover
- D) LATS

<details>
<summary>Resposta</summary>

**C) Self-Discover**

Self-Discover tem 3 fases: (1) Select — o LLM escolhe primitivas de raciocínio de um catálogo (CoT, decomposição, pensamento crítico, analogia); (2) Adapt — adapta as primitivas ao problema específico; (3) Implement — compõe um reasoning module final. É a única técnica onde o agente constrói sua própria estratégia em vez de usar uma fixa.

</details>

---

## Resultado

| Acertos | Avaliação |
|---|---|
| 5/5 | Excelente — compreensão completa do espectro de raciocínio |
| 4/5 | Bom — compreensão sólida, revisar 1 técnica |
| 3/5 | Suficiente — revisar 2 técnicas |
| 2/5 | Insuficiente — reler papers de CoT, ToT e Reflexion |
| 0-1/5 | Crítico — agendar horário com professor; revisar ETHAGT01/03 |
