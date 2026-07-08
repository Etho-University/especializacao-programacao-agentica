# ETHAGT09 — Slides Detalhados + Notas do Professor (Parte 2: Slides 37-72)

> Universidade Etho · Especialização em Programação Agêntica
> Cada slide contém: título, objetivo, conteúdo, notas do professor, diagrama, animação, imagem, tempo.

---

## SEÇÃO E — Actor Model (Slides 37-44 · continuação)

---

### Slide 37 — Princípios: Encapsulamento e Isolamento

**Título**: Princípios do Actor Model — Encapsulamento e Isolamento
**Objetivo**: Aprofundar os princípios fundamentais.
**Conteúdo**:
- **Encapsulamento**: estado do ator é inacessível externamente
- **Isolamento**: falha em um ator não derruba outros
- **"Share nothing"** — único caminho de interação é mensagem
- **Implicação para agentes**: cada agente tem estado protegido
- **Pergunta**: *Actor model vs shared state — qual é mais seguro para dados críticos?*

**Diagrama**: Caixa fechada (ator) com apenas "slot" de mensagens
**Animação**: Caixa fecha; só o slot de mensagens permanece
**Imagem**: Ícone de cofre (estado) com ranhura (mailbox)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Dois princípios definem o actor model. Encapsulamento: o estado do ator é privado. Ninguém acessa diretamente — só via mensagem. Isolamento: se um ator crasha, os outros continuam. Isso é diferente de shared state, onde um crash pode corromper o estado compartilhado. O lema é "share nothing": o único modo de interação é mensagem. Para agentes LLM, isso significa que cada agente tem seu estado protegido (memória, contexto, tools). Um agente não pode "corromper" o estado do outro.
💡 ANALOGIA: É como apartamentos em um prédio. Cada morador tem seu espaço privado (encapsulamento). Se o apartamento do vizinho pega fogo, o seu não (isolamento). A comunicação é pela portaria (mensagens), não invadindo o apartamento.
❓ PERGUNTA PARA A TURMA: "Actor model vs shared state — qual é mais seguro para dados críticos?" (Resposta: Actor model — estado encapsulado, sem race conditions. Shared state com locks é propenso a bugs.)
⚠️ ERROS COMUNS: Alunos expõem o estado do ator como atributo público "para facilitar". Isso quebra o encapsulamento e reintroduz race conditions.
➡️ TRANSIÇÃO: "Esses princípios têm uma consequência poderosa: concorrência sem locks."

---

### Slide 38 — Concorrência sem Locks

**Título**: Concorrência sem Locks
**Objetivo**: Mostrar a vantagem concorrência do actor model.
**Conteúdo**:
- **Shared state**: múltiplas threads + locks → deadlocks, race conditions
- **Actor model**: 1 mensagem por vez por ator → sem locks
- **Escala horizontalmente**: adicione mais atores
- **Trade-off**: overhead de serialização de mensagens
- **Regra**: "Don't communicate by sharing memory; share memory by communicating"

**Diagrama**: Diagrama D10 — Thread+lock vs Actor com mailbox
**Animação**: Threads brigam por lock; atores processam em paz
**Imagem**: Ícone de cadeado (lock) vs ícone de fluxo livre (actor)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A vantagem killer do actor model é concorrência sem locks. Em shared state, múltiplas threads acessam o mesmo estado — precisa de locks para evitar race conditions. Mas locks trazem deadlocks (thread A espera lock de B, B espera lock de A). No actor model, cada ator processa uma mensagem por vez. Não há estado compartilhado, não há locks, não há deadlocks. A escala é horizontal: adicione mais atores. O trade-off é o overhead de serialização (mensagens precisam ser serializadas/desserializadas). Mas em alta concorrência, o actor model escala melhor. O lema de Go é perfeito: "Don't communicate by sharing memory; share memory by communicating."
💡 ANALOGIA: Shared state = mesa compartilhada onde todos brigam pela caneta (lock). Actor model = cada um tem sua caneta, trocam recados (mensagens). Sem briga.
❓ PERGUNTA PARA A TURMA: "Qual o custo do actor model?" (Resposta: overhead de serialização de mensagens. Mas em alta concorrência, é compensado pela ausência de contenção de lock.)
⚠️ ERROS COMUNS: Alunos acham que "actor model é mais lento" por causa do overhead. Em baixa concorrência com operações simples, pode ser. Mas em alta concorrência, actor model escala melhor.
➡️ TRANSIÇÃO: "Outra vantagem: localização transparente."

---

### Slide 39 — Localização Transparente

**Título**: Localização Transparente
**Objetivo**: Explicar a vantagem de distribuição.
**Conteúdo**:
- **Ator local vs ator remoto**: mesma interface (mensagem)
- **Roteamento transparente**: framework decide para onde enviar
- **Escala**: mova atores para outros nós sem mudar código
- **Aplicação**: agentes distribuídos em múltiplos servidores
- **Pergunta**: *Como isso muda a arquitetura de deployment?*

**Diagrama**: Nós de computação com atores migrando
**Animação**: Ator migra de um nó para outro
**Imagem**: Ícone de servidores com atores se movendo
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: No actor model, um ator local e um ator remoto têm a mesma interface: você envia uma mensagem. O framework decide se a mensagem vai para a memória local ou pela rede. Isso é "localização transparente". A consequência é poderosa: você pode mover atores para outros servidores sem mudar o código. Comece com todos em uma máquina; quando precisar escalar, mova alguns para outro nó. Para LLM agents, isso significa agentes distribuídos em múltiplos servidores, coordenados por mensagens.
💡 ANALOGIA: É como ligar para um colega. Você não sabe (nem precisa saber) se ele está no escritório ou em casa — o telefone (framework) cuida do roteamento.
❓ PERGUNTA PARA A TURMA: "Como isso muda a arquitetura de deployment?" (Resposta: você pode escalar horizontalmente sem mudar o código. Adicione servidores conforme a carga cresce.)
⚠️ ERROS COMUNS: Alunos assumem que "local" e "remoto" precisam de código diferente. Não — o ponto do actor model é que a interface é a mesma.
➡️ TRANSIÇÃO: "Vamos ver implementações reais do actor model."

---

### Slide 40 — Akka / Erlang / asyncio

**Título**: Implementações do Actor Model
**Objetivo**: Mostrar implementações reais do actor model.
**Conteúdo**:
- **Erlang/OTP**: pioneiro, tolerância a falha (supervisores)
- **Akka (JVM)**: actor system para Scala/Java
- **Python asyncio**: coroutines como atores leves (sem supervisão nativa)
- Para **LLM agents**: asyncio + framework (LangGraph, AutoGen)
- **Snippet**: actor simples em asyncio

**Diagrama**: 3 colunas comparativas (Erlang, Akka, asyncio)
**Animação**: Cada coluna aparece com click
**Imagem**: Logos de Erlang, Akka, Python
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O actor model não é só teoria — tem implementações maduras. Erlang/OTP é o pioneiro: criado pela Ericsson nos anos 80 para telecom, com tolerância a falha nativa (supervisores reiniciavam atores que crashavam). Akka levou o modelo para a JVM (Scala/Java). Python asyncio não é "actor model puro" mas coroutines podem funcionar como atores leves — sem supervisão nativa. Para LLM agents, a combinação típica é asyncio + um framework (LangGraph ou AutoGen) que adiciona a camada de actor. Não reinvente a roda: use um framework.
💡 ANALOGIA: Erlang = blind-car da telecom (tolerante a falha). Akka = SUV para enterprise (JVM). asyncio = carro econômico (leve, mas você adiciona os acessórios).
⚠️ ERROS COMUNS: Alunos tentam implementar actor model do zero em Python. Use asyncio + framework. Reinventar supervision, mailbox e roteamento é trabalho desnecessário.
➡️ TRANSIÇÃO: "Como isso se aplica a agentes distribuídos?"

