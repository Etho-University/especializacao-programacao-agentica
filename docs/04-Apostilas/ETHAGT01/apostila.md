# ETHAGT01 — Arquitetura Cognitiva de Agentes LLM

> **Apostila do curso** · Especialização em Programação Agêntica · Universidade Etho
> Fase A — Fundamentos Agênticos · Carga 25 h · Versão 1.0 · Julho 2026
> *Material de referência duradouro (nível pós-graduação lato sensu). Os slides são auxiliares.*

---

## Sumário

- **Capítulo 1** — Do LLM ao Agente: o que muda
- **Capítulo 2** — O Augmented LLM: o bloco fundamental
- **Capítulo 3** — O Agent Loop: ReAct
- **Capítulo 4** — Workflows vs Agentes
- **Capítulo 5** — Implementação: do zero vs framework
- **Capítulo 6** — Observabilidade desde o dia 1
- **Capítulo 7** — Casos de estudo
- **Capítulo 8** — Referências e leituras

---

## Capítulo 1 — Do LLM ao Agente: o que muda

### 1.1 O problema do "oráculo de única jogada"

Um modelo de linguagem usado da maneira mais simples funciona como um **oráculo de única jogada** (*single-shot oracle*): você fornece um prompt, o modelo gera uma resposta e a interação termina. Esse padrão é poderoso para tarefas que cabem em uma única inferência — resumir um texto, traduzir, classificar, responder a uma pergunta factual. Mas ele quebra sistematicamente em **tarefas multi-etapas que exigem ação no mundo**.

Considere um exemplo concreto:

> *"Reserve um voo para São Paulo, reserve um hotel perto do local do evento e alugue um carro para o período. Ajuste tudo ao orçamento de R$ 4.000."*

Um LLM puro não pode resolver isso. Ele não tem como consultar preços de voos em tempo real, verificar disponibilidade de hotéis, efetuar uma reserva ou confirmar um pagamento. O máximo que pode fazer é *descrever* como resolveria a tarefa. O salto conceitual da programação agêntica é transformar o LLM de **gerador de texto** em **controlador cognitivo** capaz de, em loop, decidir o que fazer, agir, observar o resultado e decidir novamente.

> **Definição operacional (esta apostila).** Um *agente* é um sistema em que o LLM dirige, dinamicamente, seu próprio processo: decide quais ações executar, em que ordem, e observa seus resultados até julgar a tarefa concluída. A unidade central é o **agent loop**: raciocinar → agir → observar → repetir.

### 1.2 Definições concorrentes de "agente" e o recuo pragmático

A palavra "agente" é notoriamente sobrecarregada. Diferentes comunidades propõem definições incompatíveis:

- **IA clássica (Russell & Norvig):** qualquer coisa que *percebe* o ambiente e *age* sobre ele para atingir um objetivo. Nessa definição, um termostato é um agente.
- **Pesquisa em LLMs (Wang et al., 2023):** um sistema construído sobre um LLM com módulos de *profiling*, *memória*, *planejamento* e *ação*.
- **Indústria (pragmática):** varia entre "qualquer pipeline com um LLM" e "um sistema totalmente autônomo".

Essa ambiguidade gera confusão prática: é comum que equipes discutam se seu sistema "é um agente" sem nunca definir o critério. A publicação canônica *Building Effective Agents* (Anthropic, 2024) resolve isso com um **recuo pragmático**: em vez de debater a fronteira exata, propõe um espectro de **sistemas agênticos** (*agentic systems*) que vai de *workflows* totalmente predefinidos a *agentes* totalmente autônomos. A distinção útil não é binária, mas de **grau de autonomia do LLM sobre o fluxo de controle**.

> **Princípio (Anthropic).** "*Workflows* são sistemas onde os LLMs e ferramentas são orquestrados por caminhos de código predefinidos. *Agentes* são sistemas onde os LLMs dirigem dinamicamente seus próprios processos e o uso de ferramentas, mantendo controle sobre como realizar tarefas."

Adotaremos essa distinção ao longo do curso. Ela tem uma consequência prática imediata: **a primeira pergunta de projeto não é "quero um agente?" mas "quanto controle o LLM deve ter sobre o fluxo?"**. Mais controle traz flexibilidade e menos código de orquestração, mas reduz previsibilidade e aumenta custo, latência e risco. O Capítulo 4 formaliza esse trade-off.

### 1.3 A taxonomia unificada de um agente

Para decompor um agente em partes compreensíveis, adotamos a taxonomia unificada do *survey* de Arunkumar, Gangadharan e Buyya, *Agentic AI: Architectures, Taxonomies, and Evaluation of LLM Agents* (arXiv:2601.12560, 2026). Essa taxonomia é valiosa porque integra contribuições dispersas da literatura em um único modelo de referência:

1. **Perception (Percepção):** como o agente adquire informação do ambiente — prompts do usuário, conteúdo recuperado, resultados de ferramentas, sensores. A percepção determina *o que o agente consegue enxergar* e, portanto, *sobre o que pode raciocinar*.
2. **Brain (Cérebro):** o LLM propriamente dito — o motor de raciocínio e geração. É a componente que interpreta percepções, decide ações e produz linguagem.
3. **Planning (Planejamento):** a capacidade de decompor um objetivo em subpassos (ex.: Chain-of-Thought, Tree-of-Thought, ReWOO). O planejamento é o que permite lidar com tarefas que não cabem em uma única inferência.
4. **Action (Ação):** a execução concreta — chamar uma ferramenta, modificar um arquivo, enviar uma mensagem, fazer uma chamada de API.
5. **Tool Use (Uso de ferramentas):** a seleção e invocação de capacidades externas que estendem o agente para além do que o LLM sabe "de cor" — busca na web, execução de código, consulta a bancos de dados.
6. **Collaboration (Colaboração):** a interação com outros agentes ou humanos — coordenação, delegação, negociação. Esta componente, isolada no agente único, torna-se central nos sistemas multi-agente (Fase C do curso).

