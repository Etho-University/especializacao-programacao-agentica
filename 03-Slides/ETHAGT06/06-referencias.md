# ETHAGT06 — Referências

> Todas as fontes utilizadas na preparação e apresentação da aula.

---

## Canônicas (fundação do curso)

### 1. Lewis et al. — Retrieval-Augmented Generation
- **Autores**: Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, Sebastian Riedel, Douwe Kiela
- **Venue**: NeurIPS 2020
- **arXiv**: 2005.11401
- **Resumo**: Introduz o RAG original — parametric + non-parametric memory. Pipeline retrieve→generate. Fundamento direto da Seção B (Slides 9-14).
- **Importância**: Canônica
- **Slides que referenciam**: 7, 9, 83

### 2. Asai et al. — Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection
- **Autores**: Akari Asai, Zeqiu Wu, Yizhong Wang, Avirup Sil, Hannaneh Hajishirzi
- **Venue**: ICLR 2024
- **arXiv**: 2310.11511
- **Resumo**: Modelo treinado para emitir tokens de reflexão (`[Retrieve]`, `[Relevant]`, `[Fully supported]`, `[Utility]`) que controlam o fluxo. Fundamento direto da Seção E (Slides 35-44).
- **Importância**: Canônica
- **Slides que referenciam**: 7, 36, 37, 38, 39, 42, 85

### 3. Yan et al. — Corrective Retrieval Augmented Generation (CRAG)
- **Autores**: Shi-Qi Yan, Jia-Chen Gu, Yun Zhu, Zhen-Hua Ling
- **Venue**: ICML 2024
- **arXiv**: 2401.15884
- **Resumo**: Avaliador de relevância classifica docs em correto/ambíguo/incorreto; três caminhos (usar, refinar, web search). Fundamento direto da Seção D (Slides 24-34).
- **Importância**: Canônica
- **Slides que referenciam**: 7, 25, 26, 27, 28, 33, 80

### 4. Edge et al. — GraphRAG: From Local to Global
- **Autores**: Darren Edge, Ha Trinh, Newman Cheng, Joshua Bradley, Alex Chao, Apurva Mody, Steven Truitt, Jonathan Larson
- **Organização**: Microsoft
- **arXiv**: 2404.16130
- **Resumo**: Constrói grafo de conhecimento do corpus, agrupa em comunidades, sumariza. Permite responder perguntas globais. Base do Slide 52.
- **Importância**: Canônica
- **Slides que referenciam**: 7, 52, 83

---

## Importantes (complementam e aprofundam)

### 5. Gao et al. — HyDE: Hypothetical Document Embeddings
- **arXiv**: 2212.10496
- **Resumo**: Gerar resposta hipotética à pergunta, embedar a resposta e buscar por similaridade. Base do Slide 62.
- **Importância**: Importante
- **Slides que referenciam**: 62

### 6. Anthropic — Contextual Retrieval
- **Data**: setembro 2024
- **URL**: https://www.anthropic.com/news/contextual-retrieval
- **Resumo**: Late chunking — cada chunk recebe contexto do documento. Reduz falhas de recuperação em 30-50%. Base do Slide 59.
- **Importância**: Importante
- **Slides que referenciam**: 57, 59, 83

### 7. Ragas — Evaluation Framework for RAG
- **URL**: https://docs.ragas.io/
- **Resumo**: Métricas padronizadas (faithfulness, answer relevance, context precision/recall), LLM-as-judge, integração LangChain. Base da Seção H (Slides 67-73).
- **Importância**: Importante
- **Slides que referenciam**: 71, 72, 73

### 8. LangGraph Examples — adaptive_rag, crag, self_rag, agentic_rag
- **URL**: https://github.com/langchain-ai/langgraph/tree/main/docs/docs/tutorials
- **Resumo**: Implementações de referência das 4 arquiteturas em LangGraph. Base dos Slides 21, 32, 41, 53.
- **Importância**: Importante
- **Slides que referenciam**: 19, 21, 28, 32, 41, 53

### 9. Cohere — Rerank Documentation
- **URL**: https://docs.cohere.com/docs/reranking
- **Resumo**: Re-ranking cross-encoder como serviço. Base dos Slides 60-61.
- **Importância**: Importante
- **Slides que referenciam**: 61

### 10. TruLens — Tracing & Evaluation
- **URL**: https://www.trulens.org/
- **Resumo**: Tracing + avaliação de apps LLM/RAG com dashboard. Base do Slide 71.
- **Importância**: Importante
- **Slides que referenciam**: 71

### 11. DeepEval — Unit Testing for LLMs
- **URL**: https://docs.confident-ai.com/
- **Resumo**: Testes estilo pytest para LLMs, integra CI/CD. Base do Slide 71.
- **Importância**: Importante
- **Slides que referenciam**: 71

---

## Complementares (leitura opcional)

### 12. Karpukhin et al. — DPR (Dense Passage Retrieval)
- **arXiv**: 2004.04906
- **Resumo**: Recuperação densa bi-encoder. Contexto histórico para embeddings modernos.
- **Slides que referenciam**: 11

### 13. Khattab & Zaharia — ColBERT
- **arXiv**: 2004.12832
- **Resumo**: Representação multi-vetorial (1 vetor por token). Base do Slide 64.
- **Slides que referenciam**: 64

### 14. Santhanam et al. — ColBERTv2
- **arXiv**: 2112.01488
- **Resumo**: ColBERT otimizado para eficiência.
- **Slides que referenciam**: 64

### 15. Jina Reranker
- **URL**: https://jina.ai/reranker/
- **Resumo**: Re-ranker multilingual, API e self-hosted.
- **Slides que referenciam**: 61

### 16. BGE Reranker (BAAI)
- **URL**: https://huggingface.co/BAAI/bge-reranker-base
- **Resumo**: Re-ranker open-source para rodar local.
- **Slides que referenciam**: 61

### 17. Qdrant / Milvus Documentation
- **Resumo**: Vector DBs com suporte nativo a hybrid search.
- **Slides que referenciam**: 63

---

## Ficha de Pesquisa

- **Arquivo**: `20-Research/ETHAGT06-pesquisa.md`
- **Última consulta**: Julho 2026
- **Revalidação**: Janeiro 2027 (estado da arte de RAG evolui rápido)
