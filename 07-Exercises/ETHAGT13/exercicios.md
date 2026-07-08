# ETHAGT13 — Lista de Exercícios

> Curso: Segurança & Governança de Agentes. Fixação de conceitos. Use a apostila `04-Apostilas/ETHAGT13/apostila.md` como referência.

## Múltipla escolha

**1. Na injeção de prompt indireta, o vetor de ataque é:**

a) O usuário digita instruções maliciosas diretamente
b) Instruções maliciosas são embutidas em documentos/recursos que o agente recupera (ex.: RAG, MCP resources)
c) Ataque de força bruta à API
d) SQL injection

**2. Qual é uma defesa contra prompt injection?**

a) Usar modelos maiores
b) Delimitadores claros entre instrução e dados, system prompt robusto, classificadores, instrução-hierarchy
c) Desligar as tools
d) Aumentar a temperatura

**3. "Constitutional AI" (Anthropic) é uma abordagem que:**

a) Substitui o fine-tuning
b) Usa um conjunto de princípios (constituição) para que o modelo auto-avalie e corrija suas respostas
c) É um vector database
d) É um protocolo de comunicação

**4. Em policy-as-code (ex.: OPA/rego), a vantagem sobre políticas em prosa é:**

a) É mais barata
b) Políticas são versionáveis, testáveis e aplicadas deterministicamente em runtime
c) É mais rápida de escrever
d) Não precisa de manutenção

## Verdadeiro ou Falso (justificado)

**1.** "Modelos maiores são sempre mais seguros." — Justifique.

**2.** "HITL sozinho é defesa suficiente contra prompt injection." — Justifique.

**3.** "Em multi-agente, a propagação de comprometimento é um risco — um agente comprometido pode induzir outros." — Justifique.

**4.** "Red team deve ser uma atividade contínua, não apenas pontual antes do deploy." — Justifique.

## Código curto

**1.** Escreva uma política OPA (rego) que veta a execução de uma tool `deploy` fora do horário comercial (9h-18h).

**2.** Escreva o pseudocódigo de um guardrail de output que verifica se a resposta contém PII antes de retornar ao usuário.

**3.** Escreva um exemplo de prompt injection indireta: um documento recuperado por RAG contendo instrução maliciosa embutida.

## Análise de trade-off

**1.** Compare defesa em profundidade (múltiplas camadas) vs. single defense. Por que múltiplas camadas são necessárias?

**2.** Compare structured outputs como defesa vs. classificadores de input/output. Quando combinar?

**3.** Compare sandboxing de MCP servers vs. allowlist de servers. O que cada mitiga?

## Debug / diagnóstico

**1.** Um agente de suporte ao cliente começa a revelar informações de outros clientes quando recebe um ticket com texto suspeito. Diagnóstico do ataque e 3 mitigações.

**2.** Um red team descobre que um jailbreak específico funciona 100% das vezes. Estruture um plano de mitigação em 3 camadas.
