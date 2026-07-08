# Corrective RAG (CRAG): Corrective Retrieval Augmented Generation

> **Autores**: Shi-Qi Yan, Jia-Chen Gu, Yun Zhu, Zhen-Hua Ling  
> **Venue/Ano**: NAACL 2024 · arXiv:2401.15884  
> **URL**: https://arxiv.org/abs/2401.15884

## TL;DR
CRAG adiciona **avaliação da qualidade** do retrieved document e **correção** se for insatisfatório — busca na web como fallback ou reformula a query.

## Contribuições
- Mecanismo de avaliação de retrieved docs (relevância)
- Fallback adaptativo: se doc é irrelevante → busca web; se parcialmente relevante → decomposição
- Correção antes da geração, reduzindo alucinação por fonte

## Método
**Retriever** → **Evaluator** (T5 fine-tuned para relevância) → ramos: (1) doc relevante → geração, (2) doc irrelevante → busca web, (3) parcial → decomposição em sub-queries. **Generator** produz resposta final.

## Resultados
- 4 datasets de QA: CRAG supera RAG original e Self-RAG
- Robustez a retrieved docs de baixa qualidade
- Eficiente (só avalia quando necessário)

## Limitações
- Evaluator é modelo separado (fine-tuned)
- Fallback web pode introduzir latência
- Sem iteração (avalia uma vez)

## Relação com a Especialização
**Padrão fundamental de ETHAGT06**. CRAG é o precursor direto de RAG agentivo adaptativo. Padrão `15-RAG/03-corrective-rag.md` detalha implementação. Labs de ETHAGT06 implementam variante simplificada.
