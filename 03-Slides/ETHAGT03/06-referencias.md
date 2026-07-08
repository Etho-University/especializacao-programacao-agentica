# ETHAGT03 — Referências

> Todas as fontes utilizadas na preparação e apresentação da aula.

---

## Canônicas (fundação do curso)

### 1. Anthropic — Building Effective Agents
- **Autores**: Erik Schluntz, Barry Zhang
- **Data**: dezembro 2024
- **URL**: https://www.anthropic.com/engineering/building-effective-agents
- **Resumo**: Estabelece os 5 workflows canônicos (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer) com exemplos práticos. Base direta de toda a aula.
- **Importância**: Canônica
- **Slides que referenciam**: 7, 8, 9, 10, 12, 19, 25, 26, 36, 41, 48, 54

### 2. Agentic AI: Architectures, Taxonomies, and Evaluation of LLM Agents
- **Autores**: Arunkumar V, Gangadharan G.R., Rajkumar Buyya
- **Data**: janeiro 2026
- **arXiv**: 2601.12560
- **Resumo**: Survey que contextualiza workflows vs agentes na taxonomia unificada. Serve de ponte entre ETHAGT01 (taxonomia) e ETHAGT03 (workflows).
- **Importância**: Canônica
- **Slides que referenciam**: 7, 8, 49

---

## Importantes (complementam e aprofundam)

### 3. Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models
- **Autores**: Lei Wang et al.
- **arXiv**: 2305.17126 (maio 2023)
- **Resumo**: Decompõe raciocínio em planejar + executar. Base teórica para orchestrator-workers: a separação de planejamento (decompositor) e execução (workers) melhora qualidade.
- **Importância**: Importante
- **Slides que referenciam**: 36, 62

### 4. ReWOO: Decoupling Reasoning from Tool Use for Parameter-Efficient LLM-Based Tool Use
- **Autores**: Binfeng Xu et al.
- **arXiv**: 2305.18323 (maio 2023)
- **Resumo**: Plano "cego" + paralelismo de evidências. Variação eficiente de orchestrator-workers: o plano é gerado sem reagir a resultados intermediários, permitindo paralelismo total.
- **Importância**: Importante
- **Slides que referenciam**: 36, 62

### 5. LLMCompiler: An LLM Compiler for Parallel Function Calling
- **Autores**: Mingyang Chen et al.
- **arXiv**: 2312.04511 (dezembro 2023)
- **Resumo**: Paralelização estruturada de chamadas LLM. Aprofunda parallelization ao formalizar o "fan-out" de tarefas independentes com um "planner" que gera o DAG de execução.
- **Importância**: Importante
- **Slides que referenciam**: 36, 62

### 6. Anthropic — Effective Context Engineering for AI Agents
- **Data**: 2025
- **URL**: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- **Resumo**: Aprofundamento sobre context engineering. Relevante para routing (contexto focado por path) e evaluator-optimizer (rubrics como contexto estruturado).
- **Importância**: Importante
- **Slides que referenciam**: 20, 43

---

## Complementares (leitura opcional)

### 7. Towards AI — Agent Workflow Patterns: Beyond Anthropic's Playbook
- **Data**: 2025
- **Resumo**: Extensão crítica dos 5 padrões com variações e novos padrões.
- **Slides que referenciam**: 49

### 8. LangGraph Examples
- **URL**: https://github.com/langchain-ai/langgraph
- **Resumo**: Implementações de referência: `plan-and-execute.ipynb`, `llm-compiler/LLMCompiler.ipynb`, `multi_agent/hierarchical_agent_teams.ipynb`.
- **Slides que referenciam**: 36, 38, 61

### 9. Schluntz & Albert — Building more effective AI agents (YouTube)
- **URL**: https://www.youtube.com/watch?v=D7_ipDqhtwk
- **Resumo**: Apresentação ao vivo no AI Engineer Summit 2025. Schluntz (co-autor do post canônico) fala sobre os workflows em produção.
- **Slides que referenciam**: 53, 62

### 10. Pat McGuinness Substack — Série sobre Workflows
- **Resumo**: Análises práticas de padrões de workflow em produção.
- **Slides que referenciam**: 50

### 11. Coinbase / Intercom / Thomson Reuters — Case Studies (Anthropic)
- **Resumo**: Casos citados por Anthropic de workflows agênticos em suporte ao cliente.
- **Slides que referenciam**: 53

### 12. ReAct: Synergizing Reasoning and Acting in Language Models
- **Autores**: Shunyu Yao et al.
- **Venue**: ICLR 2023
- **arXiv**: 2210.03629
- **Resumo**: Referenciado para contraste — evaluator-optimizer (gerar-avaliar-refinar) vs ReAct (pensar-agir-observar).
- **Importância**: Canônica (do ETHAGT01)
- **Slides que referenciam**: 41

---

## Ficha de Pesquisa

- **Arquivo**: `20-Research/ETHAGT03-pesquisa.md`
- **Última consulta**: Julho 2026
- **Revalidação**: Janeiro 2027 (estado da arte evolui rápido)
