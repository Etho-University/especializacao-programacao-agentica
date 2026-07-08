# ETHAGT09 — Lista de Exercícios

> Curso: Comunicação e Coordenação Multi-Agente. Fixação de conceitos. Use a apostila `04-Apostilas/ETHAGT09/apostila.md` como referência.

## Múltipla escolha

**1. No padrão blackboard, a coordenação entre agentes ocorre via:**

a) Mensagens diretas p2p
b) Um espaço compartilhado de estado onde agentes leem e escrevem
c) Um modelo central de planejamento
d) Voting

**2. No handoff (estilo OpenAI Swarm), o que acontece quando um agente transfere controle?**

a) O agente original é destruído
b) O agente transfere o contexto e o controle para outro agente especializado
c) Os dois agentes passam a rodar em paralelo
d) O usuário deve escolher manualmente

**3. No actor model, a concorrência é gerenciada por:**

a) Locks e mutex
b) Atores que encapsulam estado e se comunicam apenas por mensagens (sem estado compartilhado)
c) Transações distribuídas
d) Semáforos

**4. Em um group chat (estilo AutoGen), o seletor é responsável por:**

a) Gerar a resposta final
b) Decidir qual agente fala a seguir em cada turno
c) Indexar documentos
d) Fazer fine-tuning

## Verdadeiro ou Falso (justificado)

**1.** "Actor model é mais lento que shared-state porque mensagens têm overhead." — Justifique.

**2.** "Em negociação entre agentes, deadlock ocorre quando nenhum agente aceita ceder." — Justifique.

**3.** "O protocolo A2A (Google, 2025) e MCP são complementares, não competidores." — Justifique.

**4.** "Mensagens A2A devem ter schemas versionados para evoluir sem quebrar comunicação." — Justifique.

## Código curto

**1.** Escreva um schema de mensagem A2A (JSON) com versionamento: `message_id`, `from`, `to`, `type`, `content`, `version`.

**2.** Escreva o pseudocódigo de um handoff: agente A avalia se precisa do especialista B, transfere contexto e controle.

**3.** Escreva o pseudocódigo de um seletor round-robin para group chat: alterna entre agentes em ordem fixa.

## Análise de trade-off

**1.** Compare blackboard vs. mensagens diretas (p2p). Quando blackboard é preferível?

**2.** Compare handoff (Swarm) vs. delegação (supervisor). Qual a diferença de controle?

**3.** Para um sistema de diagnóstico médico com 3 especialistas, qual padrão de conversação escolher? Justifique.

## Debug / diagnóstico

**1.** Em um group chat com 4 agentes, dois agentes entram em debate infinito respondendo um ao outro sem progredir. Diagnóstico e 2 correções.

**2.** Um sistema com actor model tem mensagens sendo processadas fora de ordem, causando inconsistência. Diagnóstico e correção.
