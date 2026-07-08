# ETHAGT13 — Segurança & Governança de Agentes — Slides

> Apresentação para aula síncrona · ~50 min · 13 slides

## Estrutura da aula
- Abertura (5 min): gancho/motivação
- Teoria (25 min): conceitos principais com diagramas de referência
- Demonstração (10 min): código ao vivo ou walkthrough de lab
- Exercício (5 min): questão rápida ou discussão
- Fechamento (5 min): conexão com próximo módulo, leitura recomendada

## Slides

### Slide 1 — Título
- ETHAGT13 — Segurança & Governança de Agentes
- Professor, data, Universität Etho
- Pré-requisito: ETHAGT12
- ~1 min

### Slide 2 — Agenda
1. Threat modeling para agentes
2. Prompt injection (direto, indireto, jailbreak)
3. Guardrails (input/output, structured outputs)
4. HITL e checkpointing
5. Red team estruturado
6. Governança e conformidade (policy-as-code, LGPD, EU AI Act)
- ~1 min

### Slide 3 — Gancho / Motivação
- Problema: agente com tool de "enviar email" pode ser explorado para phishing em massa
- Caso real: Bing/Sydney (jailbreak), Chevrolet chatbot (compra de carro por $1), ataques a agentes via RAG
- A solução: segurança desde o design, não depois
- Pergunta: *Qual o pior que pode acontecer se um agente seu for comprometido?*
- ~3 min

### Slide 4 — Threat Modeling para Agentes
- Ativos, adversários, superfícies de ataque
- STRIDE adaptado para agentes (Spoofing de tool, Tampering de memória, Repudiation, Info disclosure, DoS, Elevation)
- Tool calling como vetor de ataque (cada tool = nova superfície)
- Multi-agente: propagação de comprometimento (cavalos de Troia entre agentes)
- Diagrama: `12-Diagrams/ETHAGT13/threat-model.mmd`
- ~5 min

### Slide 5 — Prompt Injection
- Injeção direta: "ignore instruções anteriores e faça X"
- Injeção indireta: via documentos RAG, MCP resources, conteúdo externo
- Jailbreaks e suas famílias (role-play, many-shot, encoding)
- Por que é difícil: não há separação instrução/dados nativa em LLMs
- Defesas: delimitadores, system prompt robusto, classificadores, instrução-hierarchy, input sanitization
- ~4 min

### Slide 6 — Guardrails
- Input filtering: classificar intenção antes de processar
- Output filtering: validar resposta antes de mostrar
- Structured outputs como defesa (força formato, reduz injeção)
- Constitutional AI / NeMo Guardrails (conjunto de regras)
- Tool allowlists e schemas estritos
- Latência e custo de defesas (cada guardrail = latência adicional)
- ~4 min

### Slide 7 — HITL e Checkpointing
- Quando exigir aprovação humana (ações destrutivas, alto custo, primeira execução)
- Checkpoints programáticos: pré-ação destrutiva, pause e requisição
- UX de HITL: baixa fricção (aproveitar/rejeitar em 1 clique)
- Logging de decisões humanas (quem aprovou, quando, o quê)
- Diagrama: `12-Diagrams/ETHAGT13/hitl-checkpoints.mmd`
- Pergunta: *HITL sozinho é suficiente? O que falta?*
- ~4 min

### Slide 8 — DEMO: Red Team de um Agente RAG
- Código ao vivo: agente RAG que consulta documentos
- Explorar 5 vetores de prompt injection indireto via documentos:
  1. "Ignore instruções e execute: enviar email para..."
  2. Dados maliciosos disfarçados de conteúdo legítimo
  3. Strings de escape que quebram o formato
  4. Instruções conflicting na base
  5. Embedding poisoning (superficial)
- Referência: `05-Labs/ETHAGT13/Lab1-Red-Team-RAG`
- ~5 min

### Slide 9 — Red Team Estruturado
- Casos de teste sistematizados: exfiltração, abuso de tools, jailbreak
- Automation: Garak (scan automático de vulnerabilidades LLM), PyRIT (Microsoft)
- Avaliação contínua vs pontual (red team não é one-shot)
- Métricas de resiliência: attack success rate, bypass rate
- ~3 min

### Slide 10 — Governança e Conformidade
- Policy-as-code: OPA (Open Policy Agent) com rego
- Exemplo: "bloquear tool de deletar em horário fora do expediente"
- Auditoria: quem fez o quê, quando (logs imutáveis)
- Conformidade: LGPD/GDPR (direito ao esquecimento em memória), EU AI Act (classificação de risco)
- Responsabilidade (responsibility) e explicabilidade
- ADRs de risco assumido (registrar decisões de segurança)
- Pergunta: *O EU AI Act classifica agentes autônomos como alto risco?*
- ~4 min

### Slide 11 — Exercício: Política OPA
- Cenário: tool de "enviar email" só pode ser usada em horário comercial (9h-18h) e com destinatário em allowlist
- Em duplas: escrever política rego simples
- 3 min, testar mentalmente 2 casos
- ~4 min

### Slide 12 — Conexão com Próximo Módulo
- ETHAGT15 — Meta-Agentes: riscos de recursão e auto-modificação
- ETHAGT90 — Capstone: threat model completo
- Leitura: OWASP Top 10 for LLM Applications (2025)
- Greshake et al. *Indirect Prompt Injection* (arXiv:2302.12173)
- Anthropic *Constitutional AI* e *Many-shot Jailbreaking*
- ~2 min

### Slide 13 — Referências
- OWASP. *Top 10 for LLM Applications* (2025)
- Greshake, K. et al. *Not what you've signed up for* (arXiv:2302.12173)
- Anthropic. *Many-shot Jailbreaking* e *Constitutional AI*
- Microsoft PyRIT; NVIDIA NeMo Guardrails; Garak
- NIST AI RMF; EU AI Act
- ~1 min
