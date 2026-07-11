# ETHAGT12 — Slides Detalhados + Notas do Professor (Parte 1: Slides 1-43)

> Universidade Etho · Especialização em Programação Agêntica
> Cada slide contém: título, objetivo, conteúdo, notas do professor, diagrama, animação, imagem, tempo.

---

## SEÇÃO A — Abertura (Slides 1-6 · 8 min)

---

### Slide 1 — Capa

**Título**: ETHAGT12 — AgentOps, Observabilidade & Avaliação
**Objetivo**: Identificar a aula, o professor e o contexto dentro da especialização.
**Conteúdo**:
- ETHAGT12 — AgentOps, Observabilidade & Avaliação (LLMOps para agentes)
- Universidade Etho · Especialização em Programação Agêntica
- Fase D — Produção, Governança e Fronteira · 30 h
- Professor · Data

**Diagrama**: Logo Etho (canto sup. esquerdo) + imagem de fundo com dashboards e grafos de traces
**Animação**: Fade in do título (300ms)
**Imagem**: Fundo `etho-dark` (#0F1E2D) com pattern sutil de traces e spans
**Tempo**: 1 min

**Rodape**: AgentOps = Agent Operations — operacao e monitoramento de agentes em producao  ·  LLMOps = LLM Operations — praticas de MLOps adaptadas a LLMs

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Bem-vindos. Esta é a aula que separa quem brinca de agentes de quem opera agentes em produção. Até aqui vocês aprenderam a construir. Agora aprendem a saber se está bom, se ficou pior e por quê. AgentOps é a disciplina que dá confiança para iterar.
💡 ANALOGIA: É como a diferença entre saber dirigir e ter um painel com velocímetro, combustível e temperatura. Sem painel você até dirige — mas não sabe quando vai quebrar.
❓ PERGUNTA PARA A TURMA: "Quantos de vocês já deploysaram um agente sem saber se ele estava melhor ou pior que a versão anterior?" (a maioria vai levantar a mão)
⚠️ ERROS COMUNS: Alunos chegam achando que "AgentOps" é só colocar logs. Não — é observar (traces), medir (métricas), avaliar (evals) e iterar (CI). Hoje cobrimos os quatro.
➡️ TRANSIÇÃO: "Vamos definir o que vocês devem conseguir fazer ao final."

---

### Slide 2 — Objetivos do Módulo

**Título**: Objetivos do Módulo
**Objetivo**: Deixar claro o que o aluno deve conseguir FAZER ao final da aula.
**Conteúdo**:
- **Objetivo geral**: Estabelecer rigor experimental em sistemas de agentes — observar (traces), medir (métricas), avaliar (evals e benchmarks) e iterar com confiança
- **Objetivos específicos**:
  1. Implementar observabilidade end-to-end (traces, spans, métricas)
  2. Construir pipelines de avaliação automatizada (LLM-as-judge, golden cases, regressão)
  3. Aplicar benchmarks canônicos (SWE-bench, GAIA, τ-bench, AgentBench, WebArena)
  4. Operar ciclos de melhoria contínua com dados
  5. Reportar resultados com rigor (eval report)

**Diagrama**: 5 ícones representando cada objetivo (lupa, gráfico, balança, loop, relatório)
**Animação**: Objetivos aparecem um a um (on click)
**Imagem**: Ícones minimalistas em `etho-accent` (#E85D2F)
**Tempo**: 2 min

**Rodape**: LLM = Large Language Model — Modelo de Linguagem de Grande Escala  ·  SWE-bench = Software Engineering Benchmark — benchmark de issues reais do GitHub

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Cada objetivo é mensurável. Não é "entender traces" — é "implementar observabilidade". Não é "conhecer benchmarks" — é "aplicar benchmarks". Se ao final vocês não conseguem fazer essas cinco coisas, eu falhei. Vamos revisar no Slide 70.
💡 ANALOGIA: É como um checklist de pré-voo. Não basta o piloto "saber que existe manometro" — ele precisa conferir. Hoje, nosso checklist é esses 5 objetivos.
❓ PERGUNTA PARA A TURMA: "Qual desses objetivos vocês acham mais desafiador no trabalho de vocês?" (deixar responder — costuma ser #2 ou #4)
⚠️ ERROS COMUNS: Alunos acham que LLM-as-judge é plug-and-play. Não é — tem vieses que precisam de mitigação. Cobrimos isso na Seção D.
➡️ TRANSIÇÃO: "Vamos ver onde estamos no mapa de competências da especialização."

---

### Slide 3 — Competências Desenvolvidas

**Título**: Competências Desenvolvidas
**Objetivo**: Conectar a aula ao Framework Etho de competências.
**Conteúdo**:

| Competência | Nível ao final | Próximo nível em |
|---|---|---|
| C1 Programação Agêntica | **A** (Avançado) | Capstone |
| C2 Multi-Agent Systems | B (Básico) | ETHAGT09-10 |
| C4 Agent Memory | B (Básico) | ETHAGT05 |
| C5 AgentOps & Avaliação | **A** (Avançado) | Capstone |

**Diagrama**: Radar chart com 4 eixos mostrando nível A/B
**Animação**: Radar aparece com wipe (left-to-right, 500ms)
**Imagem**: Badge visual por competência (círculos coloridos)
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O Framework Etho tem 6 competências em 3 níveis. Este módulo atinge nível **A** em duas competências críticas: C1 (você justifica arquitetura de agentes) e C5 (você opera eval completo). É o módulo que consolida a maturidade técnica do programador agêntico.
💡 ANALOGIA: É como sair de motorista amador para piloto com telemetria. Você não só dirige — você lê dados, decide com base em métrica, reporta com rigor.
⚠️ ERROS COMUNS: Alunos subestimam "Avaliação". Acham que é só um quiz. Não — é a diferença entre um agente que parece funcionar e um agente que você consegue melhorar de forma sistemática.
➡️ TRANSIÇÃO: "Vamos ver como esta aula está estruturada."

---

### Slide 4 — Agenda

**Título**: Agenda da Aula
**Objetivo**: Mostrar o roteiro da aula com tempos estimados.
**Conteúdo**:
- **Bloco 1 (45 min)**:
  - Abertura (8 min) — objetivos, motivação, contexto
  - Por que difícil (10 min) — não-determinismo, falácias
  - Observabilidade (16 min) — traces, OTel, DEMO
  - Intervalo (5 min)
- **Bloco 2 (45 min)**:
  - Avaliação (18 min) — LLM-as-judge, golden cases, CI, DEMO
  - Benchmarks (14 min) — SWE-bench, GAIA, τ-bench
  - Melhoria & Report (12 min) — dataset, eval report
  - Fechamento — boas práticas, caso, quiz, projeto, Q&A

**Diagrama**: Timeline horizontal com 7 seções coloridas
**Animação**: Timeline cresce da esquerda para direita (500ms)
**Imagem**: Ícones de relógio por seção
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A aula tem dois blocos. O primeiro cobre observabilidade — a base para tudo. O segundo é a parte de avaliação e melhoria contínua. Há duas DEMOs ao vivo: traces (Slide 24) e eval automatizado (Slide 40). Tenham paciência — elas são o coração da aula.
⚠️ ERROS COMUNS: Alunos chegam atrasados e perdem a motivação (Slide 5). Avisar que o "5/5 no teste, 30% em produção" define o tom de toda a aula.
➡️ TRANSIÇÃO: "Vamos começar pelo porquê."

---

### Slide 5 — Motivação: 5/5 no Teste, 30% em Produção

**Título**: 5/5 no Teste, 30% em Produção
**Objetivo**: Criar tensão — agentes não-determinísticos falham em casos que você não testou.
**Conteúdo**:
- **Cenário real**: agente funcionou 5/5 no teste manual, mas em produção acertou só 30%
- Sem métrica, você não sabia que estava falhando
- "Parece que funciona" não é medida
- Usuários desistem silenciosamente — não reclamam, só somem
- **Pergunta**: *Como você sabe se seu agente está ficando melhor ou pior?*

**Diagrama**: Gráfico de barras — "Teste manual: 100%" vs "Produção: 30%"
**Animação**: Barras crescem lado a lado; a de produção para em 30%
**Imagem**: Barras em `etho-danger` (vermelho) para o gap
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esse é o slide mais importante da abertura. Aconteceu com todo mundo que colocou agente em produção sem eval. Você testa 5 casos, todos passam, faz deploy. Semana depois, métrica de retenção cai. Por quê? Porque os 5 casos que você testou não representam os 1000 que os usuários geram. Sem observabilidade e eval, você está cego.
💡 ANALOGIA: É como aprovar um remédio testando em 5 pessoas. "Funcionou nos 5!" Sim — mas e nos outros 9995?
❓ PERGUNTA PARA A TURMA: "Como você sabe se seu agente está ficando melhor ou pior?" (deixar pensar — geralmente silêncio. Esse silêncio é o gancho da aula toda.)
⚠️ ERROS COMUNS: Alunos acham que "testar mais 10 casos" resolve. Não resolve — você precisa de observabilidade em produção + eval sistemática.
➡️ TRANSIÇÃO: "Por que AgentOps se tornou uma disciplina só agora?"

---

### Slide 6 — Contexto: Por Que AgentOps Agora

**Título**: Por Que AgentOps Agora
**Objetivo**: Explicar a confluência histórica que tornou AgentOps essencial.
**Conteúdo**:
- **Linha do tempo**:
  - 2022 — ChatGPT: LLM como oráculo
  - 2023 — Primeiros agentes (AutoGPT, ReAct em produção)
  - 2024 — SWE-bench, GAIA, Phoenix/Langfuse surgem
  - 2025 — AgentOps consolida como disciplina
  - 2026 — AgentOps é pré-requisito para produção séria
- **Confluência**: agentes não-determinísticos + custo de runs + necessidade de iterar com confiança
- LLMOps tradicional não cobre: tools, loops, estado, ambiente
- Hamel Husain: "Evals for LLMs" como marco conceitual

**Diagrama**: Timeline horizontal com marcos
**Animação**: Marcos aparecem sequencialmente
**Imagem**: Ícones por ano
**Tempo**: 1 min

**Rodape**: ReAct = Reasoning and Acting — padrao de loop Thought / Action / Observation

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: LLMOps tradicional cobre treinar, deployar e monitorar um modelo. AgentOps cobre isso MAIS o comportamento emergente: tools, loops, estado, ambiente. É uma camada a mais. Hamel Husain formalizou o conceito de "evals for LLMs" em 2024 e a partir daí a disciplina se estruturou.
💡 ANALOGIA: É como a diferença entre monitorar um servidor web (LLMOps) e monitorar um sistema distribuído com microserviços (AgentOps). Mais moving parts, mais coisas que dão errado.
➡️ TRANSIÇÃO: "Antes das soluções, vamos entender o problema. Por que agentes são tão difíceis de avaliar?"

---

## SEÇÃO B — Por que Agentes São Difíceis de Avaliar (Slides 7-14 · 10 min)

---

### Slide 7 — [SEÇÃO] Por que Agentes São Difíceis de Avaliar

**Título**: 1 — Por que Agentes São Difíceis de Avaliar
**Objetivo**: Transição para o bloco de fundamentos.
**Conteúdo**: Número "1" grande + "Por que Agentes São Difíceis de Avaliar"
**Diagrama**: Fundo `etho-primary`
**Animação**: Número cresce com zoom
**Tempo**: 0.5 min

**Notas do Professor**:
➡️ TRANSIÇÃO: "Vamos entender por que avaliar agentes é mais difícil que avaliar software tradicional."

---

### Slide 8 — Não-Determinismo em Agentes

**Título**: Não-Determinismo em Agentes
**Objetivo**: Explicar por que a mesma entrada pode dar resultados diferentes.
**Conteúdo**:
- LLMs são probabilísticos: mesma pergunta, respostas diferentes
- Agentes amplificam: cada step tem não-determinismo que se acumula
- Temperatura, sampling, tool choice podem variar
- **Implicação**: avaliação única não é suficiente — precisamos de N runs
- **Pergunta**: *Você já rodou o mesmo prompt duas vezes e teve resultados diferentes?*

**Diagrama**: Árvore de possibilidades — 1 prompt → múltiplos caminhos
**Animação**: Ramos da árvore aparecem um a um
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Num código tradicional, `f(2)` sempre retorna 4. Num agente, `f("reserve um voo")` pode retornar 10 caminhos diferentes. Cada chamada do LLM é probabilística, e o agente faz 10-50 chamadas. A variância se acumula. Por isso precisa de N runs (mínimo 3, idealmente 5-10) por caso no eval.
💡 ANALOGIA: É como jogar uma moeda 10 vezes em sequência. Mesmo começando igual, cada jogada pode sair diferente. O caminho final raramente é o mesmo.
❓ PERGUNTA PARA A TURMA: "Vocês já rodaram o mesmo prompt duas vezes e tiveram resultados diferentes?" (todos vão concordar)
⚠️ ERROS COMUNS: Alunos fazem eval com 1 run e se surpreendem quando o resultado varia. Sempre reportar média + desvio, não ponto único.
➡️ TRANSIÇÃO: "Não-determinismo é um problema. Mas tem mais: agentes dependem de ambiente."

---

### Slide 9 — Dependência de Ambiente

**Título**: Dependência de Ambiente
**Objetivo**: Mostrar que agentes dependem de mundo externo mutável.
**Conteúdo**:
- Tools chamam APIs que podem mudar de comportamento
- RAG depende de base de conhecimento que evolui
- Ambiente de execução (sistema de arquivos, web) muda entre runs
- **Exemplo**: agente que usa API de cotação — resultado depende do momento
- **Implicação**: avaliação precisa de ambiente controlado ou sandbox

**Diagrama**: Agente cercado por fontes externas mutáveis (API, DB, Web, FS)
**Animação**: Fontes externas piscam
**Tempo**: 1.5 min

**Rodape**: RAG = Retrieval-Augmented Generation — Geracao Aumentada por Recuperacao

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Em código tradicional, você pode mockar dependências. Em agente, você mocka tools e perde realismo. Esse é o dilema: ou você testa em ambiente real (mas o resultado varia) ou em ambiente mockado (mas não testa o caso real). Solução: ambiente controlado (sandbox) com fixtures conhecidas.
💡 ANALOGIA: É como testar um piloto de F1. Se você testa no simulador, é previsível mas irreal. Se testa na pista molhada, é real mas caótico. Você precisa de ambos.
⚠️ ERROS COMUNS: Alunos fazem eval em produção direto. Isso gera custo real e variância alta. Use sandbox.
➡️ TRANSIÇÃO: "Tem mais um problema: avaliar agentes custa dinheiro de verdade."

---

### Slide 10 — Custo de Runs

**Título**: Custo de Runs
**Objetivo**: Explicar que avaliar agentes custa dinheiro real.
**Conteúdo**:
- Cada run = tokens de entrada + tokens de saída × N steps
- Agente complexo: 10-50 chamadas de LLM por tarefa
- **Cálculo**: 1000 casos × 50 chamadas × $0.01/chamada = **$500**
- Benchmarks completos (SWE-bench): centenas de dólares por modelo
- **Estratégias**: amostragem, subconjuntos, eval incremental

**Diagrama**: Fórmula de custo cumulativo
**Animação**: Fórmula aparece termo a termo
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Diferente de testes unitários (gratuitos), cada execução de agente custa tokens. Avaliar 1000 casos com agente complexo pode custar centenas de dólares. Por isso estratégia de eval importa: começar com subconjunto (10-50 casos), iterar rápido, expandir quando estiver confiante.
💡 ANALOGIA: É como fazer pesquisa de mercado. Se você entrevista 1000 pessoas, custa caro. Você começa com 30, valida o questionário, depois expande.
❓ PERGUNTA PARA A TURMA: "Qual o orçamento de eval de vocês hoje?" (geralmente: zero. Esse é o problema.)
⚠️ ERROS COMUNS: Alunos rodam eval completo a cada commit. Custa caro e demora. Eval de CI = subconjunto; eval completo = noturno ou pré-deploy.
➡️ TRANSIÇÃO: "Diante dessas dificuldades, surgem falácias. Vamos quebrá-las."

---

### Slide 11 — Falácias Comuns de Avaliação

**Título**: Falácias Comuns de Avaliação
**Objetivo**: Desconstruir crenças perigosas sobre avaliação de agentes.
**Conteúdo**:
- **"Funcionou uma vez"** → sobrevivência de amostra size=1
- **"Parece bom"** → vibes-based eval, não escala
- **"O usuário não reclamou"** → usuários desistem silenciosamente
- **"Passou no benchmark"** → benchmark ≠ produção
- **"LLM disse que está correto"** → LLM-as-judge sem calibração
- **Pergunta**: *Qual dessas falácias você já cometeu?*

**Diagrama**: 5 cards de falácia com ícone de "armadilha"
**Animação**: Cards aparecem um a um com efeito de "queda"
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Essas 5 falácias são a causa número 1 de agentes que parecem funcionar mas falham em produção. Cada uma tem uma armadilha: amostra pequena, viés de confirmação, sobrevivência silenciosa, overfitting de benchmark, confiança cega em LLM. Vamos desconstruir cada uma.
💡 ANALOGIA: É como dirigir bêbado e chegar em casa. "Funcionou!" Sim — desta vez. Na próxima você bate. Avaliação é o bafômetro.
❓ PERGUNTA PARA A TURMA: "Qual dessas falácias vocês já cometeram?" (a maioria vai rir — todos cometemos)
⚠️ ERROS COMUNS: Alunos acham que "funcionou uma vez" é validação. Não é — é sorte. Repita 10 vezes e veja.
➡️ TRANSIÇÃO: "Essas falácias viram avaliação pontual. Vamos ver por que isso não funciona."

---

### Slide 12 — Avaliação Contínua vs Pontual

**Título**: Avaliação Contínua vs Pontual
**Objetivo**: Mostrar que avaliação não é evento, é processo.
**Conteúdo**:
- **Pontual**: "rodamos eval antes do deploy" → estátua (congela no tempo)
- **Contínua**: eval roda a cada mudança, em produção, com drift detection
- Agentes mudam: prompt, tool, modelo, ambiente evoluem
- Sem eval contínua: regressão passa despercebida por semanas

**Diagrama**: Duas timelines — pontual (marcas isoladas) vs contínua (linha contínua)
**Animação**: Linha contínua cresce vs marcas isoladas aparecem
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Avaliação pontual é foto. Avaliação contínua é vídeo. Em agentes, você precisa do vídeo porque tudo muda: o modelo do provedor atualiza sem aviso, a API que você usa muda formato, a base de RAG cresce. Cada mudança pode causar regressão silenciosa. Sem eval contínua, você descobre a regressão quando o usuário reclama — tarde demais.
💡 ANALOGIA: É como checkup médico. Ir uma vez por ano é pontual. Monitorar a saúde todo dia com smartwatch é contínuo. Agentes em produção precisam do smartwatch.
➡️ TRANSIÇÃO: "A falácia mais comum tem nome: vibes-based eval."

---

### Slide 13 — Vibes-Based Eval: A Armadilha

**Título**: Vibes-Based Eval
**Objetivo**: Fixar o anti-pattern mais comum.
**Conteúdo**:
- *"Se você não tem um conjunto de avaliação, você está fazendo vibes-based development."* — Hamel Husain
- Vibes = intuição, não medida
- Intuição é útil para explorar, não para decidir deploy
- **Regra**: todo deploy precisa de número, não de feeling

**Diagrama**: Ícone de "vibes" (emoji/sentimento) vs ícone de "métrica" (gráfico)
**Animação**: Vibes treme, métrica fica estável
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Hamel Husain cunhou esse termo. Vibes-based eval é quando você "sente" que o agente está melhor. Não está. Seu cérebro é péssimo em avaliar sistemas estocásticos sem dados. A regra de ouro: se você não consegue colocar um número no que mudou, você não deveria deployar.
💡 ANALOGIA: É como decidir se a dieta está funcionando "no feeling". Sem balança, você está mentindo para si mesmo.
➡️ TRANSIÇÃO: "Vamos praticar reconhecendo falácias."

---

### Slide 14 — Exercício: Identificando Falácias

**Título**: Exercício — Identificando Falácias
**Objetivo**: Praticar o reconhecimento de falácias em cenários reais.
**Conteúdo**:
- Identifique a falácia em cada afirmação:
  1. "Testei com 3 exemplos e funcionou, pode ir para produção."
  2. "O benchmark mostra 80%, então o agente está bom."
  3. "O GPT-4 disse que a resposta está correta."
  4. "Ninguém reclamou desde o deploy."
- Votação rápida (mãos levantadas)

**Diagrama**: 4 cards com afirmações
**Animação**: Cards aparecem um a um
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Respostas esperadas:
1. Sample size=1 — sobrevivência de amostra minúscula
2. Benchmark ≠ produção — overfitting de benchmark
3. Self-preference — LLM-as-judge sem calibração
4. Sobrevivência silenciosa — usuários desistem sem reclamar
❓ PERGUNTA PARA A TURMA: Mostrar uma afirmação por vez e pedir votação. Anotar resultados no quadro.
⚠️ ERROS COMUNS: Alunos acham que #4 é OK. Não é — usuários desistem. Sem telemetria, você não vê.
➡️ TRANSIÇÃO: "Agora que entendemos o problema, vamos para a primeira solução: observabilidade."

---

## SEÇÃO C — Observabilidade (Slides 15-27 · 16 min)

---

### Slide 15 — [SEÇÃO] Observabilidade Desde o Dia 1

**Título**: 2 — Observabilidade: Traces, Spans, Métricas
**Objetivo**: Transição para o bloco de observabilidade.
**Conteúdo**: "2 — Observabilidade Desde o Dia 1"
**Diagrama**: Fundo `etho-primary`
**Animação**: Número cresce com zoom
**Tempo**: 0.5 min

**Notas do Professor**:
➡️ TRANSIÇÃO: "Observabilidade é a base de tudo. Sem ela, você não sabe o que medir."

---

### Slide 16 — Traces: O Que São

**Título**: Traces: O Que São
**Objetivo**: Introduzir o conceito de trace como árvore de execução.
**Conteúdo**:
- **Trace** = registro completo de uma execução de agente
- Estrutura de árvore: root span → child spans → sub-spans
- Cada span: nome, duração, input, output, atributos
- Diferença de log: trace mostra relações e hierarquia
- *"Sem traces, você está debugando no escuro"*

**Diagrama**: Árvore de spans conceitual
**Animação**: Spans surgem da raiz para as folhas
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Trace é a unidade fundamental de observabilidade de agentes. Quando um agente executa uma tarefa, ele gera um trace — uma árvore hierárquica de spans, onde cada span é uma operação (chamada de LLM, tool call, retrieval). A árvore mostra quem chamou quem, quanto tempo cada passo levou, e o que entrou/saiu de cada um. Diferente de logs (que são uma sequência plana), traces mostram relações.
💡 ANALOGIA: É como uma árvore genealógica. Logs são a lista telefônica — todo mundo junto, sem hierarquia. Traces mostram quem é pai de quem, neto de quem.
⚠️ ERROS COMUNS: Alunos confundem trace com log. Log é uma linha; trace é uma árvore com timing.
➡️ TRANSIÇÃO: "Vamos ver a anatomia de um trace real."

---

### Slide 17 — Anatomia de um Trace

**Título**: Anatomia de um Trace
**Objetivo**: Mostrar a estrutura detalhada de um trace de agente.
**Conteúdo**:
- **Root span**: tarefa completa (ex: "reservar voo")
- **Child spans**: chamada LLM 1, tool call A, chamada LLM 2, tool call B
- **Sub-spans**: API request dentro de tool call
- **Atributos por span**: model, tokens, latency, tool name, args, result
- **Bags**: contexto propagado entre spans (user_id, session_id)

**Diagrama**: `12-Diagrams/ETHAGT12/trace-anatomy.mmd`
**Animação**: Spans aparecem hierarquicamente (root → children → sub-spans)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vamos destrinchar o diagrama. O root span é a tarefa inteira. Dentro dele, cada operação é um child span: chamadas de LLM, tool calls. Dentro de cada tool call, podem existir sub-spans (ex: a chamada HTTP). Cada span carrega atributos: modelo usado, tokens consumidos, latência, args, result. Bags são o contexto propagado entre spans (user_id, session_id) — fundamentais para correlacionar traces de usuários diferentes.
💡 ANALOGIA: É como uma receita de bolo. O root span é "fazer bolo". Child spans: "misturar", "assar", "cobrir". Sub-spans: "ralar chocolate" dentro de "cobrir". Cada passo tem duração e ingredientes (atributos).
⚠️ ERROS COMUNS: Alunos não propagam bags entre spans. Resultado: traces isolados que não conectam a usuários. Sempre propagar context.
➡️ TRANSIÇÃO: "Como padronizar isso? OpenTelemetry."

---

### Slide 18 — OpenTelemetry para LLMs

**Título**: OpenTelemetry para LLMs
**Objetivo**: Apresentar o padrão de observabilidade para GenAI.
**Conteúdo**:
- **OpenTelemetry** (OTel): padrão CNCF para observabilidade distribuída
- **GenAI semantic conventions**: atributos padronizados para LLMs
  - `gen_ai.system`, `gen_ai.request.model`, `gen_ai.usage.prompt_tokens`
- **Vantagem**: vendor-neutral — funciona com qualquer backend
- Para agentes: traces cruzam LLM calls, tool calls, retrieval

**Diagrama**: Exemplo de span com atributos GenAI
**Animação**: Atributos aparecem um a um
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: OpenTelemetry é o padrão CNCF para observabilidade distribuída. Para LLMs, ele define "GenAI semantic conventions" — atributos padronizados como `gen_ai.system` (provedor), `gen_ai.request.model` (modelo), `gen_ai.usage.prompt_tokens` (tokens de entrada). A vantagem é vendor-neutral: você escreve uma vez e envia para qualquer backend (LangSmith, Phoenix, Langfuse, Datadog). Para agentes, OTel é poderoso porque traces cruzam tudo: chamadas de LLM, tool calls, retrieval.
💡 ANALOGIA: É como o USB-C. Antes, cada marca tinha seu conector. Agora é padrão — qualquer cabo funciona em qualquer aparelho. OTel é o USB-C da observabilidade.
⚠️ ERROS COMUNS: Alunos usam ferramenta X e depois não conseguem migrar para Y. OTel dá portabilidade.
➡️ TRANSIÇÃO: "Quais ferramentas implementam isso?"

---

### Slide 19 — Tooling: LangSmith, Phoenix, Langfuse

**Título**: Tooling: LangSmith, Phoenix, Langfuse
**Objetivo**: Apresentar as ferramentas principais de observabilidade para agentes.
**Conteúdo**:

| Ferramenta | Stack | Modelo | Foco |
|---|---|---|---|
| LangSmith | LangChain/LangGraph | Comercial SaaS | Dashboard rico, integrado ao LangChain |
| Phoenix (Arize) | Agnóstico | Open source | LLM observability + eval integrado |
| Langfuse | Agnóstico | Open source self-hostable | Traces + eval + prompts management |
| OpenLLMetry | Agnóstico | Open source | Instrumentação OTel automática |

- **Critério de escolha**: stack existente, self-host vs SaaS, custo

**Diagrama**: Tabela comparativa (4 colunas)
**Animação**: Linhas aparecem uma a uma
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Quatro ferramentas dominam. LangSmith é a escolha natural se você já usa LangChain/LangGraph — integração nativa, dashboard rico. Phoenix (da Arize) é open source e agnóstico — bom se você quer independência. Langfuse é open source e self-hostable — ideal para empresas com restrição de dados. OpenLLMetry é instrumentação automática — pluga OTel sem mudar código. A escolha depende de três coisas: stack existente, self-host vs SaaS, custo.
💡 ANALOGIA: É como escolher entre AWS, GCP e Azure. Todas fazem a mesma coisa. A escolha depende do que você já usa e do seu orçamento.
❓ PERGUNTA PARA A TURMA: "Qual de vocês já usa alguma dessas em produção?" (maioria: nenhuma — esse é o ponto)
⚠️ ERROS COMUNS: Alunos escolhem pela ferramenta mais hype. Escolha pelo fit com seu stack e seus requisitos de compliance.
➡️ TRANSIÇÃO: "Falando em ferramentas, vamos diferenciar logs de traces."

---

### Slide 20 — Logs Estruturados vs Traces

**Título**: Logs Estruturados vs Traces
**Objetivo**: Clarificar quando usar cada abordagem.
**Conteúdo**:
- **Logs estruturados**: JSON com timestamp, step, thought, action, observation
- **Traces**: árvore hierárquica com timing e relações
- **Logs**: simples, barato, bom para debug rápido
- **Traces**: rico, relacional, bom para análise e produção
- **Prática**: comece com logs estruturados, evolua para traces
- Complementares, não mututalmente exclusivos

**Diagrama**: Comparação lado a lado
**Animação**: Dois lados aparecem em paralelo
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Logs e traces não competem — complementam. Logs estruturados são JSON com timestamp, step, thought, action. São simples e baratos. Bom para debug rápido. Traces são árvores hierárquicas com timing e relações. São ricos mas custam mais storage. A regra prática: comece com logs estruturados (todo projeto deve ter desde o dia 1) e evolua para traces quando precisar de análise relacional.
💡 ANALOGIA: É como diferença entre diário (logs: uma entrada por vez) e organograma (traces: quem reporta para quem).
⚠️ ERROS COMUNS: Alunos começam sem nada e querem pular direto para traces. Sem logs estruturados primeiro, você não sabe nem o que tracear.
➡️ TRANSIÇÃO: "Observabilidade também custa. Vamos falar de amostragem."

---

### Slide 21 — Custo de Observabilidade (Amostragem)

**Título**: Custo de Observabilidade
**Objetivo**: Explicar que observabilidade também custa.
**Conteúdo**:
- Cada trace gera storage + processamento
- Em alto volume: 100% de traces é caro
- **Amostragem**: registrar apenas 1 em N traces
- **Estratégias**: head-based (decide no início), tail-based (decide no fim)
- **Tail sampling**: sempre logar traces com erro, amostrar sucesso
- **Regra**: 100% em dev, amostrado em produção, 100% em erro

**Diagrama**: Funil de amostragem
**Animação**: Funil aparece, erro escapa por fora
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Observabilidade tem custo. Cada trace ocupa storage. Em alto volume (milhões de traces/dia), 100% é caro. Amostragem é a solução: registrar só uma fração. Head-based decide no início do trace (rápido mas cego ao que vai acontecer). Tail-based decide no fim (consegue priorizar erros). A regra de ouro: 100% em dev (barato e necessário), amostrado em produção (controle de custo), 100% em erro (sempre capture falhas).
💡 ANALOGIA: É como câmera de segurança. Você não grava tudo o tempo todo (caro). Grava quando detecta movimento (tail sampling).
⚠️ ERROS COMUNS: Alunos amostram em produção e perdem os erros. Erros devem ser 100% capturados sempre.
➡️ TRANSIÇÃO: "Com traces em mãos, vamos montar um dashboard."

---

### Slide 22 — Dashboard Mínimo de Observabilidade

**Título**: Dashboard Mínimo de Observabilidade
**Objetivo**: Definir o que todo dashboard de agente deve ter.
**Conteúdo**:
- **Painel 1**: Success rate por tarefa (últimas 24h)
- **Painel 2**: Latência P50/P95/P99 por step
- **Painel 3**: Custo por execução (tokens × preço)
- **Painel 4**: Tool usage (qual tool, quantas vezes, sucesso/falha)
- **Painel 5**: Erros agrupados por tipo
- **Painel 6**: Distribuição de steps (agente fazendo muitos loops?)

**Diagrama**: Mock de dashboard com 6 painéis
**Animação**: Painéis aparecem em grid
**Tempo**: 1.5 min

**Rodape**: P95 = Percentil 95 — latencia abaixo da qual 95% das requisicoes ficam  ·  P99 = Percentil 99 — latencia abaixo da qual 99% das requisicoes ficam

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esse é o dashboard mínimo. Se você tem esses 6 painéis, você consegue operar um agente em produção. Success rate diz se está funcionando. Latência P50/P95/P99 diz se está rápido. Custo diz se está sustentável. Tool usage mostra gargalos. Erros agrupados direcionam correção. Distribuição de steps detecta loops. Sem esses, você está cego.
💡 ANALOGIA: É como o painel do carro. Velocímetro, combustível, temperatura, RPM — cada um diz algo essencial. Sem um deles você pode quebrar sem saber.
➡️ TRANSIÇÃO: "Das métricas no dashboard, duas são de primeira classe: custo e latência."

---

### Slide 23 — Métricas de Primeira Classe: Custo e Latência

**Título**: Custo e Latência — Métricas de Primeira Classe
**Objetivo**: Fixar que custo e latência são métricas, não detalhes.
**Conteúdo**:
- **Custo por execução**: tokens in/out × preço por modelo
- **Latência cumulativa**: serial = soma; paralelo = max
- **P95 e P99** importam mais que média (cauda longa)
- **Orçamento por execução**: abortar se custo > limite
- Em produção: alerta se custo médio sobe 20%

**Diagrama**: Mini-gráfico de latência P50/P95/P99
**Animação**: Linhas P50/P95/P99 aparecem
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Custo e latência não são detalhes operacionais — são métricas de produto. Custo por execução define margem. Latência define experiência do usuário. Importante: média mente. Em distribuições com cauda longa (comum em agentes), P95 e P99 importam mais. Se P99 é 30s, 1 em 100 usuários espera meio minuto — inaceitável. Regra: orçamento por execução — se passar, aborta. Alerta se custo médio subir 20% — algo regrediu.
💡 ANALOGIA: É como salário. A média da turma pode ser R$ 5k, mas se o P95 é R$ 500, tem gente sofrendo. Em latência, o sofrimento está na cauda.
⚠️ ERROS COMUNS: Alunos reportam média de latência. Sempre reportar P50/P95/P99.
➡️ TRANSIÇÃO: "Vamos ver tudo isso na prática. DEMO!"

---

### Slide 24 — DEMO: Traces Everywhere

**Título**: DEMO — Traces Everywhere
**Objetivo**: Demo ao vivo — adicionar observabilidade a um agente existente.
**Conteúdo**:
- Código do `05-Labs/ETHAGT12/Lab1-Traces-Everywhere`
- Agente ReAct simples sem observabilidade
- Adicionar LangSmith (ou Phoenix) com 3 linhas
- Mostrar trace completo: pergunta → thought → tool call → observation → response
- Dashboard: latência, custo por step, erros
- Identificar gargalo no trace (tool call lenta)

**Diagrama**: Code block + trace viewer side-by-side
**Animação**: Highlight das linhas que adicionam observabilidade
**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vamos ao vivo. Tenho um agente ReAct simples, sem observabilidade. Vou adicionar LangSmith — literalmente 3 linhas (set env var, decorator, run). Depois vamos ver o trace gerado: cada step, cada tool call, latência por span, custo por chamada. Vamos identificar onde o agente demora — geralmente a tool call.
⚠️ ERROS COMUNS: Se a API falhar, tenho screenshot do trace gravado. Não se preocupem.
💡 ANALOGIA: É como ligar o modo desenvolvedor do navegador. De repente você vê tudo: requests, timing, headers. Mesma coisa com traces.
➡️ TRANSIÇÃO: "Pergunta da demo — em duplas."

---

### Slide 25 — Pergunta da DEMO

**Título**: Pergunta da DEMO
**Objetivo**: Engajar a turma com uma pergunta sobre a demo.
**Conteúdo**:
- "O que o trace revelou que logs simples não mostrariam?"
- "Qual step do agente é o gargalo de latência?"
- "Como você decidiria se vale otimizar esse step?"
- Discussão em duplas (2 min)

**Diagrama**: Caixa de discussão
**Animação**: Perguntas aparecem uma a uma
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Deixem 2 min em duplas. Pergunta chave: o que o trace revelou que logs não mostrariam? Resposta esperada: hierarquia (quem chamou quem), timing cumulativo, custo por step, atributos estruturados. Esses são os superpoderes do trace.
❓ PERGUNTA PARA A TURMA: Pedir 2 duplas para compartilhar. Anotar insights no quadro.
➡️ TRANSIÇÃO: "Vamos praticar leitura de trace com um problema."

---

### Slide 26 — Exercício: Lendo um Trace

**Título**: Exercício — Lendo um Trace
**Objetivo**: Praticar análise de trace para identificar problemas.
**Conteúdo**:
- Trace real com problema (agente em loop de 8 steps)
- Em duplas: identificar onde o loop acontece
- Propor 2 correções (max_steps? prompt? tool?)
- 2 min discussão, 1 min compartilhar

**Diagrama**: Trace de console com problema destacado
**Animação**: Loop destacado em vermelho
**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vou mostrar um trace onde o agente entrou em loop — repetiu a mesma action 8 vezes até bater max_steps. Em duplas: onde o loop acontece? Por quê? Duas correções? Respostas esperadas: loop no step 3-10 (mesma action repetida); correções incluem (1) prompt que instrui usar observations anteriores, (2) detecção de repetição no código, (3) ajustar tool description.
⚠️ ERROS COMUNS: Alunos sugerem só "aumentar max_steps". Isso não resolve — só mascara.
➡️ TRANSIÇÃO: "Última pergunta desta seção."

---

### Slide 27 — Pergunta: Observabilidade — Custo ou Investimento?

**Título**: Observabilidade — Custo ou Investimento?
**Objetivo**: Refletir sobre o ROI de observabilidade.
**Conteúdo**:
- "Observabilidade é custo operacional ou investimento estratégico?"
- **Argumento custo**: storage, tooling, overhead de instrumentação
- **Argumento investimento**: debugging mais rápido, regressão detectada, otimização guiada por dados
- *"Sem observabilidade, você não tem como melhorar o que não mede"*

**Diagrama**: Balança — custo vs investimento
**Animação**: Balança inclina para investimento
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Custo direto: storage de traces, tooling, overhead de instrumentação (1-5% de latência). Investimento: debugging 10x mais rápido, regressão detectada antes do deploy, otimização guiada por dados em vez de intuição. A pergunta não é "custo ou investimento" — é "quanto investimento vs custo". Em quase todo caso, o ROI é positivo. Sem observabilidade, você está developmentando cego.
➡️ TRANSIÇÃO: "Vamos para o coração da aula: avaliação automatizada."

---

## SEÇÃO D — Avaliação Automatizada (Slides 28-43 · 18 min)

---

### Slide 28 — [SEÇÃO] Avaliação Automatizada

**Título**: 3 — Avaliação Automatizada
**Objetivo**: Transição para o bloco de avaliação.
**Conteúdo**: "3 — Avaliação Automatizada: LLM-as-Judge, Golden Cases, Regressão"
**Diagrama**: Fundo `etho-primary`
**Animação**: Número cresce com zoom
**Tempo**: 0.5 min

**Rodape**: LLM-as-Judge = uso de um LLM como avaliador automatico de saidas de outro LLM

**Notas do Professor**:
➡️ TRANSIÇÃO: "Observabilidade é olhar. Avaliação é julgar. Vamos automatizar o julgamento."

---

### Slide 29 — Por que Avaliação Manual Não Escala

**Título**: Avaliação Manual Não Escala
**Objetivo**: Justificar a necessidade de automação.
**Conteúdo**:
- Manual: humano lê output e julga → lento, caro, inconsistente
- **Não escala**: 1000 casos × 5 min/caso = **83 horas**
- Humano fica cansado: qualidade decai ao longo do dia
- Não é reproduzível: mesmo humano julga diferente em outro dia
- **Solução**: automação com LLM-as-judge + golden cases + métricas programáticas

**Diagrama**: Escada de mão (manual, não escala) vs escada rolante (automatizada)
**Animação**: Escada rolante se move
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Manual funciona para 10 casos. Para 1000, não. O humano cansa (qualidade cai ao longo do dia), é inconsistente (mesmo humano julga diferente amanhã), e custa caro. Por isso precisamos automatizar. Mas automatizar não é só "rodar script" — é combinar três técnicas: LLM-as-judge (para casos subjetivos), golden cases com critério programático (para casos objetivos), e métricas (success rate, custo, latência).
➡️ TRANSIÇÃO: "A primeira técnica: LLM-as-judge."

---

### Slide 30 — LLM-as-Judge: Conceito

**Título**: LLM-as-Judge: Conceito
**Objetivo**: Apresentar o padrão de usar LLM para avaliar LLM.
**Conteúdo**:
- **LLM-as-judge**: um LLM avalia a saída de outro LLM
- **Padrão**: input + output + critério (rubrica) → judge → score + justificativa
- **Vantagem**: escala, barato, reproduzível (com temperatura 0)
- **Quando usar**: tarefas subjetivas (qualidade de resposta, completude)
- **Quando NÃO usar**: tarefas com ground truth exato (use string match)

**Diagrama**: Fluxo — agent output → judge prompt → judge LLM → score
**Animação**: Fluxo aparece da esquerda para direita
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: LLM-as-judge é elegante: você usa um LLM para avaliar a saída de outro. O padrão é simples — input + output + rubrica vão para o judge, que retorna score + justificativa. Vantagens: escala (1000 casos em minutos), barato (centavos por avaliação), reproduzível (com temperatura 0). Mas — e isso é crucial — não é mágica. Tem vieses que precisam de mitigação. E não use para tarefas com ground truth exato (ex: "Qual a capital da França?" — use string match, mais barato e confiável).
💡 ANALOGIA: É como um corretor de prova. Você treina o corretor com rubrica e ele corrige 1000 redações. Mas o corretor pode ter vieses — prefere redação longa, etc.
⚠️ ERROS COMUNS: Alunos usam LLM-as-judge para tudo. Para tarefas objetivas, métricas programáticas são melhores e mais baratas.
➡️ TRANSIÇÃO: "Vamos ser honestos: LLM-as-judge tem vieses."

---

### Slide 31 — LLM-as-Judge: Vieses

**Título**: LLM-as-Judge: Vieses
**Objetivo**: Ser honesto sobre as limitações do LLM-as-judge.
**Conteúdo**:
- **Positional bias**: prefere primeira ou última opção
- **Sycophancy**: concorda com o que o humano parece querer
- **Verbosity bias**: prefere respostas mais longas
- **Self-preference**: modelo prefere saídas do mesmo modelo
- **Knowledge bias**: judge não sabe o que o agente deveria saber
- **Pergunta**: *Qual desses vieses é mais perigoso para seu caso?*

**Diagrama**: 5 ícones de viés com labels
**Animação**: Ícones aparecem um a um
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Cinco vieses principais. Positional: em comparações A vs B, o judge prefere a primeira ou última posição apresentada. Sycophancy: se o prompt sugere a resposta esperada, o judge concorda. Verbosity: prefere respostas mais longas mesmo que menos corretas. Self-preference: GPT-4 prefere saídas de GPT-4. Knowledge: o judge não sabe o que o agente deveria saber e julga errado. Cada um tem mitigação — veremos no próximo slide.
❓ PERGUNTA PARA A TURMA: "Qual desses é mais perigoso para o caso de vocês?" (deixar responder — costuma variar por domínio)
⚠️ ERROS COMUNS: Alunos ignoram vieses e confiam cegamente no judge. Sempre calibrar com humano.
➡️ TRANSIÇÃO: "Para cada viés, uma mitigação."

---

### Slide 32 — LLM-as-Judge: Mitigações

**Título**: LLM-as-Judge: Mitigações
**Objetivo**: Apresentar estratégias para reduzir vieses do judge.
**Conteúdo**:
- **Rubrica clara**: critérios explícitos, não "avalie a qualidade"
- **Exemplos**: few-shot com casos calibrados por humano
- **Múltiplos judges**: 3+ modelos, média ou votação
- **Calibração**: comparar judge com humano em subconjunto
- **Swap de posição**: rodar A vs B e B vs A, média dos resultados
- **Cross-model**: usar modelo diferente do agente como judge

**Diagrama**: Checklist de mitigações
**Animação**: Itens aparecem com check verde
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Cada viés tem mitigação. Positional bias → swap de posição (rode A vs B e B vs A, tire média). Sycophancy → rubrica explícita sem sugerir resposta. Verbosity → rubrica que penaliza verbosidade desnecessária. Self-preference → cross-model (judge diferente do agente). Knowledge bias → forneça contexto necessário no prompt do judge. Acima de tudo: calibre com humano. Compare judge vs humano em 50 casos. Se concordância < 80%, ajuste a rubrica.
💡 ANALOGIA: É como treinar um corretor. Você não entrega a rubrica e vai embora — você calibra, mostra exemplos, corrige vieses.
⚠️ ERROS COMUNS: Alunos não calibram o judge. Sem calibração, você não sabe se o judge está certo.
➡️ TRANSIÇÃO: "Vamos para a segunda técnica: golden cases."

---

### Slide 33 — Golden Cases: O Que São

**Título**: Golden Cases
**Objetivo**: Introduzir o conceito de casos de teste para agentes.
**Conteúdo**:
- **Golden case** = par (input, critério de sucesso)
- **Input**: pergunta/tarefa para o agente
- **Critério**: como saber se a resposta está correta
  - Exato: string match, regex, JSON schema
  - Subjetivo: rubrica para LLM-as-judge
  - Funcional: tool foi chamada? ação foi executada?
- **Conjunto crescente**: cada bug encontrado vira golden case

**Diagrama**: Cartão de golden case com campos
**Animação**: Campos aparecem um a um
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Golden cases são os testes unitários do mundo de agentes. Cada caso é um par: input (pergunta/tarefa) e critério de sucesso (como saber se acertou). O critério pode ser exato (string match, regex), subjetivo (rubrica para LLM-as-judge), ou funcional (a tool certa foi chamada?). A regra de ouro: todo bug que você encontra vira um novo golden case. Assim você garante que nunca mais regredirá nele.
💡 ANALOGIA: É como teste de regressão em software tradicional. Cada bug corrigido vira teste. Diferença: em agentes, o "acertou" é mais complexo (pode ser subjetivo).
⚠️ ERROS COMUNS: Alunos criam golden cases sem critério mensurável. "A resposta deve ser boa" não é critério. Use critério operacionalizável.
➡️ TRANSIÇÃO: "Vamos ver um golden case concreto."

---

### Slide 34 — Escrevendo um Golden Case

**Título**: Escrevendo um Golden Case
**Objetivo**: Mostrar um golden case concreto em código.
**Conteúdo**:
- Estrutura: id, input, expected_behavior, eval_fn, category
- **Exemplo objetivo**:
  - id: `GC-042`
  - input: "Qual a capital da França?"
  - eval_fn: `assert "Paris" in response`
  - category: "factual"
- **Exemplo subjetivo**:
  - input: "Resuma este artigo em 3 pontos"
  - eval_fn: LLM-as-judge com rubrica "3 pontos, fiel ao original"

**Diagrama**: Code block com exemplo
**Animação**: Campos do golden case aparecem
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Estrutura simples. Cada golden case tem: id (rastreabilidade), input (o que vai para o agente), expected_behavior (descrição humana), eval_fn (função que retorna True/False), category (para agrupar). Para casos objetivos (factual), eval_fn é assertion direta. Para subjetivos, eval_fn chama LLM-as-judge com rubrica. O exemplo "Qual a capital da França?" — assertion de string. O exemplo "Resuma em 3 pontos" — LLM-as-judge checa se são 3 pontos e se fiéis ao original.
💡 ANALOGIA: É como um teste unitário. `assert soma(2,2) == 4`. Em agentes, a asserção pode ser mais complexa, mas o princípio é o mesmo.
⚠️ ERROS COMUNS: Alunos não versionam golden cases. Use Git — casos são código.
➡️ TRANSIÇÃO: "Casos isolados viram conjunto de regressão."

---

### Slide 35 — Conjuntos de Regressão

**Título**: Conjuntos de Regressão
**Objetivo**: Explicar como golden cases formam um conjunto de regressão.
**Conteúdo**:
- **Conjunto de regressão**: N golden cases que rodam a cada mudança
- Toda mudança de prompt, tool, ou modelo roda o conjunto
- Se score cai: deploy bloqueado (CI gate)
- **Crescimento**: 10 → 100 → 1000+ casos ao longo de meses
- **Categorização**: factual, multi-step, tool-use, edge-case, error-handling
- **Manutenção**: remover casos obsoletos, adicionar casos de bug

**Diagrama**: Pipeline — mudança → roda regressão → score → gate
**Animação**: Pipeline flui
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Um conjunto de regressão é o ativo mais valioso do seu projeto de agente. Comece com 10 casos. Cada bug que aparece em produção vira um caso novo. Em 6 meses, você tem 200-1000. Categorize: factual (verificação direta), multi-step (cadeia de raciocínio), tool-use (a tool certa foi chamada), edge-case (limites), error-handling (recuperação de falha). Categorização permite diagnosticar onde o agente está falhando.
💡 ANALOGIA: É como uma coleção de testes de uma aplicação madura. Começa com 10 testes, cresce para milhares. Cada bug corrigido adiciona um teste.
⚠️ ERROS COMUNS: Alunos criam conjunto e nunca atualizam. Conjunto obsoleto é inútil.
➡️ TRANSIÇÃO: "Vamos definir as métricas que o conjunto mede."

---

### Slide 36 — Métricas de Tarefa

**Título**: Métricas de Tarefa
**Objetivo**: Definir métricas que medem o resultado final.
**Conteúdo**:

| Métrica | Definição |
|---|---|
| Success rate | % de casos que passaram no critério |
| Partial credit | Não é tudo ou nada (0.7 se 7 de 10 sub-tarefas corretas) |
| Custo por execução | tokens × preço |
| Latência P50/P95 | tempo total da tarefa |
| Score oficial | ex: SWE-bench usa % resolved |

**Diagrama**: Tabela de métricas com fórmulas
**Animação**: Linhas aparecem uma a uma
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Métricas de tarefa medem o resultado final. Success rate é a mais óbvia — % de casos que passaram. Partial credit é sofisticado: se o agente acerta 7 de 10 sub-tarefas, score 0.7 em vez de 0. Custo e latência já cobrimos. Em benchmarks, há score oficial: SWE-bench usa % de issues resolvidas (testes passam). Importante: reporte todas — não só success rate. Um agente com 90% de success rate mas latência de 60s é inutilizável.
⚠️ ERROS COMUNS: Alunos só reportam success rate. Sem custo e latência, a métrica é incompleta.
➡️ TRANSIÇÃO: "Mas resultado não é tudo. Como o agente chegou lá também importa."

---

### Slide 37 — Métricas de Processo

**Título**: Métricas de Processo
**Objetivo**: Definir métricas que medem como o agente chegou ao resultado.
**Conteúdo**:
- **Número de steps**: quantas iterações do loop ReAct
- **Loops detectados**: agente repetiu a mesma action?
- **Tool misuse rate**: % de tool calls que falharam ou foram inúteis
- **Token efficiency**: tokens usados / tokens necessários
- **Recovery rate**: % de vezes que agente se recuperou de erro
- **Por que importa**: processo explica sucesso ou fracasso

**Diagrama**: Dashboard de processo
**Animação**: Métricas aparecem em grid
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Métricas de tarefa dizem O QUÊ. Métricas de processo dizem COMO. Número de steps: agente fazendo 15 steps quando 3 bastavam é ineficiente. Loops detectados: agente repetindo action é bug. Tool misuse: % de tool calls que falharam — alta indica ACI ruim. Token efficiency: tokens usados / tokens necessários — baixa indica prompt inchado. Recovery rate: agente se recuperou de erro? Essas métricas explicam POR QUE o agente falhou — e direcionam onde corrigir.
💡 ANALOGIA: Métricas de tarefa é o tempo final da maratona. Métricas de processo é o ritmo, cadência, onde você tropeçou. Para melhorar, você precisa das duas.
➡️ TRANSIÇÃO: "Com métricas definidas, vamos comparar versões."

---

### Slide 38 — A/B Testing de Prompts e Tools

**Título**: A/B Testing de Prompts e Tools
**Objetivo**: Apresentar experimentação controlada para agentes.
**Conteúdo**:
- **A/B test**: versão A (atual) vs versão B (nova) no mesmo conjunto
- **Variáveis**: prompt, tool description, modelo, temperatura, max_steps
- **Uma variável por vez** (ou design de experimentos)
- **Métricas**: success rate, custo, latência, satisfação
- **Significância**: N grande o suficiente (mínimo 30 casos por versão)
- **Pergunta**: *Você mudaria o prompt sem A/B test?*

**Diagrama**: Duas versões lado a lado, resultados comparados
**Animação**: Versões aparecem, resultados comparam
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A/B test em agentes é igual a A/B test em produto. Você tem versão A (atual) e versão B (nova). Roda ambas no mesmo conjunto de casos. Compara métricas. Regra de ouro: mude uma variável por vez (prompt OU tool OU modelo, não todos juntos). Significância estatística: mínimo 30 casos por versão, idealmente 100+. Abaixo disso, diferença pode ser ruído.
💡 ANALOGIA: É como teste A/B de produto. Você não muda botão, cor e texto ao mesmo tempo — não sabe qual mudou o que.
⚠️ ERROS COMUNS: Alunos mudam 3 coisas e atribuem diferença a uma. Mude uma variável por vez.
➡️ TRANSIÇÃO: "Vamos ver como tudo isso se integra num pipeline de CI."

---

### Slide 39 — Pipeline de Eval com CI

**Título**: Pipeline de Eval com CI
**Objetivo**: Mostrar como eval se integra ao pipeline de deploy.
**Conteúdo**:
- Mudança (prompt/tool/modelo) → CI roda eval
- CI executa: golden cases + subconjunto de benchmark
- LLM-as-judge avalia resultados
- Compara com baseline: houve regressão?
- Sim → bloquear deploy; Não → permitir deploy
- Pipeline automatizado, não manual

**Diagrama**: `12-Diagrams/ETHAGT12/eval-pipeline.mmd`
**Animação**: Fluxo percorrido step-by-step
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esse é o diagrama mais importante da aula. Toda mudança dispara o pipeline de CI. CI roda golden cases (seu conjunto) + subconjunto de benchmark (representatividade). LLM-as-judge avalia. Compara com baseline. Se houve regressão > threshold, deploy bloqueado. Se não, deploy autorizado. Esse pipeline transforma "vibes-based development" em "evidence-based development". É a diferença entre chutar e saber.
💡 ANALOGIA: É como CI de software tradicional (testes automáticos bloqueiam merge). Em agentes, "testes" são evals.
⚠️ ERROS COMUNS: Alunos fazem eval manual antes do deploy. Sem CI gate, esquecem de rodar. Automatize sempre.
➡️ TRANSIÇÃO: "DEMO ao vivo!"

---

### Slide 40 — DEMO: Eval Automatizado

**Título**: DEMO — Eval Automatizado
**Objetivo**: Demo ao vivo — construir pipeline de eval com LLM-as-judge.
**Conteúdo**:
- Código do `05-Labs/ETHAGT12/Lab2-Eval-Automatizado`
- Agente com 10 golden cases
- Mudar prompt do agente
- Rodar eval: score cai de 85% para 72%
- Mostrar: quais casos regrediram? Por quê?
- LLM-as-judge com rubrica para casos subjetivos

**Diagrama**: Terminal + eval report side-by-side
**Animação**: Highlight da regressão detectada
**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vamos ao vivo. Tenho um agente com 10 golden cases. Score atual: 85%. Vou mudar o prompt (piorar de propósito) e rodar eval. Score cai para 72%. Vamos ver quais casos regrediram — o eval report mostra caso por caso, qual passou, qual falhou, e por quê (justificativa do judge). Isso é a mágica: em 30 segundos você sabe se a mudança piorou o agente e onde.
⚠️ ERROS COMUNS: Se API falhar, tenho screenshot do eval report gravado.
➡️ TRANSIÇÃO: "Pergunta da demo — discussão aberta."

---

### Slide 41 — Pergunta da DEMO

**Título**: Pergunta da DEMO
**Objetivo**: Engajar com pergunta sobre regressão.
**Conteúdo**:
- "A regressão é real ou o judge está errado?"
- "Como distinguir bug do agente de viés do judge?"
- "O que fazer: reverter o prompt ou corrigir os casos?"
- Discussão aberta (2 min)

**Diagrama**: Caixa de discussão
**Animação**: Perguntas aparecem
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Essa é a pergunta difícil. Quando o eval cai, pode ser: (1) regressão real — o agente piorou; (2) viés do judge — o judge está julgando errado; (3) casos errados — o critério está mal definido. Como distinguir? Olhe caso por caso. Se os casos que falharam fazem sentido (realmente pioraram), é regressão. Se não fazem sentido (judge julgou errado), é viés. Se o critério era ambíguo, é problema de caso. Sempre tenha humano no loop para investigar.
❓ PERGUNTA PARA A TURMA: Pedir 2-3 opiniões. Anotar no quadro.
➡️ TRANSIÇÃO: "Vamos praticar escrevendo golden cases."

---

### Slide 42 — Exercício: Escrevendo um Golden Case

**Título**: Exercício — Escrevendo um Golden Case
**Objetivo**: Praticar a escrita de casos de teste para agentes.
**Conteúdo**:
- **Cenário**: agente de reserva de voo
- Em duplas: escrever 2 golden cases com critério mensurável
  - Um caso factual (ex: "voo direto encontrado")
  - Um caso subjetivo (ex: "resposta clara e útil")
- 3 min escrita, 2 min compartilhar

**Diagrama**: Template de golden case para preencher
**Animação**: Template aparece
**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Em duplas, 3 min. Cenário: agente de reserva de voo. Escrevam 2 golden cases. Um factual (ex: input "reserve um voo direto SP-Rio amanhã" → critério: assertion que a resposta menciona voo direto). Um subjetivo (ex: input "quais opções de viagem para o RJ?" → critério: rubrica para LLM-as-judge avaliar clareza e utilidade). Importante: o critério deve ser operacionalizável — não "resposta boa".
❓ PERGUNTA PARA A TURMA: Pedir 2 duplas para compartilhar. Validar critérios.
⚠️ ERROS COMUNS: Alunos escrevem critérios vagos. "Resposta útil" não é critério. "Menciona preço e horário" é.
➡️ TRANSIÇÃO: "Vamos quebrar um mito."

---

### Slide 43 — V/F: "LLM-as-Judge É Sempre Confiável"

**Título**: V/F — LLM-as-Judge É Sempre Confiável
**Objetivo**: Quebrar o mito da confiabilidade automática do judge.
**Conteúdo**:
- Verdadeiro ou Falso: "LLM-as-judge é sempre confiável"
- **Resposta**: Falso
- LLM-as-judge tem vieses (positional, sycophancy, verbosity, self-preference)
- Mitigações necessárias: rubrica, calibração, múltiplos judges
- Sem calibração com humano, judge pode estar sistematicamente errado

**Diagrama**: Card V/F com explicação
**Animação**: "Falso" aparece em vermelho
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Falso. LLM-as-judge é ferramenta poderosa mas NÃO é always-right. Tem 5 vieses que vimos (positional, sycophancy, verbosity, self-preference, knowledge). Sem mitigação (rubrica clara, calibração com humano, múltiplos judges, cross-model), o judge pode estar sistematicamente errado — e você nem sabe. Regra: calibre sempre com humano em subconjunto. Se concordância < 80%, ajuste.
➡️ TRANSIÇÃO: "Intervalo / bloco 2 começa com benchmarks."
