---
password: Etho-Prof-2026
---
# ETHAGT13 — Avaliação do Módulo

> Curso: Segurança & Governança de Agentes · Nota mínima de aprovação: 3,0

## Composição da nota (4 pilares)

| Pilar | Peso | Instrumento |
|---|---|---|
| Técnico | 40% | Red team report + threat model |
| Consultivo | 30% | Apresentação para "comitê de risco" |
| Comportamental | 20% | Ética e responsabilidade (code review focado em risco) |
| Prático | 10% | Demo: ataque e defesa ao vivo |

**Nota final** = Σ(pilar × peso).

---

## Rubrica — Pilar Técnico (40%)

O projeto exige conduzir um red team completo de um sistema agêntico (agente de módulos anteriores ou fornecido), com threat model estruturado (STRIDE/LINDDUN), ≥10 casos de teste de ataque e plano de mitigação. Meta: ≥80% dos vetores críticos mitigados; risco residual documentado.

| Critério | Peso | 1 (muito abaixo) | 3 (esperado) | 5 (referência) |
|---|---|---|---|---|
| Correção técnica | 25% | Threat model ausente; <5 casos de ataque | Threat model estruturado; ≥10 casos de ataque executados; ≥80% mitigados | ≥10 casos + casos de borda (injeção indireta via RAG/MCP, exfiltração, tool misuse em multi-agente) testados e mitigados |
| Qualidade arquitetural | 25% | Defesas pontuais; sem defesa em profundidade | Defesa em profundidade (guardrails + HITL + allowlist); threat model coerente | Arquitetura de defesa em camadas, policy-as-code (OPA), auditoria, ADR de risco assumido com risco residual |
| Profundidade | 20% | Superficial; só repete OWASP Top-10 | Diferencia injeção direta/indireta, justifica defesas, analisa vetor por vetor | Discute trade-offs (latência/custo de defesas, HITL não é suficiente sozinho), compara ferramentas (PyRIT/Garak/NeMo), avalia eficácia quantitativamente |
| Produção-ready | 15% | Sem automação de testes | Docker + automação de red team (Garak/PyRIT); relatório estruturado | Docker + CI de red team + policy-as-code versionada + logs de auditoria + relatório com reprodução |
| Avaliação/observabilidade | 15% | Sem medição de resiliência | Métricas de resiliência (taxa de sucesso de ataque antes/depois das defesas) | Red team automatizado contínuo, métricas de redução de risco, logs de detecção de prompt injection, coverage report |

**Threat model** (parte do Pilar Técnico): documento estruturado (STRIDE/LINDDUN adaptado a agentes) modelando ativos, adversários, superfícies de ataque, com classificação de risco e mitigações. Peso: 40% do pilar técnico.

---

## Critérios dos demais pilares

- **Consultivo (30%):** Apresentação para "comitê de risco" (banca simulada como executivos de compliance/security).
  - *1:* Apresenta ataques sem contexto de risco nem recomendações.
  - *3:* Comunica riscos com clareza, prioriza vetores críticos, propõe mitigações acionáveis.
  - *5:* Quantifica risco (antes/depois), articula trade-offs de conformidade (LGPD/GDPR, EU AI Act), defende risco residual.

- **Comportamental (20%):** Code review focado em risco e ética do sistema de um colega.
  - *1:* Comentários ausentes ou puramente funcionais.
  - *3:* ≥5 observações sobre vetores de segurança, tratamento de dados sensíveis e ética.
  - *5:* Identifica prompt injection indireto, sugere guardrails, avalia conformidade regulatória, levanta dilemas éticos.

- **Prático (10%):** Demo: ataque e defesa ao vivo (prompt injection → guardrail bloqueia).
  - *1:* Não consegue demonstrar ataque nem defesa.
  - *3:* Demonstra ≥1 ataque e a defesa correspondente bloqueando.
  - *5:* Mostra exfiltração bloqueada, HITL interceptando ação destrutiva, logs de auditoria em tempo real.

---

## Regras

- Entrega: repositório Git com threat model (`./docs/threat-model.md`), relatório de red team (`./docs/red-team-report.md`) e ADR de risco assumido.
- **Integridade acadêmica:** ataques devem ser conduzidos apenas em sistemas designados para a atividade. Uso de técnicas aprendidas contra sistemas de terceiros sem autorização é violação grave do código de ética. Plágio do relatório resulta em nota 1,0.
- Atraso: -0,5 ponto por dia útil, até 3 dias.
