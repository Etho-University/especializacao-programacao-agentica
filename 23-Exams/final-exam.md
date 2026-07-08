# Prova Final Integradora — Especialização em Programação Agêntica

> Universidade Etho · Versão 1.0 · Julho 2026
> Duração: 2 horas · 20 questões ·closed book

Esta prova **integradora** cobre os 16 módulos da Especialização. Ao contrário das provas por módulo (em `23-Exams/ETHAGT0x/`), esta exige **síntese**: conectar conceitos de múltiplos módulos. Use como simulado final antes do exame de certificação.

---

## Parte 1 — Fundamentos e raciocínio (Q1-5)

**1.** Defina Augmented LLM e explique por que é a "unidade atômica" de sistemas agênticos. O que acontece ao remover cada uma das 3 augmentations?

**2.** Compare ReAct, Plan-and-Execute e ReWOO em: latência, custo (tokens), robustez a planos errados. Dê um cenário onde cada brilha.

**3.** Árvore de Thoughts (ToT) é poderoso mas caro. Dê 2 critérios para decidir se vale a pena.

**4.** O que muda no design do agente ao usar um reasoning model nativo (o1/o3) em vez de CoT promptado?

**5.** Explique a relação entre inference-time reasoning nativo e a diminuição da necessidade de Tree of Thoughts.

## Parte 2 — Tools, MCP e memória (Q6-10)

**6.** Escreva a descrição (ACI) de uma tool `delete_user_account(user_id)` indicando onde HITL é obrigatório.

**7.** Liste 3 princípios ACI aplicáveis a qualquer tool e dê exemplo de violação.

**8.** Diferencie MCP tools, resources e prompts. Dê exemplo de quando usar cada.

**9.** Para um agente pessoal de longo prazo, justifique as 4 camadas de memória (working, episódica, semântica, procedural) com exemplo de cada.

**10.** Por que checkpointer é necessário para HITL? Sem ele, o que falha?

## Parte 3 — Multi-agente e orquestração (Q11-14)

**11.** Quando topologia hierarchical supera swarm? Dê ≥3 critérios.

**12.** Em event-driven multi-agent, por que partition key importa? Dê exemplo.

**13.** Esquematize uma saga compensatória para "processar pedido + cobrar + enviar email de confirmação".

**14.** Diferencie durable execution (Temporal) de simplesmente usar Kafka com retries.

## Parte 4 — Produção e fronteira (Q15-20)

**15.** Descreva defesa em profundidade para um agente com tool de enviar email.

**16.** Por que "bom score em SWE-bench" não garante bom desempenho em produção?

**17.** Para 80% de perguntas fáceis + 20% difíceis, qual estratégia economiza mais mantendo qualidade?

**18.** Defina goal drift em sistemas auto-evolutivos e proponha 2 detecções.

**19.** O AI Scientist (Sakana) tem limitações. Liste 3 e explique por que HITL é essencial.

**20.** Você foi contratado para arquitetar uma plataforma de pesquisa autônoma para a Etho. Escreva o esqueleto de um ADR justificando topologia + memória + orquestração.

---

## Critérios de correção (resumo)

| Conceito | Questões | Peso |
|---|---|---|
| Fundamentos | 1, 2, 3, 4, 5 | 25% |
| Tools/MCP/Memória | 6, 7, 8, 9, 10 | 25% |
| Multi-agente/Orquestração | 11, 12, 13, 14 | 20% |
| Produção/Segurança | 15, 16, 17 | 15% |
| Fronteira | 18, 19 | 10% |
| Síntese | 20 | 5% |

**Conversão**: cada questão vale 5 pts; total 100 pts. Nota 1-5.
- 90+ pts: 5,0
- 80-89: 4,5
- 70-79: 4,0 (mínimo certificação)
- <70: 3,0 ou menos.

Gabarito comentado em [`final-exam-gabarito.md`](final-exam-gabarito.md).
