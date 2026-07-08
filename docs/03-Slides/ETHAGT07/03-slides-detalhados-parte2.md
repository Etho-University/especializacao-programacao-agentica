# ETHAGT07 — Slides Detalhados + Notas do Professor (Parte 2: Slides 37-80)

> Universidade Etho · Especialização em Programação Agêntica
> Cada slide contém: título, objetivo, conteúdo, notas do professor, diagrama, animação, imagem, tempo.

---

## SEÇÃO E — GraphRAG (Slides 37-51 · 15 min)

---

### Slide 37 — [SEÇÃO] GraphRAG

**Título**: 4 — GraphRAG
**Objetivo**: Transição para o bloco de GraphRAG.
**Conteúdo**: Número "4" grande + "GraphRAG"
**Diagrama**: Fundo `etho-primary`
**Animação**: Morph (400ms)
**Imagem**: Número "4" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Início do bloco GraphRAG. Esta é a técnica da Microsoft (Edge et al., 2024) que combina knowledge graph com sumarização hierárquica de comunidades. Resolve o problema que vector RAG não consegue: perguntas GLOBAIS sobre o corpus inteiro. Vamos ver o pipeline, os dois modos (local vs global), a DEMO, e os custos.
➡️ TRANSIÇÃO: "Primeiro: por que GraphRAG? Qual lacuna ele preenche?"

---

### Slide 38 — Por Que GraphRAG?

**Título**: Por Que GraphRAG?
**Objetivo**: Explicar a lacuna que GraphRAG preenche.
**Conteúdo**:
- Vector RAG: recupera chunks isolados — perde visão global
- Problema: "Quais são os temas principais deste corpus de 1000 docs?"
- Vector RAG: não consegue responder (precisa de todos os chunks)
- GraphRAG: constrói grafo de entidades + comunidades → síntese global
- Multi-hop: vector RAG falha em perguntas que exigem encadear 3+ hops

**Diagrama**: D21 — Vector RAG (chunks isolados) vs GraphRAG (grafo + comunidades)
**Animação**: Lado esquerdo (vector) aparece, depois direito (GraphRAG)
**Imagem**: Comparação visual
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vector RAG recupera chunks isolados. Isso é ótimo para "o que a página 42 diz sobre X?". Mas falha para perguntas GLOBAIS: "quais os temas principais do corpus?", "quais as tendências de pesquisa nesta área?", "resuma as posições de todos os autores sobre Y". Para responder, você precisaria ler TODOS os chunks — o que vector RAG não faz. GraphRAG resolve isso: constrói um grafo de entidades, detecta COMUNIDADES (clusters temáticos), e sumariza cada comunidade hierarquicamente. Agora você pode responder perguntas globais consultando os sumários, não os chunks brutos.
💡 ANALOGIA: Vector RAG é como buscar uma página no índice remissivo (local, preciso). GraphRAG é como ler o sumário de capítulos + índice analítico (global, sintético). Você precisa dos dois dependendo da pergunta.
⚠️ ERROS COMUNS: Alunos acham que GraphRAG substitui vector RAG. Não — eles são complementares. Vector RAG para lookup factual, GraphRAG para síntese global. O pipeline híbrido usa os dois.
➡️ TRANSIÇÃO: "Vamos ver a arquitetura completa do Microsoft GraphRAG."

---

### Slide 39 — Microsoft GraphRAG: Visão Geral

**Título**: Microsoft GraphRAG: Visão Geral
**Objetivo**: Apresentar a arquitetura do GraphRAG da Microsoft.
**Conteúdo**:
- Pipeline de construção:
  1. Text chunking
  2. Extração de entidades + relações (LLM)
  3. Construção do grafo
  4. Detecção de comunidades (Leiden algorithm)
  5. Sumarização hierárquica de comunidades (LLM)
- Pipeline de query:
  - Local search: entidades relevantes + vizinhança
  - Global search: map-reduce sobre sumários de comunidades
- Fonte: Edge et al., arXiv:2404.16130

**Diagrama**: D22 — `12-Diagrams/ETHAGT07/graphrag-pipeline.mmd`
**Animação**: Pipeline aparece etapa por etapa
**Imagem**: Diagrama de pipeline
**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O pipeline GraphRAG tem duas fases. CONSTRUÇÃO (offline): chunking do corpus → extração de entidades e relações via LLM (NER + relação) → construção do knowledge graph → detecção de comunidades com o algoritmo Leiden → sumarização hierárquica de cada comunidade (LLM gera um sumário para cada comunidade, depois agrega subcomunidades em comunidades maiores). QUERY (online): Local search (perguntas específicas — navega o subgrafo ao redor das entidades mencionadas) ou Global search (perguntas amplas — map-reduce sobre os sumários de comunidades).
💡 ANALOGIA: A construção é como escrever uma enciclopédia: você lê todos os documentos, organiza por tema (comunidades), escreve um verbete para cada tema (sumários). A query é como consultar a enciclopédia: vai direto ao verbete (global) ou ao índice remissivo dentro do verbete (local).
⚠️ ERROS COMUNS: Alunos acham que GraphRAG é "build once, query forever". O grafo envelhece: novos documentos, entidades novas, comunidades que mudam. A manutenção (Slide 49) é recorrente e cara.
➡️ TRANSIÇÃO: "Vamos aprofundar a etapa mais mágica: detecção de comunidades."

---

### Slide 40 — Construção do Grafo de Comunidades

**Título**: Construção do Grafo de Comunidades
**Objetivo**: Aprofundar a etapa de community detection.
**Conteúdo**:
- Grafo de entidades → algoritmo Leiden → comunidades
- Comunidade: grupo de entidades densamente conectadas entre si
- Hierarquia: comunidades grandes contêm subcomunidades
- Análogo a "capítulos de um livro" — estrutura temática emergente
- Resultado: grafo particionado em níveis hierárquicos

**Diagrama**: D23 — Grafo colorido por comunidade (ex: 5 cores)
**Animação**: Cores se espalham pelo grafo
**Imagem**: Grafo particionado em cores
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O algoritmo Leiden detecta comunidades: grupos de entidades densamente conectadas entre si e escassamente conectadas com o resto. É como clusterização, mas em grafos. A mágica: essa estrutura emerge dos dados — você não define os temas, eles emergem das conexões. E é hierárquica: comunidades grandes contêm subcomunidades (como capítulos contêm seções). O resultado é uma árvore temática do corpus, onde cada nível é um zoom diferente.
💡 ANALOGIA: É como a Amazon categorizando produtos automaticamente. Você não diz "eletrônicos é uma categoria" — os produtos que são comprados juntos formam clusters naturais. Leiden faz isso com entidades: as que co-aparecem muito formam uma comunidade temática.
⚠️ ERROS COMUNS: Alunos esperam comunidades "perfeitamente temáticas". Leiden é heurístico — comunidades podem ter ruído. O sumário hierárquico (próximo slide) suaviza isso, mas não é perfeito. Valide com amostragem.
➡️ TRANSIÇÃO: "Comunidades viram sumários. Como?"

---

### Slide 41 — Sumarização Hierárquica

**Título**: Sumarização Hierárquica
**Objetivo**: Explicar como comunidades viram sumários.
**Conteúdo**:
- Para cada comunidade (no nível mais baixo): LLM gera sumário
- Sumários de subcomunidades → LLM gera sumário da comunidade pai
- Resultado: árvore de sumários do específico ao geral
- Vantagem: responde perguntas globais sem ler todos os chunks
- Custo: uma chamada de LLM por comunidade (caro na construção)

**Diagrama**: D24 — Árvore de sumários (folhas → raiz)
**Animação**: Folhas aparecem, depois sobem para a raiz
**Imagem**: Árvore hierárquica
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Para cada comunidade no nível mais baixo (folhas), o LLM gera um sumário descrevendo o que aquela comunidade representa (quais entidades, quais relações, qual tema). Depois, para cada comunidade pai, o LLM agrega os sumários das subcomunidades em um sumário mais geral. O resultado é uma ÁRVORE de sumários: da folha (específico) à raiz (global). Para responder "quais os temas principais do corpus?", você consulta o sumário da raiz ou do nível mais alto — sem ler os chunks.
💡 ANALOGIA: É como um relatório executivo hierárquico. O analista junior escreve sumário de cada projeto (folhas). O gerente agrega em sumário de área (intermediário). O diretor agrega em sumário da empresa (raiz). O CEO lê só a raiz para a visão global.
⚠️ ERROS COMUNS: Alunos subestimam o custo. Cada comunidade = 1 chamada de LLM. Para 1000 comunidades, são 1000 chamadas só na sumarização (mais as de extração). Voltamos a isso no Slide 48.
➡️ TRANSIÇÃO: "Como consultamos isso? Dois modos: local e global."

