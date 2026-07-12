# ETHAGT05 — Avaliação do Módulo

> Curso: Memória de Agentes (working · episódica · semântica · procedural) · Nota mínima de aprovação: 3,0

## Composição da nota (4 pilares)

| Pilar | Peso | Instrumento |
|---|---|---|
| Técnico | 40% | Projeto (memória de agente pessoal de longo prazo) + prova |
| Consultivo | 30% | Defesa do ADR de memória |
| Comportamental | 20% | Code review |
| Prático | 10% | Demo: memória cross-sessão |

**Nota final** = Σ(pilar × peso).

---

## Rubrica — Pilar Técnico (40%)

O projeto exige projetar a memória de um agente pessoal de longo prazo (assistente de produtividade) com as 4 camadas (working, episódica, semântica, procedural), justificando trade-offs, com política de privacidade/eviction documentada.

| Critério | Peso | 1 (muito abaixo) | 3 (esperado) | 5 (referência) |
|---|---|---|---|---|
| Correção técnica | 25% | Agente não persiste estado entre sessões | 4 camadas implementadas; agente retoma estado via checkpointer (Postgres/SQLite) | 4 camadas + recall vetorial episódico funcional + casos de borda (conflito de fatos, eviction por relevância/idade, time travel/resume) |
| Qualidade arquitetural | 25% | Memória monolítica; sem distinguir tipos | Separação razoável das 4 camadas; checkpointer isolado | Padrões claros (entity-centric memory), consolidação episódica→semântica, schema versionado, ADR justifica camadas |
| Profundidade | 20% | Superficial; não entende tipos de memória | Discute trade-offs (quando memória vetorial vs relacional), política de eviction documentada | Compara MemGPT/Zep, discute consistência em multi-agente, justifica quando *não* memorizar |
| Produção-ready | 15% | Só roda em memória (sem persistência) | Persistência em Postgres; agente demonstra memória em sessões espaçadas | Docker (Postgres + vector store) + política de PII/redação + observabilidade de acesso à memória |
| Avaliação/observabilidade | 15% | Sem avaliação de utilidade da memória | Comparação com/sem memória em casos de teste | Avaliação automatizada de recall (precision/recall), logs de quem acessou a memória e quando, política de direito ao esquecimento |

**Prova** (parte do Pilar Técnico): para 5 cenários, indicar tipos de memória necessários; escrever política de eviction por relevância+idade; riscos de privacidade. Peso: 40% do pilar técnico.

---

## Critérios dos demais pilares

- **Consultivo (30%):** Defesa do ADR de memória para banca.
  - *1:* ADR ausente ou não justifica as 4 camadas.
  - *3:* ADR coerente justificando escolha de camadas, persistência e eviction.
  - *5:* Discute trade-offs de privacidade, custo e consistência com dados; antecipa cenários de evolução.

- **Comportamental (20%):** Code review do projeto de um colega.
  - *1:* Comentários ausentes ou genéricos.
  - *3:* ≥5 observações sobre persistência, eviction e tratamento de PII.
  - *5:* Identifica riscos de privacidade, sugere estratégias de sumarização, avalia robustez do checkpointer.

- **Prático (10%):** Demo: agente demonstrando memória útil em sessões espaçadas (simulado).
  - *1:* Agente não lembra de sessão anterior.
  - *3:* Agente recupera informação relevante de sessão anterior via memória.
  - *5:* Mostra recall vetorial + consolidação episódica→semântica + política de eviction em ação.

---

## Regras

- Entrega: repositório Git com código, ADR de memória (`./docs/adr-001-memory.md`) e política de privacidade/eviction.
- **Integridade acadêmica:** a política de privacidade deve ser autoral. Assistência de IA é permitida e deve ser declarada. Plágio resulta em nota 1,0.
- Atraso: -0,5 ponto por dia útil, até 3 dias.
