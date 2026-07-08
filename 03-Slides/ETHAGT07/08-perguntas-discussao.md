# ETHAGT07 — Perguntas para Discussão

> Perguntas para estimular debate durante e após a aula.
> Organizadas por profundidade: rápida (1-2 min) → média (3-5 min) → profunda (10+ min).

---

## Perguntas Rápidas (1-2 min)

### Q1 — Quando Similaridade Não Basta
"Pensem no sistema de vocês: existe uma pergunta que exige encadear 2+ fatos? O vector search atual responde?"
- **Objetivo**: Conectar a motivação ao caso real deles
- **Slide**: 5
- **Resposta esperada**: A maioria descobre que SIM existe — e que o vector search não encadeia bem.

### Q2 — Vector DB em Produção
"Quem aqui já usou um vector DB em produção? Qual?"
- **Objetivo**: Calibrar experiência prática
- **Slide**: 1, 18
- **Ação**: Contar mãos levantadas — ajustar profundidade do comparativo

### Q3 — Knowledge Graph em Produção
"Quem aqui já usou um knowledge graph (Neo4j, etc.) em produção?"
- **Objetivo**: Calibrar — costuma ser minoria
- **Slide**: 1, 27
- **Ação**: Contar mãos — se poucos, aprofundar fundamentos de triplas

### Q4 — Métrica Padrão
"Qual métrica de similaridade vocês usam hoje nos sistemas de vocês? Sabem por quê?"
- **Objetivo**: Revelar se a escolha é consciente ou default cego
- **Slide**: 13, 14
- **Resposta esperada**: Muitos usam cosine "porque era o default" — sem saber por quê.

### Q5 — Custo de GraphRAG
"Vocês imaginavam que GraphRAG custa $50-$500 de construção para 1000 docs?"
- **Objetivo**: Criar consciência de custo
- **Slide**: 48
- **Resposta esperada**: Surpresa — a maioria subestima o custo de construção.

---

## Perguntas Médias (3-5 min)

### Q6 — pgvector ou Qdrant?
"Para o sistema de vocês hoje: pgvector ou Qdrant? Por quê?"
- **Objetivo**: Aplicar o comparativo ao caso real deles
- **Slide**: 23, 24
- **Dica**: Se já usam Postgres, pgvector é a escolha de menor fricção. Qdrant se filtering complexo é core.

### Q7 — Cenário de Multi-hop
"Descrevam uma pergunta no domínio de vocês que exige multi-hop (encadear 3+ fatos). Como o vector search lida com ela hoje?"
- **Objetivo**: Identificar o "gap" que justificaria knowledge graph
- **Slide**: 27, 28, 38
- **Resposta esperada**: Vector search recupera chunks sobre o tema, mas não encadeia. Esse é o gap.

### Q8 — Híbrido ou Não?
"Para o domínio de vocês: vector sozinho resolve 90% das perguntas? Qual é o 10% que falha?"
- **Objetivo**: Avaliar se híbrido é justificado
- **Slide**: 53, 61
- **Dica**: Se o 10% que falha é crítico (multi-hop, relacional), híbrido vale. Se é marginal, vector basta.

### Q9 — Alucinação em Extração
"Vocês confiariam em triplas extraídas por LLM sem validação? Qual o risco?"
- **Objetivo**: Conscientizar sobre alucinação
- **Slide**: 34
- **Resposta esperada**: Não — LLMs alucinam relações. Schema restrito + validação + confiança na aresta.

### Q10 — Lineage na Prática
"Se o agente de vocês der uma resposta errada amanhã, vocês conseguem rastrear de onde veio?"
- **Objetivo**: Mostrar que sem lineage, debugging é impossível
- **Slide**: 58
- **Resposta esperada**: A maioria não tem lineage — caixa preta. Introduzir doc_id em nós e arestas.

---

## Perguntas Profundas (10+ min)

### Q11 — GraphRAG Vale para o Domínio de Vocês?
"Para o domínio de vocês: GraphRAG vale o custo de construção? Justifique com valor do raciocínio vs custo."
- **Objetivo**: Pensamento crítico sobre ROI
- **Slide**: 50
- **Resposta esperada**: Depende. Farmacêutica/jurídico: vale. Blog/catálogo simples: não vale. O critério é valor do multi-hop vs custo.

