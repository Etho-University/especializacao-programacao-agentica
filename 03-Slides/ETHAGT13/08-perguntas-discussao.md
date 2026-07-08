# ETHAGT13 — Perguntas para Discussão

> Perguntas para estimular debate durante e após a aula.
> Organizadas por profundidade: rápida (1-2 min) → média (3-5 min) → profunda (10+ min).

---

## Perguntas Rápidas (1-2 min)

### Q1 — Superfície de Ataque Não Considerada
"Qual superfície de ataque em agentes você não havia considerado antes desta aula?"
- **Objetivo**: Criar conscientização sobre a amplitude de vetores
- **Slide**: 8
- **Resposta esperada**: Costuma ser MCP resources, A2A (comunicação entre agentes), ou web search results. RAG é mais conhecido, mas MCP e A2A surpreendem.

### Q2 — Tool Mais Perigosa
"Qual das tools do seu agente atual é a mais perigosa se comprometida?"
- **Objetivo**: Fazer alunos pensarem sobre suas próprias tools sob ótica de risco
- **Slide**: 10
- **Resposta esperada**: Varia — mas geralmente tools de envio (email, mensagem), tools de execução (código, SQL), ou tools financeiras (transferência, reembolso).

### Q3 — Experiência com Incidente
"Alguém aqui já lidou com incidente de segurança envolvendo LLM ou agente? O que aconteceu?"
- **Objetivo**: Trazer experiência real para a sala
- **Slide**: 6
- **Ação**: Deixar 1-2 alunos compartilharem (anonimamente se necessário)

### Q4 — HITL na Prática
"Vocês têm HITL em algum sistema de LLM hoje? Funciona ou é rubber stamp?"
- **Objetivo**: Mostrar que HITL mal implementado é comum
- **Slide**: 41
- **Resposta esperada**: <30% tem HITL; dos que têm, muitos admitem fatiga de aprovação.

### Q5 — Conformidade Conhecida
"Vocês sabem se seu agente está em conformidade com LGPD? E EU AI Act?"
- **Objetivo**: Mostrar que a maioria não sabe — sinal de alerta
- **Slide**: 60
- **Resposta esperada**: A maioria não sabe ou assume que está. Raramente há análise formal.

---

## Perguntas Médias (3-5 min)

### Q6 — Defesa Contra Vetor Específico
"Como você defenderia contra o vetor #2 da DEMO (conteúdo legítimo com payload oculto)?"
- **Objetivo**: Aplicar defesas a caso concreto e difícil
- **Slide**: 27
- **Resposta esperada**: Output filter (validar que resposta não contém instrução), instruction hierarchy (tratar RAG como nível inferior), cross-validation (segunda fonte), e HITL em ações resultantes. Delimitadores sozinhos não bastam — o conteúdo parece legítimo.

### Q7 — Threat Model do Seu Sistema
"Pensem no sistema de vocês hoje: qual o ativo mais crítico? Qual a superfície mais exposta?"
- **Objetivo**: Aplicar threat modeling ao caso real
- **Slide**: 12
- **Ação**: Deixar 2-3 alunos compartilharem em 30s cada

### Q8 — Equilíbrio Utility × Security
"Seu agente tem utility 95% e security 60%. Você aceita? Ou derruba utility para subir security?"
- **Objetivo**: Praticar o trade-off quantificado pelo AgentDojo
- **Slide**: 49
- **Resposta esperada**: Depende do caso de uso. Em atendimento ao cliente, utility baixo = produto inútil. Em agente financeiro, security baixo = desastre. Calibre ao contexto.

### Q9 — HITL em Toda Tool?
"Toda tool deve ter HITL?" (V/F justificado)
- **Objetivo**: Quebrar a ideia de que HITL é sempre necessário
- **Slide**: 39
- **Resposta esperada**: **Falso**. HITL em toda tool mata UX e causa fatiga. HITL é proporcional ao risco: leitura não precisa, escrita depende, destrutiva sempre.

### Q10 — Convencendo o PM
"Como você convenceria um PM a investir em red team contínuo? Quais números usaria?"
- **Objetivo**: Estruturar argumentos de negócio para segurança
- **Slide**: 52
- **Resposta esperada**: Custo de incidente (multa LGPD até 2% faturamento, reputação) >> custo de red team (1 engenheiro + ferramentas open source). Usar casos reais (Chevrolet, Bing). Mostrar ASR atual vs meta.

### Q11 — LGPD na Memória
"Seu agente tem memória persistente. Como você implementa o direito ao esquecimento da LGPD?"
- **Objetivo**: Pensar na tensão entre memória e privacidade
- **Slide**: 60
- **Resposta esperada**: Difícil. Vector store precisa de index reverso (qual vetor pertence a qual usuário). Checkpointer precisa de cascade delete. Logs de auditoria têm tensão — pseudonimização é solução parcial. Não há bala de prata.

---

## Perguntas Profundas (10+ min)

