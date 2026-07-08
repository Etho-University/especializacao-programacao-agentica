# ETHAGT06 — Exercícios

> Exercícios para aula e para casa.
> Organizados por tipo: em aula, individual, em duplas, projeto.

---

## Exercícios em Aula

### E1 — Responder Direto ou Recuperar? (Votação Rápida)
**Slide**: 23
**Tempo**: 2 min
**Formato**: Individual, votação de mão levantada

**Enunciado**: Para cada pergunta abaixo, vote: Direto (D) ou Recuperar (R)?

1. "O que é Python?"
2. "Qual a política de home office da Etho?"
3. "Quem escreveu Dom Casmurro?"
4. "Compare as APIs de dois produtos internos"
5. "Qual a temperatura de ebulição da água?"

**Gabarito**:
1. D (conhecimento paramétrico)
2. R (conhecimento específico, interno)
3. D (conhecimento paramétrico)
4. R + query rewrite (comparação exige dois retrievals)
5. D (conhecimento paramétrico)

---

### E2 — Adaptive RAG vs Self-RAG em FAQ Jurídico (Duplas)
**Slide**: 44
**Tempo**: 5 min
**Formato**: Duplas, 3 min discussão + 2 min compartilhar

**Enunciado**: Cenário: sistema de FAQ jurídico com 10.000 documentos.

1. Quando usar Adaptive RAG vs Self-RAG?
2. Justifique com 3 critérios: tipo de pergunta, custo, qualidade esperada.
3. Escreva o prompt de reflexão para um doc recuperado (estilo Self-RAG via prompting).

**Gabarito**:
- **Adaptive RAG**: perguntas simples, latência crítica, tolerância a imprecisão.
- **Self-RAG**: alucinação inaceitável (jurídico!), custo aceitável, garantia de grounding.
- **Prompt de reflexão**: "Dado o documento abaixo e a pergunta, julgue: (a) o documento é relevante? (b) a resposta é totalmente suportada pelo documento? Responda com JSON `{relevante: yes|no, suportada: fully|partly|no}`."

---

### E3 — Escolhendo a Estratégia de Qualidade (Duplas)
**Slide**: 66
**Tempo**: 2 min
**Formato**: Duplas, 2 min discussão

**Enunciado**: Para cada cenário, escolha a estratégia de qualidade e justifique com 2 critérios:

1. Documentação técnica em inglês (10k páginas)
2. FAQ jurídico em português (5k docs)
3. Catálogo de produtos com imagens (50k items)

**Gabarito**:
1. **Hybrid search (BM25 + densa) + re-rank** — termos técnicos exigem match lexical (BM25); semântica para paráfrases (densa); re-rank para filtrar top-k.
2. **Query rewriting + semantic chunking** — sinônimos jurídicos (reescrita); docs densos (semântico).
3. **Multimodal (CLIP) + ColBERT** — imagens exigem embeddings visuais; terminologia específica de produto (ColBERT granular).

---

## Exercícios Individuais (para casa)

### E4 — Diferencie Adaptive RAG de Self-RAG
**Tempo estimado**: 10 min
**Formato**: Individual, escrito

**Enunciado**: Em suas palavras, diferencie Adaptive RAG de Self-RAG em 3-4 frases. Use um exemplo onde cada brilha.

**Critério de avaliação**:
- Define Adaptive RAG como "decide SE recuperar" ✅
- Define Self-RAG como "reflete sobre docs E resposta (hallucination check)" ✅
- Exemplo de Adaptive é realista (pergunta trivial → direto) ✅
- Exemplo de Self-RAG é realista (jurídico/médico → grounding crítico) ✅

---

### E5 — Prompt de Re-Ranking por Relevância
**Tempo estimado**: 15 min
**Formato**: Individual, código

**Enunciado**: Escreva um prompt (estruturado, com saída JSON via Pydantic) que re-rankeia 5 documentos recuperados por relevância à pergunta. O prompt deve:

- Receber a pergunta e a lista de 5 documentos
- Retornar um score de relevância (0-10) para cada documento
- Justificar brevemente cada score
- Ordenar do mais ao menos relevante

**Exemplo de resposta**:
```python
from pydantic import BaseModel, Field

class RankedDoc(BaseModel):
    doc_id: str = Field(description="Identificador do documento")
    score: int = Field(ge=0, le=10, description="Score de relevância 0-10")
    justificativa: str = Field(description="Por que este score?")

class ReRankOutput(BaseModel):
    ranked: list[RankedDoc] = Field(description="Lista ordenada do mais ao menos relevante")

RERANK_PROMPT = """Você é um avaliador de relevância.
Dada a pergunta do usuário e uma lista de documentos, atribua um score de relevância (0-10) para cada documento.

Pergunta: {question}

Documentos:
{documents}

Retorne JSON no formato especificado. Ordene do mais ao menos relevante."""
```

