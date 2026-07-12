# ETHAGT03 — Slides Detalhados + Notas do Professor (Parte 1: Slides 1-32)

> Universidade Etho · Especialização em Programação Agêntica
> Cada slide contém: título, objetivo, conteúdo, notas do professor, diagrama, animação, imagem, tempo.

---

## SEÇÃO A — Abertura (Slides 1-5 · 6 min)

---

### Slide 1 — Capa

**Título**: ETHAGT03 — Padrões de Workflow Agêntico
**Objetivo**: Identificar a aula, o professor e o contexto dentro da especialização.
**Conteúdo**:
- ETHAGT03 — Padrões de Workflow Agêntico
- Os 5 padrões canônicos da Anthropic + composições
- Universidade Etho · Especialização em Programação Agêntica
- Fase A — Fundamentos Agênticos · 30 h
- Professor · Data

**Diagrama**: Logo Etho (canto sup. esquerdo) + imagem de fundo abstrata (fluxos e conexões)
**Animação**: Fade in do título (300ms)
**Imagem**: Fundo `etho-dark` (#0F1E2D) com pattern sutil de nós e arestas representando workflows
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Bem-vindos à terceira aula da Especialização. Na ETHAGT01 estabelecemos o bloco fundamental (Augmented LLM) e a distinção workflow vs agente. Hoje vamos aprofundar o lado workflow — os 5 padrões canônicos da Anthropic. Estes padrões são a caixa de ferramentas que separa quem "faz agentes" de quem projeta sistemas agênticos previsíveis.
💡 ANALOGIA: É como um arquiteto que conhece 5 tipologias de edifício (casa, prédio, ponte, túnel, viaduto). Não dá para construir tudo com a mesma estrutura. Cada padrão resolve uma classe de problema.
❓ PERGUNTA PARA A TURMA: "Quantos de vocês já usaram algum workflow estruturado em produção?" (levantar mãos — calibrar nível)
⚠️ ERROS COMUNS: Alunos chegam achando que workflow é "menos avançado" que agente. Redirecionar: workflow é escolha deliberada por previsibilidade.
➡️ TRANSIÇÃO: "Vamos começar definindo o que vocês vão conseguir fazer ao final desta aula."

---

### Slide 2 — Objetivos do Módulo

**Título**: Objetivos do Módulo
**Objetivo**: Deixar claro o que o aluno deve conseguir FAZER ao final da aula.
**Conteúdo**:
- **Objetivo geral**: Dominar os 5 padrões canônicos de workflow de Anthropic e suas composições
- **Objetivos específicos**:
  1. Implementar os 5 workflows (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer)
  2. Identificar gates programáticos e onde inseri-los
  3. Combinar workflows em pipelines complexos
  4. Justificar workflow vs agente autônomo em cenário real
  5. Medir trade-offs de custo/latência/qualidade entre abordagens

**Diagrama**: 5 ícones representando cada objetivo (cadeia, bifurcação, paralelo, orquestra, loop)
**Animação**: Objetivos aparecem um a um (on click)
**Imagem**: Ícones minimalistas em `etho-accent` (#E85D2F)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Cada objetivo é mensurável. Não é "entender" — é "implementar", "identificar", "combinar", "justificar", "medir". O objetivo #4 é o mais estratégico: a capacidade de JUSTIFICAR a escolha é o que diferencia um sênior. Em produção, a pergunta não é "qual workflow é melhor" mas "qual é mais adequado para ESTE problema com ESTAS restrições".
💡 ANALOGIA: É como um checklist de pré-voo com 5 instrumentos. O piloto não diz "entendo aviões" — ele verifica cada instrumento. Hoje, nosso checklist são estes 5 objetivos.
❓ PERGUNTA PARA A TURMA: "Qual desses objetivos vocês acham mais desafiador?" (deixar responder — costuma ser #4 ou #5)
⚠️ ERROS COMUNS: Alunos confundem "conhecer os 5 padrões" com "saber escolher entre eles". O objetivo #4 é o que custa anos de experiência.
➡️ TRANSIÇÃO: "Vamos ver onde esta aula se conecta com o Framework Etho de competências."

---

### Slide 3 — Competências Desenvolvidas

**Título**: Competências Desenvolvidas
**Objetivo**: Conectar a aula ao Framework Etho de competências.
**Conteúdo**:

| Competência | Nível ao final | Próximo nível em |
|---|---|---|
| C1 Programação Agêntica | **I** (Intermediário) | ETHAGT04-16 |
| C2 Multi-Agent Systems | **B** (Básico) | ETHAGT09 |
| C3 MCP & Tool Use | **B** (Básico) | ETHAGT02, ETHAGT08 |
| C5 AgentOps & Avaliação | **B** (Básico) | ETHAGT12 |

**Diagrama**: Radar chart com 4 eixos mostrando nível B/I
**Animação**: Radar aparece com wipe (left-to-right, 500ms)
**Imagem**: Badge visual por competência (círculos coloridos)
**Tempo**: 1 min

**Rodape**: AgentOps = Agent Operations — operacao e monitoramento de agentes em producao  ·  MCP = Model Context Protocol — Protocolo de Contexto de Modelo

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Este módulo consolida C1 em Intermediário — você consegue não apenas construir um agente, mas projetar a arquitetura de workflow que melhor se ajusta ao problema. C2 (Multi-Agent) começa em Básico porque orchestrator-workers é proto-multi-agente. C3 aparece porque routing e tools especializados são centrais. C5 porque avaliar classificadores e convergência de loops é AgentOps na prática.
💡 ANALOGIA: É como aprender a dirigir. ETHAGT01 foi sair do estacionamento. Hoje você dirige na cidade com trânsito (Intermediário em C1). Rodovia à noite (Avançado) vem em ETHAGT04.
⚠️ ERROS COMUNS: Alunos acham que "Básico" significa "superficial". Não — significa que é a fundação. Sem C5 Básico, você não consegue medir se o router funciona.
➡️ TRANSIÇÃO: "Vamos ver como esta aula está estruturada para entregar essas competências."

---

### Slide 4 — Agenda

**Título**: Agenda da Aula
**Objetivo**: Mostrar o roteiro da aula com tempos estimados.
**Conteúdo**:
- **Bloco 1 (45 min)**:
  - Abertura (6 min) — objetivos, motivação
  - Por Que Workflows (7 min) — princípio, 5 padrões
  - Prompt Chaining (8 min) — estrutura, gates, código
  - Routing (9 min) — classificação, modelos, código
  - Parallelization (15 min) — sectioning, voting, DEMO
  - Intervalo (5 min)
- **Bloco 2 (45 min)**:
  - Orchestrator-Workers (10 min) — delegação dinâmica
  - Evaluator-Optimizer (10 min) — loop, critérios, convergência
  - Composições e Limites (8 min) — composição, trade-offs
  - Fechamento (17 min) — caso, resumo, quiz, projeto, Q&A

**Diagrama**: Timeline horizontal com 9 seções coloridas
**Animação**: Timeline cresce da esquerda para direita (500ms)
**Imagem**: Ícones de relógio por seção
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A aula tem dois blocos. O primeiro cobre a fundamentação e os 3 primeiros padrões. O segundo cobre os 2 padrões mais complexos, composições e fechamento. Há um intervalo de 5 min entre os blocos. A DEMO de latência (Slide 31) é o ponto alto do Bloco 1.
💡 ANALOGIA: É como um menu degustação. Cada padrão é um prato. Provamos os 5, mas a combinação (composição) é o prato final.
⚠️ ERROS COMUNS: Alunos chegam atrasados e perdem a motivação (Slide 5), que define o tom de toda a aula.
➡️ TRANSIÇÃO: "Vamos começar pelo porquê. Por que workflows antes de agentes?"

---

### Slide 5 — Motivação: Comece Simples

**Título**: Comece Simples
**Objetivo**: Criar tensão cognitiva — times pulam para agente autônomo e colhem complexidade desnecessária.
**Conteúdo**:
- **Problema**: time usa agente autônomo onde um `if` bastava
- **Exemplo**: chatbot de suporte com 3 etapas fixas (classificar → buscar → responder) — agente livre é overkill
- **Princípio de Anthropic**: comece simples, só aumente complexidade com evidência
- **Custo de complexidade prematura**:
  - Debugging difícil (caminho não determinístico)
  - Custo imprevisível (nº de chamadas varia)
  - Latência alta (loops extras)
- **Pergunta**: *Quantos de vocês já viram um projeto que usou agente onde um if bastava?*

**Diagrama**: Split — esquerda: agente caótico (setas em todas as direções) | direita: workflow estruturado (fluxo linear com checkpoints)
**Animação**: Split — lado esquerdo (caos) aparece primeiro, depois lado direito (ordem)
**Imagem**: Ícone de caos (esquerda) vs fluxograma ordenado (direita)
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O erro mais caro da indústria de IA hoje é a complexidade prematura. Times ouvem "agente" e imediatamente implementam um sistema autônomo onde um workflow de 3 passos bastava. Resultado: custo 10x maior, bugs impossíveis de reproduzir, latência imprevisível. A Anthropic é categórica: comece simples, só aumente com evidência de que o anterior é insuficiente.
💡 ANALOGIA: É como construir uma casa. Você não começa pela piscina e pelo jardim. Começa pela fundação. Se a fundação (workflow simples) resolve, pare. Se não resolve, adicione complexidade justificada.
❓ PERGUNTA PARA A TURMA: "Quantos já viram projeto que usou agente onde um if bastava?" (levantar mãos — a maioria vai levantar)
⚠️ ERROS COMUNS: Alunos acham que "workflow é iniciante". Falso. Workflows são escolha de engenharia por previsibilidade. Agentes são para quando flexibilidade supera previsibilidade.
➡️ TRANSIÇÃO: "Esse princípio é de Anthropic. Vamos entender a hierarquia completa."

---

## SEÇÃO B — Por Que Workflows Antes de Agentes (Slides 6-10 · 7 min)

---

### Slide 6 — [SEÇÃO] Por Que Workflows Antes de Agentes

**Título**: 1 — Por Que Workflows Antes de Agentes
**Objetivo**: Transição visual para o bloco de fundamentos.
**Conteúdo**: Número "1" grande + "Por Que Workflows Antes de Agentes"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "1" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Início do bloco de fundamentos. Vamos responder: por que workflows primeiro? Qual é a hierarquia de complexidade? E quais são os 5 padrões que vamos aprofundar?
➡️ TRANSIÇÃO: "Primeiro: o princípio norteador."

---

### Slide 7 — O Princípio de Anthropic: Comece Simples

**Título**: O Princípio de Anthropic: Comece Simples
**Objetivo**: Fixar o princípio norteador do módulo.
**Conteúdo**:
- "Comece simples, só aumente complexidade com evidência" — Anthropic
- **Níveis de escalada**:
  - Nível 0: Single LLM call + retrieval + examples
  - Nível 1: Workflow simples (prompt chaining)
  - Nível 2: Workflow complexo (orchestrator-workers)
  - Nível 3: Agente autônomo
  - Nível 4: Multi-agente
- **Regra**: só suba um nível com evidência de que o anterior é insuficiente

**Diagrama**: Pirâmide de níveis de complexidade (base larga = Nível 0, topo = Nível 4)
**Animação**: Níveis aparecem de baixo para cima (on click)
**Imagem**: Pirâmide com 5 faixas coloridas, "90% dos casos" na base
**Tempo**: 2 min

**Rodape**: LLM = Large Language Model — Modelo de Linguagem de Grande Escala

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A Anthropic propõe uma hierarquia de complexidade. A base (Nível 0) — uma chamada LLM com retrieval e examples — resolve 90% dos casos. Sim, 90%. A maioria das aplicações não precisa de workflow nem de agente. Quando isso é insuficiente, você escala para workflow simples (prompt chaining). Depois workflow complexo. Só depois agente. E multi-agente é raro — último recurso. A regra é: só suba um nível quando tem EVIDÊNCIA (métricas, testes, custos) de que o anterior é insuficiente.
💡 ANALOGIA: É como uma escada de atendimento médico. Começa com auto-cuidado (Nível 0). Se não resolve, clínico geral (Nível 1). Depois especialista (Nível 2). Depois hospital (Nível 3). Depois UTI (Nível 4). Você não manda todo mundo para a UTI.
❓ PERGUNTA PARA A TURMA: "Em que nível está o sistema de vocês hoje?" (deixar pensar — a maioria está em Nível 0 ou 1 achando que está em Nível 3)
⚠️ ERROS COMUNS: Alunos pulam para Nível 3 (agente) sem tentar Nível 1. Isso é engenharia de "resume-driven" — não de qualidade.
➡️ TRANSIÇÃO: "Vamos recapitular a distinção central, que vem de ETHAGT01."

---

### Slide 8 — Workflows vs Agentes (Recap de ETHAGT01)

**Título**: Workflows vs Agentes (Recap)
**Objetivo**: Reativar o conhecimento de ETHAGT01 e preparar para os 5 padrões.
**Conteúdo**:
- **Workflows**: LLMs e tools orquestrados via código predefinido → **previsibilidade**
- **Agentes**: LLM direciona seu próprio processo e tool usage → **flexibilidade**
- Workflows = controle do **desenvolvedor**; Agentes = controle do **modelo**
- Este módulo: foco total em workflows (ETHAGT04 aprofunda agentes)

**Diagrama**: `12-Diagrams/ETHAGT01/workflow-vs-agent.mmd` (referência)
**Animação**: Comparação lado a lado
**Imagem**: Trem (workflow — trilhos) vs táxi (agente — motorista decide)
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Recap rápido da distinção canônica de Anthropic. Workflow = código predefinido orquestra LLMs e tools. Agente = LLM orquestra a si mesmo. A diferença não é técnica — é de CONTROLE. Em workflow, o desenvolvedor controla o caminho. Em agente, o modelo controla o caminho. Previsibilidade vs flexibilidade é o trade-off central.
💡 ANALOGIA: Trem (workflow — trilhos predefinidos, horário fixo, previsível) vs táxi (agente — motorista decide o caminho, flexível, mas imprevisível). Você escolhe trem quando quer chegar na hora certa. Táxi quando o destino muda.
⚠️ ERROS COMUNS: Alunos acham que workflow é "menos poderoso". É diferente. É mais PREVISÍVEL. Em produção, previsibilidade é poder.
➡️ TRANSIÇÃO: "Dentro do mundo dos workflows, Anthropic catalogou 5 padrões. Vamos conhecê-los."

---

### Slide 9 — Os 5 Workflows Canônicos (Panorama)

**Título**: Os 5 Workflows Canônicos
**Objetivo**: Apresentar os 5 padrões que serão aprofundados na aula.
**Conteúdo**:
1. **Prompt Chaining** — sequência de steps com gates
2. **Routing** — classificação + dispatch
3. **Parallelization** — sectioning / voting
4. **Orchestrator-Workers** — delegação dinâmica
5. **Evaluator-Optimizer** — loop de refinamento
- Fonte: Anthropic, *Building Effective Agents* (2024)

**Diagrama**: 5 mini-diagramas em grid 2x3 (com 1 célula de legenda)
**Animação**: Cada workflow aparece com click
**Imagem**: Mini-flowcharts estilizados em `etho-info` (#2980B9)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A Anthropic, em "Building Effective Agents", catalogou 5 padrões de workflow que cobrem a maioria dos casos de uso em produção. Cada padrão resolve uma classe de problema: prompt chaining para tarefas lineares com checkpoints; routing para categorias; parallelization para independência ou robustez; orchestrator-workers para subtarefas dinâmicas; evaluator-optimizer para refinamento iterativo. Vamos aprofundar cada um com código.
💡 ANALOGIA: É como 5 ferramentas em uma caixa. Martelo (prompt chaining), chave-inglesa (routing), alicate (parallelization), furadeira (orchestrator-workers), lixadeira (evaluator-optimizer). Cada uma serve para um parafuso diferente.
❓ PERGUNTA PARA A TURMA: "Qual desses 5 vocês já usaram em produção?" (contar mãos — geralmente routing e prompt chaining)
⚠️ ERROS COMUNS: Alunos querem usar orchestrator-workers para tudo porque "parece avançado". É overkill para tarefas com passos fixos.
➡️ TRANSIÇÃO: "Mas como escolher? Vamos ver o panorama de quando cada um brilha."

---

### Slide 10 — Mapa: Quando Cada Padrão Brilha

**Título**: Quando Cada Padrão Brilha
**Objetivo**: Dar um panorama rápido de quando usar cada padrão.
**Conteúdo**:

| Padrão | Quando usar | Quando evitar |
|---|---|---|
| Prompt Chaining | Tarefa linear com checkpoints de qualidade | Tarefas simples (uma chamada basta) |
| Routing | Categorias discretas com tratamento especializado | Continuum sem fronteiras claras |
| Parallelization | Subtarefas independentes ou votação para robustez | Subtarefas com dependências |
| Orchestrator-Workers | Subtarefas dinâmicas não conhecidas a priori | Subtarefas fixas e conhecidas |
| Evaluator-Optimizer | Feedback articulável e iteração melhora resultado | Evaluator não é melhor que generator |

**Diagrama**: Tabela 5×3 colorida por intensidade
**Animação**: Linhas aparecem uma a uma (on click)
**Imagem**: Tabela com ícones por padrão
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Este é o mapa mental da aula. Guardem esta tabela — ela é o resumo de tudo. A coluna "quando evitar" é tão importante quanto "quando usar". Cada padrão tem uma armadilha. Prompt chaining: overkill para tarefas simples. Routing: não funciona quando categorias se sobrepõem. Parallelization: dependências ocultas. Orchestrator-workers: custo desnecessário se subtarefas são fixas. Evaluator-optimizer: diverge se evaluator é fraco.
💡 ANALOGIA: É como um guia de restaurantes por ocasião. Encontro rápido → lanchonete (routing). Jantar romântico → restaurante elegante (prompt chaining). Comemoração em grupo → rodízio (parallelization). Evento surpresa → buffet personalizado (orchestrator-workers). Receita de família → cozinhar e ajustar até ficar perfeito (evaluator-optimizer).
⚠️ ERROS COMUNS: Alunos decoram "quando usar" mas esquecem "quando evitar". A armadilha é usar o padrão certo no problema errado.
➡️ TRANSIÇÃO: "Vamos ao primeiro padrão: prompt chaining."

---

## SEÇÃO C — Prompt Chaining (Slides 11-16 · 8 min)

---

### Slide 11 — [SEÇÃO] Prompt Chaining

**Título**: 2 — Prompt Chaining: Sequência com Gates
**Objetivo**: Transição visual para o primeiro padrão canônico.
**Conteúdo**: Número "2" grande + "Prompt Chaining: Sequência com Gates"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "2" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Início do primeiro padrão. Prompt chaining é o workflow mais simples depois da chamada única. É uma cadeia de chamadas LLM com gates programáticos entre elas.
➡️ TRANSIÇÃO: "Vamos ver a estrutura fundamental."

---

### Slide 12 — Estrutura: LLM → Gate → LLM → …

**Título**: Estrutura: LLM → Gate → LLM → …
**Objetivo**: Apresentar a estrutura fundamental do prompt chaining.
**Conteúdo**:
- Cadeia de chamadas LLM intercaladas com **gates programáticos**
- **Gate** = código determinístico (não LLM) que decide se continua, roda de novo, ou para
- Cada step tem prompt especializado e contexto focado
- Saída de um step = entrada do próximo
- Gates capturam erros cedo (menos retrabalho downstream)

**Diagrama**: `12-Diagrams/ETHAGT03/prompt-chaining.mmd`
**Animação**: Step a step, gates destacados em cor diferente (`etho-warning`)
**Imagem**: Flowchart com caixas azuis (LLM) e amarelas (gates)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A estrutura é simples: LLM → gate → LLM → gate → LLM → saída. Cada LLM tem um prompt focado em UMA coisa. Os gates são código puro — if/else, regex, schema validation. Não são LLM. Isso é crucial: gates são determinísticos, LLMs não. A combinação de passos focados (qualidade) e gates (controle) é o que torna prompt chaining poderoso. Sem gates, é só uma cadeia de chamadas. Com gates, é um pipeline com checkpoints de qualidade.
💡 ANALOGIA: É como uma linha de montagem de uma fábrica. Cada estação faz uma coisa (LLM). Entre as estações há inspetores de qualidade (gates) que verificam se a peça está conforme antes de passar para a próxima estação.
❓ PERGUNTA PARA A TURMA: "Por que os gates são código e não LLM?" (Resposta: determinismo. Gate deve ser previsível.)
⚠️ ERROS COMUNS: Alunos fazem gates com LLM ("um modelo que valida a saída de outro"). Isso é evaluator-optimizer, não prompt chaining. Gate é código puro.
➡️ TRANSIÇÃO: "Mas onde colocar os gates? Vamos ver os tipos."

---

### Slide 13 — Onde Adicionar Gates

**Título**: Onde Adicionar Gates
**Objetivo**: Ensinar a identificar pontos de gate na cadeia.
**Conteúdo**:
- **Validação estrutural**: "a saída tem todos os campos obrigatórios?"
- **Classificação**: "a resposta é do tipo esperado?"
- **Formatação**: "está no formato JSON correto?"
- **Filtro de qualidade**: "passou no check de segurança?"
- Gates são código puro (if/else, regex, schema validation) — **não LLM**
- Gate falhou? → **retry** com feedback, ou **fallback**, ou **escalada**

**Diagrama**: Checklist de tipos de gate (4 ícones)
**Animação**: Cada tipo aparece com click
**Imagem**: Ícones de escudo, tag, JSON, e cadeado
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Existem 4 tipos principais de gate. Validação estrutural verifica campos obrigatórios (schema). Classificação verifica o tipo (ex.: se era uma resposta técnica ou emocional). Formatação verifica sintaxe (JSON válido). Filtro de qualidade verifica regras de negócio (sem PII, sem conteúdo tóxico). Quando um gate falha, você tem 3 opções: retry com feedback explicando o erro, fallback para um caminho seguro, ou escalada para humano. Gates baratos (regex) podem rodar sempre. Gates caros (classificação) só quando necessário.
💡 ANALOGIA: É como a alfândega. Há 4 tipos de conferência: documental (campos preenchidos), de tipo (é mercadoria declarada?), de formato (embalagem correta?), de segurança (sem itens proibidos?). Se algo falha, devolve, multa, ou encaminha para análise.
⚠️ ERROS COMUNS: Alunos colocam gates demais. Cada gate adiciona latência e complexidade. Regra: um gate só se o custo de NÃO ter é maior que o custo de ter.
➡️ TRANSIÇÃO: "Mas vale a pena a latência extra? Vamos ver o trade-off."

---

### Slide 14 — Trade-off: Latência por Accuracy

**Título**: Trade-off: Latência por Accuracy
**Objetivo**: Justificar quando o custo de latência serial vale a pena.
**Conteúdo**:
- Latência = **soma** de todos os steps (serial)
- Mas: cada step focado = melhor qualidade que uma chamada gigante
- Gates reduzem retrabalho downstream (capturam erro cedo)
- **Quando vale**: tarefas com critérios de qualidade verificáveis
- **Quando não vale**: tarefas simples onde uma chamada basta

**Diagrama**: Gráfico latência vs accuracy (curva de ganho marginal)
**Animação**: Curva cresce até platô (returns diminuem)
**Imagem**: Gráfico de linha com eixos "latência" e "accuracy"
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O trade-off central de prompt chaining é latência vs accuracy. Como é serial, latência soma. Mas cada step focado gera melhor qualidade que uma chamada monolítica. A questão é: o ganho de qualidade compensa a latência extra? A resposta depende do domínio. Em tradução técnica, sim (precisão importa). Em chatbot casual, não (latência importa mais). A curva tem retornos decrescentes: os primeiros gates dão muito ganho, os últimos pouco.
💡 ANALOGIA: É como revisar um texto. Uma passada pega 80% dos erros. Duas passadas pegam 95%. Três pegam 98%. A quarta passada mal agrega valor. O ponto ótimo é geralmente 2-3 gates.
⚠️ ERROS COMUNS: Alunos adicionam gates "por segurança" sem medir. Sem medição, você não sabe se o gate está ajudando ou só adicionando latência.
➡️ TRANSIÇÃO: "Vamos ver código concreto."

---

### Slide 15 — Exemplo + Código: Gerar → Revisar → Reescrever

**Título**: Código: Gerar → Revisar → Reescrever
**Objetivo**: Mostrar implementação concreta de prompt chaining.
**Conteúdo**:
- Domínio: geração de resposta a ticket de suporte
- Step 1: LLM gera rascunho
- Gate 1: tem todos os campos? (schema validation)
- Step 2: LLM revisa contra critérios
- Gate 2: score ≥ threshold?
- Step 3: LLM reescreve com feedback da revisão
- Snippet em Python: função `chain()` com gates

```python
def chain(ticket):
    draft = llm("Gere rascunho", ticket)
    if not validate_schema(draft, fields=["saudacao","corpo","fechamento"]):
        draft = llm("Corrija e inclua todos os campos", ticket)
    review = llm("Revise contra critérios", draft)
    if review["score"] < 0.8:
        return llm("Reescreva com feedback", draft, review["feedback"])
    return draft
```

**Diagrama**: Code block + fluxo lado a lado
**Animação**: Highlight de linhas chave (gates destacados)
**Imagem**: Screenshot do VS Code com syntax highlighting
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vejam a estrutura. Cada LLM tem um prompt focado. Entre eles, gates de código: validate_schema (validação estrutural) e score < threshold (filtro de qualidade). O gate falha? Retry com feedback (não com prompt genérico — feedback específico do que faltou). A saída do step 1 vira entrada do step 2. Esse é o padrão. Simples, mas poderoso.
💡 ANALOGIA: É como um escritor revisando um texto. Escreve (LLM 1). Verifica se tem introdução, corpo e conclusão (Gate 1). Editor revisa contra rubric (LLM 2). Se nota baixa, reescreve com as correções (Gate 2 + LLM 3).
⚠️ ERROS COMUNS: Alunos não incluem retry nos gates. Sem retry, um gate falho vira erro fatal. Com retry, o gate vira oportunidade de correção.
➡️ TRANSIÇÃO: "Vamos praticar a identificação de gates."

---

### Slide 16 — Exercício: Gate Útil em Tradução

**Título**: Exercício — Gate em Tradução
**Objetivo**: Praticar identificação de gates em outro domínio.
**Conteúdo**:
- Cenário: prompt chaining para tradução técnica (EN → PT-BR)
- Pergunta: *Descreva um gate programático útil entre o step de tradução e o step de revisão.*
- Dica: pense em verificação estrutural, não semântica
- Discussão em duplas (2 min)

**Diagrama**: Caixa de discussão (`etho-warning`)
**Animação**: Caixa aparece com fade
**Imagem**: Ícone de lápis e bandeiras (EN/PT)
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Deixem a turma pensar em duplas por 2 min. A pergunta é deliberadamente sobre verificação ESTRUTURAL, não semântica. Gates são código puro — não podem avaliar "a tradução está boa" (isso é evaluator). Mas podem verificar: o nº de parágrafos é o mesmo? Os termos técnicos do glossário foram preservados? Há termos entre chaves {como_variáveis} que não foram traduzidos? A contagem de tokens está dentro do limite?
💡 ANALOGIA: É como um inspetor de obra que verifica se a planta foi seguida (estrutura), não se a casa é bonita (semântica).
❓ PERGUNTA PARA A TURMA: "Compartilhem 2 respostas." (respostas esperadas: contagem de parágrafos, glossário, variáveis preservadas, contagem de tokens)
⚠️ ERROS COMUNS: Alunos propõe gates semânticos ("verificar se a tradução é fiel"). Isso não é gate, é evaluator. Gate é mecânico.
➡️ TRANSIÇÃO: "Vamos ao segundo padrão: routing."

---

## SEÇÃO D — Routing (Slides 17-23 · 9 min)

---

### Slide 17 — [SEÇÃO] Routing

**Título**: 3 — Routing: Classificação e Dispatch
**Objetivo**: Transição visual para o segundo padrão canônico.
**Conteúdo**: Número "3" grande + "Routing: Classificação e Dispatch"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "3" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Início do segundo padrão. Routing é sobre separação de concerns: classificar é mais barato que resolver. O router decide QUEM trata; o handler resolve.
➡️ TRANSIÇÃO: "Vamos entender o princípio."

---

### Slide 18 — Classificação como Etapa Separada

**Título**: Classificação como Etapa Separada
**Objetivo**: Explicar o princípio fundamental do routing.
**Conteúdo**:
- **Router** = LLM (ou código) que classifica a entrada em categorias
- Cada categoria tem seu próprio tratamento especializado
- **Separação de concerns**: classificar é mais barato que resolver
- Router pode ser modelo menor (Haiku) — classify é tarefa simples

**Diagrama**: Funil: input → router → N caminhos especializados
**Animação**: Funil preenche da esquerda
**Imagem**: Funil com 4 saídas coloridas
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A ideia central é separar classificação de resolução. Classificar um ticket (técnico, billing, geral) é mais barato que resolver qualquer um deles. Então você usa um modelo barato (Haiku) para classificar, e despacha para o handler certo. Cada handler tem prompt, tools e até modelo diferente. Isso é routing. O ganho é duplo: custo (modelo barato para classificar) e qualidade (handler especializado).
💡 ANALOGIA: É como a recepção de um hospital. A recepcionista (router) não trata ninguém — ela classifica (urgência, pediatria, ortopedia) e despacha para o especialista certo. Cada especialista tem ferramentas diferentes.
⚠️ ERROS COMUNS: Alunos tentam fazer um LLM resolver tudo sem classificar. Isso infla custo (modelo caro para caso simples) e reduz qualidade (prompt genérico para caso específico).
➡️ TRANSIÇÃO: "O routing pode ser por modelo, por prompt, ou por tools. Vamos ver."

---

### Slide 19 — Routing por Modelo

**Título**: Routing por Modelo
**Objetivo**: Mostrar routing por capacidade/custo do modelo.
**Conteúdo**:
- **Haiku** para tarefas fáceis (classificação, resumo simples) — barato e rápido
- **Sonnet** para tarefas difíceis (raciocínio, código complexo) — caro mas capaz
- Economia: 80% dos tickets são fáceis → Haiku → custo total cai
- Risco: classificação errada envia tarefa difícil para modelo fraco

**Diagrama**: `12-Diagrams/ETHAGT03/routing.mmd`
**Animação**: Input entra no router, seta se divide em Haiku/Sonnet
**Imagem**: Diagrama de routing com dois modelos
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A forma mais comum de routing é por modelo. O router classifica a dificuldade da tarefa. Tarefa fácil → Haiku (10x mais barato, 3x mais rápido). Tarefa difícil → Sonnet (mais capaz, mas caro). Em suporte ao cliente, 80% dos tickets são fáceis (FAQ, status de pedido). Se você manda tudo para Sonnet, está pagando 10x pelo que Haiku resolve. Se manda tudo para Haiku, os 20% difíceis viram respostas ruins. A economia real: 80% × Haiku + 20% × Sonnet é muito mais barato que 100% × Sonnet.
💡 ANALOGIA: É como um hospital. Casos leves (gripe, cortes pequenos) vão para o clínico geral (Haiku). Casos complexos (cirurgia) vão para o especialista (Sonnet). Mandar tudo para o cirurgião é desperdício. Mandar tudo para o clínico é negligência.
⚠️ ERROS COMUNS: Alunos confiam cegamente no router. Se o router erra, tarefa difícil vai para Haiku e o usuário recebe resposta ruim. Mitigação: quando incerto, despachar para o modelo forte.
➡️ TRANSIÇÃO: "Mas routing não é só por modelo. Pode ser por prompt e tools."

---

### Slide 20 — Routing por Prompt/Tools Especializados

**Título**: Routing por Prompt/Tools Especializados
**Objetivo**: Mostrar que routing não é só por modelo, mas por prompt e tools.
**Conteúdo**:
- Mesmo modelo, diferentes **system prompts** especializados
- Exemplo: ticket de billing → prompt com tools de fatura; ticket técnico → prompt com tools de docs
- Vantagem: cada path tem contexto focado (menos tokens, melhor qualidade)
- O router decide qual conjunto de tools/prompt carregar

**Diagrama**: Router → 3 paths com diferentes toolsets
**Animação**: Cada path acende conforme router decide
**Imagem**: 3 paths com ícones de toolsets diferentes
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Outra forma de routing é por prompt e tools. Mesmo modelo (ex.: Sonnet para todos), mas cada categoria carrega um system prompt diferente e um conjunto de tools diferente. Ticket de billing → tools de fatura e sistema de pagamento. Ticket técnico → tools de docs e diagnóstico. A vantagem é foco: menos tools no contexto = menos confusão para o modelo = melhor qualidade. O router decide qual "persona" ativar.
💡 ANALOGIA: É como um médico que tem várias especialidades mas ativa só a relevante. Não examina o paciente com todos os instrumentos da clínica — só com os da especialidade certa.
⚠️ ERROS COMUNS: Alunos carregam TODAS as tools no contexto sempre. Isso confunde o modelo. Regra: menos tools bem selecionadas > muitas tools genéricas.
➡️ TRANSIÇÃO: "Mas como saber se o router está funcionando?"

---

### Slide 21 — Avaliando a Qualidade do Classificador

**Título**: Avaliando a Qualidade do Classificador
**Objetivo**: Ensinar a medir se o router está funcionando.
**Conteúdo**:
- O router é um **classificador** → métricas de classificação
- **Matriz de confusão**: quais categorias confunde?
- **Precision/Recall** por categoria
- Erro mais caro: falso negativo (tarefa difícil → modelo fraco)
- Estratégia: quando incerto, enviar para path robusto (Sonnet)

**Diagrama**: Matriz de confusão 3×3 com exemplo (técnico/billing/geral)
**Animação**: Células da matriz preenchem com cores
**Imagem**: Matriz 3×3 com números de exemplo
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O router é, fundamentalmente, um classificador. E classificadores têm métricas: matriz de confusão, precision, recall, F1. A matriz de confusão mostra quais categorias confunde. Precision: dos que o router classificou como técnico, quantos eram mesmo técnicos? Recall: dos que eram técnicos, quantos o router pegou? O erro mais caro é o falso negativo em routing por modelo: tarefa difícil classificada como fácil vai para Haiku e vira resposta ruim. A mitigação é: quando o router está incerto (baixa confiança), despachar para o path robusto.
💡 ANALOGIA: É como triagem médica. Erro tipo I (mandar grave para casa) é pior que erro tipo II (manter leve no hospital). Em routing: errar difícil para fácil é pior que fácil para difícil.
⚠️ ERROS COMUNS: Alunos não medem o router. Acham que "funciona". Sem matriz de confusão, você não sabe quais categorias confundem.
➡️ TRANSIÇÃO: "Vamos ver código."

---

### Slide 22 — Código: Routing com Classifier

**Título**: Código: Routing com Classifier
**Objetivo**: Mostrar implementação concreta de routing.
**Conteúdo**:
- Função `route(input)` → classificação → dispatch
- Router: LLM com output estruturado (JSON schema com categoria)
- Switch/case para cada categoria → prompt + modelo + tools
- Fallback: categoria "unknown" → path robusto
- Snippet em Python

```python
def route(ticket):
    cat = router_llm(
        "Classifique: tecnico | billing | geral | unknown",
        ticket, response_format="json"
    )["categoria"]
    handlers = {
        "tecnico": lambda t: sonnet(PROMPT_TECNICO, t, tools=TOOLS_DOCS),
        "billing": lambda t: sonnet(PROMPT_BILLING, t, tools=TOOLS_FATURA),
        "geral":   lambda t: haiku(PROMPT_GERAL, t),
        "unknown": lambda t: sonnet(PROMPT_ROBUSTO, t, tools=ALL_TOOLS),
    }
    return handlers.get(cat, handlers["unknown"])(ticket)
```

**Diagrama**: Code block com fluxo
**Animação**: Highlight do dicionário de handlers
**Imagem**: Screenshot do VS Code
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O padrão é limpo. Router LLM classifica. Switch/case despacha. Cada handler tem prompt, modelo e tools próprios. O fallback "unknown" despacha para Sonnet com todas as tools — sempre melhor errar para o robusto. Vejam que o router usa response_format="json" — output estruturado evita parsing frágil.
💡 ANALOGIA: É como um sistema de PABX. A recepcionista virtual (router) direciona para o ramal certo. Se não sabe, manda para a recepção humana (fallback robusto).
⚠️ ERROS COMUNS: Alunos não implementam fallback. Sem fallback, categoria não prevista quebra o sistema.
➡️ TRANSIÇÃO: "Vamos discutir como avaliar isso."

---

### Slide 23 — Exercício: O Que Medir no Router?

**Título**: Exercício — Avaliando o Router
**Objetivo**: Engajar a turma com pergunta sobre avaliação do router.
**Conteúdo**:
- "Como saber se o roteador está errando? O que medir?"
- "Qual métrica é mais importante: precision ou recall? Depende do quê?"
- "Se o router envia 10% dos fáceis para o path difícil, isso é problema?"
- Discussão em duplas (2 min), 1 min compartilhar

**Diagrama**: Caixa de discussão (`etho-warning`)
**Animação**: Caixa aparece com fade
**Imagem**: Ícone de régua e balança
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Deixem a turma discutir em duplas. A pergunta 1 é sobre observabilidade: você precisa logs de classificação vs ground truth. A pergunta 2 é sobre trade-off: precision importa mais quando o path errado é caro (billing classificado como técnico gera custo); recall importa mais quando o path certo é crítico (não pode perder nenhum ticket urgente). A pergunta 3 é uma armadilha: 10% de falsos positivos (fácil para difícil) é aceitável — manda para Sonnet, custa mais mas resolve. Falsos negativos (difícil para fácil) é o problema real.
💡 ANALOGIA: É como triagem de aeroporto. Mandar passageiro comum para a revista detalhada (fácil→difícil) só atrasa. Mandar suspeito para o raio-x rápido (difícil→fácil) é perigoso.
❓ PERGUNTA PARA A TURMA: "Compartilhem 2 respostas." (resposta-chave: recall é mais importante que precision para tarefas difíceis)
⚠️ ERROS COMUNS: Alunos só medem accuracy global. Accuracy esconde vieses por categoria. Sempre olhar precision/recall por categoria.
➡️ TRANSIÇÃO: "Intervalo! Voltamos com parallelization."

---

## SEÇÃO E — Parallelization (Slides 24-32 · 15 min)

---

### Slide 24 — [SEÇÃO] Parallelization

**Título**: 4 — Parallelization: Sectioning e Voting
**Objetivo**: Transição visual para o terceiro padrão canônico.
**Conteúdo**: Número "4" grande + "Parallelization: Sectioning e Voting"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "4" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Início do terceiro padrão. Parallelization tem duas variantes: sectioning (dividir em subtarefas independentes) e voting (mesma tarefa N vezes para robustez). Vamos aprofundar ambas.
➡️ TRANSIÇÃO: "Primeiro: sectioning."

---

### Slide 25 — Sectioning: Subtarefas Independentes em Paralelo

**Título**: Sectioning: Subtarefas Independentes
**Objetivo**: Apresentar o padrão de dividir em subtarefas paralelas.
**Conteúdo**:
- Tarefa dividida em N subtarefas **independentes**
- Cada subtarefa roda em paralelo (chamadas LLM simultâneas)
- Resultados são agregados por um **reducer/sintetizador**
- Exemplo: revisar código → rodar linter + testes + typecheck em paralelo
- Ganho: latência = **max(subtasks)** vs **sum(subtasks)**

**Diagrama**: `12-Diagrams/ETHAGT03/parallelization.mmd` (lado sectioning)
**Animação**: Subtarefas disparam em paralelo, resultados convergem
**Imagem**: Fan-out/fan-in diagram
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Sectioning é dividir uma tarefa em partes independentes e rodá-las em paralelo. O ganho principal é latência: se você tem 3 subtarefas de 3s cada, serial = 9s, paralelo = 3s (max). Mas o ganho NÃO é custo — você paga as 3 chamadas de qualquer forma. O reducer agrega os resultados. O ponto crítico é a INDEPENDÊNCIA: as subtarefas não podem depender umas das outras. Se dependem, você precisa orchestrator-workers, não sectioning.
💡 ANALOGIA: É como um buffet. Em vez de uma pessoa servir tudo (serial), três pessoas servem pratos diferentes simultaneamente (paralelo). O tempo é o da pessoa mais lenta.
❓ PERGUNTA PARA A TURMA: "Por que paralelismo não reduz custo?" (Resposta: você paga todas as chamadas; só reduz latência)
⚠️ ERROS COMUNS: Alunos paralelizam subtarefas com dependência oculta. Ex.: "sumarizar documento" depende de "extrair seções" — não pode paralelizar.
➡️ TRANSIÇÃO: "A outra variante: voting."

---

### Slide 26 — Voting: Mesma Tarefa N Vezes

**Título**: Voting: Mesma Tarefa N Vezes
**Objetivo**: Apresentar o padrão de votação para robustez.
**Conteúdo**:
- Mesma tarefa executada N vezes (com temperatura/variação)
- Agregação por **maioria** (classificação) ou **seleção** (geração)
- Quando usar: classificação ambígua, geração de código crítico, decisões de segurança
- Custo: **N×** o custo base — mas com N modelos menores pode ser mais barato que 1 grande

**Diagrama**: `12-Diagrams/ETHAGT03/parallelization.mmd` (lado voting)
**Animação**: N tentativas disparam, agregador escolhe
**Imagem**: Diagrama voting com agregador (maioria/melhor)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Voting é executar a MESMA tarefa N vezes com variação (temperatura alta, prompts levemente diferentes) e agregar. A agregação pode ser por maioria (para classificação — ex.: 3 de 5 modelos disseram que é spam) ou por seleção (para geração — ex.: o melhor de 5 rascunhos). O ganho é robustez: reduz a variância do modelo. Mas NÃO resolve viés — se todos os 5 modelos têm o mesmo viés, a maioria reforça o erro. Voting é caro (N× custo) mas pode ser mais barato que 1 modelo grande: 3× Haiku pode ser mais barato que 1× Sonnet.
💡 ANALOGIA: É como pedir opinião a 3 médicos independentes. Se todos concordam, alta confiança. Se discordam, você investiga. Mas se todos têm o mesmo viés (ex.: trabalharam no mesmo hospital), a maioria não corrige.
⚠️ ERROS COMUNS: Alunos usam voting esperando corrigir viés. Voting corrige variância (aleatoriedade), não viés (erro sistemático).
➡️ TRANSIÇÃO: "Há uma variação híbrida: guardrails em paralelo."

---

### Slide 27 — Guardrails em Paralelo

**Título**: Guardrails em Paralelo
**Objetivo**: Mostrar um padrão híbrido de parallelization para segurança.
**Conteúdo**:
- Modelo A: gera a resposta principal
- Modelo B (paralelo): filtra/modera a resposta
- Se B sinaliza problema → bloqueia ou regenera
- Latência quase zero adicionada (roda em paralelo)
- Exemplo: resposta de suporte + verificação de PII em paralelo

**Diagrama**: Duas lanes paralelas: gerar + filtrar
**Animação**: Duas lanes disparam simultaneamente
**Imagem**: Duas lanes com ícones de resposta e escudo
**Tempo**: 2 min

**Rodape**: PII = Personally Identifiable Information — dados pessoais identificaveis

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Guardrails em paralelo é um padrão de produção muito útil. Enquanto o modelo principal gera a resposta, um segundo modelo (em paralelo) avalia se a resposta é segura. Se o guardrail sinaliza problema, bloqueia ou regenera. A vantagem é latência: como roda em paralelo, o guardrail não adiciona tempo. O custo é 2× (duas chamadas), mas a segurança é crítica em produção. Exemplo: resposta de suporte + verificação de PII + moderação de toxicidade, tudo em paralelo.
💡 ANALOGIA: É como um segurança em um evento. Enquanto o garçom serve (modelo principal), o segurança observa (guardrail). Se vê problema, intervém. O garçom não espera o segurança aprovar cada prato — trabalham em paralelo.
⚠️ ERROS COMUNS: Alunos rodam guardrails em série (depois da resposta). Isso adiciona latência. Paralelo é o ponto.
➡️ TRANSIÇÃO: "Outra aplicação: avaliação LLM-as-judge em paralelo."

---

### Slide 28 — LLM-as-Judge em Paralelo

**Título**: LLM-as-Judge em Paralelo
**Objetivo**: Conectar parallelization com avaliação (ponte para evaluator-optimizer).
**Conteúdo**:
- N julgamentos paralelos de uma saída (mesma tarefa de avaliação)
- Votação reduz **variância** do juiz
- Usado em pipelines de qualidade antes de entregar ao usuário
- Cuidado: viés do juiz é sistemático (votação não resolve viés, só variância)

**Diagrama**: Saída → N juízes em paralelo → agregação de scores
**Animação**: N juízes avaliam, scores convergem
**Imagem**: Diagrama com N juízes e balança de agregação
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: LLM-as-judge é usar um LLM para avaliar a saída de outro LLM. Em paralelo, você roda N juízes e agrega os scores. A votação reduz a variância — se um juiz deu 3/5 por acaso, mas os outros 5 deram 4/5, a média converge para o real. Mas atenção: viés do juiz é sistemático. Se todos os juízes têm viés de preferir respostas longas, a votação reforça esse viés. Voting resolve variância, não viés. Para viés, você precisa calibrar o juiz (ex.: rubric estruturada).
💡 ANALOGIA: É como um painel de jurados. Vários jurados reduzem a variância da nota. Mas se todos os jurados têm o mesmo viés (ex.: preferem candidatos de uma escola), a média não corrige.
⚠️ ERROS COMUNS: Alunos usam N juízes idênticos (mesmo modelo, mesmo prompt). Isso não reduz variância — você precisa variação (temperatura, prompt levemente diferente).
➡️ TRANSIÇÃO: "Mas parallelization tem armadilhas. Vamos ver."

---

### Slide 29 — Erros Comuns: Dependências Ocultas, Custo Explodindo

**Título**: Erros Comuns em Parallelization
**Objetivo**: Alertar sobre armadilhas típicas de parallelization.
**Conteúdo**:
- **Dependência oculta**: "subtarefas independentes" que não são (ex.: step 2 precisa de output de step 1)
- **Custo explodindo**: N=5 voting em pipeline de 10 steps = 50 chamadas
- **Reducer mal feito**: síntese perde informação crítica
- **Timeout não tratado**: uma subtarefa lenta atrasa todo o pipeline
- Mitigação: medir custo/latência de cada subtarefa desde o início

**Diagrama**: 4 ícones de "perigo" (`etho-danger`) com labels
**Animação**: Cada ícone aparece com click
**Imagem**: 4 ícones de armadilha (elo quebrado, explosão, funil entupido, ampulheta)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Quatro armadilhas clássicas. Dependência oculta: você acha que as subtarefas são independentes, mas não são — uma precisa do output da outra. Solução: desenhe o DAG de dependências ANTES de paralelizar. Custo explodindo: voting com N=5 em um pipeline de 10 steps gera 50 chamadas. Sem budget, você descobre no fim do mês. Reducer mal feito: o agregador perde informação — sintetizar 5 análises em 1 parágrafo pode descartar o insight crucial. Timeout: uma subtarefa lenta (modelo ocupado) atrasa tudo — use timeout e fallback.
💡 ANALOGIA: É como coordenar uma equipe. Dependência oculta = "espera, preciso do seu relatório antes de começar". Custo explodindo = cada um contratou 5 freelancers. Reducer mal feito = o gestor resumiu tudo em uma linha e perdeu o detalhe. Timeout = um membro sumiu e ninguém decide sem ele.
⚠️ ERROS COMUNS: Alunos não medem custo desde o início. Em produção, custo explode silenciosamente. Regra: log de custo por chamada desde o dia 1.
➡️ TRANSIÇÃO: "Vamos ver código de ambos os modos."

---

### Slide 30 — Código: Parallelization (Sectioning + Voting)

**Título**: Código: Parallelization
**Objetivo**: Mostrar implementação concreta de ambos os modos.
**Conteúdo**:
- Sectioning: `asyncio.gather()` com N chamadas especializadas
- Voting: `asyncio.gather()` com N chamadas idênticas (temp variada)
- Reducer: função que agrega resultados
- Snippet em Python com asyncio
- Métricas: medir custo e latência de cada modo

```python
import asyncio

async def sectioning(doc):
    parts = split(doc)
    results = await asyncio.gather(*[analyze(p) for p in parts])
    return reducer(results)

async def voting(question, n=5):
    answers = await asyncio.gather(*[
        llm(question, temperature=0.7+i*0.05) for i in range(n)
    ])
    return majority_vote(answers)
```

**Diagrama**: Code block com asyncio
**Animação**: Highlight de `gather()` e `reducer`
**Imagem**: Screenshot do VS Code
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O padrão é `asyncio.gather()` para ambas as variantes. Em sectioning, cada chamada é especializada (analisa uma parte diferente). Em voting, cada chamada é idêntica mas com temperatura diferente (para gerar variação). O reducer agrega. Vejam que a única diferença é o que vai dentro de gather: funções diferentes (sectioning) vs mesma função com parâmetros diferentes (voting). Simples, mas poderoso.
💡 ANALOGIA: Sectioning é como uma equipe onde cada um faz uma parte do relatório. Voting é como a mesma equipe escrevendo o relatório 5 vezes e escolhendo o melhor.
⚠️ ERROS COMUNS: Alunos esquecem de tratar exceções no gather. Se uma chamada falha, gather lança exceção. Use `return_exceptions=True` ou try/except em cada chamada.
➡️ TRANSIÇÃO: "Vamos ver isso rodando ao vivo."

---

### Slide 31 — DEMO: Latência = max vs sum

**Título**: DEMO — Latência Serial vs Paralelo
**Objetivo**: Demo ao vivo mostrando o ganho de latência do paralelismo.
**Conteúdo**:
- Mesma tarefa: rodar 3 subtarefas
- Versão serial: sum(3 chamadas) → ~9s
- Versão paralela: max(3 chamadas) → ~3s
- Mostrar timer no terminal
- Mostrar custo: igual nos dois casos (mesmas chamadas)
- **Lição**: paralelismo não reduz custo, reduz latência

**Diagrama**: Terminal com timer lado a lado (serial vs paralelo)
**Animação**: Barras de tempo crescendo em paralelo
**Imagem**: Terminal com output de timer
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esta é a demo mais importante do módulo. Rodo a mesma tarefa de duas formas. Serial: chamo 3 LLMs em sequência, cronometro. Paralelo: chamo os mesmos 3 LLMs com asyncio.gather, cronometro. A latência cai de ~9s para ~3s. Mas o custo é IDÊNTICO — paguei as mesmas 3 chamadas nos dois casos. A lição é visceral: paralelismo NÃO reduz custo, reduz latência. Se o problema for custo, paralelismo não ajuda. Se for latência, é a ferramenta certa.
💡 ANALOGIA: É como lavar 3 pratos. Um de cada vez (serial) = 3 minutos. Três pessoas lavando ao mesmo tempo (paralelo) = 1 minuto. Mas você pagou 3 pessoas nos dois casos — só que no serial elas ficaram ociosas.
❓ PERGUNTA PARA A TURMA: "Então quando paralelismo NÃO vale a pena?" (Resposta: quando o custo é o gargalo, não a latência)
⚠️ ERROS COMUNS: Alunos acham que paralelismo reduz custo. Não reduz. Você paga todas as chamadas. Só reduz latência.
➡️ TRANSIÇÃO: "Vamos praticar a decisão entre sectioning e voting."

---

### Slide 32 — Exercício: Voting vs Sectioning

**Título**: Exercício — Voting vs Sectioning
**Objetivo**: Praticar a decisão entre os dois modos de parallelization.
**Conteúdo**:
- Pergunta: *Quando voting é preferível a sectioning?*
- 3 cenários rápidos — voting ou sectioning?
  1. Traduzir 3 páginas independentes
  2. Decidir se um email é phishing
  3. Gerar 3 alternativas de copy para anúncio
- Votação rápida (mãos levantadas)
- Respostas: 1=sectioning, 2=voting, 3=sectioning (mas usa voting para escolher a melhor)

**Diagrama**: 3 cards com cenários
**Animação**: Cards aparecem um a um
**Imagem**: 3 cards coloridos com ícones
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Deixem a turma votar com mãos. Cenário 1: traduzir 3 páginas independentes = sectioning (cada página é uma subtarefa diferente). Cenário 2: decidir se email é phishing = voting (mesma pergunta, múltiplas perspectivas para robustez). Cenário 3: gerar 3 alternativas de copy = sectioning (cada alternativa é diferente) MAS se você quer escolher a melhor, usa voting (ou um judge) para selecionar. A regra: sectioning quando as subtarefas são DIFERENTES; voting quando é a MESMA tarefa e você quer robustez.
💡 ANALOGIA: Sectioning é como 3 pessoas cozinhando pratos diferentes para um jantar. Voting é como 3 pessoas provando o mesmo vinho e votando se está bom.
❓ PERGUNTA PARA A TURMA: "Mãos levantadas: sectioning ou voting para cada cenário?" (comparar com gabarito)
⚠️ ERROS COMUNS: Alunos usam voting para subtarefas independentes. Desperdício: se as tarefas são diferentes, voting não agrega valor.
➡️ TRANSIÇÃO: "Intervalo! Voltamos com orchestrator-workers."

---
