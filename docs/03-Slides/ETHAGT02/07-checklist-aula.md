# ETHAGT02 — Checklist da Aula

> Checklist para o professor verificar antes, durante e depois da aula.

---

## Pré-Aula (24h antes)

### Preparação Técnica
- [ ] API key (OpenAI ou Anthropic) testada e funcionando
- [ ] Python 3.11+ com `openai`, `anthropic`, `pydantic` instalados
- [ ] VS Code aberto com exemplo de tool calling (`19-Examples/ETHAGT02/`)
- [ ] Terminal testado: demo de tool_call executa sem erro
- [ ] Screenshot do workbench ACI salvo (plano B se API falhar)
- [ ] Screenshot do HITL flow salvo (plano B se demo de HITL falhar)
- [ ] Projetor testado
- [ ] Slides exportados para PDF (plano B se apresentação falhar)

### Preparação de Conteúdo
- [ ] Revisar todas as notas do professor (60 slides)
- [ ] Ensaiar a demo de tool calling (Slide 14) — rodar pelo menos 2x antes
- [ ] Preparar o schema mal-desenhado do exercício (Slide 49)
- [ ] Preparar a tool `send_email` "antes" e "depois" para o Slide 24
- [ ] Confirmar que todos os 3 diagramas `.mmd` renderizam corretamente
- [ ] Preparar handout (opcional): matriz de risco impressa + checklist ACI

### Preparação de Logística
- [ ] Sala reservada para 90 min + 15 min de buffer
- [ ] Quadro branco disponível (para desenhar matriz de risco e HITL)
- [ ] Acesso ao repositório da especialização confirmado

---

## Durante a Aula

### Bloco 1 (45 min)
- [ ] **Slide 1-6 (8 min)**: Abertura — anotar nomes de alunos que participam
- [ ] **Slide 5**: Fazer a pergunta de reflexão ("Bug onde prompt não resolve, tool resolve?")
- [ ] **Slide 9**: Destacar JSON Schema como contrato — garantir que todos entendem
- [ ] **Slide 12**: Mostrar tabela de custo (tokens de descrição × N tools)
- [ ] **Slide 13**: Mostrar antes/depois — tool bem vs mal descrita
- [ ] **Slide 14 (3 min)**: DEMO AO VIVO — se API falhar, usar screenshot do trace
- [ ] **Slide 15**: Pergunta da demo — deixar 2 min em duplas
- [ ] **Slide 17**: Estabelecer a analogia ACI :: HCI — slide-chave
- [ ] **Slide 21**: Mostrar poka-yoke (path relativo → absoluto) — slide mais importante
- [ ] **Slide 23 (3 min)**: Exercício em trios — refatorar send_email
- [ ] **Slide 25**: Caso SWE-bench — paths relativos → absolutos
- [ ] **Slide 26**: Citação Anthropic — "tempo em tools > prompt"
- [ ] Intervalo (5 min)

### Bloco 2 (45 min)
- [ ] **Slide 28**: Mostrar Pydantic como padrão de schema
- [ ] **Slide 29**: Explicar idempotência com request_id
- [ ] **Slide 31**: Tipologia de 4 tipos de tools — pedir exemplos da turma
- [ ] **Slide 33**: Regra dos 80% — 1 tool com mode vs 2 separadas
- [ ] **Slide 35**: Matriz de risco — `risk-matrix.mmd`
- [ ] **Slide 36 (3 min)**: HITL flow + exercício de classificação individual
- [ ] **Slide 38-40**: Os 5 erros mais comuns — pedir exemplos da turma
- [ ] **Slide 42**: Workbench — `aci-iteration-loop.mmd`
- [ ] **Slide 46-47**: Boas práticas e anti-patterns — pedir exemplos
- [ ] **Slide 49 (4 min)**: Exercício em trios — anti-patterns no schema DB
- [ ] **Slide 51-55 (5 min)**: Quiz — individual, sem consulta
- [ ] **Slide 58 (2 min)**: Q&A

---

## Pós-Aula

### Avaliação
- [ ] Contar resultados do quiz (≥3 acertos = compreensão básica)
- [ ] Anotar perguntas frequentes no Q&A para futuras iterações
- [ ] Pedir feedback informal: "Uma refatoração de tool que você faria amanhã"
- [ ] Verificar tempo real vs planejado por seção

### Follow-up
- [ ] Enviar leitura recomendada no Slack/email (Anthropic Appendix 2)
- [ ] Disponibilizar slides (PDF + repositório)
- [ ] Lembrar prazo do Lab 1 — "Refatorando tools" (1 semana)
- [ ] Lembrar prazo do Projeto — tools de suporte ao cliente + workbench (2 semanas)
- [ ] Preparar ETHAGT03 (próxima aula aprofunda padrões de workflow)

---

## Sinais de Alerta Durante a Aula

| Sinal | Ação |
|---|---|
| Alunos confusos no Slide 9 (JSON Schema) | Simplificar: focar só em `properties` + `required`; link para tutorial pós-aula |
| DEMO de tool calling falha | Screenshot do trace pré-gravado + seguir |
| Tempo estourado no Bloco 1 | Cortar Slide 23 (exercício send_email), mover para homework |
| Tempo estourado no Bloco 2 | Reduzir quiz para 3 perguntas (Slides 51-53) |
| Nenhuma pergunta no Q&A | Fazer pergunta inversa: "Qual princípio ACI foi menos claro?" |
| Alunos sem pré-requisito de JSON Schema | Direcionar para tutorial; oferecer lab de schema como reforço |
| Turma divide entre "1 tool com mode" vs "2 separadas" | Reforçar a regra dos 80%: se >80% dos casos usam ambas, consolidar |