---

### Slide 42 — Local Search

**Título**: Local Search
**Objetivo**: Apresentar o modo Local do GraphRAG.
**Conteúdo**:
- Input: pergunta do usuário
- Passo 1: identificar entidades relevantes na pergunta (LLM)
- Passo 2: expandir vizinhança no grafo (entidades + relações + chunks associados)
- Passo 3: LLM gera resposta com o contexto local
- Melhor para: perguntas específicas sobre entidades conhecidas
- Exemplo: "Quem são os co-autores de X?"

**Diagrama**: D25 — Grafo com subgrafo local destacado
**Animação**: Subgrafo é destacado no grafo maior
**Imagem**: Grafo com vizinhança em destaque
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Local search é para perguntas específicas sobre entidades conhecidas. A pergunta "Quem são os co-autores de X?" menciona a entidade "X". O pipeline: (1) identificar "X" como entidade relevante; (2) expandir a VIZINHANÇA no grafo — quem X está conectado, quais relações, quais chunks mencionam X; (3) LLM gera a resposta com esse contexto local. É como um "zoom in" no grafo ao redor das entidades da pergunta.
💡 ANALOGIA: Local search é como perguntar a um especialista sobre um tópico específico. Ele vai direto à seção relevante da biblioteca dele, pega os livros sobre o tema, e responde. Não precisa ler a biblioteca toda.
⚠️ ERROS COMUNS: Alunos usam local search para perguntas globais e ficam frustrados com respostas parciais. Local é para entidades específicas. Para temas amplos, use global (próximo slide).
➡️ TRANSIÇÃO: "Global search é o oposto: perguntas amplas."

---

### Slide 43 — Global Search

**Título**: Global Search
**Objetivo**: Apresentar o modo Global do GraphRAG.
**Conteúdo**:
- Input: pergunta ampla ("Quais temas principais do corpus?")
- Map: para cada comunidade (nível escolhido), LLM gera resposta parcial
- Reduce: LLM agrega respostas parciais em resposta final
- Melhor para: perguntas que exigem visão holística
- Exemplo: "Quais as tendências de pesquisa nesta área?"

**Diagrama**: D26 — Map-reduce sobre comunidades
**Animação**: Map aparece, depois reduce
**Imagem**: Fluxo map-reduce
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Global search é para perguntas amplas que exigem visão holística. "Quais os temas principais do corpus?" não é sobre uma entidade — é sobre TODAS. O pipeline é map-reduce: MAP — para cada comunidade (no nível escolhido), o LLM gera uma resposta parcial baseada no sumário daquela comunidade. REDUCE — um LLM agrega todas as respostas parciais em uma resposta final sintética. É mais lento que local (múltiplas chamadas LLM), mas responde o que vector RAG não consegue.
💡 ANALOGIA: Global search é como um censo. Você não pergunta a uma pessoa (local) — você pergunta a cada região (map), depois agrega os resultados em um relatório nacional (reduce). Mais caro, mas é a única forma de ter a visão do todo.
⚠️ ERROS COMUNS: Alunos usam global search para tudo. Global é caro (map-reduce = N chamadas LLM). Use para perguntas genuinamente globais; para específicas, local é mais rápido e barato.
➡️ TRANSIÇÃO: "Como escolher entre os dois? Vamos sistematizar."

---

### Slide 44 — Local vs Global: Quando Cada

**Título**: Local vs Global: Quando Cada
**Objetivo**: Dar critério prático de escolha.
**Conteúdo**:
- Local: pergunta menciona entidades específicas → foco no subgrafo
- Global: pergunta é temática/ampla → síntese entre comunidades
- Híbrido: começa local, escala para global se insuficiente
- Heurística: "Esta pergunta precisa de 1 entidade ou de todo o corpus?"

**Diagrama**: D27 — Tabela comparativa Local vs Global
**Animação**: Linhas da tabela aparecem
**Imagem**: Tabela de comparação
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Critério simples: a pergunta menciona entidades específicas? → Local. A pergunta é temática/ampla? → Global. Na dúvida, comece local (mais barato) e escale para global se a resposta for insuficiente. A heurística: "esta pergunta precisa de 1 entidade ou de todo o corpus?"
💡 ANALOGIA: Local é como perguntar "o que o João faz?" (vá direto ao João). Global é como perguntar "quais as profissões mais comuns na cidade?" (precisa de todo mundo). A natureza da pergunta define o modo.
➡️ TRANSIÇÃO: "Mas quando GraphRAG supera vector RAG de forma clara?"

---

### Slide 45 — GraphRAG vs Vector RAG

**Título**: GraphRAG vs Vector RAG
**Objetivo**: Sistematizar quando GraphRAG supera vector RAG.
**Conteúdo**:
- Vector RAG melhor: lookup factual, pergunta de um hop, latência baixa
- GraphRAG melhor: multi-hop, raciocínio sobre relacionamentos, visão global
- Custo: GraphRAG é 10-100x mais caro na construção
- Latência: Global search é mais lento (map-reduce)
- Regra: GraphRAG quando o valor do raciocínio justifica o custo

**Diagrama**: D28 — Tabela: Vector RAG vs GraphRAG (critérios, custo, latência, recall)
**Animação**: Linhas aparecem
**Imagem**: Tabela comparativa
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vector RAG ganha em lookup factual (pergunta de 1 hop, latência baixa). GraphRAG ganha em multi-hop, raciocínio sobre relacionamentos e visão global. Mas GraphRAG é 10-100x mais caro na construção (extração + comunidades + sumários) e a global search é mais lenta na query (map-reduce). Regra de ouro: use GraphRAG quando o VALOR do raciocínio multi-hop/global justifica o CUSTO. Para blog pessoal, vector RAG basta. Para farmacêutica (interações medicamentosas), GraphRAG vale.
💡 ANALOGIA: Vector RAG é um sedã (eficiente, barato, resolve 90% dos trajetos). GraphRAG é um helicóptero (caro de comprar e manter, mas vê o que o sedã não vê). Você não compra helicóptero para ir ao mercado — mas para resgate em área remota, é insubstituível.
⚠️ ERROS COMUNS: Alunos implementam GraphRAG "por ser moderno" sem ter perguntas que exigem multi-hop/global. O custo de construção não se paga. Comece com vector RAG; adicione GraphRAG quando a evidência (perguntas falhando) justificar.
➡️ TRANSIÇÃO: "Chegou a hora: DEMO ao vivo."

---

### Slide 46 — DEMO: GraphRAG em Neo4j

**Título**: DEMO: GraphRAG em Neo4j
**Objetivo**: Demo ao vivo — construir KG e responder pergunta multi-hop.
**Conteúdo**:
- Referência: `05-Labs/ETHAGT07/Lab2-GraphRAG-Neo4j`
- Passo 1: carregar corpus técnico
- Passo 2: extrair entidades/relações com LLM
- Passo 3: construir grafo no Neo4j
- Passo 4: query Cypher multi-hop
- Mostrar: vector RAG falha na mesma pergunta, GraphRAG acerta

**Diagrama**: Terminal + Neo4j Browser lado a lado
**Animação**: Passos aparecem sequencialmente
**Imagem**: Screenshot do Neo4j Browser
**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esta é a DEMO clímax. Vou mostrar o Lab 2: construir um KG em Neo4j a partir de um corpus técnico, e responder uma pergunta multi-hop. O momento-chave: fazer a MESMA pergunta com vector RAG (falha ou responde parcial) e com GraphRAG/grafo (acerta, com path explicável). A diferença é visível e dramática. Se a API falhar, tenho screenshots pré-gravados do Neo4j Browser.
💡 ANALOGIA: A demo é o "antes e depois". Antes: vector RAG traz chunks sobre o tema mas não encadeia. Depois: o grafo mostra o caminho A→B→C explicitamente. É a diferença entre "tenho informações soltas" e "entendo a cadeia".
⚠️ ERROS COMUNS: A demo pode demorar (extração de entidades é lenta). Use corpus pequeno pré-carregado e mostre só a query final. O objetivo não é ver a construção ao vivo, é ver a query multi-hop funcionando.
➡️ TRANSIÇÃO: "Vamos discutir o que vimos."

---

### Slide 47 — Pergunta da DEMO

**Título**: Pergunta da DEMO
**Objetivo**: Engajar a turma com uma pergunta sobre a demo.
**Conteúdo**:
- "O GraphRAG errou alguma coisa na demo? Onde?"
- "Qual o custo aproximado da construção do grafo (em tokens)?"
- "Se o corpus mudar (novos docs), quanto custa reindexar?"
- Discussão em duplas (2 min)

