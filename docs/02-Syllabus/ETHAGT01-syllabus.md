# `ETHAGT01` — Arquitetura Cognitiva de Agentes LLM

> Especialização em Programação Agêntica · Universidade Etho
> Fase A · Carga 25 h · Versão 1.0 · Última atualização: Julho 2026

## 1. Identificação

| Campo | Valor |
|---|---|
| Código | `ETHAGT01` |
| Título | Arquitetura Cognitiva de Agentes LLM |
| Fase interna | A — Fundamentos Agênticos |
| Fase Etho | Especialização (Fase 4) |
| Carga horária | 25 h |
| Pré-requisitos | `ETHDEV07`, `ETHML01`, Python Intermediário |
| Módulos que dependem deste | `ETHAGT02`, `ETHAGT03`, `ETHAGT04` |

## 2. Objetivos

**Objetivo geral**: Estabelecer o **bloco fundamental** de qualquer sistema agêntico — o *Augmented LLM* em loop — e a distinção crítica entre workflow e agente, capacitando o aluno a raciocinar sobre *arquitetura* antes de adotar qualquer framework.

**Objetivos específicos**:
1. Explicar a transição de "LLM como oráculo" para "LLM como controlador cognitivo".
2. Decompor um agente em Perception · Brain · Planning · Action · Tool Use (taxonomia arXiv:2601.12560).
3. Implementar um agente ReAct **do zero** (sem framework) para dominar o mecanismo.
4. Diferenciar workflows (predefinidos) de agentes (autônomos) e justificar quando usar cada.
5. Adicionar observabilidade mínima (logs estruturados, traces) desde a primeira implementação.
6. Avaliar criticamente 3 frameworks sob a lente dos princípios (não da API).

## 3. Competências desenvolvidas

| Competência | Nível ao final |
|---|---|
| C1 Programação Agêntica | **I** |
| C3 MCP & Tool Use | B |
| C4 Agent Memory | B |
| C5 AgentOps & Avaliação | B |

## 4. Conteúdo programático (ementa)

### Unidade 1 — Do LLM ao Agente (3 h)
- O que muda: de geração única para controle cognitivo de longo prazo
- Definições concorrentes de "agente" e o recuo pragmático de Anthropic (*agentic systems* = workflows + agentes)
- A taxonomia unificada: Perception · Brain · Planning · Action · Tool Use · Collaboration
- Por que agora: o confluência de capacidades (reasoning, tools, context)

### Unidade 2 — O Augmented LLM (5 h)
- O bloco fundamental de Anthropic: LLM + retrieval + tools + memory
- Retrieval in-loop: o modelo gera suas próprias queries
- Tools como extensão de ação; introdução ao tool calling estruturado
- Memory: working memory (context window) vs persistent — panorama
- Interface bem documentada: a regra de ouro

### Unidade 3 — O Agent Loop: ReAct (5 h)
- O padrão fundacional: Thought → Action → Observation em loop
- Por que funciona: força-grounding via observação do ambiente
- Implementação mínima em Python puro (sem SDK)
- Limitações: loops, custo, alucinação em ação
- Variações: ReAct com structured output

### Unidade 4 — Workflows vs Agentes (4 h)
- Distinção canônica de Anthropic
- Os 5 workflows (panorama; aprofundamento em `ETHAGT03`): prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer
- Critério de decisão: previsibilidade (workflow) vs flexibilidade (agente)
- A escalada de complexidade: comece simples, só aumente com evidência

### Unidade 5 — Implementação: do zero vs framework (5 h)
- ReAct em Python puro (revisão da Unidade 3, com tool real)
- Mesmo agente em LangGraph
- Mesmo agente em OpenAI Agents SDK (ou CrewAI/PydanticAI, alternando cohorts)
- Comparação estrutural: o que cada framework abstrai, o que esconde
- Quando reduzir camadas de abstração em produção

### Unidade 6 — Observabilidade desde o dia 1 (3 h)
- Logging estruturado: thought/action/observation com timestamps
- Traces: introdução ao conceito (profundidade em `ETHAGT12`)
- Custo e latência como métricas de primeira classe
- Tooling mínimo: print → structured logs → LangSmith/Phoenix opcional

## 5. Bibliografia

