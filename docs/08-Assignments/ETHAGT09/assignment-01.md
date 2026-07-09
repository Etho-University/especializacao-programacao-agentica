---
password: Etho-Prof-2026
---
# ETHAGT09 — Avaliação do Módulo

> Curso: Comunicação e Coordenação Multi-Agente (A2A · blackboard · actor model) · Nota mínima de aprovação: 3,0

## Composição da nota (4 pilares)

| Pilar | Peso | Instrumento |
|---|---|---|
| Técnico | 40% | Projeto (sistema de negociação entre agentes) + prova |
| Consultivo | 30% | Defesa arquitetural |
| Comportamental | 20% | Code review |
| Prático | 10% | Demo: agentes coordenando |

**Nota final** = Σ(pilar × peso).

---

## Rubrica — Pilar Técnico (40%)

O projeto exige implementar um sistema de negociação entre agentes (ex.: comprador/vendedor, ou especialistas debatendo um diagnóstico), com convergência em ≥80% dos casos e análise de falhas documentada.

| Critério | Peso | 1 (muito abaixo) | 3 (esperado) | 5 (referência) |
|---|---|---|---|---|
| Correção técnica | 25% | Agentes não negociam; sem troca de mensagens | Negociação funcional com schemas de mensagem; convergência ≥80% dos casos | Convergência ≥80% + casos de borda (deadlock, agente desiste, mensagens duplicadas/fora de ordem) tratados |
| Qualidade arquitetural | 25% | Padrões de comunicação acoplados; sem schemas | Padrão de comunicação claro (A2A direta, group chat ou blackboard); schemas versionados | Padrões modularizáveis (blackboard vs actor model intercambiáveis), ADR justifica escolha de coordenação |
| Profundidade | 20% | Superficial; não distingue padrões A2A | Compara padrões (blackboard vs direta, handoff vs delegação), discute deadlock | Discute trade-offs (A2A Protocol vs MCP, actor model vs shared-state), analisa convergência e resolução de conflito |
| Produção-ready | 15% | Só roda em memória, sem persistência | Roda em ambiente controlado; traces de negociação | Docker + persistência de estado de negociação + traces + análise de convergência automatizada |
| Avaliação/observabilidade | 15% | Sem avaliação de convergência | Taxa de convergência mensurada em ≥20 casos | Análise de convergência automatizada, categorização de falhas (deadlock, impasse, timeout), traces completos |

**Prova** (parte do Pilar Técnico): schemas de mensagem A2A com versionamento, diferença handoff vs delegação, prevenção de deadlock, blackboard vs mensagens diretas. Peso: 40% do pilar técnico.

---

## Critérios dos demais pilares

- **Consultivo (30%):** Defesa arquitetural do padrão de comunicação/coordenação escolhido.
  - *1:* Não justifica a arquitetura de coordenação.
  - *3:* Justifica a escolha com ≥3 critérios (convergência, complexidade, escalabilidade).
  - *5:* Articula trade-offs entre padrões, usa dados de convergência, identifica sinais de evolução.

- **Comportamental (20%):** Code review do sistema multi-agente de um colega.
  - *1:* Comentários ausentes ou genéricos.
  - *3:* ≥5 observações sobre schemas de mensagem, tratamento de deadlock e coordenação.
  - *5:* Sugere padrões alternativos, identifica riscos de deadlock, avalia robustez da negociação.

- **Prático (10%):** Demo: agentes coordenando/negociando ao vivo.
  - *1:* Agentes não coordenam ou entram em deadlock.
  - *3:* Agentes convergem em ≥2 cenários, mostrando a troca de mensagens.
  - *5:* Mostra resolução de conflito, traces de negociação, lida com impasse graciosamente.

---

## Regras

- Entrega: repositório Git com código, traces, análise de convergência e ADR de coordenação (`./docs/adr-001-coordination.md`).
- **Integridade acadêmica:** taxas de convergência devem ser reais. Assistência de IA é permitida e deve ser declarada. Plágio resulta em nota 1,0.
- Atraso: -0,5 ponto por dia útil, até 3 dias.
