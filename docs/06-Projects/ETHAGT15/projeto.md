# ETHAGT15 — Projeto do Módulo: Meta-Agente com Otimização Automatizada

> Curso: Meta-Agentes & Sistemas Autoaprendentes (agents that build agents) · Pilar: Técnico 40% + Prático 10% · Equipe: individual ou dupla

## Contexto / Cenário

O time de pesquisa aplicada de uma empresa de IA percebeu que gasta dezenas de horas por semana ajustando prompts e descrições de tools manualmente para cada novo domínio de cliente (jurídico, financeiro, saúde). Cada ajuste é tentativa-e-erro subjetivo. A diretoria de P&D quer explorar se um *meta-agente* pode automatizar essa otimização: dado um domínio e um benchmark, o sistema otimiza prompts/tools automaticamente (via DSPy ou equivalente), mede o ganho, e valida o agente otimizado em eval antes de liberar. Há preocupação legítima com riscos: recursão descontrolada, *goal drift* (o otimizador otimiza a métrica errada), e segurança. O projeto deve demonstrar o ganho *e* as salvaguardas.

## Objetivo

Implementar um sistema onde prompts e/ou tools são otimizados automaticamente (ex.: DSPy, Promptbreeder, ou otimizador próprio) sobre um benchmark de domínio. Medir o ganho antes/depois da otimização de forma reproduzível, e implementar salvaguardas (meta-governor, sandbox, veto) que previnam recursão descontrolada e goal drift.

## Requisitos

### Funcionais

1. Meta-agente que otimiza prompts e/ou descrições de tools de um agente-alvo automaticamente.
2. Benchmark de domínio com ≥25 casos e métrica objetiva (success rate, score, ou equivalente).
3. Pipeline: agente-alvo (baseline) → meta-agente otimiza → agente-otimizado → eval comparativo.
4. ≥3 iterações de otimização documentadas (cada uma com prompt/tool alterado e ganho medido).
5. Salvaguardas implementadas:
   - Meta-governor: limite de iterações, orçamento de tokens, abortar se métrica degrada.
   - Sandbox: agente-otimizado é validado em eval isolado antes de qualquer deploy.
   - Veto: regra que rejeita otimizações que violem restrições (ex.: segurança, custo).
6. Detecção de goal drift: alerta se a métrica otimizada diverge de métricas de salvaguarda.

### Não-funcionais

- Otimização reproduzível (seed fixa, modelo fixo, versão de DSPy/otimizador fixa).
- Custo total da otimização documentado (pode ser alto, mas deve ser transparente).
- Eval isolado do agente-otimizado (não pode afetar produção durante otimização).
- Logs de cada iteração de otimização (prompt anterior, prompt novo, delta de métrica).

## Entregáveis

- Código (repositório com meta-agente, agente-alvo, benchmark, otimizador).
- Eval comparativo antes/depois (≥25 casos, ≥3 iterações, métrica objetiva).
- Análise crítica (o que funcionou, o que falhou, riscos observados, limites da otimização automática).
- Demo: meta-agente otimizando em tempo real (ou timelapse das iterações).

## Critérios de sucesso (mensuráveis)

- Ganho mensurável e reproduzível: agente-otimizado supera baseline em ≥10% na métrica do benchmark (≥25 casos, re-executável).
- ≥3 iterações de otimização documentadas com delta de métrica por iteração.
- Meta-governor funciona: aborta otimização que degrada métrica ou excede orçamento (demonstrado em ≥1 caso).
- Sandbox isola o agente-otimizado do ambiente de produção durante toda a otimização.
- Análise crítica identifica ≥2 limites ou riscos da otimização automática (ex.: overfit ao benchmark, goal drift).

## Competências avaliadas

- C1 Programação Agêntica — nível **A** (sistema de meta-agência funcional).
- C2 Multi-Agent Systems — nível **A** (meta-agente operando sobre agente-alvo).
- C3 MCP & Tool Use — nível **B** (otimização de descrições de tools).
- C4 Agent Memory — nível **A** (memória de sucesso/falha entre iterações, strategy evolver).
- C6 Agent Security — nível **I** (meta-governor, veto, sandbox, detecção de goal drift).

## Referências

- Apostila: `04-Apostilas/ETHAGT15/apostila.md`
- Rubrica técnica: `08-Assignments/ETHAGT15/assignment-01.md`
