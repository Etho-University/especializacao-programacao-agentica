# ETHAGT09 — Quiz Final

> Quiz individual, sem consulta, 4 perguntas de múltipla escolha.
> Tempo estimado: 4 min
**Critério**: ≥3 acertos = compreensão básica atingida.

---

## Pergunta 1

Quando blackboard é preferível a mensagens diretas?

- A) Quando há apenas 2 agentes
- B) Quando N é grande e contribuições são independentes
- C) Quando a ordem das mensagens é crítica
- D) Quando o acoplamento entre agentes deve ser máximo

<details>
<summary>Resposta</summary>

**B) Quando N é grande e contribuições são independentes**

Blackboard tem acoplamento baixo (O(N) conexões com o espaço compartilhado) vs mensagens diretas (O(N²)). Brilha quando muitos especialistas contribuem incrementalmente para um estado compartilhado. Se há apenas 2 agentes (A), mensagens diretas são mais simples. Se a ordem é crítica (C), mensagens diretas com sequenciamento são melhores.
</details>

---

## Pergunta 2

Qual é a diferença entre handoff (Swarm) e delegação (supervisor)?

- A) Handoff é síncrono, delegação é assíncrona
- B) Handoff transfere controle (agente sai), delegação mantém supervisor esperando retorno
- C) Handoff é para 2 agentes, delegação para N
- D) Não há diferença

<details>
<summary>Resposta</summary>

**B) Handoff transfere controle (agente sai), delegação mantém supervisor esperando retorno**

Handoff (Swarm) = "passa a bola" — o agente atual sai e o novo assume. Delegação (LangGraph supervisor) = "coloca em espera e consulta" — o supervisor delega e espera o retorno para continuar. A diferença não é sincronicidade (A) nem número de agentes (C), mas quem mantém o controle após a transferência.
</details>

---

## Pergunta 3

MCP e A2A Protocol são:

- A) Competidores — um substitui o outro
- B) Complementares — MCP é agent↔system, A2A é agent↔agent
- C) A mesma coisa com nomes diferentes
- D) Ambos obsoletos

<details>
<summary>Resposta</summary>

**B) Complementares — MCP é agent↔system, A2A é agent↔agent**

MCP (Model Context Protocol) conecta agentes a ferramentas e fontes de dados (agent↔system). A2A (Agent-to-Agent) conecta agentes entre si para delegação e colaboração (agent↔agent). São camadas complementares, não competidoras. Um agente pode usar MCP para acessar uma tool e A2A para delegar parte do trabalho a outro agente.
</details>

---

## Pergunta 4

Verdadeiro ou falso: "Actor model é mais lento que shared-state."

- A) Verdadeiro — locks são mais rápidos
- B) Falso — em alta concorrência, actor model escala melhor sem locks
- C) Depende — sempre (contexto importa)
- D) Impossível determinar sem benchmark

<details>
<summary>Resposta</summary>

**B) Falso — em alta concorrência, actor model escala melhor sem locks**

A afirmação geral é falsa. Shared state com locks sofre com deadlocks, race conditions e contenção de lock em alta concorrência. Actor model processa uma mensagem por ator por vez, sem locks, e escala horizontalmente. Há overhead de serialização de mensagens, mas em cenários de alta concorrência, actor model é mais eficiente. (Caveat: em cenários de baixa concorrência com operações simples, shared state pode ser mais rápido — mas a afirmação como enunciada é falsa.)
</details>

---

## Pergunta Bônus (não conta para nota)

Qual destes NÃO é um padrão de conversação multi-agente?

- A) Two-agent dialogue (CAMEL)
- B) Group chat (AutoGen)
- C) Handoff / transfer (Swarm)
- D) Reinforcement Learning

<details>
<summary>Resposta</summary>

**D) Reinforcement Learning**

Os 3 padrões de conversação são: Two-agent dialogue (CAMEL), Group chat (AutoGen), Handoff (Swarm). Reinforcement Learning é uma técnica de treinamento, não um padrão de conversação entre agentes.
</details>

---

## Resultado

| Acertos | Avaliação |
|---|---|
| 4/4 | Excelente — compreensão completa |
| 3/4 | Bom — compreensão sólida, revisar 1 ponto |
| 2/4 | Suficiente — revisar 2 pontos |
| 1/4 | Insuficiente — reler AutoGen + Swarm + blackboard |
| 0/4 | Crítico — agendar horário com professor |