---

### Slide 41 — Aplicação a Agentes Distribuídos

**Título**: Actor Model para Agentes Distribuídos
**Objetivo**: Conectar actor model a sistemas multi-agente LLM.
**Conteúdo**:
- Cada agente = um ator com mailbox
- **Tool execution** = mensagem para ator especializado
- **Memória** = estado privado do ator
- **Escala**: agentes em nós diferentes, coordenados por mensagens
- **Caso de uso**: agentes de pesquisa distribuídos processando em paralelo

**Diagrama**: Topologia distribuída com agentes como atores
**Animação**: Mensagens fluem entre agentes em nós diferentes
**Imagem**: Ícone de nuvem com agentes distribuídos
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Para LLM agents, o actor model encaixa naturalmente. Cada agente é um ator: tem mailbox (recebe mensagens), estado privado (memória, contexto), e processa uma mensagem por vez. Tool execution vira mensagem para um ator especializado (ex.: ator "search" processa pedidos de busca). Memória é o estado privado do ator — protegido. A escala é distribuída: agentes em servidores diferentes, coordenados por mensagens. Caso de uso: 10 agentes de pesquisa, cada um em um nó, processando queries em paralelo, coordenados por mensagens.
💡 ANALOGIA: É como uma equipe remota. Cada membro (ator) trabalha de sua casa (nó), com seu próprio computador (estado privado), e se coordena por Slack (mensagens). Ninguém invade o computador dos outros.
⚠️ ERROS COMUNS: Alunos colocam todos os agentes em um processo "para simplificar". Isso perde a vantagem de distribuição. Use a localização transparente do actor model.
➡️ TRANSIÇÃO: "Vamos comparar actor model com shared state de forma sistemática."

---

### Slide 42 — Actor Model vs Shared State

**Título**: Actor Model vs Shared State
**Objetivo**: Sistematizar o trade-off para LLM agents.
**Conteúdo**:
- **Shared state (blackboard)**: leitura/escrita compartilhada, precisa de locks
- **Actor model**: estado isolado, mensagens assíncronas, sem locks
- **Blackboard + Actor = híbrido**: ator gerencia o blackboard
- **Pergunta**: *Verdadeiro ou falso: "Actor model é mais lento que shared-state."*
- **Resposta**: Falso — em cenários de alta concorrência, actor model escala melhor

**Diagrama**: Tabela comparativa (critério × shared state × actor model)
**Animação**: Linhas aparecem uma a uma
**Imagem**: Balança pesando as duas opções
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vamos comparar diretamente. Shared state (blackboard): múltiplos agentes leem/escritam um estado compartilhado. Precisa de locks para concorrência. Vantagem: simples de entender. Desvantagem: locks, race conditions. Actor model: cada agente tem estado isolado. Comunicação por mensagens. Sem locks. Vantagem: escala bem, sem deadlocks. Desvantagem: overhead de serialização. Mas há um híbrido: um ator gerencia o blackboard. Os agentes são atores que enviam mensagens de leitura/escrita para o blackboard-ator. Combina isolamento do actor com compartilhamento do blackboard.
💡 ANALOGIA: Shared state = cozinha compartilhada (todos mexem, precisa combinar quem usa o forno). Actor model = cada um tem sua cozinha (trocam pratos prontos). Híbrido = uma cozinha central com um chef (blackboard-ator) que atende pedidos.
❓ PERGUNTA PARA A TURMA: "V/F: Actor model é mais lento que shared-state." (Resposta: Falso. Em alta concorrência, actor model escala melhor sem locks.)
⚠️ ERROS COMUNS: Alunos tratam actor model e blackboard como excludentes. São complementares — híbridos são comuns e poderosos.
➡️ TRANSIÇÃO: "Hora da DEMO. Vamos ver duas arquiteturas resolvendo o mesmo problema."

---

### Slide 43 — DEMO: Duas Arquiteturas, um Problema

**Título**: DEMO — Duas Arquiteturas, um Problema
**Objetivo**: Demo ao vivo — mesma tarefa em 2 arquiteturas.
**Conteúdo**:
- **Tarefa**: pesquisar + resumir + formatar um relatório
- **Versão 1**: AutoGen-style group chat (agentes conversam)
- **Versão 2**: Blackboard (agentes compartilham espaço)
- **Comparar**: número de mensagens, tempo, acoplamento
- **Referência**: `05-Labs/ETHAGT09/Lab1-Duas-Arquiteturas`

**Diagrama**: Diagrama D11 — Code block + terminal side-by-side
**Animação**: Highlight de linhas chave
**Imagem**: Dois terminais lado a lado
**Tempo**: 4 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: DEMO ao vivo. Vou rodar a mesma tarefa em duas arquiteturas. Versão 1: group chat (AutoGen-style) — um manager coordena Researcher, Summarizer, Formatter conversando. Versão 2: blackboard — Researcher escreve facts, Summarizer lê e escreve summary, Formatter lê e produz relatório. Observem: número de mensagens (group chat gera mais), tempo (blackboard pode ser mais rápido com paralelismo), e acoplamento (group chat é mais acoplado ao manager). Se a API falhar, mostro traces pré-gravados.
💡 ANALOGIA: É como resolver um problema com dois métodos. Método A (group chat): reunião de equipe com facilitador. Método B (blackboard): cada um trabalha sozinho e posta no quadro. Mesmo problema, abordagens diferentes.
⚠️ ATENÇÃO: Se a DEMO falhar (API, rede), NÃO entre em pânico. Tenha screenshots dos traces prontos. A lição (comparar arquiteturas) é mais importante que o código rodando.
➡️ TRANSIÇÃO: "Vamos discutir a DEMO em duplas."

---

### Slide 44 — Pergunta da DEMO

**Título**: Discussão da DEMO
**Objetivo**: Engajar a turma com uma pergunta sobre a demo.
**Conteúdo**:
- "Qual arquitetura foi mais fácil de debugar? Por quê?"
- "Em qual delas adicionar um 4º agente seria mais simples?"
- Discussão em duplas (2 min)

**Diagrama**: Caixa de discussão com as 2 perguntas
**Animação**: Perguntas aparecem uma a uma
**Imagem**: Ícone de duplas conversando
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Pausa para discussão. Deixem 2 min em duplas. O objetivo é internalizar que a escolha de arquitetura afeta debuggability e extensibilidade. Blackboard é tipicamente mais fácil de debugar (estado centralizado) e estender (novo agente só lê/escreve o blackboard). Group chat é mais difícil de debugar (sequência de mensagens) e estender (precisa registrar no manager).
❓ PERGUNTA PARA A TURMA: Deixar discutir em duplas, depois compartilhar.
**Gabarito esperado**:
1. Blackboard — estado centralizado é fácil de inspecionar. Group chat exige rastrear sequência.
2. Blackboard — novo agente só lê/escreve. Group chat exige registrar no manager.
⚠️ ERROS COMUNS: Alunos acham que group chat é "mais flexível". Mas flexibilidade vem com custo de debuggability.
➡️ TRANSIÇÃO: "Agora vamos ao tópico mais delicado: negociação e conflito."

