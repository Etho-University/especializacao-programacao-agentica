# ETHAGT11 — Perguntas para Discussão

> Perguntas para estimular debate durante e após a aula.
> Organizadas por profundidade: rápida (1-2 min) → média (3-5 min) → profunda (10+ min).

---

## Perguntas Rápidas (1-2 min)

### Q1 — Pior Crash em Produção
"Qual o pior crash que você já viu em produção? Quanto tempo/work foi perdido?"
- **Objetivo**: Criar engajamento e dor real antes de introduzir durable execution
- **Slide**: 5
- **Ação**: Deixar 2-3 alunos compartilharem histórias

### Q2 — Síncrono ou Assíncrono?
"Suas tools de agente hoje são síncronas ou assíncronas? Por quê?"
- **Objetivo**: Calibrar prática atual da turma
- **Slide**: 12
- **Resposta esperada**: Maioria é síncrona. Discutir quando migrar para assíncrono.

### Q3 — Experiência com Brokers
"Quem aqui já usou Kafka, RabbitMQ ou NATS em produção? Qual?"
- **Objetivo**: Calibrar experiência prática com mensageria
- **Slide**: 14
- **Ação**: Contar mãos levantadas

### Q4 — Ordering no Kafka
"Como garantir ordering de mensagens do mesmo agente em Kafka?"
- **Objetivo**: Verificar compreensão do particionamento
- **Slide**: 17
- **Resposta esperada**: Usar agent_id como key → hash(key) % num_partitions → mesma partição → ordering preservado

### Q5 — Orquestração
"Você orquestra via código (workflow engine) ou via agente supervisor?"
- **Objetivo**: Conectar decisão arquitetural com prática atual
- **Slide**: 29
- **Resposta esperada**: Híbrido é o ideal — workflow para durability, agente para decisões

---

## Perguntas Médias (3-5 min)

### Q6 — Quando Usar Kafka vs RabbitMQ
"Para o seu sistema hoje: Kafka, RabbitMQ ou NATS? Justifique."
- **Objetivo**: Aplicar o critério de escolha ao caso real
- **Slide**: 22
- **Dica**: Usar a árvore de decisão como framework

### Q7 — Idempotência na Prática
"Pensem em uma tool que vocês usam hoje. Ela é idempotente? Como vocês tornariam ela idempotente?"
- **Objetivo**: Aplicar idempotência a um caso real
- **Slide**: 50
- **Ação**: Deixar 1-2 alunos compartilharem. Discutir chaves de idempotência adequadas.

### Q8 — O Que Acontece Se...? (Replay)
"Se uma tool externa mudou de comportamento entre a execução original e o replay, o replay quebra?"
- **Objetivo**: Pensar sobre o que replay faz e não faz
- **Slide**: 45
- **Resposta esperada**: O replay NÃO re-executa activities — usa resultados gravados. Mas a próxima execução após o replay pode se comportar diferente.

### Q9 — HITL no Seu Sistema
"Em quais ações do seu agente você exigiria HITL (human-in-the-loop)? Por quê?"
- **Objetivo**: Aplicar HITL ao caso real
- **Slide**: 40
- **Resposta esperada**: Ações irreversíveis (enviar email, cobrar, deletar) exigem HITL. Ações reversíveis não precisam.

### Q10 — Custo de Recomeçar
"Seu agente processa 10.000 documentos a $0.05 cada. Se cair no documento 8.000, quanto você perde sem durability? E com durability?"
- **Objetivo**: Praticar cálculo de custo de recomputação
- **Slide**: 5, 38
- **Cálculo**: Sem durability: perde $400 (8.000 × $0.05) ao recomeçar. Com durability: perde ~$0.05 (1 documento). Economia: $399.95.

---

## Perguntas Profundas (10+ min)

### Q11 — Event-Driven Sempre é a Resposta?
"Toda aplicação de agente deveria ser event-driven? Justifique."
- **Objetivo**: Pensamento crítico sobre quando NÃO usar event-driven
- **Slide**: 60
- **Resposta esperada**: Falso. Event-driven é overkill para tarefas síncronas e de baixa latência (ex.: responder chat). Use event-driven quando há: desacoplamento real, longa duração, necessidade de replay, ou HITL.
- **Contraponto**: Quando a tarefa é de longa duração ou multi-agente, event-driven é justificado.

### Q12 — Temporal vs Construir do Zero
"Em que cenário vale a pena construir durability do zero em vez de usar Temporal? Como você convenceria um PM?"
- **Objetivo**: Estruturar argumentos de trade-off
- **Slide**: 35
- **Argumentos a favor do Temporal**: durability provada, HITL nativo, replay/debug, ecosystem
- **Argumentos a favor de construir do zero**: aprendizado profundo, sem dependência externa, controle total
- **Para o PM**: custo de manutenção vs custo de licença/servidor; risco de bug em código próprio vs battle-tested

### Q13 — O Maior Risco de Event-Driven
"Qual o maior risco de adotar event-driven sem entender os trade-offs?"
- **Objetivo**: Conscientização sobre armadilhas
- **Slide**: 11
- **Resposta esperada**: Complexidade operacional — você agora opera um broker, monitora lag, gerencia DLQ, debuga distribuído. Sem equipe de platform engineering, event-driven vira pesadelo operacional.

### Q14 — Saga vs 2PC
"Por que saga é preferível a 2PC (two-phase commit) em sistemas distribuídos de agentes?"
- **Objetivo**: Aprofundar em trade-offs transacionais
- **Slide**: 51
- **Resposta**: 2PC bloqueia recursos (lock) durante toda a transação — é lento, frágil, e bloqueia em falha. Saga divide em transações locais com compensação — não bloqueia, é resiliente, mas aceita consistência eventual.

### Q15 — Exactly-Once: Mito ou Realidade?
"Exactly-once delivery existe de verdade ou é mito? Defenda sua posição."
- **Objetivo**: Debate profundo sobre semântica de delivery
- **Slide**: 56
- **Resposta esperada**: Na presença de falhas, exactly-once verdadeiro é impossível (o ACK pode falhar). A prática consagrada é at-least-once + idempotência = "effectively once". Kafka tem "exactly-once semantics" entre producer-broker-consumer, mas ainda requer idempotência no processamento.

---

## Perguntas Bônus (para alunos avançados)

### Q16 — Ordering Global
"Se você precisa de ordering global (todas as mensagens em ordem), como fazer em Kafka?"
- **Objetivo**: Pensar sobre limitações e workarounds
- **Resposta**: Use 1 partição (perde paralelismo) ou use um sequenciador externo (ex.: timestamp global). Para a maioria dos casos, ordering por entidade (key) é suficiente.

### Q17 — Replay e Evolução de Código
"O que acontece se você deployar uma nova versão do workflow enquanto execuções antigas estão em andamento?"
- **Objetivo**: Pensar sobre versionamento de workflows
- **Resposta**: O Temporal detecta non-determinism (se a nova versão muda a sequência de activities) e falha o replay. Solução: versionar workflows via Task Queue por versão, ou usar Patching API do Temporal.

### Q18 — DBOS vs Temporal
"DBOS propõe durable execution via banco de dados transacional. Qual a vantagem vs Temporal?"
- **Objetivo**: Introduzir alternativas emergentes
- **Resposta**: DBOS usa o DB como fonte de verdade — transações ACID garantem durability sem um server separado. Temporal usa um server dedicado. DBOS é mais simples operacionalmente; Temporal é mais maduro e tem ecosystem maior.
