# ETHAGT12 — AgentOps, Observabilidade & Avaliação

> **Apostila do curso** · Especialização em Programação Agêntica · Universidade Etho
> Fase D — Produção, Governança e Fronteira · Carga 30 h · Versão 1.0 · Julho 2026
> *Material de referência duradouro (nível pós-graduação lato sensu). Os slides são auxiliares.*

---

## Sumário

- **Capítulo 1** — Por que agentes são difíceis de avaliar
- **Capítulo 2** — Observabilidade
- **Capítulo 3** — Avaliação automatizada
- **Capítulo 4** — Benchmarks canônicos
- **Capítulo 5** — O ciclo de melhoria
- **Capítulo 6** — Reportando resultados
- **Capítulo 7** — Casos de estudo
- **Capítulo 8** — Referências e leituras

---

## Capítulo 1 — Por que agentes são difíceis de avaliar

### 1.1 O salto do LLMOps ao AgentOps

ETHAGT01 (§6) introduziu a observabilidade mínima (logs estruturados, traces, orçamentos) como primitiva desde a primeira linha de código. Este módulo eleva isso a uma **disciplina completa**: AgentOps — o equivalente, para agentes, do que DevOps/MLOps é para software/modelos tradicionais. A diferença crucial: agentes são **não-determinísticos, multi-etapas, caros e dependentes de ambiente** — o que torna a avaliação ordens de magnitude mais difícil que a de um modelo isolado.

### 1.2 Três fontes de dificuldade

1. **Não-determinismo:** a mesma entrada pode levar a caminhos (e resultados) diferentes entre execuções. Não basta testar uma vez.
2. **Dependência de ambiente:** o agente age sobre sistemas externos (APIs, arquivos) cujo estado muda — reproduzir uma execução é difícil.
3. **Custo de runs:** cada execução custa (tokens, chamadas de API). Avaliar em larga escala é caro.

### 1.3 As falácias da avaliação informal

A maior armadilha é a **avaliação por intuição** — as falácias "parece bom" e "funcionou uma vez":

- *"Parece bom":* você testa alguns casos a olho, parece correto. Mas a intuição humana é péssima em estimar frequências de falha em sistemas estocásticos. Sem medição sistemática, você não sabe a taxa de sucesso real.
- *"Funcionou uma vez":* o não-determinismo faz com que um caso possa passar numa execução e falhar noutra. Uma execução bem-sucedida não é evidência de robustez.

> **Princípio.** *You didn't measure it if you didn't measure it.* Sem um conjunto de testes sistemático, você não avaliou — você achou. A avaliação informal é o maior risco silencioso em sistemas agentes.

### 1.4 Avaliação contínua vs pontual

A avaliação não é uma atividade de fim de projeto — é **contínua**, integrada ao ciclo de desenvolvimento. Cada mudança (prompt, tool, modelo) deve ser avaliada contra um conjunto de regressão antes de ir a produção. É o *CI para agentes*: testes de regressão automatizados a cada mudança.

---

## Capítulo 2 — Observabilidade

### 2.1 Traces, spans e bags

ETHAGT01 (§6.3) introduziu o conceito de *trace* — o registro completo de uma execução. Em AgentOps, refinamos a terminologia com o modelo do OpenTelemetry:

- **Trace:** a execução ponta-a-ponta de uma tarefa pelo agente.
- **Span:** uma unidade dentro do trace — uma chamada LLM, uma execução de tool, um sub-agente. Spans se aninham.
- **Baggage (contexto):** metadados propagados ao longo do trace (user_id, versão do agente, flags).

> **Diagrama de referência:** [`12-Diagrams/ETHAGT12/trace-anatomy.mmd`](../../12-Diagrams/ETHAGT12/trace-anatomy.mmd).

### 2.2 OpenTelemetry para LLMs

O **OpenTelemetry**, com as *GenAI semantic conventions*, padroniza como instrumentar chamadas LLM — capturando modelo, tokens (input/output), custo, latência, de forma estruturada e interoperável entre ferramentas. Isso permite correlacionar traces de agentes com traces de infraestrutura (bancos, filas) num mesmo sistema.

