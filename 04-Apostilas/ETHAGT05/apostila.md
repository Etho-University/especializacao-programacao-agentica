# ETHAGT05 — Memória de Agentes

> **Apostila do curso** · Especialização em Programação Agêntica · Universidade Etho
> Fase B — Razão, Memória e Conhecimento · Carga 25 h · Versão 1.0 · Julho 2026
> *Material de referência duradouro (nível pós-graduação lato sensu). Os slides são auxiliares.*

---

## Sumário

- **Capítulo 1** — Tipos de memória
- **Capítulo 2** — Checkpointer e estado persistente
- **Capítulo 3** — Gerenciamento de contexto
- **Capítulo 4** — Memória vetorial para recall episódico
- **Capítulo 5** — Memória semântica e consolidação
- **Capítulo 6** — Produção: consistência, privacidade, custo
- **Capítulo 7** — Casos de estudo
- **Capítulo 8** — Referências e leituras

---

## Capítulo 1 — Tipos de memória

### 1.1 Por que memória é uma decisão de arquitetura

Um agente sem memória é amnéstico: a cada interação, recomeça do zero, incapaz de lembrar preferências, contexto acumulado ou lições passadas. Isso limita severamente sua utilidade — grande parte do que torna um assistente humano valioso é a memória acumulada sobre o usuário, o domínio e os próprios erros. Em ETHAGT01 registramos que *memória não é um detalhe — é uma decisão de arquitetura desde a primeira linha de código*. Este módulo cumpre essa promessa: como arquitetar memória que dá a agentes persistência, contexto acumulado e aprendizado.

### 1.2 Inspiração cognitiva sem literalismo

A literatura empresta termos da psicologia cognitiva (Tulving, 1972): memória *de trabalho*, *episódica*, *semântica*, *procedural*. Essa analogia é pedagogicamente útil — organiza o espaço de design — mas **não deve ser levada ao literalismo.** Um agente não tem um hipocampo; tem bancos de dados, vetores e prompts. Tratamos os termos cognitivos como *categorias de engenharia*, não como modelos neurológicos.

> **Princípio.** Use a taxonomia cognitiva como *mapa mental* para decidir o que memorizar e como; implemente com as ferramentas de engenharia apropriadas a cada caso.

### 1.3 As quatro camadas

| Tipo | Conteúdo | Implementação típica | Persistência | Latência de acesso |
|---|---|---|---|---|
| **Working memory** | A conversação atual | Janela de contexto (tokens) | Efêmera (sessão) | Nenhuma |
| **Episódica** | Eventos passados com timestamp | Vector store + metadados | Durável | Round-trip |
| **Semântica** | Fatos, conhecimento | KB, knowledge graph, tabelas | Durável | Round-trip |
| **Procedural** | Como fazer (skills, ferramentas) | Código, biblioteca de prompts, reflexões | Durável | Compilação/cache |

> **Diagrama de referência:** [`12-Diagrams/ETHAGT05/memory-layers.mmd`](../../12-Diagrams/ETHAGT05/memory-layers.mmd)

A *working memory* já foi introduzida em ETHAGT01 (§2.4) como a janela de contexto, com seus limites. As outras três camadas são o tema deste módulo: como *externalizar* para armazenamento durável aquilo que não cabe (ou não deve) viver no contexto.

### 1.4 Quando cada tipo é necessário

Nem todo agente precisa das quatro camadas. Um chatbot de FAQ precisa só de working memory (e talvez semântica para a base de conhecimento). Um assistente pessoal de longo prazo precisa das quatro. Um agente de pesquisa pode dispensar memória entre execuções. A regra de projeto: **adicione uma camada de memória quando houver evidência de que o agente precisa dela — não por padrão.** Cada camada adiciona complexidade, custo e vetores de falha (privacidade, inconsistência).

---

## Capítulo 2 — Checkpointer e estado persistente

### 2.1 O problema da interrupção

Considere um agente longo — uma pesquisa que leva horas, com dezenas de passos. Se o processo morre (crash, deploy, timeout), você perde tudo? A resposta é o **checkpointer**: um mecanismo que *persiste o estado do agente* periodicamente, permitindo retomar a execução de onde parou.

### 2.2 Estado serializável

O pré-requisito do checkpointing é que o estado do agente seja **serializável** — convertível para bytes e de volta. Em LangGraph, o estado é um `TypedDict` (ou schema Pydantic), e o checkpointer o serializa a cada "superpasso" do grafo. Implementações canônicas:

- **SQLite/Postgres:** persistência relacional, transacional. Ideal para produção.
- **Redis:** persistência em memória, baixa latência. Bom para estado quente.

> **Diagrama de referência:** [`12-Diagrams/ETHAGT05/checkpointer-resume.mmd`](../../12-Diagrams/ETHAGT05/checkpointer-resume.mmd)