**Poka-yokes aplicados**:
- `score` é `int` com `ge=0, le=10` (não pode errar)
- `doc_id` força rastreabilidade
- `justificativa` obriga reasoning explícito

---

### E6 — Quando CRAG Decide Buscar na Web?
**Tempo estimado**: 10 min
**Formato**: Individual, escrito

**Enunciado**: Responda em 2-3 frases: em CRAG, quando o sistema decide buscar na web em vez de usar os documentos locais? Dê um exemplo concreto.

**Gabarito**:
O sistema busca na web quando o avaliador de relevância classifica a maioria dos documentos locais como `incorreto` (irrelevantes). Isso acontece quando a base local não tem cobertura para a pergunta, está desatualizada ou a pergunta é sobre um evento recente.

**Exemplo**: pergunta "Qual a última versão do LangChain?" — a base local pode ter docs de 6 meses atrás; o avaliador percebe que estão desatualizados → fallback para web search.

---

### E7 — Estratégias de Chunking: Quando Cada Brilha?
**Tempo estimado**: 15 min
**Formato**: Individual, tabela

**Enunciado**: Para cada estratégia de chunking abaixo, dê: (a) uma vantagem, (b) uma desvantagem, (c) um caso de uso ideal.

1. Chunking fixo (512 tokens)
2. Chunking semântico
3. Chunking hierárquico (parent-child)
4. Late chunking (Contextual Retrieval)

**Gabarito**:

| Estratégia | Vantagem | Desvantagem | Caso ideal |
|---|---|---|---|
| Fixo | Simples, rápido | Quebra contexto | Protótipo, docs uniformes |
| Semântico | Preserva tópicos | Mais caro (embeddings) | Docs densos, manuais |
| Hierárquico | Contexto rico (parent) | Complexo de implementar | Docs estruturados (livros, leis) |
| Late chunking | Embeddings ricos (-50% falhas) | Processa doc inteiro | Corpus técnico, produção |

---

### E8 — Verdadeiro/Falso Justificado
**Tempo estimado**: 10 min
**Formato**: Individual, escrito

**Enunciado**: Responda V ou F e justifique em 1-2 frases:

1. "Sempre adicionar mais docs recuperados melhora a resposta."
2. "Self-RAG original funciona com GPT-4 sem fine-tuning."
3. "Re-ranking sempre melhora a qualidade do RAG."
4. "Faithfulness alta implica answer relevance alta."
5. "HyDE é melhor que query rewriting simples."

**Gabarito**:
1. **F** — Mais docs = mais ruído. Sem re-rank, chunks irrelevantes "afogam" os bons.
2. **F** — Self-RAG original é um modelo fine-tuned. Funciona com GPT-4 só via prompting (adaptado).
3. **F** — Re-rank melhora precision mas adiciona latência/custo. Em latência crítica, pode não valer.
4. **F** — Tensão: alta faithfulness (só usa docs) pode baixar relevance (não responde totalmente). Métricas independentes.
5. **Depende** — HyDE é melhor quando a query é muito diferente dos docs. Query rewriting basta para sinônimos.

---

## Projeto do Módulo

### P1 — Sistema RAG de Produção com Pipeline Agêntico
**Prazo**: 3 semanas
**Formato**: Individual ou em duplas
**Carga**: ~15h

**Descrição**: Construir um sistema RAG de produção sobre um corpus técnico (ex.: documentação Etho, docs de um framework open-source), com:

1. **Pipeline agêntico** — escolher entre Adaptive RAG, CRAG, Self-RAG ou Agentic RAG (justificar no ADR)
2. **Engenharia de qualidade** — chunking, re-ranking, hybrid search ou query rewriting (pelo menos 2)
3. **Eval automatizado** — dataset de holdout (mínimo 50 perguntas com ground truth) + Ragas
4. **Multi-tenant** — isolamento de dados entre inquilinos

**Entregáveis**:
- Repositório Git com o sistema
- Eval report (template `24-Templates/template-eval-report.md`)
- ADR (Architecture Decision Record) justificando escolhas
- Demo ao vivo: agente respondendo com fontes

**Critério de sucesso**:
- **Faithfulness ≥ 0.85** no dataset de holdout
- **Context recall ≥ 0.80** no dataset de holdout
- Latência P95 < 5s por resposta
- ADR justifica ≥3 decisões arquiteturais

**Avaliação** (rubrica de 4 pilares):

| Pilar | Peso | Critério |
|---|---|---|
| Técnico | 40% | Sistema funcional, eval report, qualidade das métricas |
| Consultivo | 30% | Apresentação dos resultados para "cliente" (clareza, recomendações) |
| Comportamental | 20% | Code review de uma dupla |
| Prático | 10% | Demo ao vivo: agente respondendo com fontes |

**Nota mínima de aprovação**: 3.0
