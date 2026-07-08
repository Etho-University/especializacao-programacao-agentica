# ETHAGT05 — Quiz Final

> Quiz individual, sem consulta, 5 perguntas de múltipla escolha.
> Tempo estimado: 5 min
**Critério**: ≥3 acertos = compreensão básica atingida.

---

## Pergunta 1

Qual tipo de memória é mais apropriado para armazenar "o usuário prefere respostas em português"?

- A) Working memory (context window)
- B) Memória episódica (vector DB)
- C) Memória semântica (KB / perfil)
- D) Memória procedural (skills)

<details>
<summary>Resposta</summary>

**C) Memória semântica (KB / perfil)**

"Prefere português" é um fato estável sobre o usuário — não é um evento (episódica), não é uma skill (procedural), e não deve ser re-promptado a cada sessão (working). Semântica armazena "o que é verdade" sobre o mundo/usuário. A memória semântica permite que o agente saiba disso em qualquer sessão sem re-perguntar.
</details>

---

## Pergunta 2

O que acontece se o schema de estado mudar (novo campo adicionado) e um checkpoint antigo for carregado via resume?

- A) Erro 500 e crash do agente
- B) O agente ignora campos novos e continua normalmente
- C) Depende — sem versionamento, pode quebrar; com migração lazy, funciona
- D) O checkpointer reescreve o estado automaticamente

<details>
<summary>Resposta</summary>

**C) Depende — sem versionamento, pode quebrar; com migração lazy, funciona**

Sem versionamento explícito, campos novos podem causar erros (KeyError, TypeError) quando o código espera o campo mas o checkpoint antigo não tem. Com `schema_version` no estado + migração lazy (converter no load), o estado antigo é convertido para o novo schema e funciona. Boa prática: sempre versionar o schema de estado.
</details>

---

## Pergunta 3

O usuário pede: "Lembra daquela conversa sobre deploy na semana passada?" Qual estratégia de recall é mais adequada?

- A) Apenas vector search (similaridade semântica com "deploy")
- B) Apenas metadata filter (timestamp da semana passada)
- C) Metadata filter (tempo) + vector search (tópico) + re-ranking
- D) Sumarização em cascata

<details>
<summary>Resposta</summary>

**C) Metadata filter (tempo) + vector search (tópico) + re-ranking**

A query tem dois componentes: temporal ("semana passada") e semântico ("deploy"). Metadata filter reduz o universo temporal; vector search recupera por similaridade semântica dentro desse universo; re-ranking melhora a precisão dos top-K. Usar só vector (A) retorna conversas sobre deploy de qualquer época; só metadata (B) retorna qualquer conversa da semana, não só sobre deploy. Sumarização (D) é estratégia de gestão de contexto, não de recall.
</details>

---

## Pergunta 4

Qual é a analogia central do MemGPT (Packer et al., arXiv:2310.08560)?

- A) Agentes como neurônios em uma rede neural
- B) LLMs como sistemas operacionais (context window = RAM, memória persistente = disco)
- C) Memória de agentes como banco de dados relacional
- D) Checkpointer como sistema de versionamento (git)

<details>
<summary>Resposta</summary>

**B) LLMs como sistemas operacionais (context window = RAM, memória persistente = disco)**

MemGPT propõe que o LLM atue como um sistema operacional: a context window é a RAM (limitada, rápida), a memória persistente é o disco (ilimitada, lenta), e o modelo gerencia sua própria memória com page-in/page-out (self-editing memory). Esta analogia inspirou Zep, A-MEM e Letta.
</details>

---

## Pergunta 5

Em qual destes casos uma memória VETORIAL é PIOR que uma relacional?

- A) "Algo sobre deploy que conversamos semana passada"
- B) "Qual o saldo atual da conta do usuário X?"
- C) "Documentação sobre a API de pagamento"
- D) "Lembrete de tarefas que combinamos"

<details>
<summary>Resposta</summary>

**B) "Qual o saldo atual da conta do usuário X?"**

Saldo é um fato transacional — muda constantemente e precisa ser exato. Vector DB é otimizado para similaridade semântica (fuzzy), não para exact match ou valores transacionais. A query correta é SQL: `SELECT saldo FROM contas WHERE user_id = X`. Vector DB seria lento, impreciso e potencialmente desatualizado. Os outros casos (A, C, D) são recall semântico — bons para vector DB.
</details>

---

## Pergunta Bônus (não conta para nota)

Qual é a fórmula de recall de Generative Agents (Park et al., arXiv:2304.03442)?

- A) `score = relevance × frequency`
- B) `score = α·recency + β·importance + γ·relevance`
- C) `score = tf-idf × cosine_similarity`
- D) `score = recency × importance`

<details>
<summary>Resposta</summary>

**B) `score = α·recency + β·importance + γ·relevance`**

Generative Agents combinam três fatores ponderados: recency (quão recente é a memória, com decaimento exponencial), importance (salience/valor da observação, atribuído pelo modelo), e relevance (similaridade com a situação atual). Os pesos α, β, γ são calibrados por contexto. Esta fórmula inspira sistemas de eviction modernos.
</details>

---

## Resultado

| Acertos | Avaliação |
|---|---|
| 5/5 | Excelente — compreensão completa das 4 camadas e estratégias |
| 4/5 | Bom — compreensão sólida, revisar 1 ponto |
| 3/5 | Suficiente — revisar 2 pontos (provavelmente recall ou schema versioning) |
| 2/5 | Insuficiente — reler MemGPT + Generative Agents + LangGraph docs |
| 0-1/5 | Crítico — agendar horário com professor; rever ETHAGT03 (StateGraph) |
