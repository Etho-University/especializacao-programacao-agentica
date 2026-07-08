# ETHAGT90 — Ficha de Pesquisa: Capstone

> Especialização em Programação Agêntica · Universidade Etho · Julho 2026

## Fontes fundamentais para a arquitetura do Capstone

### Arquitetura de referência
1. **Anthropic**. *Building Effective Agents*. Disponível em: https://docs.anthropic.com/en/docs/build-with-claude/agentic (dez/2024). — Base para a distinção workflow/agente e topologia hierarchical.
2. **OpenAI**. *OpenAI Agents SDK*. 2025.
3. **LangGraph** docs — persistência, checkpointer, interrupt. https://langchain-ai.github.io/langgraph/

### MCP (camada de tools)
4. **MCP Specification** (2025-11-25). https://spec.modelcontextprotocol.io/
5. **Anthropic**. *MCP: Connecting AI to Tools and Data*. Nov/2024.

### Memory & RAG
6. Packer et al. *MemGPT*. arXiv:2310.08560. 2023.
7. Edge et al. *GraphRAG*. arXiv:2404.16130. Microsoft, 2024.
8. Asai et al. *Self-RAG*. arXiv:2310.11511. ICLR 2024.

### Orchestration & Durable Execution
9. **Temporal** docs. https://docs.temporal.io/
10. Helland, P. *Life Beyond Distributed Transactions* (Saga pattern). 2007.

### Multi-Agent Topologies
11. Li et al. *CAML: Collaborative Agents*. 2023.
12. Hong et al. *MetaGPT*. arXiv:2308.00352. 2023.

### AgentOps
13. SWE-bench. https://www.swebench.com/
14. GAIA. https://huggingface.co/gaia-benchmark
15. τ-bench. https://github.com/sierra-research/tau-bench

### Segurança
16. OWASP Top 10 for LLM Applications. 2025.
17. Prompt Injection: Greshake et al. arXiv:2302.12173.

### Pesquisa Autônoma (capstone domain)
18. Lu et al. *AI Scientist*. Sakana AI. arXiv:2408.06292. 2024.
19. Voyager: Wang et al. arXiv:2305.16291. 2023.

## Frameworks e ferramentas de referência
- LangGraph (workflows + agentes + checkpointer)
- OpenAI Agents SDK / Anthropic Claude API
- MCP SDKs (Python, TypeScript)
- Qdrant (vector DB), Neo4j (knowledge graph)
- Postgres + pgvector, Redis
- Temporal (durable execution)
- LangSmith / Phoenix (observabilidade)
- Docker (containerização)

## Benchmarks para validação do Capstone
- SWE-bench (coding agents)
- GAIA (general assistants)
- τ-bench (tool use)
- AgentDojo (segurança)
- Critical LLM evaluation: LLM-as-judge + golden dataset + human eval

## Atualização
- **Criada**: Julho 2026
- **Próxima revalidação**: Janeiro 2027
