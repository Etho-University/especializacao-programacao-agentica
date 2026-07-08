# ETHAGT10 — Quiz Final

> Quiz individual, sem consulta, 3 perguntas de múltipla escolha (versão aula) + 5 perguntas (versão completa).
> Tempo estimado: 3-5 min
**Critério**: ≥2 acertos (versão aula) ou ≥3 acertos (versão completa) = compreensão básica.

---

## Versão Aula (3 perguntas — Slide 60)

### Pergunta 1

Qual topologia NÃO tem orquestrador central?

- A) Supervisor
- B) Hierarchical
- C) Swarm
- D) Pipeline

<details>
<summary>Resposta</summary>

**C) Swarm**

Swarm é descentralizado: agentes se transferem controle via handoffs, sem autoridade central. Supervisor (A), hierarchical (B) e pipeline (D) têm controle central (supervisor, top supervisor, ou código que orquestra a sequência).
</details>

---

### Pergunta 2

Em LangGraph, o supervisor roteia para workers via:

- A) Mensagens de evento
- B) Tool calls
- C) Handoffs
- D) Mailbox

<details>
<summary>Resposta</summary>

**B) Tool calls**

Em LangGraph, cada worker é exposto como uma tool no supervisor. O supervisor é um agente ReAct com `bind_tools([worker_a, worker_b, ...])`. O supervisor decide qual tool (worker) chamar, como qualquer agente ReAct decide qual função chamar.
</details>

---

### Pergunta 3

Recursive é anti-pattern quando:

- A) O problema se decompõe naturalmente
- B) max_depth não está definido
- C) Sub-tarefas são distintas
- D) A profundidade é 1

<details>
<summary>Resposta</summary>

**B) max_depth não está definido**

Recursive sem max_depth é anti-pattern: profundidade incontrolável, custo explode, latência inaceitável. Com max_depth definido (A, C, D são condições favoráveis), recursive é adaptativo e útil.
</details>

---

## Versão Completa (5 perguntas — para casa/avaliação)

### Pergunta 4

Qual é a diferença entre orchestrator-workers e supervisor?

- A) Não há diferença; são sinônimos
- B) Orchestrator particiona uma tarefa em sub-tarefas; supervisor roteia a tarefa inteira
- C) Supervisor é hierárquico; orchestrator é flat
- D) Orchestrator usa tool calls; supervisor usa handoffs

<details>
<summary>Resposta</summary>

**B) Orchestrator particiona uma tarefa em sub-tarefas; supervisor roteia a tarefa inteira**

O orchestrator pega UMA tarefa, a divide em sub-tarefas distintas, delega cada uma para um worker, e sintetiza. O supervisor roteia a tarefa inteira para um worker escolhido. A distinção vem da Anthropic (Building Effective Agents, 2024).
</details>

---

### Pergunta 5

"Mesh é sempre a topologia mais escalável." Esta afirmação é:

- A) Verdadeira — mesh não tem ponto de falha
- B) Falsa — conexões crescem O(N²), hierarchical é O(N)
- C) Verdadeira — mesh permite paralelismo total
- D) Falsa — swarm é sempre mais escalável que mesh

<details>
<summary>Resposta</summary>

**B) Falsa — conexões crescem O(N²), hierarchical é O(N)**

Mesh escala bem para poucos agentes altamente colaborativos. Mas o número de conexões cresce quadraticamente: 10 agentes = 100 conexões, 100 agentes = 10.000. Hierarchical escala linearmente (estrutura de árvore é O(N)). Para muitos agentes, hierarchical é mais escalável.
</details>

---

## Pergunta Bônus (não conta para nota)

Qual topologia MetaGPT usa para simular uma software house?

- A) Swarm puro
- B) Pipeline puro
- C) Hierarchical com SOPs (pipeline + hierarchical)
- D) Agent Mesh

<details>
<summary>Resposta</summary>

**C) Hierarchical com SOPs (pipeline + hierarchical)**

MetaGPT combina hierarchical (papéis em hierarquia: PM → Architect → Engineer → QA) com pipeline (artefatos fluem: PRD → design doc → código → testes). As SOPs (Standard Operating Procedures) codificam o fluxo. É um exemplo de hybrid na prática. Fonte: arXiv:2308.00352.
</details>

---

## Resultado

### Versão Aula (3 perguntas)

| Acertos | Avaliação |
|---|---|
| 3/3 | Excelente — compreensão completa |
| 2/3 | Suficiente — revisar 1 ponto |
| 0-1/3 | Insuficiente — reler MetaGPT + LangGraph multi-agent |

### Versão Completa (5 perguntas)

| Acertos | Avaliação |
|---|---|
| 5/5 | Excelente — compreensão completa das topologias |
| 4/5 | Bom — compreensão sólida, revisar 1 ponto |
| 3/5 | Suficiente — revisar 2 pontos |
| 2/5 | Insuficiente — reler catálogo de 12 topologias |
| 0-1/5 | Crítico — agendar horário com professor |