> **Diagrama de referência:** [`12-Diagrams/ETHAGT01/augmented-llm.mmd`](../../12-Diagrams/ETHAGT01/augmented-llm.mmd)

Esta apostila — e todo o curso — estrutura-se em torno desses seis blocos. ETHAGT01 estabelece os blocos fundamentais (Brain + Tool Use + Planning mínimos em loop). Os módulos seguintes aprofundam cada um: ETHAGT02 (Tool Use e ACI), ETHAGT04 (Planning), ETHAGT05 (Memory), ETHAGT06/07 (Perception via retrieval e conhecimento), e a Fase C (Collaboration).

### 1.4 Por que agora: a confluência de capacidades

Agentes baseados em LLM não são uma ideia nova — arquiteturas como ReAct (2022) e AutoGPT (2023) existem há anos. Por que a área "decolou" apenas recentemente? A resposta é uma **confluência de maturidade** em três eixos, todos necessários simultaneamente:

1. **Reasoning estruturado.** Modelos contemporâneos raciocinam melhor sobre múltiplas etapas, reduzindo alucinação em cadeia. Isso tornou viável delegar ao LLM decisões de controle de fluxo.
2. **Tool calling nativo.** Os principais provedores passaram a oferecer *function calling* / *tool use* como primitiva de API, com saída estruturada (JSON) e treinamento específico. Antes, tool calling exigia parsing frágil de texto livre.
3. **Janelas de contexto longas.** Contextos de centenas de milhares de tokens permitem manter histórico de observações, resultados de ferramentas e instruções dentro de uma única conversação — a "memória de trabalho" do agente.

A lição de engenharia é importante: **nenhuma dessas capacidades, isoladamente, basta.** Um LLM que raciocina bem mas não age é um oráculo; um que chama ferramentas mas não raciocina é um roteador burro; um que age mas não mantém contexto perde-se após duas etapas. O agente emerge da **integração em loop** dessas capacidades — e é exatamente essa integração que define a arquitetura cognitiva deste capítulo.

---

## Capítulo 2 — O Augmented LLM: o bloco fundamental

### 2.1 A decomposição de Anthropic

A unidade de construção mais útil da programação agêntica não é o "agente completo", mas um bloco menor e combinável que a Anthropic chama de **Augmented LLM** (LLM aumentado). A definição é deliberadamente modular: um Augmented LLM é um LLM envolto por um conjunto de extensões que o tornam capaz de perceber, lembrar e agir. As quatro extensões canônicas são:

- **Retrieval (recuperação):** acesso a conhecimento externo — documentos, bases vetoriais, fontes em tempo real. O ponto crucial é que a recuperação acontece *dentro* do loop: o próprio modelo decide *quando* e *o que* recuperar, gerando suas próprias queries.
- **Tools (ferramentas):** capacidades executáveis — chamadas de API, execução de código, manipulação de arquivos. Ferramentas transformam o LLM de um *falador* em um *fazedor*.
- **Memory (memória):** persistência de estado entre interações. Distingue-se a *working memory* (a janela de contexto, efêmera) da *persistent memory* (armazenamento durável entre sessões).
- **Loop de controle:** o arcabouço que coordena percepção → decisão → ação → observação.

```
                  ┌──────────────────────────────────────────┐
                  │                Augmented LLM              │
   Entrada ──────►│  ┌────────┐  retrieval   ┌─────────────┐  │──────► Resposta / Ação
   (prompt)       │  │  LLM   │◄────────────►│  Memória    │  │
                  │  │ (Brain)│  tools       │ (curto/prazo│  │
                  │  └───┬────┘◄────────────►│  longo prazo)│  │
                  │      │   loop de controle└─────────────┘  │
                  │      └──────────────► Ferramentas / APIs  │
                  └──────────────────────────────────────────┘
```

> **Diagrama de referência:** [`12-Diagrams/ETHAGT01/augmented-llm.mmd`](../../12-Diagrams/ETHAGT01/augmented-llm.mmd)

A vantagem pedagógica dessa decomposição é enorme: **todo sistema agêntico, por mais complexo, é uma composição de Augmented LLMs.** Um agente solitário é um Augmented LLM em loop. Um sistema multi-agente é uma rede de Augmented LLMs que se comunicam. Ao longo do curso, retornaremos sempre a este bloco fundamental quando precisamos entender um sistema — perguntando, para cada componente: *qual LLM, qual retrieval, quais tools, qual memória, qual loop?*

### 2.2 Retrieval in-loop: o modelo gera suas próprias queries

A diferença entre RAG *ingênuo* e RAG *agêntico* é sutil, mas arquitetural. Em um pipeline de RAG tradicional, a recuperação é **estática e externa ao modelo**: um componente fixo busca documentos *antes* da geração, sempre da mesma forma, independentemente do que o modelo "acha". O agente não decide nada sobre a recuperação.

