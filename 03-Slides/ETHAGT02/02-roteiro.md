# ETHAGT02 — Roteiro da Apresentação

> Universidade Etho · Especialização em Programação Agêntica
> Fase A — Fundamentos Agênticos · 25 h

---

## Metadados

| Campo | Valor |
|---|---|
| Código | ETHAGT02 |
| Título | Tool Calling e Agent-Computer Interface (ACI) |
| Duração | 90 min (2 blocos de 45 min) |
| Total de slides | 60 |
| Competências | C1 (I), C3 (I), C5 (B), C6 (B) |
| Fontes canônicas | Anthropic *Building Effective Agents* Appendix 2 (2024); Schick et al. *Toolformer* (NeurIPS 2023); arXiv:2305.15334 *Gorilla*; arXiv:2307.16789 *ToolLLM* |

---

## Fluxo da Aula

### BLOCO 1 — 45 min

| Seção | Slides | Tempo | Objetivo |
|---|---|---|---|
| A — Abertura | 1-6 | 8 min | Engajar, contextualizar e estabelecer objetivos de ACI |
| B — Tool Calling | 7-15 | 15 min | Function calling, JSON Schema, structured outputs, DEMO ao vivo |
| C — ACI como Disciplina | 16-26 | 15 min | Analogia HCI, 5 princípios, exercício, caso SWE-bench |
| Intervalo | — | 5 min | — |

### BLOCO 2 — 45 min

| Seção | Slides | Tempo | Objetivo |
|---|---|---|---|
| D — Engenharia de Tools | 27-33 | 12 min | Schemas, idempotência, timeouts, tipologia, versionamento |
| E — Tools Perigosas e HITL | 34-36 | 5 min | Matriz de risco, 4 níveis de HITL, exercício de classificação |
| F — Erros Comuns e Avaliação | 37-44 | 10 min | 5 erros, workbench, métricas, testes de regressão |
| G — Fechamento | 45-60 | 15 min | Boas práticas, anti-patterns, caso, exercício, quiz, Q&A |
| Q&A extra | — | 3 min | Perguntas abertas |

---

## Pontos de Engajamento

| Slide | Tipo | Interação |
|---|---|---|
| 5 | Reflexão | "Já tiveram bug onde a solução era melhorar o prompt mas o problema era a tool?" |
| 14 | DEMO ao vivo | Rodar tool calling com OpenAI SDK |
| 15 | Duplas (2 min) | "O que acontece se op='×' em vez de '*'?" |
| 23 | Trios (3 min) | "Refatore a tool send_email — o que está faltando?" |
| 26 | Reflexão | "Qual erro de design de tools vocês já cometeram?" |
| 36 | Individual (2 min) | "Classifique 5 tools por tipo e HITL" |
| 49 | Trios (4 min) | "Identifique 3 anti-patterns no schema DB" |
| 51-55 | Quiz individual | 5 perguntas de múltipla escolha |

---

## Materiais Necessários

- [ ] Projetor / tela de compartilhamento
- [ ] VS Code aberto com exemplo de tool calling (`19-Examples/ETHAGT02/`)
- [ ] Terminal com Python 3.11+, `openai` e `pydantic` instalados
- [ ] `OPENAI_API_KEY` (ou `ANTHROPIC_API_KEY`) configurada e testada
- [ ] Acesso ao repositório da especialização
- [ ] Quadro branco (para desenhar matriz de risco e fluxos de HITL)
- [ ] Handout: storyboard impresso + tabela de matriz de risco (opcional)
- [ ] Screenshots do workbench ACI salvos (plano B se demo falhar)

---

## Riscos e Planos B

| Risco | Plano B |
|---|---|
| API LLM indisponível na DEMO (Slide 14) | Mostrar trace pré-gravado de tool_call + observation (screenshot) |
| Alunos não dominam JSON Schema | Gastar 2 min extra no Slide 9; oferecer link para tutorial pós-aula |
| Tempo estourado no Bloco 1 | Cortar exercício do Slide 23 (refatoração send_email); mover para homework |
| Tempo estourado no Bloco 2 | Reduzir quiz para 3 perguntas; referências como leitura |
| Turma pouco familiarizada com idempotência | Simplificar Slide 29 para exemplo de `request_id`; aprofundar em ETHAGT08 |
| Conexão instável para demo de HITL | Usar mock local do fluxo de confirmação |

---

## Avaliação da Aula

- Quiz ao final (Slides 51-55): ≥3 acertos = compreensão básica
- Exercício de classificação de HITL (Slide 36): discussão individual
- Exercício de anti-patterns (Slide 49): discussão em trios
- Perguntas de discussão (Slide 58): profundidade das respostas no Q&A
- Feedback informal: "Uma refatoração de tool que você faria amanhã no trabalho"
