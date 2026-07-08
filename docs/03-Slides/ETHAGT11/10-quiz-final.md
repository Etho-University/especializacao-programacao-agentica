# ETHAGT11 — Quiz Final

> Quiz individual, sem consulta, 5 perguntas de múltipla escolha.
> Tempo estimado: 5 min
**Critério**: ≥3 acertos = compreensão básica atingida.

---

## Pergunta 1

Quando Temporal é preferível a Kafka puro para orquestração de agentes?

- A) Quando você precisa de máximo throughput de mensagens
- B) Quando você precisa de durable execution, HITL e orquestração de workflow
- C) Quando você quer o broker mais leve
- D) Quando você não precisa de ordering

<details>
<summary>Resposta</summary>

**B) Quando você precisa de durable execution, HITL e orquestração de workflow**

Temporal oferece durable execution (sobreviver a crashes sem perder progresso), HITL via timers/signals (pausar para aprovação humana), e orquestração de workflow (sequência de passos com retries). Kafka é mensageria — infraestrutura de comunicação. Não são mutuamente exclusivos: você pode usar Kafka para eventos e Temporal para orquestração. A (throughput) é força do Kafka. C (leveza) é NATS. D é irrelevante.
</details>

---

## Pergunta 2

Em Kafka, como garantir ordering de mensagens do mesmo agente?

- A) Usar ordering global (já vem por padrão)
- B) Usar a mesma chave de partição (agent_id)
- C) Aumentar o número de partições
- D) Usar RabbitMQ no lugar

<details>
<summary>Resposta</summary>

**B) Usar a mesma chave de partição (agent_id)**

Kafka garante ordering **dentro** de uma partição, não global. Ao usar agent_id como key, o Kafka aplica `hash(key) % num_partitions` — todas as mensagens do mesmo agente vão para a mesma partição, preservando a ordem. A é falso (não há ordering global). C (mais partições) não ajuda — pode piorar se a key não for usada. D é trocar de ferramenta, não resolver o problema.
</details>

---

## Pergunta 3

O que quebra um replay no Temporal?

- A) Usar `workflow.sleep()` no workflow
- B) Non-determinism (I/O direto, datetime.now(), random no workflow)
- C) Chamar activities
- D) Usar signals para receber input externo

<details>
<summary>Resposta</summary>

**B) Non-determinism (I/O direto, datetime.now(), random no workflow)**

O replay re-executa o código do workflow esperando que produza a mesma sequência de chamadas de activities do histórico. Se o workflow usa `datetime.now()` (valor diferente a cada replay), `random()` (resultado diferente), ou I/O direto (estado externo mudou), a sequência diverge e o replay falha. A (`workflow.sleep()`) é determinístico e seguro. C (activities) é o uso correto — activities são gravadas no histórico. D (signals) são suportados no replay.
</details>

---

## Pergunta 4

Qual é a estratégia prática para alcançar "effectively once" processing?

- A) Implementar exactly-once delivery no broker
- B) At-least-once delivery + idempotência no consumidor
- C) At-most-once delivery + retry infinito
- D) Usar transações distribuídas (two-phase commit)

<details>
<summary>Resposta</summary>

**B) At-least-once delivery + idempotência no consumidor**

Exactly-once delivery verdadeiro é impossível na presença de falhas (o ACK pode falhar). A prática consagrada é: at-least-once delivery (o broker pode entregar a mesma mensagem mais de uma vez) + idempotência no consumidor (processar 2x = processar 1x). O resultado é "effectively once" — cada mensagem causa efeito exatamente uma vez. A é impossível. C perde mensagens. D (2PC) é caro, frágil e bloqueia recursos.
</details>

---

## Pergunta 5

Em uma saga de transferência entre contas (debita A → credita B → notifica), se o passo "notificar" falha, o que se faz?

- A) Nada — a transferência já foi feita com sucesso
- B) Compensar os passos anteriores (estornar crédito em B e débito em A)
- C) Retentar infinitamente até que a notificação seja enviada
- D) Cancelar a transação via two-phase commit (2PC)

<details>
<summary>Resposta</summary>

**B) Compensar os passos anteriores (estornar crédito em B e débito em A)**

Saga compensatória: se o passo N falha, executam-se as compensações dos passos 1..N-1 em ordem reversa. Se "notificar" falha: estornar crédito em B (compensação do passo 2) e devolver débito em A (compensação do passo 1). O usuário não foi notificado, mas o dinheiro voltou ao estado original. A está errado — deixa o sistema inconsistente. C é retry infinito (pode travar indefinidamente). D (2PC) não é como saga funciona — saga é transações locais com compensação.
</details>

---

## Pergunta Bônus (não conta para nota)

Qual destes NÃO é um estado do padrão Circuit Breaker?

- A) CLOSED (normal)
- B) OPEN (rejeitando chamadas)
- C) HALF-OPEN (testando recuperação)
- D) PENDING (aguardando confirmação)

<details>
<summary>Resposta</summary>

**D) PENDING (aguardando confirmação)**

Os 3 estados do Circuit Breaker são: CLOSED (normal, chamadas passam), OPEN (após N falhas consecutivas, todas rejeitadas imediatamente), e HALF-OPEN (após cooldown, uma chamada de teste é permitida — se sucesso, volta a CLOSED; se falha, volta a OPEN). PENDING não existe no padrão Circuit Breaker.
</details>

---

## Resultado

| Acertos | Avaliação |
|---|---|
| 5/5 | Excelente — compreensão completa |
| 4/5 | Bom — compreensão sólida, revisar 1 ponto |
| 3/5 | Suficiente — revisar 2 pontos |
| 2/5 | Insuficiente — reler Temporal primer + Kafka docs |
| 0-1/5 | Crítico — agendar horário com professor |