**Diagrama**: Caixa de discussão (`etho-warning`)
**Animação**: Perguntas aparecem
**Imagem**: Ícone de discussão
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vamos refletir em duplas. Três perguntas: (1) O GraphRAG errou algo? Onde? — costuma errar em relações alucinadas ou em entidades ambíguas; (2) Qual o custo aproximado da construção em tokens? — para o corpus da demo, estimar; (3) Se o corpus mudar, quanto custa reindexar? — introduz o problema da manutenção. Deixar 2 min em duplas, depois compartilhar.
❓ PERGUNTA PARA A TURMA: "Em duplas: onde o GraphRAG pode ter errado na demo?" (2 min)
⚠️ ERROS COMUNS: Alunos saem da demo achando que GraphRAG é "perfeito". Não é — alucinações em extração, comunidades ruidosas, sumários que perdem nuance. GraphRAG é poderoso mas falível. Auditoria e lineage são essenciais.
➡️ TRANSIÇÃO: "O custo é real. Vamos quantificar."

---

### Slide 48 — Custos de Construção

**Título**: Custos de Construção
**Objetivo**: Ser transparente sobre o custo de construir GraphRAG.
**Conteúdo**:
- Extração de entidades: 1 chamada LLM por chunk
- Extração de relações: 1 chamada LLM por par de entidades
- Sumarização de comunidades: 1 chamada LLM por comunidade
- Ordem de magnitude: 1000 docs → ~5k-15k chamadas LLM
- Custo estimado: $50-$500 dependendo do modelo
- Pergunta: *Por que GraphRAG é caro? Justifique o custo.*

**Diagrama**: D29 — Breakdown de custo por etapa (bar chart)
**Animação**: Barras crescem
**Imagem**: Gráfico de custo
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vamos quantificar o custo. Para 1000 documentos: extração de entidades = 1000 chamadas (1 por chunk). Extração de relações = depende do número de pares — tipicamente 2000-5000 chamadas. Sumarização de comunidades = 500-3000 chamadas (depende do número de comunidades). Total: 5k-15k chamadas LLM. Com GPT-4o: ~$50-$500. Com modelo menor: mais barato, mas qualidade da extração cai. Esse é o CUSTO DE CONSTRUÇÃO — upfront, não recorrente (até a manutenção).
💡 ANALOGIA: É como construir uma biblioteca física. Você paga pela fundação, prateleiras, catalogação — upfront. Depois, a manutenção (limpeza, novos livros) é menor mas contínua. GraphRAG tem o mesmo perfil: construção cara, manutenção recorrente.
❓ PERGUNTA PARA A TURMA: "Por que GraphRAG é caro? Justifique o custo." (Resposta: cada etapa envolve chamadas LLM — extração, relações, sumários. O valor é o raciocínio multi-hop/global que vector RAG não dá)
➡️ TRANSIÇÃO: "E a manutenção? Também custa."

---

### Slide 49 — Custos de Manutenção

**Título**: Custos de Manutenção
**Objetivo**: Mostrar que GraphRAG tem custo recorrente, não só inicial.
**Conteúdo**:
- Novos documentos: extrair entidades/relações + atualizar comunidades
- Atualização incremental: mais barato que reconstrução total, mas complexo
- Drift de entidades: mesma entidade com nomes diferentes → merge
- Comunidades podem mudar: re-sumarização necessária
- Lineage: rastrear qual documento originou qual tripla

**Diagrama**: D30 — Ciclo de manutenção
**Animação**: Ciclo gira
**Imagem**: Ciclo circular
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: GraphRAG não é "build once". Novos documentos chegam → extração → atualização do grafo → comunidades podem mudar (uma entidade nova pode conectar comunidades antes separadas) → re-sumarização necessária. Atualização incremental é mais barata que reconstrução total, mas é complexa (precisa reconciliar entidades). Drift de entidades: "Dipirona" e "Dipirona sódica" são a mesma? Você precisa de entity resolution. Lineage (doc_id em cada tripla) é essencial para auditar e corrigir.
💡 ANALOGIA: É como manter um jardim. Você não planta uma vez e esquece — precisa regar, podar, remover ervas daninhas. GraphRAG precisa de manutenção contínua: novos docs, merge de entidades, re-sumarização. Sem manutenção, o grafo degrada.
⚠️ ERROS COMUNS: Alunos subestimam a manutenção. "Construí o GraphRAG, pronto!" Não — em 3 meses com novos documentos, o grafo está desatualizado. Planeje custo de manutenção desde o início (pipeline incremental + entity resolution).
➡️ TRANSIÇÃO: "Então, vale a pena? Depende do domínio."

---

### Slide 50 — Pergunta: Vale a Pena?

**Título**: Vale a Pena?
**Objetivo**: Estimular pensamento crítico sobre ROI.
**Conteúdo**:
- "Para qual domínio GraphRAG vale o custo de construção?"
- "E para qual domínio é overkill?"
- Critério: valor do raciocínio multi-hop vs custo de manutenção
- Exemplos: farmacêutica (vale), jurídico (vale), blog pessoal (não vale)

**Diagrama**: D31 — Matriz 2x2 (valor do raciocínio vs custo)
**Animação**: Quadrantes aparecem com exemplos
**Imagem**: Matriz 2x2
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A pergunta do ROI. GraphRAG vale quando o valor do raciocínio multi-hop/global é ALTO e o custo de manutenção é SUSTENTÁVEL. Farmacêutica: interações medicamentosas são literalmente uma questão de vida — vale. Jurídico: precedências e referências cruzadas são o core — vale. Jurídico: precedências e referências cruzadas são o core — vale. Blog pessoal: nenhuma pergunta exige multi-hop — não vale. A matriz 2x2 ajuda a decidir: eixo X = custo de manutenção, eixo Y = valor do raciocínio. Quadrante "alto valor + custo sustentável" = invista em GraphRAG.
💡 ANALOGIA: É como decidir entre comprar ou alugar. GraphRAG é "comprar" (investimento alto, custo de manutenção, mas retorna valor a longo prazo). Vector RAG é "alugar" (baixo investimento, flexível, mas limitado). A decisão depende do horizonte e do valor.
❓ PERGUNTA PARA A TURMA: "Para o domínio de vocês: vale ou é overkill?" (deixar 2-3 respostas)
⚠️ ERROS COMUNS: Alunos aplicam GraphRAG a tudo. "Mais complexo = melhor" é armadilha. GraphRAG é over-engineering quando vector RAG já resolve 95% das perguntas.
➡️ TRANSIÇÃO: "Vamos recapitular as 3 abordagens antes de combiná-las."

---

### Slide 51 — Recap: Vector vs Graph vs GraphRAG

**Título**: Recap: Vector vs Graph vs GraphRAG
**Objetivo**: Sintetizar as 3 abordagens antes de avançar para híbridos.
**Conteúdo**:
- Vector DB: similaridade semântica, barato, rápido
- Knowledge Graph: relacionamentos estruturados, modelagem cara, raciocínio multi-hop
- GraphRAG: KG + sumarização de comunidades, caro na construção, responde perguntas globais
- Próximo: combinar vector + grafo em pipeline híbrido

**Diagrama**: D32 — 3 colunas comparativas
**Animação**: Colunas aparecem uma a uma
**Imagem**: 3 cards comparativos
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Recapitulando. Vector DB: similaridade semântica, barato, rápido, mas sem raciocínio estrutural. Knowledge Graph: relacionamentos estruturados, permite multi-hop, mas modelagem é cara e manutenção contínua. GraphRAG: knowledge graph + comunidades sumarizadas, responde perguntas globais, mas caríssimo na construção. A próxima seção une os mundos: pipeline híbrido.
💡 ANALOGIA: Vector é o atleta de velocidade (rápido, direto). Knowledge graph é o estrategista (vê conexões, planeja rotas). GraphRAG é o general (visão do campo de batalha inteiro). O exército maduro usa os três.
➡️ TRANSIÇÃO: "Pipelines híbridos: o futuro maduro."

---

## SEÇÃO F — Pipelines Híbridos (Slides 52-62 · 12 min)

---

### Slide 52 — [SEÇÃO] Pipelines Híbridos

**Título**: 5 — Pipelines Híbridos
**Objetivo**: Transição para a combinação de vector + grafo.
**Conteúdo**: Número "5" grande + "Pipelines Híbridos"
**Diagrama**: Fundo `etho-primary`
**Animação**: Morph (400ms)
**Imagem**: Número "5" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Início do bloco de pipelines híbridos. Até agora vimos vector e grafo separados. Agora vamos COMBINÁ-LOS: um agente que escolhe a estratégia de retrieval certa para cada pergunta. É o coração do projeto do módulo.
➡️ TRANSIÇÃO: "Por que combinar?"

---

### Slide 53 — Vector + Grafo: Por Que Combinar?

