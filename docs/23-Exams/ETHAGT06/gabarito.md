# ETHAGT06 — Gabarito da Prova

> Restrito a mentores. Respostas esperadas e critérios de correção para [`prova.md`](prova.md).

## Parte 1 — Conceitos

**1. (b) Adaptive RAG roteia por complexidade via classificador externo; Self-RAG usa tokens de reflexão internos.** Adaptive RAG é essencialmente routing (ETHAGT03) aplicado à recuperação — um classificador decide se responde direto, recupera uma vez ou multi-hop. Self-RAG (Asai et al.) é um modelo *treinado* para emitir tokens de reflexão (`[Retrieve]`, `[Relevant]`, `[Supported]`) que controlam o processo internamente. Ref.: Capítulo 2 — Adaptive RAG e Capítulo 4 — Self-RAG.

**2. FALSO.** Adicionar mais documentos recuperados nem sempre melhora — pode *diluir* a relevância (mais ruído), aumentar custo/latência e causar "lost in the middle". O padrão correto é retrieve K grande (ex.: 20), re-rank para top-N pequeno (ex.: 5). Ref.: Capítulo 6 — Engenharia de qualidade, §6.2 (Re-ranking).

**3. (b) O sistema descarta os documentos e busca na web como fallback.** CRAG classifica os recuperados em três estados: correto (refina + usa), ambíguo (usa parte + web), incorreto (descarta + busca na web). A inovação é tratar a recuperação como *falível* e ter um plano B. Ref.: Capítulo 3 — CRAG, §3.2.

**4. VERDADEIRO.** O anti-pattern "vector DB resolve tudo" é exatamente isso: acreditar que vector search é um sistema completo. Na verdade, vector search é *uma etapa* de recuperação. A evolução para RAG agêntico consiste em adicionar inteligência ao redor: decidir se recuperar, como recuperar, avaliar e corrigir. Ref.: Capítulo 1 — Por que o RAG ingênuo falha, §1.4.

## Parte 2 — Aplicação e trade-off

**5.** Três classes de falha + correções: (i) **Chunking ruim** → chunking semântico/hierárquico/contextual (não por tamanho fixo); (ii) **Sem re-ranking** → adicionar re-ranker (Cohere, bge) para reordenar por relevância; (iii) **Sem query rewriting** → reescrever a pergunta do usuário em termos alinhados ao corpus (ou HyDE). Ref.: Capítulo 1, §1.3 e Capítulo 6.

**6.** **Densa (vetorial):** boa em semântica, sinônimos, significado. **Esparsa (BM25/keyword):** boa em termos exatos, nomes próprios, códigos, siglas. **Hybrid search** é preferível quando o corpus mistura semântica e termos exatos (ex.: nomes de produtos, códigos que não casam bem por embedding). A fusão (Reciprocal Rank Fusion) combina os rankings. Ref.: Capítulo 6, §6.4.

**7.** Faithfulness baixa (0.45) com context recall alto (0.92) indica: **os documentos corretos foram recuperados**, mas a **resposta não é sustentada por eles** (alucinação — o modelo inventa além do que está nos docs). Técnica que ajuda: **chunking melhor** (chunks mais focados) e **prompt mais restritivo** ("responda APENAS com base no contexto fornecido"). O critério de sucesso do módulo é faithfulness ≥ 0.85. Ref.: Capítulo 7 — Avaliação, §7.2.

**8. VERDADEIRO.** HyDE (Gao et al., arXiv:2212.10496): o LLM gera um documento *hipotético* que seria a resposta ideal, e busca por documentos *similares a esse documento hipotético* — casando por semântica da resposta, não da pergunta. Útil quando a pergunta do usuário não é uma boa query. Ref.: Capítulo 6, §6.3.

## Parte 3 — Projeto curto

**9.** Espera-se o agente dirigindo o processo:
```python
def agentic_rag(pergunta):
    agente = Agent(
        tools=[search_internal, search_web, search_kg],
        system=RAG_PROMPT  # "resolva a pergunta; busque quantas vezes precisar; combine fontes"
    )
    return agente.run(pergunta)  # o agente decide quantos hops, quando parar
```
Avaliar: agente com tools de múltiplas fontes, decisão autônoma sobre hops, sem pipeline fixo. Ref.: Capítulo 5 — Agentic RAG, §5.1-5.2.

**10.** As 4 métricas canônicas (Ragas):
| Métrica | Mede |
|---|---|
| **Faithfulness** | A resposta é sustentada pelos documentos recuperados? (anti-alucinação) |
| **Answer relevance** | A resposta responde à pergunta? |
| **Context precision** | Os documentos recuperados são relevantes? |
| **Context recall** | Documentos relevantes foram recuperados? (cobertura) |

Ref.: Capítulo 7 — Avaliação, §7.2.

---

## Nota esperada por perfil

- **5,0**: diagnostica falhas, implementa padrões agênticos, domina métricas de avaliação.
- **4,0**: diferencia Adaptive/CRAG/Self-RAG, com pequenas imprecisões em engenharia.
- **3,0**: conhece os padrões mas não articula quando usar cada um.
- **<3,0**: precisa revisar RAG agêntico e avaliação.
