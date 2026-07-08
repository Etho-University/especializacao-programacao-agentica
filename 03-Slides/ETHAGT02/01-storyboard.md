# ETHAGT02 — Tool Calling e Agent-Computer Interface (ACI)
## Storyboard da Apresentação

> **Universidade Etho · Especialização em Programação Agêntica**
> Fase A — Fundamentos Agênticos · 25 h
> Storyboard v1.0 · Julho 2026

---

## Metadados da Apresentação

| Campo | Valor |
|---|---|
| Código | ETHAGT02 |
| Título | Tool Calling e Agent-Computer Interface (ACI) |
| Duração estimada | 90 min (2 blocos de 45 min) |
| Total de slides | 60 |
| Público | Arquitetos, Engenheiros de Software, Engenheiros de IA, Cientistas de Dados, Tech Leads |
| Pré-requisitos | ETHAGT01 |
| Competências | C1 (I), C3 (I), C5 (B), C6 (B) |
| PPTX gerado | `03-Slides/ETHAGT02/ETHAGT02-Apresentacao.pptx` |

---

## Mapa Visual da Apresentação

```
BLOCO 1 (45 min)                              BLOCO 2 (45 min)
┌──────────────────────────────┐              ┌──────────────────────────────┐
│ SEÇÃO A — Abertura (8 min)   │              │ SEÇÃO D — Eng. de Tools (12m)│
│  Capa · Objetivos · Agenda   │              │  Schemas · Idempotência      │
│  Motivação · Contexto ACI    │              │  Timeouts · Tipologia · Vers.│
├──────────────────────────────┤              ├──────────────────────────────┤
│ SEÇÃO B — Tool Calling (15m) │              │ SEÇÃO E — HITL (8 min)       │
│  Function calling · Schema   │              │  Matriz de risco · HITL      │
│  Structured outputs · Custo  │              │  Confirmação · Dry-run       │
│  DEMO: tool calling          │              ├──────────────────────────────┤
├──────────────────────────────┤              │ SEÇÃO F — Erros + Aval (10m) │
│ SEÇÃO C — ACI (15 min)       │              │  5 erros · Workbench         │
│  5 princípios · Poka-yoke    │              │  Métricas · Regressão        │
│  Caso SWE-bench · Antes/Dep. │              ├──────────────────────────────┤
│  Intervalo (5 min)           │              │ SEÇÃO G — Fechamento (15 min)│
└──────────────────────────────┘              │  Boas práticas · Quiz · Q&A  │
                                              └──────────────────────────────┘
```

---

## Storyboard Detalhado

### SEÇÃO A — Abertura (Slides 1-6 · 8 min)

| # | Título | Tipo | Tempo | Objetivo |
|---|---|---|---|---|
| 1 | Capa | Capa | 1 min | Identificar aula, professor, contexto |
| 2 | Objetivos do Módulo | Conteúdo | 2 min | 5 objetivos específicos mensuráveis |
| 3 | Competências Desenvolvidas | Conteúdo | 1 min | C1(I), C3(I), C5(B), C6(B) |
| 4 | Agenda da Aula | Conteúdo | 1 min | Timeline com 7 seções e tempos |
| 5 | O Problema: Tools Mal Desenhadas | Conteúdo | 2 min | Tensão — falha silenciosa do agente |
| 6 | ACI como Disciplina de Design | Conteúdo | 1 min | Introduzir ACI :: HCI |

---

### SEÇÃO B — O Mecanismo do Tool Calling (Slides 7-15 · 15 min)

| # | Título | Tipo | Tempo | Objetivo | Diagrama |
|---|---|---|---|---|---|
| 7 | [SEÇÃO] O Mecanismo do Tool Calling | Seção | 0.5 min | Transição | — |
| 8 | Function Calling: Do Prompt para JSON | Conteúdo | 2 min | Fluxo do function calling | Fluxo: LLM → tool_call → exec → obs → LLM |
| 9 | JSON Schema como Contrato | Código | 2 min | Mostrar schema completo | Exemplo JSON Schema de search_product |
| 10 | Structured Outputs / Constrained Decoding | Conteúdo | 1.5 min | Forçar JSON válido | Diagrama de constrained decoding |
| 11 | Multi-tool Calls e Paralelismo | Conteúdo | 1.5 min | Múltiplas tools em 1 resposta | Duas tools executadas em paralelo |
| 12 | Custo: Tokens de Descrição vs Benefício | Conteúdo | 2 min | Trade-off de tokens | Tabela: N tools × tokens × custo |
| 13 | Tool Bem vs Mal Descrita | Comparação | 2 min | Antes vs depois | Duas colunas comparativas |
| 14 | DEMO: Tool Calling na Prática | Código | 3 min | Demo ao vivo | Código + terminal |
| 15 | Pergunta da Demo | Exercício | 2 min | Engajar turma | 3 perguntas em duplas |

---

### SEÇÃO C — ACI como Disciplina (Slides 16-26 · 15 min)

