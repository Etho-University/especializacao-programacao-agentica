# ETHAGT02 — Avaliação do Módulo

> Curso: Tool Calling e Agent-Computer Interface (ACI) · Nota mínima de aprovação: 3,0

## Composição da nota (4 pilares)

| Pilar | Peso | Instrumento |
|---|---|---|
| Técnico | 40% | Projeto (conjunto de tools com workbench) + prova de schemas |
| Consultivo | 30% | Apresentação defendendo as escolhas de design de tools |
| Comportamental | 20% | Revisão cruzada de schemas (peer review estruturado) |
| Prático | 10% | Demo: agente usando as tools em cenário real |

**Nota final** = Σ(pilar × peso).

---

## Rubrica — Pilar Técnico (40%)

O projeto exige projetar até 8 tools de um agente de suporte ao cliente, com schemas, descrições ACI, tratamento de erro e HITL, avaliadas em workbench próprio (≥20 casos).

| Critério | Peso | 1 (muito abaixo) | 3 (esperado) | 5 (referência) |
|---|---|---|---|---|
| Correção técnica | 25% | Tools não funcionam; schemas inválidos ou sem JSON Schema | Tools funcionais; schemas válidos (Pydantic/TypedDict); taxa de uso correto ≥85% | Taxa ≥85% + tools idempotentes, com timeouts/retries e fallback; HITL operacional em ações destrutivas |
| Qualidade arquitetural | 25% | Tools monolíticas, sem tipologia (leitura/escrita/destrutiva) | Tipologia razoável; HITL isolado das tools de leitura | Padrões claros (separation of concerns), versionamento de tools sem quebrar agentes, matriz de risco documentada |
| Profundidade | 20% | Descrições vagas; sem aplicar princípios ACI | Aplica poka-yoke, exemplos, paths absolutos, formato natural em todas as tools | Discute trade-offs (1 tool com `mode` vs 2 separadas), consolida tools similares, justifica idempotência com `request_id` |
| Produção-ready | 15% | Só roda no notebook; workbench ausente | Workbench funcional (20 casos); relatório antes/depois da refatoração ACI | Docker + workbench automatizado + conjunto de testes de regressão para tools + relatório de iteração |
| Avaliação/observabilidade | 15% | Sem eval de tools | Métricas básicas (taxa de uso correto, custo por chamada, latência) no workbench | Workbench com logs de auditoria para tools destrutivas; benchmark de custo/benefício de cada descrição |

**Prova de schemas** (parte do Pilar Técnico): escrever JSON Schemas a partir de especificações, identificar anti-patterns, justificar escolhas de enum/patterns e idempotência. Peso: 40% do pilar técnico.

---

## Critérios dos demais pilares

- **Consultivo (30%):** Apresentação defendendo as escolhas de design de tools como se fosse para um time de produto.
  - *1:* Apresenta as tools sem justificar o design.
  - *3:* Defende ≥3 escolhas de design com base nos princípios ACI (poka-yoke, exemplos, formato natural).
  - *5:* Usa dados do workbench (antes/depois) para provar melhoria; articula quando HITL é obrigatório vs opcional.

- **Comportamental (20%):** Revisão cruzada de schemas — cada aluno revisa os schemas de um colega.
  - *1:* Revisão superficial ou ausente.
  - *3:* Identifica ≥3 anti-patterns nos schemas do colega com sugestões concretas.
  - *5:* Reescreve descrições inteiras, identifica edge cases de schema (enum, patterns, required), propõe consolidação de tools.

- **Prático (10%):** Demo: agente usando as tools para resolver um ticket de suporte simulado.
  - *1:* Agente não consegue usar as tools corretamente.
  - *3:* Agente usa tools corretamente em ≥2 cenários, com HITL acionado quando apropriado.
  - *5:* Demo inclui dry-run, log de auditoria visível, e agente lida com erro de tool graciosamente.

---

## Regras

- Entrega: repositório Git com código, workbench, relatório de iteração ACI e schemas em `./schemas/`.
- **Integridade acadêmica:** ferramentas de IA podem auxiliar na escrita de schemas, mas a análise de trade-offs e o relatório de iteração devem ser autorais. Plágio resulta em nota 1,0.
- Atraso: -0,5 ponto por dia útil, até 3 dias.