No Augmented LLM, a recuperação é **dinâmica e dirigida pelo modelo**. O LLM recebe, como ferramenta, a capacidade de buscar; então ele *decide*:

- *se* precisa recuperar (talvez já saiba a resposta),
- *o que* buscar (gera a query),
- *quantas vezes* buscar (pode iterar, refinar),
- *como* usar o recuperado (integrar, descartar, buscar novamente).

Essa diferença tem implicações profundas. O RAG agêntico é mais flexível e preciso em tarefas complexas, porque adapta a recuperação ao caso; mas é mais caro (mais chamadas), mais lento (mais round-trips) e mais difícil de avaliar (o caminho de execução varia entre execuções). ETHAGT06 aprofunda esses padrões; aqui registramos apenas o ponto de arquitetura: **no bloco fundamental, retrieval é uma ferramenta, não um pré-processador fixo.**

### 2.3 Tools como extensão de ação

Ferramentas são o mecanismo pelo qual um agente afeta o mundo fora do seu próprio contexto de tokens. Sem tools, um agente só pode produzir texto; com tools, ele pode consultar uma API, executar código, ler e escrever arquivos, enviar e-mails, acionar dispositivos.

Há dois modos históricos de integração de ferramentas:

1. **Prompt-based (antigo):** descreve-se a ferramenta em linguagem natural no prompt e pede-se ao modelo que emita, como texto, um comando a ser *parsado*. Frágil: o modelo pode desformatar, inventar ferramentas, mesclar argumentos.
2. **Function/tool calling nativo (moderno):** provedores treinam modelos para emitir uma chamada de ferramenta em **estrutura rígida** (JSON com schema definido). A API retorna a intenção de chamada de forma separada do conteúdo textual, eliminando o problema de parsing. Hoje é o padrão.

A regra prática é: **sempre que possível, use tool calling nativo.** Reserve o modo prompt-based para modelos que não suportam function calling ou para casos muito experimentais.

> **Nota de profundidade.** O *design* das ferramentas — quais expor, como nomear, como descrever — é tão importante quanto o código que as implementa. Esta é a disciplina chamada **Agent-Computer Interface (ACI)**, tema central de ETHAGT02. Por ora, registre o princípio orientador (Seção 2.5): ferramentas devem ter **interfaces bem documentadas**, como qualquer API de qualidade.

### 2.4 Memory: working memory vs persistent

A memória de um agente divide-se em duas escalas temporais com naturezas técnicas muito distintas:

| Dimensão | Working memory | Persistent memory |
|---|---|---|
| Implementação | Janela de contexto (tokens) | Armazenamento externo (banco, KV store, vetor) |
| Persistência | Efêmera — some ao fim da sessão | Durável — sobrevive entre sessões |
| Custo | Cresce com o uso (mais tokens = mais custo) | Fixo por escrita/leitura |
| Latência | Nenhuma (já está no prompt) | Round-trip de leitura |
| Limite | Tamanho do contexto (teto duro) | Praticamente ilimitado |

A grande armadilha do iniciante é tratar a janela de contexto como se fosse infinita: acumula-se histórico, resultados de ferramentas, documentos recuperados, até estourar o limite — momento em que o comportamento degrada abruptamente (o modelo "esquece" as instruções iniciais). A engenharia de memória consiste justamente em **gerenciar o que entra e sai da working memory** e **quando externalizar para persistent memory**. ETHAGT05 trata isso em profundidade; aqui, o ponto-chave é: *memória não é um detalhe — é uma decisão de arquitetura desde a primeira linha de código.*

### 2.5 A regra de ouro: interface bem documentada

Qualquer componente do Augmented LLM — ferramenta, fonte de retrieval, esquema de memória — deve ser tratado como uma **API**: com nome claro, descrição precisa, tipos de entrada e saída definidos, exemplos de uso e tratamento de erro explícito. Isso vale não só para consumo humano (manutenção) mas, crucialmente, para consumo *pelo próprio modelo*: o LLM escolhe ferramentas **lendo suas descrições**. Uma descrição ambígua é uma ferramenta que o modelo usará errado.

> **Princípio (Anthropic).** *Spend the effort to make the interface [of tools] well-documented.* O tempo investido em descrever bem uma ferramenta paga-se em menos erros, menos loops e menos custo.

Voltaremos a este princípio no Capítulo 5 (implementação) e o aprofundaremos em ETHAGT02.

---

## Capítulo 3 — O Agent Loop: ReAct

### 3.1 O padrão fundacional

Se o Augmented LLM é o bloco, o **agent loop** é o motor que o põe em movimento. O padrão de loop mais fundacional e influente é o **ReAct** (Yao et al., *ReAct: Synergizing Reasoning and Acting in Language Models*, ICLR 2023; arXiv:2210.03629). O nome condensa a tese: unir **Rea**soning (raciocínio) e **Act**ing (ação).

O ciclo é elegantemente simples:

```
┌─────────────────────────────────────────────────────────┐
│  Thought  →  Action  →  Observation  →  Thought  →  ... │
│     (raciocínio sobre estado e próximo passo)            │
│     (execução de uma ferramenta)                         │
│     (resultado retornado ao contexto)                    │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
                    Final Answer
```

> **Diagrama de referência:** [`12-Diagrams/ETHAGT01/agent-loop.mmd`](../../12-Diagrams/ETHAGT01/agent-loop.mmd)

Em cada iteração, o modelo:

1. **Thought:** raciocina (em texto) sobre o que sabe até agora e qual o próximo passo sensato. Este *pensamento explícito* é a contribuição central do ReAct — forçar o modelo a externalizar seu raciocínio antes de agir melhora dramaticamente a qualidade das decisões (o efeito *Chain-of-Thought* aplicado à ação).
2. **Action:** escolhe e invoca uma ferramenta (ou declara que tem a resposta final).
3. **Observation:** recebe o resultado da ferramenta, que é inserido de volta no contexto.
4. Repete até emitir uma **Final Answer**.

### 3.2 Por que o ReAct funciona: força-grounding

A genialidade do ReAct está em um mecanismo sutil: o **grounding forçado pela observação**. Sem o loop, o modelo tende a *alucinar em cadeia* — inventa um fato e constrói sobre ele, sem chance de correção. Com o loop, cada passo de raciocínio é seguido de uma **verificação empírica** (a observação da ferramenta): se o modelo inventou, a observação o corrige; se acertou, a observação confirma e avança.

Em outras palavras, o loop converte o raciocínio de um processo *fechado e especulativo* em um processo *aberto e empiricamente corrigível*. Esse é o motivo pelo qual o ReAct supera consistentemente o Chain-of-Thought puro em tarefas que dependem de informação factual externa: o CoT só pode raciocinar sobre o que o modelo já sabe; o ReAct pode *descobrir* o que não sabe.

### 3.3 Implementação mínima em Python puro

Para dominar o mecanismo — e não apenas chamar um framework — vamos implementar o loop ReAct do zero, sem SDK. Esta é a versão didática do Lab 1 ("ReAct em 50 linhas").

```python
import json

# --- Definição de ferramentas -------------------------------------------------
def calcular(expressao: str) -> str:
    """Avalia uma expressão matemática e retorna o resultado."""
    try:
        return str(eval(expressao, {"__builtins__": {}}, {}))
    except Exception as e:
        return f"ERRO: {e}"

TOOLS = {
    "calcular": {
        "description": "Avalia uma expressão matemática. Use para qualquer cálculo.",
        "fn": calcular,
    },
}

# --- Prompt do sistema --------------------------------------------------------
SYSTEM_PROMPT = f"""Você é um agente ReAct. Resolva a tarefa passo a passo.

Sempre responda em EXATAMENTE uma destas duas formas:

Para agir:
Thought: <seu raciocínio>
Action: <nome-da-ferramenta>
Action Input: <entrada para a ferramenta, JSON válido>

Para finalizar:
Thought: <seu raciocínio>
Final Answer: <resposta final>

Ferramentas disponíveis:
{json.dumps({k: v["description"] for k, v in TOOLS.items()}, ensure_ascii=False)}
"""

# --- O agent loop -------------------------------------------------------------
def run_agent(llm, pergunta: str, max_iter: int = 10) -> str:
    mensagens = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": pergunta},
    ]
    for i in range(max_iter):
        resposta = llm(mensagens)              # chamada ao LLM
        mensagens.append({"role": "assistant", "content": resposta})

        if "Final Answer:" in resposta:
            return resposta.split("Final Answer:")[1].strip()

        # parsing simples da ação
        action = _extrair(resposta, "Action:")
        inp = _extrair(resposta, "Action Input:")
        if action in TOOLS:
            obs = TOOLS[action]["fn"](inp)     # executa a ferramenta
        else:
            obs = f"Ferramenta '{action}' não existe. Opções: {list(TOOLS)}"
        mensagens.append({"role": "user", "content": f"Observation: {obs}"})

    return "Limite de iterações atingido sem resposta final."


def _extrair(texto: str, marcador: str) -> str:
    """Extrai o conteúdo após um marcador até o fim da linha."""
    for linha in texto.splitlines():
        if linha.strip().startswith(marcador):
            return linha.split(marcador, 1)[1].strip()
    return ""
```

Observe os elementos essenciais que qualquer agent loop precisa ter:

- **Limite de iterações** (`max_iter`): previne loops infinitos. Sem isso, um agente preso pode consumir todo o seu orçamento.
- **Tratamento de ação inválida:** se o modelo nomeia uma ferramenta inexistente, devolvemos uma observação de erro *útil* (listando as opções), em vez de estourar uma exceção. Isso permite a auto-correção.
- **Condição de parada clara** (`Final Answer`): sem um critério explícito de "terminei", o loop nunca para.
- **Histórico acumulado** em `mensagens`: é a working memory do agente.

### 3.4 Um trace real

Veja como o agente resolve *"Quanto é 23 × 17 + 100?"*:

```
Thought: Preciso multiplicar 23 por 17 e somar 100. Vou calcular tudo de uma vez.
Action: calcular
Action Input: 23 * 17 + 100
Observation: 491
Thought: O resultado é 491. Tenho a resposta.
Final Answer: 23 × 17 + 100 = 491.
```

Cada linha de `Observation` é inserida de volta no contexto, alimentando o próximo `Thought`. O agente decidiu *como* decompor a tarefa e *quando* parar — exatamente a autonomia que distingue um agente de um pipeline fixo.

### 3.5 Limitações e variações

O ReAct é fundacional, não definitivo. Suas limitações conhecidas:

- **Loops:** sem condição de parada robusta, o agente pode entrar em ciclos (mesma ação repetida indefinidamente). Mitigação: limite de iterações + detecção de repetição.
- **Custo e latência:** cada iteração é uma chamada completa ao LLM; tarefas com muitas etapas ficam caras e lentas.
- **Alucinação em ação:** o modelo pode invocar uma ferramenta com argumentos plausíveis mas errados. Mitigação: validação de schema + tratamento de erro que retorna feedback útil.
- **Raciocínio verboso:** o `Thought` explícito consome tokens. Em modelos caros, isso multiplica o custo.

Variações evoluíram a partir do ReAct:

- **ReAct com structured output:** em vez de texto livre (`Thought:`/`Action:`), usa-se tool calling nativo para emitir a ação como JSON estruturado — eliminando o parsing frágil do exemplo acima. É a forma moderna recomendada.
- **Reflexion (Shinn et al., 2023):** adiciona uma fase de *auto-crítica* e *memória de falhas* — o agente reflete sobre por que errou e registra a lição. Aprofundado em ETHAGT04.
- **ReWOO / planejamento antecipado:** em vez de pensar a cada passo, planeja todos os passos no início e executa. Reduz chamadas ao LLM.

> **Princípio orientador.** Implemente ReAct do zero *pelo menos uma vez* para entender o mecanismo. Em produção, considere ReAct com tool calling nativo (não text-parsing) e sempre com limites de iteração, detecção de loop e tratamento de erro.

---

## Capítulo 4 — Workflows vs Agentes

### 4.1 A distinção canônica

A distinção mais importante de ETHAGT01 — e que estrutura todo o resto do curso — é entre **workflows** e **agentes** (Anthropic, 2024):

- **Workflow:** o caminho de execução é **predefinido em código**. O LLM é chamado em pontos específicos de um roteiro fixo, definido pelo desenvolvedor. O desenvolvedor retém controle total sobre *o que acontece quando*.
- **Agente:** o caminho de execução é **decidido pelo LLM em tempo de execução**. O próprio modelo escolhe a próxima ação, observa o resultado e decide novamente, até concluir (ou desistir). O desenvolvedor fornece ferramentas e instruções, mas não o roteiro.

> **Diagrama de referência:** [`12-Diagrams/ETHAGT01/workflow-vs-agent.mmd`](../../12-Diagrams/ETHAGT01/workflow-vs-agent.mmd)

A consequência para projeto é direta e aplica-se a toda decisão de arquitetura:

| Critério | Workflow | Agente |
|---|---|---|
| Previsibilidade | Alta (caminho fixo) | Baixa (caminho emerge) |
| Flexibilidade | Baixa (limitada ao roteiro) | Alta (adapta-se à tarefa) |
| Custo/latência | Controlável (chamadas fixas) | Variável (depende do nº de iterações) |
| Custo de teste | Baixo (caminhos enumeráveis) | Alto (caminhos infinitos) |
| Quando usar | Tarefa bem-understood e repetível | Tarefa aberta, com variabilidade |

### 4.2 Os cinco workflows (panorama)

A Anthropic cataloga cinco *workflows* canônicos que cobrem a maioria das necessidades pré-agente. ETHAGT03 aprofunda cada um; aqui damos o panorama para que você saiba *quanto* pode fazer sem chegar a um agente autônomo.

1. **Prompt Chaining (encadeamento):** divide uma tarefa em uma sequência fixa de chamadas ao LLM, onde a saída de uma alimenta a próxima. Ex.: (1) gerar esboço → (2) gerar rascunho → (3) revisar. *Gate* entre etapas: pode-se validar a saída de uma etapa antes de prosseguir.
2. **Routing (roteamento):** um classificador inicial classifica a entrada e a encaminha para o tratador apropriado. Ex.: suporte ao cliente → encaminha para o especialista em cobrança/técnico/cancelamento. Permite prompts especializados por caso.
3. **Parallelization (paralelização):** executa várias chamadas ao LLM simultaneamente e agrega os resultados. Duas variantes: *sectioning* (particiona a tarefa em sub-tarefas independentes) e *voting* (várias execuções da mesma tarefa, vota-se a melhor resposta).
4. **Orchestrator-Workers (orquestrador-trabalhadores):** um LLM orquestrador decompõe a tarefa dinamicamente e delega subtarefas a LLMs trabalhadores, depois sintetiza. Diferente da paralelização: a decomposição *emerge* do orquestrador, não é fixa.
5. **Evaluator-Optimizer (avaliador-otimizador):** um LLM gera, outro avalia e dá feedback, e o gerador refina — em loop até satisfazer um critério. Útil quando há um critério claro de qualidade.

> **Observação crítica.** O *Orchestrator-Workers* e o *Evaluator-Optimizer* já têm um *sabor* agêntico (decomposição dinâmica, loop). A fronteira workflow/agente é fluida — o ponto é que **mesmo dentro do paradigma workflow, há muita flexibilidade disponível** antes de precisar de um agente totalmente autônomo.

### 4.3 O critério de decisão

A pergunta de projeto não é "agente ou não", mas **"qual é o menor nível de autonomia que resolve a tarefa com previsibilidade suficiente?"**. A regra prática:

> **Princípio da complexidade crescente.** Comece com a solução mais simples que funciona. Só aumente a complexidade — de chamada única → workflow → agente — quando houver *evidência* de que a simplicidade é insuficiente.

A escalada típica:

1. **Uma chamada única** (prompt + LLM) — resolve boa parte das tarefas.
2. **Prompt chaining / routing** — para tarefas com poucos passos conhecidos.
3. **Paralelização / orchestrator-workers** — para variabilidade na decomposição.
4. **Agente autônomo** — para tarefas abertas, com número de passos imprevisível e necessidade de adaptação ao longo do caminho.

Cada degrau adiciona flexibilidade **e** custo/risco/imprevisibilidade. A armadilha mais comum — e mais cara — é começar pelo degrau 4 por "moda", quando o degrau 1 ou 2 resolveria com mais previsibilidade e menos custo. A Anthropic é explícita:

> "*Sometimes, however, complex interactions are needed [...]. Agents can be useful here. However, agents are often less predictable [...] because the LLM is making autonomous decisions.*"

### 4.4 Quando realmente usar um agente

Apesar da cautela, há tarefas para as quais um agente é *claramente* a ferramenta certa. Caracterize-as:

- **Número de passos imprevisível:** não se sabe a priori quantas ações serão necessárias (ex.: depurar um bug — pode levar 2 ou 20 passos).
- **Decisões condicionais sobre o fluxo:** o resultado de uma ação determina o que fazer em seguida, de forma que não pode ser pré-codificada (ex.: pesquisa que refina queries com base no que encontra).
- **Ambiente dinâmico:** o mundo muda durante a execução e o agente precisa reagir.
- **Tarefas abertas:** onde não há um procedimento fixo conhecido.

Mesmo nesses casos, é boa prática **delimitar a autonomia**: dar ao agente um conjunto *finito* de ferramentas, um critério claro de sucesso, um orçamento de iterações e escopo bem definido. Um agente sem cercas não é poderoso — é perigoso.

---

## Capítulo 5 — Implementação: do zero vs framework

### 5.1 Por que implementar do zero

Há uma tentação, ao aprender agentes, de pular direto para um framework (LangGraph, CrewAI, OpenAI Agents SDK...). Resistimos a isso por um motivo pedagógico sólido: **frameworks abstraem exatamente o que você precisa entender.** Se você só usa o framework, quando algo dá errado — e dá — você não saberá se a falha é no seu código, no framework ou na LLM.

A implementação do Capítulo 3 (ReAct em Python puro) torna explícitas três coisas que um framework esconde:

1. **O loop:** você *vê* o `while`, a condição de parada, o acúmulo de contexto. No framework, isso é implícito.
2. **O parsing de ação:** você *vê* como a saída do modelo vira uma chamada de função (e por que é frágil). O framework usa tool calling nativo e oculta isso.
3. **O estado:** você *vê* a lista `mensagens` crescer. O framework gerencia o estado (e, às vezes, o checkpointing) por você.

Depois de entender isso, usar um framework é *produtivo* em vez de *cegante*: você sabe o que ele faz por baixo e quando ele atrapalha.

### 5.2 O mesmo agente em LangGraph

LangGraph modela um agente como um **grafo de estado**: nós (funções) que transformam o estado, arestas (possivelmente condicionais) que decidem o próximo nó. O ReAct torna-se um grafo cíclico: `agent → tools → agent → tools → ... → END`.

```python
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from typing import TypedDict, Annotated
from langchain_core.messages import AnyMessage
import operator

class AgentState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]

def call_model(state: AgentState) -> dict:
    response = model.invoke(state["messages"])   # model com bind_tools
    return {"messages": [response]}

def should_continue(state: AgentState) -> str:
    last = state["messages"][-1]
    return "tools" if last.tool_calls else END

graph = StateGraph(AgentState)
graph.add_node("agent", call_model)
graph.add_node("tools", ToolNode([calcular_ferramenta]))
graph.set_entry_point("agent")
graph.add_conditional_edges("agent", should_continue, {"tools": "tools", END: END})
graph.add_edge("tools", "agent")                  # volta ao agente após tool
app = graph.compile()
```

O que o LangGraph traz de valor real (além de menos código):

- **Checkpointing:** persiste o estado do grafo, permitindo retomar execução, time-travel debugging, intervenção humana (*human-in-the-loop*).
- **Controle de fluxo explícito:** o grafo é um artefato visível e versionável — você *vê* a topologia.
- **Streaming e callbacks:** infraestrutura para observar a execução.

O que ele *esconde* (e que pode morder): o gerenciamento do estado, o roteamento de mensagens, o tratamento de erros de ferramenta. Em produção, você precisa entender esses detalhes para configurar timeouts, retries e limites.

### 5.3 Comparação estrutural de frameworks

A apostila não toma partido de framework: o curso é *architecture-first*. Mas é útil entender como cada um abstrai o mesmo problema, para que a escolha seja consciente. Comparamos três famílias:

| Dimensão | Python puro | LangGraph | OpenAI Agents SDK / CrewAI |
|---|---|---|---|
| Modelo mental | Loop explícito | Grafo de estado cíclico | Agentes + handoffs |
| Controle | Máximo | Alto (grafo visível) | Médio (convenções) |
| Curva de aprendizado | — (você escreve tudo) | Moderada | Baixa (DX alto) |
| Persistência/observabilidade | Por sua conta | Checkpointer nativo | Tracing nativo |
| Melhor para | Aprender o mecanismo | Sistemas complexos com estado | Protótipos rápidos, multi-agente por convenção |

> **Diagrama de referência:** [`12-Diagrams/ETHAGT01/framework-comparison.mmd`](../../12-Diagrams/ETHAGT01/framework-comparison.mmd)