---

## SEÇÃO F — Negociação e Conflito (Slides 45-52 · 10 min)

---

### Slide 45 — [SEÇÃO] Negociação e Conflito

**Título**: 5 — Negociação e Conflito
**Objetivo**: Transição para negociação entre agentes.
**Conteúdo**: "5 — Negociação e Conflito"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "5" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Até agora assumimos que agentes colaboram. Mas e quando eles têm objetivos conflitantes? Negociação é o tópico central do projeto do módulo.
➡️ TRANSIÇÃO: "Por que agentes precisam negociar?"

---

### Slide 46 — Por Que Agentes Negociam

**Título**: Por Que Agentes Negociam
**Objetivo**: Motivar a necessidade de negociação.
**Conteúdo**:
- Agentes têm **objetivos próprios** — podem conflitar
- **Exemplo**: comprador quer preço baixo, vendedor quer preço alto
- **Sem negociação**: impasse ou força bruta
- **Com negociação**: convergência para acordo mutuamente aceitável
- **Pergunta**: *O que acontece quando dois agentes têm objetivos parcialmente conflitantes?*

**Diagrama**: Dois agentes com setas de tensão
**Animação**: Setas de tensão aparecem
**Imagem**: Ícone de aperto de mãos tenso
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Nem toda colaboração é harmoniosa. Agentes podem ter objetivos próprios que conflitam parcial ou totalmente. Exemplo clássico: comprador vs vendedor. O comprador quer o menor preço; o vendedor quer o maior. Sem negociação, há impasse (ninguém cede) ou força bruta (um impõe ao outro). Com negociação, há convergência: cada parte cede até encontrar uma zona de acordo. Negociação é essencial quando agentes representam interesses diferentes — ex.: agentes de departamentos diferentes disputando orçamento.
💡 ANALOGIA: É como uma negociação de salário. O candidato quer mais; a empresa quer pagar menos. Sem negociação, não há contratação. Com negociação, encontram um valor que ambos aceitam.
❓ PERGUNTA PARA A TURMA: "O que acontece quando dois agentes têm objetivos parcialmente conflitantes?" (Resposta: tensão. Sem protocolo, impasse ou escalada. Com negociação, convergência.)
⚠️ ERROS COMUNS: Alunos assumem que "agentes colaboram naturalmente". Não quando representam interesses diferentes. Negociação é necessária.
➡️ TRANSIÇÃO: "Vamos ver o primeiro padrão de negociação: bargaining."

---

### Slide 47 — Bargaining

**Título**: Bargaining — Barganha
**Objetivo**: Apresentar o padrão de barganha.
**Conteúdo**:
- **Bargaining**: proposta → contraproposta → ... → acordo ou impasse
- **Estratégias**: conceder gradativamente, fixar reserva, BATNA
- **Convergência**: cada parte cede até encontrar zona de acordo
- **Exemplo**: comprador propõe 100, vendedor contrapropõe 150, convergem em 120
- **Risco**: loops infinitos sem estratégia de cessão

**Diagrama**: Fluxo de proposta/contraproposta
**Animação**: Propostas fluem sequencialmente
**Imagem**: Ícone de balança com moedas
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Bargaining é o padrão mais comum de negociação. O fluxo é: proposta → contraproposta → ... → acordo ou impasse. Cada parte tem uma estratégia. Conceder gradativamente: "eu abaixo 5, você abaixa 5". Fixar reserva: "não vou abaixo de 100". BATNA (Best Alternative to a Negotiated Agreement): "se não fechar, tenho outra opção". A convergência acontece quando as reservas se sobrepõem — há uma zona de acordo. O risco é loop infinito se nenhuma parte cede. Por isso, estratégia de cessão é crítica.
💡 ANALOGIA: É como regatear em um mercado. O vendedor pede 200, você oferece 100. Ele desce para 180, você sobe para 120. Vocês convergem em 150. Sem ceder, não há negócio.
⚠️ ERROS COMUNS: Alunos implementam bargaining sem estratégia de cessão. Resultado: loop infinito. Sempre defina como cada parte cede.
➡️ TRANSIÇÃO: "Outro padrão: auction."

---

### Slide 48 — Auction

**Título**: Auction — Leilão
**Objetivo**: Apresentar o padrão de leilão.
**Conteúdo**:
- **Auction**: 1 vendedor, N compradores competem
- **Tipos**: English (ascendente), Dutch (descendente), sealed-bid, Vickrey
- **Quando brilha**: valor subjetivo, múltiplos interessados
- **Exemplo**: agentes competindo por recursos computacionais
- **Vencedor**: maior lance (ou segundo maior no Vickrey)

**Diagrama**: Fluxo de leilão com lances ascendentes
**Animação**: Lances sobem sequencialmente
**Imagem**: Ícone de martelo de leilão
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Auction é outro padrão de negociação. Diferente do bargaining (1-para-1), auction é 1-para-muitos: 1 vendedor, N compradores competindo. Existem tipos. English (ascendente): lances sobem até ninguém oferecer mais. Dutch (descendente): preço começa alto e desce até alguém aceitar. Sealed-bid: cada um dá um lance secreto; maior ganha. Vickrey: sealed-bid, mas o vencedor paga o segundo maior lance (incentiva lances honestos). Para agentes, auction é útil quando há recursos limitados e múltiplos interessados — ex.: agentes competindo por tempo de GPU.
💡 ANALOGIA: English = leilão de arte (sobe até ninguém oferecer mais). Dutch = florada holandesa (desce até alguém comprar). Vickrey = leilão selado onde você paga o segundo preço.
⚠️ ERROS COMUNS: Alunos não conhecem Vickrey. Vickrey é poderoso porque incentiva lances honestos — você sempre dá seu valor verdadeiro, porque paga o segundo preço.
➡️ TRANSIÇÃO: "Vamos ver o diagrama completo de negociação."

---

### Slide 49 — Negotiation Diagram

**Título**: Fluxo de Negociação
**Objetivo**: Visualizar o fluxo completo de negociação.
**Conteúdo**:
- Comprador propõe 100 → Vendedor contrapropõe 150
- Comprador propõe 120 → Vendedor aceita → acordo
- **Caminho alternativo**: rejeita após N rounds → escalar ou timeout
- Diagrama mostra **convergência e fallback**

