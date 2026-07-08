# ETHAGT11 — Slides Detalhados + Notas do Professor (Parte 2: Slides 39-76)

> Universidade Etho · Especialização em Programação Agêntica
> Cada slide contém: título, objetivo, conteúdo, notas do professor, diagrama, animação, imagem, tempo.

---

## SEÇÃO E — Durable Execution para Agentes (Slides 39-46 · continuação)

---

### Slide 39 — Long-Running Agents (horas, dias)

**Título**: Long-Running Agents (horas, dias)
**Objetivo**: Expandir o horizonte de duração de agentes.
**Conteúdo**:
- Agente tradicional: segundos a minutos (context window limita)
- **Agente durável**: horas, dias, semanas
- Padrão: workflow que chama agente em loop, persistindo estado entre iterações
- Casos: pesquisa longitudinal, monitoramento contínuo, processamento em massa
- **Cuidado**: custo acumulado de tokens — orçamento por execução

**Diagrama**: Timeline expandida — agente rodando por dias com checkpoints
**Animação**: Timeline cresce; checkpoints aparecem ao longo
**Imagem**: Calendário com execução distribuída
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Sem durable execution, agentes estão limitados a segundos/minutos (context window enche, processo cai). Com durable execution, agentes podem rodar por dias: o workflow persiste estado entre iterações, e o agente "acorda" a cada ciclo com contexto fresco. Casos de uso: pesquisa longitudinal (monitorar tema por semanas), processamento de massa (10k documentos), monitoramento contínuo.
💡 ANALOGIA: É como um trabalhador que vai embora às 18h e volta às 9h. Sem "memória" (durable state), ele esquece tudo. Com caderno de anotações (checkpoint), ele retoma exatamente de onde parou.
⚠️ ERROS COMUNS: Alunos esquecem de definir orçamento. Um agente rodando por dias sem limite de tokens pode custar milhares de dólares. Sempre defina budget por execução.
➡️ TRANSIÇÃO: "E se o agente precisa esperar um humano aprovar? HITL."

---

### Slide 40 — Human-in-the-Loop via Timers e Signals

**Título**: Human-in-the-Loop via Timers e Signals
**Objetivo**: Mostrar como HITL funciona em workflows duráveis.
**Conteúdo**:
- **Signal**: mensagem externa entregue ao workflow em execução
- **Timer**: `workflow.sleep(dias)` — pausa durável, não consome recursos
- Padrão HITL: workflow pausa em `await signal` → humano aprova → workflow continua
- **Timeout**: se humano não responde em X → caminho alternativo
- Para agentes: agente propõe ação → workflow pausa → humano aprova → executa

**Diagrama**: Sequência — workflow → pause (await signal) → humano aprova → resume
**Animação**: Workflow pausa (amarelo) → signal chega → resume (verde)
**Imagem**: Diagrama de sequência HITL
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: HITL em workflows duráveis é elegante. O workflow pausa em `await workflow.wait_condition(...)` ou `await signal` — e fica pausado por dias, SEM consumir recursos (não é um thread dormindo; é estado persistido). Quando o humano aprova (envia signal), o workflow acorda e continua. Timeout: se ninguém aprova em 24h, caminho alternativo (ex.: escalar para gerente).
💡 ANALOGIA: É como um email esperando resposta. O email fica na caixa de entrada (estado persistido) sem consumir recursos. Quando você responde, o processo continua. Se você não responde em X dias, tem lembrete automático.
❓ PERGUNTA PARA A TURMA: "Em quais ações do seu agente você exigiria HITL?"
⚠️ ERROS COMUNS: Alunos tentam implementar HITL com polling (loop checando a cada segundo). Isso consome recursos e é frágil. Signals são event-driven — o workflow só acorda quando o signal chega.
➡️ TRANSIÇÃO: "E para debugar tudo isso? Replays."

---

### Slide 41 — Replays e Debug Temporal

**Título**: Replays e Debug Temporal
**Objetivo**: Mostrar o poder do replay para debugging.
**Conteúdo**:
- **Replay**: re-executar workflow usando histórico gravado (sem re-executar activities)
- **Debug temporal**: voltar no tempo, inspecionar estado em qualquer step
- "Time travel debugging" — ver exatamente o que o agente decidiu em cada ponto
- Ferramenta: Temporal Web UI mostra histórico completo de execução

**Diagrama**: Timeline com marcadores de replay navegáveis
**Animação**: Marcadores surgem; cursor "volta no tempo"
**Imagem**: Temporal Web UI screenshot
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Replay é uma superpotência. Quando um workflow falha, você não precisa reproduzir o bug (o que seria caro — requer re-executar tools, chamar APIs). Você faz replay: o Temporal re-executa o código do workflow usando os resultados gravados das activities. Em cada linha, você inspeciona variáveis. É "time travel debugging" — você volta a qualquer ponto da execução e vê o estado.
💡 ANALOGIA: É como uma gravação de DVR. Você pausa, volta, avança. A diferença: em vez de vídeo, você inspeciona estado de código. E os "frames" são os results das activities.
⚠️ ERROS COMUNS: Alunos confundem replay com re-execução. Replay NÃO re-executa activities — usa resultados gravados. É instantâneo e gratuito (não consome APIs).
➡️ TRANSIÇÃO: "Mas replay tem uma armadilha: non-determinism."

---

### Slide 42 — O Problema do Non-Determinism

**Título**: O Problema do Non-Determinism
**Objetivo**: Explicar a armadilha clássica do replay.
**Conteúdo**:
- Replay pressupõe que o workflow re-executa de forma idêntica
- **Non-determinism quebra o replay**:
  - `datetime.now()` → valor diferente a cada replay
  - `random()` → resultado diferente
  - I/O direto no workflow → estado externo mudou
  - Código do workflow alterado entre execução e replay
- **Solução**: todo I/O e não-determinismo vão em activities

**Diagrama**: Replay quebrado (vermelho) vs replay correto (verde)
**Animação**: Replay quebra em non-determinism; replay correto flui
**Imagem**: Comparação lado a lado
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Non-determinism é o inimigo número 1 do replay. O replay re-executa o código do workflow esperando que produza a mesma sequência de chamadas de activities. Se o workflow usa `datetime.now()`, cada replay gera um timestamp diferente — a sequência diverge do histórico — replay quebra. O mesmo com `random()`, I/O direto (o estado externo mudou), ou mudança de código do workflow.
💡 ANALOGIA: É como re-assistir um filme esperando o mesmo final, mas alguém trocou o roteiro no meio. O replay "espera" o mesmo filme; se o código mudou, dá errado.
⚠️ ERROS COMUNS: Alunos deployam nova versão do workflow sem versionar. O Temporal detecta non-determinism e falha o replay. Solução: versionar workflows (Task Queue por versão).
➡️ TRANSIÇÃO: "Vamos ver as regras práticas de código determinístico."