### 5.4 Quando reduzir camadas de abstração

Frameworks aceleram o protótipo, mas adicionam *overhead* e *acoplamento*. Em produção, três sinais sugerem *reduzir* a abstração:

1. **O framework esconde uma falha que você precisa tratar.** Ex.: ele faz retry automático de uma tool, mascarando um bug de design da ferramenta.
2. **Você luta contra as convenções.** Quando metade do seu código é *workaround* para fazer o framework comportar-se como você quer, a abstração virou peso.
3. **Latência/custo críticos.** Cada camada adiciona overhead; em alto volume, código enxuto ganha.

A regra: **use o framework até que deixe de valer a pena; então, reduza, não elimine.** Raramente se volta ao Python puro total — geralmente mantém-se o framework para infraestrutura (tracing, checkpoint) e customiza-se o núcleo do loop.

---

## Capítulo 6 — Observabilidade desde o dia 1

### 6.1 Por que observar desde o início

O erro mais caro do iniciante é *deixar observabilidade para depois*. Agentes são sistemas **não-determinísticos, multi-etapas e caros**: sem observabilidade, um bug é invisível (você não sabe *qual* iteração falhou), um custo explode (você não sabe quantas chamadas estão acontecendo) e uma regressão é impossível de atribuir (você não sabe o que mudou). A observabilidade não é uma fase de "produção" — é uma primitiva de desenvolvimento.

### 6.2 Logging estruturado

O mínimo absoluto é **logging estruturado** de cada evento do loop, com timestamp. Cada evento registra: tipo (`thought`/`action`/`observation`), conteúdo, duração e custo (se disponível).

```python
import json, time, logging

logger = logging.getLogger("agent")
logger.setLevel(logging.INFO)

def log_event(tipo: str, conteudo: dict, custo: float = 0.0):
    registro = {
        "ts": time.time(),
        "tipo": tipo,
        "conteudo": conteudo,
        "custo_usd": custo,
    }
    logger.info(json.dumps(registro, ensure_ascii=False))

# No loop:
#   log_event("thought", {"texto": thought})
#   log_event("action", {"tool": nome, "input": inp})
#   log_event("observation", {"resultado": obs})
```

O formato JSON permite consumir os logs com qualquer ferramenta (`jq`, dashboards, alertas). Evite `print`: texto livre não é consultável.

### 6.3 Traces: a unidade de diagnóstico de agentes

Acima do log, está o conceito de **trace**: o registro completo de *uma execução de agente*, do input inicial à resposta final, incluindo todos os passos intermediários. O trace é a unidade fundamental de diagnóstico de agentes porque um bug só faz sentido no contexto do caminho inteiro que levou a ele.

Um trace típico:

```
[trace 7f3a] pergunta="23*17+100?"
 ├─ thought #1  (0.4s, $0.0003)  "calcular tudo de uma vez"
 ├─ action  #1  tool=calcular input="23*17+100"
 ├─ observation "491"  (0.0s)
 ├─ thought #2  (0.3s, $0.0002)  "tenho a resposta"
 └─ final_answer "491"  (latência total 0.7s, custo $0.0005)
```

ETHAGT12 (AgentOps) aprofunda traces com ferramentas como LangSmith, Phoenix e OpenTelemetry. Por ora, o ponto é: **produza traces desde o primeiro agente**, mesmo que sejam apenas seus logs JSON concatenados.

### 6.4 Custo e latência como métricas de primeira classe

Em sistemas tradicionais, custo e latência são considerações de performance. Em agentes, são **restrições de viabilidade**: um agente que custa US$ 5 por consulta ou leva 90 segundos não é implantável, por mais correto que seja. Trate-os como métricas de primeira classe:

- Meça custo por execução (tokens × preço do modelo + chamadas de ferramenta).
- Meça latência ponta-a-ponta e por etapa.
- Estabeleça orçamentos: "esta tarefa deve custar < US$ 0,50 e < 30 s".
- Alerta quando o orçamento estoura — geralmente indica loop ou degradação.

### 6.5 A escalada de tooling

A progressão saudável de observabilidade:

1. **`print`** — só no primeiro protótipo de 10 minutos.
2. **Logs estruturados (JSON)** — mínimo aceitável para qualquer agente que vá além do notebook.
3. **Framework de tracing** (LangSmith, Phoenix, Arize) — quando você tem múltiplos agentes e precisa correlacionar traces, comparar execuções, ver regressões.
4. **Observabilidade distribuída** (OpenTelemetry + back-end) — em produção multi-serviço (ETHAGT12, ETHAGT14).

> **Regra prática.** Antes de adicionar *qualquer* nova capacidade a um agente (uma ferramenta, um passo de planejamento), garanta que você consegue *ver* o que ele faz. Funcionalidade não-observada é funcionalidade não-confiável.

---

## Capítulo 7 — Casos de estudo

### 7.1 Anthropic Coding Agent no SWE-bench

O caso canônico que ilustra o bloco fundamental em ação é o **coding agent** resolvendo *issues* reais do GitHub, medido pelo benchmark **SWE-bench** (Jimenez et al., *SWE-bench: Can Language Models Resolve Real-World GitHub Issues?*, arXiv:2310.06770). O SWE-bench avalia se um agente consegue, dado um issue de um repositório open-source, produzir um patch que passa nos testes do projeto.

O que o caso ensina sobre a arquitetura:

- **É o bloco fundamental, sem nada exótico.** O coding agent de sucesso é, em essência, um Augmented LLM em loop: percepção (lê o issue e o código), ferramentas (busca no repositório, edição de arquivo, execução de testes), loop (editar → rodar testes → observar falhas → editar novamente). Não há "mágica" — há o bloco fundamental bem aplicado.
- **O poder está nas ferramentas, não no modelo sozinho.** Sem a ferramenta de *executar testes*, o agente não teria o *grounding* para saber se seu patch funciona. A observação do teste é o que fecha o loop corretivo.
- **Iterações valem ouro.** A diferença entre um agente medíocre e um excelente, muitas vezes, está em quantas iterações de "editar-testar-corrigir" ele consegue fazer dentro do orçamento — não em inteligência intrínseca.

> **Leitura.** Detalhes completos em [`09-CaseStudies/`](../../09-CaseStudies/). A lição arquitetural: *comece com o bloco fundamental bem feito; a complexidade (multi-agente, planejamento sofisticado) só entra quando o bloco não basta.*

### 7.2 Lições transversais dos casos reais

Os casos de estudo do curso (suporte em produção, redesign de ACI, etc.) convergem em algumas lições que vale registrar já no primeiro módulo:

1. **Simplicidade vence na maior parte do tempo.** A maioria dos sistemas em produção *não* é um agente totalmente autônomo — é um workflow bem desenhado com pontos de LLM. A autonomia total é a exceção, não a regra.
2. **Ferramentas são o produto.** Em sistemas agentes reais, a maior parte do valor e da complexidade está nas ferramentas (integrações, validações, ACI), não no "cérebro".
3. **Observabilidade é pré-requisito de confiança.** Nenhum dos casos chegou a produção sem traces detalhados. Sem observabilidade, não há como ganhar a confiança das partes interessadas.

---

## Capítulo 8 — Referências e leituras

### 8.1 Bibliografia fundamental

- **Anthropic.** *Building Effective Agents.* 2024. 🏛 Canônica. <https://www.anthropic.com/engineering/building-effective-agents> — Estabelece o Augmented LLM, os 5 workflows e a distinção workflow/agente que estrutura todo este curso.
- **Yao, S. et al.** *ReAct: Synergizing Reasoning and Acting in Language Models.* ICLR 2023. arXiv:2210.03629. 🏛 Canônica — o padrão de loop fundacional.
- **Arunkumar V, Gangadharan G.R., Buyya R.** *Agentic AI: Architectures, Taxonomies, and Evaluation of LLM Agents.* arXiv:2601.12560, 2026. 🏛 Canônica — a taxonomia unificada (Perception · Brain · Planning · Action · Tool Use · Collaboration).

### 8.2 Bibliografia complementar

- **Schick, T. et al.** *Toolformer: Language Models Can Teach Themselves to Use Tools.* NeurIPS 2023. arXiv:2302.04761. — Contexto histórico do tool calling.
- **Shinn, N. et al.** *Reflexion: Language Agents with Verbal Reinforcement Learning.* NeurIPS 2023. arXiv:2303.11366. — Evolução do ReAct com auto-crítica (aprofundada em ETHAGT04).
- **Wang, L. et al.** *A Survey on Large Language Model based Autonomous Agents.* arXiv:2308.11432. — Panorama acadêmico.
- **Jimenez, C. et al.** *SWE-bench.* arXiv:2310.06770. — Benchmark do caso de estudo.

### 8.3 Recursos práticos

- **LangGraph** — repositório e documentação; `examples/react-agent-from-scratch.ipynb` como referência de implementação. <https://github.com/langchain-ai/langgraph>
- **OpenAI.** *Practical Guide to Building Agents.* 2024. — Visão pragmática de provedor.
- **Chase, H.** *LangGraph* (docs canônicos).

### 8.4 Leitura e mídia

- **Anthropic.** *Effective Agents* (YouTube, Erik Schluntz & Alex Albert).
- **Karpathy, A.** *Software 3.0* (talks) — reflexão sobre paradigma.
- **HuggingFace Agents Course** — para comparação crítica de abordagem.

### 8.5 Ficha de pesquisa

Fontes completas e data da última consulta em [`20-Research/ETHAGT01-pesquisa.md`](../../20-Research/ETHAGT01-pesquisa.md). Revalidar a cada 6 meses (a área evolui rápido).

---

## Síntese do módulo

Ao concluir ETHAGT01, você deve ser capaz de:

1. **Decompor** qualquer sistema agêntico nos seis blocos da taxonomia unificada.
2. **Explicar** o Augmented LLM como bloco fundamental e identificar, em qualquer sistema, qual LLM/retrieval/tools/memory/loop.
3. **Implementar** um agente ReAct do zero e entender *o que um framework abstrai*.
4. **Decidir**, com base em trade-offs explícitos, entre workflow e agente para uma tarefa dada.
5. **Aplicar** observabilidade mínima (logs estruturados, traces, orçamentos de custo/latência) desde a primeira linha de código.

Estas são as fundações. Os módulos seguintes aprofundam cada bloco: ETHAGT02 (Tool Use e ACI), ETHAGT03 (os 5 workflows em detalhe), ETHAGT04 (Planning), ETHAGT05 (Memory), e assim por diante. Em todos eles, retornaremos a este capítulo como referência.

---

*Mantido por: Escola de Tecnologia — Universidade Etho · Área de Inteligência Artificial · Versão 1.0 · Julho 2026*