### 2.3 Tooling: LangSmith, Phoenix, Langfuse, OpenLLMetry

A observabilidade de agentes tem um ecossistema maduro de ferramentas:

- **LangSmith:** integrado ao ecossistema LangChain; traces, datasets, evals.
- **Phoenix (Arize):** open-source; foco em LLM observability e eval.
- **Langfuse:** open-source, self-hostable; tracing, prompt management, eval.
- **OpenLLMetry:** instrumentação OpenTelemetry para LLMs (provedor-agnóstica).

A escolha depende de preferência self-hosted vs SaaS e do ecossistema. O importante é *ter* observabilidade estruturada — não logs ad-hoc.

### 2.4 Logs estruturados vs traces

Há uma distinção útil: **logs** são eventos discretos (uma linha por evento); **traces** são a *estrutura* hierárquica de uma execução. Logs são bons para alertas e métricas agregadas; traces são bons para diagnóstico de uma execução específica. Em AgentOps, você precisa de *ambos*: logs para "quantos erros por hora?" e traces para "por que *esta* execução falhou?".

### 2.5 O custo da observabilidade

Observabilidade tem custo: capturar traces consome armazenamento e processamento. Em alto volume, *sampling* (registrar só uma fração das execuções) equilibra custo e visibilidade. Mas *nunca* sampleie 100% das execuções críticas/destrutivas — essas precisam de registro completo para auditoria.

---

## Capítulo 3 — Avaliação automatizada

### 3.1 LLM-as-judge

A avaliação de saídas de agentes é difícil porque a "correção" é frequentemente subjetiva. O **LLM-as-judge** usa um LLM para avaliar outro — dá um score à resposta com base numa rubrica. É escalável (automatizado) e flexível (qualquer critério articulável).

Mas tem vieses conhecidos:

- **Viés de verbosity:** juízes tendem a preferir respostas mais longas.
- **Viés de auto-preferência:** juízes preferem respostas no estilo do próprio modelo.
- **Inconsistência:** o mesmo juiz pode dar scores diferentes à mesma resposta em execuções distintas.

Mitigações: rubricas *estruturadas* (critérios explícitos e pontuados), múltiplos juízes (consenso), e *validação contra rótulos humanos* numa amostra (calibrar o juiz contra a verdade).

### 3.2 Golden cases e conjuntos de regressão

O coração da avaliação automatizada é o conjunto de **golden cases**: casos rotulados (pergunta + resposta/critério esperado) que não mudam entre execuções. Esse conjunto permite:

- **Medir a taxa de sucesso** ao longo do tempo.
- **Detectar regressões:** se você muda o prompt e a taxa cai, você sabe.
- **Comparar versões:** A/B testing de prompts/tools/modelos.

> **Diagrama de referência:** [`12-Diagrams/ETHAGT12/eval-pipeline.mmd`](../../12-Diagrams/ETHAGT12/eval-pipeline.mmd).

### 3.3 Métricas de tarefa vs de processo

| Categoria | Métrica | Mede |
|---|---|---|
| **Tarefa** | Success rate | A tarefa foi completada corretamente? |
| | Partial credit | Completou parcialmente? |
| | Custo / latência | A que preço? |
| **Processo** | Nº de steps | Quantas iterações? |
| | Loops | Entrou em loop? |
| | Tool misuse | Usou ferramentas erradas? |

Métricas de *tarefa* medem o resultado; métricas de *processo* medem *como* chegou lá. Ambas importam: um agente que acerta mas entra em 50 loops é caro e frágil, mesmo "certo".

### 3.4 A/B testing de prompts e tools

A avaliação contínua habilita experimentação controlada: mude uma variável (prompt, tool, modelo), avalie contra o conjunto golden, compare. Sem avaliação sistemática, "melhorar o agente" é adivinhação; com ela, é *experimentação científica*.

---