---

### Slide 43 — Determinismo em Código de Workflow

**Título**: Determinismo em Código de Workflow
**Objetivo**: Mostrar as regras práticas de código determinístico.
**Conteúdo**:
- No workflow: usar `workflow.now()`, `workflow.random()` (seeded do histórico)
- No workflow: **NUNCA** fazer I/O direto (HTTP, DB, filesystem)
- No workflow: **NUNCA** usar `time.sleep()` — usar `workflow.sleep()`
- Em activities: tudo permitido (I/O, side effects, chamadas de API)
- Snippet: código correto vs código quebrado lado a lado

**Diagrama**: Dois snippets: "✗ Quebrado" vs "✓ Correto"
**Animação**: Linhas problemáticas destacadas em vermelho; corretas em verde
**Imagem**: Side-by-side code blocks
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: As regras são simples. No workflow: use as APIs determinísticas do Temporal (`workflow.now()`, `workflow.random()`, `workflow.sleep()`). Nunca faça I/O direto. Em activities: tudo permitido — HTTP, DB, filesystem, chamadas de API. A separação é clara: workflow = lógica pura; activity = efeitos colaterais.
💡 ANALOGIA: Workflow é como um contrato (deve ser reproduzível). Activity é como a execução do contrato (tem efeitos no mundo real). Você não muda o contrato a cada assinatura.
⚠️ ERROS COMUNS: Alunos usam `datetime.now()` "só uma vez, não tem problema". Tem. No primeiro replay, quebra. Use `workflow.now()` sempre.
➡️ TRANSIÇÃO: "Vamos ver tudo isso na DEMO ao vivo."

---

### Slide 44 — DEMO: Workflow Durável em Temporal

**Título**: DEMO: Workflow Durável em Temporal
**Objetivo**: Demo ao vivo — agente de longa duração sobrevivendo a kill do processo.
**Conteúdo**:
- Referência: `05-Labs/ETHAGT11/Lab2-Workflow-Temporal`
- Workflow que processa tickets em loop, chamando agente como activity
- Mostrar execução em andamento na Temporal Web UI
- **Kill do worker (Ctrl+C)** → reiniciar → workflow retoma do último ticket
- Sem perda de progresso, sem reprocessamento

**Diagrama**: Terminal + Temporal Web UI lado a lado
**Animação**: Kill → restart → continuação destacada
**Imagem**: Screenshot da Temporal Web UI
**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Demo ao vivo. O workflow processa tickets em loop, chamando o agente como activity a cada ticket. Mostro a execução na Temporal Web UI (localhost:8080). Depois de alguns tickets, faço Ctrl+C no worker. O workflow fica pausado (não há worker). Reinicio o worker — ele pega o histórico, faz replay, e continua do último ticket processado. Zero perda.
💡 ANALOGIA: É como desligar e religar o computador durante uma compilação. Sem durable execution, você recompila do zero. Com Temporal, você continua do arquivo que parou.
❓ PERGUNTA PARA A TURMA: (deixar para o Slide 45)
⚠️ ERROS COMUNS: Se a demo falhar (Temporal indisponível), ter vídeo/screenshot prontos. A demo é o ponto alto — não improvisar.
➡️ TRANSIÇÃO: "Pergunta sobre a demo."

---

### Slide 45 — Pergunta da DEMO

**Título**: Pergunta da DEMO
**Objetivo**: Engajar com pergunta sobre replay e tools externas.
**Conteúdo**:
- "Replay: se uma tool externa mudou de comportamento, o replay quebra?"
- "O que acontece se o agente tomar decisão diferente no replay?"
- Discussão aberta (2 min)

**Diagrama**: Caixa de discussão
**Animação**: Perguntas aparecem uma a uma
**Imagem**: Ícone de discussão
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Respostas: (1) Tool externa mudou de comportamento → o replay NÃO quebra, porque o replay NÃO re-executa activities — usa resultados gravados. Mas a próxima execução (após o replay) pode se comportar diferente. (2) Agente tomar decisão diferente → se o agente é determinístico (mesmo input = mesma output), o replay reproduz a mesma decisão. Se o agente usa temperatura > 0, pode divergir — por isso use temperatura 0 em workflows críticos, ou persista a decisão do agente como activity.
💡 ANALOGIA: É como reassistir um filme. Os atores não refilmam — a gravação (histórico) é replayed. Mas se você for refazer a cena (nova execução), os atores podem improvisar diferente.
⚠️ ERROS COMUNS: Alunos acham que replay re-executa tools. Não re-executa. Replay usa resultados gravados — é instantâneo.
➡️ TRANSIÇÃO: "Vamos praticar HITL."

---

### Slide 46 — Exercício: HITL com Signal

**Título**: Exercício: HITL com Signal
**Objetivo**: Praticar o padrão de human-in-the-loop.
**Conteúdo**:
- Cenário: agente propõe enviar email para cliente
- Em duplas: esboçar o workflow com signal de aprovação + timeout de 24h
- O que acontece se o humano rejeitar? E se não responder?
- 2 min discussão, 1 min compartilhar

**Diagrama**: Esqueleto de workflow para preencher
**Animação**: Campos vazios para preencher
**Imagem**: Template de workflow HITL
**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Exercício em duplas. Esboçar o workflow: (1) agente gera email; (2) workflow pausa esperando signal "aprovado" ou "rejeitado" com timeout 24h; (3) se aprovado → envia; (4) se rejeitado → volta ao agente para revisar; (5) se timeout → escalar para gerente ou cancelar. O ponto é pensar nas ramificações — HITL não é só "esperar aprovação", é tratar todos os caminhos.
💡 ANALOGIA: É como um processo de compra que precisa aprovação do gerente. Se ele aprova, segue. Se rejeita, volta para revisão. Se não responde em 24h, escala.
⚠️ ERROS COMUNS: Alunos esquecem o timeout. Sem timeout, o workflow pode ficar pausado para sempre se o humano ignorar.
➡️ TRANSIÇÃO: "Com HITL dominado, vamos aos patterns de resiliência."

---

## SEÇÃO F — Patterns de Resiliência & Produção (Slides 47-60 · 12 min)

---

### Slide 47 — [SEÇÃO] Patterns de Resiliência

