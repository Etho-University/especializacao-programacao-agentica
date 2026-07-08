# ETHAGT16 — Roteiro da Apresentação

> Universidade Etho · Especialização em Programação Agêntica
> Fase D — Fronteira · 15 h

---

## Metadados

| Campo | Valor |
|---|---|
| Código | ETHAGT16 |
| Título | Sociedades de Agentes & Autonomous Research Systems |
| Duração | 50 min (2 blocos de 25 min) |
| Total de slides | 50 |
| Competências | C1 (A), C2 (A), C3 (B), C4 (A), C5 (I), C6 (I) |
| Pré-requisitos | ETHAGT15 |
| Fontes canônicas | Park et al. *Generative Agents* (arXiv:2304.03442); Lu et al. *AI Scientist* (arXiv:2408.06292); Chen et al. *AgentVerse* (arXiv:2308.10848); DeepMind *AlphaEvolve* (2024) |

---

## Fluxo da Aula

### BLOCO 1 — 25 min

| Seção | Slides | Tempo | Objetivo |
|---|---|---|---|
| A — Abertura | 1-6 | 6 min | Engajar, posicionar a fronteira e estabelecer objetivos |
| B — Sociedades de Agentes | 7-15 | 8 min | Papéis, normas, reputação, modelos canônicos, diagrama, exercício |
| C — Simulações Sociais | 16-22 | 6 min | Smallville, arquitetura técnica, casos de uso, limites |
| Intervalo | — | 5 min | — |

### BLOCO 2 — 25 min

| Seção | Slides | Tempo | Objetivo |
|---|---|---|---|
| D — Autonomous Research Systems | 23-33 | 12 min | Pipeline, AI Scientist, AlphaEvolve, DEMO, estudo de caso |
| E — Emergência e Alinhamento | 34-41 | 8 min | Comportamento emergente, alinhamento, avaliação, exercício |
| F — Fechamento | 42-50 | 10 min | Fronteira, ética, exercício, resumo, quiz, Capstone, Q&A |
| Q&A extra | — | 5 min | Perguntas abertas |

---

## Pontos de Engajamento

| Slide | Tipo | Interação |
|---|---|---|
| 5 | Hook | "O que acontece quando 100 agentes interagem sem supervisão humana?" |
| 9 | Discussão rápida | "Qual papel de uma sociedade de agentes é mais difícil de automatizar?" |
| 15 | Duplas (1 min) | Definir 5 papéis para comitê editorial + norma + reputação |
| 20 | Hook | "Uma simulação social com LLMs pode prever comportamento humano real?" |
| 21 | V/F | "Sociedades de agentes sempre convergem." |
| 22 | Duplas (1 min) | Design de simulação: 3 agentes, 2 normas, 1 métrica (home office) |
| 30 | DEMO ao vivo | Mini sociedade de 5 agentes produzindo relatório |
| 31 | Duplas (1 min) | "Qual papel foi mais crítico? E sem o crítico?" |
| 40 | Hook | "Quando comportamento emergente é indesejado?" |
| 41 | Duplas (1 min) | Detectar emergência indesejada em trace + 2 correções |
| 44 | Hook | "Onde você traça a linha entre agente útil e perigoso?" |
| 46 | Grupo (3 min) | Definir 3 critérios para avaliar qualidade científica de AI Scientist |
| 48 | Quiz individual | 3 perguntas rápidas (pipeline, emergência, convergência) |
| 49 | Reflexão | "Pesquisa, produto ou impacto social — para onde vocês querem levar isso?" |

---

## Materiais Necessários

- [ ] Projetor / tela de compartilhamento
- [ ] VS Code aberto com `05-Labs/ETHAGT16/Lab1-Mini-Sociedade/main.py`
- [ ] Terminal com Python 3.11+ e `OPENAI_API_KEY` configurada
- [ ] Acesso ao repositório da especialização
- [ ] Quadro branco (para diagramas improvisados)
- [ ] Handout: storyboard impresso (opcional)
- [ ] Screenshot do trace da DEMO (plano B)
- [ ] Paper fake para exercício do Slide 46

---

## Riscos e Planos B

| Risco | Plano B |
|---|---|
| API LLM indisponível na DEMO (Slide 30) | Mostrar trace pré-gravado (screenshot) do Lab1 |
| Alunos sem ETHAGT15 | Revisar multi-agent básico (ETHAGT09-10) em 3 min |
| Tempo estourado no Bloco 1 | Cortar exercício do Slide 22 (home office); mover para homework |
| Tempo estourado no Bloco 2 | Reduzir quiz para 1 pergunta (Slide 48); referências como leitura |
| Debate ético (Slide 44) tomam tempo demais | Colocar limite de 2 min; coletar perguntas para o Q&A |

---

## Avaliação da Aula

- Quiz ao final (Slide 48): ≥2 acertos em 3 = compreensão básica
- Exercício de papéis (Slide 15): discussão em duplas
- Exercício de emergência (Slide 41): profundidade das correções propostas
- Exercício de avaliação de AI Scientist (Slide 46): qualidade dos critérios
- Feedback informal: "O que vocês querem investigar no Capstone?"
