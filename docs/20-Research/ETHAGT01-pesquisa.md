# ETHAGT01 — Ficha de pesquisa

> Fontes consultadas para produzir o material deste módulo. Convenção: fonte · autor · data · URL · resumo · importância (canônico / importante / complementar).

## Canônicas (fundação do curso)

### Anthropic — Building Effective Agents
- **Autores**: Erik Schluntz, Barry Zhang
- **Data**: dezembro 2024
- **URL**: <https://www.anthropic.com/engineering/building-effective-agents>
- **Resumo**: Estabelece Augmented LLM como bloco fundamental; 5 workflows; distinção workflow/agente; 3 princípios (simplicidade, transparência, ACI). Base direta dos capítulos 2, 3, 4 e 6 da apostila.
- **Importância**: 🏛 Canônica

### ReAct: Synergizing Reasoning and Acting in Language Models
- **Autores**: Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Shafran Narang, Karpathy, Cui, Chen
- **Venue**: ICLR 2023 · arXiv:2210.03629
- **Resumo**: Introduz o padrão Thought/Action/Observation em loop. Fundamento direto do Capítulo 3 (agent loop).
- **Importância**: 🏛 Canônica

### Agentic AI: Architectures, Taxonomies, and Evaluation of LLM Agents
- **Autores**: Arunkumar V, Gangadharan G.R., Rajkumar Buyya
- **Data**: janeiro 2026 · arXiv:2601.12560
- **Resumo**: Survey com taxonomia unificada (Perception, Brain, Planning, Action, Tool Use, Collaboration); mapeia transição CoT → inference-time reasoning e APIs fixas → MCP. Base do Capítulo 1.
- **Importância**: 🏛 Canônica

## Importantes (complementam e aprofundam)

### Toolformer: Language Models Can Teach Themselves to Use Tools
- **Autores**: Tim Schick et al.
- **Venue**: NeurIPS 2023 · arXiv:2302.04761
- **Resumo**: Mostra que LLMs podem aprender a usar tools com treino. Contexto histórico para tool calling moderno.
- **Importância**: Importante

### Reflexion: Language Agents with Verbal Reinforcement Learning
- **Autores**: Noah Shinn et al.
- **Venue**: NeurIPS 2023 · arXiv:2303.11366
- **Resumo**: Adiciona auto-crítica e memória de falhas ao loop. Referência para evolução (aprofundado em ETHAGT04).
- **Importância**: Importante

### A Survey on Large Language Model based Autonomous Agents
- **Autores**: Lei Wang et al.
- **arXiv**: 2308.11432
- **Resumo**: Panorama acadêmico de arquiteturas de agentes. Leitura de comparação.
- **Importância**: Importante

### SWE-bench: Can Language Models Resolve Real-World GitHub Issues?
- **Autores**: Carlos Jimenez et al.
- **arXiv**: 2310.06770
- **Resumo**: Benchmark que fundamenta o caso de estudo (Anthropic coding agent).
- **Importância**: Importante

## Complementares (leitura opcional)

- **LangGraph examples** — `examples/react-agent-from-scratch.ipynb` · implementação de referência do agente ReAct em LangGraph. Base do Lab 1 (versão comparativa). URL: <https://github.com/langchain-ai/langgraph>
- **OpenAI — Practical Guide to Building Agents** (2024) · visão pragmática de um provedor.
- **Karpathy, A. — Software 3.0** (talks) · reflexão sobre paradigma; útil para contexte.
- **HuggingFace Agents Course** · para comparação crítica de abordagem.

## Última consulta

Julho 2026. Revalidar a cada 6 meses (estado da arte evolui rápido).
