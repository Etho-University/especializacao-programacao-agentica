# ETHAGT15 — Referências

> Todas as fontes utilizadas na preparação e apresentação da aula.

---

## Canônicas (fundação do módulo)

### 1. DSPy: Compiling Declarative LLM Calls into Self-Improving Pipelines
- **Autores**: Omar Khattab, Arnav Singhvi, Maithili Patel, et al.
- **Venue**: arXiv preprint (2024)
- **arXiv**: 2310.03714
- **Resumo**: Introduz a compilação declarativa de chamadas de LLM. Você escreve assinaturas (`question -> answer`), o DSPy compila em prompts otimizados via teleprompters (BootstrapFewShot, MIPRO). Fundamento direto da Seção D (otimização automatizada).
- **Importância**: Canônica
- **Slides que referenciam**: 6, 11, 27, 28, 59, 66

### 2. Voyager: An Open-Ended Embodied Agent with Large Language Models
- **Autores**: Guanzhi Wang, Yuqi Xie, Yunfan Jiang, et al. (NVIDIA)
- **Venue**: arXiv preprint (2023)
- **arXiv**: 2305.16291
- **Resumo**: Agente que aprende skills no Minecraft autonomamente via automatic curriculum, skill library (código JS executável) e iterative prompting. Caso canônico de auto-aprendizado em ambiente fechado. Base dos Slides 40 e 55.
- **Importância**: Canônica
- **Slides que referenciam**: 6, 11, 40, 55, 59, 66

### 3. Promptbreeder: Self-Referential Self-Improvement via Prompt Evolution
- **Autores**: Chris Fernando, Dylan Banarse, Henry Goh, et al. (DeepMind)
- **Venue**: arXiv preprint (2023)
- **arXiv**: 2309.16797
- **Resumo**: Aplica algoritmos genéticos para evoluir populações de prompts. Mutação guiada por LLM + seleção por eval. Gerações sucessivas melhoram os prompts. Fundamento do Slide 29.
- **Importância**: Canônica
- **Slides que referenciam**: 11, 29, 59, 66

### 4. AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery
- **Autores**: Chris Lu, Lianghua Liu, Stanislas Polu, et al. (Sakana AI)
- **Venue**: arXiv preprint (2024)
- **arXiv**: 2408.06292
- **Resumo**: Sistema que conduz pesquisa científica end-to-end — ideação, experimentação, escrita de paper — autonomamente. Caso extremo de meta-agência aplicada a pesquisa.
- **Importância**: Canônica
- **Slides que referenciam**: 6, 11, 66

---

## Importantes (complementam e aprofundam)

### 5. Meta-Prompting: Enhancing Language Models with Task-Agnostic Scaffolding
- **Autores**: Sukolsak Sakshuwong, et al.; primary: Hu, S.
- **Venue**: arXiv preprint (2024)
- **arXiv**: 2311.11402
- **Resumo**: Meta-agente que decompora tarefas chamando especialistas LLM. Abordagem de meta-agência via composição de especialistas.
- **Importância**: Importante
- **Slides que referenciam**: 6, 11, 66

### 6. Generative Agents: Interactive Simulacra of Human Behavior
- **Autores**: Joon Sung Park, Joseph O'Brien, Carrie J. Cai, et al.
- **Venue**: UIST 2023
- **arXiv**: 2304.03442
- **Resumo**: Agentes com memória, reflexão e planejamento que simulam comportamento humano. Contexto para auto-aprendizado e memória acumulada.
- **Importância**: Importante
- **Slides que referenciam**: 37, 38

### 7. Reflexion: Language Agents with Verbal Reinforcement Learning
- **Autores**: Noah Shinn, Federico Cassano, Edward Berman, et al.
- **Venue**: NeurIPS 2023
- **arXiv**: 2303.11366
- **Resumo**: Adiciona auto-crítica e memória de falhas ao loop de agentes. Referência para reflexão individual e sistêmica.
- **Importância**: Importante
- **Slides que referenciam**: 38

### 8. Anthropic — Constitutional AI
- **Autores**: Anthropic
- **Resumo**: Governança de auto-modificação via princípios constitucionais. Referência para meta-governor e vetos.
- **Importância**: Importante
- **Slides que referenciam**: 49, 52

---

## Complementares (leitura opcional)

### 9. Atlas Prompt Optimization
- **Resumo**: Otimização guiada por árvore de pensamentos. Alternativa a DSPy e Promptbreeder.
- **Slides que referenciam**: 30

### 10. OPRO (Optimization by PROmpting) — Google
- **Autores**: Chengrun Yang, et al. (Google DeepMind)
- **arXiv**: 2309.03409
- **Resumo**: Otimização de prompts via meta-prompting. Um LLM gera candidatos baseado em exemplos.
- **Slides que referenciam**: 30

### 11. TextGrad: Automatic "Differentiation" via Text
- **Resumo**: Aplica ideia de gradientes ao texto — retropropaga feedback textual através de pipelines de LLM.
- **Slides que referenciam**: 30

### 12. LangGraph Documentation
- **URL**: https://github.com/langchain-ai/langgraph
- **Resumo**: Exemplos de meta-agentes e orquestração. Útil para o projeto do módulo.
- **Slides que referenciam**: projeto

### 13. Open Policy Agent (OPA) / Rego
- **URL**: https://www.openpolicyagent.org/
- **Resumo**: Engine de policy-as-code para implementar vetos determinísticos no meta-governor.
- **Slides que referenciam**: 52

### 14. CEL (Common Expression Language)
- **Resumo**: Alternativa a Rego para policy-as-code. Usado em Kubernetes e Istio.
- **Slides que referenciam**: 52

---

## Ficha de Pesquisa

- **Arquivo**: `20-Research/ETHAGT15-pesquisa.md`
- **Última consulta**: Julho 2026
- **Revalidação**: Janeiro 2027 (estado da arte evolui rápido)