**Título**: Vector + Grafo: Por Que Combinar?
**Objetivo**: Justificar a combinação.
**Conteúdo**:
- Vector: bom em "encontrar documentos sobre X"
- Grafo: bom em "encontrar entidades relacionadas a X"
- Híbrido: "encontrar documentos sobre entidades relacionadas a X"
- Exemplo: "Artigos sobre medicamentos que interagem com o que o paciente X toma"
- Vector sozinho: não sabe interações. Grafo sozinho: não tem texto dos artigos.

**Diagrama**: D33 — Venn diagram (vector ∩ graph = híbrido)
**Animação**: Círculos se sobrepõem
**Imagem**: Venn diagram
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vector e grafo têm forças complementares. Vector recupera documentos por semântica. Grafo raciocina sobre relacionamentos. A pergunta "artigos sobre medicamentos que interagem com o que o paciente X toma" precisa dos DOIS: o grafo sabe quais medicamentos interagem (multi-hop), e o vector busca artigos sobre esses medicamentos (semântica). Vector sozinho não sabe interações. Grafo sozinho não tem o texto dos artigos. O híbrido une as forças.
💡 ANALOGIA: Vector é como um bibliotecário (encontra livros por tema). Grafo é como um detetive (conecta suspeitos). A pergunta "livros sobre os suspeitos conectados ao caso X" precisa dos dois: o detetive identifica os suspeitos, o bibliotecário encontra os livros.
⚠️ ERROS COMUNS: Alunos acham que híbrido é "vector OU grafo". Não — é vector E grafo, combinados. A fusão é onde a mágica acontece.
➡️ TRANSIÇÃO: "Qual é a arquitetura híbrida canônica?"

---

### Slide 54 — Arquitetura Híbrida

**Título**: Arquitetura Híbrida
**Objetivo**: Apresentar a arquitetura canônica de retrieval híbrido.
**Conteúdo**:
- Componentes:
  1. Ingestão: texto → embeddings (vector DB) + entidades/relações (grafo)
  2. Query: pergunta → vector search + graph traversal
  3. Fusão: combinar resultados (RAG com contexto do grafo)
  4. Geração: LLM com chunks + subgrafo como contexto
- Sync: vector DB e grafo devem referenciar os mesmos documentos

**Diagrama**: D34 — `12-Diagrams/ETHAGT07/hybrid-retrieval.mmd`
**Animação**: Componentes aparecem em sequência
**Imagem**: Diagrama de arquitetura
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A arquitetura híbrida canônica. INGESTÃO: cada documento vira embedding (vector DB) E entidades/relações (grafo). Ambos referenciam o mesmo doc_id. QUERY: a pergunta vai para vector search (recupera chunks relevantes) e/ou graph traversal (encontra entidades relacionadas). FUSÃO: combina os resultados — chunks do vector + subgrafo do grafo, ambos como contexto para o LLM. GERAÇÃO: LLM gera resposta com chunks + subgrafo, permitindo citar tanto o texto quanto as relações.
💡 ANALOGIA: É como um jornalista que consulta o arquivo (vector) e a rede de contatos (grafo). O arquivo dá os documentos; a rede de contatos dá as conexões. A matéria final usa os dois, com fontes citadas.
⚠️ ERROS COMUNS: Alunos esquecem o SYNC entre vector e grafo. Se o vector DB tem um documento que o grafo não (extração falhou), a fusão fica inconsistente. doc_id compartilhado + reconciliation job são essenciais.
➡️ TRANSIÇÃO: "Mas nem toda pergunta precisa de híbrido. O agente deve escolher."

---

### Slide 55 — RetrievalAgent: Escolhendo Estratégia

**Título**: RetrievalAgent: Escolhendo Estratégia
**Objetivo**: Mostrar que o agente decide qual estratégia de retrieval usar.
**Conteúdo**:
- Nem toda pergunta precisa de grafo
- RetrievalAgent classifica a pergunta:
  - "O que é X?" → vector search (simples)
  - "Quem está conectado a X?" → graph traversal
  - "Documentos sobre entidades relacionadas a X?" → híbrido
- Implementação: LLM como router (classifica intenção da pergunta)
- Alternativa: sempre híbrido e deixar o LLM filtrar (mais caro, mais simples)

**Diagrama**: D35 — Router: pergunta → {vector | graph | híbrido} → resultado
**Animação**: Ramos do router aparecem
**Imagem**: Fluxograma de roteamento
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Nem toda pergunta precisa de híbrido. "O que é GraphRAG?" é uma pergunta factual — vector search resolve. "Quem são os co-autores de X?" é relacional — graph traversal resolve. "Documentos sobre medicamentos que interagem com X?" é híbrida. Um RetrievalAgent inteligente CLASSIFICA a pergunta e escolhe a estratégia. Implementação: um LLM como router ("esta pergunta é vector, graph, ou híbrida?"). Alternativa: sempre híbrido (mais caro, mas mais simples de implementar). O trade-off é latência/custo vs complexidade de código.
💡 ANALOGIA: É como um médico que tria o paciente. Dor de cabeça? → clínico geral (vector). Suspeita de interação medicamentosa? → especialista (grafo). Caso complexo? → equipe multidisciplinar (híbrido). Nem todo paciente precisa da equipe inteira.
⚠️ ERROS COMUNS: Alunos implementam "sempre híbrido" e ficam surpresos com a latência. O router adiciona 1 chamada LLM mas economiza retrieval desnecessário. Comece com router.
➡️ TRANSIÇÃO: "Vamos ver o código do router."

---

### Slide 56 — Implementação do Router

**Título**: Implementação do Router
**Objetivo**: Mostrar código real do router.
**Conteúdo**:
- Snippet:
  ```python
  def retrieve(question: str) -> list[Document]:
      strategy = classify_strategy(question)
      if strategy == "vector":
          return vector_search(question)
      elif strategy == "graph":
          return graph_traverse(question)
      else:  # híbrido
          entities = extract_entities(question)
          related = graph.find_related(entities)
          return vector_search(question, filter=related)
  ```
- `classify_strategy`: LLM com prompt simples ("vector/graph/hybrid?")
- Trade-off: router adiciona 1 chamada LLM, mas economiza retrieval desnecessário

**Diagrama**: Code block com syntax highlighting
**Animação**: Código aparece linha a linha
**Imagem**: Código em `etho-dark`
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A função `retrieve` é o coração do RetrievalAgent. Primeiro, `classify_strategy` usa um LLM com prompt simples para classificar a pergunta em vector/graph/hybrid. Depois, despacha para a estratégia certa. No caso híbrido: extrai entidades da pergunta, encontra entidades relacionadas no grafo, e faz vector search FILTRANDO pelos documentos que mencionam essas entidades. O router adiciona 1 chamada LLM (classificação), mas economiza retrieval desnecessário (não faz graph traversal para "o que é X?").
💡 ANALOGIA: É como um gerente de suporte que encaminha o ticket. Ele lê o título (1 chamada LLM = classificação) e decide: FAQ (vector), especialista (grafo), ou equipe (híbrido). Sem o gerente, todo ticket iria para a equipe inteira — desperdício.
⚠️ ERROS COMUNS: Alunos pulam o router e fazem híbrido sempre. Funciona, mas a latência e o custo sobem. O router é uma otimização que se paga rapidamente.
➡️ TRANSIÇÃO: "E como manter isso atualizado? Manutenção incremental."

---

### Slide 57 — Manutenção: Incremental Update

**Título**: Manutenção: Incremental Update
**Objetivo**: Mostrar como manter o pipeline híbrido atualizado.
**Conteúdo**:
- Novo documento chega → 2 pipelines disparam:
  1. Embedding → insert no vector DB
  2. Extração de entidades/relações → insert/update no grafo
- Sync: ambos devem referenciar o mesmo doc_id
- Desafio: se extração falha, grafo fica incompleto (vector tem, grafo não)
- Solução: retry queue + reconciliation job

**Diagrama**: D36 — Pipeline de ingestão dual (vector + graph)
**Animação**: Pipeline flui
**Imagem**: Fluxo de ingestão dupla
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Quando um novo documento chega, dois pipelines disparam em paralelo: (1) embedding → insert no vector DB; (2) extração de entidades/relações → insert/update no grafo. Ambos referenciam o mesmo doc_id. O desafio: se a extração falha (LLM indisponível, rate limit), o vector DB tem o documento mas o grafo não — inconsistência. Solução: retry queue (re-tenta extração) + reconciliation job (periodicamente, verifica se todos os docs no vector têm triplas no grafo).
💡 ANALOGIA: É como um casal dividindo tarefas. Um lava a louça (vector), o outro seca (grafo). Se um falha, a louça fica molhada na prateleira — inconsistência. O reconciliation job é a checagem periódica: "tem louça molhada na prateleira?"
⚠️ ERROS COMUNS: Alunos não implementam reconciliation. A inconsistência cresce silenciosamente até alguém notar que "o agente não sabe sobre o documento X" (porque o grafo não tem as entidades). Reconciliation desde o dia 1.
➡️ TRANSIÇÃO: "E como rastrear de onde veio cada resposta? Lineage."

