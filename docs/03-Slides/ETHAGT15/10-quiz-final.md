# ETHAGT15 — Quiz Final

> Quiz individual, sem consulta, 3 perguntas de múltipla escolha.
> Tempo estimado: 3 min
**Critério**: ≥2 acertos = compreensão básica atingida.

---

## Pergunta 1

Qual é a diferença fundamental entre um agente e um meta-agente?

- A) O meta-agente usa um modelo maior
- B) O meta-agente opera sobre agentes (seu ambiente é outro agente)
- C) O meta-agente tem mais tools
- D) O meta-agente é sempre mais rápido

<details>
<summary>Resposta</summary>

**B) O meta-agente opera sobre agentes**

A diferença não é tamanho, número de tools, ou velocidade. É o alvo da atuação: um agente comum age sobre o ambiente (APIs, dados, código); um meta-agente age sobre agentes (cria, configura, otimiza outros agentes). Essa mudança de alvo é o que define meta-agência.
</details>

---

## Pergunta 2

O que é goal drift?

- A) Agente muda de tarefa
- B) Agente otimiza uma métrica que diverge do objetivo real
- C) Agente esquece o objetivo original
- D) Agente muda de modelo

<details>
<summary>Resposta</summary>

**B) Agente otimiza uma métrica que diverge do objetivo real**

Goal drift acontece quando a métrica (usada como proxy do objetivo) diverge do objetivo real. O agente otimiza a métrica — que sobe — mas o objetivo real piora. Exemplo clássico: objetivo = "resolver tickets", métrica = "tickets fechados/hora" → agente fecha sem resolver. A causa raiz é que toda métrica é um proxy imperfeito.
</details>

---

## Pergunta 3

Qual é a PRIMEIRA camada de defesa em safety fences para mudanças auto-propostas?

- A) Canary deployment
- B) Shadow run
- C) Policy-as-code (vetos)
- D) Rollback automático

<details>
<summary>Resposta</summary>

**C) Policy-as-code (vetos)**

A primeira camada é policy-as-code — regras declarativas (vetos) que bloqueiam mudanças que violam políticas antes de qualquer teste. É o gate mais barato e mais rápido. Canary (A) e shadow run (B) vêm depois; rollback (D) é a última camada de emergência. A ordem é: policy → sandbox → shadow → canary → rollback.
</details>

---

## Pergunta Bônus (não conta para nota)

Qual destes papers NÃO é sobre meta-agência ou auto-aprendizado?

- A) DSPy (Khattab)
- B) Voyager (Wang)
- C) ReAct (Yao)
- D) Promptbreeder (Fernando)

<details>
<summary>Resposta</summary>

**C) ReAct (Yao)**

ReAct é sobre o padrão Thought/Action/Observation para agentes comuns (agência sobre ambiente). DSPy (otimização de prompts), Voyager (auto-aprendizado de skills) e Promptbreeder (evolução de prompts) são todos sobre meta-agência. ReAct é um pré-requisito — define o loop do agente que o meta-agente vai otimizar.
</details>

---

## Resultado

| Acertos | Avaliação |
|---|---|
| 3/3 | Excelente — compreensão completa |
| 2/3 | Bom — compreensão sólida, revisar 1 ponto |
| 1/3 | Insuficiente — revisar slides 8, 48 e 50 |
| 0/3 | Crítico — agendar horário com professor |