**Diagrama**: `12-Diagrams/ETHAGT09/negotiation.mmd` (Diagrama D12)
**Animação**: Propostas fluem sequencialmente
**Imagem**: Fluxograma com branch de acordo/timeout
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vejam o diagrama completo. Comprador propõe 100. Vendedor contrapropõe 150. Comprador avalia: aceita 150? Não. Propõe 120. Vendedor avalia: aceita 120? Sim. Acordo fechado em 120. Mas há um caminho alternativo: se após max_rounds não há acordo, o fluxo vai para timeout ou escala para um mediator. Esse fallback é crítico — sem ele, agentes podem negociar para sempre. O critério de sucesso do projeto do módulo é convergência em ≥80% dos casos. Os outros 20% devem cair no fallback (timeout/mediator), não em loop infinito.
💡 ANALOGIA: É como uma negociação de contrato com prazo. Se não fecharem até sexta, o contrato expira. O prazo força convergência.
❓ PERGUNTA PARA A TURMA: "Se o vendedor nunca aceita abaixo de 140, e o comprador nunca oferece mais de 130, o que acontece?" (Resposta: não há zona de acordo. Timeout ou mediator são necessários.)
⚠️ ERROS COMUNS: Alunos não implementam max_rounds. Sem ele, agentes podem negociar indefinidamente.
➡️ TRANSIÇÃO: "Mesmo com acordo, pode haver conflito. Como resolver?"

---

### Slide 50 — Resolução de Conflito: Voting e Mediator

**Título**: Resolução de Conflito — Voting e Mediator
**Objetivo**: Mostrar estratégias para resolver divergências.
**Conteúdo**:
- **Voting**: cada agente vota, maioria vence (simples, pode errar)
- **Weighted voting**: votos ponderados por confiança/expertise
- **Mediator**: agente neutro facilita consenso (mais caro, mais robusto)
- **Trade-off**: simplicidade vs qualidade da decisão
- **Pergunta**: *Voting ou mediator para 3 especialistas com diagnóstico divergente?*

**Diagrama**: 2 fluxos lado a lado (voting com urna; mediator com mesa redonda)
**Animação**: Cada fluxo aparece com click
**Imagem**: Ícone de urna (voting) vs ícone de mesa (mediator)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Quando agentes divergem, como resolver? Voting: cada agente vota, maioria vence. Simples, mas pode errar (2-1 onde o 1 estava certo). Weighted voting pondera por confiança ou expertise — mais justo. Mediator: um agente neutro facilita o consenso, ouvindo todos e propondo uma solução. Mais caro (precisa de um agente extra), mas mais robusto. A escolha depende dos stakes: para decisões de baixo custo, voting basta. Para decisões críticas (ex.: diagnóstico médico), mediator (ou humano no loop) é necessário.
💡 ANALOGIA: Voting = eleição (maioria vence, nem sempre certo). Mediator = terapia de casal (profissional neutro facilita acordo). Weighted voting = conselho de acionistas (votos ponderados por participação).
❓ PERGUNTA PARA A TURMA: "Voting ou mediator para 3 especialistas com diagnóstico divergente?" (Resposta: Mediator — stakes altos. Voting pode errar 2-1.)
⚠️ ERROS COMUNS: Alunos usam voting simples para decisões críticas. Voting pode errar. Para stakes altos, mediator ou humano no loop.
➡️ TRANSIÇÃO: "O risco de qualquer negociação: não convergir."

---

### Slide 51 — Convergência e Deadlock

**Título**: Convergência e Deadlock
**Objetivo**: Lidar com o risco de não convergir.
**Conteúdo**:
- **Convergência**: acordo alcançado em N rounds
- **Deadlock**: nenhum agente cede, loop infinito
- **Causas**: estratégia rígida, sem BATNA, "orgulho" do agente
- **Mitigação**: max_rounds, timeout, concessão forçada, escalar para mediator
- **Critério de sucesso do projeto**: convergência em ≥ 80% dos casos

**Diagrama**: Fluxo com branch de deadlock → timeout
**Animação**: Branch de deadlock aparece em vermelho
**Imagem**: Ícone de loop infinito (deadlock) vs ícone de mão estendida (acordo)
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O maior risco de negociação é deadlock — nenhum agente cede, e o loop é infinito. Causas: estratégia rígida ("nunca abaixo de X"), sem BATNA (não há alternativa, então não há pressão para ceder), ou "orgulho" do agente (recusa por princípio). As mitigações são: max_rounds (força parada após N rounds), timeout (para após T segundos), concessão forçada (após N rounds, a parte que menos cedeu é forçada a ceder), escalar para mediator (um agente neutro decide). O critério de sucesso do projeto é convergência em ≥80%. Os 20% restantes devem cair no fallback (timeout/mediator), documentados como análise de falhas.
💡 ANALOGIA: Deadlock = dois carros em uma rua estreita, nenhum recua. Sem deadline (max_rounds) ou um policial (mediator), ficam para sempre.
⚠️ ERROS COMUNS: Alunos não implementam max_rounds no projeto. Sem max_rounds, deadlock é garantido em casos de divergência total.
➡️ TRANSIÇÃO: "Vamos ver um exemplo concreto."

---

### Slide 52 — Exemplo: Objetivos Parcialmente Conflitantes

**Título**: Objetivos Parcialmente Conflitantes
**Objetivo**: Caso real de negociação com tensão.
**Conteúdo**:
- **Cenário**: agente de velocidade (quer rápido) vs agente de qualidade (quer completo)
- **Negociação**: trade-off entre tempo e profundidade
- **Solução**: definir orçamento de tempo + threshold de qualidade mínima
- **Convergência**: ambos aceitam um meio-termo documentado
- **Pergunta**: *Como evitar que o agente de qualidade nunca aceite?*

**Diagrama**: Diagrama D13 — Eixo tempo × qualidade com zona de acordo
**Animação**: Zona de acordo destaca-se
**Imagem**: Gráfico tempo × qualidade
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Caso prático de objetivos parcialmente conflitantes. Agente de velocidade quer terminar rápido (baixo tempo). Agente de qualidade quer resultado completo (alta qualidade). Tensão: mais qualidade leva mais tempo. A negociação é definir um trade-off: orçamento de tempo máximo + threshold de qualidade mínima. Se ambos aceitam, há convergência. O ponto crítico é como evitar que o agente de qualidade nunca aceite — porque sempre dá para melhorar. Solução: threshold de qualidade mínima (abaixo disso, inaceitável) + tempo máximo (acima disso, inaceitável). A interseção é a zona de acordo.
💡 ANALOGIA: É como escolher restaurante. Você quer barato e rápido; seu amigo quer chique e elaborado. Vocês negociam: "ok, restaurante médio, 30 min de espera". Meio-termo.
❓ PERGUNTA PARA A TURMA: "Como evitar que o agente de qualidade nunca aceite?" (Resposta: definir threshold de qualidade mínima + tempo máximo. Sem limites, a qualidade sempre pode melhorar.)
⚠️ ERROS COMUNS: Alunos deixam o agente de qualidade sem limite. Resultado: nunca converge. Sempre defina threshold.
➡️ TRANSIÇÃO: "Vamos aos protocolos emergentes que estão padronizando tudo isso."

---

## SEÇÃO G — Protocolos e Padrões Emergentes (Slides 53-59 · 8 min)

---

### Slide 53 — [SEÇÃO] Protocolos Emergentes

**Título**: 6 — Protocolos e Padrões Emergentes
**Objetivo**: Transição para padrões de comunicação.
**Conteúdo**: "6 — Protocolos e Padrões Emergentes"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "6" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Até agora vimos padrões conceituais. Agora vamos ver os protocolos que estão padronizando a comunicação A2A — especialmente o A2A Protocol do Google e como ele se relaciona com o MCP.
➡️ TRANSIÇÃO: "O A2A Protocol é o mais novo."

---

### Slide 54 — A2A Protocol (Google, 2024)