### Q12 — Sempre Híbrido é Over-Engineering?
"Por que 'sempre híbrido' é um anti-pattern? Em que caso híbrido é justificado?"
- **Objetivo**: Combater o reflexo "mais complexo = melhor"
- **Slide**: 61
- **Resposta esperada**: Híbrido adiciona complexidade (2 sistemas, router, reconciliation). Justificado quando vector falha em perguntas importantes E o valor dessas perguntas justifica o custo.

### Q13 — Reindexação e Troca de Modelo
"Vocês precisam trocar de modelo de embedding. Qual o impacto? Como fazer zero-downtime?"
- **Objetivo**: Pensar em operação real
- **Slide**: 66
- **Resposta esperada**: Vetores antigos são incompatíveis com o novo modelo. Estratégia: dual index (manter velho + novo durante transição) + swap atômico.

### Q14 — O Maior Risco de GraphRAG
"Qual o maior risco de implementar GraphRAG sem entender os trade-offs?"
- **Objetivo**: Conscientização sobre armadilhas
- **Slide**: 45, 71
- **Resposta esperada**: Custo explosivo (construção + manutenção) sem retorno proporcional. GraphRAG em domínio que não precisa de multi-hop = desperdício.

### Q15 — Agente que Escolhe Estratégia
"Como convencer um PM de que o RetrievalAgent (router) é melhor que 'sempre híbrido'?"
- **Objetivo**: Estruturar argumentos de trade-off para stakeholders
- **Slide**: 55, 56
- **Argumentos**: (1) latência menor para perguntas simples (router economiza retrieval desnecessário); (2) custo menor (nem toda query precisa de graph traversal); (3) transparência (o router justifica a escolha).

---

## Perguntas Bônus (para alunos avançados)

### Q16 — RDF/SPARQL vs Labeled Property Graph
"Neo4j usa Labeled Property Graph. RDF/SPARQL é outro paradigma (W3C). Quando cada um é melhor?"
- **Objetivo**: Aprofundar escolha de paradigma
- **Resposta**: LPG (Neo4j) é mais prático para aplicações (propriedades em nós e arestas). RDF/SPARQL é mais "acadêmico", padronizado (W3C), forte em Linked Open Data e interoperabilidade semântica.

### Q17 — Product Quantization vs Binary Quantization
"Quando preferir PQ e quando binary quantization?"
- **Objetivo**: Aprofundar trade-offs de quantização
- **Resposta**: PQ (90%+ redução, perda moderada) para a maioria dos casos. Binary (97% redução, perda maior) para escala extrema onde memória é o gargalo, com re-scoring para preservar qualidade.

### Q18 — GraphRAG Incremental
"Como manter GraphRAG atualizado sem reconstruir tudo a cada novo documento?"
- **Objetivo**: Pensar em manutenção incremental
- **Resposta**: Atualização incremental: extrair entidades/relações do novo doc, inserir no grafo, re-detectar comunidades AFETADAS (não todas), re-sumarizar apenas as comunidades modificadas. Complexo, mas mais barato que reconstrução total. Entity resolution para merge de duplicatas.

### Q19 — Comunidades que Mudam
"Se um novo documento conecta duas comunidades antes separadas, o que acontece?"
- **Objetivo**: Pensar em dinâmica de grafos
- **Resposta**: A estrutura de comunidades muda — as duas podem se fundir. Isso invalida os sumários antigos. Re-sumarização é necessária. Por isso a manutenção do GraphRAG é recorrente e cara.

### Q20 — Ontologias e LOD
"O que são ontologias e Linked Open Data (LOD)? Como se relacionam com knowledge graphs?"
- **Objetivo**: Conectar a fundamentos W3C
- **Resposta**: Ontologias definem os tipos e relações permitidas (schema formal). LOD é o ecossistema de datasets interligados na web (DBpedia, Wikidata). Knowledge graphs práticos (Neo4j) muitas vezes se inspiram em ontologias mas não exigem formalismo RDF completo.