**Título**: Patterns de Resiliência
**Objetivo**: Transição para patterns de resiliência.
**Conteúdo**: "5 — Patterns de Resiliência: Retries, Idempotência, Saga, Circuit Breakers"
**Diagrama**: Fundo `etho-primary`
**Animação**: Fade in do número e título
**Imagem**: —
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Event-driven traz resiliência, MAS falhas ainda acontecem. Precisamos de patterns para lidar com elas: retries (recuperar de falhas temporárias), idempotência (lidar com duplicação), saga (compensar falhas em transações distribuídas), circuit breakers (proteger de falhas em cascata).
➡️ TRANSIÇÃO: "Comecemos pelo mais fundamental: retries."

---

### Slide 48 — Retries com Backoff (Exponential, Jitter)

**Título**: Retries com Backoff
**Objetivo**: Apresentar o pattern mais fundamental de resiliência.
**Conteúdo**:
- Retry simples: tentar N vezes
- **Backoff exponencial**: 1s → 2s → 4s → 8s → 16s
- **Jitter**: adicionar aleatoriedade para evitar thundering herd
- Limite de tentativas + circuit breaker quando excedido
- Para agentes: retry em tool calls com timeout
- Snippet: função `retry_with_backoff()`

**Diagrama**: Timeline de retries com backoff crescente (1s, 2s, 4s, 8s)
**Animação**: Tentativas aparecem com intervalos crescentes
**Imagem**: Gráfico de backoff exponencial
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Retry é o pattern mais fundamental. Se uma chamada falha (rede, timeout), tentar de novo. Mas retries ingênuos causam problemas: se 1000 clientes retentam simultaneamente, você causa um "thundering herd" que derruba o servidor. Solução: backoff exponencial (espera cresce a cada tentativa) + jitter (aleatoriedade para dessincronizar). Temporal oferece retry com backoff embutido nas RetryOptions.
💡 ANALOGIA: É como tentar ligar para alguém ocupado. Em vez de discar a cada segundo (piora), espere 1s, depois 2s, depois 4s. E se 100 pessoas estiverem tentando a mesma hora, cada uma espera um tempo levemente diferente (jitter).
⚠️ ERROS COMUNS: Alunos usam retry sem backoff. Isso causa thundering herd e piora a situação. Sempre use backoff exponencial com jitter.
➡️ TRANSIÇÃO: "Mas retry só é seguro se a operação for idempotente."

---

### Slide 49 — Idempotência (Chaves de Idempotência)

**Título**: Idempotência
**Objetivo**: Explicar por que idempotência é essencial em event-driven.
**Conteúdo**:
- **At-least-once delivery**: mensagens podem chegar mais de uma vez
- **Idempotência**: processar 2x = processar 1x (mesmo resultado)
- **Chave de idempotência**: ID único por operação
- Antes de processar: verificar se já processou aquela chave
- Armazenar chaves processadas (Redis, DB)

**Diagrama**: Fluxo — recebe mensagem → checa chave → já processou? → ignora/processa
**Animação**: Fluxo de decisão com branch "já processou"
**Imagem**: Diagrama de idempotência
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Idempotência é o complemento essencial do retry. Se você retenta, pode processar a mesma operação 2x. Se a operação é "enviar email", você manda 2 emails. Solução: cada operação tem uma chave de idempotência única. Antes de processar, verifique se a chave já foi processada. Se sim, retorne o resultado anterior. Se não, processe e armazene a chave.
💡 ANALOGIA: É como um carimbo "PAGO" em uma fatura. Se alguém tentar pagar a mesma fatura de novo, o carimbo impede. A chave de idempotência é o carimbo digital.
❓ PERGUNTA PARA A TURMA: "Quais das suas tools hoje são idempotentes?"
⚠️ ERROS COMUNS: Alunos acham que "se eu não retento, não preciso de idempotência". Errado — at-least-once delivery pode duplicar mesmo sem retry da sua parte (network glitch após processar, antes do ACK).
➡️ TRANSIÇÃO: "Vamos aplicar idempotência em um caso concreto."

---

### Slide 50 — Idempotência em Tool de "Enviar Email"

**Título**: Idempotência: Tool "Enviar Email"
**Objetivo**: Aplicar idempotência em um caso concreto.
**Conteúdo**:
- Tool: `send_email(to, subject, body, idempotency_key)`
- Antes de enviar: `SELECT 1 FROM sent_emails WHERE key = ?`
- Se existe: retornar resultado anterior (não reenvia)
- Se não existe: enviar, gravar key + resultado, retornar
- **Pergunta**: *Como garantir idempotência em tool de "enviar email"?*

**Diagrama**: Code block + fluxo de decisão
**Animação**: Fluxo de decisão com branch "existe?"
**Imagem**: Snippet Python
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Caso concreto. A tool `send_email` recebe `idempotency_key` (gerada pelo chamador — ex.: hash do conteúdo + timestamp). Antes de enviar, consulta o DB: se a key já existe, retorna o resultado anterior (não reenvia). Se não existe, envia, grava a key + resultado no DB. Próxima chamada com a mesma key retorna o resultado gravado. Resultado: mesmo que o agente retente 10x, só 1 email é enviado.
💡 ANALOGIA: É como um cofre com código. Você só abre uma vez com aquele código. Tentar de novo não abre nada novo.
⚠️ ERROS COMUNS: Alunos usam "idempotency_key = email_content_hash". Se o conteúdo muda (ex.: timestamp no corpo), a hash muda e você perde idempotência. Use keys estáveis (ex.: request_id, message_id do Kafka).
➡️ TRANSIÇÃO: "Idempotência é para operações individuais. E para transações distribuídas? Saga."

---

### Slide 51 — Compensação: Saga Pattern

**Título**: Compensação: Saga Pattern
**Objetivo**: Aprofundar o padrão saga.
**Conteúdo**:
- **Saga**: sequência de transações locais com compensação
- Passo 1 (execute) → Passo 2 (execute) → Passo 3 (FALHA)
- Compensar Passo 2 → Compensar Passo 1
- Não é rollback — é uma **ação reversa** (nem sempre perfeita)
- Dois estilos: **orquestrada** (central) vs **coreografada** (eventos)

