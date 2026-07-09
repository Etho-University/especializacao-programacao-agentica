---
tags:
  - ETHAGT02
  - syllabus
  - tool-calling
  - aci
---

# `ETHAGT02` — Tool Calling e Agent-Computer Interface (ACI)

> Especialização em Programação Agêntica · Universidade Etho
> Fase A · Carga 25 h · Versão 1.0 · Última atualização: Julho 2026

## 1. Identificação

| Campo | Valor |
|---|---|
| Código | `ETHAGT02` |
| Título | Tool Calling e Agent-Computer Interface (ACI) |
| Fase interna | A — Fundamentos Agênticos |
| Fase Etho | Especialização (Fase 4) |
| Carga horária | 25 h |
| Pré-requisitos | `ETHAGT01` |
| Módulos que dependem deste | `ETHAGT08` (MCP aprofunda), `ETHAGT13` (security) |

## 2. Objetivos

**Objetivo geral**: Capacitar o aluno a **projetar, documentar e validar tools** que tornam um agente confiável — tratando a *Agent-Computer Interface* com o mesmo rigor de uma HCI.

**Objetivos específicos**:
1. Dominar o mecanismo de tool calling (function calling, structured outputs, JSON schema).
2. Aplicar os princípios de Anthropic para ACI: poka-yoke, exemplos, paths absolutos, formato próximo ao natural.
3. Projetar tools idempotentes, com tratamento de erro e timeouts.
4. Distinguir tools seguras de destrutivas; aplicar HITL onde necessário.
5. Avaliar empiricamente o uso de tools por um agente (workbench, iterar).

## 3. Competências desenvolvidas

| Competência | Nível ao final |
|---|---|
| C1 Programação Agêntica | **I** |
| C3 MCP & Tool Use | **I** |
| C5 AgentOps & Avaliação | B |
| C6 Agent Security | B |

## 4. Conteúdo programático

### Unidade 1 — O mecanismo do tool calling (4 h)
- Function calling: do prompt para JSON estruturado
- JSON Schema como contrato
- Structured outputs / constrained decoding (visão)
- Multi-tool calls em uma resposta; paralelismo
- Custo: tokens de descrição vs benefício

### Unidade 2 — ACI como disciplina (5 h)
- A analogia de Anthropic: invista em ACI tanto quanto em HCI
- Princípios: "pôr-se no lugar do modelo"; descrições ricas
- Exemplos, edge cases, requisitos de formato, fronteiras entre tools
- Formato próximo ao natural (sem escaping desnecessário, sem diffs complexos)
- "Pense em tokens antes de escrever": dar espaço para pensar

### Unidade 3 — Engenharia de tools (5 h)
- Schemas claros (Pydantic, TypedDict, Zod)
- Idempotência e onde ela importa
- Timeouts, retries, fallbacks
- Tipologia: leitura / escrita / destrutiva / external-side-effect
- Versionamento de tools (sem quebrar agentes em produção)

### Unidade 4 — Tools perigosas e HITL (4 h)
- Matriz de risco: irreversível × impactante
- HITL obrigatório para ações destrutivas (delete, deploy, transfer, email)
- Confirmação explícita, dry-run, simulação
- Allowlists vs dinâmico

### Unidade 5 — Erros comuns e correções (4 h)
- Paths relativos → absolutos (caso real Anthropic)
- Muitas tools similares → consolidar ou renomear
- Descrições vagas → reescrever como docstring de dev júnior
- Schema frouxo → apertar com enum/patterns
- Falta de erro tratado → propagar com mensagem útil ao modelo

### Unidade 6 — Avaliando tools (3 h)
- Workbench: rodar N inputs, observar erros, iterar
- Métricas: taxa de uso correto, custo por chamada, latência
- Conjunto de testes de regressão para tools

## 5. Bibliografia

### Fundamental
- Anthropic. *Building Effective Agents*, Appendix 2: "Prompt engineering your tools". 2024.
- OpenAI. *Function Calling Guide* e *Structured Outputs*. 2024.
- Pydantic Team. *Pydantic AI Documentation* (para padrões de schema).

### Complementar
- Patterson, D. *Tools, not Agents* (reflexão sobre quando ferramentas bastam).
- Pat McGuinness. *Design Patterns for Effective AI Agents* (Substack).

## 6. Papers canônicos

- `arXiv:2303.11366` — Reflexion (usa tools em loop; referência de erro)
- `arXiv:2305.15334` — Gorilla (LLM com 1.700 APIs; comparação de performance)
- `arXiv:2307.16789` — ToolLLM (benchmark de tool use)

## 7. Laboratórios

- **Lab 1** (4 h): "Refatorando tools". Dado um conjunto de 5 tools mal-desenhidas, aplicar os princípios ACI e medir melhoria de taxa de uso correto em 20 casos.
- **Lab 2** (4 h): "Tool destrutiva com HITL". Construir uma tool de "enviar email" com confirmação, dry-run e log de auditoria.

## 8. Projeto do módulo

**Descrição**: projetar o conjunto de tools de um agente de suporte ao cliente (até 8 tools) com schemas, descrições, tratamento de erro e HITL. Implementar e avaliar com um workbench próprio (20 casos).
**Entrega**: código + workbench + relatório de iteração (antes/depois de refatoração ACI).
**Critério de sucesso**: taxa de uso correto ≥ 85%; HITL funcionando para ações destrutivas.

## 9. Exercícios

1. Reescreva a descrição de uma tool vaga em uma ACI de qualidade.
2. Identifique 3 anti-patterns em um schema fornecido.
3. Quando é melhor ter 1 tool com parâmetro `mode` vs 2 tools separadas?
4. Escreva um JSON schema que force idempotência (ex.: com `request_id`).
5. Liste 5 tools que exigem HITL e justifique.

## 10. Avaliação

| Pilar | Peso | Instrumento |
|---|---|---|
| Técnico | 40% | Projeto + prova de schemas |
| Consultivo | 30% | Apresentação defendendo as escolhas de design |
| Comportamental | 20% | Revisão cruzada de schemas |
| Prático | 10% | Demo: agente usando as tools |

**Nota mínima**: 3,0.

## 11. Slides

`03-Slides/ETHAGT02-slides.md` — ~70 slides. Diagramas: matriz de risco, workbench loop, schema-vs-descrição.

## 12. Leitura complementar

- Anthropic Engineering Blog (séries sobre tool use).
- Coda, Notion, Replit — relatos de produção com tools.
- LangChain *Tool Calling* guide.

## 13. Ferramentas

Python · Pydantic · OpenAI/Anthropic SDK · `instructor` (structured outputs) · tooling de eval próprio · Docker.

## 14. Diagramas

`12-Diagrams/ETHAGT02/` — risk-matrix.mmd · aci-iteration-loop.mmd · hitl-flow.mmd.

## 15. Estudo de caso

Como Anthropic reprojeta tools (paths relativos → absolutos) durante o desenvolvimento do agente SWE-bench. `09-CaseStudies/`.

## 16. Ficha de pesquisa

`20-Research/ETHAGT02-pesquisa.md` — Anthropic Appendix 2; docs OpenAI function calling; paper Gorilla; docs Pydantic AI. Consulta: Julho 2026.

---

*Mantido por: Universidade Etho · Versão 1.0 · Julho 2026*
