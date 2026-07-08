# ETHAGT09 — Exercícios

> Exercícios para aula e para casa.
> Organizados por tipo: em aula, individual, em duplas, projeto.

---

## Exercícios em Aula

### E1 — Topologia Ideal (Votação Rápida)
**Slide**: 15
**Tempo**: 2 min
**Formato**: Individual, votação de mão levantada

**Enunciado**: Para cada cenário, vote a topologia + garantia de entrega ideais:

1. "Triager despacha para especialista"
2. "3 agentes votam em um diagnóstico"
3. "Agente publica evento de conclusão"
4. "Negociação comprador/vendedor"

**Gabarito**:
1. P2P + handoff (Swarm)
2. Broadcast + at-least-once (garantir que todos votem)
3. Pub/Sub + at-most-once (fire-and-forget é suficiente)
4. P2P + exactly-once (não pode duplicar nem perder proposta)

---

### E2 — Padrão de Conversação Ideal (Votação)
**Slide**: 26
**Tempo**: 2 min
**Formato**: Individual, votação de mão levantada

**Enunciado**: Para cada cenário, vote o padrão de conversação ideal:

1. "Writer e reviewer refinam um texto"
2. "3 especialistas debatem diagnóstico"
3. "Triager encaminha para dept correto"
4. "Equipe de dev constrói um feature"

**Gabarito**:
1. Two-agent dialogue (CAMEL) — refinamento iterativo entre 2 perspectivas
2. Group chat com selector — múltiplas especialidades, ordem imprevisível
3. Handoff (Swarm) — roteamento baseado em especialização
4. MetaGPT (SOPs) — workflow estruturado com papéis

---

### E3 — Blackboard ou Mensagens? (Duplas)
**Slide**: 33
**Tempo**: 2 min
**Formato**: Duplas, 2 min discussão + compartilhar

**Enunciado**: Discutam em duplas: blackboard ou mensagens diretas para:

1. "5 agentes contribuem com partes de um relatório"
2. "Agente pergunta preço a outro"
3. "3 agentes debatem com estado compartilhado"

**Gabarito**:
1. Blackboard — contribuições independentes, N grande, baixo acoplamento
2. Mensagem direta — P2P, ordem controlada, 2 agentes
3. Blackboard — estado compartilhado, múltiplos especialistas

---

### E4 — Schema de Mensagem A2A (Duplas)
**Slide**: 64
**Tempo**: 3-4 min
**Formato**: Duplas, 3 min discussão + compartilhar no quadro

**Enunciado**: Em duplas, escrevam um schema JSON de mensagem A2A para negociação comprador/vendedor. Incluam:
- Campos obrigatórios: `sender`, `receiver`, `message_type`, `payload`, `timestamp`, `version`
- Como representar: proposta, contraproposta, aceitação
- Versionamento (semver)

**Exemplo de resposta**:
```json
{
  "message_id": "msg_001",
  "sender": "agent://buyer-01",
  "receiver": "agent://seller-02",
  "message_type": "propose",
  "version": "1.0.0",
  "timestamp": "2026-07-07T14:30:00Z",
  "in_reply_to": null,
  "payload": {
    "item": "produto-x",
    "price": 100.00,
    "currency": "BRL",
    "deadline": "2026-07-07T15:00:00Z"
  }
}
```

**message_type** pode ser: `propose`, `counter_propose`, `accept`, `reject`.

---

### E5 — Pergunta da DEMO (Duplas)
**Slide**: 44
**Tempo**: 2 min
**Formato**: Duplas, 2 min discussão

**Enunciado**: Após a DEMO de 2 arquiteturas, discutam:

1. "Qual arquitetura foi mais fácil de debugar? Por quê?"
2. "Em qual delas adicionar um 4º agente seria mais simples?"

**Gabarito**:
1. Blackboard — estado centralizado é fácil de inspecionar. Group chat exige rastrear a sequência de mensagens.
2. Blackboard — novo agente só precisa ler/escrever o blackboard. Group chat exige registrar o agente no manager.

---

## Exercícios Individuais (para casa)

### E6 — Escreva um Schema A2A com Versionamento
**Tempo estimado**: 15 min
**Formato**: Individual, código

