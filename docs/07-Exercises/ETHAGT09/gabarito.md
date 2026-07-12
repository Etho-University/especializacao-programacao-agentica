# ETHAGT09 — Gabarito

> Restrito a mentores. Cada resposta justificada com referência à apostila.

## Múltipla escolha

1. **b)** — No padrão blackboard, a coordenação ocorre via um espaço compartilhado de estado onde agentes leem e escrevem contribuições, sem comunicação direta entre eles (Capítulo 3 — Blackboard).

2. **b)** — No handoff, o agente transfere o contexto da conversa e o controle para outro agente especializado, que continua a interação a partir dali (Capítulo 2.3 — Handoff/transfer).

3. **b)** — No actor model, atores encapsulam seu estado internamente e se comunicam apenas por troca assíncrona de mensagens, eliminando a necessidade de locks e estado compartilhado (Capítulo 4 — Actor Model).

4. **b)** — O seletor decide qual agente fala a seguir em cada turno do group chat, podendo ser round-robin, dinâmico (baseado em LLM) ou selector (Capítulo 2.2 — Group chat).

## Verdadeiro ou Falso (justificado)

1. **Falso (depende).** O overhead de mensagens existe, mas o actor model elimina locks, contentions e deadlocks de estado compartilhado, frequentemente sendo mais eficiente em sistemas distribuídos e concorrentes. O trade-off é complexidade vs. robustez (Capítulo 4.4).

2. **Verdadeiro.** Deadlock em negociação ocorre quando nenhum agente aceita ceder e o sistema não tem mecanismo de quebra (timeout, mediator, ou fallback). É necessário definir regras de convergência (Capítulo 5.3 — Convergência e deadlock).

3. **Verdadeiro.** A2A (agent-to-agent) resolve comunicação entre agentes; MCP resolve conexão de agentes a ferramentas/dados. São camadas complementares na stack multi-agente (Capítulo 6.2 — MCP vs A2A).

4. **Verdadeiro.** Schemas versionados permitem que agentes com versões diferentes da mensagem continuem interoperando (ou falhem graciosamente), evitando quebras quando o protocolo evolui (Capítulo 1.3 — Schemas de mensagem).

## Código curto

1. **Schema de mensagem A2A:**
```json
{
  "message_id": "msg-001",
  "version": "1.0",
  "from": "agent-researcher",
  "to": "agent-critic",
  "type": "review_request",
  "content": {"text": "Revise esta hipótese...", "context": "..."},
  "timestamp": "2026-07-08T10:00:00Z"
}
```
Referência: Capítulo 1.3 (Schemas de mensagem).

2. **Handoff:**
```python
def maybe_handoff(agent_a, query, context):
    if needs_specialist(query):
        return handoff(to="agent_b", context=context + [query])
    return agent_a.respond(query)
```
Referência: Capítulo 2.3 (Handoff/transfer).

3. **Seletor round-robin:**
```python
def round_robin_selector(agents, messages):
    idx = len(messages) % len(agents)
    return agents[idx]
```
Referência: Capítulo 2.2 (Group chat, round-robin).

## Análise de trade-off

1. **Blackboard vs. mensagens diretas:** Blackboard é preferível quando o problema é dinâmico, múltiplos especialistas contribuem para uma solução compartilhada, e a ordem de contribuição não é fixa. Mensagens diretas são melhores quando a interação é estruturada e sequencial entre agentes específicos (Capítulo 3.3).

2. **Handoff vs. delegação (supervisor):** No handoff, o controle transfere completamente para o novo agente (sem retorno automático). Na delegação, o supervisor mantém controle e recebe o resultado de volta. Handoff é melhor para transferência de especialidade; delegação é melhor para orquestração hierárquica (Capítulo 2.3 e exercícios do syllabus).

3. **Diagnóstico médico (3 especialistas):** Group chat com seletor dinâmico — cada especialista contribui com sua perspectiva, um mediator sintetiza. O seletor garante que todos contribuam e evita dominância de um só (Capítulo 2.2).

## Debug / diagnóstico

1. **Diagnóstico:** Falta de condição de convergência — não há mecanismo para encerrar o debate. **Correções:** (1) Definir máximo de turnos por agente ou total; (2) Introduzir um seletor/mediator que detecte repetição e force síntese (Capítulo 5.3).

2. **Diagnóstico:** Mensagens assíncronas sem ordenação garantida. **Correção:** Usar ordering por chave/partição (se via fila) ou timestamps com buffer de reordenação; garantir que atores dependentes processem em sequência (Capítulo 1.4 e 4).
