# ETHAGT07 — Exercícios

> Exercícios para aula e para casa.
> Organizados por tipo: em aula, individual, em duplas, projeto.

---

## Exercícios em Aula

### E1 — Vector, Graph, ou Híbrido? (Grupos)
**Slide**: 60
**Tempo**: 2 min
**Formato**: Grupos de 3-4, discussão + votação

**Enunciado**: Para cada cenário abaixo, decidam: Vector (V), Graph (G), ou Híbrido (H)? Justifiquem em uma frase.

1. Catálogo de produtos com busca por similaridade visual e textual
2. Base de conhecimento médica com relações entre doenças, sintomas e tratamentos
3. Documentos jurídicos com referências cruzadas entre jurisprudências
4. Chatbot de RH com perguntas sobre políticas da empresa
5. Sistema de recomendação de filmes baseado em gostos e elenco

**Gabarito**:
1. **V** — busca por similaridade é o core; sem necessidade de raciocínio multi-hop
2. **G ou H** — relações doença-sintoma-tratamento são estruturais; híbrido se precisa recuperar texto clínico
3. **H** — referências cruzadas (grafo) + texto das decisões (vector); híbrido clássico
4. **V ou H** — perguntas sobre políticas costumam ser lookup factual (vector); híbrido se há hierarquia de políticas
5. **H ou G** — gostos (similaridade) + elenco/relações (grafo); híbrido ou graph puro

---

### E2 — Cardinalidade de um KG (Duplas)
**Slide**: 36
**Tempo**: 2 min
**Formato**: Duplas, 2 min discussão + 1 min compartilhar

**Enunciado**: Para o domínio de vocês (ou um domínio de escolha), estimem:

1. Quantas entidades (nós) vocês teriam?
2. Quantas relações (arestas)?
3. Qual a densidade média (relações por entidade)?

**Gabarito (ordem de magnitude)**:
- 10k-100k entidades para um corpus de 10k-50k documentos
- 50k-500k relações
- 5-15 relações por entidade em média
- Depende do domínio: farmacêutica e jurídico têm maior densidade; RH menor

---

### E3 — Pergunta da DEMO (Duplas)
**Slide**: 47
**Tempo**: 2 min
**Formato**: Duplas, 2 min discussão

**Enunciado**: Após a DEMO do GraphRAG (Slide 46), discutam:

1. O GraphRAG errou alguma coisa na demo? Onde?
2. Qual o custo aproximado da construção do grafo (em tokens)?
3. Se o corpus mudar (novos docs), quanto custa reindexar?

**Gabarito**:
1. **Erros típicos**: relações alucinadas, entidades ambíguas não resolvidas (coreferência), comunidades ruidosas
2. **Custo**: para o corpus da demo, estimar chamadas LLM (extração + relações + sumários)
3. **Reindexação**: mais barato que construção total se incremental, mas entity resolution e re-sumarização de comunidades afetadas ainda custam

---

### E4 — Sempre Híbrido? (Votação)
**Slide**: 61
**Tempo**: 1 min
**Formato**: Individual, votação de mão levantada

**Enunciado**: Verdadeiro ou falso: "Sempre preferir híbrido."

**Gabarito**: **Falso**. Híbrido adiciona complexidade (2 sistemas, router, reconciliation) e custo. Justificado quando vector sozinho falha em perguntas importantes E o valor justifica o custo. Regra: comece com vector, adicione grafo com evidência de gap.

---

## Exercícios Individuais (para casa)

### E5 — Query Cypher: "Co-autores de X"
**Tempo estimado**: 15 min
**Formato**: Individual, código

**Enunciado**: Escreva uma query Cypher que encontre os co-autores de um autor "X", ordenados pelo número de papers co-escritos, limitando aos top 10.

**Gabarito**:
```cypher
MATCH (a:Author {name: "X"})-[:WROTE]->(p:Paper)<-[:WROTE]-(b:Author)
WHERE b <> a
RETURN DISTINCT b.name AS coauthor, count(p) AS papers
ORDER BY papers DESC
LIMIT 10
```

**Critério de avaliação**:
- Usa MATCH com padrão Author → Paper ← Author ✅
- Exclui o próprio autor (WHERE b <> a) ✅
- Conta papers (count(p)) ✅
- Ordena e limita ✅

---

### E6 — Cenários: Vector DB ou Knowledge Graph?
**Tempo estimado**: 20 min
**Formato**: Individual, escrito

**Enunciado**: Para cada um dos 5 cenários abaixo, indique Vector DB (V) ou Knowledge Graph (KG) e justifique em 2-3 frases:

1. Buscar documentos semelhantes a uma patente
2. Rastrear a cadeia de fornecedores de um componente
3. Recomendar produtos "parecidos com este"
4. Responder "quais medicamentos este paciente não pode tomar?"
5. Buscar "documentos sobre mudança climática"

**Gabarito**:
1. **V** — similaridade semântica da patente
2. **KG** — cadeia de fornecedores é relacional (multi-hop)
3. **V** — similaridade de produtos
4. **KG** — interações medicamentosas são relacionais (multi-hop: paciente → medicação → interage → contraindicado)
5. **V** — busca semântica por tema

---

### E7 — Quando pgvector é Melhor que Qdrant?
**Tempo estimado**: 10 min
**Formato**: Individual, escrito

**Enunciado**: Em suas palavras, explique em 3-4 frases quando pgvector é melhor que Qdrant. Dê um exemplo concreto.

