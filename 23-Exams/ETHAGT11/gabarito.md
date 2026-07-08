# ETHAGT11 — Gabarito da Prova
> Restrito a mentores.

## Parte 1 — Conceitos

**1.** **(b)** Correta. Event-driven traz desacoplamento (produtores não conhecem consumidores), escala independente e resiliência. Latência ponta-a-ponta pode até aumentar; debug é *mais* difícil, não mais simples. — *Ref.: Cap. 1 — Por que event-driven (§1.2, §1.3 trade-off).*

**2.** **Falso.** Ordering é garantido **apenas dentro de uma partição**, não globalmente no tópico. Para ordem global é preciso uma única partição (perdendo paralelismo) ou modelar a ordenação via chave. — *Ref.: Cap. 2 — Mensageria (§2.2 Kafka).*

**3.** **(b)** Correta. Durable execution = estado do workflow persistido/checkpointado; sobrevive a queda do processo e pode ser replayado. Kafka (a) persiste mensagens, não a *lógica* do workflow. — *Ref.: Cap. 3 — Orquestração (§3.2 Temporal); Cap. 4 — Durable execution (§4.1).*

**4.** **Falso.** Event-driven escala melhor em cenários de desacoplamento/paralelismo, mas adiciona complexidade, latência e dificuldade de debug. Para fluxos simples/síncronos, orquestração direta pode ser superior. "Sempre" é o erro. — *Ref.: Cap. 1 (§1.3 O trade-off).*

## Parte 2 — Aplicação e trade-off

**5.** Temporal > Kafka puro quando: (i) workflow tem **lógica de múltiplos passos com estado**, timers e HITL de longa duração (Kafka só entrega mensagens, não modela a lógica); (ii) precisa de **replay determinístico** e sobrevivência a crashes do *orquestrador* (não só da mensagem). Kafka puro exige reescrever essa lógica. — *Ref.: Cap. 3 (§3.1 Workflow engine vs agentes); Cap. 4 (§4.1, §4.2).*

**6.** Formas de idempotência em `send_email`: (i) **chave de idempotência** (ex.: `message_id`/`request_id`) armazenada — antes de enviar, verifica se já enviou aquela chave; (ii) **upsert** num registro de envio por `(recipient, dedupe_window)` e só envia se inexistente. Combinar com tabela de "envios confirmados". — *Ref.: Cap. 5 — Patterns de resiliência (§5.2 Idempotência).*

**7.** O partition key determina a partição, e o ordering é garantido **dentro** da partição. Exemplo de bug: usar um key que coloca `delete` e `create` do mesmo `user_id` em partições distintas — o consumidor pode processar o `delete` antes do `create`. Solução: usar `user_id` como key → mesma partição → ordem preservada. — *Ref.: Cap. 2 (§2.2 Kafka); Cap. 6 — Produção (§6.2 Sharding).*

**8.** *At-least-once*: a mensagem pode ser entregue/reprocessada mais de uma vez (rede/retry). *Exactly-once* end-to-end é raro/mítico porque envolve produtor, broker e consumidor com semânticas distintas. Projeta-se **assumindo at-least-once** e tornando consumidores **idempotentes** (chaves de idempotência, dedupe), o que *efetivamente* dá exactly-once no resultado observável. — *Ref.: Cap. 6 — Produção (§6.1 Exactly-once vs at-least-once: mitos e realidade).*

## Parte 3 — Projeto curto

**9.** Saga compensatória "transferência A→B":
```
1. debitar A          ✓   compensar: creditar A de volta
2. creditar B         ✓   compensar: debitar B (se possível)
3. notificar          ✓   compensar: enviar aviso de estorno
```
Se passo 2 falha: compensa 1 (reestitui A) e aborta. Se 3 falha após 1 e 2: compensa 2 e 1 (estorno total) ou marca para reconciliação. Cada compensação deve ser idempotente. — *Ref.: Cap. 2 (§2.5 patterns: saga); Cap. 5 (§5.3 Compensação).*

**10.** Pseudo-código estilo Temporal:
```python
@workflow
def destructive_action(req):
    # checkpoint automático (durable)
    decision = workflow.execute_activity(ask_human_approval, req, start_to_close=timedelta(hours=24))
    if decision != "approved":
        return "cancelled"
    workflow.execute_activity(perform_destructive, req)
    return "done"
```
O `ask_human_approval` é uma activity/signal HITL; se o processo cair, ao reiniciar o workflow retoma do último checkpoint (estado não se perde). — *Ref.: Cap. 4 (§4.3 Human-in-the-loop via timers/signals; §4.4 Replays).*

---

## Erros comuns (parcial/dedução)

- **Q1**: marcar (c) "debug mais simples" → anular (mostra visão invertida do trade-off).
- **Q2**: afirmar ordering global em Kafka → anular; erro central do módulo.
- **Q3**: confundir durable execution com retenção de mensagens (Kafka) ou cache (Redis) → anular.
- **Q4**: defender "sempre mais escalável" → anular; deve reconhecer complexidade/debug.
- **Q7**: não ligar partition key à ordem dentro da partição → até -50%.
- **Q8**: afirmar que exactly-once é trivialmente alcançável → até -50% (não capta o "mito").
- **Q9**: saga sem compensação idempotente ou sem tratar falha no meio → -40%.

Crédito parcial: idempotência descrita conceitualmente sem chave concreta vale até 60%.

---

## Rubrica por questão (pts)

| Q | Tipo | pts | Aceita parcial |
|---|---|---|---|
| 1 | Múltipla escolha | 10 | 0 |
| 2 | V/F justificado | 10 | 5 |
| 3 | Múltipla escolha | 10 | 0 |
| 4 | V/F justificado | 10 | 5 |
| 5 | Trade-off (2 cenários) | 10 | 5 por cenário justificado |
| 6 | Debug (2 formas idempotência) | 10 | 5 por forma concreta |
| 7 | Análise (key + exemplo) | 10 | 5 conceito + 5 exemplo de bug |
| 8 | Trade-off (exactly/at-least) | 10 | 5 distinção + 5 projeto contra |
| 9 | Projeto (saga) | 10 | 2 pts por passo + compensação correta |
| 10 | Projeto (workflow HITL) | 10 | 5 estrutura + 5 durabilidade/HITL |

---

## Nota esperada por perfil

- **5,0**: modela sagas e durable execution corretos, entende mito do exactly-once, justifica Temporal vs Kafka.
- **4,0**: aplica resiliência (retries/idempotência) com pequenas lacunas.
- **3,0**: conhece conceitos mas confunde ordering global vs por partição.
- **<3,0**: afirma que event-driven é sempre mais escalável ou que ordering é global.
