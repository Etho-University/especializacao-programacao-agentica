# Caso de Estudo — GraphRAG em farmacêutica / jurídico

> ETHAGT07 · Onde GraphRAG brilha na prática.

## Contexto

Domínios com muitas entidades inter-relacionadas — farmacêutico (drogas, alvos, doenças, ensaios), jurídico (casos, precedentes, partes, leis), científico (autores, papers, instituições, tópicos) — são o terreno ideal para GraphRAG.

## Exemplo farmacêutico

**Pergunta**: *"Quais drogas em ensaios de fase 3 têm como alvo proteínas da família X e mostraram eficácia em doenças autoimunes?"*

Esta pergunta é **multi-hop**: precisa conectar droga → alvo → família de proteínas, e droga → ensaio → doença → categoria. Vector RAG recupera documentos similares mas não "conecta" as relações. GraphRAG traversa o grafo:

```cypher
MATCH (d:Droga)-[:ALVO]->(p:Proteina)-[:MEMBRO_DE]->(f:Familia {nome: "X"})
MATCH (d)-[:EM_ENSAIO]->(e:Ensaio {fase: 3})-[:PARA_DOENCA]->(doenca:Doenca)-[:CATEGORIA]->(:Categoria {nome: "autoimune"})
WHERE e.resultado = "eficaz"
RETURN d.nome
```

## Comparativo (estimativas de caso)

| Aspecto | Vector RAG | GraphRAG |
|---|---|---|
| Construção | barato | caro (extração + clusterização) |
| Latência por query | ~500ms | ~2s (local), ~10s (global) |
| Success em específicas | alto | alto |
| Success em multi-hop | baixo (~30%) | alto (~80%) |
| Manutenção | re-embed | re-clusterizar |

## Lições

1. **GraphRAG não substitui vector — complementa.** Use ambos.
2. **Construção cara se paga** se o domínio tem valor (descoberta de droga vale milhões por insight).
3. **Local vs global**: GraphRAG global brilha em "panorama"; local em específicas.
4. **Manutenção contínua**: novas drogas/ensaios exigem re-extração e re-clusterização.

## Referências

- Edge, D. et al. *GraphRAG*. arXiv:2404.16130.
- Microsoft GraphRAG implementation (GitHub).
- Aplicações: Pfizer, Novartis (relatos públicos).