### Fundamental
- Anthropic. *Building Effective Agents*. 2024. (canonical)
- Yao, S. et al. *ReAct: Synergizing Reasoning and Acting in Language Models*. ICLR 2023.
- Arunkumar V, Gangadharan G.R., Buyya R. *Agentic AI: Architectures, Taxonomies, and Evaluation of LLM Agents*. arXiv:2601.12560, 2026.

### Complementar
- Chase, H. *LangGraph* (documentação e exemplos canônicos).
- OpenAI. *Practical Guide to Building Agents*. 2024.
- Schick, T. et al. *Toolformer: Language Models Can Teach Themselves to Use Tools*. NeurIPS 2023.

## 6. Papers e artigos canônicos

- `arXiv:2210.03629` — ReAct (Yao et al., 2022/2023)
- `arXiv:2303.11366` — Reflexion (Shinn et al., 2023) — leitura para contexto de evolução
- `arXiv:2308.00352` — *A Survey on LLM Agents* (Wang et al.) — panorama

## 7. Laboratórios

- **Lab 1** (4 h): "ReAct em 50 linhas". Implementar o agent loop em Python puro chamando uma LLM API, com uma tool de cálculo. Entrega: repo + trace de exemplo.
- **Lab 2** (4 h): "Augmented LLM". Adicionar retrieval (vector store simples) e 2 tools ao agente do Lab 1. Entrega: agente que decide quando recuperar vs usar tool.

## 8. Projeto do módulo

**Descrição**: implementar um agente "research assistant" que, dada uma pergunta factual, decide entre (a) responder direto, (b) recuperar de uma base local, ou (c) usar uma tool de busca. Compare 3 versões: Python puro, LangGraph, e um terceiro framework à escolha.
**Entrega**: repositório + README comparativo + traces.
**Critério de sucesso**: agente funcional nas 3 versões; comparação justifica escolha com base em ao menos 3 critérios (controle, transparência, esforço).

## 9. Exercícios

1. Defina, em suas palavras, a diferença entre workflow e agente (2-3 frases).
2. Dado um trace quebrado, identifique onde o agente entrou em loop e proponha 2 correções.
3. Escreva a descrição de uma tool seguindo princípios ACI (poka-yoke, exemplos).
4. Verdadeiro/falso justificado: "Toda aplicação de LLM deveria ser um agente."
5. Liste 3 trade-offs de custo/latência ao adicionar retrieval em loop.

## 10. Avaliação

| Pilar | Peso | Instrumento |
|---|---|---|
| Técnico | 40% | Prova escrita + projeto comparativo (rubrica) |
| Consultivo | 30% | Apresentação de 10 min justificando a arquitetura escolhida |
| Comportamental | 20% | Code review de um colega |
| Prático | 10% | Demo ao vivo: agente respondendo a 3 perguntas |

**Nota mínima de aprovação**: 3,0.

## 11. Slides

`03-Slides/ETHAGT01-slides.md` — 6 unidades, ~80 slides. Diagramas: augmented LLM, agent loop, workflow-vs-agent.

## 12. Leitura complementar

- Anthropic. *Effective Agents* (YouTube, Erik Schluntz & Alex Albert).
- Karpathy, A. *Software 3.0* (talks).
- HuggingFace Agents Course (para comparação crítica).

## 13. Ferramentas

Python 3.11+ · OpenAI/Anthropic SDK · LangGraph · um framework à escolha (CrewAI/PydanticAI/Agno) · `chromadb` ou `qdrant` (lab 2) · Docker.

## 14. Diagramas

`12-Diagrams/ETHAGT01/` — augmented-llm.mmd · agent-loop.mmd · workflow-vs-agent.mmd · framework-comparison.mmd.

## 15. Estudo de caso

Anthropic Coding Agent no SWE-bench — como o bloco fundamental (Augmented LLM + loop) resolve issues reais. Ver `09-CaseStudies/`.

## 16. Ficha de pesquisa

`20-Research/ETHAGT01-pesquisa.md` — fontes: Anthropic Engineering blog (dez/2024), arXiv:2601.12560 (jan/2026), LangGraph repo (examples/react-agent-from-scratch.ipynb). Última consulta: Julho 2026.

---

*Mantido por: Escola de Tecnologia — Universidade Etho · Versão 1.0 · Julho 2026*
