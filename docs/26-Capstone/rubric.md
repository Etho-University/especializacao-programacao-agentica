# ETHAGT90 — Rubrica Detalhada

> Nota mínima em **cada pilar**: 4,0. Falhar num pilar reprova o capstone.

## Pilar Técnico (40%)

| Critério | Peso | 1 (muito abaixo) | 3 (esperado) | 5 (referência) |
|---|---|---|---|---|
| **Cobertura de requisitos** | 20% | <50% dos requisitos do enunciado | ≥80% | 100% + extras |
| **Profundidade arquitetural** | 20% | ADRs rasos; cópia de exemplo | ≥3 ADRs coerentes com trade-offs | ADRs discutem alternativas + consequências + riscos |
| **Qualidade da implementação** | 15% | Bugs; não roda estável | Roda happy path | Robusto; sobrevive a chaos test |
| **Eval report** | 15% | Ausente ou superficial | Métricas básicas | 4 dimensões + análise de falhas + reprodutível |
| **Produção-ready** | 15% | Sem Docker | Dockerfile | Compose + observabilidade + FinOps |
| **Segurança** | 15% | Sem threat model; sem HITL | Threat model básico + HITL | + red team + policy-as-code + ASR documentado |

**Nota final (Técnico)** = Σ(nota × peso) / Σ(pesos). Mínimo para aprovação: **4,0**.

## Pilar Consultivo (30%)

| Critério | Peso | 1 | 3 | 5 |
|---|---|---|---|---|
| **Clareza da apresentação** | 30% | Confusa; fora do tempo | Estruturada; no tempo | Clara + envolvente + tempo preciso |
| **Defesa das decisões** | 30% | Não justifica | Justifica razoavelmente | Trade-offs explícitos; responde bem |
| **Honestidade** | 20% | Infla/omite | Razoável | Discute limites abertamente |
| **Visão arquitetural** | 20% | Sem visão de conjunto | Boa visão | Insight de arquiteto sênior |

Mínimo: **4,0**.

## Pilar Comportamental (20%)

| Critério | Peso | 1 | 3 | 5 |
|---|---|---|---|---|
| **Code review recebido** | 30% | Rejeita feedback | Aceita | Integra e melhora |
| **Colaboração** (se em equipe) | 30% | Isolado | Cooperativo | Multiplica |
| **Ética** | 40% | Omite riscos | Cauteloso | Proativo em responsabilidade |

Mínimo: **4,0**.

## Pilar Prático (10%) — Demo ao vivo

| Critério | Peso | 1 | 3 | 5 |
|---|---|---|---|---|
| **Funciona sem ensaio** | 50% | Falha em todas | 1-2 de 3 | 3/3 + resiliência |
| **Trace visível** | 25% | Não mostra | Mostra básico | Explica trace em tempo real |
| **Resiliência em demo** | 25% | Quebra sem recuperar | Recupera com ajuda | Lida com falha elegantemente |

Mínimo: **4,0**.

## Nota final do Capstone

**Nota final** = Σ(pilar × peso). Aprovação exige:
- Nota final ≥ **4,0**.
- E **cada pilar individualmente** ≥ 4,0.

Exemplo: técnico 4.5, consultivo 4.0, comportamental 3.5 (reprova), prático 4.5 → **reprovado** (comportamental < 4.0).

## Critérios de excelência (para distinção)

Capstones com nota ≥ 4,5 em **todos** os pilares podem receber **distinção**:
- "Capstone de Excelência" no certificado.
- Apresentação em evento interno Etho.
- Contribuição como referência para futuras turmas.

## Política de re-tentativa

Se reprovado:
- Painel explica onde falhou.
- Aluno tem **3 meses** para corrigir e re-defender.
- Segunda re-tentativa (se necessária) exige plano de estudo adicional.
- Terceira falha: re-fazer módulos específicos antes de nova tentativa.
