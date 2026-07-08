# ETHAGT15 — Avaliação do Módulo

> Curso: Meta-Agentes & Sistemas Autoaprendentes (agents that build agents) · Nota mínima de aprovação: 3,0

## Composição da nota (4 pilares)

| Pilar | Peso | Instrumento |
|---|---|---|
| Técnico | 40% | Projeto (otimização automatizada) + análise crítica |
| Consultivo | 30% | Apresentação dos riscos/benefícios |
| Comportamental | 20% | Ética (code review focado em risco) |
| Prático | 10% | Demo: meta-agente em ação |

**Nota final** = Σ(pilar × peso).

---

## Rubrica — Pilar Técnico (40%)

O projeto exige implementar um sistema onde prompts/tools são otimizados automaticamente (ex.: DSPy) e medir ganho em um benchmark. Alternativamente, um meta-agente que gera/configura agentes especializados para uma tarefa, com eval antes de deploy. Meta: ganho mensurável e reproduzível.

| Critério | Peso | 1 (muito abaixo) | 3 (esperado) | 5 (referência) |
|---|---|---|---|---|
| Correção técnica | 25% | Otimização não funciona; sem ganho mensurável | Otimização automatizada funcional; ganho mensurável e reproduzível no benchmark | Ganho reproduzível + casos de borda (overfitting ao benchmark, agente gerado inválido, eval antes de deploy) tratados |
| Qualidade arquitetural | 25% | Meta-agente acoplado ao agente alvo; sem validação | Separação razoável (meta-agente · agente alvo · eval); meta-governor presente | Padrões claros (synthesis/evolution/optimization modularizados), meta-governor com vetos, sandbox antes de produção, ADR |
| Profundidade | 20% | Superficial; não entende meta-agência | Compara antes/depois da otimização; justifica DSPy vs Promptbreeder vs manual | Discute trade-offs (overfitting, goal drift, quando otimizar vs reescrever manualmente), analisa riscos de auto-modificação |
| Produção-ready | 15% | Só roda em notebook | Docker; benchmark reproduzível; eval antes/depois | Docker + sandbox de agentes gerados + pipeline de validação + política de confiança incremental |
| Avaliação/observabilidade | 15% | Sem eval do agente gerado/otimizado | Eval comparando antes/depois da otimização no benchmark | Avaliação contínua (CI), detecção de goal drift, logs de auto-modificação, análise de divergência |

**Análise crítica** (parte do Pilar Técnico): documento discutindo o que funcionou, o que falhou, riscos identificados (recursão descontrolada, drift, segurança) e mitigações aplicadas. Peso: 40% do pilar técnico.

---

## Critérios dos demais pilares

- **Consultivo (30%):** Apresentação dos riscos/benefícios do sistema autoaprendente para banca.
  - *1:* Apresenta sem discutir riscos.
  - *3:* Discute ganhos e ≥3 riscos com mitigações coerentes.
  - *5:* Quantifica ganho vs risco, articula limites éticos, propõe governance framework para meta-agentes.

- **Comportamental (20%):** Code review focado em risco do sistema de um colega.
  - *1:* Comentários ausentes ou puramente funcionais.
  - *3:* ≥5 observações sobre safety fences, goal drift e riscos de recursão.
  - *5:* Identifica loops de auto-modificação perigosos, sugere vetos/meta-governor, avalia ética do sistema.

- **Prático (10%):** Demo: meta-agente em ação (gerando/otimizando um agente ao vivo).
  - *1:* Meta-agente não funciona na demo.
  - *3:* Meta-agente otimiza/gera um agente, mostrando ganho.
  - *5:* Mostra eval antes/depois, meta-governor interceptando iteração ruim, sandbox em ação.

---

## Regras

- Entrega: repositório Git com código, análise crítica (`./docs/critical-analysis.md`), eval antes/depois e ADR de governança.
- **Integridade acadêmica:** ganhos devem ser reais e reproduzíveis. Assistência de IA é permitida e deve ser declarada. Plágio ou fabricação de resultados resulta em nota 1,0.
- Atraso: -0,5 ponto por dia útil, até 3 dias.