**Diagrama**: `12-Diagrams/ETHAGT11/saga.mmd`
**Animação**: Passos executam → falha → compensações revertem
**Imagem**: Diagrama saga completo
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Saga resolve transações distribuídas. Em vez de 2PC (two-phase commit — caro, frágil, bloqueia recursos), você divide em transações locais. Cada passo tem uma compensação. Se o passo 3 falha, você executa as compensações dos passos 2 e 1 (em ordem reversa). Importante: compensação NÃO é rollback — é uma ação que reverte o efeito. Nem sempre é perfeita (ex.: se você já enviou uma notificação, não pode "desenviar").
💡 ANALOGIA: É como planejar uma festa. Se o buffet cancela (passo 3 falha), você cancela o salão (compensação 2) e devolve os convites (compensação 1). Não é "desfazer" — é reverter o efeito. Alguns convidados já leram o convite — não pode "desler".
⚠️ ERROS COMUNS: Alunos acham que saga é rollback. Não é. Compensação é melhor esforço. Algumas operações não têm compensação perfeita (enviar email, fazer cobrança).
➡️ TRANSIÇÃO: "Vamos a um caso concreto: transferência bancária."

---

### Slide 52 — Saga: Transferência entre Contas

**Título**: Saga: Transferência entre Contas
**Objetivo**: Caso concreto de saga compensatória.
**Conteúdo**:
- Transferência: **debita** conta A → **credita** conta B → **notifica** usuário
- Se "notifica" falha: compensar "credita B" (estorna) → compensar "debita A" (devolve)
- **Saga orquestrada**: orquestrador coordena passos e compensações
- **Saga coreografada**: cada serviço publica evento e reage
- Exercício do syllabus: escrever a lógica de compensação

**Diagrama**: Fluxo saga com 3 passos + 3 compensações
**Animação**: Passos executam → falha na notificação → compensações revertem
**Imagem**: Diagrama saga de transferência
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Caso clássico de saga. Transferência entre contas: (1) debita A, (2) credita B, (3) notifica usuário. Se o passo 3 falha (serviço de notificação down), você compensa: estorna crédito em B, devolve débito em A. O usuário não foi notificado, mas o dinheiro voltou. Saga orquestrada: um orquestrador (ex.: Temporal workflow) coordena. Saga coreografada: cada serviço publica eventos e reage (ex.: servico de crédito escuta evento "débito feito" e credita).
💡 ANALOGIA: É como uma devolução na loja. Você não "desfaz" a compra — você faz uma operação reversa (estorno). O dinheiro volta, mas a transação original continua existindo.
❓ PERGUNTA PARA A TURMA: "Qual compensação não é perfeita neste caso?" (Resposta: notificação — se o email saiu, não pode "desenviar".)
⚠️ ERROS COMUNS: Alunos esquecem que compensações também podem falhar. Saga precisa de retry nas compensações também.
➡️ TRANSIÇÃO: "Outro pattern essencial: circuit breaker."

---

### Slide 53 — Circuit Breakers

**Título**: Circuit Breakers
**Objetivo**: Introduzir circuit breaker para proteger tools falhando.
**Conteúdo**:
- Estados: **CLOSED** (normal) → **OPEN** (falhando, rejeita) → **HALF-OPEN** (testa)
- Após N falhas consecutivas: **OPEN** (para de chamar a tool)
- Após timeout: **HALF-OPEN** (permite 1 tentativa)
- Se sucesso: **CLOSED**; se falha: **OPEN**
- Para agentes: se uma tool de API está down, circuit breaker evita desperdício de tokens

**Diagrama**: State machine — Closed → Open → Half-Open → Closed/Open
**Animação**: Transições entre estados (destacar estado atual)
**Imagem**: State machine diagram
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Circuit breaker protege sistemas de falhas em cascata. Normal: CLOSED (todas as chamadas passam). Se N chamadas falham consecutivamente: OPEN (todas rejeitadas imediatamente — sem esperar timeout). Depois de um cooldown: HALF-OPEN (uma chamada de teste passa). Se sucesso: volta a CLOSED. Se falha: volta a OPEN. Para agentes: se a API do LLM está down, o circuit breaker evita que o agente gaste tokens em chamadas que vão falhar.
💡 ANALOGIA: É como o disjuntor de casa. Se há sobrecarga, ele "abre" (corta energia). Você não fica tentando ligar os aparelhos. Você espera, reseta o disjuntor (HALF-OPEN), e se não há sobrecarga, volta ao normal (CLOSED).
⚠️ ERROS COMUNS: Alunos implementam retry infinito sem circuit breaker. Se a API está realmente down, retry infinito desperdiça recursos e tokens.
➡️ TRANSIÇÃO: "Esses patterns se combinam. Vamos ver como."

---

### Slide 54 — Composição de Patterns

**Título**: Composição de Patterns
**Objetivo**: Mostrar como os patterns se combinam.
**Conteúdo**:
- **Retry + Idempotência**: retry é seguro porque idempotência garante não-duplicação
- **Saga + Idempotência**: compensações são idempotentes
- **Circuit Breaker + Retry**: breaker protege; retry recupera
- **Durable Execution + tudo**: Temporal oferece retry, timeout, idempotência embutidos
- **Regra**: não reinvente — Temporal já tem a maioria

**Diagrama**: Matriz de composição
**Animação**: Combinações aparecem uma a uma
**Imagem**: Grid de patterns
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Os patterns não são isolados — se combinam. Retry + Idempotência: o retry pode duplicar, mas a idempotência garante que duplicar não causa efeito. Saga + Idempotência: compensações devem ser idempotentes (se a compensação for retentada, não deve "desfazer" 2x). Circuit Breaker + Retry: o breaker para de chamar quando há muitas falhas; o retry recupera em HALF-OPEN. Temporal oferece tudo isso embutido.
💡 ANALOGIA: É como equipamentos de segurança do carro. Cinto (idempotência), airbag (compensação), ABS (circuit breaker). Cada um protege de um tipo de falha; juntos, maximizam segurança.
⚠️ ERROS COMUNS: Alunos reinventam patterns que o Temporal já oferece. Retry, timeout, idempotência — tudo configurável no Temporal. Não reescreva.
➡️ TRANSIÇÃO: "Com os patterns dominados, vamos a tópicos de produção."

---

### Slide 55 — [SEÇÃO] Produção: Ordering, Escala, Observabilidade

**Título**: Produção: Ordering, Escala, Observabilidade
**Objetivo**: Transição para tópicos de produção.
**Conteúdo**: "6 — Produção: Ordering, Escala, Observabilidade"
**Diagrama**: Fundo `etho-primary`
**Animação**: Fade in do número e título
**Imagem**: —
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Passamos dos fundamentos para produção. Como colocar event-driven em escala? Como garantir ordering? Como observar pipelines distribuídos?
➡️ TRANSIÇÃO: "Comecemos pelo debate mais quente: exactly-once."

---

### Slide 56 — Exactly-once vs At-least-once

