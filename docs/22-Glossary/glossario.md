# Glossário — Programação Agêntica

Termos técnicos em **inglês** são mantidos quando consagrados; em **português** quando há tradução estável. Marcações: 🏛 *canônico* · 🆕 *emergente*.

---

## A

**ACI** (Agent-Computer Interface) — *Interface Agente-Computador* — A interface entre o agente e suas ferramentas; análoga à HCI. Anthropic defende que merece tanto esforço quanto a interface humano-computador. 🏛

**Actor Model** — *Modelo de Ator* — Modelo de concorrência onde "atores" encapsulam estado e se comunicam só por mensagens assíncronas. Base para sistemas multi-agente distribuídos.

**Agent Loop** — *Loop de Agente* — O ciclo perceive → think → act → observe que define um agente autônomo. Implementação canônica: ReAct.

**Agentic RAG** — RAG onde o agente decide *quando*, *o quê* e *como* recuperar, podendo refinar queries iterativamente.

**Augmented LLM** — *LLM Aumentado* — Bloco fundamental de Anthropic: LLM + retrieval + tools + memory. A unidade atômica de qualquer sistema agêntico. 🏛

**AutoGPT** — Um dos primeiros agentes autônomos open source (2023); demonstrou ambition e limites (loops, custo).

## B

**Blackboard** — *Quadro-Negro* — Padrão arquitetural onde múltiplos agentes leem/escrevem em um espaço compartilhado; útil quando a estrutura do problema é dinâmica.

**Benchmark** — Conjunto padronizado de tarefas para medir agentes. Canônicos: SWE-bench (código), GAIA (raciocínio geral), τ-bench (tool use), AgentBench, WebArena (web).

## C

**Checkpoint / Checkpointer** — Persistência do estado de um agente/graph entre execuções; primitiva de memória de longo prazo. LangGraph: implementações Postgres, SQLite.

**Computer Use** — *Uso de Computador* — Capacidade de um agente operar uma interface gráfica (mouse, teclado, screen). Categoria nativa desde Claude 3.5 Sonnet.

**Constitutional AI (CAI)** — Abordagem de treinar/alinhar modelos com uma "constituição" de princípios; base para guardrails.

**Critic / Evaluator** — Padrão de agente que avalia a saída de outro agente em loop; coração do workflow *evaluator-optimizer*.

## D

**Durable Execution** — *Execução Durável* — Orquestração onde o estado do workflow sobrevive a crashes; Temporal é referência. Crítico para agentes de longa duração.

## E

**Embeddings** — Vetores densos que representam semântica de texto/imagem; base para vector search e RAG.

**Evaluator-Optimizer** — Workflow de Anthropic onde um LLM gera e outro avalia/critica em loop até satisfazer critério.

**Event-Driven** — *Orientado a Eventos* — Arquitetura onde agentes reagem a eventos assíncronos via mensageria (Kafka, NATS, RabbitMQ).

## F

**Few-Shot** — Técnica de prompt com poucos exemplos; pré-requisito de conhecimento nesta Especialização.

**FinOps (de Agentes)** — Gestão de custo/latência de agentes: caching de LLM, seleção de modelo por tarefa, orçamento por execução.

## G

**GAIA** — Benchmark de raciocínio geral multi-step; agentes humanos resolvem em ~90%, modelos ainda muito abaixo.

**Guardrails** — *Guardas-corpos* — Mecanismos que filtram/constraint entrada e saída de agentes (schemas, classifiers, constitutions).

## H

**Hallucination (in action)** — Alucinação que ocorre em *ações* (tool calls erradas), não só em texto; mais perigosa que alucinação de chat.

**Hierarchical Agents** — Topologia onde um supervisor/orchestrator delega a workers especializados em árvore.

**Human-in-the-Loop (HITL)** — *Humano no Loop* — Padrão onde humanos aprovam/editam ações críticas em checkpoints; essencial para produção.

## I

**Inference-Time Reasoning** — *Raciocínio no Tempo de Inferência* — Modelos que "pensam" antes de responder (o1/o3, Claude reasoning); distinto de CoT promptado. 🆕

## K

**Knowledge Graph** — *Grafo de Conhecimento* — Representação estruturada de entidades e relações; complementar ao vector store para raciocínio.

## L

**LATS** (Language Agent Tree Search) — Algoritmo que combina MCTS com LLM para exploração de árvores de ações.

