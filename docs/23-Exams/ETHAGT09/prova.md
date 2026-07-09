---
password: Etho-Prof-2026
---
# ETHAGT09 — Prova do Módulo: Comunicação e Coordenação Multi-Agente

> Universidade Etho · Versão 1.0 · Julho 2026
> Duração: ~60 min · 10 questões · closed book · Pilar Técnico (40%)

Esta prova avalia domínio dos **modelos de comunicação e coordenação A2A** — mensagens, padrões de conversação, blackboard, actor model e negociação — e a capacidade de escolher o padrão certo para cada problema.

---

## Parte 1 — Conceitos (Q1-4)

**1. (Múltipla escolha)** No espectro da comunicação A2A, qual combinação associa corretamente *broadcast*, *p2p* e *pub/sub* a suas propriedades?
- (a) broadcast = 1 emissor → todos; p2p = 1→1; pub/sub = desacoplado via tópicos.
- (b) broadcast = desacoplado; p2p = síncrono sempre; pub/sub = 1→1.
- (c) broadcast = ordenado globalmente; p2p = lossy; pub/sub = síncrono.

**2. (V/F justificado)** "Actor model é sempre mais lento que shared-state com locks." Verdadeiro ou falso? Justifique.

**3. (Múltipla escolha)** O handoff (estilo OpenAI Swarm) difere da delegação de um supervisor porque:
- (a) Handoff transfere o controle (e o contexto) para outro agente; o supervisor retém controle e apenas roteia tool calls.
- (b) Handoff é síncrono; delegação é assíncrona.
- (c) Não há diferença prática.

**4. (V/F justificado)** "No blackboard, os especialistas precisam conhecer uns aos outros para se coordenar."

---

## Parte 2 — Aplicação e trade-off (Q5-8)

**5. (Trade-off)** Dê 3 critérios para decidir entre *blackboard* e *mensagens diretas* (p2p) num sistema multi-agente.

**6. (Debug de trace)** Um group chat (AutoGen) entra em loop: dois agentes ficam se cumprimentando indefinidamente. Cite 2 causas prováveis e 2 correções.

**7. (Análise)** Por que o *actor model* é frequentemente escolhido como fundação de agentes distribuídos? Aponte 2 propriedades e 1 trade-off.

**8. (Trade-off)** Em negociação entre agentes (bargaining), dê 2 estratégias para evitar deadlock e garantir convergência em ≥ 80% dos casos.

---

## Parte 3 — Projeto curto (Q9-10)

**9. (Projeto)** Escreva um schema JSON mínimo de mensagem A2A com *versionamento*, campos `from`, `to`, `type`, `payload` e `version`.

**10. (Projeto)** MCP vs A2A: explique em 3 linhas por que são "complementares, não competidores" e dê um exemplo de sistema que usa ambos.

---

## Critérios de correção (resumo)

| Parte | Questões | Peso |
|---|---|---|
| Conceitos | 1, 2, 3, 4 | 40% |
| Aplicação/trade-off | 5, 6, 7, 8 | 40% |
| Projeto curto | 9, 10 | 20% |

**Conversão**: cada questão vale 10 pts; total 100 pts → nota 1-5.
- 90+: 5,0 · 80-89: 4,5 · 70-79: 4,0 · 60-69: 3,5 · 50-59: 3,0 (mínimo) · <50: reprovação.

Gabarito comentado em [`gabarito.md`](gabarito.md).
