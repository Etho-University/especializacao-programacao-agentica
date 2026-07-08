# `ETHAGT13` — Segurança & Governança de Agentes

> Fase D · Carga 25 h · Versão 1.0 · Julho 2026

## 1. Identificação

| Campo | Valor |
|---|---|
| Código | `ETHAGT13` |
| Título | Segurança & Governança de Agentes |
| Fase interna | D |
| Carga horária | 25 h |
| Pré-requisitos | `ETHAGT12` |
| Módulos que dependem deste | `ETHAGT15`, `ETHAGT90` |

## 2. Objetivos

**Objetivo geral**: Tornar o aluno capaz de **proteger agentes** e **governar** seu comportamento em ambientes adversariais e regulados — indo além do OWASP LLM Top-10 superficial.

**Objetivos específicos**:
1. Modelar ameaças (threat modeling) para sistemas de agentes.
2. Defesa contra prompt injection (direto, indireto via RAG, jailbreak).
3. Aplicar guardrails (input/output, structured outputs, constitutions).
4. Implementar HITL em checkpoints críticos.
5. Conduzir red team estruturado.
6. Definir governança (policy-as-code, auditoria, conformidade).

## 3. Competências desenvolvidas

| Competência | Nível ao final |
|---|---|
| C1 Programação Agêntica | **A** |
| C2 Multi-Agent Systems | B |
| C3 MCP & Tool Use | **A** |
| C5 AgentOps & Avaliação | **I** |
| C6 Agent Security | **A** |

## 4. Conteúdo programático

### Unidade 1 — Threat modeling para agentes (4 h)
- Ativos, adversários, superfícies de ataque
- Modelo STRIDE / LINDDUN adaptado
- Tool calling como vetor
- Multi-agente: propagação de comprometimento

### Unidade 2 — Prompt injection (5 h)
- Injeção direta vs indireta (via documentos em RAG, MCP resources)
- Jailbreaks e suas famílias
- Por que é difícil: não há separação instrução/dados nativa
- Defesas: delimitadores, system prompt robusto, classificadores, instrução-hierarchy

### Unidade 3 — Guardrails (4 h)
- Input/output filtering
- Structured outputs como defesa
- Constitutional AI / NeMo Guardrails
- Tool allowlists e schemas estritos
- Latência e custo de defesas

### Unidade 4 — HITL e checkpointing (3 h)
- Quando exigir aprovação humana
- Checkpoints programáticos (pré-ação destrutiva)
- UX de HITL (baixa fricção)
- Logging de decisões humanas

### Unidade 5 — Red team estruturado (5 h)
- Casos de teste: exfiltração, abuso de tools, jailbreak
- Automation (Garak, PyRIT)
- Avaliação contínua vs pontual
- Métricas de resiliência

### Unidade 6 — Governança e conformidade (4 h)
- Policy-as-code (OPA, rego)
- Auditoria: quem fez o quê, quando
- Conformidade: LGPD/GDPR, EU AI Act, setorial
- Responsabilidade (responsibility), explicabilidade
- ADRs de risco assumido

## 5. Bibliografia

### Fundamental
- OWASP. *Top 10 for LLM Applications* (2025).
- Greshake, K. et al. *Not what you've signed up for: Compromising Real-World LLM-integrated Applications* (arXiv:2302.12173 — prompt injection indireto).
- Anthropic. *Many-shot Jailbreaking* e *Constitutional AI*.

### Complementar
- Microsoft PyRIT; NVIDIA NeMo Guardrails; Garak.
- NIST AI RMF; EU AI Act.

## 6. Papers canônicos

- `arXiv:2302.12173` — Indirect prompt injection (Greshake)
- `arXiv:2310.04451` — AgentDojo (eval de injeção em agentes)
- `arXiv:2406.18510` — InjecAgent

## 7. Laboratórios

- **Lab 1** (4 h): "Red team de um agente RAG". Construir agente e explorar 5 vetores de prompt injection indireto.
- **Lab 2** (5 h): "Defesa em profundidade". Aplicar guardrails, HITL e allowlist; medir redução de sucesso de ataque.

## 8. Projeto do módulo

**Descrição**: conduzir red team completo de um sistema agêntico, com threat model, ≥10 casos de teste, e plano de mitigação.
**Entrega**: threat model + relatório de red team + ADR de risco assumido.
**Critério de sucesso**: ≥80% dos vetores críticos mitigados; risco residual documentado.

## 9. Exercícios

1. Diferencie injeção direta de indireta com exemplo.
2. Por que HITL não é defesa suficiente sozinho?
3. Escreva uma política OPA para vetar uma tool em horário fora do expediente.
4. Liste 5 conformidades regulatórias relevantes a agentes.
5. Verdadeiro/falso: "Modelos maiores são sempre mais seguros."

## 10. Avaliação

| Pilar | Peso | Instrumento |
|---|---|---|
| Técnico | 40% | Red team report + threat model |
| Consultivo | 30% | Apresentação para "comitê de risco" |
| Comportamental | 20% | Ética e responsabilidade (code review) |
| Prático | 10% | Demo: ataque e defesa ao vivo |

**Nota mínima**: 3,0.

## 11. Slides

- Slides: `03-Slides/ETHAGT13-slides.md` (~80 slides).

## 12. Leitura complementar

- OWASP LLM Top-10; Anthropic security blogs; EU AI Act.

## 13. Ferramentas

- PyRIT, Garak, NeMo Guardrails, OPA, Lakera.

## 14. Diagramas

- Diagramas: `12-Diagrams/ETHAGT13/` — threat-model.mmd, defense-in-depth.mmd, hitl-checkpoints.mmd.

## 15. Estudo de caso

- incidentes reais (Bing/Sydney, Chevrolet chatbot, ataques a agentes).

## 16. Ficha de pesquisa

- Ficha: `20-Research/ETHAGT13-pesquisa.md`.

---

*Mantido por: Universidade Etho · Versão 1.0 · Julho 2026*
