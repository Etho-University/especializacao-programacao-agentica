# ETHAGT16 — Slides Detalhados + Notas do Professor (Parte 1: Slides 1-25)

> Universidade Etho · Especialização em Programação Agêntica
> Cada slide contém: título, objetivo, conteúdo, notas do professor, diagrama, animação, imagem, tempo.

---

## SEÇÃO A — Abertura (Slides 1-6 · 6 min)

---

### Slide 1 — Capa

**Título**: ETHAGT16 — Sociedades de Agentes & Autonomous Research Systems
**Objetivo**: Identificar a aula, o professor e o contexto — último módulo antes do Capstone.
**Conteúdo**:
- ETHAGT16 — Sociedades de Agentes & Autonomous Research Systems
- Universidade Etho · Especialização em Programação Agêntica
- Fase D — Fronteira · 15 h
- Professor · Data
- "Último módulo antes do Capstone (ETHAGT90)"

**Diagrama**: Logo Etho (canto sup. esquerdo) + imagem de fundo abstrata (rede de agentes interconectados)
**Animação**: Fade in do título (300ms)
**Imagem**: Fundo `etho-dark` (#0F1E2D) com pattern de nós e arestas
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Bem-vindos à fronteira. Este é o último módulo antes do Capstone. Tudo que vimos até aqui — Augmented LLM (ETHAGT01), reasoning (ETHAGT04), memory (ETHAGT05), RAG (ETHAGT06), MCP (ETHAGT08), multi-agent (ETHAGT09-10), AgentOps (ETHAGT12), security (ETHAGT13) — converge aqui. Hoje vamos de 1 agente a uma SOCIEDADE de agentes, e de uma tarefa a um SISTEMA DE PESQUISA AUTÔNOMA. Vocês estão na ponta do que existe hoje.
💡 ANALOGIA: É como a diferença entre dirigir um carro (ETHAGT01) e gerenciar uma frota de carros autônomos numa cidade (ETHAGT16). O problema muda de escala e de natureza.
❓ PERGUNTA PARA A TURMA: "Quantos de vocês já rodaram uma simulação multi-agente na vida?" (levantar mãos — calibrar)
⚠️ ERROS COMUNS: Alunos chegam querendo "deployar" sociedades em produção. Preciso calibrar: o estado da arte ainda é experimental. O foco hoje é entender a fronteira, não operacionalizá-la.
➡️ TRANSIÇÃO: "Vamos começar definindo o que vocês vão conseguir fazer ao final desta aula."

---

### Slide 2 — Objetivos do Módulo

**Título**: Objetivos do Módulo
**Objetivo**: Deixar claro o que o aluno deve conseguir FAZER ao final da aula.
**Conteúdo**:
- **Objetivo geral**: Atingir a fronteira do estado da arte — sociedades de agentes, simulações sociais, sistemas de pesquisa autônoma
- **Objetivos específicos**:
  1. Modelar sociedades de agentes (papéis, instituições, normas)
  2. Aplicar simulações multi-agente (Smallville-like)
  3. Construir um sistema de pesquisa autônoma (pergunta → hipótese → experimento → relatório)
  4. Discutir emergência, convergência e alinhamento
  5. Conhecer a fronteira de pesquisa (AI Scientist, AlphaEvolve, Swarm research)

**Diagrama**: 5 ícones representando cada objetivo (sociedade, simulação, pipeline, emergência, fronteira)
**Animação**: Objetivos aparecem um a um (on click)
**Imagem**: Ícones minimalistas em `etho-accent` (#E85D2F)
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Cada objetivo é mensurável. O objetivo #3 — construir um sistema de pesquisa autônoma — é o que vocês vão prototipar no Projeto do módulo. É também o esboço do Capstone (ETHAGT90). O objetivo #4 — emergência — é o mais sutil: é onde a soma é diferente das partes, e onde mora o risco.
💡 ANALOGIA: É como a diferença entre biologia molecular e ecologia. Em ETHAGT01-15 vocês estudaram a "molécula" (agente). Agora estudamos o "ecossistema" (sociedade). O comportamento do ecossistema não se reduz às moléculas.
❓ PERGUNTA PARA A TURMA: "Qual desses objetivos vocês acham mais desafiador?" (deixar responder — costuma ser #3 ou #4)
⚠️ ERROS COMUNS: Alunos acham que "sociedade de agentes" é só "muito multi-agent". Não — sociedade adiciona normas, reputação, instituições e emergência. São conceitos novos.
➡️ TRANSIÇÃO: "Antes de detalhar, vamos ver onde esta aula toca o Framework Etho de competências."

---

### Slide 3 — Competências Desenvolvidas

**Título**: Competências Desenvolvidas
**Objetivo**: Conectar a aula ao Framework Etho de competências.
**Conteúdo**:

| Competência | Nível ao final |
|---|---|
| C1 Programação Agêntica | **A** (Avançado) |
| C2 Multi-Agent Systems | **A** (Avançado) |
| C3 MCP & Tool Use | **B** (Básico) |
| C4 Agent Memory | **A** (Avançado) |
| C5 AgentOps & Avaliação | **I** (Intermediário) |
| C6 Agent Security | **I** (Intermediário) |

**Diagrama**: Radar chart com 6 eixos mostrando níveis A/B/I
**Animação**: Radar aparece com wipe (left-to-right, 500ms)
**Imagem**: Badge visual por competência (círculos coloridos)
**Tempo**: 0.5 min

**Rodape**: AgentOps = Agent Operations — operacao e monitoramento de agentes em producao  ·  MCP = Model Context Protocol — Protocolo de Contexto de Modelo

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Este módulo leva C1 e C2 ao nível Avançado — vocês vão modelar e justificar sociedades inteiras, não só agentes. C4 — Agent Memory — também chega ao Avançado porque sociedades exigem memory streams (Smallville), reflection e memória distribuída. C5 e C6 ficam em Intermediário: AgentOps e Security em sociedades ainda são áreas em aberto, então o nível é "entendo os desafios e sei onde estão as lacunas".
💡 ANALOGIA: Vocês estão saindo do estágio de "piloto de um drone" e entrando no de "comandante de uma esquadrilha". A escala muda as competências exigidas.
⚠️ ERROS COMUNS: Alunos acham que C5 e C6 em "I" significa "fracos". Não — significa que a própria área é imatura. Ninguém tem AgentOps de sociedade maduro hoje.
➡️ TRANSIÇÃO: "Vamos ver como esta aula está estruturada para entregar essas competências."

---

### Slide 4 — Agenda

**Título**: Agenda da Aula
**Objetivo**: Mostrar o roteiro da aula com tempos estimados.
**Conteúdo**:
- **Bloco 1 (25 min)**:
  - Abertura (6 min) — objetivos, motivação, contexto
  - Sociedades de Agentes (8 min) — papéis, normas, reputação, modelos
  - Simulações Sociais (6 min) — Smallville, casos de uso, limites
  - Intervalo (5 min)
- **Bloco 2 (25 min)**:
  - Autonomous Research Systems (12 min) — pipeline, AI Scientist, AlphaEvolve, DEMO
  - Emergência e Alinhamento (8 min) — desejada vs indesejada, alinhamento
  - Fechamento (10 min) — fronteira, ética, resumo, quiz, Capstone, Q&A

**Diagrama**: Timeline horizontal com 6 seções coloridas
**Animação**: Timeline cresce da esquerda para direita (500ms)
**Imagem**: Ícones de relógio por seção
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A aula tem dois blocos. O primeiro estabelece sociedades e simulações. O segundo é onde mora a fronteira: Research Systems, AI Scientist, DEMO ao vivo, e emergência. A DEMO Mini Sociedade (Slide 30) é o ponto alto — vocês vão ver 5 agentes produzindo um relatório em tempo real.
⚠️ ERROS COMUNS: Alunos chegam atrasados e perdem a motivação (Slide 5). Avisar que a motivação define o tom de toda a aula.
➡️ TRANSIÇÃO: "Vamos começar pelo porquê. Por que sociedades de agentes agora?"

---

### Slide 5 — Motivação: O Problema do Agente Isolado

**Título**: O Problema do Agente Isolado
**Objetivo**: Criar tensão — agentes isolados não escalam para problemas complexos.
**Conteúdo**:
- **Agente isolado**: resolve uma tarefa bem
- **Sociedade de agentes**: pode resolver problemas que nenhum agente resolve sozinho
- **Exemplo**: Generative Agents (Stanford Smallville) — 25 agentes simulam vida social, organizam festa de Valentine's Day sozinhos
- **Fronteira**: AI Scientist (Sakana) — agente que conduz pesquisa científica do início ao fim
- **Pergunta**: *O que acontece quando 100 agentes interagem sem supervisão humana?*

**Diagrama**: Crescimento: 1 agente (ponto) → 5 agentes (grupo) → 25 agentes (sociedade) → 100 agentes (emergência)
**Animação**: Pontos surgem e se conectam em rede (D1)
**Imagem**: Sequência de 4 painéis em `etho-primary` → `etho-accent`
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Um agente isolado resolve uma tarefa. Mas alguns problemas exigem múltiplas perspectivas, debate, validação por pares, especialização. Nesses casos, uma SOCIEDADE de agentes pode resolver o que nenhum agente resolve sozinho. Smallville mostrou isso em 2023: 25 agentes com memória e rotinas organizaram uma festa sozinhos — ninguém programou "organize festa". O AI Scientist (Sakana, 2024) levou isso à pesquisa: conduziu ML de ponta a ponta por ~$15/paper. Mas a pergunta-chave é: o que acontece quando 100 agentes interagem sem supervisão? Emergência — pode ser cooperação... ou conluio.
💡 ANALOGIA: Um músico toca bem. Uma orquestra toca coisas que nenhum músico toca sozinho. Mas uma orquestra SEM maestro pode descarrilar. Sociedade de agentes é isso: o potencial é enorme, mas sem coordenação pode colapsar.
❓ PERGUNTA PARA A TURMA: "O que acontece quando 100 agentes interagem sem supervisão humana?" (deixar pensar 5s — não responder ainda, esse é o gancho da aula)
⚠️ ERROS COMUNS: Alunos acham que "mais agentes = melhor". Não — mais agentes = mais emergência, e emergência pode ser boa ou ruim. Quantidade não é qualidade.
➡️ TRANSIÇÃO: "Por que só agora isso é viável? O que mudou?"

---

### Slide 6 — Contexto: Por Que Sociedades Agora

**Título**: Por Que Sociedades Agora
**Objetivo**: Explicar a confluência histórica que tornou sociedades de agentes viáveis.
**Conteúdo**:
- **Linha do tempo**:
  - 2022 — ReAct (padrão de agente individual)
  - 2023 — tool calling nativo + frameworks multi-agent
  - abr/2023 — Generative Agents / Smallville (arXiv:2304.03442)
  - ago/2024 — AI Scientist (Sakana, arXiv:2408.06292) + AlphaEvolve (DeepMind)
- **Confluência**: reasoning + tools + memory + context window + cost reduction
- **Próxima fronteira**: sociedades autônomas

**Diagrama**: Timeline horizontal com marcos (D2)
**Animação**: Marcos aparecem sequencialmente
**Imagem**: Timeline estilizada em `etho-primary`
**Tempo**: 1 min

**Rodape**: ReAct = Reasoning and Acting — padrao de loop Thought / Action / Observation

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Três coisas convergiram: (1) reasoning estruturado (ReAct, Reflexion), (2) tool calling nativo (API), (3) context window grande e barata. Em 2023, Smallville provou que agentes podem habitar um mundo compartilhado e produzir emergência. Em 2024, AI Scientist e AlphaEvolve provaram que agentes podem conduzir pesquisa autônoma. Estamos a 2-3 anos de sociedades realmente autônomas em escala.
💡 ANALOGIA: É como a transição da web 1.0 para a 2.0. A tecnologia existia antes, mas a confluência (AJAX, banda larga, smartphones) criou algo novo. Em agentes, a confluência é reasoning + tools + cost.
⚠️ ERROS COMUNS: Alunos acham que sociedades de agentes são "novidade de 2024". Não — Smallville é de abril de 2023. A ideia existe, mas só agora é acessível.
➡️ TRANSIÇÃO: "Vamos começar pelo básico: o que é uma sociedade de agentes?"

---

## SEÇÃO B — Sociedades de Agentes (Slides 7-15 · 8 min)

---

### Slide 7 — [SEÇÃO] Sociedades de Agentes

**Título**: Sociedades de Agentes
**Objetivo**: Transição para a Unidade 1 — Sociedades de agentes.
**Conteúdo**: Número "1" grande + "Sociedades de Agentes"
**Diagrama**: Fundo `etho-primary`
**Animação**: Número 1 surge em `etho-accent` (300ms)
**Imagem**: Pattern sutil de nós em `etho-dark`
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Entramos na primeira unidade. Vamos do agente individual até a sociedade, definindo papéis, normas, reputação e confiança.
➡️ TRANSIÇÃO: "Comecemos pela evolução: do 1 agente à sociedade."

---

### Slide 8 — Do Agente Individual à Sociedade

**Título**: Do Agente Individual à Sociedade
**Objetivo**: Mostrar a evolução de 1 agente → sociedade em 4 níveis.
**Conteúdo**:
- **Nível 0**: Agente individual (LLM + tools + memory)
- **Nível 1**: Pequeno grupo (2-5 agentes, colaboração direta)
- **Nível 2**: Instituição (papéis fixos, normas explícitas, hierarquia)
- **Nível 3**: Sociedade (25+ agentes, normas emergentes, comportamento não programado)
- Cada nível adiciona: complexidade, potencial e risco

**Diagrama**: Escada de 4 níveis (D3)
**Animação**: Níveis aparecem de baixo para cima
**Imagem**: 4 níveis em gradiente `etho-primary` → `etho-accent`
**Tempo**: 1 min

**Rodape**: LLM = Large Language Model — Modelo de Linguagem de Grande Escala

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A escada tem 4 níveis. Nível 0 é o que vocês dominam — um agente. Nível 1 é o multi-agent básico (ETHAGT09-10). Nível 2 é a instituição: papéis fixos, normas explícitas — pense em MetaGPT, onde cada agente tem um SOP. Nível 3 é a sociedade: normas emergem, o comportamento coletivo não é programado. Smallville é o caso canônico de Nível 3.
💡 ANALOGIA: Nível 0 é uma pessoa. Nível 1 é uma equipe de projeto. Nível 2 é uma empresa com organograma. Nível 3 é uma cidade — ninguém programa tudo, mas padrões emergem.
⚠️ ERROS COMUNS: Alunos pulam direto para Nível 3 sem entender Nível 2. Sem normas explícitas (Nível 2), Nível 3 vira caos. A escada é cumulativa.
➡️ TRANSIÇÃO: "No Nível 2 e 3, precisamos de papéis. Quais?"

---

### Slide 9 — Papéis em Sociedades de Agentes

**Título**: Papéis em Sociedades de Agentes
**Objetivo**: Apresentar papéis canônicos em sociedades de agentes.
**Conteúdo**:
- **Pesquisador**: explora, levanta informações
- **Crítico**: identifica falhas, questiona premissas
- **Sintetizador**: integra contribuições divergentes
- **Revisor**: valida qualidade e coerência
- **Editor**: finaliza, formata, publica
- Análogo a um time de pesquisa humano
- Papéis podem ser dinâmicos (agentes trocam de papel)

**Diagrama**: 5 ícones de papéis em círculo (D4)
**Animação**: Papéis aparecem um a um
**Imagem**: Ícones minimalistas em `etho-accent`
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esses 5 papéis são canônicos em sociedades de agentes de pesquisa. Vocês vão vê-los na DEMO (Slide 30). Cada papel tem um prompt, um conjunto de tools e um critério de sucesso. Mas o detalhe importante: papéis podem ser dinâmicos. Um agente pode começar como pesquisador e virar editor se a situação exigir.
💡 ANALOGIA: É como um time editorial de revista: cada um tem um papel, mas em emergências as pessoas trocam de chapéu. O crítico vira autor se o autor adoecer.
❓ PERGUNTA PARA A TURMA: "Qual desses papéis vocês acham mais difícil de automatizar bem?" (costuma ser o crítico — exige julgamento — ou o sintetizador — exige integração de perspectivas divergentes)
⚠️ ERROS COMUNS: Alunos acham que papéis são fixos. Não — a vantagem de LLMs é que o mesmo modelo pode trocar de papel com prompt diferente. Mas isso abre risco de confusão.
➡️ TRANSIÇÃO: "Papéis sem normas viram anarquia. O que são normas?"

---

### Slide 10 — Normas e Instituições

**Título**: Normas e Instituições
**Objetivo**: Explicar como sociedades de agentes estabelecem regras.
**Conteúdo**:
- **Normas**: regras compartilhadas (explícitas ou emergentes)
- **Instituições**: estruturas que mantêm normas (ex: revisão por pares)
- Análogo a instituições humanas (tribunais, mercados, universidades)
- Em sociedades de agentes: constitution, votação, reputação
- **Tensão**: normas explícitas (controláveis) vs emergentes (adaptáveis)

**Diagrama**: Estrutura hierárquica: Sociedade → Instituições → Normas
**Animação**: Hierarquia surge de cima para baixo
**Imagem**: Pirâmide de 3 níveis
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Normas são regras compartilhadas. Instituições são estruturas que mantêm normas — revisão por pares é uma instituição. Em sociedades de agentes, temos três mecanismos: constitution (regras globais), votação (decisão coletiva), reputação (memória de comportamento passado). A tensão central: normas explícitas dão controle mas são rígidas; normas emergentes são adaptáveis mas imprevisíveis.
💡 ANALOGIA: Pense numa constituição política vs costumes sociais. A constituição é explícita (você pode ler). Os costumes emergem (ninguém votou, mas todo mundo segue). Em agentes, mesmo padrão.
⚠️ ERROS COMUNS: Alunos querem controlar tudo com normas explícitas. Mas se você controla tudo, você não tem emergência — só tem um workflow grande. Sociedade precisa de espaço para emergência.
➡️ TRANSIÇÃO: "Normas precisam de confiança. Como agentes decidem em quem confiar?"

---

### Slide 11 — Reputação e Confiança

**Título**: Reputação e Confiança
**Objetivo**: Explicar como agentes decidem em quem confiar.
**Conteúdo**:
- **Reputação**: histórico de interações de um agente
- **Confiança**: função da reputação + contexto
- Em sociedades: agentes podem "votar" em quem confiar
- Análogo a PageRank: confiança propagada pela rede
- **Sem reputação**: sociedade colapsa (free-riders, manipulação)

**Diagrama**: Grafo de agentes com pesos de confiança (D5)
**Animação**: Arestas grossas vs finas se destacam
**Imagem**: Grafo colorido por peso
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Reputação é a memória coletiva de quem cumpriu normas. Confiança é a decisão de cooperar baseada nessa memória. Sem reputação, a sociedade colapsa: free-riders exploram, manipuladores dominam. A analogia técnica é PageRank — confiança não é só sobre você, é sobre quem confia em você.
💡 ANALOGIA: É como avaliação no Airbnb. Você confia no hóspede não só pela nota dele, mas por quem deu a nota. Nota de um superhost vale mais que nota de um novato.
⚠️ ERROS COMUNS: Alunos acham que reputação é uma métrica simples. Não — reputação é contextual (bom em X pode ser ruim em Y) e propagada (quem confia em você importa).
➡️ TRANSIÇÃO: "Vamos ver os modelos conônicos que implementam isso."

---

### Slide 12 — Modelos: Generative Agents, AgentVerse, ChatArena

**Título**: Modelos Canônicos de Sociedade
**Objetivo**: Apresentar os 3 modelos canônicos de sociedade de agentes.
**Conteúdo**:
- **Generative Agents** (Stanford): 25 agentes, Smallville, vida social simulada
- **AgentVerse** (arXiv:2308.10848): framework multi-agente, papéis flexíveis, tarefas colaborativas
- **ChatArena**: ambientes de jogo/diálogo multi-agente
- Cada modelo resolve um problema diferente

**Diagrama**: 3 colunas comparativas
**Animação**: Colunas aparecem uma a uma
**Imagem**: Logos dos 3 modelos (placeholder)
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Generative Agents (Smallville) é o caso canônico de simulação social — foco em emergência. AgentVerse é um framework para tarefas colaborativas — foco em produtividade. ChatArena é mais leve, foco em diálogo/jogo. Cada um resolve um problema diferente: Smallville = entender, AgentVerse = produzir, ChatArena = experimentar.
💡 ANALOGIA: Smallville é como um reality show (observar), AgentVerse é como uma fábrica (produzir), ChatArena é como um jogo (experimentar).
⚠️ ERROS COMUNS: Alunos confundem os 3. Generative Agents é o paper/pesquisa; AgentVerse e ChatArena são frameworks. Não são equivalentes.
➡️ TRANSIÇÃO: "Vamos ver a arquitetura de uma sociedade de agentes."

---

### Slide 13 — Diagrama: Arquitetura de uma Sociedade

**Título**: Arquitetura de uma Sociedade de Agentes
**Objetivo**: Visualizar a arquitetura de uma sociedade de agentes.
**Conteúdo**:
- Ambiente compartilhado (sandbox)
- Agentes com papéis (pesquisador, crítico, sintetizador, revisor, editor)
- Normas governando a sociedade
- Saída: comportamento emergente

**Diagrama**: `12-Diagrams/ETHAGT16/society.mmd`
**Animação**: Componentes surgem do centro para fora
**Imagem**: Diagrama `.mmd` renderizado
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esta é a arquitetura canônica. No centro, a sociedade — agentes com papéis que interagem. Acima, as normas que governam as interações ("citar fontes", "editor tem veto"). Abaixo, a saída: comportamento emergente. Note que as normas são externas à sociedade — elas vêm de fora (designer) ou emergem de dentro. Essa é a diferença entre instituição (normas externas) e sociedade (normas emergentes).
💡 ANALOGIA: Pense num tribunal: os advogados (agentes) têm papéis, as leis (normas) governam, e a sentença (emergência) resulta de interação. Ninguém programou a sentença — ela emerge.
⚠️ ERROS COMUNS: Alunos acham que emergência é "mágica". Não — emergência é o resultado determinístico de regras locais em grande escala. Mas é imprevisível para o designer.
➡️ TRANSIÇÃO: "Vamos sistematizar a distinção entre níveis."

---

### Slide 14 — Comparação: Grupo vs Instituição vs Sociedade

**Título**: Grupo vs Instituição vs Sociedade
**Objetivo**: Sistematizar a distinção entre níveis de organização.
**Conteúdo**:
- **Grupo**: colaboração ad-hoc, sem normas fixas
- **Instituição**: papéis fixos, normas explícitas, hierarquia
- **Sociedade**: normas emergentes, reputação, comportamento não programado
- **Trade-off**: controle (grupo) vs adaptabilidade (sociedade)

**Diagrama**: 3 colunas com eixos: controle, adaptabilidade, previsibilidade, risco (D7)
**Animação**: Colunas aparecem uma a uma
**Imagem**: Tabela 3x4 colorida
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A tabela é direta: grupo tem controle alto mas adaptabilidade baixa. Instituição é meio-termo. Sociedade tem controle baixo mas adaptabilidade alta — e risco alto. A pergunta de design é: qual nível meu problema exige? Para tarefas estruturadas, grupo. Para processos com SOPs, instituição. Para descoberta e exploração, sociedade.
⚠️ ERROS COMUNS: Alunos começam pela sociedade sem precisar. 80% dos problemas se resolvem em instituição. Sociedade é para quando você PRECISA de emergência.
➡️ TRANSIÇÃO: "Vamos praticar com um exercício rápido."

---

### Slide 15 — Exercício Rápido: Definindo Papéis

**Título**: Exercício — Comitê Editorial
**Objetivo**: Praticar design de papéis para um problema.
**Conteúdo**:
- Cenário: "Simular um comitê editorial de revista científica"
- Em duplas: definir 5 papéis e suas responsabilidades
- Qual norma deve ser compartilhada?
- Como reputação é acumulada?
- 1 min discussão, share rápido

**Diagrama**: Caixa de discussão em `etho-warning`
**Animação**: Caixa surge com bounce
**Imagem**: Ícone de discussão em duplas
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: 1 minuto em duplas. Depois peço 2 duplas para compartilhar. O ponto-chave: a norma compartilhada deve ser operacional (não "seja justo", mas "toda decisão vem com justificativa escrita"). E reputação deve ser mensurável (número de revisões aceitas).
❓ PERGUNTA PARA A TURMA: Após 1 min: "Qual dupla definiu uma norma operacional clara?"
⚠️ ERROS COMUNS: Duplas propõem normas vagas ("seja rigoroso"). Eu rebato: "Como um agente verifica isso?" A norma precisa ser executável por um LLM.
➡️ TRANSIÇÃO: "Vamos mudar de foco: das sociedades em si para as SIMULAÇÕES sociais."

---

## SEÇÃO C — Simulações Sociais (Slides 16-22 · 6 min)

---

### Slide 16 — [SEÇÃO] Simulações Sociais

**Título**: Simulações Sociais
**Objetivo**: Transição para a Unidade 2 — Simulações sociais.
**Conteúdo**: Número "2" grande + "Simulações Sociais"
**Diagrama**: Fundo `etho-primary`
**Animação**: Número 2 surge em `etho-accent`
**Imagem**: Pattern sutil de nós
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Segunda unidade. Vamos do conceito de sociedade para o caso canônico de simulação social: Smallville. Depois casos de uso e limites.
➡️ TRANSIÇÃO: "Comecemos pelo caso mais famoso."

---

### Slide 17 — Sandbox Social: Smallville

**Título**: Sandbox Social — Smallville
**Objetivo**: Apresentar Smallville como caso canônico de simulação social.
**Conteúdo**:
- **Smallville**: mundo virtual com 25 agentes
- Cada agente: perfil, rotina, memória, objetivos
- Ambiente: mapas, locais, recursos compartilhados
- **Resultado**: agentes organizam festa de Valentine's Day sozinhos
- Fonte: Park et al., arXiv:2304.03442

**Diagrama**: Mapa de Smallville com agentes em locais (D8)
**Animação**: Mapa surge, agentes aparecem como pontos
**Imagem**: Mapa estilizado de Smallville
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Smallville é o experimento que abriu o campo. 25 agentes, cada um com um perfil ("John Lin, farmacêutico, gosta de família"), rotina diária, e um memory stream. Eles habitam um mundo virtual com mapa, locais (café, parque, casa). O resultado que chocou: um agente decidiu dar uma festa de Valentine's Day, convidou outros, e a festa aconteceu — ninguém programou "organize festa". Foi emergência pura.
💡 ANALOGIA: É como The Sims, mas cada personagem tem um LLM que decide o que fazer com base em memória e reflexão. A diferença: ninguém programou os eventos — eles emergem.
⚠️ ERROS COMUNS: Alunos acham que Smallville "prevê" comportamento humano. Não — Smallville gera comportamento PLAUSÍVEL, não necessariamente preditivo. A diferença é crucial.
➡️ TRANSIÇÃO: "Como essa mágica funciona tecnicamente?"

---

### Slide 18 — Como Smallville Funciona

**Título**: Como Smallville Funciona
**Objetivo**: Explicar a arquitetura técnica de Smallville.
**Conteúdo**:
- **Memory stream**: log cronológico de experiências
- **Retrieval**: relevância + recência + importância
- **Reflection**: síntese de memórias em insights de alto nível
- **Planning**: planos diários baseados em rotina + objetivos
- **Action**: geração de ação baseada em contexto + reflexão

**Diagrama**: Pipeline: Memory → Retrieval → Reflection → Planning → Action (D9)
**Animação**: Pipeline flui da esquerda para direita
**Imagem**: Diagrama `.mmd` renderizado
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O motor do Smallville é um pipeline de memória. Cada agente tem um memory stream — um log cronológico de tudo que experimentou. Para agir, ele faz retrieval de memórias relevantes, ponderando três fatores: relevância (similaridade semântica), recência (memórias recentes pesam mais), importância (memórias marcadas como importantes). Em períodos regulares, ele faz reflection — sintetiza memórias em insights de alto nível ("John valoriza família"). Com isso, ele planeja o dia e age.
💡 ANALOGIA: É como a sua própria memória. Você não lembra tudo igual — lembra do jantar de ontem (recência), da morte do seu cachorro (importância), e do que é relevante para a conversa atual. Smallville formaliza isso.
⚠️ ERROS COMUNS: Alunos confundem reflection com summarization. Reflection é mais — é síntese semântica que produz novos insights. Summarization só comprime.
➡️ TRANSIÇÃO: "Para que serve isso na prática?"

---

### Slide 19 — Casos de Uso: Policy, Mercado, Opinião

**Título**: Casos de Uso de Simulações Sociais
**Objetivo**: Mostrar aplicações práticas de simulações sociais.
**Conteúdo**:
- **Policy simulation**: simular impacto de lei (imposto, subsídio)
- **Mercado**: agentes compram/vendem, formação de preços
- **Opinião pública**: difusão de ideias, polarização
- **Vantagem**: testar hipóteses sem custo social
- **Mas**: validação é difícil (não há ground truth)

**Diagrama**: 3 ícones de aplicação (política, mercado, opinião)
**Animação**: Ícones surgem em sequência
**Imagem**: Ícones minimalistas
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Três grandes casos de uso. Policy: "se eu aumentar o imposto de X%, o que acontece com o consumo?" — simular antes de legislar. Mercado: agentes com orçamentos e preferências formam preços. Opinião: como uma ideia se espalha numa rede social simulada? A vantagem é testar hipóteses sem custo social. A desvantagem é brutal: você não tem ground truth. Como você sabe que a simulação está certa? Em mercado, dá para comparar com dados reais. Em opinião pública, quase impossível.
⚠️ ERROS COMUNS: Alunos querem usar simulação social para tudo. Em alta stakes (política pública real), o risco de confiar numa simulação não-validada é enorme.
➡️ TRANSIÇÃO: "Por isso precisamos falar dos limites."

---

### Slide 20 — Limites e Críticas

**Título**: Limites e Críticas das Simulações Sociais
**Objetivo**: Ser honesto sobre as limitações das simulações sociais.
**Conteúdo**:
- Agentes são muito coerentes vs humanos (menos ruído)
- Vieses dos LLMs se amplificam em sociedade
- Custo computacional (25+ agentes × N interações)
- Difícil validação (não há ground truth)
- **Pergunta**: *Uma simulação social com LLMs pode prever comportamento humano real?*

**Diagrama**: 4 ícones de limitação
**Animação**: Ícones surgem um a um
**Imagem**: Ícones em `etho-danger`
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Quatro limites sérios. Primeiro, agentes LLM são MUITO coerentes — humanos são ruidosos, erráticos, emocionais. Segundo, vieses dos LLMs (de gênero, raça, classe) se amplificam em sociedade: se todos os agentes têm o mesmo viés, a sociedade polariza. Terceiro, custo: 25 agentes × 100 interações × tokens = $. Quarto e mais profundo: validação. Sem ground truth, como você sabe que está certo?
💡 ANALOGIA: É como um simulador de voo sem comparar com voos reais. Parece realista, mas ninguém garante que está certo. Você não entra num avião pilotado por alguém treinado só em simulador não-validado.
❓ PERGUNTA PARA A TURMA: "Uma simulação social com LLMs pode prever comportamento humano real?"
⚠️ ERROS COMUNS: Alunos confiam na plausibilidade. Plausível ≠ correto. Um paper plausível pode estar errado; uma simulação plausível pode estar errada.
➡️ TRANSIÇÃO: "Vamos refletir rápido sobre isso."

---

### Slide 21 — Pergunta: Simulação = Predição?

**Título**: Simulação = Predição?
**Objetivo**: Provocar reflexão sobre o valor preditivo de simulações.
**Conteúdo**:
- "Uma simulação social com LLMs pode prever comportamento humano real?"
- V/F: "Sociedades de agentes sempre convergem."
- Discussão aberta rápida (1 min)

**Diagrama**: Caixa de discussão em `etho-warning`
**Animação**: V/F surge com bounce
**Imagem**: Ícone de balança (predição vs explicação)
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A resposta honesta: depende. Em mercados com dados reais para validar, sim — simulação tem valor preditivo. Em opinião pública sem ground truth, não — só tem valor EXPLICATIVO (gera hipóteses, não predições). E "sociedades sempre convergem" é FALSO: podem polarizar, oscilar, colapsar.
❓ PERGUNTA PARA A TURMA: Votação rápida de V/F. A maioria erra para "V" — usar como gancho didático.
⚠️ ERROS COMUNS: Convergência parece intuitiva, mas não é garantida. Reputação mal desenhada polariza. Normas rígidas podem oscilar.
➡️ TRANSIÇÃO: "Vamos praticar design de simulação."

---

### Slide 22 — Exercício Rápido: Cenário de Simulação

**Título**: Exercício — Home Office
**Objetivo**: Praticar design de simulação social.
**Conteúdo**:
- Cenário: "Simular o impacto de uma política de home office em uma empresa"
- Em duplas: definir 3 tipos de agentes, 2 normas, 1 métrica
- Qual resultado você espera? Qual pode surpreender?
- 1 min discussão

**Diagrama**: Caixa de discussão em `etho-warning`
**Animação**: Caixa surge com bounce
**Imagem**: Ícone de empresa
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: 1 minuto em duplas. O ponto é: vocês definem agentes com características diferentes (gestor, sênior, júnior), normas (reuniões síncronas só à tarde), e métrica (produtividade). O resultado esperado costuma ser "produtividade sobe". A surpresa costuma ser "júnior sem mentoria presencial cai". Essa é a emergência — você não programou "júnior sofre", mas emerge da interação.
❓ PERGUNTA PARA A TURMA: Após 1 min: "Qual dupla previu uma surpresa não-trivial?"
⚠️ ERROS COMUNS: Duplas definem métricas vagas ("satisfação"). Eu rebato: "Como um agente reporta satisfação de forma mensurável?"
➡️ TRANSIÇÃO: "Intervalo. Voltamos para a fronteira: Research Systems."
