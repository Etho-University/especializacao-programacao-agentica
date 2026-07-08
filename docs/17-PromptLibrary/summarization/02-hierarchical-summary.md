# summarization/02-hierarchical-summary.md

## objetivo
Prompt para sumarização hierárquica (multi-nível): primeiro segmentos individuais, depois sumário de alto nível, depois sumário executivo.

## variáveis
- `{{document}}` — texto completo a ser sumarizado
- `{{segment_size}}` — tamanho de cada segmento (ex.: 1000 tokens ou 5 parágrafos)
- `{{summary_levels}}` — níveis desejados (ex.: 3: detalhado, médio, executivo)

## template

```
Summarize the following document at {{summary_levels}} levels of detail.

Document:
{{document}}

Segment size: {{segment_size}}

Process:
1. First, divide the document into segments of approximately {{segment_size}} tokens.
2. For each segment, produce a 2-3 sentence summary.
3. Group these segment summaries into sections and produce a medium-level summary for each section.
4. Finally, produce an executive summary (1 paragraph) covering the entire document.

Output format:

## Segment Summaries
- Segment 1: ...
- Segment 2: ...

## Section Summaries
- Section A: ...
- Section B: ...

## Executive Summary
(one paragraph)

Ensure each level adds abstraction — do not simply concatenate lower-level summaries.
```

## exemplo de uso
Sumarizar um whitepaper de 30 páginas: executivo → 1 parágrafo, seções → 1 parágrafo cada, segmentos → 2-3 frases cada.

## trade-offs
- Segmentação rígida (tamanho fixo) pode quebrar no meio de uma ideia
- Níveis demais geram sumários redundantes
- Muito eficaz para documentos longos, mas consome múltiplas chamadas de LLM

## variações
- **Sliding window summary**: segmentos com overlap para evitar corte no meio de ideias
- **Query-focused hierarchy**: cada nível prioriza informações relevantes a uma query específica
- **Recursive summarization**: aplicar o mesmo prompt recursivamente ao output até caber em N tokens