**LLM-as-Judge** — Usar um LLM para avaliar saídas de outro LLM; técnica central de eval automatizado, com vieses conhecidos.

**LLMOps** — Práticas de MLOps adaptadas a LLMs; superconjunto de AgentOps.

## M

**MCP** (Model Context Protocol) — *Protocolo de Contexto de Modelo* — Padrão aberto da Anthropic para conectar LLMs a fontes de dados e ferramentas; arquitetura client-server-host. 🏛

**Memory** (de agentes) — Tipos: **episódica** (eventos passados), **semântica** (fatos), **procedural** (como fazer), **working** (sessão atual).

**Meta-Agent** — Agente que cria/configura/outros agentes; base para sistemas auto-evolutivos. 🆕

## O

**Orchestrator-Workers** — Workflow de Anthropic onde um LLM central divide tarefa, delega a workers e sintetiza; difere da parallelização por subtasks *dinâmicas*.

## P

**Parallelization** — Workflow de Anthropic; variantes: *sectioning* (subtasks independentes) e *voting* (múltiplas tentativas).

**Plan-and-Execute** — Padrão: planner gera plano, executor opera cada passo; vantagem: eficiência, desvantagem: rigidez vs mudanças.

**Prompt Chaining** — Workflow de Anthropic onde a saída de um LLM alimenta o próximo; com gates programáticos entre etapas.

**Prompt Injection** — Ataque onde entrada maliciosa faz o agente desviar de instruções; crítico em RAG e tool use.

## R

**Reasoning Model** — Modelo treinado para raciocínio extendido (CoT interno); exemplos: o1, o3, Claude com extended thinking.

**ReAct** (Reason+Act) — Padrão fundamental onde o agente intercala *Thought*, *Action*, *Observation* em loop.

**Reflection / Reflexion** — Padrão onde o agente critica sua própria saída e re-tenta; Reflexion adiciona memória de falhas anteriores.

**Retrieval Agent** — Agente especializado em buscar/recuperar informação; núcleo de RAG agêntico.

**ReWOO** (Reasoning WithOut Observation) — Decompõe tarefa gerando plano "cego" e evidências em paralelo.

**Routing** — Workflow de Anthropic que classifica input e direciona para subtarefa especializada.

## S

**Self-Discover** — Padrão onde o agente descobre sua própria estratégia de raciocínio composta a partir de primitivas.

**Self-RAG** — RAG onde o modelo decide se recuperar e se criticar; treino específico.

**Structured Output** — *Saída Estruturada* — Forçar LLM a produzir JSON/schema; base para tool calling confiável.

**Supervisor** — Padrão multi-agente onde um supervisor orquestra workers via tool calls (LangGraph *supervisor pattern*).

**Swarm** — Topologia inspirada em OpenAI Swarm; agentes se "transferem" controle via handoffs.

## T

**τ-bench** (Tau-bench) — Benchmark de tool use em domínios de agentes (airline, retail); mede política adherence.

**Tool Calling** — *Chamada de Ferramentas* — Capacidade do LLM emitir chamadas estruturadas para funções externas; mecanismo subjacente a qualquer agente útil.

**ToT** (Tree of Thoughts) — Explora múltiplos caminhos de raciocínio em árvore com avaliação/backtracking.

## V

**Vector Database** — *Banco Vetorial* — Sistema otimizado para similaridade vetorial (ANN). Exemplos: Qdrant, Milvus, Weaviate, Chroma, pgvector.

## W

**WebVoyager** — Agente que navega web por múltiplos passos; referência para browser agents.

**Workflow** — Sistema onde LLMs e tools são orquestrados por *caminhos de código predefinidos*. Distinto de **Agent** (controle dinâmico pelo LLM). Distinção canônica de Anthropic. 🏛

---

## Conceitos da Universidade Etho (recapitulando)

- **Fases**: Onboarding → Formação → Autonomia → Especialização → Liderança.
- **4 Pilares de avaliação**: Técnico 40% · Consultivo 30% · Comportamental 20% · Prático 10%.
- **Níveis de competência**: B (Básico) · I (Intermediário) · A (Avançado).
- **Tronco Comum**: cursos compartilhados referenciados por código.
- **PDI**: Plano de Desenvolvimento Individual.

---

*Princípio: termos em inglês são mantidos quando (i) não há tradução estável, (ii) são os usados em papers/docs canônicos, ou (iii) a tradução introduz ambiguidade. Caso contrário, traduz-se.*