### 2.3 Resume, replay e branching

O checkpointer habilita três capacidades poderosas:

- **Resume:** retomar a execução de um ponto salvo (após interrupção ou intervenção humana).
- **Replay / time travel:** re-executar a partir de um checkpoint anterior — essencial para debug ("o que o agente fez na iteração 5?").
- **Branching:** criar um ramo alternativo a partir de um checkpoint — explorar "e se?".

### 2.4 Implementação (esboço)

```python
from langgraph.checkpoint.postgres import PostgresSaver

checkpointer = PostgresSaver.from_conn_string(DB_URL)
graph = builder.compile(checkpointer=checkpointer)

config = {"configurable": {"thread_id": "sessao-usuario-42"}}
graph.invoke({"messages": [msg]}, config)   # salva estado a cada passo
# ... dias depois, mesmo thread_id retoma o estado ...
graph.invoke({"messages": [nova_msg]}, config)
```

O `thread_id` isola o estado por conversa/usuário — cada um tem sua "linha do tempo" persistente.

### 2.5 Versionamento de schema de estado

O estado evolui: você adiciona campos, muda tipos. Em produção, isso quebra checkpoints antigos. Estratégias: versionar o schema (`state_v1`, `state_v2`), manter migrações, ou usar schemas tolerantes a ausência de campos (valores padrão). Negligenciar isso leva a erros enigmáticos ao retomar estados antigos.

---

## Capítulo 3 — Gerenciamento de contexto

### 3.1 A armadilha da context window

A working memory (janela de contexto) é *finita* e *cara*. O erro clássico do iniciante é acumular histórico, resultados de ferramentas e documentos recuperados até estourar o limite — momento em que o comportamento degrada abruptamente: o modelo "esquece" instruções iniciais, perde coerência. A engenharia de contexto consiste em **gerenciar ativamente o que entra e sai da working memory.**

### 3.2 Custo do contexto: uma visão crítica

Há uma crença comum de que o custo cresce *quadraticamente* com o tamanho do contexto (devido à atenção). Na prática, para a maioria dos provedores, o custo é **linear** por token de entrada, *mas* a latência cresce e a qualidade pode degradar ("lost in the middle": modelos ignoram conteúdo no meio de contextos longos). A lição: **mesmo quando você tem contexto longo disponível, não o preencha sem critério.**

### 3.3 Sumarização em cascata

Quando o histórico cresce demais, **sumarize** as partes mais antigas: um LLM comprime N mensagens antigas em um resumo, que substitui as mensagens originais no contexto. Em conversas longas, isso pode ser feito em cascata (resumos de resumos), mantendo o contexto num tamanho manejável.

> **Padrão:** [`16-Memory/summarization.md`](../../16-Memory/summarization.md).

```python
def gerenciar_contexto(mensagens, max_tokens):
    while contar_tokens(mensagens) > max_tokens:
        antigas = mensagens[:K]
        resumo = llm_summarize(antigas)
        mensagens = [{"role": "system", "content": "Resumo da conversa: " + resumo}] + mensagens[K:]
    return mensagens
```

### 3.4 Eviction por relevância e idade

Nem tudo merece ficar no contexto. Políticas de **eviction** (expurgo) removem conteúdo de baixo valor:

- **Por idade:** remove mensagens mais antigas que N interações.
- **Por relevância:** mantém só as mais relevantes à consulta atual (recall vetorial, Capítulo 4).
- **Combinada:** a fórmula dos *Generative Agents* (Park et al.) combina `recency` (quão recente), `importance` (quão importante) e `relevance` (quão relevante à situação) num score único.

> **Diagrama de referência:** [`12-Diagrams/ETHAGT05/eviction-flow.mmd`](../../12-Diagrams/ETHAGT05/eviction-flow.mmd).

### 3.5 Entity-centric memory (estilo MemGPT/Zep)

Uma abordagem sofisticada é organizar a memória **por entidade**: cada entidade relevante (o usuário, um projeto, um contato) tem um "dossiê" que o agente lê/escreve seletivamente. É o modelo do **MemGPT** (Packer et al., arXiv:2310.08560), que trata o LLM como um sistema operacional gerenciando memória paginada — trazendo para a working memory ("RAM") apenas as páginas relevantes, mantendo o resto em armazenamento ("disco").

> **Padrão:** [`16-Memory/entity-memory.md`](../../16-Memory/entity-memory.md).

---

## Capítulo 4 — Memória vetorial para recall episódico

### 4.1 Recordar eventos passados por similaridade

A memória episódica registra *eventos* — "o que aconteceu e quando". Para que seja útil, o agente precisa *recordar* eventos relevantes à situação atual. A técnica padrão é a **memória vetorial**: cada evento é *embedado* (convertido em vetor) e armazenado num vector store; na hora de recordar, a consulta atual é embedada e os eventos mais *similares* são recuperados.

