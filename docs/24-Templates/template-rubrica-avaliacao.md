# Template — Rubrica de Avaliação (Pilar Técnico 40%)

> Define **como** um módulo ou capstone é avaliado no Pilar Técnico. Cada item recebe nota 1-5 (escala Etho: 1 muito abaixo · 2 abaixo · 3 esperado · 4 acima · 5 referência). Nota final = média ponderada.

---

# Rubrica — `[Módulo/Capstone]`

| Critério | Peso | 1 (muito abaixo) | 3 (esperado) | 5 (referência) |
|---|---|---|---|---|
| **Correção técnica** | 25% | Não implementa o núcleo | Implementa o núcleo com bugs menores | Implementa completo + casos de borda |
| **Qualidade arquitetural** | 25% | Acoplamento, sem separação | Separação razoável de responsabilidades | Padrões claros, extensível, justificada em ADR |
| **Profundidade** | 20% | Superficial, sem trade-offs | Cobre o esperado | Discute trade-offs, compara alternativas |
| **Produção-ready** | 15% | Não roda fora do notebook | Roda em ambiente controlado | Docker, observabilidade, testes |
| **Avaliação/observabilidade** | 15% | Sem eval | Eval básico (LLM-as-judge) | Eval automatizado, benchmarks, traces |

**Nota final (Técnico)** = Σ(nota × peso) / Σ(pesos). Aprovação ≥ 3,0 · Certificação ≥ 4,0.

## Como os 4 pilares se combinam

| Pilar | Peso | Instrumento típico |
|---|---|---|
| Técnico | 40% | Esta rubrica (aplicada ao projeto + prova) |
| Consultivo | 30% | Apresentação "para cliente" + estudo de caso |
| Comportamental | 20% | Code review + colaboração em labs |
| Prático | 10% | Demo ao vivo + Q&A |

**Nota final do módulo** = Σ(pilar × peso).

## Notas específicas para Capstone (`ETHAGT90`)

- Avaliado por **painel de ≥ 3 especialistas**.
- Exige **nota ≥ 4,0** em todos os pilares (não média — cada um).
- Defesa ao vivo de 45 min (25 min apresentação + 20 min Q&A).
- Código + docs + eval report + ADRs entregues previamente (≥ 5 dias úteis).
