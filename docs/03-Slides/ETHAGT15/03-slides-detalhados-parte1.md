# ETHAGT15 — Slides Detalhados + Notas do Professor (Parte 1: Slides 1-34)

> Universidade Etho · Especialização em Programação Agêntica
> Cada slide contém: título, objetivo, conteúdo, notas do professor, diagrama, animação, imagem, tempo.

---

## SEÇÃO A — Abertura (Slides 1-6 · 8 min)

---

### Slide 1 — Capa

**Título**: ETHAGT15 — Meta-Agentes & Sistemas Autoaprendentes
**Objetivo**: Identificar a aula, o professor e o contexto dentro da especialização.
**Conteúdo**:
- ETHAGT15 — Meta-Agentes & Sistemas Autoaprendentes
- Universidade Etho · Especialização em Programação Agêntica
- Fase D — Fronteira · 15 h
- Professor · Data

**Diagrama**: Logo Etho (canto sup. esquerdo) + imagem de fundo abstrata (recursão, agentes gerando agentes)
**Animação**: Fade in do título (300ms)
**Imagem**: Fundo `etho-dark` (#0F1E2D) com pattern sutil de nós e arestas que se replicam
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Bem-vindos à fronteira. Esta é ETHAGT15 — a aula onde paramos de construir agentes à mão e começamos a construir sistemas que constroem agentes. Se até agora vocês eram artesãos que esculpiam prompts, hoje vocês vão aprender a construir a oficina que esculpe os prompts automaticamente. Estamos na última fronteira da programação agêntica: meta-agentes, auto-aprendizado e otimização automática.
💡 ANALOGIA: É como aprender a construir máquinas-ferramenta. Um marceneiro faz móveis. Um engenheiro faz a máquina que faz móveis. Hoje vocês sobem um nível de abstração.
❓ PERGUNTA PARA A TURMA: "Quantos de vocês já tentaram otimizar um prompt manualmente por dias e sentiram que ainda existia uma versão melhor?" (levantar mãos)
⚠️ ERROS COMUNS: Alunos chegam achando que meta-agência é magia. Preciso deixar claro: meta-agência é engenharia com ciclos de feedback automatizados, não inteligência emergente espontânea.
➡️ TRANSIÇÃO: "Vamos começar definindo o que vocês vão conseguir fazer ao final desta aula."

---

### Slide 2 — Objetivos do Módulo

**Título**: Objetivos do Módulo
**Objetivo**: Deixar claro o que o aluno deve conseguir FAZER ao final da aula.
**Conteúdo**:
- **Objetivo geral**: Explorar a fronteira dos meta-agentes — agentes que criam, otimizam e evoluem outros agentes — com conscientização dos riscos
- **Objetivos específicos**:
  1. Definir meta-agente, strategy evolver e meta-learning para agentes
  2. Implementar um sistema onde um agente gera/configura agentes especializados
  3. Aplicar otimização automatizada de prompts e tools (DSPy, Promptbreeder)
  4. Discutir auto-aprendizado contínuo com memória acumulada (Voyager, AI Scientist)
  5. Identificar riscos (recursão, goal drift, segurança) e propor mitigações

**Diagrama**: 5 ícones representando cada objetivo (hierarquia, engrenagem, lupa, memória, escudo)
**Animação**: Objetivos aparecem um a um (on click)
**Imagem**: Ícones minimalistas em `etho-accent` (#E85D2F)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Cada objetivo é mensurável. Não é "entender meta-agentes" — é "definir", "implementar", "aplicar", "discutir", "identificar". O mais importante é o #5: vocês não saem desta aula achando que auto-aprendizado é uma bala de prata. Vocês saem sabendo onde está o perigo e como construir safety fences. Esta é a aula mais perigosa da especialização — e também a mais poderosa.
💡 ANALOGIA: É como aprender reação nuclear. Você pode gerar energia limpa para milhões — ou pode construir uma bomba. A diferença está nos controles de segurança que você implementa desde o início.
❓ PERGUNTA PARA A TURMA: "Qual desses objetivos vocês acham mais arriscado?" (deixar responder — costuma ser #3 ou #5)
⚠️ ERROS COMUNS: Alunos focam só na parte positiva (otimização automática) e ignoram os riscos. Reenfatizar que sem governance, meta-agentes são uma liability.
➡️ TRANSIÇÃO: "Vamos ver onde esta aula se encaixa no framework de competências."

---

### Slide 3 — Competências Desenvolvidas

**Título**: Competências Desenvolvidas
**Objetivo**: Conectar a aula ao Framework Etho de competências.
**Conteúdo**:

| Competência | Nível ao final | Status anterior |
|---|---|---|
| C1 Programação Agêntica | **A** (Avançado) | I em ETHAGT10 |
| C2 Multi-Agent Systems | **A** (Avançado) | I em ETHAGT10 |
| C3 MCP & Tool Use | **B** (Básico) | I em ETHAGT08 |
| C4 Agent Memory | **A** (Avançado) | I em ETHAGT05 |
| C6 Agent Security | **I** (Intermediário) | B em ETHAGT13 |

**Diagrama**: Radar chart com 5 eixos mostrando nível B/I/A
**Animação**: Radar aparece com wipe (left-to-right, 500ms)
**Imagem**: Badge visual por competência (círculos coloridos)
**Tempo**: 1 min

**Rodape**: MCP = Model Context Protocol — Protocolo de Contexto de Modelo

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esta é a aula de culminância técnica. C1 e C2 atingem Avançado aqui — vocês saem capazes de arquitetar sistemas onde agentes geram agentes. C4 também chega ao Avançado porque memória acumulada é central em auto-aprendizado. Mas o destaque é C6: Agent Security salta para Intermediário porque meta-agentes introduzem riscos novos (recursão, drift, auto-modificação) que vocês precisam saber mitigar.
💡 ANALOGIA: É como tirar o brevet de piloto comercial. Você não só voa — você é responsável por voos com passageiros. O nível de rigor sobe.
⚠️ ERROS COMUNS: Alunos acham que "Avançado em C1" significa "sei tudo". Não — significa que você consegue arquitetar, justificar e operar sistemas complexos. Há sempre mais.
➡️ TRANSIÇÃO: "Vamos ver como esta aula está estruturada para entregar essas competências."

---

### Slide 4 — Agenda

**Título**: Agenda da Aula
**Objetivo**: Mostrar o roteiro da aula com tempos estimados.
**Conteúdo**:
- **Bloco 1 (45 min)**:
  - Abertura (8 min) — objetivos, motivação, contexto
  - Meta-Agência (12 min) — definição, estratégias, arquitetura
  - Geração de Agentes (15 min) — meta-agente, templates, DEMO
  - Intervalo (5 min)
- **Bloco 2 (45 min)**:
  - Otimização Automatizada (15 min) — DSPy, Promptbreeder, Atlas
  - Auto-Aprendizado (13 min) — memória, Voyager, drift
  - Riscos e Governança (12 min) — recursão, goal drift, meta-governor
  - Fechamento (10 min) — boas práticas, quiz, Q&A

**Diagrama**: Timeline horizontal com 7 seções coloridas
**Animação**: Timeline cresce da esquerda para direita (500ms)
**Imagem**: Ícones de relógio por seção
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A aula tem uma progressão clara: primeiro entendemos o que é meta-agência, depois aprendemos a gerar agentes, depois a otimizá-los, depois a fazê-los aprender sozinhos, e por fim aprendemos a controlar os riscos. As seções D-F são onde a coisa fica séria — é onde a otimização encontra a segurança.
💡 ANALOGIA: É como um curso de pilotagem: primeiro você aprende a decolar (geração), depois a ajustar a navegação (otimização), depois a voar cego (auto-aprendizado), e por fim a pousar em emergência (governança).
⚠️ ERROS COMUNS: Alunos querem pular direto para DSPy. Resistir — sem entender a arquitetura de meta-agente, DSPy vira caixa-preta.
➡️ TRANSIÇÃO: "Vamos começar pelo porquê. Por que meta-agência agora?"

---

### Slide 5 — Motivação: A Fronteira dos Meta-Agentes

**Título**: A Fronteira dos Meta-Agentes
**Objetivo**: Criar tensão cognitiva — otimização manual não escala.
**Conteúdo**:
- Prompts e ferramentas são otimizados manualmente — escala não
- Equipe de 5 engenheiros mantendo prompts de 20 agentes → impraticável
- Cada novo domínio = novo agente manual = semanas de trabalho
- A solução: meta-agente que otimiza automaticamente
- Fronteira: agente que cria outro agente — onde está o limite?
- **Pergunta**: *Você deixaria um agente modificar o próprio prompt?*

**Diagrama**: Split — esquerda: engenheiros escrevendo prompts manualmente (lento, caótico) | direita: meta-agente gerando configs (rápido, sistemático)
**Animação**: Split — lado esquerdo aparece primeiro, depois lado direito
**Imagem**: Ícone de martelo e cinzel (esquerda) vs ícone de impressora 3D (direita)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O problema é de escala. Quando você tem 1 agente, otimizar o prompt manualmente é factível. Quando você tem 20 agentes, cada um com 3-5 prompts, cada prompt com 10 variações de teste... você está falando de centenas de configurações para manter. Humanos não conseguem explorar esse espaço sistematicamente. É aí que entra o meta-agente: um agente cujo trabalho é gerar, otimizar e evoluir outros agentes.
💡 ANALOGIA: É como a transição da agricultura de subsistência para a mecanização. Um camponês planta o suficiente para a família. Um trator planta para uma cidade. O meta-agente é o trator.
❓ PERGUNTA PARA A TURMA: "Você deixaria um agente modificar o próprio prompt?" (levantar mãos — a maioria hesita)
⚠️ ERROS COMUNS: Alunos acham que a resposta é "nunca". Mas a realidade é: empresas já estão fazendo isso em produção (DSPy, Promptbreeder). A pergunta não é "se", é "como" — com que salvaguardas.
➡️ TRANSIÇÃO: "Mas por que isso só é viável agora?"

---

### Slide 6 — Contexto: Por Que Meta-Agência Agora

**Título**: Por Que Meta-Agência Agora
**Objetivo**: Explicar a confluência histórica que tornou meta-agentes viáveis.
**Conteúdo**:
- **Linha do tempo**:
  - 2023 · DSPy (Khattab) — compilação declarativa de chamadas de LLM
  - 2023 · Voyager (Wang) — agente que aprende skills no Minecraft
  - 2023 · Promptbreeder (Fernando) — evolução de prompts
  - 2024 · Meta-Prompting (Hu) — decomposição com especialistas
  - 2024 · AI Scientist (Lu/Sakana) — pesquisa científica autônoma
  - 2025 · Adoção industrial
- **Confluência**: modelos capazes de gerar código/config + frameworks de eval + necessidade de escala
- **Paper canônico**: DSPy (arXiv:2310.03714) — "compilar" prompts

**Diagrama**: Timeline horizontal com 6 marcos
**Animação**: Marcos aparecem sequencialmente
**Imagem**: Logos/arXiv IDs de cada paper
**Tempo**: 1 min

**Rodape**: LLM = Large Language Model — Modelo de Linguagem de Grande Escala

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Três coisas convergiram. Primeiro, modelos ficaram bons o suficiente para gerar configuração declarativa (JSON, YAML, código) de forma confiável. Segundo, surgiram frameworks de avaliação que permitem medir se uma configuração gerada é boa. Terceiro, a escala de adoção tornou a otimização manual inviável. A combinação desses três fatores tornou a meta-agência não apenas viável, mas necessária. 2023 foi o ano seminal: DSPy, Voyager e Promptbreeder em meses.
💡 ANALOGIA: É como a invenção do compilador. Antes, programadores escreviam assembly à mão. O compilador automatizou a tradução. DSPy faz o mesmo para prompts: você escreve a intenção, ele compila o prompt otimizado.
⚠️ ERROS COMUNS: Alunos confundem "meta-agência" com "fine-tuning". São coisas diferentes. Fine-tuning treina pesos do modelo. Meta-agência otimiza a configuração ao redor do modelo (prompts, tools, topologia).
➡️ TRANSIÇÃO: "Agora que sabemos o porquê, vamos definir formalmente o quê."

---

## SEÇÃO B — O Que É Meta-Agência (Slides 7-14 · 12 min)

---

### Slide 7 — [SEÇÃO] O Que É Meta-Agência

**Título**: 1 — O Que É Meta-Agência
**Objetivo**: Transição para o bloco de fundamentos.
**Conteúdo**: Número "1" grande + "O Que É Meta-Agência"
**Diagrama**: Fundo `etho-primary`
**Animação**: Fade in
**Imagem**: —
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Entramos na primeira seção substantiva. Vamos definir o que é meta-agência de forma precisa, distinguir de agência comum, e apresentar as três estratégias fundamentais.
➡️ TRANSIÇÃO: "Comecemos pela definição."

---

### Slide 8 — Agentes que Operam sobre Agentes

**Título**: Agentes que Operam sobre Agentes
**Objetivo**: Definir meta-agência e distinguir de agência comum.
**Conteúdo**:
- **Agente comum**: opera sobre o ambiente (tools, APIs, dados)
- **Meta-agente**: opera sobre agentes (criar, configurar, otimizar, evoluir)
- O meta-agente é um agente cujo "ambiente" é outro agente
- Analogia: compilador é para código o que meta-agente é para agente
- **Níveis de meta**: agente → meta-agente → meta-meta-agente (cuidado com recursão)
- A recursão é tentadora mas perigosa — voltamos a isso na Seção F

**Diagrama**: Hierarquia: meta-agente (topo) → agentes (meio) → ambiente (base)
**Animação**: Níveis aparecem de cima para baixo
**Imagem**: —
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A definição chave é esta: meta-agente é um agente cujo ambiente de atuação é outro agente. Um agente comum age sobre o mundo — chama APIs, busca dados, executa código. Um meta-agente age sobre agentes — gera configuração, ajusta prompts, seleciona tools, modifica topologia. Isso é uma mudança fundamental de alvo. A analogia do compilador é poderosa: um compilador não executa seu programa, ele gera o código que será executado. Um meta-agente não executa a tarefa, ele gera o agente que executará.
💡 ANALOGIA: É a diferença entre um operário (agente) e um gerente de fábrica (meta-agente). O operário opera máquinas. O gerente configura as máquinas e decide quais operários fazerão quais tarefas.
❓ PERGUNTA PARA A TURMA: "Vocês conseguem pensar em um sistema que já usa meta-agência hoje?" (respostas comuns: AutoGPT, Cursor agent config, LangSmith otimização)
⚠️ ERROS COMUNS: Alunos acham que meta-agente precisa ser "consciente" ou "auto-aware". Não — é só um agente cujas tools operam sobre configuração de outros agentes.
➡️ TRANSIÇÃO: "Existem três estratégias fundamentais de meta-agência."

---

### Slide 9 — Estratégias: Synthesis, Evolution, Optimization

**Título**: Três Estratégias de Meta-Agência
**Objetivo**: Apresentar as 3 estratégias de meta-agência.
**Conteúdo**:
- **Synthesis**: criar um agente do zero para uma tarefa específica
  - Exemplo: meta-agente recebe "preciso de um agente de suporte para produto X"
  - Risco: médio · Reward: alto (novo agente funcional)
- **Evolution**: mutar a configuração de um agente existente
  - Exemplo: trocar modelo, adicionar tool, mudar prompt
  - Risco: baixo-médio · Reward: médio (melhoria incremental)
- **Optimization**: ajustar parâmetros finos sem mudar estrutura
  - Exemplo: otimizar prompt com DSPy, ajustar temperatura
  - Risco: baixo · Reward: baixo-médio (ajuste fino)
- Cada estratégia tem nível crescente de risco e reward
- A escolha depende do objetivo e da maturidade do sistema

**Diagrama**: 3 colunas comparativas (Synthesis / Evolution / Optimization) com ícones e níveis de risco
**Animação**: Colunas aparecem uma a uma
**Imagem**: Ícones: fábrica (synthesis), DNA (evolution), lupa/filtro (optimization)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: As três estratégias formam um espectro. Synthesis é a mais drástica — você cria um agente novo do zero. Evolution é intermediária — você pega um agente existente e muda sua configuração estrutural. Optimization é a mais sutil — você ajusta parâmetros finos (prompt, temperatura) sem mudar a estrutura. A escolha depende do problema: synthesis para novos domínios, evolution para adaptação, optimization para tuning. Importante: o risco cresce com a drasticidade. Synthesis tem maior potencial de regressão porque introduz variáveis novas.
💡 ANALOGIA: Synthesis é como construir um carro novo. Evolution é como trocar o motor. Optimization é como calibrar a injeção eletrônica. Todas são válidas, mas exigem níveis diferentes de cautela.
⚠️ ERROS COMUNS: Alunos começam por synthesis ("vamos criar um agente novo!") quando optimization resolveria. Regra: sempre tentar optimization antes de evolution, evolution antes de synthesis.
➡️ TRANSIÇÃO: "Vamos ver a arquitetura conceitual que sustenta essas estratégias."

---

### Slide 10 — Meta-Agente: Arquitetura Conceitual

**Título**: Arquitetura Conceitual do Meta-Agente
**Objetivo**: Visualizar a arquitetura de um meta-agente.
**Conteúdo**:
- tarefa T → Meta-agente → compõe primitivas (personas, tools, workflows)
- → gera config JSON → validar → passa: instanciar / falha: iterar
- → executar T
- O meta-agente usa um LLM para gerar configuração declarativa
- **Validação é crítica**: eval antes de deploy — sempre
- O loop de feedback (falha → iterar) é o que torna o sistema auto-corretivo

**Diagrama**: `12-Diagrams/ETHAGT15/meta-agent.mmd`
**Animação**: Fluxo percorre o diagrama, loop de validação destacado
**Imagem**: —
**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Este é o diagrama central da aula. Sigam comigo: a tarefa T entra no meta-agente. O meta-agente tem acesso a uma biblioteca de primitivas — personas (templates de system prompt), tools (biblioteca MCP) e workflows (padrões de orquestração). Ele compõe essas primitivas e gera uma configuração JSON declarativa. Essa config passa por validação: schema check, eval em sandbox, safety check. Se passa, o agente é instanciado e executa a tarefa. Se falha, o feedback volta para o meta-agente, que itera. Este loop de validação é o coração do sistema — é o que separa meta-agência responsável de caos.
💡 ANALOGIA: É como uma linha de montagem com controle de qualidade. O produto (config) passa por estações de inspeção (validação). Se reprova, volta para o início da linha. Sem QC, você despacha produtos defeituosos.
❓ PERGUNTA PARA A TURMA: "O que acontece se removermos a etapa de validação?" (resposta: agente gerado pode ser pior que manual, regressão silenciosa)
⚠️ ERROS COMUNS: Alunos pulam a validação "para economizar tempo". Resultado: agente gerado funciona em casos triviais mas falha em edge cases que o eval teria pegado.
➡️ TRANSIÇÃO: "Esta arquitetura não é teórica — há implementações reais."

---

### Slide 11 — Exemplos: DSPy, Voyager, Meta-Prompting, Promptbreeder

**Título**: Implementações Reais de Meta-Agência
**Objetivo**: Conectar conceito a implementações reais.
**Conteúdo**:
- **DSPy** (Khattab et al., arXiv:2310.03714): compilação declarativa — otimiza prompts automaticamente via teleprompters
- **Voyager** (Wang et al., arXiv:2305.16291): agente que aprende skills no Minecraft — auto-curriculum + skill library
- **Meta-Prompting** (Hu et al., arXiv:2311.11402): decomposição de tarefa com especialistas LLM
- **Promptbreeder** (Fernando et al., arXiv:2309.16797): evolução de prompts via mutação + seleção (algoritmo genético)
- **AI Scientist** (Lu et al., arXiv:2408.06292): conduz pesquisa científica autônoma end-to-end
- **Padrão comum**: loop de gerar → avaliar → selecionar → iterar

**Diagrama**: 5 cards com nome, ano, contribuição
**Animação**: Cards aparecem um a um
**Imagem**: Logos dos papers / instituições (Stanford, NVIDIA, DeepMind, Sakana)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Cinco papers definiram o campo. DSPy, de Khattab em Stanford, introduziu a ideia de "compilar" prompts declarativos em prompts otimizados — como um compilador otimiza código. Voyager, da NVIDIA, mostrou que um agente pode aprender skills complexas automaticamente no Minecraft. Promptbreeder, do DeepMind, aplicou algoritmos genéticos para evoluir populações de prompts. Meta-Prompting mostrou que um meta-agente pode decompor tarefas chamando especialistas. E AI Scientist, da Sakana AI, mostrou que um sistema pode conduzir pesquisa científica — de ideação a paper — autonomamente. O padrão comum a todos: gerar variações, avaliar, selecionar, iterar. É evolução aplicada a configuração.
💡 ANALOGIA: Cada um desses papers é como uma escola de pensamento na pintura renascentista. Mesmo tema (meta-agência), técnicas diferentes. DSPy é o compilador, Voyager é o autodidata, Promptbreeder é o criador evolutivo.
⚠️ ERROS COMUNS: Alunos acham que precisam escolher um. Não — você combina. Pode usar DSPy para otimizar prompts e Voyager-style skill library para acumular conhecimento.
➡️ TRANSIÇÃO: "Mas antes de mergulharmos em implementação, precisamos ser honestos sobre os trade-offs."

---

### Slide 12 — Risco vs Benefício

**Título**: Risco vs Benefício da Meta-Agência
**Objetivo**: Ser honesto sobre os trade-offs da meta-agência.
**Conteúdo**:
- **Benefícios**:
  - Escala: otimizar 100 agentes automaticamente
  - Adaptação: ajustar a mudanças de domínio sem intervenção manual
  - Descoberta: encontrar configurações que humanos não pensariam
  - Velocidade: de semanas para horas
- **Riscos**:
  - Perda de controle: agente otimiza métrica errada (goal drift)
  - Recursão: loops de auto-modificação sem convergência
  - Opacidade: difícil entender por que a config é assim
  - Drift: otimizando para ambiente antigo
  - Segurança: agente remove suas próprias constraints

**Diagrama**: Balança: benefícios (esquerda, verde) vs riscos (direita, vermelho)
**Animação**: Balança inclina para cada lado conforme itens aparecem
**Imagem**: Ícone de balança da justiça
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Precisamos encarar os trade-offs de frente. Do lado dos benefícios: escala absurda (otimizar centenas de agentes em paralelo), adaptação automática a mudanças de domínio, descoberta de configurações contraintuitivas que humanos não encontrariam, e velocidade — o que levava semanas agora leva horas. Mas do lado dos riscos: perda de controle quando a métrica diverge do objetivo, recursão descontrolada quando o agente se modifica, opacidade (por que o prompt ficou assim?), drift para ambientes obsoletos, e o mais perigoso — um agente que remove suas próprias constraints de segurança. A pergunta não é "usar ou não usar meta-agentes". É "usar com quais salvaguardas".
💡 ANALOGIA: É como energia nuclear. Pode iluminar cidades ou devastá-las. A física é a mesma. A diferença são os controles de segurança.
❓ PERGUNTA PARA A TURMA: "Qual desses riscos vocês acham mais difícil de mitigar?" (deixar responder — opacidade e goal drift são comuns)
⚠️ ERROS COMUNS: Alunos focam só nos benefícios na empolgação. Reenfatizar: toda implementação de meta-agente precisa de um meta-governor (voltamos a isso na Seção F).
➡️ TRANSIÇÃO: "Vamos exercitar o pensamento crítico com uma pergunta provocativa."

---

### Slide 13 — Pergunta: Você Deixaria um Agente Modificar o Próprio Prompt?

**Título**: Você Deixaria?
**Objetivo**: Engajar a turma com uma pergunta provocativa sobre auto-modificação.
**Conteúdo**:
- "Você deixaria um agente modificar o próprio prompt?"
- **Votação**: sim / não / depende
- "Em que condições você aceitaria?"
  - Sandbox isolado?
  - Com eval rigoroso antes de aplicar?
  - Com aprovação humana?
- "Quem audita as mudanças?"
- Discussão aberta (2 min)

**Diagrama**: Caixa de votação (sim/não/depende) com barras
**Animação**: Barras crescem conforme votação
**Imagem**: Ícone de urna
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esta é a pergunta central ética desta aula. A maioria das pessoas responde "depende" — e está certo. A resposta certa é: sim, desde que haja (1) sandbox, (2) eval rigoroso, (3) meta-governor com vetos, (4) versionamento e rollback, (5) HITL para mudanças críticas. Sem essas cinco salvaguardas, a resposta é não. A questão não é ideológica — é de engenharia de segurança. Promptbreeder e DSPy já fazem auto-modificação de prompt em produção. A pergunta é como, não se.
💡 ANALOGIA: É como perguntar "você deixaria um piloto de avião ajustar a rota durante o voo?". Sim — desde que haja regras de tráfego aéreo, torre de controle, e procedimentos de emergência.
❓ PERGUNTA PARA A TURMA: "Votem: sim, não ou depende?" (contar mãos — anotar resultado para retomar no Slide 54)
⚠️ ERROS COMUNS: Alunos respondem "nunca" por medo. Mas a realidade do mercado é que a concorrência está fazendo. O que não pode fazer é fazer sem governança.
➡️ TRANSIÇÃO: "Vamos praticar identificação de meta-agência."

---

### Slide 14 — Exercício Rápido: Identificar Meta-Agência

**Título**: É Meta-Agência ou Não?
**Objetivo**: Praticar identificação de meta-agência em cenários.
**Conteúdo**:
- 4 cenários — quais são meta-agência?
  1. Agente que escreve código Python → **NÃO** (agência comum)
  2. Agente que gera prompt para outro agente → **SIM** (synthesis)
  3. Agente que ajusta sua própria temperatura → **SIM** (optimization)
  4. Agente que busca na web → **NÃO** (agência comum)
- Votação rápida (1 voto por cenário)

**Diagrama**: 4 cards com cenários e ícones SIM/NÃO
**Animação**: Cards aparecem, depois revelam resposta
**Imagem**: —
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Exercício rápido para fixar a definição. A regra é simples: se o agente opera sobre agentes (gera, configura, otimiza outro agente), é meta-agência. Se opera sobre o ambiente (código, web, APIs), é agência comum. Cenário 1: escrever código é agir sobre o ambiente. Cenário 2: gerar prompt para outro agente é synthesis. Cenário 3: ajustar própria temperatura é optimization (modifica configuração de agente). Cenário 4: buscar na web é agir sobre ambiente. A pegadinha é o 3 — muita gente acha que não é meta-agência porque é "só um parâmetro". Mas ajustar configuração de agente É meta-agência, mesmo que trivial.
💡 ANALOGIA: É como distinguir "jogar futebol" (agência comum) de "ser técnico de futebol" (meta-agência). O técnico não joga, ele configura o time.
❓ PERGUNTA PARA A TURMA: "Votem em cada cenário: meta-agência ou não?" (votação rápida, revelar respostas)
➡️ TRANSIÇÃO: "Com a definição clara, vamos para a primeira estratégia na prática: geração de agentes."

---

## SEÇÃO C — Geração de Agentes (Slides 15-24 · 15 min)

---

### Slide 15 — [SEÇÃO] Geração de Agentes

**Título**: 2 — Geração de Agentes
**Objetivo**: Transição para geração de agentes.
**Conteúdo**: "2 — Geração de Agentes"
**Diagrama**: Fundo `etho-primary`
**Animação**: Fade in
**Imagem**: —
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Entramos na estratégia de synthesis. Vamos ver como um meta-agente gera agentes especializados do zero, como usar templates para reuso, e como validar o agente gerado.
➡️ TRANSIÇÃO: "Comecemos pelo mecanismo de geração."

---

### Slide 16 — Meta-Agente que Produz Agentes

**Título**: Meta-Agente que Produz Agentes
**Objetivo**: Detalhar como um meta-agente gera agentes especializados.
**Conteúdo**:
- **Input**: descrição de tarefa ("preciso de um agente que responda dúvidas de produto X")
- **Output**: config completa (system prompt, tools, modelo, parâmetros)
- O meta-agente usa **primitivas reutilizáveis**:
  - **Personas**: template de system prompt
  - **Tools**: biblioteca de tools MCP
  - **Workflows**: padrões de orquestração
- **Composição**: selecionar primitivas + instanciar + configurar
- O meta-agente não "inventa" do zero — ele compõe a partir de uma biblioteca

**Diagrama**: Input → meta-agente → primitivas → config → agente especializado
**Animação**: Fluxo esquerda → direita
**Imagem**: Ícones de peças de LEGO (composição)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O segredo da geração é que o meta-agente não parte do zero. Ele tem acesso a uma biblioteca de primitivas: personas (templates de system prompt para diferentes papéis — suporte, vendas, QA, etc.), tools (uma biblioteca MCP com tools catalogadas por domínio) e workflows (padrões de orquestração como routing, parallelization, evaluator-optimizer). Dada uma tarefa, o meta-agente seleciona as primitivas relevantes, instancia com parâmetros específicos, e gera uma configuração JSON completa. É composição, não criação ex nihilo. Isso torna o processo auditável: você sabe quais primitivas foram usadas e pode versioná-las.
💡 ANALOGIA: É como um chef que tem uma despensa com ingredientes pré-preparados (molhos, massas, temperos). Ele não colhe trigo — ele combina ingredientes da despensa para criar pratos. A desposa é a biblioteca de primitivas.
⚠️ ERROS COMUNS: Alunos acham que o meta-agente precisa "gerar código do zero". Não — gerar JSON declarativo que referencia primitivas é mais seguro e auditável que gerar código executável arbitrário.
➡️ TRANSIÇÃO: "Templates são o que tornam isso reutilizável."

---

### Slide 17 — Templates e Composição

**Título**: Templates e Composição
**Objetivo**: Mostrar como templates tornam a geração reutilizável.
**Conteúdo**:
- **Template** = configuração parametrizada de um agente
- Exemplo: `SupportAgentTemplate(product, knowledge_base, escalation_policy)`
- **Composição**: combinar templates (agente de suporte + agente de QA)
- **Biblioteca de templates**: catálogo versionado de padrões
- **Vantagens**: reuso, consistência, auditabilidade
- **Desafio**: manter templates atualizados com mudanças de domínio

**Diagrama**: Biblioteca de templates → composição → agente final
**Animação**: Templates entram como blocos, saem como agente composto
**Imagem**: Ícones de blocos de montar
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Templates são o mecanismo de reuso. Em vez de o meta-agente gerar cada agente do zero, ele instancia templates parametrizados. Um template de SupportAgent tem parâmetros como produto, base de conhecimento e política de escalonamento. O meta-agente preenche os parâmetros com valores específicos da tarefa. Templates podem ser compostos: um agente de suporte + um agente de QA formam um sistema multi-agente. A biblioteca de templates é versionada — você sabe qual versão de template gerou qual agente. O desafio é manutenção: quando o domínio muda, os templates precisam ser atualizados.
💡 ANALOGIA: É como uma cozinha industrial com receitas padronizadas. Cada receita é um template. O chef (meta-agente) seleciona receitas, ajusta porções (parâmetros), e produz pratos consistentes em escala.
⚠️ ERROS COMUNS: Alunos criam templates genéricos demais ("AgenteTemplate"). Templates precisam ser específicos de domínio para serem úteis.
➡️ TRANSIÇÃO: "Vamos ver o pipeline completo de geração."

---

### Slide 18 — Pipeline de Geração

**Título**: Pipeline de Geração de Agentes
**Objetivo**: Visualizar o pipeline completo de geração de agentes.
**Conteúdo**:
- **Passo 1**: Interpretar tarefa (LLM analisa descrição)
- **Passo 2**: Selecionar primitivas (da biblioteca)
- **Passo 3**: Gerar config (JSON declarativo)
- **Passo 4**: Validar (schema check + eval em sandbox)
- **Passo 5**: Instanciar (criar agente executável)
- **Passo 6**: Deploy (com confiança incremental)
- Falha em qualquer passo → feedback → iterar

**Diagrama**: Pipeline horizontal com 6 passos + loop de feedback
**Animação**: Passos se preenchem sequencialmente, loop destacado em falha
**Imagem**: Ícones de esteira de montagem
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O pipeline tem 6 passos. Primeiro, o meta-agente interpreta a tarefa — usa um LLM para analisar a descrição e entender o que é preciso. Segundo, seleciona primitivas da biblioteca — quais personas, tools e workflows são relevantes. Terceiro, gera a configuração JSON declarativa. Quarto — e este é o passo crítico — valida: verifica o schema (a config é bem-formada?), roda eval em sandbox (passa nos casos de teste?), e faz safety check (não viola políticas?). Quinto, instancia o agente executável. Sexto, faz deploy com confiança incremental (sandbox → shadow → canary → produção). Em qualquer passo, se falha, o feedback volta para o meta-agente iterar. É um pipeline com QC embutido.
💡 ANALOGIA: É como uma fábrica com esteira de montagem e estações de inspeção. Cada peça é verificada antes de avançar. Se reprova, volta para retrabalho.
❓ PERGUNTA PARA A TURMA: "Qual passo vocês acham que consome mais tempo?" (resposta: validaçãolhe passo 4 — eval é o gargalo)
⚠️ ERROS COMUNS: Alunos subestimam o passo 4. Geração é rápida (segundos); validação é lenta (minutos a horas). O eval é o novo bottleneck.
➡️ TRANSIÇÃO: "Vamos aprofundar na validação."

---

### Slide 19 — Validação do Agente Gerado

**Título**: Validação do Agente Gerado
**Objetivo**: Enfatizar que validação é crítica antes de deploy.
**Conteúdo**:
- "Confie, mas verifique" — agent generated ≠ agent good
- **Validação automática**:
  - Schema check (config é válida?)
  - Eval em subset de casos de teste (passa nos critérios?)
  - Safety check (não viola políticas?)
- **Validação humana**:
  - Review da config gerada
  - Aprovação para mudanças críticas
- Sem validação: agente pode ser pior que o manual
- **Pergunta**: *Como garantir que o agente gerado não é pior que o manual?*

**Diagrama**: Funil de validação: schema → eval → safety → review → deploy
**Animação**: Funil filtra de cima para baixo
**Imagem**: Ícone de funil/peneira
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Validação tem três camadas automáticas e uma humana. Schema check verifica se a config é bem-formada — campos obrigatórios presentes, tipos corretos. Eval roda o agente em um subset de casos de teste e mede success rate — se for abaixo do threshold (ex.: 90%), reprova. Safety check verifica se a config não viola políticas — não removeu constraints de segurança, não aumentou custo além do limite, não usa modelo não-aprovado. Por fim, validação humana: para mudanças críticas, um humano revisa a config antes de aprovar. Sem essas camadas, você está deployando código não-testado — em produção.
💡 ANALOGIA: É como controle de qualidade em fábrica de remédios. Cada lote passa por testes de pureza, dosagem e segurança antes de ir para a farmácia. Sem isso, você vende placebo — ou veneno.
❓ PERGUNTA PARA A TURMA: "Como garantir que o agente gerado não é pior que o manual?" (resposta: benchmark comparativo — rode ambos no mesmo eval)
⚠️ ERROS COMUNS: Alunos acham que "gerado por LLM" significa "bom". Não — LLM gera config plausível, não necessariamente boa. Eval é o árbitro.
➡️ TRANSIÇÃO: "Vamos ver um caso prático."

---

### Slide 20 — Caso: Agentes de Suporte por Produto

**Título**: Caso Prático — Suporte por Produto
**Objetivo**: Mostrar um caso prático de geração.
**Conteúdo**:
- Empresa com 10 produtos, cada um precisa de agente de suporte
- **Manual**: 10 engenheiros × 2 semanas = 20 semanas
- **Com meta-agente**: 1 engenheiro + meta-agente × 2 dias = 2 dias
- Meta-agente recebe: descrição do produto + KB + política de escalonamento
- Gera: system prompt + tools (search_kb, escalate, create_ticket) + config
- Validação: 50 casos de teste por produto → aprovação automática se >90%
- **Resultado**: 10 agentes em 2 dias, 92% de precisão média

**Diagrama**: Antes (10 engenheiros, 20 semanas) vs Depois (1 engenheiro, 2 dias)
**Animação**: Comparação lado a lado
**Imagem**: Ícones de equipe (esquerda) vs engrenagem + humano (direita)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Caso concreto para materializar o ganho. Uma empresa com 10 produtos precisa de um agente de suporte para cada. Manualmente: 10 engenheiros, 2 semanas por agente, 20 semanas no total. Com meta-agente: 1 engenheiro supervisiona o meta-agente, que gera configs para os 10 produtos em 2 dias. Cada config inclui system prompt específico do produto, tools relevantes (busca na KB, escalonamento, criação de ticket) e parâmetros. A validação roda 50 casos de teste por produto — se passa >90%, deploy automático. Resultado: 10 agentes em 2 dias com 92% de precisão média. O ganho não é só velocidade — é consistência (todos os agentes seguem o mesmo padrão).
💡 ANALOGIA: É como a diferença entre costurar 10 camisas à mão vs usar uma máquina de costura industrial. A máquina não substitui o designer — ela amplifica a produtividade.
⚠️ ERROS COMUNS: Alunos acham que o meta-agente elimina o engenheiro. Não — o engenheiro muda de papel: de escritor de prompts para curador de primitivas e supervisor de eval.
➡️ TRANSIÇÃO: "Agora vamos ver isso rodando ao vivo."

---

### Slide 21 — DEMO: Agente que Escreve Agente

**Título**: DEMO — Agente que Escreve Agente
**Objetivo**: Demo ao vivo — meta-agente que gera um agente especializado.
**Conteúdo**:
- Código do `05-Labs/ETHAGT15/Lab1-Agente-que-Escreve-Agente`
- **Input**: "preciso de um agente que classifique tickets de suporte"
- Meta-agente gera: system prompt + tool de classificação + config
- Avalia o agente gerado em 3 casos de teste
- Mostra resultado: aprovado/reprovado → itera se necessário
- Terminal: meta-agente → config JSON → eval → deploy

**Diagrama**: Code block + terminal side-by-side
**Animação**: Highlight de linhas chave; terminal mostra geração e eval
**Imagem**: Screenshot do terminal com saída colorida
**Tempo**: 5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esta é a DEMO central. Eu vou rodar o Lab 1 ao vivo. O input é simples: "preciso de um agente que classifique tickets de suporte em: bug, feature request, dúvida, elogio". O meta-agente vai: interpretar a tarefa, selecionar primitivas (persona de classificador, tool de classificação), gerar a config JSON, validar (schema + eval em 3 casos), e mostrar o resultado. Se passar, deploy. Se falhar, itera. Vocês vão ver o ciclo completo em 5 minutos. Prestem atenção em três coisas: (1) a config gerada é legível e auditável, (2) o eval é o árbitro — não a intuição, (3) o loop de iteração é automático mas supervisionado.
💡 ANALOGIA: É como ver um chef preparar um prato ao vivo. A receita (config) é visível, o teste de sabor (eval) é explícito, e se o prato reprova, o chef ajusta.
❓ PERGUNTA PARA A TURMA: "O que vocês observaram no processo?" (deixar comentarem antes de avançar)
⚠️ ERROS COMUNS: Se a API falhar, tenho screenshot do terminal pré-gravado. Não tentar debugar ao vivo — isso quebra o ritmo.
➡️ TRANSIÇÃO: "Vamos refletir sobre a DEMO."

---

### Slide 22 — Pergunta da DEMO

**Título**: Perguntas sobre a DEMO
**Objetivo**: Engajar a turma com perguntas sobre a demo.
**Conteúdo**:
- "O agente gerado é pior que um agente escrito manualmente?"
- "Como sabemos que o eval cobre casos suficientes?"
- "E se o meta-agente gerar uma config que funciona no eval mas falha em produção?"
- Discussão em duplas (2 min)

**Diagrama**: Caixa de discussão
**Animação**: Perguntas aparecem uma a uma
**Imagem**: Ícone de balão de diálogo
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Três perguntas para discussão em duplas. A primeira: o agente gerado é pior? Resposta honesta — às vezes sim, às vezes não. Depende da qualidade das primitivas e do eval. A segunda: como saber que o eval é suficiente? Resposta: você nunca sabe com certeza — por isso confiança incremental (sandbox → shadow → canary). A terceira é a mais importante: overfitting ao eval. Se o meta-agente otimiza para passar no eval, pode falhar em produção. Solução: holdout set que o meta-agente não vê, e monitoramento em produção.
💡 ANALOGIA: É como um estudante que decora provas anteriores mas não entende a matéria. Passa no simulado, reprova na prova real. O eval é o simulado — precisa ser representativo.
❓ PERGUNTA PARA A TURMA: "Em duplas, 2 minutos: qual é a sua maior preocupação com a DEMO que vimos?" (deixar discutir, depois compartilhar 2-3 respostas)
➡️ TRANSIÇÃO: "Vamos formalizar critérios de qualidade."

---

### Slide 23 — Exercício: Como Garantir Qualidade

**Título**: Critérios de Qualidade para Agentes Gerados
**Objetivo**: Praticar critérios de qualidade para agentes gerados.
**Conteúdo**:
- Em duplas: listar 5 critérios de qualidade para um agente gerado
- Exemplos: success rate, latência, custo, safety, robustez a edge cases
- **Bônus**: como detectar overfitting ao eval?
- 2 min listar, 1 min compartilhar

**Diagrama**: Caixa de exercício com checkbox
**Animação**: Checklist cresce
**Imagem**: Ícone de checklist
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Exercício rápido para fixar critérios. Em duplas, listem 5 critérios para avaliar se um agente gerado é bom. Pensem além de "acertou?". Critérios importantes: success rate (acertou?), latência (quão rápido?), custo (quanto custou?), safety (não violou políticas?), robustez (lida com edge cases?), consistência (comportamento previsível?), auditabilidade (dá para entender por que fez isso?). O bônus é overfitting ao eval — como detectar? Resposta: holdout set, testes fora da distribuição de treino, monitoramento em produção.
💡 ANALOGIA: É como avaliar um funcionário. Não é só "entregou?" — é "como entregou, quanto custou, e como se comportou sob pressão".
❓ PERGUNTA PARA A TURMA: "Em duplas, 2 minutos. Depois compartilho 2 listas." (cronometrar)
➡️ TRANSIÇÃO: "Vamos sintetizar as lições da geração."

---

### Slide 24 — Lições da Geração

**Título**: Lições da Geração de Agentes
**Objetivo**: Sintetizar os aprendizados da geração de agentes.
**Conteúdo**:
- Geração é rápida, mas **validação é o gargalo**
- Eval de qualidade é mais importante que velocidade de geração
- Templates reduzem variabilidade e aumentam reuso
- Comece com domínio estreito, expanda gradualmente
- Human-in-the-loop para mudanças críticas
- A config gerada deve ser auditável e versionada

**Diagrama**: 6 ícones com as lições
**Animação**: Ícones aparecem um a um
**Imagem**: —
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Seis lições para levar. Primeira: geração é rápida, validação é lenta — planejem tempo para eval. Segunda: qualidade do eval > velocidade de geração. Terceira: templates são seu melhor amigo para consistência e reuso. Quarta: comecem com domínio estreito (um produto, uma tarefa) antes de generalizar. Quinta: HITL é obrigatório para mudanças críticas. Sexta: versionem tudo — config, templates, evals. Se não for auditável, não é production-ready.
💡 ANALOGIA: É como cozinhar para um restaurante. A receita (config) precisa ser reproduzível, o controle de qualidade (eval) precisa ser rigoroso, e cada prato precisa ser rastreável (versionamento).
➡️ TRANSIÇÃO: "Encerramos o Bloco 1. Intervalo de 5 minutos. Voltamos para otimização automatizada com DSPy."

---

## SEÇÃO D — Otimização Automatizada (Slides 25-34 · início do Bloco 2)

---

### Slide 25 — [SEÇÃO] Otimização Automatizada

**Título**: 3 — Otimização Automatizada
**Objetivo**: Transição para otimização.
**Conteúdo**: "3 — Otimização Automatizada"
**Diagrama**: Fundo `etho-primary`
**Animação**: Fade in
**Imagem**: —
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Entramos na estratégia de optimization. Vamos ver DSPy (compilação declarativa), Promptbreeder (evolução), Atlas/OPRO/TextGrad (outras abordagens), otimização de tools e topologia.
➡️ TRANSIÇÃO: "Comecemos pelo porquê."

---

### Slide 26 — Por Que Otimizar Automaticamente?

**Título**: Por Que Otimizar Automaticamente?
**Objetivo**: Justificar a necessidade de otimização automatizada.
**Conteúdo**:
- Prompts manuais: arte, não ciência — dependem de intuição humana
- Humanos são ruins em explorar espaço de prompts sistematicamente
- Otimização automática: explora centenas de variações em horas
- Encontra configurações que humanos não pensariam
- **Reprodutível**: mesma otimização → mesmo resultado
- **Escala**: otimizar 100 agentes em paralelo

**Diagrama**: Espaço de busca humano (poucos pontos dispersos) vs automático (grade densa)
**Animação**: Grade densa aparece sobreposta aos pontos esparsos
**Imagem**: Gráfico de dispersão
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Por que automatizar? Três razões. Primeira: humanos são ruins em explorar o espaço de prompts sistematicamente. Você tenta 5 variações, escolhe a melhor, e para. Mas o espaço tem milhares de combinações. Segunda: reprodutibilidade. Otimização manual não é reprodutível — depende de quem fez, do humor, do dia. Otimização automática é determinística (dado o mesmo seed). Terceira: escala. Você consegue otimizar 100 agentes em paralelo — impossível manualmente. O argumento não é "humanos são ruins". É "humanos não conseguem explorar esse espaço eficientemente em escala".
💡 ANALOGIA: É como a diferença entre prospectar ouro com peneira vs com radar geológico. A peneira acha ouro onde você procura. O radar mapeia todo o terreno.
⚠️ ERROS COMUNS: Alunos acham que otimização automática substitui o humano. Não — ela amplia a busca. O humano define a métrica e os constraints; a máquina explora.
➡️ TRANSIÇÃO: "Vamos conhecer o framework canônico: DSPy."

---

### Slide 27 — DSPy: Compilação Declarativa

**Título**: DSPy — Compilação Declarativa
**Objetivo**: Apresentar DSPy como framework de otimização.
**Conteúdo**:
- **DSPy**: "compilar" chamadas declarativas de LLM em prompts otimizados
- Analogia: DSPy é para prompts o que um compilador é para código
- Você escreve o **QUE** quer (assinatura), DSPy gera o **COMO** (prompt)
- Assinatura: `question -> answer` (declarativo)
- DSPy escolhe: few-shot examples, formato, instruções
- Fonte: Khattab et al., arXiv:2310.03714

**Diagrama**: Código declarativo → DSPy compiler → prompt otimizado
**Animação**: Fluxo esquerda → direita
**Imagem**: Logo DSPy (Stanford)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: DSPy é o paper canônico desta área. A ideia é revolucionária na sua simplicidade: em vez de escrever prompts manualmente, você escreve uma assinatura declarativa — `question -> answer` — e o DSPy "compila" essa assinatura em um prompt otimizado. O compilador escolhe few-shot examples, formato, instruções. É exatamente como um compilador: você escreve em alto nível (C), ele gera em baixo nível (assembly). Aqui: você escreve a intenção, ele gera o prompt. Isso separa o "o que" do "como" — você foca na lógica, DSPy foca na otimização. Paper: Khattab et al., arXiv:2310.03714.
💡 ANALOGIA: É como escrever SQL vs escrever o plano de execução manualmente. Você escreve "SELECT * FROM users WHERE age > 18" e o otimizador escolhe o índice. DSPy faz o mesmo: você escreve a assinatura, ele escolhe o prompt.
❓ PERGUNTA PARA A TURMA: "Quem aqui já passou dias ajustando few-shot examples manualmente?" (levantar mãos)
⚠️ ERROS COMUNS: Alunos acham que DSPy é "mais um framework de prompts". Não — é uma mudança de paradigma. De imperativo (escrever o prompt) para declarativo (escrever a intenção).
➡️ TRANSIÇÃO: "Vamos ver como o DSPy funciona por dentro."

---

### Slide 28 — DSPy: Como Funciona (Teleprompters)

**Título**: DSPy — Teleprompters
**Objetivo**: Detalhar o mecanismo de otimização do DSPy.
**Conteúdo**:
- **Teleprompter** = otimizador do DSPy
- **BootstrapFewShot**: seleciona melhores exemplos de treino
- **MIPRO**: otimiza instruções + exemplos via busca bayesiana
- **Processo**:
  1. Definir assinatura e métrica
  2. Fornecer dados de treino
  3. Teleprompter explora variações
  4. Avalia cada variação na métrica
  5. Retorna melhor config
- Resultado: prompt otimizado sem intervenção humana manual

**Diagrama**: Fluxo: assinatura + dados → teleprompter → prompt otimizado
**Animação**: Fluxo percorre as etapas
**Imagem**: Ícone de engrenagem (teleprompter)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O coração do DSPy é o teleprompter — o otimizador. Existem vários. BootstrapFewShot é o mais simples: ele roda o programa em dados de treino, identifica quais exemplos levaram a sucesso, e os adiciona como few-shot. MIPRO é mais sofisticado: otimiza tanto as instruções quanto os exemplos usando busca bayesiana — ele explora o espaço de prompts de forma inteligente, não aleatória. O processo é: você define a assinatura (`question -> answer`), define uma métrica (ex.: exatidão), fornece dados de treino. O teleprompter explora variações, avalia cada uma, e retorna a melhor config. O resultado é um prompt otimizado sem que você escrevesse uma linha dele manualmente.
💡 ANALOGIA: É como um tuner de carros. Você fornece o carro (assinatura) e a pista (dados). O tuner ajusta injeção, aerodinâmica, pneus (instruções, exemplos) para maximizar a velocidade (métrica). Você não ajusta nada manualmente — o tuner faz a busca.
⚠️ ERROS COMUNS: Alunos confundem teleprompter com fine-tuning. Fine-tuning treina pesos. Teleprompter otimiza a config ao redor (prompts, exemplos). São ortogonais — pode combinar.
➡️ TRANSIÇÃO: "Mas DSPy não é a única abordagem. Vamos ver Promptbreeder."

---

### Slide 29 — Promptbreeder: Evolução de Prompts

**Título**: Promptbreeder — Evolução de Prompts
**Objetivo**: Apresentar Promptbreeder como abordagem evolutiva.
**Conteúdo**:
- **Promptbreeder**: prompts "reproduzem" e "mutam"
- População inicial de prompts → mutação (LLM reescreve) → seleção (eval)
- Gerações sucessivas: prompts melhoram com evolução
- Analogia: algoritmo genético onde genes = palavras do prompt
- Mutação exemplo: "Responda a pergunta" → "Você é um especialista. Responda com precisão."
- Fonte: Fernando et al., arXiv:2309.16797

**Diagrama**: Ciclo evolutivo: população → mutação → seleção → nova população
**Animação**: Ciclo gira
**Imagem**: Ícone de DNA + prompt
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Promptbreeder, do DeepMind, toma uma abordagem diferente de DSPy. Em vez de busca bayesiana, usa evolução. Você começa com uma população de prompts (variações iniciais). Cada geração, um LLM "muta" os prompts — reescreve, reformula, adiciona contexto. Os prompts mutados são avaliados em uma métrica. Os melhores sobrevivem e reproduzem; os piores morrem. Geração após geração, os prompts evoluem. É algoritmo genético aplicado a prompts. A mutação é inteligente — não é aleatória, é guiada por LLM. Paper: Fernando et al., arXiv:2309.16797. O resultado é fascinante: prompts evoluídos chegam a phrasing que humanos não escreveriam, mas que performam melhor.
💡 ANALOGIA: É como seleção natural em uma fazenda. Você cruza as melhores plantas, descarta as piores, e após várias gerações tem uma variedade superior. Aqui as "plantas" são prompts.
⚠️ ERROS COMUNS: Alunos acham que evolução é "aleatória". Não — mutação é guiada por LLM, e seleção é dirigida por métrica. É evolução direcionada, não deriva genética.
➡️ TRANSIÇÃO: "Existem outras abordagens. Vamos ver um panorama."

---

### Slide 30 — Atlas e Outras Abordagens

**Título**: Panorama de Otimização
**Objetivo**: Panorama de outras ferramentas de otimização.
**Conteúdo**:
- **Atlas**: otimização guiada por árvore de pensamentos
- **OPRO** (Google): otimização de prompts via meta-prompting
- **TextGrad**: gradientes de texto para otimizar prompts
- **Padrão comum**: gerar variações → avaliar → selecionar → iterar
- **Diferença principal**: estratégia de busca (greedy, evolutiva, bayesiana)
- Escolha depende: orçamento de eval, tamanho do espaço, tempo

**Diagrama**: Tabela comparativa: DSPy vs Promptbreeder vs Atlas vs OPRO vs TextGrad
**Animação**: Tabela revela colunas
**Imagem**: Logos das ferramentas
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Existem várias abordagens além de DSPy e Promptbreeder. Atlas usa árvore de pensamentos para guiar a busca — explora ramificações de prompts e poda as piores. OPRO, do Google, usa meta-prompting — um LLM gera candidatos a prompt baseado em exemplos de sucesso/falha. TextGrad, mais recente, aplica a ideia de gradientes ao texto — retropropaga feedback textual através de um pipeline de LLM. Todas seguem o mesmo padrão: gerar variações, avaliar, selecionar, iterar. A diferença é a estratégia de busca: DSPy usa bayesiana (MIPRO), Promptbreeder usa evolutiva, OPRO usa LLM-guided, TextGrad usa gradiente. A escolha depende do orçamento de eval (OPRO é barato), do tamanho do espaço (Promptbreeder explora mais) e do tempo (DSPy é rápido).
💡 ANALOGIA: É como diferentes algoritmos de busca em xadrez. Minimax, alpha-beta, MCTS — todos resolvem o mesmo problema com estratégias diferentes. Aqui é o mesmo: otimizar prompts, com estratégias de busca diferentes.
⚠️ ERROS COMUNS: Alunos querem saber "qual é o melhor". Não há melhor — depende do problema. Teste 2-3 e escolha com base no seu eval.
➡️ TRANSIÇÃO: "Mas não é só prompt que pode ser otimizado. Tools também."

---

### Slide 31 — Otimização de Tools (Reescrita de Descrições)

**Título**: Otimização de Tools
**Objetivo**: Mostrar que tools também podem ser otimizadas.
**Conteúdo**:
- **Tool description** afeta diretamente quando e como o modelo a chama
- Descrição ruim → modelo não chama ou chama errado
- **Otimização**: reescrever descrições baseada em taxa de erro
- Exemplo: "Busca documentos" → "Busca documentos na base de conhecimento interna. Use para responder perguntas sobre produtos, políticas e procedimentos."
- **Métrica**: tool call accuracy (chamou a tool certa?)
- **Loop**: medir erro → reescrever descrição → re-avaliar

**Diagrama**: Loop: descrição → eval → taxa de erro → reescrever → eval
**Animação**: Loop gira
**Imagem**: Ícone de chave inglesa + texto
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Prompts não são a única coisa otimizável. Tools também. Lembrem-se do ACI — Agent-Computer Interface — da ETHAGT01. A descrição da tool é o que o modelo usa para decidir quando chamá-la. Descrição vaga ("Busca documentos") → modelo não sabe quando chamar. Descrição rica ("Busca na base interna, use para produtos e políticas") → modelo chama na hora certa. Otimização de tools é: medir a taxa de erro de tool calls (chamou a certa?), identificar onde o modelo confunde, reescrever a descrição, re-avaliar. É o mesmo loop de otimização, aplicado a descrições de tools em vez de prompts.
💡 ANALOGIA: É como otimizar a sinalização de uma estrada. Se a placa é confusa, motoristas erram a saída. Sinalização clara → menos erros. A "descrição da tool" é a placa.
⚠️ ERROS COMUNS: Alunos focam só no prompt e ignoram tools. Mas muitas vezes o problema não é o prompt — é a descrição da tool. Meça tool call accuracy antes de mexer no prompt.
➡️ TRANSIÇÃO: "E a estrutura do sistema? Topologia também é otimizável."

---

### Slide 32 — Otimização de Topologia

**Título**: Otimização de Topologia
**Objetivo**: Apresentar otimização da estrutura do sistema multi-agente.
**Conteúdo**:
- **Topologia** = como agentes estão conectados (qual chama qual)
- Perguntas de topologia:
  - Preciso de N workers ou N-1?
  - Qual worker agrego? Qual removo?
  - Deveria ter um orchestrator ou peer-to-peer?
- **Otimização**: testar topologias alternativas em benchmark
- Exemplo: 5 workers → 3 workers + 2 especializados = mesma qualidade, menor custo
- **Desafio**: espaço de topologias é enorme (combinatório)

**Diagrama**: Topologia A (5 workers paralelos) vs Topologia B (3 + 2 especializados) com métricas
**Animação**: Topologias alternam
**Imagem**: Grafos de rede
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A otimização mais estrutural é de topologia — como os agentes estão conectados. Em um sistema multi-agente, você pode ter 5 workers paralelos. Mas será que precisa de 5? Talvez 3 workers + 2 especializados façam o mesmo com menor custo. Ou talvez um orchestrator centralizado seja melhor que peer-to-peer. A otimização de topologia testa essas alternativas em benchmark e mede custo/latência/qualidade. O desafio é que o espaço de topologias é combinatório — explosão exponencial. Por isso, otimização de topologia geralmente é guiada por heurísticas (começar com menos agentes, adicionar só se necessário) em vez de busca exaustiva.
💡 ANALOGIA: É como otimizar a organização de um time. Você tem 5 desenvolvedores. Precisa de todos em paralelo, ou 3 generalistas + 2 especialistas? A resposta depende da tarefa — e você só sabe testando.
⚠️ ERROS COMUNS: Alunos começam com topologia complexa (5+ agentes) "para ser flexível". Comece simples (1-2 agentes) e adicione só se o eval mostrar que precisa.
➡️ TRANSIÇÃO: "Vamos ver o loop de otimização visualizado."

---

### Slide 33 — Loop de Otimização

**Título**: Loop de Otimização (Strategy Evolver)
**Objetivo**: Visualizar o loop de evolução (strategy evolver).
**Conteúdo**:
- estratégia atual → gerar variações → avaliar em subset → melhor que atual?
- sim: substituir · não: manter atual
- substituir → estratégia atual (loop)
- **HITL**: audit periódico para prevenir drift
- **Padrão**: mutação + seleção + retenção = evolução

**Diagrama**: `12-Diagrams/ETHAGT15/evolution-loop.mmd`
**Animação**: Loop percorre o diagrama, HITL aparece como checkpoint
**Imagem**: —
**Tempo**: 2 min

**Rodape**: HITL = Human-in-the-Loop — Humano no Ciclo

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Este diagrama é o coração do strategy evolver. Sigam: a estratégia atual é a config em produção. O evolver gera variações (mutação — seja por DSPy, Promptbreeder ou reescrita manual). As variações são avaliadas em um subset de tarefas. Se uma variação é melhor que a atual, ela substitui. Se não, a atual se mantém. E o loop repete. O HITL aparece como audit periódico — a cada N ciclos, um humano revisa para prevenir drift. Este padrão — mutação + seleção + retenção — é evolução biológica aplicada a configuração. É poderoso, mas sem HITL pode driftar. O audit é o que mantém o sistema alinhado com o objetivo real.
💡 ANALOGIA: É como um laboratório de testes A/B contínuo. Você sempre testa variações, mantém as melhores, descarta as piores. Mas periodicamente um humano revisa se "melhor na métrica" ainda significa "melhor para o negócio".
❓ PERGUNTA PARA A TURMA: "O que acontece se o audit (HITL) for removido?" (resposta: drift silencioso — a métrica melhora mas o objetivo real diverge)
⚠️ ERROS COMUNS: Alunos acham que o loop pode rodar "para sempre" sem intervenção. Não — precisa de audit. Sem audit, drift é inevitável.
➡️ TRANSIÇÃO: "Vamos sistematizar a comparação manual vs automatizado."

---

### Slide 34 — Comparação: Manual vs Automatizado

**Título**: Manual vs Automatizado
**Objetivo**: Sistematizar os trade-offs.
**Conteúdo**:

| Eixo | Manual | Automatizado |
|---|---|---|
| Velocidade | Lento (dias/semanas) | Rápido (horas) |
| Reprodutibilidade | Não (depende do humano) | Sim (determinístico) |
| Exploração | Limitada (5-10 variações) | Ampla (centenas) |
| Custo de eval | Baixo | Alto (muitas execuções) |
| Controle | Alto (humano decide) | Médio (humano define constraints) |
| Transparência | Alta (humano entende) | Baixa (opaco) |

- **Recomendação**: automatizar para volume, manual para edge cases

**Diagrama**: Tabela comparativa colorida
**Animação**: Linhas aparecem uma a uma
**Imagem**: —
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Tabela de trade-offs. Manual é lento, não-reprodutível, explora pouco, mas é barato em eval e altamente controlável/transparente. Automatizado é rápido, reprodutível, explora muito, mas é caro em eval e mais opaco. A recomendação não é "um ou outro" — é "ambos". Automatize para volume (otimizar 100 prompts), use manual para edge cases (o 1 prompt crítico que precisa de intuição humana). O ponto de transparência é importante: otimização automatizada pode gerar prompts "estranhos" que performam bem mas são difíceis de entender. Para agentes em produção com auditoria, isso é um risco.
💡 ANALOGIA: É como cozinhar em escala. Para 1000 pratos, use máquina (automatizado). Para o prato do chef, use mãos humanas (manual). Ambos têm lugar.
➡️ TRANSIÇÃO: "Antes de avançar para auto-aprendizado, vamos discutir quando otimizar."