**Título**: Exactly-once vs At-least-once
**Objetivo**: Desconstruir o mito do exactly-once.
**Conteúdo**:
- **At-least-once**: mensagem pode chegar 1+ vezes (default do Kafka)
- **At-most-once**: mensagem pode se perder (fire and forget)
- **Exactly-once**: cada mensagem é processada exatamente 1 vez
- **Realidade**: exactly-once verdadeiro não existe na presença de falhas
- **Prática**: at-least-once + idempotência = "effectively once"
- **Pergunta**: *Exactly-once existe de verdade ou é mito?*

**Diagrama**: Comparação visual dos 3 modelos
**Animação**: 3 colunas aparecem com exemplos
**Imagem**: 3 ícones representando os modelos
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O debate clássico. Exactly-once delivery (cada mensagem entregue exatamente uma vez) é um mito na presença de falhas. O argumento (artigo famoso do Konieczny): para garantir exactly-once, você precisa de um mecanismo de ack que não pode falhar — mas qualquer mecanismo pode falhar. A prática consagrada: at-least-once delivery (pode duplicar) + idempotência no consumidor (duplicar não causa efeito) = "effectively once". É assim que Kafka, NATS, Temporal funcionam na prática.
💡 ANALOGIA: É como o carteiro. Ele pode entregar a mesma carta duas vezes (at-least-once). Mas se o destinatário for idempotente (arquiva por ID, não duplica), o efeito é "uma vez". Exactly-once exigiria um carteiro que nunca erra — não existe.
❓ PERGUNTA PROVOCATIVA PARA A TURMA: "Exactly-once existe de verdade ou é mito?"
⚠️ ERROS COMUNS: Alunos perdem tempo tentando implementar exactly-once. O tempo é melhor investido em idempotência — que é mais simples e robusta.
➡️ TRANSIÇÃO: "Com delivery resolvido, como escalar consumidores?"

---

### Slide 57 — Sharding de Consumidores

**Título**: Sharding de Consumidores
**Objetivo**: Mostrar como escalar consumidores de eventos.
**Conteúdo**:
- **Consumer Group**: partições divididas entre consumers
- **Sharding por chave**: agent_id → partition → consumer dedicado
- Adicionar consumers → rebalanceamento automático
- **Limite**: # consumers ativos ≤ # partições
- Para agentes: cada shard processa um conjunto de agentes

**Diagrama**: Múltiplas partições → múltiplos consumers em paralelo
**Animação**: Consumers surgem; setas de atribuição
**Imagem**: Diagrama de sharding
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Sharding é como Kafka escala. Partições são divididas entre consumers do mesmo group. Se você tem 100 partições e 10 consumers, cada um pega 10. Sharding por chave (agent_id) garante que o mesmo agente é sempre processado pelo mesmo consumer (preservando ordering). Para escalar mais, adicione partições ( requer reconfiguração) e consumers.
💡 ANALOGIA: É como divisão de trabalho em uma fábrica. Cada operário (consumer) cuida de um conjunto de máquinas (partições). Para produzir mais, contrate mais operários — mas cada um precisa de máquinas para trabalhar.
⚠️ ERROS COMUNS: Alunos adicionam consumers sem adicionar partições. Consumers extras ficam ociosos.
➡️ TRANSIÇÃO: "E para observar tudo isso? Distributed tracing."

---

### Slide 58 — Distributed Tracing em Pipelines de Agentes

**Título**: Distributed Tracing em Pipelines de Agentes
**Objetivo**: Conectar tracing ao contexto event-driven.
**Conteúdo**:
- Em event-driven: trace espalhado por producer, broker, consumer
- **OpenTelemetry**: spans distribuídos com context propagation
- **Trace ID** propagado via headers de mensagem
- Visualização: timeline de spans cruzando serviços
- Para agentes: cada tool call = span; cada agente = service
- Aprofundamento em ETHAGT12 (AgentOps)

**Diagrama**: Trace distribuído com spans em múltiplos serviços
**Animação**: Spans surgem em timeline
**Imagem**: Trace waterfall (Jaeger/Tempo)
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Em event-driven, um request passa por múltiplos serviços. Sem distributed tracing, você não sabe onde a latência está. OpenTelemetry propaga um Trace ID via headers de mensagem — cada serviço cria spans filhos. Visualização: waterfall mostrando quanto tempo cada serviço gastou. Para agentes: cada tool call é um span; cada agente é um service. O trace completo mostra: producer → Kafka → consumer A (agente) → tool (LLM) → consumer B (validação).
💡 ANALOGIA: É como rastrear uma encomenda. Cada parada (serviço) é registrada com timestamp. Você vê exatamente onde a encomenda passou e quanto tempo ficou em cada lugar.
⚠️ ERROS COMUNS: Alunos implementam tracing por serviço, sem propagation do Trace ID. Sem propagation, os traces ficam fragmentados — você não vê o fluxo completo. Aprofundamos em ETHAGT12.
➡️ TRANSIÇÃO: "Lembre-se: mensageria tem custo."

---

### Slide 59 — Custo da Mensageria

**Título**: Custo da Mensageria
**Objetivo**: Lembrar que mensageria não é grátis.
**Conteúdo**:
- **Infraestrutura**: brokers, ZooKeeper/KRaft, monitoramento
- **Storage**: retenção de logs consome disco
- **Network**: replicação entre datacenters
- **Operação**: equipe de platform engineering
- Para agentes: cada evento tem custo de storage + processamento
- **Regra**: mensure custo por evento antes de escalar

**Diagrama**: Breakdown de custos (pizza chart conceitual)
**Animação**: Fatias da pizza surgem
**Imagem**: Gráfico de custos
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Mensageria não é grátis. Infraestrutura (brokers, ZooKeeper/KRaft, monitoramento), storage (logs retidos consomem disco), network (replicação entre datacenters), operação (equipe de platform engineering). Para agentes: cada evento tem custo de storage + processamento. Se você produz 1M eventos/dia com retenção de 7 dias, são 7M eventos armazenados. Mensure custo por evento antes de escalar.
💡 ANALOGIA: É como um armazém. Cada caixa (evento) ocupa espaço. Retenção longa = armazém grande = caro. Periodicamente, faça limpeza (expire eventos antigos).
⚠️ ERROS COMUNS: Alunos configuram retenção infinita "por segurança". Disco enche, cluster cai. Defina retenção conscientemente.
➡️ TRANSIÇÃO: "Vamos quebrar um mito."

---

### Slide 60 — V/F: "Event-driven é sempre mais escalável"

