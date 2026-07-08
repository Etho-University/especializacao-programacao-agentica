# ETHAGT02 — Slides Detalhados + Notas do Professor (Parte 1: Slides 1-26)

> Universidade Etho · Especialização em Programação Agêntica
> Cada slide contém: título, objetivo, conteúdo, notas do professor, diagrama, animação, imagem, tempo.

---

## SEÇÃO A — Abertura (Slides 1-6 · 8 min)

---

### Slide 1 — Capa

**Título**: ETHAGT02 — Tool Calling e Agent-Computer Interface (ACI)
**Objetivo**: Identificar a aula, o professor e o contexto dentro da especialização.
**Conteúdo**:
- ETHAGT02 — Tool Calling e Agent-Computer Interface (ACI)
- Universidade Etho · Especialização em Programação Agêntica
- Fase A — Fundamentos Agênticos · 25 h
- Professor · Data

**Diagrama**: Logo Etho (canto sup. esquerdo) + imagem de fundo abstrata (tools, schemas, conectores)
**Animação**: Fade in do título (300ms)
**Imagem**: Fundo `etho-dark` (#0F1E2D) com pattern sutil de nós e chaves
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Bem-vindos. Na aula anterior (ETHAGT01) vimos o Augmented LLM como bloco fundamental — LLM com retrieval, tools e memória em loop. Hoje vamos fazer um zoom profundo no componente "tools". Vamos tratar o design de tools com o mesmo rigor que um designer de UI trata a interface humana. Esta aula vai mudar como vocês pensam sobre a linha que separa "o prompt" de "a tool" — e por que a maioria dos bugs de agentes está do lado erro dessa linha.
💡 ANALOGIA: ETHAGT01 foi aprender a anatomia do agente. ETHAGT02 é a cirurgia das tools — onde mora a confiabilidade.
❓ PERGUNTA PARA A TURMA: "Quantos de vocês já escreveram uma tool que o modelo usou errado?" (levantar mãos — quase todos vão levantar)
⚠️ ERROS COMUNS: Alunos chegam achando que tool calling é "só chamar uma função". Não é — é desenhar uma interface para um usuário não-humano que não pode perguntar de novo.
➡️ TRANSIÇÃO: "Vamos começar definindo o que vocês vão conseguir fazer ao final desta aula."

---

### Slide 2 — Objetivos do Módulo

**Título**: Objetivos do Módulo
**Objetivo**: Deixar claro o que o aluno deve conseguir FAZER ao final da aula.
**Conteúdo**:
- **Objetivo geral**: Capacitar o aluno a **projetar, documentar e validar tools** que tornam um agente confiável
- **Objetivos específicos**:
  1. Dominar o mecanismo de tool calling (function calling, structured outputs, JSON schema)
  2. Aplicar os princípios de Anthropic para ACI: poka-yoke, exemplos, paths absolutos, formato próximo ao natural
  3. Projetar tools idempotentes, com tratamento de erro e timeouts
  4. Distinguir tools seguras de destrutivas; aplicar HITL onde necessário
  5. Avaliar empiricamente o uso de tools por um agente (workbench, iterar)

**Diagrama**: 5 ícones representando cada objetivo (engrenagem, escudo, loop, semáforo, microscópio)
**Animação**: Objetivos aparecem um a um (on click)
**Imagem**: Ícones minimalistas em `etho-accent` (#E85D2F)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Cada objetivo é mensurável. Não é "entender tool calling" — é "dominar o mecanismo". Não é "saber o que é ACI" — é "aplicar os princípios". O objetivo geral captura a essência: tool confiável. Um agente só é tão confiável quanto sua tool menos confiável. Se uma das 8 tools falha 30% das vezes, o agente falha 30% das vezes. Vamos revisar estes objetivos no final para confirmar.
💡 ANALOGIA: É como um checklist de inspeção de segurança de um avião. Cada item é verificável: trem retraído? flaps ok? combustível suficiente? Não é "o avião parece bom" — é cada item confirmado.
❓ PERGUNTA PARA A TURMA: "Qual desses objetivos vocês acham mais difícil de aplicar no trabalho hoje?" (deixar responder — costuma ser #2 ou #4)
⚠️ ERROS COMUNS: Alunos acham que "projetar tools" é só escrever o JSON Schema. Não é — é pensar na experiência do modelo, prever modos de falha, validar empiricamente.
➡️ TRANSIÇÃO: "Antes de saber o que vamos fazer, vamos saber onde estamos no mapa."

---

### Slide 3 — Competências Desenvolvidas

**Título**: Competências Desenvolvidas
**Objetivo**: Conectar a aula ao Framework Etho de competências.
**Conteúdo**:

| Competência | Nível ao final | Próximo nível em |
|---|---|---|
| C1 Programação Agêntica | **I** (Intermediário) | ETHAGT04-16 |
| C3 MCP & Tool Use | **I** (Intermediário) | ETHAGT08 (MCP) |
| C5 AgentOps & Avaliação | **B** (Básico) | ETHAGT12 |
| C6 Agent Security | **B** (Básico) | ETHAGT13 |

**Diagrama**: Radar chart com 4 eixos mostrando nível B/I
**Animação**: Radar aparece com wipe (left-to-right, 500ms)
**Imagem**: Badge visual por competência (círculos coloridos)
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Em ETHAGT01 vocês alcançaram C1 Básico e C3 Básico. Hoje, C1 e C3 sobem para Intermediário — vocês vão conseguir projetar tools de qualidade e justificar escolhas de design. C5 (AgentOps) e C6 (Security) entram em Básico — vocês conhecem workbench e HITL, mas o aprofundamento vem em ETHAGT12 e ETHAGT13. O salto de C3 de Básico para Intermediário é o coração desta aula.
💡 ANALOGIA: É como aprender a cozinhar. Ontem você aprendeu a ligar o fogão (Básico). Hoje você vai aprender técnicas de corte e controle de temperatura (Intermediário). Cozinhar um banquete (Avançado) vem nos próximos módulos.
⚠️ ERROS COMUNS: Alunos acham que "Intermediário em C3" significa "saber usar frameworks de tool calling". Não — significa saber PROJETAR tools boas, independente do framework.
➡️ TRANSIÇÃO: "Vamos ver como esta aula está estruturada."

---

### Slide 4 — Agenda da Aula

**Título**: Agenda da Aula
**Objetivo**: Mostrar o roteiro da aula com tempos estimados.
**Conteúdo**:
- **Bloco 1 (45 min)**:
  - Abertura (8 min) — objetivos, motivação, contexto ACI
  - Tool Calling (15 min) — function calling, JSON Schema, structured outputs, demo
  - ACI como Disciplina (15 min) — 5 princípios, exercício, caso SWE-bench
  - Intervalo (5 min)
- **Bloco 2 (45 min)**:
  - Engenharia de Tools (12 min) — schemas, idempotência, timeouts, tipologia
  - HITL (5 min) — matriz de risco, 4 níveis, exercício
  - Erros + Avaliação (10 min) — 5 erros, workbench, métricas
  - Fechamento (15 min) — boas práticas, anti-patterns, quiz, Q&A

**Diagrama**: Timeline horizontal com 7 seções coloridas
**Animação**: Timeline cresce da esquerda para direita (500ms)
**Imagem**: Ícones de relógio por seção
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A aula tem dois blocos. O primeiro estabelece o mecanismo (como tool calling funciona) e a disciplina (como projetar bem). O segundo é mais prático: engenharia de robustez (idempotência, timeouts), governança (HITL), avaliação (workbench) e fechamento. Há um intervalo de 5 min entre os blocos. O quiz final tem 5 perguntas.
💡 ANALOGIA: É como montar um carro. Bloco 1: entender o motor e o design das peças. Bloco 2: cinto de segurança, airbag, teste de colisão e inspeção final.
⚠️ ERROS COMUNS: Alunos chegam atrasados e perdem a motivação (Slide 5). Avisar que o Slide 5 define o problema central de toda a aula.
➡️ TRANSIÇÃO: "Vamos começar pelo problema. Por que tools mal desenhadas são um pesadelo?"

---

### Slide 5 — O Problema: Tools Mal Desenhadas

**Título**: O Problema: Tools Mal Desenhadas
**Objetivo**: Criar tensão cognitiva — bugs de agentes quase sempre vêm de tools ruins, não de prompts ruins.
**Conteúdo**:
- **Cenário real**: agente de suporte que busca produto, mas a tool `search` aceita qualquer string
  - Modelo envia `search("iphone quinze")` em vez de `search("iPhone 15")`
  - Catálogo retorna vazio → agente diz "não encontramos"
  - Usuário frustrado. Suporte reclama. Time culpa o prompt.
- **O que aconteceu**: a tool não tinha `enum` de variação, não normalizava, não sugeria correção
- **Instinto**: "vamos melhorar o prompt para dizer 'use o nome exato'"
- **Realidade**: refazer a tool com `pattern`, exemplos e fuzzy matching resolve para sempre
- **Pergunta**: *Já tiveram bug onde a solução parecia ser melhorar o prompt mas o problema era a tool?*

**Diagrama**: Split — esquerda: prompt não resolve (loop de remendos) | direita: refatorar a tool resolve
**Animação**: Split — lado esquerdo aparece primeiro, depois lado direito
**Imagem**: Ícone de martelo (prompt) vs chave de fenda (tool)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Este é o problema central da aula. Quando um agente falha sistematicamente, o instinto de todo desenvolvedor é melhorar o prompt. "Vamos dizer ao modelo para fazer X diferente." Mas a maioria das falhas sistêmicas — as que acontecem de novo e de novo — vem de tools mal desenhadas. Prompt é remendo. Tool é cura. A Anthropic descobriu isso no SWE-bench: gastaram mais tempo nas tools do que no prompt. E o erro sumiu. Hoje vamos aprender a diagnosticar quando o problema é a tool e como refatorá-la.
💡 ANALOGIA: É como uma porta que não fecha direito. Você pode colocar uma placa "empurre com força" (prompt). Ou pode ajustar a dobradiça (tool). A placa funciona às vezes. A dobradiça resolve para sempre.
❓ PERGUNTA PARA A TURMA: "Já tiveram bug onde a solução parecia ser melhorar o prompt, mas o problema era a tool?" (levantar mãos — a maioria experiente vai levantar)
⚠️ ERROS COMUNS: Alunos acham que "tool bem feita" é tool que funciona quando o modelo acerta os args. Não — é tool que DIFICULTA o modelo errar.
➡️ TRANSIÇÃO: "Para resolver isso, precisamos de uma disciplina. Ela se chama ACI."

---

### Slide 6 — ACI como Disciplina de Design

**Título**: ACI como Disciplina de Design
**Objetivo**: Introduzir ACI como disciplina formal, análoga a HCI.
**Conteúdo**:
- **ACI** = Agent-Computer Interface
- **Analogia da Anthropic**: invista em ACI tanto quanto em HCI
  - HCI: como o HUMANO interage com o computador (UI/UX)
  - ACI: como o MODELO (agente) interage com o computador (tools)
- **Por que é disciplina**: o modelo não pode "perguntar de novo", não pode "olhar de novo", não tem intuição de uso
  - Tudo o que ele sabe sobre a tool está na descrição e no schema
- **Nesta aula**: vamos dos fundamentos (como tool calling funciona) à prática (como projetar, validar, governar)

**Diagrama**: Dois círculos sobrepostos — HCI (humano ↔ UI) e ACI (modelo ↔ tools)
**Animação**: Círculos aparecem um após o outro, depois se sobrepõem
**Imagem**: Ícone de humano (HCI) + ícone de robô (ACI)
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A insight fundamental da Anthropic é que o design de tools é uma disciplina tão séria quanto o design de UI. Quando você desenha uma UI mal, o humano confunde — mas pode perguntar, tentar de novo, ou usar a intuição. Quando você desenha uma tool mal, o modelo confunde — e não tem recurso. Ele só tem a descrição e o schema. Se esses forem vagos, o modelo vai errar. E não vai saber que errou. Esta é a diferença crucial: o modelo é um usuário que não pode pedir esclarecimento. Por isso ACI é mais exigente que HCI.
💡 ANALOGIA: Imagine desenhar uma interface para um usuário cego, mudo, que só pode ler um manual uma vez e nunca perguntar de novo. Você seria EXTREMAMENTE cuidadoso com o manual. A tool é o manual. A descrição é o manual.
➡️ TRANSIÇÃO: "Antes da disciplina, vamos entender o mecanismo. Como o tool calling funciona por baixo dos panos?"

---

## SEÇÃO B — O Mecanismo do Tool Calling (Slides 7-15 · 15 min)

---

### Slide 7 — [SEÇÃO] O Mecanismo do Tool Calling

**Título**: 1 — O Mecanismo do Tool Calling
**Objetivo**: Transição visual para o bloco de fundamentos do tool calling.
**Conteúdo**: Número "1" grande + "O Mecanismo do Tool Calling"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "1" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Início do bloco de mecanismo. Vamos responder: o que acontece quando o modelo "chama uma tool"? Como o JSON viaja? O que é JSON Schema? O que são structured outputs? Quanto custa em tokens?
➡️ TRANSIÇÃO: "Comecemos pelo fluxo básico do function calling."

---

### Slide 8 — Function Calling: Do Prompt para JSON

**Título**: Function Calling: Do Prompt para JSON
**Objetivo**: Mostrar o fluxo completo do function calling — do prompt do usuário à execução da tool e volta.
**Conteúdo**:
- **O fluxo** (4 passos):
  1. **Usuário envia mensagem** + **tools disponíveis** (com descrições e schemas)
  2. **LLM decide**: responder direto OU chamar tool
     - Se chamar tool: retorna `tool_call` com nome + args em JSON
  3. **Runtime executa** a tool com os args
  4. **Resultado (observation)** volta ao LLM como mensagem `role: "tool"`
  5. LLM usa a observation para gerar próxima resposta (ou novo tool_call)
- **Onde mora a inteligência**: o LLM decide QUAL tool e QUAIS args
- **Onde mora a confiabilidade**: o design da tool (descrição + schema + error handling)

**Diagrama**: `D1` — Diagrama de sequência (Usuário → LLM → Tool → LLM → Usuário)
**Animação**: Setas aparecem sequencialmente
**Imagem**: Diagrama de sequência D1
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Function calling é o mecanismo padrão desde 2023 (OpenAI jun/2023, Anthropic pouco depois). O LLM recebe, além do prompt, uma lista de tools com descrições e schemas. Durante a geração, o modelo pode decidir NÃO responder direto, mas produzir um `tool_call` — um JSON estruturado com o nome da tool e os argumentos. O runtime (seu código) captura esse JSON, executa a função real, e devolve o resultado como uma mensagem com `role: "tool"`. O LLM então usa esse resultado para continuar. A intelligence está em decidir QUAL tool e QUAIS args. A confiabilidade está no design da tool — se a descrição é clara e o schema é restritivo, o modelo acerta. Se não, erra sistematicamente.
💡 ANALOGIA: É como um garçom (LLM) que tem um menu de ações (tools). O cliente pede algo. O garçom decide: responder direto ("sim, temos isso") ou ir à cozinha (chamar tool). Se o menu é claro, o garçom pede certo. Se o menu é confuso, o garçom erra o pedido.
❓ PERGUNTA PARA A TURMA: "Onde vocês acham que mora mais bug — na decisão do modelo ou na execução da tool?" (Resposta: na decisão, mas a CAUSA costuma ser design da tool)
➡️ TRANSIÇÃO: "O contrato entre modelo e tool é o JSON Schema. Vamos vê-lo."

---

### Slide 9 — JSON Schema como Contrato

**Título**: JSON Schema como Contrato
**Objetivo**: Mostrar um JSON Schema completo e explicar cada parte.
**Conteúdo**:
- **JSON Schema** = contrato formal que descreve nome, descrição e parâmetros da tool
- **Exemplo completo** — `search_product`:
```json
{
  "type": "function",
  "function": {
    "name": "search_product",
    "description": "Busca um produto pelo nome exato ou parcial no catálogo. Retorna preço, disponibilidade e SKU. Use esta tool quando o usuário perguntar sobre preço, estoque ou detalhes de um produto específico. NÃO use para listar todos os produtos — use list_products para isso.",
    "parameters": {
      "type": "object",
      "properties": {
        "query": {
          "type": "string",
          "description": "Nome do produto ou parte do nome. Exemplo: 'iPhone 15' ou 'notebook Dell'"
        },
        "category": {
          "type": "string",
          "enum": ["electronics", "clothing", "food", "books"],
          "description": "Categoria para filtrar. Opcional — omita se não souber."
        }
      },
      "required": ["query"]
    }
  }
}
```
- **Partes-chave**:
  - `name` — verbo + objeto (clareza)
  - `description` — o QUÊ, QUANDO usar, QUANDO NÃO usar
  - `enum` — poka-yoke (restringe valores)
  - `required` — o que é obrigatório

**Diagrama**: Code block com syntax highlighting + anotações nas partes-chave
**Animação**: Partes-chave destacadas uma a uma (on click)
**Imagem**: Screenshot do VS Code com JSON
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O JSON Schema é o contrato. Tudo o que o modelo sabe sobre a tool vem deste schema. Vejam este exemplo: o nome é `search_product` — verbo + objeto, inequívoco. A descrição diz o que faz, quando USAR e quando NÃO usar (redireciona para `list_products`). O parâmetro `category` é um `enum` — poka-yoke puro, o modelo só pode escolher entre 4 valores. `query` é required. Cada parte do schema é uma oportunidade de clareza OU de ambiguidade. Schema vago = modelo confuso. Schema rico = modelo confiável.
💡 ANALOGIA: É como o contrato de um serviço. Quanto mais específico — "entrega em até 3 dias úteis, via correios, com rastreamento" — menos margem para interpretação. Schema genérico ("entrega rápida") gera conflito.
❓ PERGUNTA PARA A TURMA: "Qual parte de um schema de vocês é mais genérica hoje?" (deixar 1-2 responderem)
⚠️ ERROS COMUNS: Alunos escrevem schemas sem `description` nos parâmetros. O modelo recebe `{"q": {"type": "string"}}` e não faz ideia do que `q` significa.
➡️ TRANSIÇÃO: "Mas o JSON Schema garante que o OUTPUT é válido? Nem sempre. Para isso existe structured outputs."

---

### Slide 10 — Structured Outputs / Constrained Decoding

**Título**: Structured Outputs / Constrained Decoding
**Objetivo**: Explicar como forçar a saída do LLM a seguir o schema (JSON válido garantido).
**Conteúdo**:
- **Problema**: mesmo com schema, o LLM pode produzir JSON inválido (aspas faltando, campos extras)
- **Solução: Structured Outputs / Constrained Decoding**
  - Durante a geração, cada token é validado contra o schema
  - Se o token quebraria o JSON, ele é bloqueado
  - Resultado: JSON válido é matematicamente garantido
- **Como funciona (visão)**:
  - O servidor aplica uma máscara de logits baseada no schema
  - Tokens que violariam a estrutura têm probabilidade = 0
- **OpenAI**: `response_format: {"type": "json_schema", "json_schema": {...}}`
- **Anthropic / outros**: via tool_choice ou bibliotecas como `instructor`
- **Trade-off**: mais confiabilidade, menos flexibilidade (modelo não pode "improvisar")

**Diagrama**: `D2` — Comparação: geração livre vs constrained decoding
**Animação**: Diagrama D2 aparece com wipe
**Imagem**: Diagrama D2
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Structured outputs é uma das inovações mais importantes dos últimos 2 anos. Antes, você mandava o schema e rezava para o modelo produzir JSON válido. Às vezes funcionava, às vezes não — especialmente com schemas complexos. Constrained decoding resolve isso na camada de inferência: durante a geração token a token, o servidor verifica se o token é compatível com o schema. Se não for, bloqueia. O resultado é que o JSON de saída é garantidamente válido. Isso elimina uma classe inteira de bugs — parse errors, campos faltando, tipos errados. OpenAI tem `response_format: json_schema`. Anthropic e outros usam via tool_choice ou bibliotecas como `instructor`.
💡 ANALOGIA: É como um editor de texto com autocomplete que só sugere palavras que fazem sentido gramaticalmente. Você não pode escrever algo que não faça sentido — o editor bloqueia. Constrained decoding é isso para JSON.
⚠️ ERROS COMUNS: Alunos acham que structured outputs substitui o schema. Não substitui — usa o schema. O schema continua sendo a especificação; o constrained decoding é o mecanismo de enforcement.
➡️ TRANSIÇÃO: "E se precisarmos de várias tools em uma resposta?"

---

### Slide 11 — Multi-tool Calls e Paralelismo

**Título**: Multi-tool Calls e Paralelismo
**Objetivo**: Mostrar que o LLM pode chamar múltiplas tools em uma única resposta.
**Conteúdo**:
- **Multi-tool call**: em uma resposta, o LLM pode retornar **mais de um** `tool_call`
  - Ex.: "Compare iPhone 15 e Samsung S24" → 2 calls: `search_product("iPhone 15")` + `search_product("Samsung S24")`
- **Paralelismo**: o runtime pode executar as tools em paralelo (asyncio)
  - Latência total = max(tool_1, tool_2), não soma
- **Quando o modelo faz isso**: quando as informações são independentes
- **Cuidado**: tools com dependência (a saída de uma é entrada da outra) NÃO podem ser paralelizadas
- **Boa prática**: projetar tools independentes facilita paralelismo automático

**Diagrama**: `D3` — Multi-tool em paralelo (1 LLM response → 2 tools → merge)
**Animação**: Tools executam em paralelo (barras crescem juntas)
**Imagem**: Diagrama D3
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Modelos modernos suportam multi-tool calls — em uma resposta, podem pedir múltiplas tools. Isso é poderoso para latência: se o usuário pede "compare A e B", o modelo pode pedir as duas buscas de uma vez, e o runtime executa em paralelo. Latência total é o máximo, não a soma. Mas cuidado: se a tool B depende da saída da tool A (ex.: buscar usuário, depois buscar pedidos desse usuário), o modelo precisa fazer sequencialmente — uma tool_call, esperar observation, outra tool_call. O modelo geralmente sabe fazer isso, mas vale monitorar.
💡 ANALOGIA: É como um garçom que anota o pedido inteiro da mesa de uma vez (multi-call) em vez de ir e voltar para cada prato (sequential). Mais eficiente — mas só funciona se os pratos forem independentes.
➡️ TRANSIÇÃO: "Tudo isso tem um custo. Vamos falar de tokens."

---

### Slide 12 — Custo: Tokens de Descrição vs Benefício

**Título**: Custo: Tokens de Descrição vs Benefício
**Objetivo**: Mostrar o trade-off de adicionar tools — cada uma custa tokens em toda chamada.
**Conteúdo**:
- **Cada tool** envia sua descrição + schema no prompt de toda chamada
- **Exemplo de custo**:
  - 1 tool com descrição de 200 tokens = +200 tokens por chamada
  - 10 tools = +2.000 tokens por chamada
  - 30 tools = +6.000 tokens por chamada
- **Cálculo** (gpt-4o-mini, $0.15/1M input):
  - 10 tools × 200 tokens = 2k tokens × $0.15/1M = $0.0003/chamada
  - 1.000 chamadas/dia × 30 dias = $9/mês só em descrição
  - 30 tools = $27/mês
- **O trade-off**: mais tools = mais capacidade, MAS mais custo E mais confusão (Gorilla: degradação com >1.700)
- **Solução**: MCP (ETHAGT08) — descoberta dinâmica de tools

**Diagrama**: Tabela: N tools × tokens × custo mensal
**Animação**: Linhas da tabela aparecem uma a uma
**Imagem**: Gráfico de barras crescente
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Cada tool adicionada ao agente tem um custo recorrente: sua descrição e schema são enviados em TODA chamada. Não é one-time — é por request. Com 10 tools de 200 tokens, são 2k tokens extras por chamada. Parece pouco, mas em escala (1k chamadas/dia), são $9/mês só para descrever as tools ao modelo. Com 30 tools, $27/mês. E pior: o paper Gorilla mostrou que a performance do modelo degrada com muitas tools disponíveis — ele fica confuso, escolhe errado, mistura args. A solução de longo prazo é MCP (Model Context Protocol, ETHAGT08), que permite descoberta dinâmica — o modelo só vê as tools relevantes. Mas por ora, a lição é: menos tools, melhor. Consolidar > multiplicar.
💡 ANALOGIA: É como um cardápio de restaurante. Cardápio com 10 pratos: o cliente decide rápido. Cardápio com 200 pratos: o cliente trava, pede errado, demora. Menos opções, mais clareza.
❓ PERGUNTA PARA A TURMA: "Quantas tools vocês têm no agente de produção de vocês?" (Calibrar — maioria tem 5-15)
➡️ TRANSIÇÃO: "Vamos ver o antes e depois de uma tool bem vs mal descrita."

---

### Slide 13 — Tool Bem vs Mal Descrita

**Título**: Tool Bem vs Mal Descrita
**Objetivo**: Comparação visual direta de uma tool mal desenhada vs bem desenhada.
**Conteúdo**:
- **Duas colunas comparativas**:

| ❌ Mal descrita | ✅ Bem descrita |
|---|---|
| `name: "search"` | `name: "search_product"` |
| `description: "Busca produtos."` | `description: "Busca produto por nome. Retorna preço e SKU. Use quando..."` |
| `q: {type: string}` (sem desc) | `query: {type: string, description: "Nome do produto..."}` |
| `c: {type: string}` (sem enum) | `category: {type: string, enum: [...]}` |
| Sem `required` | `required: ["query"]` |

- **Impacto**: a mal descrita gera ~40% de uso incorreto; a bem descrita, <10%

**Diagrama**: `D3` — Comparação lado a lado
**Animação**: Colunas aparecem uma a uma; diferenças destacadas em vermelho/verde
**Imagem**: Duas telas de código lado a lado
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esta é a diferença entre uma tool que funciona 60% das vezes e uma que funciona 90%+. Cada elemento da coluna da direita é um poka-yoke ou uma clareza: nome diz o que faz, descrição diz quando usar, parâmetros têm descrição, enum restringe, required é explícito. A tool da esquerda é o que 80% dos desenvolvedores escrevem — e é por isso que 80% dos agentes têm bugs sistemáticos. A boa notícia: refatorar de uma para a outra leva 10 minutos. E resolve bugs que meses de prompt engineering não resolveram.
💡 ANALOGIA: É como a diferença entre um manual de instrução de 1 página ("use o botão") e um manual de 10 páginas com diagramas, exemplos e troubleshooting. O de 1 página parece suficiente até você tentar usar.
➡️ TRANSIÇÃO: "Vamos ver isso rodando ao vivo."

---

### Slide 14 — DEMO: Tool Calling na Prática

**Título**: DEMO — Tool Calling na Prática
**Objetivo**: Mostrar tool calling funcionando ao vivo com OpenAI SDK.
**Conteúdo**:
- **Demo ao vivo**:
  - Definir 1 tool: `search_product`
  - Enviar mensagem do usuário: "Tem iPhone 15?"
  - Mostrar o `tool_call` retornado pelo LLM
  - Executar a tool (mock)
  - Devolver observation
  - LLM gera resposta final
- **Código** (~30 linhas):
```python
from openai import OpenAI
import json

client = OpenAI()

tools = [{
    "type": "function",
    "function": {
        "name": "search_product",
        "description": "Busca produto por nome. Retorna preço e estoque.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Nome do produto"}
            },
            "required": ["query"]
        }
    }
}]

def search_product(query):
    return {"name": "iPhone 15", "price": 7999, "stock": 12}

messages = [{"role": "user", "content": "Tem iPhone 15?"}]
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    tools=tools
)
msg = response.choices[0].message
messages.append(msg)

for tc in msg.tool_calls:
    args = json.loads(tc.function.arguments)
    result = search_product(**args)
    messages.append({"role": "tool", "tool_call_id": tc.id, "content": json.dumps(result)})

final = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
print(final.choices[0].message.content)
```

**Diagrama**: Code block (esquerda) + terminal (direita) side-by-side
**Animação**: Highlight de linhas chave durante execução
**Imagem**: Screenshot do VS Code + terminal
**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esta é a parte mais importante da Seção B. Vamos rodar tool calling REAL em 30 linhas. Prestem atenção em três momentos: (1) como o modelo decide chamar a tool (ele retorna `tool_calls` em vez de content); (2) como capturamos o JSON de args e executamos a função; (3) como devolvemos o resultado como `role: "tool"` e o modelo gera a resposta final. Esta é a essência do function calling. Tudo o que vimos de ACI se aplica a este fluxo — a diferença entre uma tool boa e ruim é a diferença entre esta demo funcionar sempre ou às vezes.
💡 ANALOGIA: É como ver o motor de tool calling funcionando com o capô aberto. Depois disso, quando usarem LangChain ou qualquer framework, vão saber exatamente o que está acontecendo.
⚠️ ERROS COMUNS: Se a demo falhar (API indisponível), tenho screenshot do trace. Não tentar debugar ao vivo — mostrar o screenshot e seguir.
➡️ TRANSIÇÃO: "Antes de seguir, uma pergunta para vocês em duplas."

---

### Slide 15 — Pergunta da Demo

**Título**: O Que Acontece Se...?
**Objetivo**: Engajar a turma com perguntas sobre edge cases da demo.
**Conteúdo**:
- **Pergunta 1**: "O que acontece se o modelo enviar `op='×'` em vez de `op='*'`?"
- **Pergunta 2**: "E se o modelo não chamar tool nenhuma?"
- **Pergunta 3**: "E se o modelo chamar uma tool que não existe?"
- **Discussão em duplas** (2 min)
- **Compartilhar** (1 min)

**Diagrama**: Caixa de discussão com 3 perguntas
**Animação**: Perguntas aparecem uma a uma
**Imagem**: Ícone de balão de discussão
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Deixem os alunos discutirem em duplas por 2 minutos. As respostas esperadas: (1) Se `op='×'`, a função `calculator` recebe um valor não previsto — se não houver enum, o modelo pode alucinar qualquer string como operador. Poka-yoke: usar `enum: ["+", "-", "*", "/"]`. (2) Se o modelo não chama tool, o código não entra no `for tc in msg.tool_calls` e vai direto para a resposta final — pode estar errada. (3) Se chamar tool inexistente, `search_product(**args)` falha com erro. Sem validação de nome, o runtime quebra. A lição: cada um destes cenários precisa ser tratado — enum, fallback, validação de tool name.
💡 ANALOGIA: É como perguntar "o que acontece se o cliente pedir um item que não está no cardápio?" antes de abrir o restaurante. Você não espera o problema — você prevê.
⚠️ ERROS COMUNS: Alunos acham que o modelo "sabe" tratar erros. Não sabe — ele só vê a Observation. Se for um traceback de Python, fica confuso. Retornar `{"error": "...", "suggestion": "..."}`.
➡️ TRANSIÇÃO: "Agora que entendemos o mecanismo, vamos à disciplina: ACI."

---

## SEÇÃO C — ACI como Disciplina (Slides 16-26 · 15 min)

---

### Slide 16 — [SEÇÃO] ACI como Disciplina de Design

**Título**: 2 — ACI como Disciplina de Design
**Objetivo**: Transição visual para o bloco de ACI.
**Conteúdo**: Número "2" grande + "ACI como Disciplina de Design"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "2" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Já entendemos COMO o tool calling funciona. Agora vamos ao COMO PROJETAR bem. Esta seção é o coração da aula — os 5 princípios da Anthropic para ACI. Se vocês só lembrarem de uma coisa hoje, devem ser estes princípios.
➡️ TRANSIÇÃO: "Comecemos pela analogia fundamental."

---

### Slide 17 — A Analogia: ACI :: HCI

**Título**: A Analogia: ACI :: HCI
**Objetivo**: Estabelecer a analogia central que fundamenta toda a disciplina.
**Conteúdo**:
- **HCI** (Human-Computer Interface): como o HUMANO interage com software
  - Disciplina madura: Fitts' Law, heurísticas de Nielsen, design de UI
  - Investimos milhões em HCI porque humano confuso = produto falha
- **ACI** (Agent-Computer Interface): como o MODELO interage com software
  - Disciplina nova, mas igualmente crítica
  - Investir em ACI = investir em HCI
- **Diferença crítica**: o humano pode pedir esclarecimento, tentar de novo, usar intuição
  - O modelo NÃO pode — só tem a descrição e o schema
  - Por isso ACI é MAIS exigente que HCI
- **Citação**: "Tools are how agents take action in the world. Invest in them accordingly." — Anthropic

**Diagrama**: Comparação lado a lado — HCI (humano ↔ UI) vs ACI (modelo ↔ tools)
**Animação**: Duas colunas aparecem; diferenças destacadas
**Imagem**: Ícone de humano + ícone de robô
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esta é a insight mais importante da aula. Quando vocês desenham uma UI, pensam em cada detalhe: onde o botão fica, qual cor, qual texto, qual feedback. Quando desenham uma tool, a maioria NÃO pensa assim — escreve `description: "Busca produtos"` e segue. Mas a tool é a UI do modelo. E o modelo é um usuário mais limitado que o humano: não pode perguntar de novo, não pode tentar, não tem intuição. Tudo o que ele sabe está na descrição e no schema. Se vocês tratam ACI com menos rigor que HCI, o agente vai falhar sistematicamente. A Anthropic trata ACI com o MESMO rigor. Por isso os agentes deles funcionam.
💡 ANALOGIA: Imagine desenhar uma interface para um usuário que é cego, mudo, e só pode ler o manual uma vez. Você seria obsessivo com a clareza do manual. ACI é isso.
❓ PERGUNTA PARA A TURMA: "Vocês dedicam mais tempo a UI/UX ou a design de tools?" (Quase todos dirão UI/UX — este é o ponto)
➡️ TRANSIÇÃO: "Vamos aos 5 princípios. Princípio 1."

---

### Slide 18 — Princípio 1: Ponha-se no Lugar do Modelo

**Título**: Princípio 1 — Ponha-se no Lugar do Modelo
**Objetivo**: Introduzir o princípio da empatia com o modelo como usuário da tool.
**Conteúdo**:
- **O princípio**: antes de escrever a descrição, pergunte-se:
  - "Se eu fosse o modelo, com ZERO contexto além desta descrição, eu saberia usar?"
  - "Eu saberia QUANDO usar esta tool vs outra?"
  - "Eu saberia quais args passar?"
- **Exercício mental**: leia apenas a descrição da tool. Decida: usaria? Com quais args?
- **Anti-pattern**: escrever para outro desenvolvedor humano ("busca produtos" — claro para você, opaco para o modelo)
- **Prática**: escrever como se fosse um docstring para um estagiário JÚNIOR que nunca viu o sistema

**Diagrama**: Ícone de empatia (coração + engrenagem)
**Animação**: Perguntas aparecem uma a uma
**Imagem**: Ícone de cérebro pensando
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O primeiro princípio é empatia. Parece óbvio, mas quase ninguém faz. O desenvolvedor escreve a descrição pensando "eu sei o que esta tool faz" — mas o modelo não é o desenvolvedor. O modelo só tem as palavras da descrição. A regra prática da Anthropic: escreva a descrição como um docstring para um estagiário júnior que nunca viu o sistema. Se o estagiário entender, o modelo entende. Se o estagiário perguntar "mas quando eu uso isso?", sua descrição está incompleta.
💡 ANALOGIA: É como escrever um manual para alguém que não pode ligar para você. Cada manual de IKEA é desenhado assim — sem texto, só figuras, porque o usuário pode não falar sua língua. A descrição da tool é o manual IKEA do modelo.
⚠️ ERROS COMUNS: Alunos escrevem descrições técnicas ("executa query parametrizada no ORM"). O modelo não sabe o que é ORM. Escreva no idioma do modelo: "busca registros no banco de dados".
➡️ TRANSIÇÃO: "Princípio 2: descrições ricas."

---

### Slide 19 — Princípio 2: Descrições Ricas

**Título**: Princípio 2 — Descrições Ricas
**Objetivo**: Mostrar o padrão de uma descrição completa: o QUÊ, QUANDO, COMO, EXEMPLO.
**Conteúdo**:
- **Uma descrição rica responde 4 perguntas**:
  1. **O QUÊ** a tool faz (resultado, formato de saída)
  2. **QUANDO** usar (gatilhos, contexto)
  3. **QUANDO NÃO** usar (redireciona para outra tool)
  4. **EXEMPLO** de uso (args concretos)
- **Template**:
  > "[O QUÊ]. Retorna [formato]. Use esta tool quando [QUANDO]. NÃO use para [QUANDO NÃO] — use [alternativa]. Exemplo: tool('valor_exemplo')."
- **Antes**: `"Envia email."`
- **Depois**: `"Envia um email transacional para o cliente. Requer destinatário validado, assunto e corpo em texto puro. Use para confirmações de pedido e notificações. NÃO use para marketing em massa — use send_bulk_email. Exemplo: send_email(to='cliente@email.com', subject='Pedido confirmado', body='Seu pedido #123 foi recebido.')"`

**Diagrama**: Template visual com 4 campos coloridos
**Animação**: Campos do template preenchem um a um
**Imagem**: Formulário com 4 seções
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A descrição rica segue um template: o quê, quando, quando não, exemplo. Vejam a diferença entre "Envia email" e a versão completa. A versão completa diz: o que faz (email transacional), o formato (texto puro), quando usar (confirmações, notificações), quando NÃO usar (marketing — redireciona para send_bulk_email), e dá um exemplo concreto. O modelo com esta descrição raramente erra. O modelo com "Envia email" erra frequentemente — não sabe que é só texto puro, não sabe que não é para marketing, não tem exemplo de formato. Cada palavra da descrição rica economiza 10 tentativas erradas.
💡 ANALOGIA: É como a diferença entre "consulte o site" e "consulte a página /suporte/faq entre 9h e 18h, clique em 'Minha Conta' > 'Pedidos' > 'Rastrear'". A segunda instrução não deixa margem.
➡️ TRANSIÇÃO: "Princípio 3: formato próximo ao natural."

---

### Slide 20 — Princípio 3: Formato Próximo ao Natural

**Título**: Princípio 3 — Formato Próximo ao Natural
**Objetivo**: Mostrar que o formato dos args e da observation deve ser natural ao modelo, não técnico.
**Conteúdo**:
- **O princípio**: os dados que entram e saem da tool devem estar no formato mais natural para o modelo gerar e interpretar
- **Evitar**:
  - Escaping desnecessário (JSON dentro de string dentro de JSON)
  - Diffs complexos como args (ex.: `old_text`, `new_text` com whitespace sensível)
  - Formatos técnicos que o modelo não treina bem (base64, hex, protobuf)
- **Preferir**:
  - JSON estruturado simples
  - Texto natural
  - Listas e objetos nativos
- **Caso real (Anthropic SWE-bench)**: ao invés de pedir `edit_file(old="def foo():\n    pass", new="def foo():\n    return 42")`, usar `str_replace_editor(command="replace", path="...", old_str="...", new_str="...")`
- **Trade-off**: às vezes o formato natural é mais verboso, mas a acurácia compensa

**Diagrama**: Comparação — formato técnico (confuso) vs formato natural (claro)
**Animação**: Transformação do técnico para natural (morph)
**Imagem**: Dois blocos de código
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O modelo é treinado em texto natural — prosa, código, JSON simples. Ele NÃO é treinado em diffs unificados, em JSON escapado dentro de string, em base64. Se vocês pedem para o modelo gerar um diff complexo como argumento, ele vai errar — whitespace sensível, escaping de aspas, contagem de linhas. A solução é simplificar o formato: ao invés de diff, usar um comando de replace que o modelo entende naturalmente. A Anthropic fez exatamente isso no SWE-bench. A regra: se o modelo precisa "pensar muito" para gerar o arg, o formato está errado.
💡 ANALOGIA: É como pedir para alguém escrever à mão um documento em latim vs em português. Mesmo conteúdo, mas um vai ter erros e o outro não. Use o idioma nativo do modelo.
➡️ TRANSIÇÃO: "Princípio 4: poka-yoke. Este é o mais poderoso."

---

### Slide 21 — Princípio 4: Poka-yoke

**Título**: Princípio 4 — Poka-yoke (Torne o Erro Impossível)
**Objetivo**: Apresentar o conceito de poka-yoke aplicado a design de tools.
**Conteúdo**:
- **Poka-yoke** (japonês): "prevenção de erros" — design que torna o erro impossível
- **Na manufatura**: encaixe que só permite montagem na direção correta
- **Em ACI**: tool que só aceita args válidos, impossibilitando erro
- **Caso canônico (Anthropic SWE-bench)**:
  - **Problema**: agente usava paths relativos errados após sair do diretório raiz
  - **Solução frágil**: "melhorar o prompt para dizer 'use paths absolutos'" (modelo pode esquecer)
  - **Solução robusta (poka-yoke)**: mudar a tool para EXIGIR path absoluto via regex `^/.+`
  - **Resultado**: erro desapareceu, sem mexer no prompt
- **Outros exemplos de poka-yoke em tools**:
  - `enum` em vez de `string` livre
  - `format: email` em vez de `string`
  - `exclusiveMinimum: 0` em valores
  - `pattern: ^\d{4}$` para CEP

**Diagrama**: `D4` — Antes (path relativo → erro) → Depois (path absoluto → sucesso)
**Animação**: Transformação antes → depois (morph)
**Imagem**: Ícone de escudo (proteção)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Este é o princípio mais transformador. Poka-yoke é um conceito da manufatura japonesa (Toyota) — desenhar peças de forma que o erro de montagem seja fisicamente impossível. Em ACI, é desenhar a tool de forma que o erro seja estruturalmente impossível. O caso canônico é o SWE-bench: a Anthropic tinha um bug onde o agente usava paths relativos errados. A solução óbvia era "dizer no prompt para usar paths absolutos". Mas isso é frágil — o modelo pode esquecer, especialmente em conversas longas. A solução robusta foi mudar a tool: em vez de aceitar qualquer path, passou a exigir path absoluto via regex. Aí o modelo NÃO PODE errar, mesmo que queira. Poka-yoke. O erro desapareceu sem mexer no prompt. Este é o poder do poka-yoke: resolve na raiz, não no sintoma.
💡 ANALOGIA: É como colocar uma proteção numa tomada para que uma criança não enfie o dedo. Você pode "ensinar a criança a não colocar o dedo" (prompt). Ou pode colocar a proteção (poka-yoke na tool). A proteção funciona mesmo se a criança esquecer a lição. E crianças esquecem. Modelos também.
❓ PERGUNTA PARA A TURMA: "Qual tool de vocês poderia receber poka-yoke hoje?" (Deixar 1-2 responderem)
➡️ TRANSIÇÃO: "Princípio 5: dê espaço para o modelo pensar."

---

### Slide 22 — Princípio 5: Tokens para Pensar

**Título**: Princípio 5 — Dê Tokens para o Modelo Pensar
**Objetivo**: Mostrar que max_tokens generoso permite reasoning antes da tool_call.
**Conteúdo**:
- **O princípio**: o modelo "pensa" gerando tokens. Se max_tokens é baixo, ele é cortado antes de raciocinar
- **Impacto**: max_tokens=100 pode cortar o raciocínio antes da tool_call → JSON incompleto
- **Boa prática**:
  - max_tokens generoso (≥1000 para respostas com tool_call)
  - Permitir chain-of-thought antes da decisão
  - Modelos com reasoning (o1, Claude thinking) precisam de ainda mais espaço
- **Trade-off**: mais tokens = mais custo, mas acurácia compensa
- **Anti-pattern**: max_tokens=50 "para economizar" → tool_calls quebrados, erros sistemáticos

**Diagrama**: Comparação — max_tokens baixo (cortado) vs alto (raciocínio completo)
**Animação**: Barra de tokens cresce; linha de corte se move
**Imagem**: Ícone de balão de pensamento
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O modelo raciocina gerando tokens. Se você corta cedo (max_tokens baixo), corta o raciocínio. Em tool calling, isso é crítico: o modelo precisa "pensar" qual tool usar, quais args, e então gerar o JSON. Se max_tokens=100 e o raciocínio leva 80 tokens, sobram 20 para o JSON — que pode sair incompleto. A regra: para respostas que envolvem tool_call, use max_tokens generoso (1000+). Para modelos com reasoning explícito (o1, Claude com extended thinking), ainda mais. O custo extra de tokens vale a acurácia.
💡 ANALOGIA: É como pedir para alguém resolver um problema de matemática mas dar 10 segundos. Eles não pensam — chutam. Dê 2 minutos e eles resolvem direito. max_tokens é o tempo de pensamento.
➡️ TRANSIÇÃO: "Vamos praticar. Exercício em trios."

---

### Slide 23 — Exercício: O Que Está Faltando?

**Título**: Exercício — O Que Está Faltando no send_email?
**Objetivo**: Aplicar os 5 princípios na prática — diagnosticar uma tool incompleta.
**Conteúdo**:
- **Em trios (3 min)**: analisem a tool abaixo e listem o que está faltando:

```json
{
  "name": "send_email",
  "description": "Envia um email.",
  "parameters": {
    "type": "object",
    "properties": {
      "to": {"type": "string"},
      "subject": {"type": "string"},
      "body": {"type": "string"}
    }
  }
}
```

- **Perguntas-guia**:
  1. A descrição responde o QUÊ, QUANDO, QUANDO NÃO, EXEMPLO?
  2. Há poka-yoke (enum, format, pattern)?
  3. Há required?
  4. É uma tool destrutiva? Precisa de HITL?
  5. Há idempotência (request_id)?

**Diagrama**: Tool exibida com campos marcados como "?"
**Animação**: Campos piscam indicando lacunas
**Imagem**: Código com pontos de interrogação
**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Deixem os trios discutirem por 2 minutos. As respostas esperadas: descrição vazia ("Envia email" não diz o quê, quando, exemplo); `to` sem `format: email`; sem `cc`/`bcc`; sem `dry_run` ou preview; sem `request_id` para idempotência; sem `required`; e CRUCIAL: send_email é uma tool DESTRUTIVA (external side-effect irreversível) — precisa de HITL. Cada um destes é uma oportunidade de poka-yoke e clareza. A tool "depois" (próximo slide) resolve tudo isso.
💡 ANALOGIA: É como revisar um contrato antes de assinar. Cada cláusula faltando é uma brecha para erro.
➡️ TRANSIÇÃO: "Vamos ver o antes e depois."

---

### Slide 24 — Antes vs Depois: Refatoração ACI

**Título**: Antes vs Depois — Refatoração ACI do send_email
**Objetivo**: Mostrar a versão refatorada da tool do exercício anterior.
**Conteúdo**:
- **Antes** (do exercício): descrição vazia, sem poka-yoke, sem HITL
- **Depois** (refatorado):
```json
{
  "name": "send_email",
  "description": "Envia um email transacional para o cliente. Requer destinatário validado, assunto e corpo em texto puro. Use para confirmações de pedido e notificações. NÃO use para marketing em massa — use send_bulk_email. Exemplo: send_email(to='cliente@email.com', subject='Pedido #123', body='Seu pedido foi recebido.').",
  "parameters": {
    "type": "object",
    "properties": {
      "request_id": {"type": "string", "format": "uuid", "description": "ID único para idempotência. Reuse em retentativas."},
      "to": {"type": "string", "format": "email", "description": "Email do destinatário."},
      "subject": {"type": "string", "maxLength": 100, "description": "Assunto. Máx 100 chars."},
      "body": {"type": "string", "description": "Corpo em texto puro."},
      "dry_run": {"type": "boolean", "default": false, "description": "Se true, retorna preview sem enviar."}
    },
    "required": ["request_id", "to", "subject", "body"]
  }
}
```
- **Melhorias**: descrição rica, format email, maxLength, request_id (idempotência), dry_run, required explícito

**Diagrama**: `D3` — Comparação antes/depois lado a lado
**Animação**: Transformação do antes para depois (morph)
**Imagem**: Dois blocos de código
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vejam a diferença. A versão refatorada tem: descrição completa (quê, quando, quando não, exemplo), `format: email` em `to` (poka-yoke — o modelo não pode enviar email inválido), `maxLength` em subject, `request_id` com UUID (idempotência — retentativas não duplicam), `dry_run` (permite preview antes de enviar), e `required` explícito. Cada uma destas mudanças reduz uma classe de erro. A versão "antes" gera ~40% de uso incorreto. A "depois", <10%. E levou 10 minutos para refatorar.
💡 ANALOGIA: É como a diferença entre um contrato de 1 parágrafo ("você faz o trabalho") e um contrato de 5 páginas com cláusulas de escopo, prazo, pagamento e rescisão. O segundo é mais longo mas não deixa brecha para interpretação.
➡️ TRANSIÇÃO: "Isto não é teoria. A Anthropic fez exatamente isso. Vamos ao caso real."

---

### Slide 25 — Caso Real: Anthropic SWE-bench

**Título**: Caso Real — Anthropic Coding Agent no SWE-bench
**Objetivo**: Mostrar o caso real que originou os princípios ACI.
**Conteúdo**:
- **Contexto**: Anthropic construiu um agente para resolver issues reais de GitHub (SWE-bench)
  - Tools: `view_file`, `edit_file`, `run_tests`
  - Arquitetura: Augmented LLM + loop + sandbox
- **O bug**: agente saía do diretório raiz e usava paths relativos errados
  - `view_file("src/main.py")` → arquivo não encontrado
  - Agente travava, gastava steps, falhava
- **Solução ingênua**: "adicionar ao prompt: 'use paths absolutos sempre'"
  - Funcionava às vezes. Modelo esquecia em conversas longas.
- **Solução robusta (poka-yoke)**: mudar `view_file` para exigir path absoluto
  - `pattern: ^/.+` no schema
  - Modelo NÃO PODE usar path relativo, mesmo que queira
- **Resultado**: erro desapareceu completamente. Sem mexer no prompt.

**Diagrama**: `D5` — Arquitetura do coding agent (issue → agente com tools → loop → patch)
**Animação**: Fluxo aparece step-by-step; destaque no view_file
**Imagem**: Diagrama de arquitetura
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Este caso é a evidência empírica de que ACI funciona. A Anthropic enfrentou um bug real em produção — não um exemplo de sala de aula. O agente usava paths relativos errados. O instinto de qualquer engenheiro seria melhorar o prompt. Eles tentaram. Funcionou parcialmente — o modelo "lembrava" na maioria das vezes, mas esquecia em conversas longas. A solução definitiva foi poka-yoke: mudar a tool para exigir path absoluto via regex. A partir daí, o erro era ESTRUTURALMENTE impossível. O modelo não podia errar mesmo que quisesse. Este caso é tão importante que vira citação recorrente em toda a literatura de ACI.
💡 ANALOGIA: É como resolver o problema de "pessoas batendo o carro na garagem". Você pode colocar uma placa "dirija com cuidado" (prompt). Ou pode colocar um poste de proteção (poka-yoke na tool). O poste funciona 100% das vezes. A placa, não.
❓ PERGUNTA PARA A TURMA: "Vocês têm algum bug de agente hoje que poderia ser resolvido com poka-yoke em vez de prompt?" (Deixar responder)
➡️ TRANSIÇÃO: "Qual é a lição geral deste caso?"

---

### Slide 26 — A Lição: Tempo em Tools > Prompt

**Título**: A Lição — Tempo em Tools > Prompt
**Objetivo**: Fixar o princípio mais importante: invista mais tempo nas tools do que no prompt principal.
**Conteúdo**:
- **Citação direta da Anthropic** (SWE-bench):
  > "We spent more time optimizing our tools than the overall prompt."
- **A inversão**: a maioria dos desenvolvedores passa 80% do tempo no prompt e 20% nas tools
  - Deveria ser o inverso: 20% no prompt, 80% nas tools
- **Por quê**:
  - Prompt é global — afeta tudo, mas é "lembrete" frágil
  - Tool é local — afeta uma ação, mas é enforcement estrutural
  - Poka-yoke na tool resolve para sempre; prompt é remendo
- **Checklist mental** ao debugar um agente:
  1. O bug é sistematico (acontece sempre) ou ocasional?
  2. Se sistemático → provavelmente é a tool, não o prompt
  3. A tool tem poka-yoke? A descrição é rica? O schema é restritivo?
  4. Só mexer no prompt depois de confirmar que a tool está bem desenhada

**Diagrama**: Gráfico de pizza — "Tempo gasto" (antes: 80% prompt / depois: 80% tools)
**Animação**: Pizza gira e inverte as fatias
**Imagem**: Duas pizzas comparativas
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Se vocês só lembrarem de UMA coisa desta aula, deve ser esta: tempo em tools > tempo no prompt. A Anthropic foi explícita — gastaram mais tempo otimizando tools do que o prompt principal. Por quê? Porque o prompt é um lembrete global — afeta tudo, mas é frágil. O modelo pode esquecer, especialmente em conversas longas. A tool é enforcement local — afeta uma ação, mas é estrutural. Poka-yoke na tool resolve para sempre. A próxima vez que o agente de vocês falhar sistematicamente, antes de mexer no prompt, perguntem: a tool tem poka-yoke? A descrição é rica? O schema é restritivo? Se a resposta for não em qualquer uma, mexam na tool primeiro.
💡 ANALOGIA: É como educaçao de filhos. Você pode repetir "não toque na tomada" 100 vezes (prompt). Ou pode colocar uma proteção na tomada (poka-yoke na tool). A proteção funciona mesmo quando você não está olhando.
❓ PERGUNTA PARA A TURMA: "Qual erro de design de tools vocês já cometeram?" (Honestidade aqui é valiosa)
➡️ TRANSIÇÃO: "Intervalo. Voltamos em 5 min para engenharia de tools, HITL e avaliação."
