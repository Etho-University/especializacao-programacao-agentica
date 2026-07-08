# MemGPT: Operating System-like Memory Management for LLMs

> **Autores**: Charles Packer, Vivian Fang, Shishir G. Patil, Kevin Lin, Sarah Wooders, Joseph E. Gonzalez  
> **Venue/Ano**: arXiv, Outubro 2023 · arXiv:2310.08560  
> **URL**: https://arxiv.org/abs/2310.08560

## TL;DR
MemGPT aplica memória hierárquica inspirada em sistemas operacionais: **contexto** (working memory) + **arquivo externo** (storage), com gerenciamento automático de recall e eviction.

## Contribuições
- Framework de gestão de memória para LLMs com janela de contexto limitada
- Analogia OS: contexto principal = RAM, contexto externo = disco
- Geração automática de eventos de gerenciamento (recall, eviction, search)

## Método
**Working Context** (LLM context window): `system` + `core context` (memória principal) + `recent events`. **External Context**: `recall storage` (histórico) + `archival storage` (conhecimento permanente). O LLM emite `function calls` para gerenciar: `recall`, `search`, `core_memory_append/replace`.

## Resultados
- Conversas com contexto de 1M+ tokens efetivos (com janela de 4K)
- Memória consistente por centenas de turnos de diálogo
- Supera GPT-4 sem memória em QA sobre história longa

## Limitações
- Depende de function calling (não funciona com modelos sem tool use)
- Custo de passes extras para search/recall
- Política de eviction é manual (não aprendida)

## Relação com a Especialização
**Fundamento de ETHAGT05**. Conceito de 4 camadas de memória da Especialização é diretamente inspirado no MemGPT. Padrão de checkpointer (`16-Memory/01-checkpointer-pattern.md`) implementa mecanismo similar.