**Título**: V/F: Event-driven é sempre mais escalável
**Objetivo**: Quebrar o mito da escalabilidade automática.
**Conteúdo**:
- Verdadeiro ou Falso: "Event-driven é sempre mais escalável"
- **Resposta: Falso**
- Event-driven escala horizontalmente, mas introduz overhead de broker, latência de fila, complexidade de debugging
- Para tarefas simples e síncronas, a escalabilidade não compensa o custo
- Exercício do syllabus

**Diagrama**: Card V/F com explicação
**Animação**: "Falso" revelado em vermelho
**Imagem**: Card V/F
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Resposta: Falso. Event-driven escala horizontalmente (mais consumers = mais throughput), MAS introduz overhead: latência de broker (ms a segundos), complexidade de operação, debugging distribuído. Para tarefas simples e síncronas (ex.: responder pergunta de chat), event-driven é overkill — a latência adicional piora a UX. Event-driven é melhor quando há desacoplamento real, longa duração, ou necessidade de replay.
💡 ANALOGIA: É como dizer "caminhões são sempre melhores que carros". Caminhões carregam mais, mas são lentos, caros, difíceis de estacionar. Para ir à padaria, use carro. Para transportar carga, use caminhão.
⚠️ ERROS COMUNS: Alunos adotam event-driven para tudo "porque escala". Over-engineering. Comece simples (síncrono) e migre para event-driven quando houver dor real.
➡️ TRANSIÇÃO: "Vamos ao fechamento."

---

## SEÇÃO G — Fechamento (Slides 61-76 · 18 min)

---

### Slide 61 — [SEÇÃO] Fechamento

**Título**: Fechamento
**Objetivo**: Transição para o fechamento.
**Conteúdo**: "7 — Fechamento: Boas Práticas, Caso de Estudo, Quiz"
**Diagrama**: Fundo `etho-primary`
**Animação**: Fade in do número e título
**Imagem**: —
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Última seção. Vamos consolidar com exercício de saga, boas práticas, anti-patterns, caso de estudo real, quiz e Q&A.
➡️ TRANSIÇÃO: "Exercício primeiro."

---

### Slide 62 — Exercício: Saga Compensatória

**Título**: Exercício: Saga Compensatória
**Objetivo**: Praticar saga em cenário real.
**Conteúdo**:
- Cenário: sistema de transferência entre contas (debita A → credita B → notifica)
- Em duplas: escrever a lógica de compensação para cada passo falhar
- Quais compensações não são perfeitas? (ex.: notificação já enviada)
- 3 min discussão, 2 min apresentar 2 exemplos

**Diagrama**: Esqueleto de saga para preencher
**Animação**: Campos vazios para preencher
**Imagem**: Template de saga
**Tempo**: 5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Exercício em duplas (5 min total). Cada dupla escreve: (1) o que acontece se "debita A" falha; (2) se "credita B" falha; (3) se "notifica" falha. E para cada falha, qual a compensação. Discutir: quais compensações não são perfeitas? (Resposta: notificação — se o email saiu, não pode "desenviar".) Pedir 2 duplas para compartilhar.
💡 ANALOGIA: É como planejar o que fazer se algo der errado em uma viagem. Voo cancela? Hotel cancela? Carro não disponível? Para cada cenário, qual a compensação?
⚠️ ERROS COMUNS: Alunos escrevem compensação sem considerar que a compensação também pode falhar. O que fazer se o estorno falha?
➡️ TRANSIÇÃO: "Vamos às boas práticas."

---

### Slide 63 — Boas Práticas (DO)

**Título**: Boas Práticas (DO)
**Objetivo**: Checklist de boas práticas.
**Conteúdo**:
- Comece com at-least-once + idempotência (não persiga exactly-once)
- Use chaves de partição para preservar ordering por entidade
- Coloque I/O em activities; mantenha workflows determinísticos
- Defina DLQ (dead letter queue) desde o dia 1
- Monitore lag de consumer (Kafka) / depth de fila (RabbitMQ)
- Use circuit breakers em tools externas
- Version seus eventos (schema registry)

**Diagrama**: Checklist verde (`etho-success`)
**Animação**: Itens surgem um a um com checkmark
**Imagem**: Lista com checkmarks
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: As 7 boas práticas são cumulativas. (1) At-least-once + idempotência é a base. (2) Chaves de partição preservam ordering por entidade. (3) I/O em activities é a regra do Temporal. (4) DLQ desde o dia 1 — mensagens que falham N vezes vão para DLQ para análise manual. (5) Monitore lag (Kafka) ou depth (RabbitMQ) — consumer atrasado é problema. (6) Circuit breakers em tools externas. (7) Version eventos — schema registry para evolução sem quebrar consumers.
💡 ANALOGIA: É como o checklist de pré-voo. Cada item evita uma classe de problema.
⚠️ ERROS COMUNS: Alunos esquecem o DLQ. Sem DLQ, mensagens que falham N vezes somem ou bloqueiam a fila. Sempre defina DLQ.
➡️ TRANSIÇÃO: "E o que NÃO fazer?"

---

### Slide 64 — Anti-Patterns (DON'T)