**Gabarito (critérios)**:
- Já usa Postgres e não quer adicionar infra ✅
- Precisa de transações ACID com vetores ✅
- Volume até ~1M de vetores (pgvector resolve) ✅
- Exemplo: aplicação que já tem Postgres e adiciona busca semântica em uma tabela de produtos ✅

---

### E8 — Por Que GraphRAG é Caro? Justifique o Custo
**Tempo estimado**: 15 min
**Formato**: Individual, escrito

**Enunciado**: GraphRAG custa $50-$500 de construção para 1000 documentos. Justifique esse custo:

1. Liste as 3 etapas que consomem chamadas LLM
2. Estime o número de chamadas para cada etapa
3. Dê um exemplo de domínio onde o custo é justificado

**Gabarito**:
1. **Etapas**: (a) extração de entidades (1 chamada/chunk), (b) extração de relações (1 chamada/par de entidades), (c) sumarização de comunidades (1 chamada/comunidade)
2. **Estimativa**: 1000 docs → ~1000 extrações de entidades + ~3000 relações + ~1500 sumários = ~5500 chamadas
3. **Domínio justificado**: farmacêutica (interações medicamentosas = risco de vida), jurídico (precedências = decisão judicial)

---

### E9 — Verdadeiro/Falso Justificado
**Tempo estimado**: 15 min
**Formato**: Individual, escrito

**Enunciado**: Responda V ou F e justifique em 2-3 frases:

1. "Sempre preferir híbrido."
2. "Cosine e dot product dão o mesmo ranking quando embeddings são normalizados."
3. "Vector DB é melhor que DB relacional para busca por igualdade (WHERE id = 42)."
4. "GraphRAG substitui completamente vector RAG."
5. "É seguro confiar cegamente em triplas extraídas por LLM."

**Gabarito**:
1. **F** — Híbrido adiciona complexidade e custo. Só quando vector falha e o valor justifica.
2. **V** — Quando normalizados (norma = 1), cosine = dot product. Por isso muita gente normaliza e usa dot (mais rápido).
3. **F** — DB relacional é melhor para igualdade. Vector DB é para similaridade.
4. **F** — GraphRAG e vector RAG são complementares. Vector para lookup factual, GraphRAG para multi-hop/global.
5. **F** — LLMs alucinam relações. Schema restrito + validação + confiança na aresta.

---

### E10 — Implementar o Router do RetrievalAgent
**Tempo estimado**: 30 min
**Formato**: Individual, código

**Enunciado**: Implemente a função `retrieve` do RetrievalAgent em Python. A função deve:

1. Classificar a pergunta em "vector", "graph", ou "híbrido" (use um LLM com prompt simples)
2. Despachar para a estratégia correta
3. No caso híbrido, extrair entidades, encontrar relacionadas no grafo, e fazer vector search filtrado

**Exemplo de resposta**:
```python
def retrieve(question: str) -> list[Document]:
    strategy = classify_strategy(question)
    if strategy == "vector":
        return vector_search(question)
    elif strategy == "graph":
        return graph_traverse(question)
    else:
        entities = extract_entities(question)
        related = graph.find_related(entities)
        return vector_search(question, filter=related)

def classify_strategy(question: str) -> str:
    prompt = f"""
    Classifique esta pergunta em uma estratégia de retrieval:
    - "vector": lookup factual, busca semântica, pergunta de 1 hop
    - "graph": pergunta sobre relacionamentos, conexões, multi-hop
    - "híbrido": documentos sobre entidades relacionadas (precisa de ambos)
    
    Pergunta: {question}
    Estratégia:"""
    return llm.complete(prompt).strip().lower()
```

**Critério de avaliação**:
- Função `retrieve` com classificação ✅
- Despacho condicional ✅
- Caso híbrido extrai entidades + filtra vector ✅
- `classify_strategy` usa LLM com prompt claro ✅

---

## Projeto do Módulo

### P1 — Pipeline Híbrido (Vector + Grafo) com Benchmark
**Prazo**: 2 semanas
**Formato**: Individual ou dupla
**Carga**: ~10h

**Descrição**: Construir um pipeline híbrido (vector + grafo) para um corpus técnico, com um agente que escolhe a estratégia de retrieval e justifica a escolha.

**Entrega**:
1. **Sistema**: pipeline híbrido funcional (vector DB + knowledge graph + RetrievalAgent)
2. **Benchmark**: comparar vector vs grafo vs híbrido em um conjunto de perguntas (incluindo multi-hop)
3. **ADR** (Architecture Decision Record): documento justificando as escolhas (qual vector DB, qual grafo, quando híbrido)

**Métricas do benchmark**:
- Success rate (% de perguntas respondidas corretamente)
- Latência p50/p99
- Custo por query

**Entregáveis**:
- Repositório Git com o sistema
- README com instruções de execução
- Relatório de benchmark (tabela + gráfico)
- ADR justificando escolhas

**Critério de sucesso**:
- Híbrido melhora success rate em casos multi-hop sem explodir custo
- ADR justifica escolhas com ≥3 critérios (valor do raciocínio, custo, latência)
- Benchmark tem ≥10 perguntas (incluindo multi-hop)

**Avaliação** (rubrica de 4 pilares):

| Pilar | Peso | Critério |
|---|---|---|
| Técnico | 40% | Sistema funcional, benchmark, qualidade da implementação |
| Consultivo | 30% | ADR — clareza da justificativa de escolhas |
| Comportamental | 20% | Code review de um colega |
| Prático | 10% | Demo ao vivo: query multi-hop respondida corretamente |

**Nota mínima de aprovação**: 3.0
