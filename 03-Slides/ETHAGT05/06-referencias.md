# ETHAGT05 — Referências

> Todas as fontes utilizadas na preparação e apresentação da aula.

---

## Canônicas (fundação do curso)

### 1. MemGPT: Towards LLMs as Operating Systems
- **Autores**: Charles Packer, Sarah Wooders, Kevin Lin, Vivian Fang, Shishir Patil, Ion Stoica, Joseph Gonzalez, Joseph Hellerstein
- **Data**: outubro 2023
- **arXiv**: 2310.08560
- **Resumo**: Apresenta a analogia central LLM-como-SO: context window como RAM, memória persistente como disco, e self-editing memory (o modelo gerencia suas próprias páginas). Base direta dos Slides 16, 37, 66.
- **Importância**: Canônica
- **Slides que referenciam**: 6, 16, 37, 52, 56, 66, 70

### 2. Generative Agents: Interactive Simulacra of Human Behavior
- **Autores**: Joon Sung Park, Joseph O'Brien, Carrie Cai, Meredith Ringel Morris, Percy Liang, Michael S. Bernstein
- **Venue**: UIST 2023
- **arXiv**: 2304.03442
- **Resumo**: 25 agentes em Smallville, cada um com memory stream (log de observações com timestamp), retrieval por recência + importância + relevância, e reflection (consolidação em insights). Demonstra que a arquitetura de memória define a identidade do agente. Base direta dos Slides 35, 52, 53, 56, 66.
- **Importância**: Canônica
- **Slides que referenciam**: 6, 35, 52, 53, 56, 66, 70

### 3. Reflexion: Language Agents with Verbal Reinforcement Learning
- **Autores**: Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao
- **Venue**: NeurIPS 2023
- **arXiv**: 2303.11366
- **Resumo**: Adiciona auto-crítica verbal e memória de falhas ao loop do agente. Fundamento da memória procedural (skills aprendidas pela reflexão sobre sucessos e erros). Base do Slide 12.
- **Importância**: Canônica
- **Slides que referenciam**: 12, 53

### 4. LangGraph — Persistence & Memory
- **URL**: https://langchain-ai.github.io/langgraph/concepts/persistence/
- **Resumo**: Documentação oficial do modelo de checkpointer do LangGraph. Define estado serializável, thread_id, checkpoint_id, resume/replay/branching. Implementações para Postgres, SQLite, Redis. Base direta de toda a Seção C (Slides 17-29).
- **Importância**: Canônica
- **Slides que referenciam**: 17, 19, 20, 21, 23, 25, 26, 28

---

## Importantes (complementam e aprofundam)

### 5. Lost in the Middle: How Language Models Use Long Contexts
- **Autores**: Nelson Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Beigelman, Noah Smith, Hannaneh Hajishirzi, Percy Liang
- **Data**: julho 2023
- **arXiv**: 2307.03172
- **Resumo**: Mostra que LLMs perdem precisão no meio de contextos longos (curva em U). Fundamento para por que context window maior não resolve memória. Base do Slide 9.
- **Importância**: Importante
- **Slides que referenciam**: 9, 32

### 6. Zep — Long-term Memory for Assistant Apps
- **URL**: https://www.getzep.com/
- **Resumo**: Sistema de memória de longo prazo para agentes. Combina graph memory (entidades + relações) com vector recall. Referência de produção para entity-centric memory. Base dos Slides 37, 54.
- **Importância**: Importante
- **Slides que referenciam**: 37, 54

### 7. A-MEM: Agentic Memory for Long-Term Recall
- **Data**: 2024
- **Resumo**: Proposta de memória agêntica em que o próprio agente decide o que memorizar, como consolidar, e o que esquecer. Evolução da ideia MemGPT.
- **Importância**: Importante
- **Slides que referenciam**: 6, 37

### 8. Episodic and Semantic Memory
- **Autor**: Endel Tulving
- **Data**: 1972
- **Resumo**: Fundação cognitiva da distinção entre memória episódica (eventos com tempo) e semântica (fatos/conhecimento). Referência teórica para a taxonomia de 4 camadas. Base dos Slides 10, 11, 15.
- **Importância**: Importante
- **Slides que referenciam**: 10, 11, 15

### 9. LangGraph `checkpoint-postgres`
- **URL**: https://github.com/langchain-ai/langgraph/tree/main/libs/checkpoint-postgres
- **Resumo**: Implementação de referência do checkpointer para Postgres. Base direta do Lab 1 (Checkpointer em Postgres) e da DEMO (Slide 28).
- **Importância**: Importante
- **Slides que referenciam**: 21, 28

---

## Complementares (leitura opcional)

### 10. Memória de Trabalho (Working Memory)
- **Autor**: Alan Baddeley e Graham Hitch
- **Data**: 1974
- **Resumo**: Modelo cognitivo de working memory com componentes (phonological loop, visuospatial sketchpad, central executive). Inspiração para o conceito de context window como memória de trabalho. Base do Slide 15.
- **Slides que referenciam**: 8, 15

### 11. Memória Procedural
- **Autor**: Larry Squire
- **Resumo**: Distinção entre memória declarativa (episódica + semântica) e não-declarativa (procedural, skills). Referência teórica para a camada procedural. Base do Slide 12, 15.
- **Slides que referenciam**: 12, 15

### 12. Qdrant Documentation
- **URL**: https://qdrant.tech/documentation/
- **Resumo**: Vector DB open-source. Documentação sobre hybrid search (vector + metadata filtering), re-ranking, payload filtering. Base do Lab 2.
- **Slides que referenciam**: 44, 45, 47

### 13. Anthropic — Effective Context Engineering for AI Agents
- **Data**: 2025
- **URL**: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- **Resumo**: Aprofundamento sobre gestão de contexto em agentes. Complementa a Seção D (gerenciamento de contexto) com visão prática de produção.
- **Slides que referenciam**: 31, 32, 33

### 14. LangSmith — Memory Traces
- **URL**: https://docs.smith.langchain.com/
- **Resumo**: Observabilidade de memória (quem acessou qual memória, quando, hit rate do recall). Base do Slide 63.
- **Slides que referenciam**: 63

### 15. Letta (antigo MemGPT-lib)
- **URL**: https://www.letta.com/
- **Resumo**: Framework de produção inspirado no MemGPT. Implementa self-editing memory em agentes reais.
- **Slides que referenciam**: 16, 37

---

## Ficha de Pesquisa

- **Arquivo**: `20-Research/ETHAGT05-pesquisa.md`
- **Última consulta**: Julho 2026
- **Revalidação**: Janeiro 2027 (estado da arte de memória de agentes evolui rapidamente; novas abordagens como A-MEM e Letta podem amadurecer)

---

## Como Usar Estas Referências

| Seção da Aula | Referência Principal | Referência Complementar |
|---|---|---|
| A — Abertura | (contexto do curso) | MemGPT, Generative Agents (timelines) |
| B — Tipos de Memória | Tulving (1972); Baddeley (1974) | Squire (procedural); Reflexion |
| C — Checkpointer | LangGraph docs | `checkpoint-postgres` README |
| D — Gerenciamento de Contexto | Lost in the Middle (arXiv:2307.03172) | Anthropic Context Engineering |
| E — Memória Vetorial | LangGraph docs; Qdrant docs | A-MEM (2024) |
| F — Semântica e Grafos | Generative Agents (arXiv:2304.03442) | Zep; Tulving (consolidação) |
| G — Produção | LangSmith (observabilidade) | LGPD/GDPR (direito ao esquecimento) |
| H — Fechamento | MemGPT; Generative Agents | Reflexion |