**Título**: Anti-Patterns (DON'T)
**Objetivo**: Checklist do que NÃO fazer.
**Conteúdo**:
- Perseguir exactly-once sem idempotência
- I/O direto em código de workflow (non-determinism)
- Sem DLQ (mensagens falhadas somem)
- Sem schema versioning (quebra consumidores ao evoluir)
- Ordering global esperado em Kafka (só existe por partição)
- Sem monitoring de lag (consumer fica atrás sem ninguém saber)
- Usar Airflow para orquestração em tempo real
- Começar com Kafka quando RabbitMQ bastava

**Diagrama**: Checklist vermelho (`etho-danger`)
**Animação**: Itens surgem um a um com X
**Imagem**: Lista com X vermelhos
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Os 8 anti-patterns são os erros mais comuns. (1) Exactly-once sem idempotência — perda de tempo. (2) I/O no workflow — quebra replay. (3) Sem DLQ — mensagens somem. (4) Sem schema versioning — evoluir evento quebra consumers. (5) Ordering global em Kafka — não existe, só por partição. (6) Sem monitoring de lag — consumer atrasa silenciosamente. (7) Airflow para tempo real — não foi feito para isso. (8) Kafka quando RabbitMQ bastava — over-engineering.
💡 ANALOGIA: É como a lista de "o que não fazer na cozinha". Não deixe a faca cair, não corte na mão, não use pano sujo. Cada item evita um desastre.
⚠️ ERROS COMUNS: Alunos acham que "anti-patterns não acontecem comigo". Acontecem. Todo mundo comete esses erros na primeira vez.
➡️ TRANSIÇÃO: "Vamos ver tudo junto num caso real."

---

### Slide 65 — Caso de Estudo: Processamento de Documentos em Enterprise

**Título**: Caso de Estudo: Processamento de Documentos
**Objetivo**: Mostrar todos os conceitos em um caso real.
**Conteúdo**:
- Pipeline: ingestão (Kafka) → classificação (agente) → extração (agente) → validação (HITL) → publicação
- **Temporal** orquestra o workflow; agentes são activities
- **Saga compensatória** se validação falha
- **Circuit breaker** no agente de extração (API de LLM)
- **DLQ** para documentos que falham após N retries
- **Distributed tracing** via OpenTelemetry
- Lição: event-driven + durable execution + resiliência = produção

**Diagrama**: Arquitetura completa do pipeline
**Animação**: Componentes surgem em sequência; fluxo de dados animado
**Imagem**: Diagrama de arquitetura enterprise
**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Caso real que junta tudo. Pipeline de processamento de documentos: (1) Ingestão via Kafka (documentos chegam como eventos); (2) Agente de classificação (activity do Temporal — categoriza); (3) Agente de extração (activity — extrai dados); (4) Validação HITL (workflow pausa, humano aprova); (5) Publicação. Se validação falha: saga compensatória reverte. Circuit breaker no agente de extração (se API LLM cai, não desperdiça). DLQ para documentos irreparáveis. Tracing via OpenTelemetry para observabilidade.
💡 ANALOGIA: É como uma fábrica de processamento de alimentos. Esteira (Kafka) transporta, classificador (agente) separa, extrator (agente) processa, inspetor (HITL) aprova, empacotador publica. Se algo falha, há linha de reversão (saga) e descarte controlado (DLQ).
⚠️ ERROS COMUNS: Alunos acham que "vou começar simples e adicionar resiliência depois". Comece com DLQ e circuit breaker desde o dia 1 — adicionar depois é refatoração cara.
➡️ TRANSIÇÃO: "Vamos resumir."

---

### Slide 66 — Resumo da Aula

**Título**: Resumo da Aula
**Objetivo**: Sintetizar os pontos-chave.
**Conteúdo**:
- **Event-driven** = desacoplamento, escala, resiliência (com complexidade)
- **Mensageria**: Kafka (log/volume), RabbitMQ (routing), NATS (leveza)
- **Temporal** = durable execution: sobreviver a crashes, long-running, HITL
- **Resiliência**: retry + idempotência + saga + circuit breaker
- **Produção**: at-least-once + idempotência = "effectively once"
- **Determinismo** é a regra de ouro do replay

**Diagrama**: 6 ícones com os pontos-chave
**Animação**: Ícones surgem um a um
**Imagem**: Grid de 6 conceitos
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Se vocês vão lembrar de 6 coisas desta aula: (1) Event-driven traz desacoplamento, escala e resiliência — mas com complexidade; (2) Kafka é log de volume, RabbitMQ é routing, NATS é leveza; (3) Temporal é durable execution — sobrevive a crashes, roda por dias, pausa para HITL; (4) Resiliência é composição: retry + idempotência + saga + circuit breaker; (5) Exactly-once é mito — at-least-once + idempotência = effectively once; (6) Determinismo é a regra de ouro do replay.
💡 ANALOGIA: É como os 6 mandamentos da cozinha. Se seguir, o prato sai bom.
➡️ TRANSIÇÃO: "Checklist final."

---

### Slide 67 — Checklist da Aula

**Título**: Checklist da Aula
**Objetivo**: Confirmar que todos os tópicos foram cobertos.
**Conteúdo**:
- [ ] Diferenciou síncrono de event-driven
- [ ] Comparou Kafka, RabbitMQ e NATS
- [ ] Explicou durable execution e Temporal
- [ ] Implementou retries e idempotência
- [ ] Escreveu uma saga compensatória
- [ ] Discutiu exactly-once vs at-least-once

**Diagrama**: Checklist visual
**Animação**: Itens são marcados um a um
**Imagem**: Lista com checkboxes
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Checklist final. Se todos os 6 itens estão marcados, a aula cumpriu os objetivos. Se algum não está, indique onde revisar (slides correspondentes).
➡️ TRANSIÇÃO: "Quiz para verificar compreensão."

---

### Slide 68 — Quiz: Pergunta 1

**Título**: Quiz 1: Temporal vs Kafka
**Objetivo**: Verificar compreensão.
**Conteúdo**:
- "Quando Temporal é preferível a Kafka puro?"
- A) Quando você precisa de máximo throughput
- B) Quando você precisa de durable execution, HITL e orquestração de workflow
- C) Quando você quer o broker mais leve
- D) Quando você não precisa de ordering
- **Resposta: B**

**Diagrama**: 4 opções
**Animação**: Resposta revelada após votação
**Imagem**: Card de quiz
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Resposta B. Temporal é para durable execution, HITL e orquestração. Kafka é mensageria (infraestrutura de comunicação). Não são mutuamente exclusivos — você pode usar ambos. A (throughput) é Kafka. C (leveza) é NATS. D (sem ordering) é irrelevante.
➡️ TRANSIÇÃO: "Pergunta 2."

---

### Slide 69 — Quiz: Pergunta 2

**Título**: Quiz 2: Ordering no Kafka
**Objetivo**: Verificar compreensão.
**Conteúdo**:
- "Em Kafka, como garantir ordering de mensagens do mesmo agente?"
- A) Usar ordering global (não existe)
- B) Usar a mesma chave de partição (agent_id)
- C) Aumentar o número de partições
- D) Usar RabbitMQ no lugar
- **Resposta: B**

**Diagrama**: 4 opções
**Animação**: Resposta revelada
**Imagem**: Card de quiz
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Resposta B. Mesma chave = mesma partição = ordering preservado. A é falso (não há ordering global). C (mais partições) não ajuda ordering — pode piorar (mensagens do mesmo agente podem ir para partições diferentes se a key não for usada). D é trocar de ferramenta, não resolver.
➡️ TRANSIÇÃO: "Pergunta 3."

---

### Slide 70 — Quiz: Pergunta 3

**Título**: Quiz 3: Non-Determinism
**Objetivo**: Verificar compreensão.
**Conteúdo**:
- "O que quebra um replay no Temporal?"
- A) Usar `workflow.sleep()` no workflow
- B) Non-determinism (I/O direto, datetime.now(), random no workflow)
- C) Chamar activities
- D) Usar signals
- **Resposta: B**