> **Padrão:** [`16-Memory/vector-recall.md`](../../16-Memory/vector-recall.md).

### 4.2 Pipeline

1. **Gravação:** ao final de um evento relevante, gere um embedding descritivo e armazene com metadados (timestamp, usuário, sessão, tipo).
2. **Recall:** embede a consulta/situação atual, busque os K eventos mais similares.
3. **Filtragem por metadados:** restrinja a um usuário, período ou tipo.
4. **Re-ranking:** opcionalmente, reordene os recuperados por um modelo mais preciso (cross-encoder).

```python
def memorizar(evento, metadados):
    vec = embedder.encode(evento["descricao"])
    vstore.add(id=evento["id"], vector=vec, metadata=metadados, text=evento["descricao"])

def recordar(situacao, user_id, k=5):
    q = embedder.encode(situacao)
    resultados = vstore.search(q, filter={"user_id": user_id}, k=k)
    return [r.text for r in resultados]
```

### 4.3 Quando a memória vetorial é pior que a relacional

A memória vetorial brilha em *recall aproximado por semântica* ("eventos parecidos com isto"). Mas para fatos *estruturados* com consultas exatas ("qual o CPF do usuário?"), uma base **relacional** é superior: mais barata, mais precisa, mais consistente. A regra: **vetorial para similaridade, relacional para fatos estruturados, grafos para relações.** Muitas vezes, os três coexistem.

---

## Capítulo 5 — Memória semântica e consolidação

### 5.1 De episódico a semântico

A distinção episódico/semântico é operacional: *episódico* são eventos ("na terça, o cliente disse X"); *semântico* são fatos consolidados ("o cliente prefere resposta por e-mail"). Há um fluxo natural de **consolidação**: episódios repetidos se consolidam em fatos semânticos — exatamente como, em humanos, memórias episódicas se consolidam em conhecimento durante o sono.

### 5.2 O padrão de consolidação

Periodicamente (ou por gatilho), um processo analisa episódios recentes e *promove* padrões a fatos semânticos:

```python
def consolidar(user_id):
    episodios = recordar_episodios_recentes(user_id, desde="30d")
    fatos = llm(f"Extraia fatos consolidados destes eventos:\n{episodios}")
    for fato in fatos:
        upsert_fato_semantico(user_id, fato)   # sobrescreve se conflitante
```

> **Padrão:** [`16-Memory/consolidation.md`](../../16-Memory/consolidation.md).

### 5.3 Fatos que mudam ao longo do tempo

Um desafio: fatos não são imutáveis. "O usuário mora em São Paulo" pode virar "mora no Rio". A memória semântica precisa lidar com *versões* e *invalidação*:

- **Timestamping:** cada fato tem validade (desde/quando).
- **Invalidação:** um fato novo conflitante invalida o antigo (ou ambos coexistem com data).
- **Decaimento:** fatos não acessados há muito tempo perdem confiança.

A memória estruturada como **knowledge graph** (ETHAGT07) oferece ferramentas naturais para isso: nós com atributos temporais, arestas versionadas.

### 5.4 Memória procedural

A quarta camada — *procedural* — armazena "como fazer": skills, receitas, reflexões aprendidas (a memória de erros do Reflexion, ETHAGT04, é procedural). Implementação: biblioteca de prompts, snippets de código, ou "ferramentas" que o agente descobriu serem úteis. É a memória que mais se aproxima de *código* — e de fato, muitas vezes a melhor "memória procedural" é simplesmente versionar e melhorar as ferramentas/prompts ao longo do tempo.

---

## Capítulo 6 — Produção: consistência, privacidade, custo

### 6.1 Consistência em sistemas multi-agente

Em sistemas multi-agente (Fase C), múltiplos agentes podem ler/escrever a mesma memória *concorrentemente*. Isso introduz problemas clássicos de concorrência: *race conditions*, leituras obsoletas, ordem de eventos. Estratégias:

- **Isolamento por agente/usuário:** cada um tem seu espaço de memória (evita contenção).
- **Eventual consistency + ordenação:** aceitar consistência eventual, mas ordenar eventos por timestamp lógico.
- **Locks/versionamento otimista:** para escritas conflitantes, conflito detectado por versão.

### 6.2 Privacidade e PII

Memória de longo prazo, especialmente sobre usuários, é um campo minado de privacidade:

- **PII:** dados pessoais (CPF, e-mail, saúde) precisam de redação, criptografia, ou armazenamento segregado.
- **Retenção:** defina por quanto tempo a memória persiste; políticas de expurgo automáticas.
- **Direito ao esquecimento:** o usuário deve poder solicitar a exclusão de sua memória (LGPD/GDPR).
- **Acesso:** registre quem acessou quê, quando (log de auditoria).

