# ETHAGT15 — Perguntas para Discussão

> Perguntas para estimular debate durante e após a aula.
> Organizadas por profundidade: rápida (1-2 min) → média (3-5 min) → profunda (10+ min).

---

## Perguntas Rápidas (1-2 min)

### Q1 — Auto-Modificação de Prompt
"Você deixaria um agente modificar o próprio prompt? Em quais condições?"
- **Objetivo**: Calibrar atitude da turma sobre auto-modificação
- **Slide**: 5, 13
- **Resposta esperada**: A maioria hesita. Resposta correta: sim, com sandbox + eval + governor + HITL.

### Q2 — Identificar Meta-Agência
"Qual destes é meta-agência: agente que escreve código, agente que gera prompt para outro, agente que busca na web?"
- **Objetivo**: Fixar definição
- **Slide**: 14
- **Resposta esperada**: Só "agente que gera prompt para outro" é meta-agência.

### Q3 — Experiência com Otimização
"Quem aqui já usou DSPy, Promptbreeder ou similar em produção?"
- **Objetivo**: Calibrar experiência
- **Slide**: 27
- **Ação**: Contar mãos levantadas

### Q4 — Goal Drift na Vida Real
"Vocês já viram um sistema onde a métrica subiu mas o resultado real piorou?"
- **Objetivo**: Conectar conceito com experiência
- **Slide**: 48
- **Resposta esperada**: Exemplos comuns: YouTube recommender, KPIs de vendas, métricas de SLA.

---

## Perguntas Médias (3-5 min)

### Q5 — Quando Otimizar vs Reescrever
"Para o sistema de vocês hoje: otimização automatizada ou reescrita manual? Por quê?"
- **Objetivo**: Aplicar trade-offs ao caso real
- **Slide**: 35
- **Dica**: Usar volume, clareza da métrica e domínio como critérios

### Q6 — Validar Agente Gerado
"Como garantir que um agente gerado por meta-agente não é pior que um manual?"
- **Objetivo**: Pensar em benchmarking comparativo
- **Slide**: 19, 22
- **Resposta esperada**: Benchmark comparativo — rode ambos no mesmo eval. E holdout set que o meta-agente não vê.

### Q7 — Overfitting ao Eval
"O meta-agente otimiza para passar no eval. Como detectar overfitting?"
- **Objetivo**: Pensar em validação além do eval
- **Slide**: 22
- **Resposta esperada**: Holdout set, shadow run, monitoramento em produção, distribuição diferente de inputs.

### Q8 — Drift no Sistema Real
"O sistema de vocês tem drift? Como detectam?"
- **Objetivo**: Conectar drift com a realidade deles
- **Slide**: 41, 43
- **Ação**: Deixar 1-2 alunos compartilharem experiências

---

## Perguntas Profundas (10+ min)

### Q9 — Quando um Meta-Agente Se Torna Perigoso?
"Em que ponto um meta-agente se torna perigoso? Listem 3 sinais de alerta."
- **Objetivo**: Pensamento crítico sobre limites
- **Slide**: 54
- **Resposta esperada**: Pode modificar suas regras de segurança, pode escolher sua métrica, não tem HITL, pode escalar sem canary. Fórmula: perigo = capacidade × autonomia × falta de oversight.

### Q10 — Governor Também é Agente?
"Se o meta-governor também for um agente LLM, quem governa o governor? Como evitar regressão infinita?"
- **Objetivo**: Pensar sobre separação de poderes
- **Slide**: 53
- **Resposta esperada**: Governors críticos devem ser determinísticos (código, não LLM). Quando são LLM, precisam de governor-meta, idealmente humano. Regressão infinita é um risco real — por isso regras de veto devem ser policy-as-code.

### Q11 — Auto-Aprendizado Sempre Melhora?
"Defendam ou refutem: 'auto-aprendizado contínuo sempre melhora o sistema.'"
- **Objetivo**: Desafiar mito
- **Slide**: 44
- **Resposta esperada**: Falso. Overfitting, drift não detectado, loop de feedback positivo (jogar a métrica), catastrophic forgetting. Precisa de monitoramento, validação e reset.

### Q12 — Meta-Governor na Prática
"Pensem no sistema de vocês. Quais 3 regras de veto vocês implementariam primeiro?"
- **Objetivo**: Aplicar governance ao caso real
- **Slide**: 52, 53
- **Ação**: Em trios, 5 min. Compartilhar as 3 mais criativas. Exemplos: nunca remover safety constraints, nunca aumentar custo >10%, nunca mudar modelo não-aprovado.

---

## Perguntas Bônus (para alunos avançados)

### Q13 — DSPy vs Promptbreeder vs Fine-Tuning
"Qual a diferença entre DSPy, Promptbreeder e fine-tuning? Quando usar cada um?"
- **Objetivo**: Clarificar técnicas ortogonais
- **Resposta**: DSPy otimiza prompts via busca bayesiana (compilação). Promptbreeder otimiza via evolução (genético). Fine-tuning treina pesos do modelo. São ortogonais — pode combinar os três. Use DSPy para pipelines declarativos, Promptbreeder para exploração evolutiva, fine-tuning para adaptação profunda de domínio.

### Q14 — Voyager em Produção
"Voyager funciona no Minecraft. O que precisaria mudar para aplicar em um sistema de suporte ao cliente?"
- **Objetivo**: Pensar sobre transferência de ambiente controlado para real
- **Resposta**: Ambiente não é sandboxed (clientes reais), feedback não é determinístico (satisfação é subjetiva), skills não são código puro (envolvem tom, empatia), há consequências reais (perda de cliente). Precisa adaptar: sandbox para treino, métricas proxys claras, skills auditáveis, HITL para casos críticos.

### Q15 — Recursão de Meta-Agentes
"Um meta-agente cria um meta-agente que cria um meta-agente. Em que nível isso para? Quem decide?"
- **Objetivo**: Pensar sobre limites de recursão
- **Resposta**: Na prática, 2 níveis bastam (agente → meta-agente). Nível 3+ adiciona complexidade exponencial sem benefício proporcional. Quem decide é o arquiteto do sistema, via max_depth no meta-agente. Recursão infinita é um anti-pattern — cada nível precisa de governor separado.
