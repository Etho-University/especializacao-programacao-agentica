# ETHAGT05 — Checklist da Aula

> Checklist para o professor verificar antes, durante e depois da aula.

---

## Pré-Aula (24h antes)

### Preparação Técnica
- [ ] Postgres rodando: `docker run -d -p 5432:5432 -e POSTGRES_PASSWORD=etho postgres:16`
- [ ] Qdrant rodando: `docker run -d -p 6333:6333 qdrant/qdrant`
- [ ] Python 3.11+ com dependências instaladas (`langgraph`, `langgraph-checkpoint-postgres`, `openai`, `qdrant-client`, `psycopg2-binary`)
- [ ] `OPENAI_API_KEY` configurada no `.env`
- [ ] VS Code aberto com `05-Labs/ETHAGT05/Lab1-Checkpointer-Postgres/`
- [ ] Terminal testado: `python main.py` executa sem erro (agente inicia + checkpoint gravado)
- [ ] Testar resume: matar processo e reiniciar com mesmo `thread_id`
- [ ] Screenshot do resume de checkpointer salvo (plano B se demo falhar)
- [ ] Projetor testado
- [ ] Slides exportados para PDF (plano B se apresentação falhar)

### Preparação de Conteúdo
- [ ] Revisar todas as notas do professor (70 slides)
- [ ] Ensaiar a demo (Slide 28) — rodar pelo menos 3x antes (pause/resume)
- [ ] Preparar o exercício de eviction (Slide 39) — template impresso
- [ ] Confirmar que todos os 16 diagramas estão legíveis (ver `05-diagramas.md`)
- [ ] Revisar os 3 diagramas `.mmd` existentes (memory-layers, checkpointer-resume, eviction-flow)
- [ ] Preparar handout (opcional): storyboard impresso

### Preparação de Logística
- [ ] Sala reservada para 90 min + 15 min de buffer
- [ ] Quadro branco disponível (para desenhar as 4 camadas de improviso)
- [ ] Acesso ao repositório da especialização confirmado
- [ ] Confirmar pré-requisito: alunos cursaram ETHAGT04 (reasoning patterns)

---

## Durante a Aula

### Bloco 1 (45 min)

#### Seção A — Abertura (8 min)
- [ ] **Slide 1-2**: Apresentar — confirmar nomes de alunos novos
- [ ] **Slide 5**: Fazer a pergunta de mão levantada ("Quanto contexto um assistente precisa reter?")
- [ ] **Slide 6**: Destacar a timeline de marcos — 2020 (2k tokens) → 2025 (MemGPT, Zep)

#### Seção B — Tipos de Memória (12 min)
- [ ] **Slide 8**: Mostrar working memory como context window — anotar "tokens processados a cada chamada"
- [ ] **Slide 9**: Mostrar curva U (Lost in the Middle) — esta é a prova de que context maior não resolve
- [ ] **Slide 13**: Mostrar a tabela 4×4 — pedir para turma preencher uma linha
- [ ] **Slide 14**: Mostrar diagrama `memory-layers.mmd` — este é o slide-chave do bloco
- [ ] **Slide 16**: Apresentar MemGPT — analogia SO (RAM vs disco)

#### Seção C — Checkpointer (15 min)
- [ ] **Slide 19**: Explicar estado serializável — conectar com ETHAGT03 (StateGraph)
- [ ] **Slide 22**: Comparar backends — anotar qual a turma usaria
- [ ] **Slide 24**: Mostrar diagrama `checkpointer-resume.mmd`
- [ ] **Slide 26**: Mostrar branching com git graph — analogia `git checkout -b`
- [ ] **Slide 28 (3 min)**: DEMO AO VIVO — checkpointer em Postgres
  - Passo 1: agente inicia tarefa (`thread_id = "demo-001"`)
  - Passo 2: interromper processo (`Ctrl+C`)
  - Passo 3: reiniciar, retomar com mesmo `thread_id`
  - Passo 4: mostrar estado preservado (mensagens, contexto)
  - Se Postgres falhar: usar screenshot
- [ ] **Slide 29**: Pergunta da demo — deixar 2 min em duplas

#### Seção D — Gerenciamento de Contexto (10 min)
- [ ] **Slide 32**: Desmistificar o "custo quadrático" — este é o ponto crítico de pensamento
- [ ] **Slide 34**: Mostrar sumarização em cascata — pirâmide invertida
- [ ] **Slide 36**: Mostrar diagrama `eviction-flow.mmd`
- [ ] **Slide 39 (3 min)**: Exercício de política de eviction em trios
- [ ] Intervalo (5 min)