| # | Título | Tipo | Tempo | Objetivo | Diagrama |
|---|---|---|---|---|---|
| 16 | [SEÇÃO] ACI como Disciplina de Design | Seção | 0.5 min | Transição | — |
| 17 | A Analogia: ACI :: HCI | Conteúdo | 2 min | Estabelecer analogia | Comparação HCI vs ACI |
| 18 | Princípio 1: Ponha-se no Lugar do Modelo | Conteúdo | 1.5 min | Empatia com o modelo | — |
| 19 | Princípio 2: Descrições Ricas | Conteúdo | 1.5 min | Docstring de júnior | — |
| 20 | Princípio 3: Formato Próximo ao Natural | Conteúdo | 1.5 min | Sem escaping desnecessário | — |
| 21 | Princípio 4: Poka-yoke | Conteúdo | 2 min | Tornar erro impossível | Antes (path relativo) → Depois (absoluto) |
| 22 | Princípio 5: Tokens para Pensar | Conteúdo | 1 min | max_tokens generoso | — |
| 23 | Exercício: O Que Está Faltando? | Exercício | 3 min | Trios — refatorar send_email | — |
| 24 | Antes vs Depois: Refatoração ACI | Comparação | 2 min | Caso send_email refatorado | Duas colunas |
| 25 | Caso Real: Anthropic SWE-bench | Conteúdo | 2 min | Paths relativos → absolutos | Arquitetura do coding agent |
| 26 | A Lição: Tempo em Tools > Prompt | Conteúdo | 1 min | Checklist mental | Citação Anthropic |

---

### SEÇÃO D — Engenharia de Tools (Slides 27-33 · 12 min)

| # | Título | Tipo | Tempo | Objetivo | Diagrama |
|---|---|---|---|---|---|
| 27 | [SEÇÃO] Engenharia de Tools | Seção | 0.5 min | Transição | — |
| 28 | Schemas Claros: Pydantic, TypedDict, Zod | Conteúdo | 2 min | Padrões de schema | Exemplo Pydantic |
| 29 | Idempotência | Conteúdo | 2 min | request_id, idempotency key | Fluxo de retry com dedup |
| 30 | Timeouts, Retries, Fallbacks | Conteúdo | 2 min | Três camadas de proteção | — |
| 31 | Tipologia: Leitura/Escrita/Destrutiva/External | Conteúdo | 2 min | 4 tipos + nível de proteção | Tabela tipológica |
| 32 | Versionamento de Tools | Conteúdo | 2 min | Compatibilidade retroativa | — |
| 33 | 1 tool com mode vs 2 separadas | Conteúdo | 1.5 min | Regra dos 80% | — |

---

### SEÇÃO E — Tools Perigosas e HITL (Slides 34-36 · 5 min)

| # | Título | Tipo | Tempo | Objetivo | Diagrama |
|---|---|---|---|---|---|
| 34 | [SEÇÃO] Tools Perigosas e HITL | Seção | 0.5 min | Transição | — |
| 35 | Matriz de Risco: Irreversível × Impactante | Conteúdo | 2 min | 4 quadrantes | `12-Diagrams/ETHAGT02/risk-matrix.mmd` |
| 36 | HITL: Confirmação, Dry-run, Simulação | Conteúdo + Exerc. | 3 min | 4 níveis de HITL + exercício de classificação | `12-Diagrams/ETHAGT02/hitl-flow.mmd` |

---

### SEÇÃO F — Erros Comuns e Avaliação (Slides 37-44 · 10 min)

| # | Título | Tipo | Tempo | Objetivo | Diagrama |
|---|---|---|---|---|---|
| 37 | [SEÇÃO] Erros Comuns e Avaliação | Seção | 0.5 min | Transição | — |
| 38 | Os 5 Erros Mais Comuns | Conteúdo | 2 min | Visão geral | — |
| 39 | Erro 1: Paths Relativos → Absolutos | Comparação | 1.5 min | Caso detalhado | Antes vs depois com pattern regex |
| 40 | Erros 2 e 3: Tools Similares, Descrições Vagas | Conteúdo | 1.5 min | Consolidar e reescrever | — |
| 41 | [SEÇÃO] Avaliando Tools | Seção | 0.5 min | Transição | — |
| 42 | Workbench: Rodar, Observar, Iterar | Conteúdo | 2 min | Fluxo de avaliação | `12-Diagrams/ETHAGT02/aci-iteration-loop.mmd` |
| 43 | Métricas: Taxa de Uso, Custo, Latência | Conteúdo | 1.5 min | 4 métricas + metas | Dashboard mockup |
| 44 | Testes de Regressão para Tools | Conteúdo | 1.5 min | CI/CD para tools | Exemplo de caso de teste |

---

### SEÇÃO G — Fechamento (Slides 45-60 · 15 min)

