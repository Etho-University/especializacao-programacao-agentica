# ETHAGT12 — AgentOps, Observabilidade & Avaliação — Slides

> Apresentação para aula síncrona · ~50 min · 14 slides

## Estrutura da aula
- Abertura (5 min): gancho/motivação
- Teoria (25 min): conceitos principais com diagramas de referência
- Demonstração (10 min): código ao vivo ou walkthrough de lab
- Exercício (5 min): questão rápida ou discussão
- Fechamento (5 min): conexão com próximo módulo, leitura recomendada

## Slides

### Slide 1 — Título
- ETHAGT12 — AgentOps, Observabilidade & Avaliação (LLMOps para agentes)
- Professor, data, Universität Etho
- Pré-requisito: ETHAGT11
- ~1 min

### Slide 2 — Agenda
1. Por que agentes são difíceis de avaliar
2. Observabilidade (traces, spans, OpenTelemetry)
3. Avaliação automatizada (LLM-as-judge, golden cases)
4. Benchmarks canônicos (SWE-bench, GAIA, τ-bench)
5. Ciclo de melhoria contínua
6. Reportando resultados (eval report)
- ~1 min

### Slide 3 — Gancho / Motivação
- Problema: "parece que funciona" não é medida — agente não-determinístico falha em casos que você não testou
- Exemplo: agente funcionou 5/5 no teste manual, mas em produção acertou 30% — sem métrica, você não sabia
- A solução: observabilidade + avaliação automatizada + benchmarks
- Pergunta: *Como você sabe se seu agente está ficando melhor ou pior?*
- ~3 min

### Slide 4 — Por que Agentes São Difíceis de Avaliar
- Não-determinismo: mesma pergunta pode dar respostas diferentes
- Dependência de ambiente: tools podem falhar, APIs mudar
- Custo de runs: cada avaliação custa tokens
- Falácias comuns: "funcionou uma vez", "parece bom", "o usuário não reclamou"
- Avaliação contínua vs pontual
- ~3 min

### Slide 5 — Observabilidade
- Traces: grafo completo de chamadas (LLM, tools, retrieval)
- Spans: cada operação individual com timing
- OpenTelemetry para LLMs (GenAI semantic conventions)
- Tooling: LangSmith, Phoenix (Arize), Langfuse, OpenLLMetry
- Logs estruturados vs traces (complementares)
- Custo de observabilidade (amostragem)
- Diagrama: `12-Diagrams/ETHAGT12/trace-anatomy.mmd`
- ~5 min

### Slide 6 — DEMO: Traces Everywhere
- Código ao vivo: adicionar LangSmith (ou Phoenix) a um agente existente
- Mostrar trace completo: pergunta → thought → tool call → observation → response
- Dashboard: latência, custo por step, erros
- Identificar gargalo no trace (tool calls lentas)
- Referência: `05-Labs/ETHAGT12/Lab1-Traces-Everywhere`
- ~5 min

### Slide 7 — Avaliação Automatizada
- LLM-as-judge: quando confiável? Vieses (positional, sycophancy, verbosity)
- Mitigações: rubrica clara, exemplos, múltiplos judges, calibração
- Golden cases: pares (pergunta, resposta esperada, critério)
- Conjuntos de regressão: toda mudança de prompt/tool roda N casos
- Métricas de tarefa: success rate, partial credit
- Métricas de processo: steps, loops, tool misuse rate
- ~4 min

### Slide 8 — Benchmarks Canônicos
- **SWE-bench / SWE-bench Verified**: resolução de issues de GitHub
- **GAIA**: raciocínio geral multi-step com tools
- **τ-bench**: tool use em domínios (airline, retail)
- **AgentBench**: panorama de capacidades
- **WebArena / VisualWebArena**: navegação web autônoma
- Como rodar localmente, limites, contaminação
- Diagrama: `12-Diagrams/ETHAGT12/benchmark-landscape.mmd`
- Pergunta: *Um score alto em SWE-bench garante bom desempenho em produção de código?*
- ~4 min

### Slide 9 — Ciclo de Melhoria Contínua
- Dataset crescente: cada execução em produção pode gerar caso de teste
- CI para agentes: testes de regressão a cada mudança (prompt, tool, modelo)
- Shadow runs: nova versão roda em paralelo sem afetar usuário
- Canary: 5% → 25% → 100%
- Feedback humano estruturado (thumbs up/down com contexto)
- ~3 min

### Slide 10 — Reportando Resultados
- Eval report: template em `24-Templates/template-eval-report.md`
- Análise de falhas: categorização (não entendeu, tool errada, alucinação, loop)
- Comparações honestas: vs baseline, vs versão anterior, vs humano
- Comunicação para stakeholders: métricas que importam para negócio
- Pergunta: *O que é mais importante reportar para o CEO — accuracy ou custo por execução?*
- ~4 min

### Slide 11 — Exercício: Detectando Regressão
- Cenário: time mudou o prompt do agente e o eval score caiu de 85% para 72%
- Em grupos: analisar causas possíveis (vies do judge? mudança no comportamento?)
- Propor: golden cases, A/B test, análise de falhas
- 3 min discussão, 2 min compartilhar
- ~5 min

### Slide 12 — Conexão com Próximo Módulo
- ETHAGT13 — Segurança & Governança: observabilidade como defesa
- ETHAGT90 — Capstone: eval report completo
- Leitura: Jimenez et al. *SWE-bench* (arXiv:2310.06770)
- Mialon et al. *GAIA* (arXiv:2311.12983)
- Yao et al. *τ-bench* (arXiv:2404.44529)
- ~2 min

### Slide 13 — Referências
- Jimenez, C. *SWE-bench* (arXiv:2310.06770)
- Mialon, G. *GAIA* (arXiv:2311.12983)
- Yao, S. *τ-bench* (arXiv:2404.44529)
- Liu, X. *AgentBench* (arXiv:2308.03688)
- Zhou, S. *WebArena* (arXiv:2307.13854)
- LangSmith / Phoenix / Langfuse docs
- ~1 min