### Bloco 2 (45 min)

#### Seção E — Memória Vetorial (12 min)
- [ ] **Slide 42**: Explicar embedding de eventos — pipeline (texto → embedding → vector DB)
- [ ] **Slide 44**: Explicar metadata filtering — "filter + rank, não um ou outro"
- [ ] **Slide 46**: Mostrar pipeline completo de recall (6 etapas) — slide-chave do bloco
- [ ] **Slide 48**: Apresentar Lab 2 (Memória Episódica)
- [ ] **Slide 49 (2 min)**: Discussão aberta — "Embedding ou metadata? 3 cenários"

#### Seção F — Semântica e Grafos (8 min)
- [ ] **Slide 52**: Mostrar consolidação — eventos convergindo para fatos
- [ ] **Slide 56**: Apresentar Generative Agents — memory stream de Smallville
- [ ] **Slide 57**: Preview de ETHAGT07 (Knowledge Graphs)

#### Seção G — Produção (8 min)
- [ ] **Slide 59**: Mostrar race condition multi-agente
- [ ] **Slide 60**: Destacar PII e redação — conectar com LGPD
- [ ] **Slide 61**: Direito ao esquecimento em vector DB — 3 estratégias
- [ ] **Slide 62**: Discutir "quando NÃO memorizar" — critério de custo vs benefício
- [ ] **Slide 63**: Observabilidade de memória — "memória é sistema, precisa de monitoring"

#### Seção H — Fechamento (12 min)
- [ ] **Slide 64-65**: Boas práticas e anti-patterns — pedir exemplos da turma
- [ ] **Slide 66**: Resumo — revisar os 6 pontos-chave
- [ ] **Slide 67-69 (3 min)**: Quiz — individual, sem consulta
- [ ] **Slide 70**: Conexão (ETHAGT06, ETHAGT07, ETHAGT14), projeto, labs, Q&A
- [ ] Q&A extra (5 min)

---

## Pós-Aula

### Avaliação
- [ ] Contar resultados do quiz (≥2 acertos = compreensão básica)
- [ ] Anotar perguntas frequentes no Q&A para futuras iterações
- [ ] Pedir feedback informal: "Um tipo de memória que você não conhecia antes de hoje"
- [ ] Verificar tempo real vs planejado por seção
- [ ] Avaliar engajamento no exercício de eviction (Slide 39)

### Follow-up
- [ ] Enviar leitura recomendada no Slack/email: MemGPT (arXiv:2310.08560)
- [ ] Disponibilizar slides (PDF + repositório)
- [ ] Lembrar prazo do Lab 1 (Checkpointer em Postgres, 4h, 1 semana)
- [ ] Lembrar prazo do Lab 2 (Memória Episódica, 5h, 2 semanas)
- [ ] Lembrar prazo do Projeto do módulo (memória de agente pessoal + ADR + política)
- [ ] Preparar ETHAGT06 (a próxima aula aprofunda RAG Agêntico)

---

## Sinais de Alerta Durante a Aula

| Sinal | Ação |
|---|---|
| Alunos confusos na distinção das 4 camadas | Simplificar: focar só em Working vs Episódica primeiro |
| DEMO falha (Postgres ou API) | Screenshot do resume + logs pré-gravados + seguir |
| Tempo estourado no Bloco 1 | Cortar Slide 39 (eviction exercise), mover para homework |
| Tempo estourado no Bloco 2 | Reduzir quiz para 2 perguntas (Slides 67-68) |
| Turma sem pré-requisito de StateGraph | Revisar ETHAGT03 em 5 min antes da Seção C |
| Confusão sobre vector DB | Simplificar: focar só em "texto → número → busca por distância" |
| Nenhuma pergunta no Q&A | Fazer pergunta inversa: "Qual camada de memória achou menos clara?" |
| Alunos questionam inspiração cognitiva | Valido: reforçar "framework de design, não modelo neural" (Slide 15) |

---

## Checkpoint de Progresso (Mid-Lesson)

No fim do Bloco 1 (após Slide 40), verificar:

- [ ] A turma distingue as 4 camadas de memória?
- [ ] Entenderam que context window NÃO é memória de longo prazo?
- [ ] Viram o checkpointer funcionando (resume)?
- [ ] Conhecem pelo menos 2 estratégias de gestão de contexto?

Se algum "não", ajustar o Bloco 2 para reforçar.