---

### Slide 58 — Lineage e Provenance

**Título**: Lineage e Provenance
**Objetivo**: Explicar rastreabilidade no pipeline híbrido.
**Conteúdo**:
- Lineage: qual documento originou qual tripla do grafo
- Provenance: qual tripla originou qual parte da resposta
- Implementação: `doc_id` como propriedade em nós e arestas
- Valor: debugging ("por que o agente disse isso?"), auditoria, correção
- Sem lineage: grafo é caixa preta — impossível explicar respostas

**Diagrama**: D37 — Resposta → tripla → documento (chain of provenance)
**Animação**: Cadeia aparece
**Imagem**: Cadeia de proveniência
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Lineage é a rastreabilidade do dado. Cada tripla no grafo deve ter `doc_id` como propriedade — qual documento originou aquela relação. Quando o agente responde "Dipirona interage com Warfarin", a provenance rastreia: resposta ← tripla "interage_com" ← documento #42 (bula da Dipirona). Isso permite: debugging ("por que o agente disse isso?" → rastreia até o doc), auditoria (a fonte é confiável?), e correção (se o doc #42 estava errado, invalida a tripla).
💡 ANALOGIA: Lineage é como a citação em um paper acadêmico. Sem citação, a afirmação é "dizem que..." (caixa preta). Com citação, você pode verificar a fonte. Em agentes, lineage é a citação que torna a resposta auditável.
⚠️ ERROS COMUNS: Alunos não implementam lineage e depois não conseguem explicar respostas erradas. "O agente disse X, mas não sei de onde tirou isso." Sem lineage, o grafo é caixa preta. doc_id em cada nó e aresta, SEMPRE.
➡️ TRANSIÇÃO: "Vamos ao caso de estudo do projeto."

---

### Slide 59 — Caso: Base de Conhecimento Técnica

**Título**: Caso: Base de Conhecimento Técnica
**Objetivo**: Apresentar o caso de estudo do projeto do módulo.
**Conteúdo**:
- Corpus: documentação técnica + issues + changelogs
- Vector DB: busca por "como fazer X"
- Grafo: "X depende de Y", "X substituiu Z", "X foi introduzido na v2.3"
- Híbrido: "documentação sobre features que dependem de X"
- Agente: escolhe estratégia e justifica a escolha

**Diagrama**: D38 — Caso (corpus → pipeline híbrido → agente)
**Animação**: Pipeline aparece
**Imagem**: Arquitetura do caso
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Este é o caso do projeto do módulo. Corpus técnico: documentação, issues do GitHub, changelogs. Vector DB busca por "como fazer X" (lookup semântico). Grafo codifica "X depende de Y", "X substituiu Z", "X foi introduzido na v2.3" (relações estruturais). O híbrido responde "documentação sobre features que dependem de X" — precisa do grafo para saber dependências E do vector para achar os docs. O agente escolhe a estratégia e JUSTIFICA ("usei grafo porque a pergunta é sobre dependências").
💡 ANALOGIA: É como um desenvolvedor sênior consultando a wiki (vector) e o código-fonte (grafo de dependências). A pergunta "quais features quebram se eu mudar X?" precisa dos dois: o grafo de dependências e a documentação de cada feature.
➡️ TRANSIÇÃO: "Vamos praticar a decisão."

---

### Slide 60 — Exercício: Vector, Graph, ou Híbrido?

**Título**: Vector, Graph, ou Híbrido?
**Objetivo**: Praticar a decisão em cenários reais.
**Conteúdo**:
- 5 cenários:
  1. Catálogo de produtos com busca por similaridade → Vector
  2. Base de conhecimento médica com relações entre doenças e tratamentos → Graph (ou híbrido)
  3. Documentos jurídicos com referências cruzadas → Híbrido
  4. Chatbot de RH com perguntas sobre políticas → Vector (ou híbrido)
  5. Sistema de recomendação de filmes → Híbrido (ou graph)
- Em grupos: vector, graph, ou híbrido? Justificar.

**Diagrama**: 5 cards com cenários
**Animação**: Cards aparecem
**Imagem**: Cards numerados
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Exercício em grupos. Para cada cenário, decidir vector/graph/híbrido e justificar. Não há resposta única — depende dos detalhes. O objetivo é praticar o CRITÉRIO: a pergunta é sobre similaridade (vector), relacionamentos (graph), ou ambos (híbrido)? Deixar 2 min em grupos, depois compartilhar.
❓ PERGUNTA PARA A TURMA: "Em grupos: para cada cenário, vector, graph, ou híbrido? Por quê?" (2 min)
⚠️ ERROS COMUNS: Alunos respondem "híbrido para tudo". Nem sempre — catálogo de produtos com busca por similaridade é vector puro. Híbrido adiciona complexidade; só use quando há evidência de gap.
➡️ TRANSIÇÃO: "Justamente: sempre híbrido?"

---

### Slide 61 — Pergunta: Sempre Híbrido?

**Título**: Sempre Híbrido?
**Objetivo**: Combater o reflexo de "mais complexo = melhor".
**Conteúdo**:
- Verdadeiro/falso: "Sempre preferir híbrido."
- Resposta: Falso — híbrido adiciona complexidade e custo
- Híbrido só quando: vector sozinho falha E o valor justifica o custo
- Anti-pattern: "vamos fazer híbrido por precaução" → over-engineering
- Regra: comece com vector, adicione grafo com evidência de gap

**Diagrama**: D39 — Escada de complexidade (vector → graph → híbrido → GraphRAG)
**Animação**: Degraus aparecem
**Imagem**: Escada
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Verdadeiro ou falso: "Sempre preferir híbrido." FALSO. Híbrido adiciona complexidade (2 sistemas para sincronizar, router, reconciliation) e custo. Híbrido é justificado QUANDO vector sozinho falha em perguntas importantes E o valor dessas perguntas justifica o custo. Anti-pattern clássico: "vamos fazer híbrido por precaução" — over-engineering. Regra: comece com vector, meça o gap (perguntas que falham), adicione grafo com EVIDÊNCIA.
💡 ANALOGIA: É como comprar um canivete suíço quando você só precisa de uma faca. O canivete faz tudo, mas é mais caro, mais pesado, e cada ferramenta é menos boa que a dedicada. Híbrido é o canivete — use quando realmente precisa de múltiplas ferramentas.
⚠️ ERROS COMUNS: Alunos implementam híbrido desde o dia 1 "para estarem prontos". Resultado: 2x a complexidade, 2x os bugs, sem evidência de que precisavam. Comece simples (vector), adicione complexidade (grafo/híbrido) quando a evidência pedir.
➡️ TRANSIÇÃO: "Mas quando híbrido vale, os números falam."

---

### Slide 62 — Benchmark: Vector vs Grafo vs Híbrido

**Título**: Benchmark: Vector vs Grafo vs Híbrido
**Objetivo**: Mostrar resultados reais de comparação.
**Conteúdo**:
- Dataset: corpus técnico com perguntas multi-hop
- Métricas: success rate, latência p50/p99, custo por query
- Resultado típico:
  - Vector: 60% success, 200ms, $0.01/query
  - Graph: 75% success, 400ms, $0.02/query
  - Híbrido: 85% success, 500ms, $0.03/query
- Híbrido melhora success rate em casos multi-hop sem explodir custo
- Critério de sucesso do projeto

**Diagrama**: D40 — Gráfico de barras (success rate) + tabela (latência/custo)
**Animação**: Barras crescem
**Imagem**: Gráfico + tabela
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Resultados típicos de benchmark. Vector sozinho: 60% de success rate — falha em perguntas multi-hop. Graph sozinho: 75% — melhor em multi-hop, mas falha em lookup semântico. Híbrido: 85% — o melhor dos dois mundos. O custo: híbrido é 3x mais caro por query que vector, mas o success rate salta 25 pontos. Esse é o critério de sucesso do projeto do módulo: híbrido melhora success rate em casos multi-hop sem explodir custo.
💡 ANALOGIA: É como comparar modos de transporte. Vector é a bicicleta (barata, rápida no curto, mas não sobe morro). Graph é o jipe (sobe morro, mas mais lento no plano). Híbrido é o carro com tração 4x4 (faz os dois, custo intermediário). Para a maioria das perguntas, o carro é a melhor escolha — mas só se você tem morros para subir (multi-hop).
⚠️ ERROS COMUNS: Alunos olham só success rate e ignoram latência/custo. 85% success a $0.03 pode ser pior que 75% a $0.02 dependendo do orçamento. Otimize para a métrica que importa para o negócio.
➡️ TRANSIÇÃO: "Por último: operar isso em escala."