**Título**: A2A Protocol (Google, 2024)
**Objetivo**: Apresentar o protocolo A2A do Google.
**Conteúdo**:
- **A2A (Agent-to-Agent) Protocol**: padrão aberto para comunicação entre agentes
- **Objetivo**: interoperabilidade entre agentes de diferentes frameworks
- **Agent Card**: manifesto de capacidades do agente
- **Tasks**: unidade de trabalho delegável entre agentes
- **Status**: emerging spec (ainda em evolução)

**Diagrama**: Agent Card + Task flow
**Animação**: Agent Card aparece, depois Task flow
**Imagem**: Ícone de cartão de visitas (Agent Card)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O A2A Protocol é um padrão aberto lançado pelo Google em 2024. O objetivo é interoperabilidade: agentes de frameworks diferentes (LangGraph, CrewAI, AutoGen) possam se comunicar. Dois conceitos centrais. Agent Card: um manifesto que descreve as capacidades do agente — exposto em uma URL padrão (`/.well-known/agent.json`). Tasks: a unidade de trabalho delegável entre agentes. Um agente A descobre o Agent Card do agente B, envia uma Task, B processa e retorna o resultado. O status é "emerging spec" — ainda evoluindo, mas com adoção crescente.
💡 ANALOGIA: Agent Card = cartão de visitas digital (diz o que o agente faz). Tasks = ordem de serviço (o que você pede). A2A = protocolo que padroniza a interação.
⚠️ ERROS COMUNS: Alunos confundem A2A com MCP. A2A é agent↔agent. MCP é agent↔system. Veremos isso no próximo slide.
➡️ TRANSIÇÃO: "Como o A2A funciona na prática?"

---

### Slide 55 — A2A Protocol: Como Funciona

**Título**: A2A Protocol — Como Funciona
**Objetivo**: Mostrar o fluxo do protocolo A2A.
**Conteúdo**:
1. Agente A descobre Agent Card de B (via URL `/.well-known/agent.json`)
2. A envia Task para B
3. B processa e retorna status + resultado
4. Streaming opcional para tarefas longas (SSE)
- Suporte a **Server-Sent Events** para updates em tempo real

**Diagrama**: Diagrama D14 — Sequência de mensagens A2A
**Animação**: Passos aparecem sequencialmente
**Imagem**: Diagrama de sequência estilo UML
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O fluxo do A2A é elegante. Passo 1: o agente A descobre o Agent Card do agente B fazendo GET em `/.well-known/agent.json` (padrão inspirado em HTTPS well-known). O Agent Card diz: capacidades, endpoints, autenticação. Passo 2: A envia uma Task para B via POST. Passo 3: B processa e retorna status (working, completed, failed) + resultado. Passo 4: para tarefas longas, B pode fazer streaming via SSE (Server-Sent Events) — updates em tempo real. O protocolo é HTTP-based, o que facilita adoção. Não reinventa a roda — usa REST + JSON.
💡 ANALOGIA: É como contratar um freelancer. Você vê o perfil dele (Agent Card), envia um brief (Task), ele trabalha e entrega. Se demora, ele manda updates (SSE).
⚠️ ERROS COMUNS: Alunos acham que A2A é "novo e complicado". É HTTP + JSON. A inovação é a padronização, não a tecnologia.
➡️ TRANSIÇÃO: "A pergunta que todo mundo faz: A2A vs MCP?"

---

### Slide 56 — MCP vs A2A

**Título**: MCP vs A2A
**Objetivo**: Esclarecer a relação entre MCP e A2A.
**Conteúdo**:
- **MCP (Model Context Protocol)**: agent ↔ system (tools, data sources)
- **A2A (Agent-to-Agent)**: agent ↔ agent (delegação, colaboração)
- **Complementares, não competidores!**
- **Analogia**: MCP = como o agente fala com ferramentas; A2A = como agentes falam entre si
- **Pergunta**: *MCP e A2A são complementares ou competidores?*

**Diagrama**: Diagrama D15 — Diagrama Venn ou 2 eixos (agent ↔ system vs agent ↔ agent)
**Animação**: Venn aparece, depois as legendas
**Imagem**: Diagrama de Venn
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esta é a comparação mais importante da seção. MCP (Model Context Protocol, da Anthropic) conecta agentes a ferramentas e fontes de dados — é agent↔system. A2A (Agent-to-Agent, do Google) conecta agentes entre si para delegação e colaboração — é agent↔agent. São complementares, não competidores! Um agente pode usar MCP para acessar uma tool (ex.: banco de dados) e A2A para delegar parte do trabalho a outro agente. A confusão vem do nome parecido, mas resolvem problemas diferentes.
💡 ANALOGIA: MCP = como você usa suas ferramentas (martelo, chave de fenda). A2A = como você fala com seu colega de equipe. Você precisa dos dois.
❓ PERGUNTA PARA A TURMA: "MCP e A2A são complementares ou competidores?" (Resposta: Complementares. MCP = agent↔system. A2A = agent↔agent.)
⚠️ ERROS COMUNS: Alunos acham que "preciso escolher entre MCP e A2A". Não — use ambos. MCP para tools, A2A para agentes.
➡️ TRANSIÇÃO: "Vamos ver padrões de orquestração."

---

### Slide 57 — Padrões de Orquestração Multi-Agente

**Título**: Padrões de Orquestração Multi-Agente
**Objetivo**: Visão geral de orquestração.
**Conteúdo**:
- **Centralizada** (supervisor/orchestrator): um agente coordena os demais
- **Descentralizada** (peer-to-peer): agentes se coordenam sem líder
- **Hierárquica**: supervisor → sub-supervisores → agentes
- **Market-based**: agentes "licitam" tarefas
- **Trade-off**: controle vs flexibilidade vs escalabilidade

**Diagrama**: Diagrama D16 — 4 mini-topologias em grid 2x2
**Animação**: Cada topologia aparece com click
**Imagem**: 4 ícones de topologia
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Existem 4 padrões de orquestração multi-agente. Centralizada: um supervisor coordena tudo — controle máximo, mas gargalo. Descentralizada: agentes se coordenam sem líder (P2P) — flexível, mas sem garantia de convergência. Hierárquica: supervisor no topo, sub-supervisores no meio, agentes na base — escala melhor, mas complexa. Market-based: agentes "licitam" tarefas baseado em capacidade/custo — eficiente para alocação dinâmica. A escolha depende: controle (centralizada), flexibilidade (descentralizada), escalabilidade (hierárquica), eficiência (market-based).
💡 ANALOGIA: Centralizada = ditador (controle total). Descentralizada = assembleia (todos decidem). Hierárquica = corporação (CEO → diretores → funcionários). Market-based = leilão (quem oferece melhor, faz).
⚠️ ERROS COMUNS: Alunos usam centralizada para tudo porque é simples. Mas centralizada não escala — o supervisor vira gargalo.
➡️ TRANSIÇÃO: "Esses padrões não são novos. Vamos contextualizar com FIPA."

---

### Slide 58 — FIPA e Padrões Históricos

**Título**: FIPA e Padrões Históricos
**Objetivo**: Contextualizar com padrões clássicos de multi-agente.
**Conteúdo**:
- **FIPA** (Foundation for Intelligent Physical Agents): padrões de comunicação ACL
- **FIPA-ACL**: performatives (request, inform, propose, accept, reject)
- **Aprendizado**: LLM agents redescobrem conceitos de FIPA
- **KQML**: predecessor de FIPA (anos 90)
- **Lição**: muita coisa "nova" já foi pensada — aprender com o passado

