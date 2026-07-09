---
password: Etho-Prof-2026
---
# Missão, Visão e Princípios

## Missão

Formar **arquitetos de sistemas de agentes autônomos** capazes de projetar, construir, avaliar e operar plataformas completas de Agentic AI em produção — superando em profundidade e rigor as formações disponíveis no mercado.

## Visão

Ser a referência em **Programação Agêntica** na Universidade Etho e a formação mais completa disponível em língua portuguesa, ancorada no estado da arte internacional (arXiv, Anthropic, OpenAI, principais repositórios open source) e alinhada ao modelo de competências e avaliações da Etho.

## Princípios pedagógicos

### 1. Aprender Fazendo
Todo conceito é acompanhado de laboratório guiado e projeto aplicado. Não há módulo exclusivamente teórico. A avaliação prática (Pilar Prático, 10%) valida a tradução teoria → execução.

### 2. Arquitetura primeiro, framework depois
O bloco fundamental é o **Augmented LLM em loop** (Anthropic), não um SDK. Frameworks (LangGraph, OpenAI Agents SDK, CrewAI, AutoGen, etc.) são estudados como **instanciações** de princípios — nunca como fim em si mesmos. Isso garante que o conhecimento permaneça válido quando os frameworks mudarem.

### 3. Rastreabilidade competência → módulo → avaliação
Cada módulo declara quais competências desenvolve e quais itens da avaliação as medem. Nenhum conteúdo é órfão. Ver [`01-Curriculum/mapa-competencias-modulos.md`](../01-Curriculum/mapa-competencias-modulos.md).

### 4. Pesquisa viva (evidence-based)
Conteúdo ancorado em fontes canônicas com data e citação. Cada módulo mantém ficha de pesquisa em `20-Research/`. **Não se produz conteúdo apenas de memória** quando há fonte consultável via MCPs (web-search, web-reader, github, zread).

### 5. Equilíbrio + fronteira
Cobertura equilibrada das dimensões (fundamentos → produção), com **ênfase deliberada em multi-agentes e pesquisa autônoma** — a fronteira do estado da arte, onde está a diferenciação.

### 6. Simplicidade, transparência, ACI
Adoção dos três princípios de Anthropic para agentes: manter designs simples, expor explicitamente os passos de planejamento, investir na **Agent-Computer Interface** tanto quanto em HCI.

## Princípios arquiteturais

| Princípio | Aplicação na Especialização |
|---|---|
| **Comece simples, aumente complexidade só com evidência** | Ordem pedagógica: workflows → agentes → multi-agentes → sociedades |
| **Workflows para previsibilidade, agentes para flexibilidade** | Critério de decisão ensinado em `ETHAGT03` e reafirmado no Capstone |
| **Ground truth a cada passo** | Agentes obtêm feedback do ambiente; módulos exigem execução real |
| **Sandboxing + guardrails** | Segurança (`ETHAGT13`) é pré-requisito de produção, não apêndice |
| **Custo e latência são cidadãos de primeira classe** | `ETHAGT14` e FinOps de agentes integrados ao currículo |
| **Observabilidade desde o dia 1** | Traces e eval introduzidos em `ETHAGT01` e aprofundados em `ETHAGT12` |

## Não-objetivos (explícitos)

- **Não** formar "prompt engineers". Prompt engineering é pré-requisito, não destino.
- **Não** certificar em um framework específico. Frameworks entram e saem; princípios permanecem.
- **Não** cobrir ML/DL fundamental. Isso é `ETHML01/02`.
- **Não** substituir o Tronco Comum. Esta é uma trilha de **Especialização** que se apoia nele.

## Público-alvo detalhado

| Persona | Maturidade de entrada | Expectativa de saída |
|---|---|---|
| Engenheiro de Software sênior | Python sólido, sem agentes | Arquiteto de plataformas agênticas |
| Arquiteto de Software | Sistemas distribuídos, sem LLM | Arquiteto de sistemas multi-agente |
| Cientista de Dados | ML/RAG, sem engenharia de agentes | Engenheiro de agentes de produção |
| Engenheiro de IA | LLM APIs, sem arquitetura | Arquiteto de sistemas autônomos |
| Pesquisador | Teórico, sem engenharia | Prototipador de sistemas de pesquisa autônoma |

## Indicadores de sucesso da Especialização

- ≥ 80% dos alunos certificados com nota ≥ 4,0
- Capstone avaliado como "pronto para produção" por painel de especialistas
- NPS da formação ≥ 9,0
- Adoção interna: ≥ 30% dos times de IA com ao menos 1 certificado em 24 meses
- Contribuições de volta ao repositório (pull requests de exemplos, patterns)

---

*Relacionado: [`roadmap.md`](roadmap.md) · [`adr/ADR-001`](adr/ADR-001-fundacoes-especializacao.md)*
