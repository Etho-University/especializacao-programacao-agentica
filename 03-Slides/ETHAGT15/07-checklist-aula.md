# ETHAGT15 — Checklist da Aula

> Checklist para o professor verificar antes, durante e depois da aula.

---

## Pré-Aula (24h antes)

### Preparação Técnica
- [ ] API key (OpenAI ou Anthropic) testada e funcionando
- [ ] Python 3.11+ instalado com dependências (`openai`, `dspy` opcional)
- [ ] VS Code aberto com `05-Labs/ETHAGT15/Lab1-Agente-que-Escreve-Agente`
- [ ] Terminal testado: `python main.py` executa sem erro
- [ ] Screenshot da config JSON gerada + eval salvo (plano B se API falhar)
- [ ] Projetor testado
- [ ] Slides exportados para PDF (plano B se apresentação falhar)
- [ ] Diagramas `.mmd` renderizados ou convertidos para imagem

### Preparação de Conteúdo
- [ ] Revisar todas as notas do professor (67 slides)
- [ ] Ensaiar a DEMO (Slide 21) — rodar pelo menos 2x antes
- [ ] Preparar o exercício de meta-governor (Slide 53) — template impresso
- [ ] Confirmar que todos os diagramas estão legíveis
- [ ] Preparar handout (opcional): storyboard impresso
- [ ] Revisar papers canônicos (DSPy, Promptbreeder, Voyager, AI Scientist)

### Preparação de Logística
- [ ] Sala reservada para 90 min + 15 min de buffer
- [ ] Quadro branco disponível (para diagramas de safety fences)
- [ ] Acesso ao repositório da especialização confirmado
- [ ] Cronômetro ou app de timer para exercícios cronometrados

---

## Durante a Aula

### Bloco 1 (45 min)
- [ ] **Slide 1-6 (8 min)**: Abertura — anotar votação do Slide 13
- [ ] **Slide 5**: Pergunta provocativa — "Você deixaria um agente modificar o próprio prompt?"
- [ ] **Slide 8**: Garantir que todos entendem a hierarquia meta→agente→ambiente
- [ ] **Slide 9**: Destacar as 3 estratégias — synthesis/evolution/optimization
- [ ] **Slide 10**: Diagrama meta-agent.mmd — destacar loop de validação
- [ ] **Slide 13**: Votação sim/não/depende — anotar resultado
- [ ] **Slide 14**: Exercício rápido de identificação — votação por cenário
- [ ] **Slide 18**: Pipeline de geração — enfatizar validação como gargalo
- [ ] **Slide 21 (5 min)**: DEMO AO VIVO — se API falhar, usar screenshot
- [ ] **Slide 22**: Perguntas da demo — 2 min em duplas
- [ ] **Slide 23**: Exercício critérios de qualidade — 3 min em duplas
- [ ] Intervalo (5 min)

### Bloco 2 (45 min)
- [ ] **Slide 25-30 (9 min)**: DSPy, Promptbreeder, Atlas, OPRO, TextGrad
- [ ] **Slide 33**: Diagrama evolution-loop.mmd — destacar HITL
- [ ] **Slide 35**: Discussão "quando otimizar" — 2 min aberta
- [ ] **Slide 37-39 (5 min)**: Memória, reflexion sistêmico, strategy evolver
- [ ] **Slide 40**: Voyager — destacar por que é seguro (ambiente fechado)
- [ ] **Slide 41-43**: Drift — exercício em duplas
- [ ] **Slide 44**: V/F "auto-aprendizado sempre melhora" — revelar FALSO
- [ ] **Slide 47-48**: Recursão e goal drift — riscos centrais
- [ ] **Slide 49-50**: Meta-governor + safety-fences.mmd — blueprint de segurança
- [ ] **Slide 52**: Vetos — mostrar snippet policy-as-code
- [ ] **Slide 53 (5 min)**: Exercício projetar meta-governor em trios
- [ ] **Slide 54**: Discussão "quando meta-agente é perigoso" — 2 min
- [ ] **Slide 57-58**: DO e DON'T — pedir exemplos da turma
- [ ] **Slide 61-63 (3 min)**: Quiz — individual, sem consulta
- [ ] **Slide 64**: Perguntas de discussão se houver tempo
- [ ] **Slide 66**: Projeto e labs — lembrar prazos
- [ ] **Slide 67 (2 min)**: Q&A

---

## Pós-Aula

### Avaliação
- [ ] Contar resultados do quiz (≥2 acertos = compreensão básica)
- [ ] Anotar as regras de veto mais criativas do Slide 53
- [ ] Anotar perguntas frequentes no Q&A para futuras iterações
- [ ] Pedir feedback informal: "Uma técnica de otimização que você aprendeu hoje"
- [ ] Verificar tempo real vs planejado por seção

### Follow-up
- [ ] Enviar leitura recomendada no Slack/email (DSPy, Promptbreeder)
- [ ] Disponibilizar slides (PDF + repositório)
- [ ] Lembrar prazo do Lab 1 (1 semana): "Agente que escreve agente"
- [ ] Lembrar prazo do Projeto (2 semanas): otimização automática + benchmark
- [ ] Preparar ETHAGT16 (Sociedades de Agentes)

---

## Sinais de Alerta Durante a Aula

| Sinal | Ação |
|---|---|
| Alunos confusos na distinção synthesis/evolution/optimization (Slide 9) | Simplificar: usar só synthesis vs optimization com exemplos |
| DEMO falha (Slide 21) | Screenshot da config JSON + eval pré-gravado |
| Tempo estourado no Bloco 1 | Cortar exercício do Slide 14; mover para homework |
| Tempo estourado no Bloco 2 | Reduzir quiz para 1 pergunta (Slide 61); referências como leitura |
| Debate acalorado sobre perigo de AGI (Slide 54) | Redirecionar para mitigações concretas (safety fences); levar ao fórum |
| Nenhuma pergunta no Q&A | Fazer pergunta inversa: "Qual parte foi menos clara?" |
| Trios criam governors muito permissivos (Slide 53) | Reenfatizar: veto é binário, sem "exceto se" |
| Alunos sem ETHAGT10 | Recaptular eval, memória e multi-agente em 2 min |
