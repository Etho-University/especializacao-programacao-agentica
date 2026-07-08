# ETHAGT14 — Referências

> Todas as fontes utilizadas na preparação e apresentação da aula.

---

## Canônicas (fundação do curso)

### 1. Kleppmann, M. — Designing Data-Intensive Applications
- **Autor**: Martin Kleppmann
- **Editora**: O'Reilly Media
- **Edição**: 1ª (2017)
- **Resumo**: Bíblia de sistemas distribuídos. Capítulos essenciais: 5 (Replication), 6 (Partitioning/Sharding), 9 (Consistency and Consensus). Base direta das Seções E (Distribuição) e F (Infraestrutura).
- **Importância**: Canônica
- **Slides que referenciam**: 11, 42, 43, 44, 45, 50, 52, 74

### 2. Richards, M. & Ford, N. — Fundamentals of Software Architecture
- **Autores**: Mark Richards, Neal Ford
- **Editora**: O'Reilly Media
- **Edição**: 1ª (2020)
- **Resumo**: Fundamentos de arquitetura de software. Útil para entender trade-offs arquiteturais (stateless vs stateful, monólito vs distribuído). Complementa Kleppmann com perspectiva de arquiteto.
- **Importância**: Canônica
- **Slides que referenciam**: 41, 45, 50, 74

### 3. FinOps Foundation — FinOps for ML/AI
- **Autor**: FinOps Foundation
- **URL**: https://finops.org
- **Resumo**: Framework FinOps aplicado a ML/AI. Orçamento, medição, otimização. Base direta da Seção G (FinOps de Agentes).
- **Importância**: Canônica
- **Slides que referenciam**: 55, 56, 58, 59, 60, 61, 74

---

## Importantes (complementam e aprofundam)

### 4. Leviathan et al. — Fast Inference from Transformers via Speculative Decoding
- **Autores**: Yaniv Leviathan, Matan Kalman, Yossi Matias
- **Venue**: arXiv, 2023
- **arXiv**: 2211.17192
- **Resumo**: Introduz speculative decoding (draft model + target model). Base do Slide 33.
- **Importância**: Importante
- **Slides que referenciam**: 33, 74

### 5. vLLM Documentation
- **URL**: https://docs.vllm.ai
- **Resumo**: Servidor de inferência otimizado (PagedAttention, continuous batching). Referência para inferência local e serving de LLMs.
- **Importância**: Importante
- **Slides que referenciam**: 33, 52, 74

### 6. Anthropic — Prompt Caching
- **URL**: https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching
- **Resumo**: Cache de prefixo no provider-side. Reduz custo de system prompts repetidos. Base do Slide 17 e 25.
- **Importância**: Importante
- **Slides que referenciam**: 17, 25

### 7. OpenAI — Prompt Caching
- **URL**: https://platform.openai.com/docs/guides/prompt-caching
- **Resumo**: Implementação OpenAI de cache de prompt. Complementa Anthropic.
- **Importância**: Importante
- **Slides que referenciam**: 17, 25

### 8. LiteLLM Documentation
- **URL**: https://docs.litellm.ai
- **Resumo**: Biblioteca de roteamento de LLMs multi-provider. Suporta routing, fallback, rate limit handling, custo tracking. Base do Slide 31 e 74.
- **Importância**: Importante
- **Slides que referenciam**: 31, 56, 74

### 9. Kubernetes — Horizontal Pod Autoscaler
- **URL**: https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/
- **Resumo**: Documentação oficial de HPA. Base do Slide 46 e 50.
- **Importância**: Importante
- **Slides que referenciam**: 46, 50

### 10. KEDA — Kubernetes Event-Driven Autoscaling
- **URL**: https://keda.sh
- **Resumo**: Autoscaling baseado em eventos (fila, métricas custom). Complementa HPA com escala por métricas de negócio.
- **Importância**: Importante
- **Slides que referenciam**: 46

---

## Complementares (leitura opcional)

### 11. Cloud Provider Docs — Anthropic, OpenAI, Bedrock, Vertex
- **Anthropic**: https://docs.anthropic.com
- **OpenAI**: https://platform.openai.com/docs
- **AWS Bedrock**: https://aws.amazon.com/bedrock
- **Google Vertex**: https://cloud.google.com/vertex-ai
- **Resumo**: Rate limits, pricing, capabilities. Referência contínua para todas as decisões de routing e custo.
- **Slides que referenciam**: 9, 10, 30A, 31, 52

### 12. Redis Documentation — Vector Search
- **URL**: https://redis.io/docs/interact/search-and-query/query/vector-search/
- **Resumo**: Redis como vector store para cache semântico. Base do Lab 1.
- **Importância**: Complementar
- **Slides que referenciam**: 19, 26

### 13. Istio / Linkerd (Service Mesh)
- **Istio**: https://istio.io
- **Linkerd**: https://linkerd.io
- **Resumo**: Service mesh para comunicação entre agentes. mTLS, retries, circuit breakers, observabilidade distribuída.
- **Importância**: Complementar
- **Slides que referenciam**: 52

### 14. OpenTelemetry
- **URL**: https://opentelemetry.io
- **Resumo**: Padrão de observabilidade (traces, metrics, logs). Base de dashboards FinOps.
- **Importância**: Complementar
- **Slides que referenciam**: 59

### 15. Grafana
- **URL**: https://grafana.com
- **Resumo**: Visualização de métricas e dashboards. Mockup no Slide 59.
- **Importância**: Complementar
- **Slides que referenciam**: 59

### 16. Datadog / LangSmith / Helicone (Observabilidade de LLM)
- **Datadog**: https://www.datadoghq.com
- **LangSmith**: https://smith.langchain.com
- **Helicone**: https://helicone.ai
- **Resumo**: Plataformas de observabilidade específicas para LLM. Custo tracking, traces, eval.
- **Importância**: Complementar
- **Slides que referenciam**: 53, 59

---

## Papers Adicionais (avançado)

### 17. Chen et al. — Accelerating Large Language Model Decoding with Speculative Sampling
- **Venue**: arXiv, 2023
- **arXiv**: 2302.01318
- **Resumo**: Variante de speculative decoding (DeepMind). Complementa o paper 4.

### 18. Hinton et al. — Distilling the Knowledge in a Neural Network
- **Venue**: arXiv, 2015
- **arXiv**: 1503.02531
- **Resumo**: Paper fundacional de knowledge distillation. Base conceitual do Slide 35.

---

## Ficha de Pesquisa

- **Arquivo**: `20-Research/ETHAGT14-pesquisa.md`
- **Última consulta**: Julho 2026
- **Revalidação**: Janeiro 2027 (pricing e capabilities de LLM evoluem rápido)
