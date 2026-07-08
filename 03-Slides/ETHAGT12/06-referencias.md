# ETHAGT12 — Referências

> Todas as fontes utilizadas na preparação e apresentação da aula.

---

## Canônicas (fundação do curso)

### 1. SWE-bench: Can Language Models Resolve Real-World GitHub Issues?
- **Autores**: Carlos Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan
- **Venue**: ICLR 2024
- **arXiv**: 2310.06770
- **Resumo**: Benchmark com 2.294 issues reais de 12 repositórios Python. Agente gera patch, testes validam. SWE-bench Verified (500 casos) com validação humana. Base direta da Seção E (Slides 47, 68).
- **Importância**: Canônica
- **Slides que referenciam**: 6, 45, 47, 51, 52, 53, 68, 77

### 2. GAIA: a benchmark for General AI Assistants
- **Autores**: Grégoire Mialon, Clémentine Fourrier, Craig Swift, Thomas Wolf, Yann LeCun, Thomas Scialom
- **Venue**: ICLR 2024 (Spotlight)
- **arXiv**: 2311.12983
- **Resumo**: 466 questões de raciocínio multi-step com tools. Níveis 1-3. Humanos: 92% no Level 1; GPT-4 + plugins: ~15%. Testa capacidade geral de agente assistente. Base direta da Seção E (Slide 48).
- **Importância**: Canônica
- **Slides que referenciam**: 6, 45, 48, 51, 53, 77

### 3. τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains
- **Autores**: Shunyu Yao, Noah Shinn, Fedor Moiseev, et al.
- **arXiv**: 2404.44529
- **Resumo**: Benchmark de tool-agent-user interaction em domínios (airline, retail). Agente simula atendente com APIs. Avalia success rate em tarefas com usuários simulados e políticas. Base direta da Seção E (Slide 49) e do projeto do módulo.
- **Importância**: Canônica
- **Slides que referenciam**: 6, 45, 49, 51, 53, 76, 77

---

## Importantes (complementam e aprofundam)

### 4. AgentBench: Evaluating LLMs as Agents
- **Autores**: Xiao Liu, Hao Yu, Hanchen Zhang, et al.
- **Venue**: ICLR 2024
- **arXiv**: 2308.03688
- **Resumo**: Benchmark com 8 ambientes (OS, DB, KG, web, card game, etc.). Avalia capacidades diversas de agentes. Base do Slide 50.
- **Importância**: Importante
- **Slides que referenciam**: 6, 45, 50, 77

### 5. WebArena: A Realistic Web Environment for Building Autonomous Agents
- **Autores**: Shuyan Zhou, Frank F. Xu, Hao Zhu, et al.
- **Venue**: ICLR 2024
- **arXiv**: 2307.13854
- **Resumo**: Navegação web autônoma em sites simulados. VisualWebArena adiciona compreensão visual. Base do Slide 50.
- **Importância**: Importante
- **Slides que referenciam**: 6, 45, 50, 77

### 6. Hamel Husain — Evals for LLMs
- **URL**: https://hamel.dev/blog/posts/evals/
- **Resumo**: Marco conceitual para avaliação de LLMs. Cunhou "vibes-based development". Base do Slide 13 e marco histórico do Slide 6.
- **Importância**: Importante
- **Slides que referenciam**: 6, 13, 29, 77

### 7. OpenTelemetry GenAI Semantic Conventions
- **URL**: https://opentelemetry.io/docs/specs/semconv/gen-ai/
- **Resumo**: Padrão CNCF de atributos para LLMs (gen_ai.system, gen_ai.request.model, gen_ai.usage.*). Base do Slide 18.
- **Importância**: Importante
- **Slides que referenciam**: 18, 19, 20

### 8. Anthropic — Avaliação de Claude em SWE-bench
- **URL**: https://www.anthropic.com/
- **Resumo**: Estudo de caso de como a Anthropic iterou Claude em SWE-bench com traces + eval contínua. Base do caso de estudo (Slide 68).
- **Importância**: Importante
- **Slides que referenciam**: 68

---

## Complementares (leitura opcional)

### 9. LangSmith Documentation
- **URL**: https://docs.smith.langchain.com/
- **Resumo**: Plataforma de observabilidade para LangChain/LangGraph. Base do Slide 19 e Labs.
- **Slides que referenciam**: 19, 24

### 10. Phoenix (Arize) Documentation
- **URL**: https://docs.arize.com/phoenix
- **Resumo**: LLM observability open source. Base do Slide 19 e Labs.
- **Slides que referenciam**: 19, 24

### 11. Langfuse Documentation
- **URL**: https://langfuse.com/docs
- **Resumo**: Plataforma open source self-hostable de traces + eval + prompt management. Base do Slide 19.
- **Slides que referenciam**: 19

### 12. OpenLLMetry
- **URL**: https://github.com/traceloop/openllmetry
- **Resumo**: Instrumentação OpenTelemetry automática para LLMs. Base do Slide 19.
- **Slides que referenciam**: 19

### 13. Eugene Yan — Evaluating LLM Applications
- **URL**: https://eugeneyan.com/writing/evaluating-llm-applications/
- **Resumo**: Blog com práticas de eval. Complementa Hamel Husain.
- **Slides que referenciam**: 29

### 14. Ragas — RAG Assessment
- **URL**: https://docs.ragas.io/
- **Resumo**: Framework de avaliação para RAG. Complementar para casos de RAG agêntico.

### 15. DeepEval
- **URL**: https://github.com/confident-ai/deepeval
- **Resumo**: Framework de eval com métricas prontas e integração com CI. Complementar para a Seção D.

### 16. TruLens
- **URL**: https://www.trulens.org/
- **Resumo**: Observability + eval para LLM apps. Alternativa a Phoenix/Langfuse.

### 17. AgentDojo
- **arXiv**: 2406.13352
- **Resumo**: Benchmark de segurança (injeção em agentes). Prepara ETHAGT13.
- **Slides que referenciam**: 46

---

## Ficha de Pesquisa

- **Arquivo**: `20-Research/ETHAGT12-pesquisa.md`
- **Última consulta**: Julho 2026
- **Revalidação**: Janeiro 2027 (estado da arte em evals evolui rápido)