## Capítulo 4 — Benchmarks canônicos

### 4.1 Por que benchmarks

Benchmarks são *conjuntos padronizados* de tarefas que permitem comparar agentes (e modelos) numa base comum. São essenciais para *posicionar* seu sistema no estado da arte e para medir progresso objetivo.

> **Diagrama de referência:** [`12-Diagrams/ETHAGT12/benchmark-landscape.mmd`](../../12-Diagrams/ETHAGT12/benchmark-landscape.mmd).

### 4.2 Os benchmarks canônicos

| Benchmark | Domínio | Mede |
|---|---|---|
| **SWE-bench / SWE-bench Verified** (arXiv:2310.06770) | Código | Resolver issues reais do GitHub |
| **GAIA** (arXiv:2311.12983) | Geral | Raciocínio multi-step, tool use, web |
| **τ-bench** (arXiv:2404.44529) | Tool-agent-user | Tool use em domínios (airline, retail) |
| **AgentBench** (arXiv:2308.03688) | Panorama amplo | Múltiplas tarefas agentais |
| **WebArena / VisualWebArena** (arXiv:2307.13854) | Navegação web | Agentes navegando sites |

### 4.3 Como rodar, limites, contaminação

Rodar benchmarks tem armadilhas:

- **Contaminação:** se o modelo viu os casos do benchmark no treino, o score é inflado. Use *Verified* ou *held-out* splits; monitore contaminação.
- **Ambiente:** muitos benchmarks exigem infraestrutura (containers, sandboxes de código, ambientes web). Configure corretamente.
- **Limites de generalização:** bom score num benchmark *não* garante bom desempenho em *seu* domínio. Benchmarks medem capacidades gerais; seu sistema precisa de avaliação *no seu* domínio (golden cases próprios).

> **Princípio.** *Bom score em benchmark não garante bom desempenho em produção.* Benchmarks são necessários, não suficientes.

### 4.4 SWE-bench vs benchmark custom

Use **SWE-bench/GAIA/τ-bench** para posicionar-se no estado da arte e medir capacidades gerais. Construa um **benchmark custom** para o *seu* domínio — os casos reais que seus usuários enfrentam. Ambos coexistem: um para comparabilidade externa, outro para relevância interna.

---

## Capítulo 5 — O ciclo de melhoria

### 5.1 Dataset crescente

A avaliação melhora com dados. Cada execução em produção é uma oportunidade de *aprender*: casos de falha viram golden cases (rotulados com o que deveria ter sido); casos de sucesso confirmam. O conjunto cresce com o tempo, tornando-se cada vez mais representativo. A regra: **você não está avaliando se seu conjunto de teste não cresce.**

### 5.2 CI para agentes

Integre a avaliação ao *continuous integration*: a cada mudança (PR), rode o conjunto golden e bloqueie merges que reduzem a taxa de sucesso. É a versão agêntica dos testes unitários — e tão indispensável quanto.

### 5.3 Shadow runs e canary

Antes de promover uma nova versão do agente a produção total:

- **Shadow run:** a nova versão roda *em paralelo* com a atual, sem afetar usuários, para comparar resultados.
- **Canary:** libere a nova versão para uma *fração* do tráfego, monitore, e expanda gradualmente se estável.

Essas práticas reduzem o risco de mudanças em sistemas não-determinísticos.

### 5.4 Feedback humano estruturado

O feedback humano (thumbs up/down, correções) é sinal valioso — mas precisa ser *estruturado* (o que especificamente falhou?) e *incorporado* ao dataset (virar golden cases). Feedback não-incorporado é desperdiçado.

---

## Capítulo 6 — Reportando resultados

### 6.1 O eval report

A avaliação precisa ser *comunicada*. Um **eval report** estrutura os resultados: o que foi avaliado, com que conjunto, quais métricas, quais resultados, quais falhas, quais correções. O template está em [`24-Templates/template-eval-report.md`](../../24-Templates/template-eval-report.md). Um bom eval report é *reproduzível* — alguém com o código e os dados chega aos mesmos números.

