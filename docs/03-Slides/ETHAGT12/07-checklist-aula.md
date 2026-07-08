# ETHAGT12 — Checklist da Aula

> Checklist para o professor verificar antes, durante e depois da aula.

---

## Pré-Aula (24h antes)

### Preparação Técnica
- [ ] API key (OpenAI ou Anthropic) testada e funcionando
- [ ] Python 3.11+ instalado e com dependências (`openai`, `langchain`, `langsmith`, `langfuse` ou `arize-phoenix`)
- [ ] VS Code aberto com `05-Labs/ETHAGT12/Lab1-Traces-Everywhere` e `Lab2-Eval-Automatizado`
- [ ] Terminal testado: ambos os labs executam sem erro
- [ ] Conta LangSmith configurada (ou Phoenix/Langfuse local rodando)
- [ ] Screenshot de trace real salvo (plano B se API falhar) — Slide 24
- [ ] Screenshot de eval report com regressão salvo — Slide 40
- [ ] Conjunto de 10 golden cases pronto para DEMO do Slide 40
- [ ] Projetor testado
- [ ] Slides exportados para PDF (plano B se apresentação falhar)

### Preparação de Conteúdo
- [ ] Revisar todas as notas do professor (78 slides)
- [ ] Ensaiar a DEMO de traces (Slide 24) — rodar pelo menos 2x antes
- [ ] Ensaiar a DEMO de eval (Slide 40) — validar que regressão aparece
- [ ] Preparar o trace com loop para exercício do Slide 26
- [ ] Confirmar que todos os 22 diagramas estão legíveis (3 existem em `12-Diagrams/ETHAGT12/`)
- [ ] Preparar handout (opcional): storyboard impresso

### Preparação de Logística
- [ ] Sala reservada para 90 min + 15 min de buffer
- [ ] Quadro branco disponível (para anotar votações)
- [ ] Acesso ao repositório da especialização confirmado
- [ ] Template de eval report acessível (`24-Templates/template-eval-report.md`)

---

## Durante a Aula

### Bloco 1 (45 min)
- [ ] **Slides 1-6 (8 min)**: Abertura — anotar resposta da turma no Slide 5
- [ ] **Slide 5**: Fazer a pergunta "Como você sabe se seu agente está melhor ou pior?"
- [ ] **Slide 11**: Anotar quais falácias a turma já cometeu
- [ ] **Slide 14**: Votação de falácias — anotar resultados no quadro
- [ ] **Slides 15-23 (10 min)**: Observabilidade — garantir que todos entendem spans e traces
- [ ] **Slide 17**: Animar o diagrama `trace-anatomy.mmd` — explicar hierarquia
- [ ] **Slide 24 (3 min)**: DEMO AO VIVO de traces — se API falhar, usar screenshot
- [ ] **Slides 25-26**: Discussão em duplas (lendo um trace)
- [ ] **Slide 27**: Pergunta custo vs investimento
- [ ] Intervalo (5 min)

### Bloco 2 (45 min)
- [ ] **Slides 28-37 (10 min)**: LLM-as-judge, golden cases, métricas
- [ ] **Slide 31**: Pergunta sobre viés mais perigoso
- [ ] **Slide 39**: Animar o diagrama `eval-pipeline.mmd` — explicar gate de CI
- [ ] **Slide 40 (3 min)**: DEMO AO VIVO de eval — se API falhar, usar screenshot
- [ ] **Slides 41-42**: Discussão em duplas (escrevendo golden cases)
- [ ] **Slide 43**: V/F rápido
- [ ] **Slides 44-54 (14 min)**: Benchmarks
- [ ] **Slide 46**: Animar `benchmark-landscape.mmd`
- [ ] **Slide 53**: Votação de benchmark por cenário
- [ ] **Slide 54**: Pergunta benchmark vs produção
- [ ] **Slides 55-59 (5 min)**: Melhoria contínua — CI, shadow, canary
- [ ] **Slides 60-63 (5 min)**: Eval report e análise de falhas
- [ ] **Slide 64 (3 min)**: Exercício em grupos (detectando regressão)
- [ ] **Slides 65-70 (2 min)**: Boas práticas, anti-patterns, caso, resumo
- [ ] **Slides 71-75 (5 min)**: Quiz — individual, sem consulta
- [ ] **Slides 76-77**: Conexão, projeto, leitura
- [ ] **Slide 78 (2 min)**: Q&A

---

## Pós-Aula

### Avaliação
- [ ] Contar resultados do quiz (≥3 acertos = compreensão básica)
- [ ] Anotar perguntas frequentes no Q&A para futuras iterações
- [ ] Pedir feedback informal: "Um conceito que você vai aplicar segunda-feira"
- [ ] Verificar tempo real vs planejado por seção
- [ ] Avaliar qualidade dos golden cases escritos no Slide 42

### Follow-up
- [ ] Enviar leitura recomendada no Slack/email (3 papers canônicos)
- [ ] Disponibilizar slides (PDF + repositório)
- [ ] Lembrar prazo do Lab 1 — "Traces Everywhere" (1 semana)
- [ ] Lembrar prazo do Lab 2 — "Eval Automatizado" (2 semanas)
- [ ] Lembrar prazo do Projeto do módulo (4 semanas)
- [ ] Preparar ETHAGT13 (a próxima aula: Segurança & Governança — observabilidade vira defesa)

---

## Sinais de Alerta Durante a Aula

| Sinal | Ação |
|---|---|
| Alunos confusos no Slide 16-17 (traces) | Simplificar: focar só em root + children + timing |
| DEMO de traces falha | Screenshot do trace pré-gravado + seguir |
| DEMO de eval falha | Screenshot do eval report com regressão + seguir |
| Tempo estourado no Bloco 1 | Cortar Slide 26 (exercício de trace), mover para homework |
| Tempo estourado no Bloco 2 | Reduzir quiz para 3 perguntas (Slides 71-73); Slide 77 como leitura |
| Nenhuma pergunta no Q&A | Fazer pergunta inversa: "Qual parte foi menos clara?" |
| Discussão longa no Slide 64 | Encerrar com 1-2 compartilhamentos e seguir |
| Alunos sem ETHAGT11 | Reforçar conceitos de traces no Slide 16-17; oferecer material complementar |
| LangSmith/Phoenix indisponível | Mostrar traces de arquivo JSONL exportado |

---

## Pontos Críticos de Atenção

### DEMOs (Slides 24 e 40)
- **Plano A**: rodar ao vivo
- **Plano B**: screenshot pré-gravado (sempre ter pronto)
- **Plano C**: vídeo gravado (em caso de falha total)

### Exercícios em Duplas (Slides 26, 42)
- Garantir que todos estejam em duplas
- Tempo rigoroso (cronometrar)
- Pedir 2 compartilhamentos no máximo

### Quiz (Slides 71-75)
- Individual, sem consulta
- Cronometrar 5 min total
- Pedir mãos levantadas por alternativa para medir compreensão
