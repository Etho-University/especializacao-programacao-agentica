# ETHAGT15 — Roteiro da Apresentação

> Universidade Etho · Especialização em Programação Agêntica
> Fase D — Fronteira · 15 h

---

## Metadados

| Campo | Valor |
|---|---|
| Código | ETHAGT15 |
| Título | Meta-Agentes & Sistemas Autoaprendentes (agents that build agents) |
| Duração | 90 min (2 blocos de 45 min) |
| Total de slides | 67 |
| Competências | C1 (A), C2 (A), C3 (B), C4 (A), C6 (I) |
| Fontes canônicas | Khattab et al. *DSPy* (arXiv:2310.03714); Fernando et al. *Promptbreeder* (arXiv:2309.16797); Wang et al. *Voyager* (arXiv:2305.16291); Lu et al. *AI Scientist* (arXiv:2408.06292) |

---

## Fluxo da Aula

### BLOCO 1 — 45 min

| Seção | Slides | Tempo | Objetivo |
|---|---|---|---|
| A — Abertura | 1-6 | 8 min | Engajar, contextualizar meta-agência e estabelecer objetivos |
| B — Meta-Agência | 7-14 | 12 min | Definição, estratégias, arquitetura, risco × benefício |
| C — Geração de Agentes | 15-24 | 15 min | Meta-agente, templates, pipeline, validação, DEMO |
| Intervalo | — | 5 min | — |

### BLOCO 2 — 45 min

| Seção | Slides | Tempo | Objetivo |
|---|---|---|---|
| D — Otimização Automatizada | 25-35 | 15 min | DSPy, Promptbreeder, Atlas, tools, topologia |
| E — Auto-Aprendizado Contínuo | 36-45 | 13 min | Memória, Reflexion, Voyager, drift |
| F — Riscos e Governança | 46-55 | 12 min | Recursão, goal drift, meta-governor, vetos |
| G — Fechamento | 56-67 | 10 min | Boas práticas, quiz, referências, Q&A |

---

## Pontos de Engajamento

| Slide | Tipo | Interação |
|---|---|---|
| 5 | Pergunta provocativa | "Você deixaria um agente modificar o próprio prompt?" |
| 13 | Votação | Sim / Não / Depende — auto-modificação |
| 14 | Votação rápida | 4 cenários: é meta-agência ou não? |
| 21 | DEMO ao vivo | Agente que escreve agente |
| 22 | Duplas (2 min) | Perguntas sobre a DEMO |
| 23 | Duplas (3 min) | Listar 5 critérios de qualidade |
| 35 | Discussão aberta | Quando otimizar vs reescrever manualmente |
| 42 | Duplas (2 min) | O que acontece se o ambiente muda? |
| 44 | V/F | Auto-aprendizado sempre melhora? |
| 53 | Trios (5 min) | Projetar um meta-governor |
| 54 | Discussão aberta | Quando um meta-agente se torna perigoso? |
| 61-63 | Quiz individual | 3 perguntas de múltipla escolha |
| 64 | Grupo | 4 perguntas de discussão profunda |

---

## Materiais Necessários

- [ ] Projetor / tela de compartilhamento
- [ ] VS Code aberto com `05-Labs/ETHAGT15/Lab1-Agente-que-Escreve-Agente`
- [ ] Terminal com Python 3.11+ e `OPENAI_API_KEY` configurada
- [ ] Acesso ao repositório da especialização
- [ ] Quadro branco (para diagramas improvisados)
- [ ] Handout: storyboard impresso (opcional)
- [ ] Sandbox de DSPy preparado (caso queira rodar otimização ao vivo)

---

## Riscos e Planos B

| Risco | Plano B |
|---|---|
| API LLM indisponível na DEMO (Slide 21) | Mostrar config JSON gerada + eval pré-gravado (screenshot) |
| Alunos sem ETHAGT10 concluído | Recaptular eval, memória e multi-agente nos primeiros 2 min |
| Tempo estourado no Bloco 1 | Cortar exercício do Slide 14; mover para homework |
| Tempo estourado no Bloco 2 | Reduzir quiz para 1 pergunta (Slide 61); referências como leitura |
| Discussão do Slide 54 muito longa | Limitar a 2 min e levar o tema para o fórum assíncrono |
| Debate acalorado sobre perigo de AGI | Redirecionar para mitigações concretas (safety fences) |

---

## Avaliação da Aula

- Quiz ao final (Slides 61-63): ≥2 acertos = compreensão básica
- Exercício de meta-governor (Slide 53): qualidade das regras de veto propostas
- Perguntas de discussão (Slide 64): profundidade das respostas
- Feedback informal: "Uma técnica de otimização que você aprendeu hoje e não conhecia"