---

## SEÇÃO G — Operação em Escala (Slides 63-68 · 8 min)

---

### Slide 63 — [SEÇÃO] Operação em Escala

**Título**: 6 — Operação em Escala
**Objetivo**: Transição para tópicos de produção.
**Conteúdo**: Número "6" grande + "Operação em Escala"
**Diagrama**: Fundo `etho-primary`
**Animação**: Morph (400ms)
**Imagem**: Número "6" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Último bloco técnico: operação em escala. Construir um pipeline híbrido é uma coisa; operá-lo em produção com milhões de vetores e milhares de queries por segundo é outra. Vamos cobrir sharding, consistência, reindexação, quantização e observabilidade.
➡️ TRANSIÇÃO: "Sharding e replicação."

---

### Slide 64 — Sharding e Replicação

**Título**: Sharding e Replicação
**Objetivo**: Explicar como vector DBs escalam horizontalmente.
**Conteúdo**:
- Sharding: dividir vetores em partições (por hash ou range)
- Replicação: cópias para disponibilidade e leitura paralela
- Qdrant: sharding por collection, replicação configurável
- Milvus: arquitetura distribuída nativa (QueryNode, DataNode, Proxy)
- Trade-off: mais shards = mais paralelismo, mas mais coordenação

**Diagrama**: D41 — Cluster com shards e réplicas
**Animação**: Shards aparecem, depois réplicas
**Imagem**: Cluster distribuído
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Sharding divide os vetores em partições (por hash do id, por exemplo). Cada shard vive em um nó diferente — isso permite paralelismo (cada nó processa um pedaço da query). Replicação faz cópias de cada shard — para disponibilidade (se um nó cai, a réplica assume) e para leitura paralela (múltiplas réplicas atendem queries). Qdrant faz sharding por collection com replicação configurável. Milvus é distribuído nativo (componentes separados: QueryNode, DataNode, Proxy). O trade-off: mais shards = mais paralelismo, mas mais coordenação (a query precisa ser fan-out e agregada).
💡 ANALOGIA: Sharding é como dividir uma biblioteca entre filiais (cada filial tem parte do acervo). Replicação é ter cópias do best-seller em cada filial (para disponibilidade e leitura paralela). Mais filiais = mais capacidade, mas mais logística de coordenação.
⚠️ ERROS COMUNS: Alunos adicionam shards demais "para escalar" e ficam surpresos com a latência de coordenação. Comece com poucos shards, adicione quando a evidência (latência, throughput) pedir.
➡️ TRANSIÇÃO: "E consistência? Strong vs eventual."

---

### Slide 65 — Consistência

**Título**: Consistência
**Objetivo**: Discutir modelos de consistência em vector DBs.
**Conteúdo**:
- Strong: toda leitura vê o último write (mais caro)
- Eventual: leituras podem ver dados stale (mais rápido)
- Bounded staleness: stale por no máximo T segundos
- Qdrant: configurável por collection
- Para RAG: eventual costuma bastar (embeddings não mudam a cada segundo)

**Diagrama**: Espectro strong ←→ eventual
**Animação**: Espectro aparece
**Imagem**: Gradiente de consistência
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Modelos de consistência. Strong: toda leitura vê o último write — mais caro (precisa de quorum síncrono). Eventual: leituras podem ver dados stale (atualizações propagam eventualmente) — mais rápido. Bounded staleness: stale por no máximo T segundos. Para RAG, eventual costuma bastar: embeddings não mudam a cada segundo, e uma query ver um documento 2 segundos depois do insert é aceitável. Qdrant permite configurar consistência por collection.
💡 ANALOGIA: Strong é como um banco (você vê o saldo exato agora). Eventual é como um extrato do cartão (pode estar alguns minutos defasado). Para RAG, "extrato" é suficiente — você não precisa de consistência bancária para recomendar documentos.
⚠️ ERROS COMUNS: Alunos exigem strong consistency "por segurança" e pagam em latência. Para RAG, eventual é suficiente na maioria dos casos. Reserve strong para casos críticos (ex: imediatamente após um insert, o usuário precisa ver o documento).
➡️ TRANSIÇÃO: "E quando você troca de modelo de embedding? Reindexação."

---

### Slide 66 — Reindexação e Drift de Embeddings

**Título**: Reindexação e Drift de Embeddings
**Objetivo**: Explicar o problema de trocar modelo de embedding.
**Conteúdo**:
- Modelo de embedding novo → vetores antigos são incompatíveis
- Reindexação total: re-embeddar todos os documentos (caro, demorado)
- Estratégias:
  - Dual index: manter novo e velho durante transição
  - Zero-downtime reindex: construir novo index em background, swap quando pronto
- Drift: se documentos mudam, embeddings antigos perdem relevância
- Frequência de reindex: depende da volatilidade do corpus

**Diagrama**: D42 — Timeline de reindexação (dual index → swap)
**Animação**: Timeline avança
**Imagem**: Timeline T0-T3
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Se você troca de modelo de embedding (ex: OpenAI text-embedding-3-small → text-embedding-3-large), os vetores antigos são INCOMPATÍVEIS com o novo modelo — você não pode misturar. Precisa re-embeddar todos os documentos e reconstruir o index. Isso é caro (tempo + custo de API) e demorado. Estratégia de zero-downtime: (1) manter o index velho servindo; (2) construir o index novo em background; (3) quando o novo está pronto, fazer swap atômico; (4) desligar o velho. Outro problema: drift. Se seus documentos mudam (wiki atualizada, issues resolvidas), embeddings antigos perdem relevância. A frequência de reindex depende da volatilidade do corpus.
💡 ANALOGIA: É como trocar a linguagem de catalogação de uma biblioteca. Você não pode ter metade dos livros em Dewey e metade em LOC — precisa recatalogar tudo. Zero-downtime é manter as duas catalogações durante a transição e trocar de uma vez.
⚠️ ERROS COMUNS: Alunos trocam de modelo sem reindexar e não entendem por que o recall despenca. Os vetores antigos e novos estão em "espaços" diferentes — cosine similarity entre eles é lixo. SEMPRE reindex ao trocar modelo.
➡️ TRANSIÇÃO: "E custo de armazenamento? Quantização."

---

### Slide 67 — Custo de Armazenamento (Quantização)

**Título**: Custo de Armazenamento (Quantização)
**Objetivo**: Mostrar como reduzir custo de memória.
**Conteúdo**:
- Vetor de 1536 dims em float32 = 6 KB por vetor
- 100M vetores = 600 GB (só vetores, sem index)
- Quantização:
  - float32 → float16: 50% redução, perda mínima
  - Product Quantization (PQ): 90%+ redução, perda moderada
  - Binary quantization: 97% redução, perda maior
- Qdrant: suporta quantização com re-scoring (busca rápida + re-rank preciso)

**Diagrama**: D43 — Tabela de trade-off (precisão vs tamanho)
**Animação**: Linhas da tabela aparecem
**Imagem**: Tabela de quantização
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Um vetor de 1536 dimensões em float32 ocupa 6 KB. 100 milhões de vetores = 600 GB SÓ de vetores (sem o index HNSW, que é ainda maior). Para reduzir, usamos quantização. float16 (metade da precisão): 50% de redução, perda de recall mínima. Product Quantization (PQ): comprime cada vetor em um código — 90%+ de redução, perda moderada. Binary quantization: cada dimensão vira 1 bit — 97% de redução, perda maior. Qdrant suporta quantização com RE-SCORING: busca no index quantizado (rápido) e re-ranqueia os top-k candidatos com os vetores originais (preciso). Melhor dos dois mundos.
💡 ANALOGIA: Quantização é como comprimir uma foto em JPEG. float32 é o RAW (perfeito, enorme). float16 é PNG (ótimo, metade do tamanho). PQ é JPEG alta qualidade (bom, 10x menor). Binary é JPEG baixa (reconhecível, mas com artefatos). Re-scoring é como tirar a foto em JPEG para busca rápida, depois abrir o RAW dos top candidatos para detalhe.
⚠️ ERROS COMUNS: Alunos ativam quantização agressiva sem re-scoring e ficam surpresos com recall baixo. Sempre teste recall COM seus filtros reais antes de confiar na quantização. Re-scoring custa pouco e preserva qualidade.
➡️ TRANSIÇÃO: "Por último: observabilidade."

---

### Slide 68 — Observabilidade

