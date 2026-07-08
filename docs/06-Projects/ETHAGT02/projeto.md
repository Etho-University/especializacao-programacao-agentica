# ETHAGT02 — Projeto do Módulo: Tools de Suporte ao Cliente com ACI

> Curso: Tool Calling e Agent-Computer Interface (ACI) · Pilar: Técnico 40% + Prático 10% · Equipe: individual ou dupla

## Contexto / Cenário

Uma empresa de SaaS B2B (plataforma de gestão de assinaturas) opera um agente de suporte ao cliente que atende ≥2.000 tickets por dia. O agente atual possui 12 tools mal documentadas com descrições vagas, paths inconsistentes e sem tratamento de erro estruturado — a taxa de uso correto de tools é de apenas 58%. O time de Customer Success exige que o agente consiga: consultar status de assinatura, processar reembolso, escalar para humano, buscar artigo na base de conhecimento, atualizar endereço de cobrança, cancelar plano, aplicar cupom, e verificar histórico de tickets. Ações destrutivas (cancelar, reembolsar) exigem confirmação humana (HITL). Você é responsável por redesenhar e validar o conjunto de tools.

## Objetivo

Projetar, implementar e avaliar um conjunto de até 8 tools para um agente de suporte ao cliente, aplicando os princípios de ACI (poka-yoke, descrições ricas, exemplos, paths absolutos, tratamento de erro útil). Construir um *workbench* próprio com 20 casos de teste para medir a taxa de uso correto antes e depois da refatoração ACI, garantindo HITL funcional para todas as ações destrutivas.

## Requisitos

### Funcionais

1. Até 8 tools com schemas Pydantic (parâmetros tipados, descrições detalhadas, exemplos na docstring).
2. Cada tool classifica-se como leitura, escrita, destrutiva ou external-side-effect.
3. Tools destrutivas (cancelar plano, processar reembolso) exigem HITL: confirmação explícita, dry-run e log de auditoria.
4. Tratamento de erro em todas as tools: timeout, retry com backoff, e mensagem de erro útil ao modelo (não stack trace).
5. Idempotência via `request_id` nas tools de escrita/destrutiva.
6. Workbench próprio que roda 20 casos de teste e reporta: taxa de uso correto, custo por chamada, latência.

### Não-funcionais

- Schemas validados com Pydantic v2 (ou TypedDict + JSON Schema).
- Versionamento de tools (semântico) documentado.
- Latência por chamada de tool ≤ 2 segundos (mocks permitidos para serviços externos).
- Workbench reproduzível via script único (`pytest` ou CLI).
- Logs estruturados de cada chamada de tool com input, output, latência e status.

## Entregáveis

- Código (repositório com README descrevendo cada tool, seu tipo e matriz de risco).
- Workbench de avaliação (20 casos com inputs, expected outputs e critério de sucesso).
- Relatório de iteração ACI (antes/depois: taxa de uso correto, exemplos de reescrita de descrição, decisões de merge/split de tools).
- Matriz de risco (irreversível × impactante) com justificativa de HITL.

## Critérios de sucesso (mensuráveis)

- Taxa de uso correto de tools ≥ 85% nos 20 casos do workbench (após refatoração ACI).
- HITL funcionando para 100% das ações destrutivas (cancelar, reembolsar) com confirmação, dry-run e log.
- Relatório documenta melhoria quantitativa de taxa de uso correto (antes vs depois) em pelo menos 3 tools.
- Todas as tools possuem tratamento de erro que retorna mensagem útil ao modelo (não exceção não-tratada).
- Workbench é reproduzível com um único comando e gera relatório automático.

## Competências avaliadas

- C1 Programação Agêntica — nível **I** (integração de tools em agente funcional).
- C3 MCP & Tool Use — nível **I** (design de ACI, schemas, idempotência, HITL).
- C5 AgentOps & Avaliação — nível **B** (workbench, métricas de uso de tools).
- C6 Agent Security — nível **B** (matriz de risco, HITL, allowlist de ações).

## Referências

- Apostila: `04-Apostilas/ETHAGT02/apostila.md`
- Rubrica técnica: `08-Assignments/ETHAGT02/assignment-01.md`
