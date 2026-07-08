# ETHAGT13 — Checklist da Aula

> Checklist para o professor verificar antes, durante e depois da aula.

---

## Pré-Aula (24h antes)

### Preparação Técnica
- [ ] API key (OpenAI ou Anthropic) testada e funcionando
- [ ] Python 3.11+ instalado com dependências (`openai`, `pydantic`, `regex`)
- [ ] VS Code aberto com `05-Labs/ETHAGT13/Lab1-Red-Team-RAG`
- [ ] Terminal testado: agente RAG rodando e respondendo
- [ ] Documento RAG malicioso preparado (5 payloads de injeção indireta)
- [ ] OPA / Rego CLI instalado (`opa version` roda sem erro)
- [ ] Política Rego de exemplo salva (Slide 58) para mostrar
- [ ] Garak instalado e com probes básicos rodando (`garak --model ... `)
- [ ] Screenshot do trace da DEMO salvo (plano B se API falhar)
- [ ] Projetor testado
- [ ] Slides exportados para PDF (plano B se apresentação falhar)

### Preparação de Conteúdo
- [ ] Revisar todas as notas do professor (77 slides)
- [ ] Ensaiar a DEMO de red team (Slide 26) — rodar pelo menos 3x antes
- [ ] Preparar os 5 payloads de injeção para a DEMO (testados)
- [ ] Confirmar que todos os diagramas (3 do `12-Diagrams/ETHAGT13/`) estão legíveis
- [ ] Preparar templates de exercícios (Slides 14, 36, 54, 63)
- [ ] Revisar papers canônicos (OWASP, Greshake, AgentDojo, InjecAgent)
- [ ] Preparar handout (opcional): storyboard impresso

### Preparação de Logística
- [ ] Sala reservada para 90 min + 15 min de buffer
- [ ] Quadro branco disponível (para desenhar defense in depth)
- [ ] Acesso ao repositório da especialização confirmado
- [ ] Confirmar que alunos completaram ETHAGT12 (pré-requisito)

---

## Durante a Aula

### Bloco 1 (45 min)
- [ ] **Slide 1-6 (8 min)**: Abertura — destacar a urgência (incidentes reais)
- [ ] **Slide 5**: Fazer a pergunta de tensão ("Qual o pior que pode acontecer?")
- [ ] **Slide 6**: Conectar incidentes reais com a realidade dos alunos
- [ ] **Slide 8**: Anotar superfícies que a turma não havia considerado
- [ ] **Slide 9**: Mostrar STRIDE adaptado — garantir que todos entendem as 6 categorias
- [ ] **Slide 11**: Destacar multi-agente como risco exponencial
- [ ] **Slide 12**: Diagrama threat model — ponto de referência para o projeto
- [ ] **Slide 14 (3 min)**: Exercício de threat modeling em duplas
- [ ] **Slide 16**: Explicar o problema fundamental (sem separação instr/dados) com calma
- [ ] **Slide 18**: Injeção indireta — destacar que usuário é vítima, não atacante
- [ ] **Slide 21**: Many-shot — destacar a ironia (modelos maiores = mais vulneráveis)
- [ ] **Slide 26 (3 min)**: DEMO AO VIVO — se API falhar, usar screenshots do Lab1
- [ ] **Slide 27 (2 min)**: Discussão da DEMO em duplas
- [ ] **Slide 29-30**: Guardrails input/output — conectar com defense in depth
- [ ] **Slide 34**: Diagrama defense in depth — segundo ponto de referência
- [ ] **Slide 36 (3 min)**: Exercício de camadas de defesa em duplas
- [ ] Intervalo (5 min)

### Bloco 2 (45 min)
- [ ] **Slide 39**: HITL — quando exigir; destacar regra "custo do erro > custo da espera"
- [ ] **Slide 41**: UX de HITL — anti-pattern fatiga de aprovação
- [ ] **Slide 43**: Diagrama HITL checkpoints — terceiro ponto de referência
- [ ] **Slide 44**: V/F HITL sozinho — quebrar o mito
- [ ] **Slide 46**: 6 categorias de red team — garantir cobertura mental
- [ ] **Slide 49-50**: AgentDojo e InjecAgent — destacar trade-off utility × security
- [ ] **Slide 51**: Garak/PyRIT — enfatizar uso em CI, não só pontual
- [ ] **Slide 54 (3 min)**: Exercício de casos de red team em duplas
- [ ] **Slide 55**: V/F modelos maiores — quebrar o mito
- [ ] **Slide 57-58**: OPA/Rego — mostrar política concreta
- [ ] **Slide 60**: LGPD/EU AI Act — destacar multas e obrigações
- [ ] **Slide 63 (3 min)**: Exercício de política OPA em duplas
- [ ] **Slide 65-66**: Boas práticas e anti-patterns — pedir exemplos da turma
- [ ] **Slide 67**: Casos reais — conectar com cada defesa que faltava
- [ ] **Slide 70-74 (5 min)**: Quiz — individual, sem consulta
- [ ] **Slide 75**: Perguntas de discussão se houver tempo
- [ ] **Slide 76**: Projeto e labs — esclarecer critérios
- [ ] **Slide 77 (2 min)**: Q&A

---

## Pós-Aula

### Avaliação
- [ ] Contar resultados do quiz (≥3 acertos = compreensão básica)
- [ ] Anotar perguntas frequentes no Q&A para futuras iterações
- [ ] Pedir feedback informal: "Uma vulnerabilidade que você não considerava antes"
- [ ] Verificar tempo real vs planejado por seção
- [ ] Avaliar qualidade dos exercícios em duplas (Slides 14, 36, 54, 63)

### Follow-up
- [ ] Enviar leitura recomendada no Slack/email (OWASP, Greshake)
- [ ] Disponibilizar slides (PDF + repositório)
- [ ] Lembrar prazo do Lab 1 (Red Team RAG — 1 semana)
- [ ] Lembrar prazo do Projeto (red team completo — 2 semanas)
- [ ] Preparar ETHAGT14 (Escalabilidade & Performance — próxima aula)
- [ ] Disponibilizar templates de ADR e política Rego para o projeto

---

## Sinais de Alerta Durante a Aula

| Sinal | Ação |
|---|---|
| Alunos confusos no Slide 9 (STRIDE) | Simplificar: focar só em Information Disclosure + Elevation of Privilege |
| Alunos confusos no Slide 16 (sem separação instr/dados) | Usar analogia da sala de reunião; dar exemplo concreto de SQL prepared statement vs prompt |
| DEMO falha (Slide 26) | Screenshot do Lab1 pré-gravado + seguir; não pular a discussão (Slide 27) |
| Tempo estourado no Bloco 1 | Cortar exercício do Slide 36 (camadas de defesa); mover para homework |
| Tempo estourado no Bloco 2 | Reduzir quiz para 3 perguntas (Slides 70-72); governança como leitura |
| Exercício OPA (Slide 63) muito lento | Mostrar política pré-escrita do Slide 58 e focar na discussão |
| Nenhuma pergunta no Q&A | Fazer pergunta inversa: "Qual parte foi menos clara?" ou "Qual vulnerabilidade mais te preocupou?" |
| Alunos sem pré-requisito de ETHAGT12 | Recap rápido de traces/observabilidade no Slide 5 (5 min extra) |
| Alunos acham que "isto é responsabilidade do time de security" | Reforçar Slide 1 notas: em agentes LLM, segurança é de quem escreve prompt e define tools |
