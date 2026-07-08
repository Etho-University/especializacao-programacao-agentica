# ETHAGT09 — Perguntas para Discussão

> Perguntas para estimular debate durante e após a aula.
> Organizadas por profundidade: rápida (1-2 min) → média (3-5 min) → profunda (10+ min).

---

## Perguntas Rápidas (1-2 min)

### Q1 — Quantos Agentes Antes do Caos
"Quantos agentes colaborando antes de virar caos sem protocolo?"
- **Objetivo**: Motivar a necessidade de coordenação
- **Slide**: 5
- **Resposta esperada**: Sem protocolo, 3+ agentes já geram confusão de quem faz o quê. A resposta exata depende da tarefa, mas o ponto é: sem estrutura, escala mal rápido.

### Q2 — Topologia para Diagnóstico
"Qual topologia para 10 agentes debatendo um diagnóstico?"
- **Objetivo**: Praticar escolha de topologia
- **Slide**: 9
- **Resposta esperada**: Pub/Sub (tópico por hipótese) ou blackboard. Broadcast satura. P2P fica O(N²).

### Q3 — Garantia para Transferência Bancária
"Qual garantia de entrega para transferência bancária entre agentes?"
- **Objetivo**: Conectar semânticas de entrega a casos reais
- **Slide**: 14
- **Resposta esperada**: Exactly-once (ideal) ou at-least-once com idempotência. At-most-once é inaceitável (pode perder dinheiro).

### Q4 — Experiência com Multi-Agente
"Quem aqui já usou AutoGen, CrewAI ou LangGraph multi-agent em produção?"
- **Objetivo**: Calibrar experiência prática
- **Slide**: 17
- **Ação**: Contar mãos levantadas

### Q5 — Actor vs Shared State
"Actor model vs shared state — qual é mais seguro para dados críticos?"
- **Objetivo**: Pensar sobre isolamento de estado
- **Slide**: 37
- **Resposta esperada**: Actor model — estado encapsulado, sem race conditions. Shared state exige locks (propensos a bugs).

---

## Perguntas Médias (3-5 min)

### Q6 — Handoff ou Delegação para Suporte
"Para um sistema de suporte ao cliente: handoff (Swarm) ou delegação (supervisor)?"
- **Objetivo**: Aplicar a distinção a um caso real
- **Slide**: 23
- **Dica**: Handoff é mais simples (triager sai). Delegação dá controle (supervisor monitora). Para suporte com SLA, delegação permite escalar.

### Q7 — Blackboard para Relatório
"5 agentes contribuem com partes de um relatório. Blackboard ou mensagens diretas?"
- **Objetivo**: Praticar a decisão blackboard vs direto
- **Slide**: 33
- **Resposta esperada**: Blackboard — contribuições independentes, N grande, baixo acoplamento.

### Q8 — Voting ou Mediator
"Voting ou mediator para 3 especialistas com diagnóstico divergente?"
- **Objetivo**: Pensar sobre resolução de conflito
- **Slide**: 50
- **Resposta esperada**: Depende dos stakes. Voting é rápido mas pode errar (2-1). Mediator é mais caro mas justifica a decisão. Para medicina, mediator (humano no loop).

### Q9 — Deadlock na Prática
"Vocês já enfrentaram deadlock (loop infinito) em algum sistema? Como resolveram?"
- **Objetivo**: Conectar deadlock teórico a experiência prática
- **Slide**: 51
- **Ação**: Deixar 1-2 alunos compartilharem

### Q10 — MCP vs A2A
"MCP e A2A Protocol são complementares ou competidores?"
- **Objetivo**: Confirmar a distinção canônica
- **Slide**: 56
- **Resposta esperada**: Complementares. MCP = agent↔system (tools, data). A2A = agent↔agent (delegação, colaboração).

---

## Perguntas Profundas (10+ min)

### Q11 — Quando 1 Agente vs N Agentes
"Quando é melhor ter 1 agente com muitas tools vs N agentes especializados? Quais os trade-offs?"
- **Objetivo**: Pensamento crítico sobre arquitetura
- **Slide**: 25, 61
- **Resposta esperada**: 1 agente quando tarefas se sobrepõem e contexto é compartilhado. N agentes quando especializações são distintas, contextos grandes, ou isolamento é necessário. Trade-offs: overhead de comunicação vs foco do contexto; coordenação vs simplicidade.
- **Contraponto**: Anthropic — "comece com 1 agente; multi-agente é complexidade de último recurso."

### Q12 — Negociação Sem Convergência
"Como evitar deadlock em negociação entre agentes com objetivos parcialmente conflitantes?"
- **Objetivo**: Aplicar max_rounds, BATNA, mediator ao projeto do módulo
- **Slide**: 51, 52
- **Resposta esperada**: (1) max_rounds obrigatório; (2) timeout; (3) estratégia de concessão forçada após N rounds; (4) BATNA explícita (melhor alternativa se não houver acordo); (5) escalar para mediator.

### Q13 — Protocolo Próprio vs Padrão
"Vocês implementariam um protocolo de comunicação próprio ou adotariam A2A Protocol? Por quê?"
- **Objetivo**: Pensar sobre build vs adopt
- **Slide**: 59
- **Argumentos a favor do próprio**: controle total, otimizado para o domínio, sem dependência de spec emergente.
- **Argumentos a favor do A2A**: interoperabilidade, menos código, alinhado com tendência de padronização.
- **Para o PM**: risco de lock-in vs custo de manutenção de protocolo próprio.

### Q14 — Blackboard + Actor Híbrido
"É possível combinar blackboard e actor model? Em que cenário isso faria sentido?"
- **Objetivo**: Pensar arquiteturalmente sobre híbridos
- **Slide**: 42
- **Resposta esperada**: Sim. Um ator gerencia o blackboard (serializa acesso). Agentes são atores que leem/escrevem via mensagens para o blackboard-actor. Combina isolamento do actor com compartilhamento do blackboard. Útil em sistemas distribuídos com estado compartilhado.

---

## Perguntas Bônus (para alunos avançados)

### Q15 — FIPA-ACL em LLM Agents
"FIPA-ACL define performatives (request, inform, propose). LLM agents precisam disso ou o LLM 'descobre' implicitamente?"
- **Objetivo**: Conectar padrões clássicos a LLM agents
- **Resposta**: LLMs frequentemente "descobrem" performatives implicitamente via prompts. Mas schemas explícitos (como A2A) tornam a comunicação mais confiável e debugável. Lição: estrutura > improvisação.

### Q16 — Escalabilidade de Group Chat
"Um AutoGen GroupChat com 20 agentes escala bem? Quais os limites?"
- **Objetivo**: Pensar sobre limites práticos
- **Resposta**: Não escala bem. O manager precisa decidir entre 20 agentes a cada turno — o contexto explode e o custo explode. Para N grande, blackboard ou arquitetura hierárquica (sub-grupos) é melhor.

### Q17 — Agent Card e Segurança
"Um Agent Card público expõe capacidades do agente. Isso é risco de segurança?"
- **Objetivo**: Introduzir ETHAGT13 (Security)
- **Resposta**: Sim — expor capacidades pode facilitar ataques. Necessário autenticação, autorização e rate limiting. Prepara para o módulo de segurança.