**Diagrama**: Timeline FIPA → KQML → A2A
**Animação**: Timeline cresce da esquerda para direita
**Imagem**: Timeline histórica
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vale contextualizar: comunicação multi-agente não é nova. FIPA (Foundation for Intelligent Physical Agents, anos 90) definiu padrões de comunicação ACL (Agent Communication Language). FIPA-ACL tem performatives — request, inform, propose, accept, reject — que mapeiam para o que LLM agents fazem implicitamente. KQML (Knowledge Query and Manipulation Language) foi o predecessor. A lição é importante: muita coisa "nova" em LLM agents já foi pensada em sistemas multi-agente clássicos. Os conceitos de performatives, blackboard, actor model são dos anos 70-90. O que é novo é a viabilidade com LLMs — não os conceitos.
💡 ANALOGIA: É como redescobrir a roda. FIPA já tinha "request" e "inform" nos anos 90. LLM agents fazem o mesmo, mas sem saber que já tem nome. Aprender com o passado economiza tempo.
⚠️ ERROS COMUNS: Alunos acham que "LLM agents inventaram multi-agent". Não — FIPA, HEARSAY-II, KQML já existiam. O LLM tornou viável, não inventou.
➡️ TRANSIÇÃO: "Qual o estado da padronização hoje?"

---

### Slide 59 — Estado da Padronização

**Título**: Estado da Padronização
**Objetivo**: Ser honesto sobre a maturidade do ecossistema.
**Conteúdo**:
- **MCP**: mais maduro (Anthropic, amplamente adotado)
- **A2A**: emergente (Google, adoção crescente)
- **FIPA**: maduro mas sub-adotado em LLM agents
- **Fragmentação**: cada framework tem seu próprio protocolo
- **Tendência**: convergência para MCP + A2A como camadas complementares

**Diagrama**: Matriz de maturidade (adoção × maturidade)
**Animação**: Protocolos aparecem na matriz
**Imagem**: Gráfico de maturidade
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Sejamos honestos sobre a maturidade. MCP é o mais maduro — da Anthropic, amplamente adotado, com ferramentas e data sources padronizados. A2A é emergente — do Google, com adoção crescente mas spec ainda evoluindo. FIPA é maduro como padrão, mas sub-adotado em LLM agents (muito acadêmico). O problema atual é fragmentação: cada framework (LangGraph, CrewAI, AutoGen) tem seu próprio protocolo. A tendência é convergência: MCP + A2A como camadas complementares (MCP para tools, A2A para agentes). Mas estamos em 2026 — ainda cedo para dizer que venceu.
💡 ANALOGIA: É como os formatos de vídeo nos anos 2000 (VHS vs Betamax, Blu-ray vs HD-DVD). Fragmentação até o mercado convergir. Em agentes, estamos na fase de fragmentação.
⚠️ ERROS COMUNS: Alunos adotam um protocolo cegamente. Avalie maturidade, adoção e direção antes de apostar.
➡️ TRANSIÇÃO: "Vamos ao fechamento — boas práticas e caso de estudo."

---

## SEÇÃO H — Fechamento (Slides 60-72 · 12 min)

---

### Slide 60 — [SEÇÃO] Boas Práticas e Anti-Patterns

**Título**: 7 — Boas Práticas e Anti-Patterns
**Objetivo**: Transição para o fechamento.
**Conteúdo**: "7 — Boas Práticas e Anti-Patterns"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "7" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vimos muita teoria. Agora vamos consolidar em boas práticas (o que fazer) e anti-patterns (o que não fazer).
➡️ TRANSIÇÃO: "Comecemos pelo que fazer."

---

### Slide 61 — Boas Práticas (DO)

**Título**: Boas Práticas (DO)
**Objetivo**: Checklist de boas práticas em comunicação multi-agente.
**Conteúdo**:
- Comece com **2 agentes** antes de escalar para N
- Defina **schemas de mensagem com versionamento** desde o dia 1
- Use **blackboard** quando N é grande e contribuições são independentes
- Defina **max_rounds** em negociações (evitar deadlock)
- **Logue todas as mensagens A2A** (traces são seu debugging)
- **Isole agentes como atores** (estado protegido)
- **Documente o protocolo** de handoff/delegação explicitamente

**Diagrama**: Checklist verde (`etho-success`)
**Animação**: Itens aparecem um a um com checkmark
**Imagem**: Ícones de checkmark verde
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Sete boas práticas. Comece com 2 agentes: multi-agente é complexidade; comece simples e escale só quando necessário. Schemas com versionamento desde o dia 1: agentes evoluem; sem versionamento, uma mudança quebra tudo. Blackboard para N grande: escala melhor que mensagens diretas. max_rounds em negociações: sem isso, deadlock é garantido. Logar todas as mensagens: em multi-agente, o debugging É o trace; sem logs, você está cego. Isole agentes como atores: estado protegido previne race conditions. Documente handoff/delegação: a ambiguidade entre eles é a fonte de muitos bugs.
💡 ANALOGIA: É como boas práticas de trânsito. Comece devagar (2 agentes), use cinto (schemas), siga padrões (blackboard), tenha freio (max_rounds), olhe pelo retrovisor (logs), mantenha distância (isolamento), use seta (documentação).
⚠️ ERROS COMUNS: Alunos pulam o versionamento "para ir mais rápido". Quando o schema muda, dói.
➡️ TRANSIÇÃO: "Agora o que NÃO fazer."

---

### Slide 62 — Anti-Patterns (DON'T)

