# ETHAGT13 — Projeto do Módulo: Red Team de Sistema Agêntico

> Curso: Segurança & Governança de Agentes · Pilar: Técnico 40% + Prático 10% · Equipe: individual ou dupla

## Contexto / Cenário

Um banco digital lançou um agente de suporte financeiro que acessa dados de conta do cliente, executa transferências (com HITL) e consulta produtos de investimento via MCP servers de terceiros. A área de Segurança da Informação (CISO) exige um red team completo antes de escalar para todos os clientes: o agente foi exposto a documentos maliciosos (prompt injection indireto via anexo de comprovante), a ataques de jailbreak em chat, e a cenários de exfiltração via tools. Você lidera o red team: deve modelar ameaças, executar ≥10 casos de teste (automatizados com PyRIT/Garak onde possível), aplicar defesas em profundidade (guardrails, HITL, allowlist) e documentar o risco residual para o comitê de risco aprovar (ou rejeitar) a escalação.

## Objetivo

Conduzir um red team completo de um sistema agêntico (o agente de suporte financeiro do cenário, ou agente equivalente construído em módulos anteriores). Entregar um threat model, ≥10 casos de teste executados (com e sem defesas), e um plano de mitigação que reduza o sucesso de ataque a um nível aceitável, com risco residual documentado em ADR.

## Requisitos

### Funcionais

1. Threat model (STRIDE ou LINDDUN adaptado): ativos, adversários, superfícies de ataque, vetores priorizados.
2. ≥10 casos de teste de ataque cobrindo: prompt injection direto, indireto (via documento/RAG/MCP resource), jailbreak, exfiltração de dados via tool, abuso de tool destrutiva.
3. Automação de ≥5 casos via PyRIT ou Garak.
4. Defesas em profundidade implementadas: guardrails de input/output, structured outputs, allowlist de tools, HITL em ações destrutivas, delimitadores de contexto.
5. Medição de sucesso de ataque antes e depois das defesas (attack success rate — ASR).
6. Política de governança: ≥1 regra policy-as-code (OPA/rego) que veta ou condiciona uma tool.

### Não-funcionais

- Casos de teste reproduzíveis (scripts, não apenas manuais).
- Latência adicionada pelas defesas documentada (overhead de guardrails).
- Logs de auditoria de cada ataque e defesa (quem tentou o quê, qual foi o resultado).
- Conformidade mapeada a ≥2 frameworks (OWASP LLM Top-10, LGPD/GDPR, ou EU AI Act).

## Entregáveis

- Threat model (documento estruturado, diagrama de superfície de ataque).
- Relatório de red team (≥10 casos: vetor, payload, resultado antes/depois da defesa, ASR).
- ADR de risco assumido (riscos residuais aceitos, mitigações, owner, data de revisão).
- Demo ao vivo: ataque e defesa (1 vetor demonstrado em tempo real).

## Critérios de sucesso (mensuráveis)

- ≥80% dos vetores críticos mitigados (ASR reduzido para ≤20% nos casos de teste após defesas).
- Threat model documenta ≥8 ameaças priorizadas com adversários e superfícies.
- ≥10 casos de teste executados com ≥5 automatizados (PyRIT/Garak).
- Risco residual documentado no ADR com owner e data de revisão definidos.
- Política policy-as-code (OPA) funcionando: bloqueia a ação proibida em 100% dos casos de teste.

## Competências avaliadas

- C1 Programação Agêntica — nível **A** (integração de defesas em sistema agêntico).
- C2 Multi-Agent Systems — nível **B** (propagação de comprometimento em multi-agente).
- C3 MCP & Tool Use — nível **A** (allowlist, schemas estritos, tool misuse).
- C5 AgentOps & Avaliação — nível **I** (automação de red team, medição de ASR).
- C6 Agent Security — nível **A** (threat model, prompt injection, guardrails, HITL, governança, conformidade).

## Referências

- Apostila: `04-Apostilas/ETHAGT13/apostila.md`
- Rubrica técnica: `08-Assignments/ETHAGT13/assignment-01.md`
