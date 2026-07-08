# GraphRAG: Uniting LLMs and Knowledge Graphs for RAG

> **Autores**: Darren Edge, Ha Trinh, Newman Cheng, Joshua Bradley, Alex Chao, Apurva Gandhi, Jasmine Bayrooti, Benno Stein, Gabriel Ilharco, Alex Trott, Sujith Ravi, Douwe Kiela  
> **Venue/Ano**: Microsoft Research, Julho 2024 · arXiv:2404.16130  
> **URL**: https://arxiv.org/abs/2404.16130

## TL;DR
GraphRAG constroi um **grafo de conhecimento** a partir do corpus, usa comunidades Leiden para sumarização hierárquica, e responde perguntas globais que exigem síntese sobre o corpus inteiro.

## Contribuições
- Indexação em grafo com comunidades (Leiden) para sumarização hierárquica
- Respostas a perguntas **globais** (todo o corpus) vs locais (documentos específicos)
- Geração de comunidades → sumários → respostas em múltiplos níveis de granularidade

## Método
**Index**: extrair entidades e relações (LLM) → construir grafo → detectar comunidades (Leiden) → sumarizar comunidades → gerar respostas para cada comunidade. **Query**: mapear pergunta a comunidades relevantes, sintetizar respostas parciais.

## Resultados
- Supera RAG naive em perguntas globais (síntese) por 20+ pontos
- Respostas mais abrangentes e estruturadas
- Útil para corpora grandes e heterogêneos

## Limitações
- Custo de indexação alto (extração de entidades para todo o corpus)
- Complexidade de implementação
- Overkill para perguntas factuais simples

## Relação com a Especialização
**Fundamento de ETHAGT07** (KG & Vector DBs). GraphRAG é o estado da arte em integração de knowledge graphs com LLMs. Padrão `15-RAG/07-graphrag.md` e laboratório dedicado em ETHAGT07.