**Título**: Observabilidade
**Objetivo**: Definir métricas mínimas para operar vector DBs em produção.
**Conteúdo**:
- Latência de query: p50, p95, p99
- Recall@k: verdadeiros vizinhos vs retornados (amostragem)
- Cache hit rate: queries repetidas (economiza ANN)
- Index size vs collection size
- Throughput: queries por segundo
- Alertas: p99 > threshold, recall < threshold, index desatualizado

**Diagrama**: D44 — Dashboard com métricas
**Animação**: Métricas aparecem no dashboard
**Imagem**: Dashboard mockup
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Para operar vector DB em produção, métricas mínimas. LATÊNCIA: p50 (mediana), p95, p99 (cauda). RECALL@k: amostralmente, compare os top-k do index com brute force — se recall cai, algo está errado (index degradado, quantização agressiva demais). CACHE HIT RATE: queries repetidas — se alto, cache economiza ANN. INDEX SIZE vs COLLECTION SIZE: se o index é muito maior que a coleção, algo está errado. THROUGHPUT: queries por segundo. ALERTAS: p99 acima de threshold, recall abaixo de threshold, index desatualizado (não sincronizado com a coleção).
💡 ANALOGIA: É como o painel de um carro. Você não dirige só olhando a velocidade (latência) — também ó combustível (index size), a temperatura (recall), e o conta-quilômetros (throughput). Sem o painel, você só descobre o problema quando o carro para.
⚠️ ERROS COMUNS: Alunos monitoram só latência ("está rápido"). Latência boa com recall ruim = respostas rápidas mas ERRADAS. Monitore recall desde o dia 1 — é a métrica de QUALIDADE, não só de performance.
➡️ TRANSIÇÃO: "Fechamento. Boas práticas, anti-patterns, caso, quiz."

---

## SEÇÃO H — Fechamento (Slides 69-80 · 10 min)

---

### Slide 69 — [SEÇÃO] Boas Práticas e Anti-Patterns

**Título**: 7 — Boas Práticas e Anti-Patterns
**Objetivo**: Transição para o fechamento.
**Conteúdo**: "7 — Boas Práticas e Anti-Patterns"
**Diagrama**: Fundo `etho-primary`
**Animação**: Morph (400ms)
**Imagem**: Número "7" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Última seção. Vamos consolidar tudo em boas práticas (DO), anti-patterns (DON'T), um caso de estudo, resumo, quiz e Q&A.
➡️ TRANSIÇÃO: "Primeiro: o que FAZER."

---

### Slide 70 — Boas Práticas (DO)

**Título**: Boas Práticas (DO)
**Objetivo**: Checklist de boas práticas.
**Conteúdo**:
- Comece com vector DB, adicione grafo com evidência de gap
- Normalize embeddings se usar cosine (vira dot, mais rápido)
- Defina schema de entidades/relações antes de extrair
- Valide triplas extraídas por LLM (confiança + amostragem)
- Mantenha lineage: doc_id em cada nó e aresta
- Monitore recall@k em produção (não só latência)
- Reindexação planejada quando trocar modelo de embedding
- Híbrido só quando success rate do vector é insuficiente

**Diagrama**: Checklist verde (`etho-success`)
**Animação**: Itens aparecem com checkmark
**Imagem**: Checklist verde
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Checklist das boas práticas. Comece simples (vector), adicione complexidade (grafo/híbrido) com EVIDÊNCIA de gap. Normalize embeddings se usar cosine (vira dot, mais rápido). Defina schema de entidades/relações ANTES de extrair (evita ruído). Valide triplas extraídas por LLM (alucinação é real). Mantenha lineage (doc_id em cada nó e aresta) para auditoria. Monitore recall@k, não só latência. Planeje reindexação ao trocar modelo. Híbrido só quando o success rate do vector é insuficiente.
💡 ANALOGIA: É como um código de boas práticas de engenharia. Você não constrói um prédio sem fundação (comece com vector). Você não pinta sem projeto (defina schema). Você audita a obra (valide triplas, mantenha lineage). E você só adiciona andares quando a base aguenta (híbrido com evidência).
➡️ TRANSIÇÃO: "E o que NÃO fazer."

---

### Slide 71 — Anti-Patterns (DON'T)

**Título**: Anti-Patterns (DON'T)
**Objetivo**: Checklist do que NÃO fazer.
**Conteúdo**:
- Começar com GraphRAG quando vector RAG basta
- Misturar métricas entre index e query
- Modelar grafo com "RELATED_TO" genérico em tudo
- Confiar cegamente em triplas extraídas por LLM (alucinação)
- Sem lineage — impossível debugar respostas erradas
- Não monitorar recall (latência boa ≠ qualidade boa)
- Reindexar em horário de pico sem dual index
- Adicionar vector DB quando Postgres já resolve
- Híbrido "por precaução" sem evidência de gap

**Diagrama**: Checklist vermelho (`etho-danger`)
**Animação**: Itens aparecem com X
**Imagem**: Checklist vermelho
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Checklist dos anti-patterns. Começar com GraphRAG quando vector RAG basta (overkill). Misturar métricas entre index e query (recall destruído). Modelar grafo com "RELATED_TO" genérico (queries fracas). Confiar cegamente em triplas extraídas por LLM (alucinação vira fato). Sem lineage (caixa preta, impossível debugar). Não monitorar recall (latência boa com qualidade ruim). Reindexar em pico sem dual index (downtime). Adicionar vector DB quando Postgres resolve (complexidade desnecessária). Híbrido "por precaução" (over-engineering).
💡 ANALOGIA: Cada anti-pattern é um pecado capital da infraestrutura cognitiva. Overkill (GraphRAG desnecessário) é orgulho. Caixa preta (sem lineage) é preguiça. Over-engineering (híbrido sem evidência) é ganância por complexidade. Reconheça o pecado, evite a armadilha.
➡️ TRANSIÇÃO: "Vamos ver tudo junto em um caso real."

---

### Slide 72 — Caso de Estudo: GraphRAG em Farmacêutica

**Título**: Caso: GraphRAG em Farmacêutica
**Objetivo**: Mostrar todos os conceitos em um caso real.
**Conteúdo**:
- Domínio: interações medicamentosas em base farmacêutica
- Corpus: 50k documentos (bulas, papers, guidelines)
- Vector DB: busca por "documentos sobre efeito colateral X"
- Grafo: medicamento → interage_com → medicamento → contraindicado_para → condição
- GraphRAG: comunidades de medicamentos relacionados → visão de classes terapêuticas
- Resultado: multi-hop "paciente com condição X + medicação Y → risco?"
- Custo: ~$200 de construção, justificado por valor clínico

**Diagrama**: D45 — Arquitetura do caso (corpus → vector + graph → GraphRAG → resposta)
**Animação**: Pipeline aparece
**Imagem**: Arquitetura do caso
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Caso real que une tudo. Farmacêutica: 50k documentos (bulas, papers, guidelines). Vector DB busca "documentos sobre efeito colateral X" (semântico). Grafo codifica "medicação → interage_com → medicação → contraindicado_para → condição" (estrutural). GraphRAG detecta comunidades de medicamentos relacionados (classes terapêuticas emergentes). A pergunta-chave: "paciente com condição X + tomando medicação Y → qual o risco?" — multi-hop que vector RAG não responde. Custo: ~$200 de construção, justificado porque uma interação medicamentosa não detectada pode custar uma vida.
💡 ANALOGIA: É o "exército completo" da analogia do Slide 51. Vector é o médico de plantão (encontra a bula certa). Grafo é o farmacêutico (sabe as interações). GraphRAG é o comitê de especialistas (vê as classes terapêuticas inteiras). Para segurança do paciente, você precisa dos três.
⚠️ ERROS COMUNS: Alunos saem do caso achando que TODO domínio precisa de GraphRAG. Farmacêutica é o caso onde o valor do raciocínio multi-hop é LITERALMENTE de vida ou morte. Para blog de receitas, vector RAG basta. Contexto define a escolha.
➡️ TRANSIÇÃO: "Vamos resumir tudo."

---

### Slide 73 — Resumo da Aula

**Título**: Resumo da Aula
**Objetivo**: Sintetizar os pontos-chave.
**Conteúdo**:
- Vector DB: similaridade semântica via ANN (HNSW/IVF), métricas, filtering
- 5 vector DBs com trade-offs distintos (Qdrant, Milvus, Weaviate, Chroma, pgvector)
- Knowledge Graph: triplas, propriedades, raciocínio multi-hop via Cypher
- GraphRAG: comunidades + sumarização hierárquica → local vs global
- Híbrido: vector + grafo, RetrievalAgent escolhe estratégia
- Escala: sharding, reindexação, quantização, observabilidade
- Regra: comece simples (vector), adicione complexidade com evidência

**Diagrama**: 7 ícones com os pontos-chave
**Animação**: Ícones aparecem em grid
**Imagem**: Grid de 7 ícones
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Resumo dos 7 pontos-chave. (1) Vector DB: ANN (HNSW/IVF), métricas (cosine/dot/euclidean), filtering (pre/post). (2) 5 vector DBs com trade-offs: Qdrant (filtering), Milvus (escala), Weaviate (modules), Chroma (simples), pgvector (operacional). (3) Knowledge Graph: triplas, propriedades, Cypher, raciocínio multi-hop. (4) GraphRAG: comunidades + sumarização hierárquica, local vs global. (5) Híbrido: vector + grafo, RetrievalAgent como router. (6) Escala: sharding, reindexação, quantização, observabilidade. (7) Regra de ouro: comece simples, adicione complexidade com EVIDÊNCIA.
💡 ANALOGIA: O resumo é a "mochila" que vocês levam. 7 ferramentas: vector, grafo, GraphRAG, híbrido, escala, observabilidade, e o critério de decisão. Usem com critério, não com entusiasmo cego.
➡️ TRANSIÇÃO: "Checklist da aula — confirmar que cobrimos tudo."

---

### Slide 74 — Checklist da Aula

**Título**: Checklist da Aula
**Objetivo**: Confirmar que todos os tópicos foram cobertos.
**Conteúdo**:
- [ ] Explicou ANN (HNSW, IVF) e métricas
- [ ] Comparou 5 vector DBs por cenário
- [ ] Modelou knowledge graph com triplas e Cypher
- [ ] Apresentou GraphRAG (local + global)
- [ ] Construiu pipeline híbrido com router
- [ ] Discutiu escala, reindexação e observabilidade

**Diagrama**: Checklist visual
**Animação**: Checkmarks aparecem
**Imagem**: Checklist verde
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Checklist para confirmar que cobrimos tudo. Se algum item não ficou claro, é hora de perguntar. O Q&A (Slide 80) é o espaço para isso.
➡️ TRANSIÇÃO: "Quiz — vamos verificar a compreensão."

---

### Slide 75 — Quiz: Pergunta 1

**Título**: Quiz — Pergunta 1
**Objetivo**: Verificar compreensão.
**Conteúdo**:
- "Qual métrica de similaridade é equivalente a dot product quando os embeddings estão normalizados?"
- A) Euclidean
- B) Cosine
- C) Manhattan
- D) Jaccard
- Resposta: B