**Enunciado**: Escreva um schema JSON completo para uma mensagem A2A entre dois agentes que colaboram em um diagnóstico médico. Inclua:
- Campos obrigatórios (`sender`, `receiver`, `message_type`, `payload`, `timestamp`, `version`)
- Campo `payload` com subcampos para hipótese diagnóstica, confiança e evidências
- Estratégia de versionamento (semver no campo `version`)
- Justifique como o schema evolui: v1 não tem `priority`, v2 adiciona — como v1 reage?

**Critério de avaliação**:
- Schema é JSON válido com todos os campos obrigatórios ✅
- Payload tem subcampos apropriados para diagnóstico ✅
- Versionamento é semver ✅
- Justificativa de compatibilidade backward é correta (v1 ignora campos novos) ✅

---

### E7 — Verdadeiro/Falso Justificado
**Tempo estimado**: 10 min
**Formato**: Individual, escrito

**Enunciado**: Responda V ou F e justifique em 2-3 frases:

1. "Actor model é mais lento que shared-state."
2. "Handoff (Swarm) e delegação (supervisor) são a mesma coisa."
3. "Blackboard escala melhor que mensagens diretas quando N é grande."
4. "MCP e A2A Protocol são competidores."
5. "Em negociações, max_rounds é opcional se os agentes forem bem projetados."

**Gabarito**:
1. **F** — Em cenários de alta concorrência, actor model escala melhor sem locks. Shared state sofre com deadlocks e race conditions.
2. **F** — Handoff transfere controle (agente original sai). Delegação mantém supervisor esperando retorno.
3. **V** — Blackboard é O(N) conexões; mensagens diretas são O(N²). Com N grande, blackboard escala melhor.
4. **F** — São complementares. MCP = agent↔system (tools). A2A = agent↔agent (delegação).
5. **F** — max_rounds é guardrail de segurança. Sem ele, agentes podem entrar em loop infinito.

---

### E8 — Trace de Negociação
**Tempo estimado**: 20 min
**Formato**: Individual, código

**Enunciado**: Dado o seguinte trace de negociação, identifique:
1. Quem cedeu primeiro?
2. Qual foi a zona de acordo?
3. Quantos rounds até convergir?
4. Se houvesse deadlock, qual seria a mitigação?

```
[Round 1] Buyer propõe: 80   | Seller contrapropõe: 200
[Round 2] Buyer propõe: 100  | Seller contrapropõe: 180
[Round 3] Buyer propõe: 120  | Seller contrapropõe: 160
[Round 4] Buyer propõe: 140  | Seller aceita
```

**Gabarito**:
1. Ambos cederam gradativamente (buyer subiu de 80→140; seller desceu de 200→140)
2. Zona de acordo: 140 (buyer aceitou pagar até ~150; seller aceitou receber a partir de ~130)
3. 4 rounds
4. max_rounds, timeout, concessão forçada, escalar para mediator

---

## Projeto do Módulo

### P1 — Sistema de Negociação Entre Agentes
**Prazo**: 2 semanas
**Formato**: Individual ou em duplas
**Carga**: ~8h

**Descrição**: Implementar um sistema de negociação entre agentes (comprador/vendedor OU especialistas debatendo um diagnóstico). O sistema deve:

1. Usar mensagens estruturadas (schema A2A com versionamento)
2. Implementar estratégia de negociação (bargaining com concessão ou auction)
3. Ter max_rounds e timeout configuráveis
4. Logar todas as mensagens (traces)

**Entregáveis**:
- Repositório Git com o código
- Traces de execução mostrando convergência e falha
- Análise de convergência: % de casos que convergem
- Análise de falhas: documentar casos que não convergiram e por quê

**Critério de sucesso**:
- Convergência em ≥ 80% dos casos de teste (≥10 cenários)
- Análise de falhas documentada (deadlock, timeout, rejeição)
- Schema de mensagem versionado
- Traces legíveis e debugáveis

**Avaliação** (rubrica de 4 pilares):

| Pilar | Peso | Critério |
|---|---|---|
| Técnico | 40% | Código funcional, schema, traces, qualidade da implementação |
| Consultivo | 30% | Defesa arquitetural — justificar escolha de padrão de negociação |
| Comportamental | 20% | Code review de um colega (ou dupla) |
| Prático | 10% | Demo ao vivo: agentes negociando em tempo real |

**Nota mínima de aprovação**: 3.0