**Título**: Anti-Patterns (DON'T)
**Objetivo**: Checklist do que NÃO fazer.
**Conteúdo**:
- Começar com **group chat de 5 agentes** sem necessidade
- **Sem schema** de mensagem ("telefone sem fio")
- **Negociação sem max_rounds** (deadlock infinito)
- **Shared state sem locks** (race condition)
- **Actor model para tudo** (overhead desnecessário em tarefas simples)
- **Não logar mensagens** (debug cego em multi-agente)
- **Misturar MCP e A2A** sem entender a diferença
- Confiar que agentes **"vão se entender"** sem protocolo

**Diagrama**: Checklist vermelho (`etho-danger`)
**Animação**: Itens aparecem um a um com X vermelho
**Imagem**: Ícones de X vermelho
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Oito anti-patterns. Começar com group chat de 5: complexidade desnecessária no início. Sem schema: cada agente interpreta diferente. Negociação sem max_rounds: deadlock garantido. Shared state sem locks: race condition. Actor model para tudo: overhead em tarefas simples (1 agente com 1 tool não precisa de actor). Não logar: debug cego em multi-agente é pesadelo. Misturar MCP e A2A: MCP é tools, A2A é agentes; confundir = bugs. Confiar que "agentes vão se entender": LLMs não são mágicos; sem protocolo, viram caos.
💡 ANALOGIA: É como anti-patterns de dieta. Pular refeições (sem schema), fasting sem limite (sem max_rounds), tudo frito (shared state sem locks), suplemento para tudo (actor para tudo). Cada um parece boa ideia, mas faz mal.
⚠️ ERROS COMUNS: Alunos acreditam que "agentes inteligentes se coordenam sozinhos". Não. Sem protocolo, até agentes inteligentes viram caos.
➡️ TRANSIÇÃO: "Vamos ver tudo isso em um caso real: MetaGPT."

---

### Slide 63 — Caso de Estudo: MetaGPT

**Título**: Caso de Estudo — MetaGPT
**Objetivo**: Mostrar todos os conceitos em um caso real.
**Conteúdo**:
- **MetaGPT**: framework multi-agente para desenvolvimento de software
- **Papéis**: Product Manager → Architect → Engineer → QA
- **Comunicação via artefatos estruturados** (não chat livre)
- **SOPs** codificam o workflow: cada papel sabe o que esperar
- **Resultado**: gera código funcional de ponta a ponta
- **Lição**: estrutura > improvisação em sistemas multi-agente

**Diagrama**: Diagrama D7 (expandido) — Pipeline MetaGPT com papéis e artefatos
**Animação**: Pipeline flui mostrando cada artefato
**Imagem**: Pipeline MetaGPT
**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: MetaGPT é o caso de estudo perfeito porque junta tudo que vimos. Framework multi-agente para desenvolvimento de software. Papéis claros: Product Manager recebe a tarefa, produz PRD. Architect recebe PRD, produz Design Doc. Engineer recebe Design, produz Code. QA recebe Code, produz Test Report. A comunicação NÃO é chat livre — é passagem de artefatos estruturados. Isso é MetaGPT aplicando SOPs (Standard Operating Procedures): cada papel sabe exatamente o que esperar do anterior. O resultado é código funcional de ponta a ponta — dado um pedido ("faça um jogo da velha"), MetaGPT gera o código. A lição central: estrutura > improvisação. Onde chat livre gera ambiguidade, SOPs geram clareza.
💡 ANALOGIA: É como uma linha de montagem de fábrica. Cada estação (papel) recebe um insumo (artefato), processa, entrega um produto. Sem improviso — tudo definido. MetaGPT formaliza isso para agentes.
❓ PERGUNTA PARA A TURMA: "Por que MetaGPT funciona melhor que group chat livre?" (Resposta: estrutura. SOPs reduzem ambiguidade; cada papel sabe o que esperar.)
⚠️ ERROS COMUNS: Alunos acham que "chat livre é mais flexível". MetaGPT prova o oposto — estrutura melhora resultados.
➡️ TRANSIÇÃO: "Vamos praticar com um exercício de schema."

---

### Slide 64 — Exercício: Schema de Mensagem A2A

**Título**: Exercício — Schema de Mensagem A2A
**Objetivo**: Praticar o design de um schema de comunicação.
**Conteúdo**:
- **Cenário**: agentes de compra e venda negociando preço
- **Em duplas**: escrever schema JSON de mensagem com versionamento
- **Incluir**: `sender`, `receiver`, `message_type`, `payload`, `timestamp`, `version`
- **Considerar**: como representar proposta, contraproposta, aceitação
- 3 min discussão, compartilhar no quadro

**Diagrama**: Template de schema em branco
**Animação**: Campos do template destacados
**Imagem**: JSON template em branco
**Tempo**: 4 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Exercício em duplas para internalizar schemas A2A. Cenário: negociação comprador/vendedor. Em duplas, escrevam um schema JSON com os campos obrigatórios e pensem em como representar proposta, contraproposta e aceitação (dica: campo `message_type`). 3 minutos, depois compartilhamos no quadro. Este exercício prepara para o projeto do módulo (sistema de negociação).
💡 ANALOGIA: É como desenhar um formulário de proposta comercial. Quais campos você precisa? Remetente, destinatário, tipo (proposta/contraproposta/aceite), valor, prazo. O schema é o formulário padronizado.
❓ PERGUNTA PARA A TURMA: "Como vocês representariam uma contraproposta?" (Resposta: `message_type: "counter_propose"` + campo `in_reply_to` referenciando a proposta original.)
⚠️ ERROS COMUNS: Alunos esquecem o `version`. Sem versionamento, quando o schema evolui, quebra.
➡️ TRANSIÇÃO: "Vamos resumir tudo que vimos."

---

### Slide 65 — Resumo da Aula

**Título**: Resumo da Aula
**Objetivo**: Sintetizar os pontos-chave.
**Conteúdo**:
- **Espectro A2A**: síncrono vs assíncrono, topologias, schemas, garantias
- **Padrões de conversação**: CAMEL (2-agent), AutoGen (group), Swarm (handoff)
- **Blackboard**: espaço compartilhado, baixo acoplamento, escala com N
- **Actor model**: isolamento, concorrência sem locks, distribuição transparente
- **Negociação**: bargaining, auction, voting, mediator, evitar deadlock
- **Protocolos**: MCP (agent↔system) + A2A (agent↔agent) = complementares
- **MetaGPT**: SOPs estruturados > chat livre

**Diagrama**: 7 ícones com os pontos-chave
**Animação**: Ícones aparecem um a um
**Imagem**: Grid de ícones resumindo
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Recapitulando os 7 blocos. Espectro A2A: síncrono vs assíncrono, 3 topologias (broadcast, P2P, pub/sub), schemas com versionamento, 3 garantias de entrega. Padrões de conversação: CAMEL (2 agentes em turnos), AutoGen (group chat com manager), Swarm (handoff). Blackboard: espaço compartilhado, baixo acoplamento, escala com N. Actor model: isolamento de estado, concorrência sem locks, localização transparente. Negociação: bargaining (1-1), auction (1-N), voting/mediator (resolução de conflito), max_rounds contra deadlock. Protocolos: MCP para tools, A2A para agentes — complementares. MetaGPT: SOPs estruturados batem chat livre.
💡 ANALOGIA: É como o resumo de um curso de orquestra. Aprendemos notas (mensagens), partitura (schemas), seções (padrões), regente (orquestração), afinação (negociação), padrão musical (protocolos), e a apresentação final (MetaGPT).
➡️ TRANSIÇÃO: "Vamos confirmar que cobrimos tudo."

---

### Slide 66 — Checklist da Aula

**Título**: Checklist da Aula
**Objetivo**: Confirmar que todos os tópicos foram cobertos.
**Conteúdo**:
- [ ] Definiu o espectro A2A (síncrono/assíncrono, topologias)
- [ ] Apresentou schemas de mensagem com versionamento
- [ ] Explicou 3 padrões de conversação (CAMEL, AutoGen, Swarm)
- [ ] Demontrou blackboard vs mensagens diretas
- [ ] Implementou actor model ou mostrou a demo
- [ ] Discutiu negociação, conflito e deadlock
- [ ] Comparou MCP vs A2A Protocol

**Diagrama**: Checklist visual
**Animação**: Checkmarks aparecem
**Imagem**: Ícone de checklist
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Checklist para confirmar cobertura. Se algum item ficou de fora, mencione brevemente ou indique leitura. Esta é também uma auto-avaliação do professor — se algo ficou confuso, é hora de endereçar.
➡️ TRANSIÇÃO: "Hora do quiz."

---

### Slide 67 — Quiz: Pergunta 1

**Título**: Quiz — Pergunta 1
**Objetivo**: Verificar compreensão.
**Conteúdo**:
- "Quando blackboard é preferível a mensagens diretas?"
- A) Quando há apenas 2 agentes
- B) Quando N é grande e contribuições são independentes
- C) Quando a ordem das mensagens é crítica
- D) Quando o acoplamento entre agentes deve ser máximo
- **Resposta**: B