**Diagrama**: 4 opções
**Animação**: Resposta revelada
**Imagem**: Card de quiz
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Resposta B. Non-determinism quebra o replay porque o re-execução do código do workflow diverge do histórico. A (`workflow.sleep()`) é determinístico e seguro. C (activities) é o uso correto. D (signals) são suportados no replay.
➡️ TRANSIÇÃO: "Pergunta 4."

---

### Slide 71 — Quiz: Pergunta 4

**Título**: Quiz 4: Effectively Once
**Objetivo**: Verificar compreensão.
**Conteúdo**:
- "Qual é a estratégia prática para 'effectively once'?"
- A) Implementar exactly-once delivery no broker
- B) At-least-once delivery + idempotência no consumidor
- C) At-most-once + retry infinito
- D) Usar transações distribuídas (2PC)
- **Resposta: B**

**Diagrama**: 4 opções
**Animação**: Resposta revelada
**Imagem**: Card de quiz
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Resposta B. At-least-once (pode duplicar) + idempotência (duplicar não causa efeito) = effectively once. É a prática consagrada. A (exactly-once no broker) é mito. C perde mensagens. D (2PC) é caro e frágil.
➡️ TRANSIÇÃO: "Pergunta 5."

---

### Slide 72 — Quiz: Pergunta 5

**Título**: Quiz 5: Saga
**Objetivo**: Verificar compreensão.
**Conteúdo**:
- "Em uma saga de transferência, se o passo 'notificar' falha, o que se faz?"
- A) Nada — a transferência já foi feita
- B) Compensar os passos anteriores (estornar crédito e débito)
- C) Retentar infinitamente até notificar
- D) Cancelar a transação via 2PC
- **Resposta: B**

**Diagrama**: 4 opções
**Animação**: Resposta revelada
**Imagem**: Card de quiz
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Resposta B. Compensar: estornar crédito em B e devolver débito em A. O usuário não foi notificado, mas o dinheiro voltou ao estado original. A está errado — deixar inconsistente. C é retry infinito (pode travar). D (2PC) não é como saga funciona.
➡️ TRANSIÇÃO: "Vamos conectar com o futuro."

---

### Slide 73 — Conexão com Próximos Módulos

**Título**: Conexão com Próximos Módulos
**Objetivo**: Mostrar como ETHAGT11 conecta com o resto da especialização.
**Conteúdo**:
- ETHAGT12 — AgentOps: observabilidade + avaliação (aprofunda tracing)
- ETHAGT14 — Escalabilidade: event-driven em produção em larga escala
- ETHAGT90 — Projeto final: pipeline event-driven como componente

**Diagrama**: Mapa da especialização com ETHAGT11 destacado
**Animação**: ETHAGT11 pulsando; conexões surgem
**Imagem**: Mind map da especialização
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: ETHAGT11 conecta diretamente com ETHAGT12 (AgentOps — aprofunda distributed tracing), ETHAGT14 (Escalabilidade — event-driven em larga escala) e ETHAGT90 (Projeto final — pipeline event-driven como componente). A base de hoje é usada em todos esses módulos.
➡️ TRANSIÇÃO: "Projeto e labs."

---

### Slide 74 — Projeto do Módulo e Labs

**Título**: Projeto do Módulo e Labs
**Objetivo**: Apresentar projeto e laboratórios.
**Conteúdo**:
- **Projeto**: pipeline event-driven para processamento de tickets em massa
  - Durable execution, retries e compensação
  - Entrega: código + ADR + análise de falhas injetadas (chaos)
  - Critério: pipeline sobrevive a ≥2 falhas injetadas sem perda de dados
- **Lab 1** (4h): "Agente com Kafka" — dois agentes coordenados via tópicos
- **Lab 2** (5h): "Workflow durável em Temporal" — agente sobrevivendo a kill

**Diagrama**: Cards de projeto e labs
**Animação**: Cards surgem um a um
**Imagem**: Ícones de projeto e labs
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O projeto é a avaliação principal. Pipeline event-driven que sobrevive a falhas injetadas (chaos test). A entrega inclui ADR (Architecture Decision Record) — documento que justifica escolhas arquiteturais. Critério de sucesso: pipeline sobrevive a ≥2 falhas sem perda de dados. Os labs são preparatórios: Lab 1 (Kafka) e Lab 2 (Temporal).
💡 ANALOGIA: O projeto é como um teste de colisão de carro. Você precisa provar que o "carro" (pipeline) sobrevive a "colisões" (falhas) sem "ferir o motorista" (perder dados).
➡️ TRANSIÇÃO: "Leitura recomendada."

---

### Slide 75 — Leitura Recomendada e Referências

**Título**: Leitura Recomendada e Referências
**Objetivo**: Indicar o que ler antes da próxima aula.
**Conteúdo**:
- **Obrigatório**: Temporal.io *Durable Execution* primer
- **Obrigatório**: Kreps, *The Log* (LinkedIn Engineering)
- **Recomendado**: Narkhede et al., *Kafka: The Definitive Guide*
- **Recomendado**: Microsoft *Cloud Design Patterns* (saga, CQRS)
- **Complementar**: CloudEvents spec (CNCF); NATS docs; RabbitMQ docs
- **Vídeo**: Temporal *Durable Execution* talks (YouTube)

**Diagrama**: Lista com prioridades
**Animação**: Itens surgem por prioridade
**Imagem**: Capas de livros/docs
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: As duas leituras obrigatórias são: Temporal primer (entendimento profundo de durable execution) e Kreps The Log (fundamento conceitual de Kafka/eventos). O livro do Kafka é a referência canônica. Microsoft Cloud Design Patterns cobre saga e CQRS. CloudEvents é a spec de padronização.
➡️ TRANSIÇÃO: "Q&A."

---

### Slide 76 — Q&A / Encerramento

**Título**: Perguntas?
**Objetivo**: Abrir para perguntas e encerrar.
**Conteúdo**:
- "Perguntas?"
- Contato do professor
- "Na próxima aula: ETHAGT12 — AgentOps: Observabilidade & Avaliação"

**Diagrama**: Logo Etho + fundo `etho-dark`
**Animação**: Fade in
**Imagem**: Logo Etho
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Abrir para Q&A. Se não houver perguntas: "Qual parte foi menos clara?" Mensagem final: "Event-driven não é sobre Kafka ou Temporal — é sobre desacoplamento, resiliência e durabilidade. As ferramentas mudam; os princípios permanecem. Se entenderam os princípios, qualquer ferramenta será uma instanciação."
💡 ANALOGIA FINAL: "Vocês aprenderam a cozinhar. Kafka, Temporal, RabbitMQ são as panelas. O prato (pipeline de agentes) depende do cozinheiro."
➡️ Fim da aula.

---