| # | Título | Tipo | Tempo | Objetivo |
|---|---|---|---|---|
| 45 | [SEÇÃO] Boas Práticas e Fechamento | Seção | 0.5 min | Transição |
| 46 | Boas Práticas (DO) | Conteúdo | 2 min | 11 boas práticas |
| 47 | Anti-Patterns (DON'T) | Conteúdo | 2 min | 11 anti-patterns |
| 48 | Caso Consolidado: Anthropic Tool Redesign | Conteúdo | 2 min | Síntese do caso SWE-bench |
| 49 | Exercício: Anti-patterns em Schema | Exercício | 3 min | Trios — refatorar schema de DB |
| 50 | Resumo da Aula | Resumo | 1.5 min | 8 pontos-chave |
| 51-55 | Quiz (5 perguntas) | Quiz | 5 min | ACI, poka-yoke, HITL, erro tratado, regra de ouro |
| 56 | Conexão com Próximos Módulos | Conteúdo | 1 min | ETHAGT03, 04, 08, 12, 13 |
| 57 | Leitura Recomendada e Referências | Referências | 1 min | Anthropic Appendix 2, Gorilla, ToolLLM |
| 58 | Projeto do Módulo | Conteúdo | 1 min | Tools de suporte ao cliente + workbench |
| 59 | Q&A / Encerramento | Capa | 2 min | Perguntas + próxima aula |

---

## Resumo do Storyboard

| Seção | Slides | Tempo | Conteúdo |
|---|---|---|---|
| A — Abertura | 1-6 | 8 min | Capa, objetivos, competências, agenda, motivação, contexto ACI |
| B — Tool Calling | 7-15 | 15 min | Function calling, JSON Schema, structured outputs, custo, demo |
| C — ACI | 16-26 | 15 min | 5 princípios, exercício, antes/depois, caso SWE-bench |
| D — Engenharia | 27-33 | 12 min | Schemas, idempotência, timeouts, tipologia, versionamento |
| E — HITL | 34-36 | 5 min | Matriz de risco, 4 níveis de HITL, exercício |
| F — Erros + Avaliação | 37-44 | 10 min | 5 erros, workbench, métricas, regressão |
| G — Fechamento | 45-60 | 15 min | Boas práticas, anti-patterns, caso, exercício, quiz, Q&A |
| **Total** | **60** | **90 min** | |

---

## Diagramas Necessários

| # | Slide | Diagrama | Tipo | Status |
|---|---|---|---|---|
| D1 | 8 | Fluxo de function calling | Sequência | 🆕 Novo |
| D2 | 9 | JSON Schema exemplo | Código | ✅ No slide |
| D3 | 13 | Tool bem vs mal descrita | Comparação | ✅ No slide |
| D4 | 21 | Poka-yoke: path relativo → absoluto | Antes/Depois | 🆕 Novo |
| D5 | 25 | Arquitetura coding agent SWE-bench | Flowchart | 🆕 Novo |
| D6 | 29 | Idempotência com request_id | Fluxo | 🆕 Novo |
| D7 | 31 | Tipologia de tools (4 tipos) | Tabela | ✅ No slide |
| D8 | 35 | Matriz de risco 2x2 | Matriz | ✅ `risk-matrix.mmd` |
| D9 | 36 | HITL flow | Flowchart | ✅ `hitl-flow.mmd` |
| D10 | 42 | Workbench iteration loop | Loop | ✅ `aci-iteration-loop.mmd` |
| D11 | 43 | Dashboard de métricas | Mockup | 🆕 Novo |

**Total**: 3 existentes + 5 novos + 3 no próprio slide = 11 diagramas.

---

## Pontos de Engajamento

| Slide | Tipo | Interação |
|---|---|---|
| 5 | Reflexão | "Já tiveram bug onde a solução era melhorar o prompt mas o problema era a tool?" |
| 15 | Duplas (2 min) | "O que acontece se op='×' em vez de '*'?" |
| 23 | Trios (3 min) | "Refatore a tool send_email — o que está faltando?" |
| 26 | Reflexão | "Qual erro vocês já cometeram?" |
| 36 | Individual | "Classifique 5 tools por tipo e HITL" |
| 49 | Trios (4 min) | "Identifique 3 anti-patterns no schema DB" |
| 51-55 | Quiz individual | 5 perguntas de múltipla escolha |

---

## Entregáveis do Módulo

| # | Arquivo | Status |
|---|---|---|
| 01 | Storyboard | ✅ Este arquivo |
| 02 | Roteiro | 📋 A ser criado |
| 03 | Slides detalhados + notas | ✅ No PPTX gerado |
| 04 | Notas do professor | ✅ Embutidas no PPTX |
| 05 | Sugestões de diagramas | 📋 A ser criado |
| 06 | Referências | ✅ `20-Research/ETHAGT02-pesquisa.md` |
| 07 | Checklist da aula | 📋 A ser criado |
| 08 | Perguntas para discussão | 📋 A ser criado |
| 09 | Exercícios | 📋 A ser criado |
| 10 | Quiz final | ✅ Slides 51-55 do PPTX |
| PPTX | Apresentação PowerPoint | ✅ `ETHAGT02-Apresentacao.pptx` |