### 6.2 Análise de falhas

Erros precisam de *categorização*: não basta "X% de falha" — é preciso *quais* falhas, *por que*. Agrupe por causa-raiz (alucinação em tool calling, loop, contexto perdido, etc.) e priorize correções pelo impacto. A categorização transforma dados em *insight acionável*.

### 6.3 Comparações honestas

Compare contra *baselines* honestos: vs versão anterior, vs um prompt simples, vs humano. "85% de sucesso" significa pouco sem contexto; "85% vs 70% da versão anterior, vs 60% do baseline simples" comunica progresso real.

### 6.4 Comunicação para stakeholders

Para decisores (que podem não ser técnicos), comunique o que importa: taxa de sucesso *no domínio*, custo por tarefa, principais modos de falha e o plano de mitigação. Evite jargão; use números concretos e comparações familiares.

---

## Capítulo 7 — Casos de estudo

### 7.1 Anthropic avaliando Claude em SWE-bench

O caso canônico de AgentOps é a própria avaliação de modelos em benchmarks: Anthropic (e OpenAI, etc.) usam SWE-bench para medir capacidades de coding, com metodologia rigorosa para evitar contaminação. A lição: *mesmo os criadores dos modelos dependem de avaliação sistemática* — não há atalho para "saber se está bom".

> **Leitura.** [`09-CaseStudies/`](../../09-CaseStudies/) e Research KB ([`20-Research/`](../../20-Research/), benchmarks).

### 7.2 Lições transversais

1. **Sem avaliação sistemática, você não sabe.** Intuição é insuficiente em sistemas estocásticos.
2. **Observabilidade é pré-requisito de confiança.** Traces + métricas + golden cases.
3. **Avaliação é contínua, não pontual.** CI para agentes, dataset crescente.

---

## Capítulo 8 — Referências e leituras

### 8.1 Bibliografia fundamental

- **Jimenez, C. et al.** *SWE-bench.* arXiv:2310.06770. 🏛
- **Mialon, G. et al.** *GAIA.* arXiv:2311.12983. 🏛
- **Yao, S. et al.** *τ-bench.* arXiv:2404.44529. 🏛

### 8.2 Bibliografia complementar

- **Liu, X. et al.** *AgentBench.* arXiv:2308.03688.
- **Zhou, S. et al.** *WebArena.* arXiv:2307.13854.
- **OpenTelemetry** GenAI semantic conventions.

### 8.3 Recursos práticos

- **Tooling:** LangSmith, Phoenix (Arize), Langfuse, OpenLLMetry, Ragas, DeepEval, TruLens.
- **Red team:** Garak, PyRIT (aprofundado em ETHAGT13).
- **Leitura:** Hamel Husain *Evals for LLMs*; Eugene Yan blog.

### 8.4 Ficha de pesquisa

Fontes em [`20-Research/ETHAGT12-pesquisa.md`](../../20-Research/ETHAGT12-pesquisa.md). Revalidar benchmarks a cada 6 meses. Última consulta: Julho 2026.

---

## Síntese do módulo

Ao concluir ETHAGT12, você deve ser capaz de:

1. **Implementar** observabilidade end-to-end (traces, spans, métricas) com tooling apropriado.
2. **Construir** pipelines de avaliação automatizada (LLM-as-judge calibrado, golden cases, regressão).
3. **Aplicar** benchmarks canônicos (SWE-bench, GAIA, τ-bench) com consciência de seus limites.
4. **Operar** ciclos de melhoria contínua (CI, shadow, canary, feedback).
5. **Reportar** resultados com rigor (eval report reproduzível, análise de falhas categorizada).

Próximos passos: ETHAGT13 (Segurança) usa a observabilidade daqui para detecção de ataques; ETHAGT90 exige um eval report completo no Capstone.

---

*Mantido por: Escola de Tecnologia — Universidade Etho · Área de Inteligência Artificial · Versão 1.0 · Julho 2026*
