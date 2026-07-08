# ETHAGT01 — Quiz Final

> Quiz individual, sem consulta, 5 perguntas de múltipla escolha.
> Tempo estimado: 5 min
**Critério**: ≥3 acertos = compreensão básica atingida.

---

## Pergunta 1

Qual é o bloco fundamental de qualquer sistema agêntico segundo a Anthropic?

- A) Um framework como LangGraph
- B) O Augmented LLM (LLM + retrieval + tools + memory)
- C) Um prompt bem escrito
- D) Um modelo grande o suficiente

<details>
<summary>Resposta</summary>

**B) O Augmented LLM**

A Anthropic é explícita: "The basic building block of agentic systems is an LLM enhanced with augmentations such as retrieval, tools, and memory." Frameworks são instanciações, não o bloco. Prompt é importante mas não é o bloco. Modelo é necessário mas sem as augmentations não é agêntico.
</details>

---

## Pergunta 2

Em ReAct, o que força o "grounding" do modelo?

- A) O prompt do sistema
- B) A temperatura baixa
- C) A Observation (resultado real da tool)
- D) O max_steps

<details>
<summary>Resposta</summary>

**C) A Observation**

Grounding significa ancorar o raciocínio em fato real. A Observation é o resultado real da tool executada — não é alucinável. O prompt pode ser ignorado, a temperatura não garante correção, max_steps só limita iterações.
</details>

---

## Pergunta 3

Quando você DEVERIA usar um agente em vez de um workflow?

- A) Quando a tarefa tem passos predefinidos
- B) Quando você precisa de previsibilidade total
- C) Quando os passos são imprevisíveis e exigem flexibilidade
- D) Quando o custo precisa ser mínimo

<details>
<summary>Resposta</summary>

**C) Quando os passos são imprevisíveis e exigem flexibilidade**

Agentes são para problemas abertos onde não dá para predefinir o caminho. Se os passos são predefinidos (A), workflow. Se precisa de previsibilidade (B), workflow. Se custo é prioridade (D), workflow (mais barato). Agente é para flexibilidade (C).
</details>

---

## Pergunta 4

O que é ACI?

- A) Agent Communication Interface
- B) Agent-Computer Interface (design de tools)
- C) Automated Code Injection
- D) Agent Control Infrastructure

<details>
<summary>Resposta</summary>

**B) Agent-Computer Interface**

ACI = Agent-Computer Interface, análogo a HCI (Human-Computer Interface). É o design das tools — descrição, parâmetros, validação. A Anthropic dedica tanto esforço a ACI quanto a HCI. Poka-yoke suas tools.
</details>

---

## Pergunta 5

Qual é a PRIMEIRA coisa que você deve adicionar a um agente em produção?

- A) Um framework
- B) Múltiplas tools
- C) Observabilidade (logs estruturados + traces)
- D) HITL (Human-in-the-Loop)

<details>
<summary>Resposta</summary>

**C) Observabilidade (logs estruturados + traces)**

Sem observabilidade, você não pode debugar, medir custo, ou reproduzir bugs. Framework (A) é opcional. Múltiplas tools (B) vêm depois da observabilidade. HITL (D) é importante mas você precisa ver o que o agente faz antes de decidir onde intervir.
</details>

---

## Pergunta Bônus (não conta para nota)

Qual destes NÃO é um dos 5 workflows canônicos da Anthropic?

- A) Prompt Chaining
- B) Routing
- C) Reinforcement Learning
- D) Evaluator-Optimizer

<details>
<summary>Resposta</summary>

**C) Reinforcement Learning**

Os 5 workflows são: Prompt Chaining, Routing, Parallelization, Orchestrator-Workers, Evaluator-Optimizer. Reinforcement Learning é uma técnica de treinamento, não um padrão de workflow agêntico.
</details>

---

## Resultado

| Acertos | Avaliação |
|---|---|
| 5/5 | Excelente — compreensão completa |
| 4/5 | Bom — compreensão sólida, revisar 1 ponto |
| 3/5 | Suficiente — revisar 2 pontos |
| 2/5 | Insuficiente — reler Anthropic + ReAct |
| 0-1/5 | Crítico — agendar horário com professor |
