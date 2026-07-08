# ETHAGT11 — Exercícios

> Exercícios para aula e para casa.
> Organizados por tipo: em aula, individual, em duplas, projeto.

---

## Exercícios em Aula

### E1 — Síncrono ou Assíncrono? (Votação Rápida)
**Slide**: 13
**Tempo**: 1.5 min
**Formato**: Individual, votação de mão levantada

**Enunciado**: Para cada cenário abaixo, vote: Síncrono (S) ou Assíncrono (A)?

1. Responder pergunta do usuário em chat
2. Processar 10.000 documentos
3. Buscar em RAG e responder
4. Coordenar 3 agentes em pipeline longo

**Gabarito**:
1. S — usuário espera resposta em chat (UX não pode esperar)
2. A — processamento em massa, longa duração
3. S com timeout — baixa latência, mas com fallback se demorar
4. A — coordenação complexa, longa duração

---

### E2 — O Que Acontece Se...? (Discussão em Duplas)
**Slide**: 27
**Tempo**: 2 min
**Formato**: Duplas, 2 min discussão + 1 min compartilhar

**Enunciado**: Após a DEMO Kafka, discutam em duplas:

1. O que acontece se o Agente B processar duas vezes a mesma mensagem?
2. Como garantir que o resultado não seja duplicado?
3. E se o consumer cair após processar mas antes de commitar o offset?

**Gabarito**:
1. Sem idempotência: resultado duplicado (ex.: 2 emails enviados). Com idempotência: só processa 1x.
2. Chave de idempotência — verificar se a mensagem já foi processada antes de processar.
3. At-least-once delivery: ao reiniciar, o consumer volta ao último offset commitado e reprocessa. Por isso idempotência é essencial.

---

### E3 — HITL com Signal (Exercício em Duplas)
**Slide**: 46
**Tempo**: 3 min
**Formato**: Duplas, 2 min discussão + 1 min compartilhar

**Enunciado**: Cenário: agente propõe enviar email para cliente.

Esboce o workflow HITL com:
1. Signal de aprovação (humano aprova/rejeita)
2. Timeout de 24h
3. Ramificações: o que acontece se o humano rejeitar? E se não responder?

**Gabarito esperado**:
- Workflow: agente gera email → `await signal` (aprovado/rejeitado) com `workflow.sleep(24h)` como timeout
- Se aprovado: enviar email
- Se rejeitado: voltar ao agente para revisar e regenerar
- Se timeout (24h): escalar para gerente OU cancelar operação

---

### E4 — Saga Compensatória: Transferência entre Contas (Duplas)
**Slide**: 62
**Tempo**: 5 min
**Formato**: Duplas, 3 min discussão + 2 min apresentar 2 exemplos

**Enunciado**: Sistema de transferência entre contas com 3 passos:
1. Debita conta A
2. Credita conta B
3. Notifica usuário

Para cada passo que pode falhar, escreva:
- A compensação correspondente
- Se a compensação é perfeita (reverte totalmente) ou imperfeita

**Gabarito**:

| Passo que falha | Compensação | Perfeita? |
|---|---|---|
| 1. Debita A falha | Nenhuma (ainda não debitou) | — |
| 2. Credita B falha | Estornar débito em A (devolver valor) | ✅ Perfeita |
| 3. Notifica falha | Estornar crédito em B → devolver débito em A | ⚠️ Imperfeita: se email já saiu parcialmente, não pode "desenviar" |

**Discussão**: Quais compensações não são perfeitas? Por quê?

---

## Exercícios Individuais (para casa)

### E5 — Quando Temporal é Preferível a Kafka Puro?
**Tempo estimado**: 10 min
**Formato**: Individual, escrito

**Enunciado**: Em 3-4 frases, explique quando Temporal é preferível a Kafka puro para orquestração de agentes. Dê um exemplo concreto.

**Critério de avaliação**:
- Menciona durable execution (sobreviver a crashes) ✅
- Menciona HITL (timers/signals) ✅
- Menciona orquestração de workflow (sequência de passos) ✅
- Exemplo é realista ✅

**Exemplo de resposta**:
Temporal é preferível quando você precisa de durable execution (sobreviver a crashes sem perder progresso), HITL (pausar para aprovação humana) e orquestração de workflow (sequência de passos com retries). Kafka puro é mensageria — não oferece durability de execução nem HITL. Exemplo: agente que processa 10.000 tickets, pausa para validação humana em casos ambíguos, e retoma após crash do worker.

---

### E6 — Escrever uma Saga Compensatória
**Tempo estimado**: 20 min
**Formato**: Individual, código ou pseudocódigo

**Enunciado**: Escreva uma saga compensatória para "processar pedido de e-commerce":

Passos:
1. Reservar estoque
2. Processar pagamento
3. Gerar nota fiscal
4. Enviar email de confirmação

Para cada passo, defina:
- A ação principal
- A compensação
- Se a compensação é perfeita ou imperfeita

**Exemplo de resposta**:

```
Passo 1: Reservar estoque
  Compensação: Liberar estoque reservado
  Perfeita: ✅

Passo 2: Processar pagamento
  Compensação: Estornar pagamento
  Perfeita: ✅ (mas pode demorar dias)

Passo 3: Gerar nota fiscal
  Compensação: Cancelar nota fiscal
  Perfeita: ⚠️ (nota já pode ter sido enviada ao SEFAZ)

Passo 4: Enviar email de confirmação
  Compensação: Enviar email de cancelamento
  Perfeita: ❌ (email original já foi enviado — não pode "desenviar")
```

---

### E7 — Idempotência em Tool de "Enviar Email"
**Tempo estimado**: 15 min
**Formato**: Individual, código

**Enunciado**: Implemente idempotência na tool `send_email`:

Requisitos:
- Aceitar `idempotency_key` como parâmetro
- Antes de enviar, verificar se a key já foi processada
- Se já foi: retornar resultado anterior
- Se não foi: enviar, gravar key + resultado, retornar

**Exemplo de resposta (Python)**:
```python
async def send_email(to, subject, body, idempotency_key):
    existing = await db.find("sent_emails", key=idempotency_key)
    if existing:
        return existing.result

    result = await email_provider.send(to, subject, body)
    await db.insert("sent_emails", {
        "key": idempotency_key,
        "result": result,
        "sent_at": datetime.utcnow()
    })
    return result
```

**Poka-yokes aplicados**:
- `idempotency_key` é obrigatório (não pode enviar sem)
- Verificação antes de enviar (evita duplicação)
- Gravação após enviar (garante que próximas chamadas retornam cache)

---

### E8 — Verdadeiro/Falso Justificado
**Tempo estimado**: 10 min
**Formato**: Individual, escrito

**Enunciado**: Responda V ou F e justifique em 2-3 frases:

1. "Event-driven é sempre mais escalável que síncrono."
2. "Kafka garante ordering global de mensagens."
3. "Exactly-once delivery é impossível na presença de falhas."
4. "No Temporal, I/O deve ir em activities, nunca no workflow."
5. "Compensação em saga é equivalente a rollback em transação tradicional."

**Gabarito**:
1. **F** — Event-driven escala horizontalmente, mas introduz overhead de broker, latência e complexidade. Para tarefas simples, síncrono é melhor.
2. **F** — Kafka garante ordering **por partição**, não global. Ordering global só com 1 partição (perde paralelismo).
3. **V** — Na presença de falhas, o ACK pode falhar, tornando impossible distinguir "não recebido" de "recebido mas ACK perdido". A prática é at-least-once + idempotência.
4. **V** — Workflow deve ser determinístico. I/O (HTTP, DB, filesystem) vai em activities para preservar determinismo e permitir replay.
5. **F** — Compensação é uma **ação reversa**, não um rollback. Rollback desfaz atomicamente; compensação reverte o efeito (nem sempre perfeitamente — ex.: email enviado não pode ser "desenviado").

---

### E9 — Trade-offs de Custo em Mensageria
**Tempo estimado**: 15 min
**Formato**: Individual, cálculo

**Enunciado**: Você produz 1 milhão de eventos/dia no Kafka com retenção de 7 dias. Cada evento tem 1KB. Calcule:

1. Volume de disco consumido por retenção
2. Custo mensal de storage (assuma $0.10/GB/mês)
3. Se você aumentar retenção para 30 dias, qual o novo custo?

**Gabarito**:
1. 1M eventos/dia × 7 dias × 1KB = 7GB
2. 7GB × $0.10 = $0.70/mês (storage apenas — sem contar replicação)
3. 1M × 30 × 1KB = 30GB → $3.00/mês

**Nota**: Com replicação fator 3 (comum em Kafka): multiplique por 3. Infraestrutura de broker (CPU, memória) é custo adicional significativo.

---

## Projeto do Módulo

### P1 — Pipeline Event-Driven com Chaos Testing
**Prazo**: 2 semanas
**Formato**: Individual
**Carga**: ~10h

**Descrição**: Projetar e implementar pipeline event-driven para processamento de tickets em massa, com:
- Durable execution (Temporal ou equivalente)
- Retries com backoff
- Idempotência
- Saga compensatória para falhas
- DLQ para tickets irreparáveis

**Entregáveis**:
- Código funcional (repositório Git)
- ADR (Architecture Decision Record) justificando escolhas
- Análise de falhas injetadas (chaos test):
  - Matar worker no meio do processamento
  - Simular API LLM indisponível
  - Simular broker indisponível

**Critério de sucesso**: Pipeline sobrevive a ≥2 falhas injetadas sem perda de dados.

**Avaliação** (rubrica de 4 pilares):

| Pilar | Peso | Critério |
|---|---|---|
| Técnico | 40% | Código funcional, durable execution, chaos test |
| Consultivo | 30% | ADR justifica escolhas arquiteturais |
| Comportamental | 20% | Code review de um colega |
| Prático | 10% | Demo ao vivo: recuperação após crash |

**Nota mínima de aprovação**: 3.0