**Diagrama**: 4 opções em cards
**Animação**: Opções aparecem; resposta destaca após votação
**Imagem**: Cards de quiz
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Pergunta 1. Deixem 20 segundos para pensar. A resposta é B — blackboard brilha com N grande e contribuições independentes. Com 2 agentes (A), mensagens diretas são mais simples. Ordem crítica (C) favorece mensagens diretas com sequenciamento. Acoplamento máximo (D) é o oposto do blackboard.
➡️ TRANSIÇÃO: "Pergunta 2."

---

### Slide 68 — Quiz: Pergunta 2

**Título**: Quiz — Pergunta 2
**Objetivo**: Verificar compreensão.
**Conteúdo**:
- "Qual é a diferença entre handoff (Swarm) e delegação (supervisor)?"
- A) Handoff é síncrono, delegação é assíncrona
- B) Handoff transfere controle (agente sai), delegação mantém supervisor
- C) Handoff é para 2 agentes, delegação para N
- D) Não há diferença
- **Resposta**: B

**Diagrama**: 4 opções em cards
**Animação**: Opções aparecem; resposta destaca após votação
**Imagem**: Cards de quiz
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Pergunta 2. A resposta é B — handoff transfere controle (agente original sai), delegação mantém supervisor esperando retorno. A diferença não é sincronicidade (A) nem número de agentes (C), mas quem mantém o controle. D está errado — a diferença é crucial.
➡️ TRANSIÇÃO: "Pergunta 3."

---

### Slide 69 — Quiz: Pergunta 3

**Título**: Quiz — Pergunta 3
**Objetivo**: Verificar compreensão.
**Conteúdo**:
- "MCP e A2A Protocol são:"
- A) Competidores — um substitui o outro
- B) Complementares — MCP é agent↔system, A2A é agent↔agent
- C) A mesma coisa com nomes diferentes
- D) Ambos obsoletos
- **Resposta**: B

**Diagrama**: 4 opções em cards
**Animação**: Opções aparecem; resposta destaca após votação
**Imagem**: Cards de quiz
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Pergunta 3. A resposta é B — são complementares. MCP conecta agentes a ferramentas/dados (agent↔system). A2A conecta agentes entre si (agent↔agent). A está errado (não competem), C está errado (resolvem problemas diferentes), D está errado (ambos em adoção crescente).
➡️ TRANSIÇÃO: "Última pergunta."

---

### Slide 70 — Quiz: Pergunta 4

**Título**: Quiz — Pergunta 4
**Objetivo**: Verificar compreensão.
**Conteúdo**:
- "Verdadeiro ou falso: 'Actor model é mais lento que shared-state.'"
- A) Verdadeiro — locks são mais rápidos
- B) Falso — em alta concorrência, actor model escala melhor sem locks
- C) Depende — sempre (contexto importa)
- D) Impossível determinar sem benchmark
- **Resposta**: B (com caveat: contexto importa, mas a afirmação geral é falsa)

**Diagrama**: 4 opções em cards
**Animação**: Opções aparecem; resposta destaca após votação
**Imagem**: Cards de quiz
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Pergunta 4. A resposta é B. A afirmação geral é falsa: em alta concorrência, actor model escala melhor sem locks. Shared state sofre com deadlocks e race conditions. Há overhead de serialização no actor model, mas em cenários de alta concorrência, é compensado pela ausência de contenção de lock. C tem uma ponta de verdade (contexto importa), mas a afirmação como enunciada é falsa.
➡️ TRANSIÇÃO: "Vamos às referências e conexão com próximos módulos."

---

### Slide 71 — Conexão com Próximos Módulos + Referências

**Título**: Conexão com Próximos Módulos + Referências
**Objetivo**: Mostrar conexões e indicar leitura.
**Conteúdo**:
- **ETHAGT10** — Padrões de Arquitetura Multi-Agente: topologias completas
- **ETHAGT11** — Event-Driven Agents: comunicação assíncrona em escala
- **ETHAGT15** — (depende deste módulo)
- **Leitura obrigatória**:
  - Wu et al. *AutoGen* (arXiv:2308.08155)
  - Li et al. *CAMEL* (arXiv:2303.17760)
  - Hewitt, C. *Actor Model* (1973)
- **Recomendado**: Google *A2A Protocol* spec; OpenAI Swarm (repo)
- **Survey**: arXiv:2308.00352

**Diagrama**: Diagrama D17 — Mapa da especialização com ETHAGT09 destacado
**Animação**: Conexões surgem do ETHAGT09
**Imagem**: Mind map da especialização
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: ETHAGT09 é a fundação para ETHAGT10 (Padrões de Arquitetura Multi-Agente — topologias completas), ETHAGT11 (Event-Driven Agents — comunicação assíncrona em escala) e ETHAGT15 (Sociedades de Agentes). A leitura obrigatória é: AutoGen (para GroupChat), CAMEL (para two-agent dialogue), e Hewitt (para actor model). Recomendado: A2A Protocol spec (do Google) e o repo do Swarm (da OpenAI). O survey arXiv:2308.00352 dá panorama acadêmico.
📖 IMPORTANTE: Leiam os papers. A aula cobre os conceitos, mas os papers têm os detalhes — traces de exemplo, experimentos, limitações.
➡️ TRANSIÇÃO: "Vamos ao encerramento."

---

### Slide 72 — Projeto, Labs e Q&A

**Título**: Projeto, Labs e Q&A
**Objetivo**: Apresentar projeto/labs e encerrar.
**Conteúdo**:
- **Projeto**: sistema de negociação entre agentes (comprador/vendedor ou especialistas)
  - Entrega: código + traces + análise de convergência
  - Critério: convergência ≥ 80% + análise de falhas
- **Lab 1** (4h): "Duas Arquiteturas, um Problema" — AutoGen vs blackboard
- **Lab 2** (4h): "Actor Model com Handoffs" — swarm com transferência de controle
- **Próxima aula**: ETHAGT10 — Padrões de Arquitetura Multi-Agente
- "Perguntas?"
- Contato do professor

**Diagrama**: Logo Etho + fundo `etho-dark`
**Animação**: Fade out
**Imagem**: Logo Etho centralizado
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Encerramento. O projeto do módulo é um sistema de negociação entre agentes — comprador/vendedor ou especialistas debatendo diagnóstico. Entrega: código + traces + análise de convergência (≥80%) + análise de falhas. Os labs complementam: Lab 1 compara duas arquiteturas (group chat vs blackboard); Lab 2 implementa actor model com handoffs. A próxima aula é ETHAGT10 (Padrões de Arquitetura Multi-Agente) — vamos aprofundar topologias completas. Abrir para Q&A.
💡 ANALOGIA: Hoje vocês aprenderam a reger a orquestra. O projeto é a primeira apresentação. Os labs são os ensaios. ETHAGT10 aprofunda a regência.
❓ PERGUNTA PARA A TURMA: "Perguntas?" (Se não houver, faça a inversa: "Qual parte foi menos clara?")
⚠️ Se tempo permitir, faça a pergunta de feedback: "Um padrão de comunicação que você não conhecia."
➡️ FIM: "Obrigado. Nos vemos na ETHAGT10."