> **Aprofundamento:** ETHAGT13 (Segurança) trata privacidade e governança em profundidade.

### 6.3 Custo de memória vs benefício

Memória não é grátis: armazenamento, embeddings, round-trips de recall, manutenção de consistência. A pergunta constante: **isto precisa ser memorizado?** Muita memória é guardada "por se acaso" e nunca é recuperada. Meça a *taxa de utilização* da memória — fatos nunca recordados são candidatos a eviction. Em volume alto, a economia de não memorizar o supérfluo é significativa.

### 6.4 Observabilidade de memória

Memória é estado oculto — sem observabilidade, bugs de memória ("o agente esqueceu algo que deveria saber") são intratáveis. Registre: escritas (quem escreveu, o quê, quando), leituras (o quê foi recuperado a cada invocação), e *misses* (quando o recall não trouxe algo relevante). Isso torna a memória depurável.

---

## Capítulo 7 — Casos de estudo

### 7.1 Generative Agents (Smallville)

O paper *Generative Agents: Interactive Simulacra of Human Behavior* (Park et al., UIST 2023; arXiv:2304.03442) é o caso canônico de memória rica: 25 agentes virtuais numa vila, cada um com uma *memory stream* de eventos, com recall pela fórmula `recency · importance · relevance`, consolidação em reflexões, e planejamento baseado em memória. O caso mostra que memória bem arquitetada sustenta comportamento *coerente de longo prazo* — agentes que lembram, planejam e agem de forma consistente ao longo de "dias".

> **Leitura.** Detalhes em [`09-CaseStudies/`](../../09-CaseStudies/). A lição de arquitetura: a *estrutura* da memória (stream + scoring + consolidação) é mais importante que o volume.

### 7.2 MemGPT / Letta e a memória paginada

O **MemGPT** (Packer et al., arXiv:2310.08560; hoje projeto *Letta*) trata o LLM como sistema operacional, gerenciando uma hierarquia de memória (main context ↔ external storage) com "page faults" que trazem dados relevantes sob demanda. A inspiração em sistemas operacionais é produtiva: ajuda a raciocinar sobre *o que está residente* vs *o que está arquivado*.

### 7.3 Lições transversais

1. **Memória é camadas, não uma coisa.** Diferentes necessidades pedem diferentes implementações.
2. **Evite memorizar por padrão.** Cada camada tem custo; adicione só com evidência.
3. **Memória sem observabilidade é impossível de depurar.**

---

## Capítulo 8 — Referências e leituras

### 8.1 Bibliografia fundamental

- **Packer, C. et al.** *MemGPT: Towards LLMs as Operating Systems.* arXiv:2310.08560, 2023. 🏛
- **Park, J.S. et al.** *Generative Agents: Interactive Simulacra of Human Behavior.* UIST 2023. arXiv:2304.03442. 🏛
- **Shinn, N. et al.** *Reflexion.* NeurIPS 2023. arXiv:2303.11366. 🏛 (memória de falhas)

### 8.2 Bibliografia complementar

- **LangGraph docs** — *Persistence* e *Memory*.
- **Zep** — *Long-term memory for assistant apps*.
- **A-MEM** — *Agentic Memory for Long-Term Recall* (2024).
- **Tulving, E.** *Episodic and Semantic Memory.* 1972 — fundação cognitiva.

### 8.3 Recursos práticos

- **LangGraph** `checkpoint-postgres`, `checkpoint-sqlite`, `checkpoint-redis`.
- **Vector stores:** Qdrant, Chroma, pgvector.
- **Biblioteca de padrões de memória:** [`16-Memory/`](../../16-Memory/) (6 padrões).

### 8.4 Ficha de pesquisa

Fontes em [`20-Research/ETHAGT05-pesquisa.md`](../../20-Research/ETHAGT05-pesquisa.md). Última consulta: Julho 2026.

---

## Síntese do módulo

Ao concluir ETHAGT05, você deve ser capaz de:

1. **Distinguir** os quatro tipos de memória e decidir quais um agente precisa.
2. **Implementar** persistência via checkpointer (resume, replay, branching).
3. **Gerenciar** a context window (sumarização, eviction, entity-centric memory).
4. **Construir** memória vetorial para recall episódico e consolidar episódios em fatos semânticos.
5. **Lidar** com consistência, privacidade e custo de memória em produção.

Próximos passos: ETHAGT07 aprofunda knowledge graphs como memória estruturada; ETHAGT09/14 tratam consistência em multi-agente e distribuído; ETHAGT15 conecta memória com meta-agentes autoaprendentes.

---

*Mantido por: Escola de Tecnologia — Universidade Etho · Área de Inteligência Artificial · Versão 1.0 · Julho 2026*