**Diagrama**: 4 opções em cards
**Animação**: Opções aparecem
**Imagem**: Cards de múltipla escolha
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A resposta é B) Cosine. Quando os embeddings são normalizados (norma = 1), cosine e dot product dão o mesmo ranking. Por isso muita gente normaliza e usa dot (uma multiplicação a menos por dimensão). Euclidean não é equivalente (mede distância, não ângulo). Manhattan é outra métrica. Jaccard é para conjuntos, não vetores.
➡️ TRANSIÇÃO: "Pergunta 2."

---

### Slide 76 — Quiz: Pergunta 2

**Título**: Quiz — Pergunta 2
**Objetivo**: Verificar compreensão.
**Conteúdo**:
- "Quando GraphRAG supera vector RAG de forma mais clara?"
- A) Quando a pergunta é sobre um fato específico em um documento
- B) Quando a pergunta exige raciocínio multi-hop entre entidades
- C) Quando a latência é o requisito mais importante
- D) Quando o corpus é pequeno (< 100 documentos)
- Resposta: B

**Diagrama**: 4 opções em cards
**Animação**: Opções aparecem
**Imagem**: Cards de múltipla escolha
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A resposta é B) raciocínio multi-hop. GraphRAG brilha quando a pergunta exige encadear relacionamentos entre entidades (A → B → C). Fato específico (A) é melhor com vector RAG. Latência baixa (C) é melhor com vector RAG. Corpus pequeno (D) não justifica o custo de GraphRAG.
➡️ TRANSIÇÃO: "Pergunta 3."

---

### Slide 77 — Quiz: Pergunta 3

**Título**: Quiz — Pergunta 3
**Objetivo**: Verificar compreensão.
**Conteúdo**:
- "Em um pipeline híbrido, o que o RetrievalAgent faz?"
- A) Sempre faz busca vetorial e grafo em paralelo
- B) Classifica a pergunta para escolher vector, graph ou híbrido
- C) Substitui o vector DB por um grafo
- D) Gera embeddings para o grafo
- Resposta: B

**Diagrama**: 4 opções em cards
**Animação**: Opções aparecem
**Imagem**: Cards de múltipla escolha
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A resposta é B). O RetrievalAgent CLASSIFICA a pergunta (vector/graph/híbrido) e despacha para a estratégia certa. Nem toda pergunta precisa de híbrido — o router economiza retrieval desnecessário. A) descreve "sempre híbrido" (mais caro). C) e D) estão conceitualmente errados (não substitui nem gera embeddings para grafo).
➡️ TRANSIÇÃO: "Como isso conecta com o resto da especialização?"

---

### Slide 78 — Conexão com Próximos Módulos

**Título**: Conexão com Próximos Módulos
**Objetivo**: Mostrar como ETHAGT07 conecta com o resto da especialização.
**Conteúdo**:
- ETHAGT14 — Escalabilidade: vector DBs em produção multi-tenant
- ETHAGT90 — Capstone: integra vector + grafo no projeto final
- ETHAGT05 — Memória: vector DB como memória semântica de agentes
- ETHAGT12 — AgentOps: observabilidade de pipelines híbridos

**Diagrama**: D46 — Mapa da especialização com ETHAGT07 no centro
**Animação**: Conexões aparecem
**Imagem**: Mind map
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: ETHAGT07 conecta com 4 módulos. ETHAGT14 (Escalabilidade) aprofunda vector DBs em produção multi-tenant. ETHAGT90 (Capstone) integra vector + grafo no projeto final. ETHAGT05 (Memória) usa vector DB como memória semântica de agentes. ETHAGT12 (AgentOps) cobre observabilidade de pipelines híbridos. O que vocês aprenderam hoje é a INFRAESTRUTURA que sustenta esses módulos.
➡️ TRANSIÇÃO: "Leitura recomendada e referências."

---

### Slide 79 — Leitura Recomendada e Referências

**Título**: Leitura Recomendada e Referências
**Objetivo**: Indicar o que ler e listar fontes.
**Conteúdo**:
- Obrigatório: Edge, D. et al. *GraphRAG: From Local to Global* (Microsoft, arXiv:2404.16130)
- Obrigatório: Lewis, P. et al. *RAG* (arXiv:2005.11401)
- Recomendado: Pan, S. et al. *Unifying Large Language Models and Knowledge Graphs* (arXiv:2306.08302)
- Documentação: Qdrant, Milvus, Weaviate, Neo4j, pgvector
- Próxima aula: ETHAGT14 — Escalabilidade

**Diagrama**: Lista de referências com logos
**Animação**: Referências aparecem
**Imagem**: Capas dos papers
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Leitura obrigatória: o paper do GraphRAG (Edge et al., arXiv:2404.16130) — é o fundamento canônico. E o paper do RAG original (Lewis et al., arXiv:2005.11401) para entender de onde viemos. Recomendado: o survey do Pan et al. (arXiv:2306.08302) unindo LLMs e knowledge graphs. Documentação: Qdrant, Milvus, Weaviate, Neo4j, pgvector — escolham a do DB que vão usar no projeto. Próxima aula: ETHAGT14 — Escalabilidade.
➡️ TRANSIÇÃO: "Q&A e encerramento."

---

### Slide 80 — Q&A / Encerramento

**Título**: Q&A / Encerramento
**Objetivo**: Abrir para perguntas e encerrar.
**Conteúdo**:
- "Perguntas?"
- Contato do professor
- "Na próxima aula: ETHAGT14 — Escalabilidade"
- Lembrete: iniciar Lab 1 (Vector DB Bake-off)

**Diagrama**: Logo Etho + fundo `etho-dark`
**Animação**: Fade out
**Imagem**: Logo Etho centralizado
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Hora do Q&A. Se não houver perguntas, faça a pergunta inversa: "Qual parte foi menos clara — vector, grafo ou híbrido?" Lembrem de iniciar o Lab 1 (Vector DB Bake-off) — comparar Qdrant, pgvector e Chroma no mesmo corpus. E o projeto do módulo: pipeline híbrido com benchmark. Obrigado pela atenção!
❓ PERGUNTA PARA A TURMA: "Perguntas? Ou: qual parte foi menos clara?"
⚠️ ERROS COMUNS: Nenhuma pergunta no Q&A costuma significar que alunos estão sobrecarregados. Sugira revisar os slides e trazer dúvidas no fórum. Disponibilidade para horário de atendimento.
➡️ TRANSIÇÃO: "Fim da aula. Vejo vocês em ETHAGT14!"
