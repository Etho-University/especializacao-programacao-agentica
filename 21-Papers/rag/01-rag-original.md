# RAG: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

> **Autores**: Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, Sebastian Riedel, Douwe Kiela  
> **Venue/Ano**: NeurIPS 2020 · arXiv:2005.11401  
> **URL**: https://arxiv.org/abs/2005.11401

## TL;DR
RAG combina um **retriever** (Dense Passage Retrieval) com um **generator** (BART/Llama) em um modelo híbrido: o generator condiciona a resposta em documentos recuperados.

## Contribuições
- Framework que fundamenta retrieval-augmented generation
- Demonstra que integrar conhecimento externo reduz alucinação e melhora facticidade
- Dois variantes: RAG-Sequence (mesmo doc para toda a sequência) e RAG-Token (doc diferente por token)

## Método
**Retriever**: DPR codifica query e documentos em espaço denso. Top-k recuperados via MIPS. **Generator**: BART codifica query + doc recuperado e gera resposta. Treinado end-to-end.

## Resultados
- Open-domain QA (Natural Questions): supera modelos sem retrieval por 10+ pontos
- Fact verification: melhora significativa
- Parametric memory é complementada por non-parametric memory

## Limitações
- Retriever fixo (não adaptativo)
- Sem iteração: recupera uma vez, gera uma vez
- Depende de qualidade do corpus indexado

## Relação com a Especialização
**Fundamento de ETHAGT06 e ETHAGT07**. Todo o espectro RAG da Especialização (Naive → Adaptive → CRAG → Self-RAG → GraphRAG → Agentic) constroi sobre RAG original. Lab 1 de ETHAGT06 implementa RAG naive.