### Q12 — O Mito do "Modelo Seguro"
"Por que o mito 'modelos maiores são mais seguros' persiste apesar da evidência? Como você combate isto na sua empresa?"
- **Objetivo**: Pensamento crítico sobre crenças populares
- **Slide**: 55
- **Resposta esperada**: Persiste porque modelos maiores parecem mais "inteligentes" e pessoas confundem inteligência com segurança. Combate-se com dados: mostrar AgentDojo (modelos frontier vulneráveis), many-shot (context window maior = mais vulnerável). Defesa vem de camadas, não de tamanho.
- **Contraponto**: Modelos maiores podem ter melhores alinhamentos de fábrica (Constitutional AI), mas não substituem defense in depth.

### Q13 — HITL como Falsa Segurança
"HITL pode dar falsa sensação de segurança. Como você detecta e corrige HITL que virou rubber stamp?"
- **Objetivo**: Identificar e corrigir falha sutil em HITL
- **Slide**: 41, 44
- **Resposta esperada**: Sinais: taxa de aprovação > 95%, tempo médio de revisão < 5s, humano não edita args. Correção: amostrar decisões e revisar manualmente, rotar humanos (evitar fadiga de um só), automatizar o que for seguro o suficiente, exigir justificativa em rejeições (não só aprovações).

### Q14 — Governança sem Burocracia
"Como você implementa policy-as-code (OPA) sem criar burocracia que mata a velocidade do time?"
- **Objetivo**: Equilibrar governança e agilidade
- **Slide**: 57
- **Resposta esperada**: Policy-as-code é justamente a solução — automação substitui burocracia. Regras em Rego rodam automaticamente, sem aprovação manual. Desenvolvedores escrevem políticas como código (code review, não comitê). CI valida políticas a cada PR. O que mata velocidade é reunião de aprovação; OPA elimina a reunião.

### Q15 — Defesa vs Inovação
"Defense in depth adiciona latência e custo. Em startup com recursos limitados, quais 3 camadas você implementa primeiro?"
- **Objetivo**: Priorização sob restrição
- **Slide**: 34
- **Resposta esperada**: Top 3 para começar: (1) Tool allowlist + schema estrito (baixo custo, alto impacto), (2) System prompt robusto + delimitadores (quase zero custo), (3) Output filter de PII (médio custo, previne vazamento). HITL vem depois que as 3 estão em vigor.

### Q16 — Incidente Real Próprio
"Se o seu agente fosse comprometido amanhã, qual seria o impacto? Quanto tempo levaria para detectar?"
- **Objetivo**: Mapear prontidão real
- **Slide**: 59
- **Ação**: Em duplas, 5 min para discutir. Compartilhar 2-3 cenários.
- **Resposta esperada**: A maioria não sabe a resposta. Sem logs imutáveis, detecção é lenta (dias/semanas). Sem auditoria, investigação é impossível. Este exercício motiva a Seção G.

---

## Perguntas Bônus (para alunos avançados)

### Q17 — Multi-Agente e Confiança Transitiva
"Em um sistema com 10 agentes, quantas fronteiras de confiança existem? Como você valida todas?"
- **Objetivo**: Quantificar o problema de multi-agente
- **Resposta**: 10 × 9 = 90 fronteiras direcionadas (ou 45 não-direcionadas). Cada fronteira precisa de validação de output (tratar outro agente como não-confiável). Em prática, usa-se allowlist de agentes + validação de schema de mensagem A2A.

### Q18 — Embedding Poisoning
"Como funciona embedding poisoning e por que é difícil de detectar?"
- **Objetivo**: Introduzir vetor avançado de ataque ao RAG
- **Resposta**: Atacante otimiza o documento para que seu embedding seja sempre recuperado (independente da query), e inclui payload. Detectar requer análise estatística de distribuição de retrievals, ou ensemble de retrievers. É vetor ativo de pesquisa.

### Q19 — Constitutional AI vs NeMo Guardrails
"Quando você escolhe Constitutional AI (treinamento) vs NeMo Guardrails (runtime)?"
- **Objetivo**: Decisão de arquitetura de defesa
- **Resposta**: Constitutional AI é proprietário do modelo (você não treina, escolhe Claude). NeMo é runtime (você implementa com qualquer modelo). Se usa modelo open source, NeMo é opção. Se usa Claude, Constitutional AI já está embutido. Complementares, não excludentes.

### Q20 — EU AI Act e Seu Agente
"Seu agente faz atendimento ao cliente com tools de CRM e email. O EU AI Act classifica como alto risco? Quais obrigações?"
- **Objetivo**: Aplicar regulamentação a caso concreto
- **Resposta**: Provavelmente sim — agentes autônomos com tools que afetam direitos de usuários (atendimento, decisões) tendem a "alto risco". Obrigações: documentação técnica, avaliação de risco, supervisão humana (HITL!), robustez e cybersecurity, registro de eventos. Multas até 7% faturamento global.
