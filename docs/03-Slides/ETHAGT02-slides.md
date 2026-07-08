# ETHAGT02 — Tool Calling e Agent-Computer Interface (ACI) — Slides

> Apresentação para aula síncrona · ~50 min · 13 slides

## Estrutura da aula
- Abertura (5 min): gancho/motivação
- Teoria (25 min): conceitos principais com diagramas de referência
- Demonstração (10 min): código ao vivo ou walkthrough de lab
- Exercício (5 min): questão rápida ou discussão
- Fechamento (5 min): conexão com próximo módulo, leitura recomendada

## Slides

### Slide 1 — Título
- ETHAGT02 — Tool Calling e Agent-Computer Interface (ACI)
- Professor, data, Universität Etho
- Pré-requisito: ETHAGT01
- ~1 min

### Slide 2 — Agenda
1. Mecanismo do tool calling
2. ACI como disciplina de design
3. Engenharia de tools (schemas, idempotência, erros)
4. Tools perigosas e HITL
5. Erros comuns e correções
6. Avaliando tools
- ~1 min

### Slide 3 — Gancho / Motivação
- Problema: tools mal desenhadas fazem o agente falhar silenciosamente
- Exemplo real (Anthropic): paths relativos em vez de absolutos — agente escreve no lugar errado
- Pergunta: *O que acontece quando uma tool devolve erro não tratado?*
- A solução: tratar ACI com o mesmo rigor de HCI
- ~3 min

### Slide 4 — O Mecanismo do Tool Calling
- Function calling: do prompt para JSON estruturado
- JSON Schema como contrato entre LLM e sistema
- Structured outputs / constrained decoding (visão geral)
- Multi-tool calls em uma resposta; paralelismo
- Custo: tokens de descrição vs benefício
- Pergunta técnica: *Quantos tokens "custam" 5 tools bem descritas?*
- ~4 min

### Slide 5 — ACI como Disciplina
- Analogia de Anthropic: invista em ACI tanto quanto em HCI
- Princípios: "pôr-se no lugar do modelo"; descrições ricas
- Exemplos, edge cases, requisitos de formato, fronteiras entre tools
- Formato próximo ao natural (sem escaping desnecessário)
- "Pense em tokens antes de escrever": dar espaço para pensar
- Exercício interativo: *Leia esta descrição de tool — o que está faltando?*
- ~4 min

### Slide 6 — DEMO: Refatorando Tools
- Código ao vivo: 5 tools mal desenhadas → aplicar princípios ACI
- Antes: descrição vaga, schema frouxo, sem tratamento de erro
- Depois: descrição rica com exemplos, enum/patterns, timeouts
- Referência: `05-Labs/ETHAGT02/Lab1-Refatorando-Tools`
- Medir melhoria: taxa de uso correto em 20 casos (workbench)
- ~5 min

### Slide 7 — Engenharia de Tools
- Schemas claros (Pydantic, TypedDict, Zod)
- Idempotência e onde ela importa (cobrança, email, DB writes)
- Timeouts, retries, fallbacks
- Tipologia: leitura / escrita / destrutiva / external-side-effect
- Versionamento de tools sem quebrar agentes em produção
- Diagrama: `12-Diagrams/ETHAGT02/aci-iteration-loop.mmd`
- Pergunta: *Quando é melhor ter 1 tool com parâmetro `mode` vs 2 tools separadas?*
- ~4 min

### Slide 8 — Matriz de Risco e HITL
- Matriz: irreversível × impactante
- HITL obrigatório para ações destrutivas (delete, deploy, transfer, email)
- Confirmação explícita, dry-run, simulação
- Allowlists vs dinâmico
- Diagrama: `12-Diagrams/ETHAGT02/risk-matrix.mmd`
- Diagrama: `12-Diagrams/ETHAGT02/hitl-flow.mmd`
- ~4 min

### Slide 9 — Erros Comuns e Correções
1. Paths relativos → absolutos (caso real Anthropic SWE-bench)
2. Muitas tools similares → consolidar ou renomear
3. Descrições vagas → reescrever como docstring de dev júnior
4. Schema frouxo → apertar com enum/patterns
5. Falta de erro tratado → propagar com mensagem útil ao modelo
- Discussão: *Qual desses erros você já cometeu (ou viu acontecer)?*
- ~3 min

### Slide 10 — Avaliando Tools
- Workbench: rodar N inputs, observar erros, iterar
- Métricas: taxa de uso correto, custo por chamada, latência
- Conjunto de testes de regressão para tools
- Exemplo de workbench mínimo em Python
- ~3 min

### Slide 11 — Exercício: Anti-patterns em Schema
- Entregar um JSON Schema de tool mal projetado (ex: `"type": "object"` sem propriedades)
- Em trios: identificar 3 anti-patterns e reescrever
- 3 min discussão, 1 min compartilhar
- ~4 min

### Slide 12 — Conexão com Próximos Módulos
- ETHAGT08 — MCP: aprofunda tool use como padrão de servidor
- ETHAGT13 — Segurança: tools como vetor de ataque
- Leitura: Anthropic *Building Effective Agents* Appendix 2
- Paper: Gorilla (arXiv:2305.17126) — LLM com 1700+ APIs
- ~2 min

### Slide 13 — Referências
- Anthropic. *Building Effective Agents*, Appendix 2: "Prompt engineering your tools"
- OpenAI. *Function Calling Guide* e *Structured Outputs*
- Pydantic AI documentation
- Anthropic Engineering Blog — tool use series
- ~1 min
