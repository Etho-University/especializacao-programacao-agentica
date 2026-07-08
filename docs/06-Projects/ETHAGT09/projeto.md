# ETHAGT09 — Projeto do Módulo: Sistema de Negociação Multi-Agente

> Curso: Comunicação e Coordenação Multi-Agente (A2A · blackboard · actor model) · Pilar: Técnico 40% + Prático 10% · Equipe: individual ou dupla

## Contexto / Cenário

Uma plataforma de *marketplace* B2B quer automatizar a negociação de contratos de fornecimento entre compradores e vendedores representados por agentes. Cada agente tem objetivos parcialmente conflitantes: o agente comprador minimiza preço e maximiza prazo de garantia; o agente vendedor maximiza margem e volume. Há um agente mediador que propõe ajustes quando as partes entram em deadlock. A plataforma precisa demonstrar que os agentes convergem para um acordo em um percentual alto dos cenários, e que os casos de falha (deadlock, divergência) são compreendidos e documentados. A coordenação ocorre via troca estruturada de mensagens (schemas versionados), podendo usar padrão blackboard ou mensagens diretas.

## Objetivo

Implementar um sistema de negociação entre agentes (comprador/vendedor/mediador, ou especialistas debatendo um diagnóstico clínico) com comunicação A2A estruturada (schemas versionados). Entregar traces completos das negociações e uma análise de convergência que demonstre o percentual de acordos alcançados e categorize as falhas.

## Requisitos

### Funcionais

1. ≥3 agentes com objetivos distintos e parcialmente conflitantes (comprador, vendedor, mediador — ou equivalente: especialistas de diagnóstico).
2. Comunicação A2A com schema de mensagem versionado (estrutura, versão, timestamp, remetente, destinatário, payload tipado).
3. Padrão de coordenação implementado: mensagens diretas (request/response) ou blackboard (espaço compartilhado).
4. Agente mediador propõe ajustes quando detecta deadlock ou estagnação (delta de proposta abaixo de limiar por N rodadas).
5. Negociação com limite de rodadas e condição de parada (acordo, rejeição, ou timeout).
6. Cada agente mantém estado interno (preferências, reserva, histórico de propostas).

### Não-funcionais

- Traces completos de cada negociação (todas as mensagens trocadas, com timestamps).
- Reprodutível: seed de execução fixa produz resultados comparáveis.
- Latência total de uma negociação ≤ 30 segundos.
- Custo por negociação documentado (tokens de LLM consumidos).
- Suíte de ≥30 cenários de negociação com ground truth (acordo esperado ou deadlock esperado).

## Entregáveis

- Código (repositório com agentes, schemas de mensagem, executor de cenários).
- Traces de ≥10 negociações representativas (acordos, deadlocks, mediações).
- Análise de convergência: taxa de acordos, número médio de rodadas, casos de falha categorizados.
- ADR de padrão de coordenação (mensagens diretas vs blackboard: justificativa).

## Critérios de sucesso (mensuráveis)

- Convergência (acordo alcançado) em ≥80% dos cenários de teste (≥30 cenários).
- Análise de falhas documentada: ≥3 categorias de falha (deadlock, divergência irredutível, timeout) com exemplos.
- Agente mediador intervém corretamente em ≥70% dos cenários de deadlock simulados.
- Schema de mensagem é versionado e backward-compatible (demonstrado com ≥2 versões).
- Traces completos permitem *replay* e auditoria de qualquer negociação.

## Competências avaliadas

- C1 Programação Agêntica — nível **A** (sistema multi-agente funcional).
- C2 Multi-Agent Systems — nível **I** (padrões A2A, negociação, resolução de conflito).
- C3 MCP & Tool Use — nível **B** (tools de consulta usadas pelos agentes na negociação).
- C4 Agent Memory — nível **B** (estado interno de cada agente persistido durante a negociação).
- C5 AgentOps & Avaliação — nível **B** (traces, análise de convergência, métricas).

## Referências

- Apostila: `04-Apostilas/ETHAGT09/apostila.md`
- Rubrica técnica: `08-Assignments/ETHAGT09/assignment-01.md`
