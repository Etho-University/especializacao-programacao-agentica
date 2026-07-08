# ETHAGT14 — Quiz Final

> Quiz individual, sem consulta, 3 perguntas de múltipla escolha.
> Tempo estimado: 3 min
**Critério**: ≥2 acertos = compreensão básica atingida.

---

## Pergunta 1

Qual é a PRIMEIRA otimização que você deve aplicar a um agente em produção?

- A) Fine-tuning do modelo para o domínio
- B) Multi-region deployment para reduzir latência global
- C) Caching (semântico + exact match)
- D) Speculative decoding para reduzir latência de geração

<details>
<summary>Resposta</summary>

**C) Caching (semântico + exact match)**

Caching tem o maior ROI de todas as otimizações: alto impacto (reduz custo E latência simultaneamente), baixo esforço (implementação direta com Redis) e baixo risco (não afeta qualidade se configurado corretamente). Fine-tuning (A) é alto esforço e só vale para volume alto. Multi-region (B) é para latência global, não primeira otimização. Speculative decoding (D) é complexo e exige infraestrutura especializada. Sempre comece por caching.
</details>

---

## Pergunta 2

Cache semântico com threshold muito baixo (ex: 0.75) causa qual problema?

- A) Aumenta significativamente a latência total
- B) Falsos positivos (resposta errada servida como correta)
- C) Rate limit excedido pelo excesso de buscas vetoriais
- D) Aumenta o custo de embedding além da economia

<details>
<summary>Resposta</summary>

**B) Falsos positivos (resposta errada servida como correta)**

Threshold baixo captura queries semanticamente próximas mas factualmente diferentes. Exemplo clássico: "Preço do iPhone 15" (0.89 de similaridade com "Preço do iPhone 14") — você serve o preço do iPhone 14 como se fosse o do 15. Este é o pior tipo de erro: silencioso (sem exceção) e confiável (o usuário acredita na resposta). Por isso, recomenda-se começar conservador (0.92) e ajustar com eval. Os outros efeitos (A, C, D) são marginais ou inexistentes.
</details>

---

## Pergunta 3

Streaming reduz a latência TOTAL de uma resposta?

- A) Sim, significativamente — o LLM gera tokens mais rápido
- B) Sim, marginalmente — há otimização no protocolo
- C) Não, reduz apenas a latência PERCEBIDA (usuário vê tokens mais cedo)
- D) Não, na verdade aumenta a latência total devido ao overhead

<details>
<summary>Resposta</summary>

**C) Não, reduz apenas a latência PERCEBIDA**

Esta é uma pegadinha clássica. Streaming NÃO reduz a latência total — o LLM ainda gera os mesmos tokens no mesmo tempo (TTFT + TPOT × N tokens é constante). Mas reduz a latência PERCEBIDA: o usuário vê o primeiro token em ~500ms (vs 10s para a resposta completa). Psicologicamente, espera-se muito mais por algo em movimento (tokens aparecendo) do que por uma tela vazia (spinner). Em agentes, streamar a resposta final melhora UX drasticamente. Não confunda latência percebida com latência real.
</details>

---

## Pergunta Bônus (não conta para nota)

Qual destas NÃO é uma estratégia válida de balanceamento de carga para agentes?

- A) Round-robin
- B) Least-connections
- C) Consistent hashing
- D) Random-walk selection

<details>
<summary>Resposta</summary>

**D) Random-walk selection**

Estratégias válidas: Round-robin (distribuição circular), Least-connections (menos ocupada), Consistent hashing (mesmo tenant → mesma réplica, preserva sessão), Weighted (réplicas potentes recebem mais), Latency-based (menor latência). "Random-walk" não é uma estratégia de load balancing — é um algoritmo de exploração estocástica. Para agentes, as mais úteis são Least-connections e Consistent hashing.
</details>

---

## Resultado

| Acertos | Avaliação |
|---|---|
| 3/3 | Excelente — compreensão completa dos conceitos centrais |
| 2/3 | Bom — compreensão sólida, revisar 1 ponto |
| 1/3 | Suficiente — revisar 2 pontos, especialmente caching |
| 0/3 | Insuficiente — reler Kleppmann cap. 5-6 e FinOps Foundation; agendar horário com professor |

---

## Reflexão Pós-Quiz

Após o quiz, reflitam:

1. "Qual das técnicas vistas eu vou aplicar primeiro no meu sistema?"
2. "Qual métrica eu vou começar a medir amanhã?"
3. "Qual anti-pattern eu cometí e como corrigir?"

> A escalabilidade não é um destino — é uma prática contínua. Comecem pelo caching, meçam tudo, iterem.
