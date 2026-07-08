# ETHAGT15 — Meta-Agentes & Sistemas Autoaprendentes
## Storyboard da Apresentação

> **Universidade Etho · Especialização em Programação Agêntica**
> Fase D — Fronteira · 15 h
> Storyboard v1.0 · Julho 2026

---

## Metadados da Apresentação

| Campo | Valor |
|---|---|
| Código | ETHAGT15 |
| Título | Meta-Agentes & Sistemas Autoaprendentes (agents that build agents) |
| Duração estimada | 90 min (2 blocos de 45 min) |
| Total de slides | 67 |
| Público | Arquitetos, Engenheiros de Software, Engenheiros de IA, Tech Leads, Pesquisadores |
| Pré-requisitos | ETHAGT10 |
| Competências | C1 (A), C2 (A), C3 (B), C4 (A), C6 (I) |

---

## Mapa Visual da Apresentação

```
BLOCO 1 (45 min)                              BLOCO 2 (45 min)
┌──────────────────────────────┐              ┌──────────────────────────────┐
│ SEÇÃO A — Abertura (8 min)   │              │ SEÇÃO D — Otimização (15 min)│
│  Capa · Objetivos · Agenda   │              │  DSPy · Promptbreeder · Atlas│
│  Motivação · Contexto        │              │  Tools · Topologia · Loop    │
├──────────────────────────────┤              ├──────────────────────────────┤
│ SEÇÃO B — Meta-Agência (12m) │              │ SEÇÃO E — Auto-Aprend (13 m) │
│  Agentes sobre agentes       │              │  Memória · Reflexion · Evolver│
│  Estratégias · Risco × Benef.│              │  Voyager · Drift · Esquecer  │
├──────────────────────────────┤              ├──────────────────────────────┤
│ SEÇÃO C — Geração (15 min)   │              │ SEÇÃO F — Riscos (12 min)    │
│  Meta-agente · Templates     │              │  Recursão · Goal drift       │
│  Validação · DEMO            │              │  Meta-governor · Vetos       │
│                              │              ├──────────────────────────────┤
│                              │              │ SEÇÃO G — Fechamento (10 min)│
│                              │              │  Boas práticas · Quiz · Refs │
└──────────────────────────────┘              └──────────────────────────────┘
```

---

## Storyboard Detalhado

### SEÇÃO A — Abertura (Slides 1-6 · 8 min)

---

#### Slide 1 — Capa
- **Tipo**: Capa
- **Objetivo**: Identificar a aula, professor e contexto
- **Conteúdo**:
  - ETHAGT15 — Meta-Agentes & Sistemas Autoaprendentes
  - Universidade Etho · Especialização em Programação Agêntica
  - Fase D — Fronteira
  - Professor · Data
- **Diagrama**: Logo Etho + imagem de fundo abstrata (agentes gerando agentes, recursão visual)
- **Animação**: Fade in do título
- **Tempo**: 1 min

---

#### Slide 2 — Objetivos do Módulo
- **Tipo**: Conteúdo
- **Objetivo**: Deixar claro o que o aluno deve conseguir fazer ao final
- **Conteúdo**:
  - Objetivo geral: Explorar a fronteira dos meta-agentes — agentes que criam, otimizam e evoluem outros agentes — com conscientização dos riscos
  - 5 objetivos específicos (1 linha cada):
    1. Definir meta-agente, strategy evolver, meta-learning para agentes
    2. Implementar um sistema onde um agente gera/configura agentes especializados
    3. Aplicar otimização automatizada de prompts/tools
    4. Discutir auto-aprendizado contínuo com memória acumulada
    5. Identificar riscos (recursão, drift, segurança) e mitigações
- **Diagrama**: Ícones representando cada objetivo
- **Animação**: Aparecer objetivos um a um (on click)
- **Tempo**: 2 min

---

#### Slide 3 — Competências Desenvolvidas
- **Tipo**: Conteúdo
- **Objetivo**: Conectar a aula ao Framework Etho de competências
- **Conteúdo**:
  - Tabela: 5 competências com nível B/I/A
  - C1 Programação Agêntica → A
  - C2 Multi-Agent Systems → A
  - C3 MCP & Tool Use → B
  - C4 Agent Memory → A
  - C6 Agent Security → I
  - Badge visual por competência
- **Diagrama**: Radar chart dos 5 pilares
- **Animação**: Radar aparece com wipe
- **Tempo**: 1 min

---

#### Slide 4 — Agenda
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar o roteiro da aula com tempos
- **Conteúdo**:
  - Bloco 1: Abertura → Meta-Agência → Geração de Agentes
  - Bloco 2: Otimização → Auto-Aprendizado → Riscos → Fechamento
  - Tempos estimados por seção
- **Diagrama**: Timeline horizontal com 7 seções
- **Animação**: Timeline cresce da esquerda para direita
- **Tempo**: 1 min

---

#### Slide 5 — Motivação: A Fronteira dos Meta-Agentes
- **Tipo**: Conteúdo
- **Objetivo**: Criar tensão — otimização manual não escala
- **Conteúdo**:
  - Prompts e ferramentas são otimizados manualmente — escala não
  - Equipe de 5 engenheiros mantendo prompts de 20 agentes → impraticável
  - Cada novo domínio = novo agente manual = semanas de trabalho
  - A solução: meta-agente que otimiza automaticamente
  - Fronteira: agente que cria outro agente — onde está o limite?
  - Pergunta: *Você deixaria um agente modificar o próprio prompt?*
- **Diagrama**: Antes (engenheiros escrevendo prompts manualmente) vs Depois (meta-agente gerando)
- **Animação**: Split — lado esquerdo (manual, lento), depois lado direito (automático, rápido)
- **Tempo**: 2 min

---

#### Slide 6 — Contexto: Por Que Meta-Agência Agora
- **Tipo**: Conteúdo
- **Objetivo**: Explicar a confluência que tornou meta-agentes viáveis
- **Conteúdo**:
  - Linha do tempo: 2023 (DSPy) → 2023 (Voyager) → 2023 (Promptbreeder) → 2024 (Meta-Prompting) → 2025 (adoção)
  - Confluência: modelos capazes de gerar código/config + frameworks de eval + necessidade de escala
  - DSPy: compilação declarativa de chamadas de LLM (arXiv:2310.03714)
  - Voyager: agente que aprende skills automaticamente (arXiv:2305.16291)
  - Meta-Prompting: decomposição com especialistas (arXiv:2311.11402)
- **Diagrama**: Timeline horizontal com marcos
- **Animação**: Marcos aparecem sequencialmente
- **Tempo**: 1 min

---

### SEÇÃO B — O Que É Meta-Agência (Slides 7-14 · 12 min)

---

#### Slide 7 — [SEÇÃO] O Que É Meta-Agência
- **Tipo**: Seção
- **Objetivo**: Transição para o bloco de fundamentos
- **Conteúdo**: Número "1" grande + "O Que É Meta-Agência"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 8 — Agentes que Operam sobre Agentes
- **Tipo**: Conteúdo
- **Objetivo**: Definir meta-agência e distinguir de agência comum
- **Conteúdo**:
  - Agente comum: opera sobre o ambiente (tools, APIs, dados)
  - Meta-agente: opera sobre agentes (criar, configurar, otimizar, evoluir)
  - Meta-agente é um agente cujo "ambiente" é outro agente
  - Analogia: compilador é para código o que meta-agente é para agente
  - Níveis de meta: agente → meta-agente → meta-meta-agente (cuidado com recursão)
- **Diagrama**: Hierarquia: meta-agente → agentes → ambiente
- **Animação**: Níveis aparecem de cima para baixo
- **Tempo**: 2 min

---

#### Slide 9 — Estratégias: Synthesis, Evolution, Optimization
- **Tipo**: Comparação
- **Objetivo**: Apresentar as 3 estratégias de meta-agência
- **Conteúdo**:
  - Synthesis: criar um agente do zero para uma tarefa específica
    - Exemplo: meta-agente recebe "preciso de um agente de suporte para produto X"
  - Evolution: mutar a configuração de um agente existente
    - Exemplo: trocar modelo, adicionar tool, mudar prompt
  - Optimization: ajustar parâmetros finos sem mudar estrutura
    - Exemplo: otimizar prompt com DSPy, ajustar temperatura
  - Cada estratégia tem nível crescente de risco e reward
- **Diagrama**: 3 colunas comparativas (Synthesis / Evolution / Optimization)
- **Animação**: Colunas aparecem uma a uma
- **Tempo**: 2 min

---

#### Slide 10 — Meta-Agente: Arquitetura Conceitual
- **Tipo**: Diagrama
- **Objetivo**: Visualizar a arquitetura de um meta-agente
- **Conteúdo**:
  - tarefa T → Meta-agente → compõe primitivas (personas, tools, workflows)
  - → gera config JSON → validar → passa: instanciar / falha: iterar
  - → executar T
  - O meta-agente usa um LLM para gerar configuração declarativa
  - Validação é crítica: eval antes de deploy
- **Diagrama**: `12-Diagrams/ETHAGT15/meta-agent.mmd`
- **Animação**: Fluxo percorre o diagrama, loop de validação destacado
- **Tempo**: 3 min

---

#### Slide 11 — Exemplos: DSPy, Voyager, Meta-Prompting
- **Tipo**: Conteúdo
- **Objetivo**: Conectar conceito a implementações reais
- **Conteúdo**:
  - DSPy (Khattab et al.): compilação declarativa — otimiza prompts automaticamente
  - Voyager (Wang et al.): agente que aprende skills no Minecraft — auto-curriculum
  - Meta-Prompting (Hu et al.): decomposição de tarefa com especialistas LLM
  - Promptbreeder (Fernando et al.): evolução de prompts via mutação + seleção
  - Padrão comum: loop de gerar → avaliar → selecionar → iterar
- **Diagrama**: 4 cards com nome, ano, contribuição
- **Animação**: Cards aparecem um a um
- **Tempo**: 2 min

---

#### Slide 12 — Risco vs Benefício
- **Tipo**: Comparação
- **Objetivo**: Ser honesto sobre os trade-offs da meta-agência
- **Conteúdo**:
  - Benefícios:
    - Escala: otimizar 100 agentes automaticamente
    - Adaptação: ajustar a mudanças de domínio
    - Descoberta: encontrar configurações que humanos não pensariam
  - Riscos:
    - Perda de controle: agente otimiza métrica errada
    - Recursão: loops de auto-modificação sem convergência
    - Opacidade: difícil entender por que a config é assim
    - Drift: otimizando para ambiente antigo
- **Diagrama**: Balança: benefícios vs riscos
- **Animação**: Balança inclina para cada lado conforme itens aparecem
- **Tempo**: 2 min

---

#### Slide 13 — Pergunta: Você Deixaria um Agente Modificar o Próprio Prompt?
- **Tipo**: Exercício
- **Objetivo**: Engajar a turma com uma pergunta provocativa
- **Conteúdo**:
  - "Você deixaria um agente modificar o próprio prompt?"
  - Votação: sim / não / depende
  - "Em que condições você aceitaria?"
  - "Quem audita as mudanças?"
  - Discussão aberta (2 min)
- **Diagrama**: Caixa de votação (sim/não/depende)
- **Tempo**: 2 min

---

#### Slide 14 — Exercício Rápido: Identificar Meta-Agência
- **Tipo**: Exercício
- **Objetivo**: Praticar identificação de meta-agência em cenários
- **Conteúdo**:
  - 4 cenários — quais são meta-agência?
    1. Agente que escreve código Python → NÃO (agência comum)
    2. Agente que gera prompt para outro agente → SIM (synthesis)
    3. Agente que ajusta sua própria temperatura → SIM (optimization)
    4. Agente que busca na web → NÃO (agência comum)
  - Votação rápida
- **Diagrama**: 4 cards com cenários
- **Tempo**: 1.5 min

---

### SEÇÃO C — Geração de Agentes (Slides 15-24 · 15 min)

---

#### Slide 15 — [SEÇÃO] Geração de Agentes
- **Tipo**: Seção
- **Objetivo**: Transição para geração de agentes
- **Conteúdo**: "2 — Geração de Agentes"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 16 — Meta-Agente que Produz Agentes
- **Tipo**: Conteúdo
- **Objetivo**: Detalhar como um meta-agente gera agentes especializados
- **Conteúdo**:
  - Input: descrição de tarefa ("preciso de um agente que responda dúvidas de produto X")
  - Output: config completa (system prompt, tools, modelo, parâmetros)
  - O meta-agente usa primitivas reutilizáveis:
    - Personas (template de system prompt)
    - Tools (biblioteca de tools MCP)
    - Workflows (padrões de orquestração)
  - Composição: selecionar primitivas + instanciar + configurar
- **Diagrama**: Input → meta-agente → primitivas → config → agente especializado
- **Tempo**: 2 min

---

#### Slide 17 — Templates e Composição
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar como templates tornam a geração reutilizável
- **Conteúdo**:
  - Template = configuração parametrizada de um agente
  - Exemplo: `SupportAgentTemplate(product, knowledge_base, escalation_policy)`
  - Composição: combinar templates (agente de suporte + agente de QA)
  - Biblioteca de templates: catálogo versionado de padrões
  - Vantagem: reuso, consistência, auditabilidade
  - Desafio: manter templates atualizados com mudanças de domínio
- **Diagrama**: Biblioteca de templates → composição → agente final
- **Tempo**: 2 min

---

#### Slide 18 — Pipeline de Geração
- **Tipo**: Diagrama
- **Objetivo**: Visualizar o pipeline completo de geração de agentes
- **Conteúdo**:
  - Passo 1: Interpretar tarefa (LLM analisa descrição)
  - Passo 2: Selecionar primitivas (da biblioteca)
  - Passo 3: Gerar config (JSON declarativo)
  - Passo 4: Validar (schema check + eval em sandbox)
  - Passo 5: Instanciar (criar agente executável)
  - Passo 6: Deploy (com confiança incremental)
  - Falha em qualquer passo → feedback → iterar
- **Diagrama**: Pipeline horizontal com 6 passos + loop de feedback
- **Animação**: Passos se preenchem sequencialmente, loop destacado em falha
- **Tempo**: 2 min

---

#### Slide 19 — Validação do Agente Gerado
- **Tipo**: Conteúdo
- **Objetivo**: Enfatizar que validação é crítica antes de deploy
- **Conteúdo**:
  - "Confie, mas verifique" — agent generated ≠ agent good
  - Validação automática:
    - Schema check (config é válida?)
    - Eval em subset de casos de teste (passa nos critérios?)
    - Safety check (não viola políticas?)
  - Validação humana:
    - Review da config gerada
    - Aprovação para mudanças críticas
  - Sem validação: agente pode ser pior que o manual
  - Pergunta: *Como garantir que o agente gerado não é pior que o manual?*
- **Diagrama**: Funil de validação: schema → eval → safety → review → deploy
- **Tempo**: 2 min

---

#### Slide 20 — Caso: Agentes de Suporte por Produto
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar um caso prático de geração
- **Conteúdo**:
  - Empresa com 10 produtos, cada um precisa de agente de suporte
  - Manual: 10 engenheiros × 2 semanas = 20 semanas
  - Com meta-agente: 1 engenheiro + meta-agente × 2 dias = 2 dias
  - Meta-agente recebe: descrição do produto + KB + política de escalonamento
  - Gera: system prompt + tools (search_kb, escalate, create_ticket) + config
  - Validação: 50 casos de teste por produto → aprovação automática se >90%
  - Resultado: 10 agentes em 2 dias, 92% de precisão média
- **Diagrama**: Antes (10 engenheiros, 20 semanas) vs Depois (1 engenheiro, 2 dias)
- **Tempo**: 2 min

---

#### Slide 21 — DEMO: Agente que Escreve Agente
- **Tipo**: Código
- **Objetivo**: Demo ao vivo — meta-agente que gera um agente especializado
- **Conteúdo**:
  - Código do `05-Labs/ETHAGT15/Lab1-Agente-que-Escreve-Agente`
  - Input: "preciso de um agente que classifique tickets de suporte"
  - Meta-agente gera: system prompt + tool de classificação + config
  - Avalia o agente gerado em 3 casos de teste
  - Mostra resultado: aprovado/reprovado → itera se necessário
  - Terminal: meta-agente → config JSON → eval → deploy
- **Diagrama**: Code block + terminal side-by-side
- **Animação**: Highlight de linhas chave; terminal mostra geração e eval
- **Tempo**: 5 min

---

#### Slide 22 — Pergunta da DEMO
- **Tipo**: Exercício
- **Objetivo**: Engajar a turma com uma pergunta sobre a demo
- **Conteúdo**:
  - "O agente gerado é pior que um agente escrito manualmente?"
  - "Como sabemos que o eval cobre casos suficientes?"
  - "E se o meta-agente gerar uma config que funciona no eval mas falha em produção?"
  - Discussão em duplas (2 min)
- **Diagrama**: Caixa de discussão
- **Tempo**: 2 min

---

#### Slide 23 — Exercício: Como Garantir Qualidade
- **Tipo**: Exercício
- **Objetivo**: Praticar critérios de qualidade para agentes gerados
- **Conteúdo**:
  - Em duplas: listar 5 critérios de qualidade para um agente gerado
  - Exemplos: success rate, latência, custo, safety, robustez a edge cases
  - Bônus: como detectar overfitting ao eval?
  - 2 min listar, 1 min compartilhar
- **Diagrama**: Caixa de exercício
- **Tempo**: 2 min

---

#### Slide 24 — Lições da Geração
- **Tipo**: Conteúdo
- **Objetivo**: Sintetizar os aprendizados da geração de agentes
- **Conteúdo**:
  - Geração é rápida, mas validação é o gargalo
  - Eval de qualidade é mais importante que velocidade de geração
  - Templates reduzem variabilidade e aumentam reuso
  - Comece com domínio estreito, expanda gradualmente
  - Human-in-the-loop para mudanças críticas
  - A config gerada deve ser auditável e versionada
- **Diagrama**: 6 ícones com as lições
- **Tempo**: 1 min

---

### SEÇÃO D — Otimização Automatizada (Slides 25-35 · 15 min)

---

#### Slide 25 — [SEÇÃO] Otimização Automatizada
- **Tipo**: Seção
- **Objetivo**: Transição para otimização
- **Conteúdo**: "3 — Otimização Automatizada"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 26 — Por Que Otimizar Automaticamente?
- **Tipo**: Conteúdo
- **Objetivo**: Justificar a necessidade de otimização automatizada
- **Conteúdo**:
  - Prompts manuais: arte, não ciência — dependem de intuição humana
  - Humanos são ruins em explorar espaço de prompts sistematicamente
  - Otimização automática: explora centenas de variações em horas
  - Encontra configurações que humanos não pensariam
  - Reprodutível: mesma otimização → mesmo resultado
  - Escala: otimizar 100 agentes em paralelo
- **Diagrama**: Espaço de busca humano (poucos pontos) vs automático (grade densa)
- **Tempo**: 1.5 min

---

#### Slide 27 — DSPy: Compilação Declarativa
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar DSPy como framework de otimização
- **Conteúdo**:
  - DSPy: "compilar" chamadas declarativas de LLM em prompts otimizados
  - Analogia: DSPy é para prompts o que um compilador é para código
  - Você escreve o QUE quer (assinatura), DSPy gera o COMO (prompt)
  - Assinatura: `question -> answer` (declarativo)
  - DSPy escolhe: few-shot examples, formato, instruções
  - Fonte: Khattab et al., arXiv:2310.03714
- **Diagrama**: Código declarativo → DSPy compiler → prompt otimizado
- **Tempo**: 2 min

---

#### Slide 28 — DSPy: Como Funciona (Teleprompters)
- **Tipo**: Conteúdo
- **Objetivo**: Detalhar o mecanismo de otimização do DSPy
- **Conteúdo**:
  - Teleprompter = otimizador do DSPy
  - BootstrapFewShot: seleciona melhores exemplos de treino
  - MIPRO: otimiza instruções + exemplos via busca bayesiana
  - Processo:
    1. Definir assinatura e métrica
    2. Fornecer dados de treino
    3. Teleprompter explora variações
    4. Avalia cada variação na métrica
    5. Retorna melhor config
  - Resultado: prompt otimizado sem intervenção humana manual
- **Diagrama**: Fluxo: assinatura + dados → teleprompter → prompt otimizado
- **Tempo**: 2 min

---

#### Slide 29 — Promptbreeder: Evolução de Prompts
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar Promptbreeder como abordagem evolutiva
- **Conteúdo**:
  - Promptbreeder: prompts "reproduzem" e "mutam"
  - População inicial de prompts → mutação (LLM reescreve) → seleção (eval)
  - Gerações sucessivas: prompts melhoram com evolução
  - Analogia: algoritmo genético onde genes = palavras do prompt
  - Mutação exemplo: "Responda a pergunta" → "Você é um especialista. Responda com precisão."
  - Fonte: Fernando et al., arXiv:2309.16797
- **Diagrama**: Ciclo evolutivo: população → mutação → seleção → nova população
- **Tempo**: 2 min

---

#### Slide 30 — Atlas e Outras Abordagens
- **Tipo**: Conteúdo
- **Objetivo**: Panorama de outras ferramentas de otimização
- **Conteúdo**:
  - Atlas: otimização guiada por árvore de pensamentos
  - OPRO (Google): otimização de prompts via meta-prompting
  - TextGrad: gradientes de texto para otimizar prompts
  - Padrão comum: gerar variações → avaliar → selecionar → iterar
  - Diferença principal: estratégia de busca (greedy, evolutiva, bayesiana)
  - Escolha depende: orçamento de eval, tamanho do espaço, tempo
- **Diagrama**: Tabela comparativa: DSPy vs Promptbreeder vs Atlas vs OPRO
- **Tempo**: 1.5 min

---

#### Slide 31 — Otimização de Tools (Reescrita de Descrições)
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar que tools também podem ser otimizadas
- **Conteúdo**:
  - Tool description afeta diretamente quando e como o modelo a chama
  - Descrição ruim → modelo não chama ou chama errado
  - Otimização: reescrever descrições baseada em taxa de erro
  - Exemplo: "Busca documentos" → "Busca documentos na base de conhecimento interna. Use para responder perguntas sobre produtos, políticas e procedimentos."
  - Métrica: tool call accuracy (chamou a tool certa?)
  - Loop: medir erro → reescrever descrição → re-avaliar
- **Diagrama**: Loop: descrição → eval → taxa de erro → reescrever → eval
- **Tempo**: 1.5 min

---

#### Slide 32 — Otimização de Topologia
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar otimização da estrutura do sistema multi-agente
- **Conteúdo**:
  - Topologia = como agentes estão conectados (qual chama qual)
  - Perguntas de topologia:
    - Preciso de N workers ou N-1?
    - Qual worker agrego? Qual removo?
    - Deveria ter um orchestrator ou peer-to-peer?
  - Otimização: testar topologias alternativas em benchmark
  - Exemplo: 5 workers → 3 workers + 2 especializados = mesma qualidade, menor custo
  - Desafio: espaço de topologias é enorme (combinatório)
- **Diagrama: Topologia A (5 workers) vs Topologia B (3 + 2) com métricas
- **Tempo**: 1.5 min

---

#### Slide 33 — Loop de Otimização
- **Tipo**: Diagrama
- **Objetivo**: Visualizar o loop de evolução (strategy evolver)
- **Conteúdo**:
  - estratégia atual → gerar variações → avaliar em subset → melhor que atual?
  - sim: substituir · não: manter atual
  - substituir → estratégia atual (loop)
  - HITL: audit periódico para prevenir drift
  - Padrão: mutação + seleção + retenção = evolução
- **Diagrama**: `12-Diagrams/ETHAGT15/evolution-loop.mmd`
- **Animação**: Loop percorre o diagrama, HITL aparece como checkpoint
- **Tempo**: 2 min

---

#### Slide 34 — Comparação: Manual vs Automatizado
- **Tipo**: Comparação
- **Objetivo**: Sistematizar os trade-offs
- **Conteúdo**:
  - Tabela: otimização manual vs automatizada
  - Eixos: velocidade, reprodutibilidade, exploração, custo de eval, controle, transparência
  - Manual: lento, não-reprodutível, exploração limitada, baixo custo de eval, alto controle, transparente
  - Automatizado: rápido, reprodutível, exploração ampla, alto custo de eval, médio controle, opaco
  - Recomendação: automatizar para volume, manual para edge cases
- **Diagrama**: Tabela comparativa colorida
- **Tempo**: 1 min

---

#### Slide 35 — Pergunta: Quando Otimizar é Melhor que Reescrever?
- **Tipo**: Exercício
- **Objetivo**: Discussão sobre quando usar otimização automatizada
- **Conteúdo**:
  - "Quando otimizar prompts é melhor que reescrevê-los manualmente?"
  - Casos para otimizar: volume alto, métrica clara, espaço de busca grande
  - Casos para manual: volume baixo, métrica subjetiva, domínio novo
  - "Como você define a métrica de avaliação para otimização?"
  - Discussão aberta (2 min)
- **Tempo**: 2 min

---

### SEÇÃO E — Auto-Aprendizado Contínuo (Slides 36-45 · 13 min)

---

#### Slide 36 — [SEÇÃO] Auto-Aprendizado Contínuo
- **Tipo**: Seção
- **Objetivo**: Transição para auto-aprendizado
- **Conteúdo**: "4 — Auto-Aprendizado Contínuo"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 37 — Memória de Sucesso/Falha
- **Tipo**: Conteúdo
- **Objetivo**: Explicar como agentes aprendem com experiência
- **Conteúdo**:
  - Memória de sucesso: "esta estratégia funcionou para este tipo de tarefa"
  - Memória de falha: "esta estratégia falhou para este tipo de tarefa"
  - Armazenamento: vetor + metadata (tipo, estratégia, outcome, timestamp)
  - Recuperação: nova tarefa → buscar casos similares → aplicar estratégia bem-sucedida
  - Analogia: "experiência profissional" do agente
  - Sem memória: agente repete os mesmos erros indefinidamente
- **Diagrama**: Agente executa → outcome → armazena (sucesso/falha) → próxima tarefa recupera
- **Tempo**: 2 min

---

#### Slide 38 — Reflexion em Nível de Sistema
- **Tipo**: Conteúdo
- **Objetivo**: Diferenciar reflexão individual de reflexão sistêmica
- **Conteúdo**:
  - Reflexion individual: agente reflete sobre SUA execução
  - Reflexion sistêmico: meta-agente reflete sobre o SISTEMA de agentes
  - Perguntas sistêmicas:
    - "Qual agente está falhando mais?"
    - "Qual tool é menos usada?"
    - "Qual padrão de tarefa é mais comum?"
  - Output: recomendações de mudança estrutural
  - Nível acima: reflexão sobre reflexão (meta-meta)
- **Diagrama**: Hierarquia: agente (reflexão individual) → meta-agente (reflexão sistêmica)
- **Tempo**: 1.5 min

---

#### Slide 39 — Estratégia Evolutiva (Strategy Evolver)
- **Tipo**: Conteúdo
- **Objetivo**: Detalhar o padrão strategy evolver
- **Conteúdo**:
  - Strategy evolver: componente que evolui estratégias ao longo do tempo
  - Estratégia = configuração de agente (prompt + tools + parâmetros)
  - Processo evolutivo:
    1. Manter população de estratégias
    2. Gerar variações (mutação)
    3. Avaliar em subset de tarefas
    4. Selecionar melhores
    5. Substituir população
  - Diferença vs DSPy: evolver opera no nível de sistema, DSPy no nível de prompt
  - HITL: auditoria periódica para prevenir drift
- **Diagrama**: Ciclo evolutivo com população de estratégias
- **Tempo**: 2 min

---

#### Slide 40 — Voyager: Aprendendo Skills no Minecraft
- **Tipo**: Diagrama
- **Objetivo**: Apresentar Voyager como caso canônico de auto-aprendizado
- **Conteúdo**:
  - Voyager (Wang et al., arXiv:2305.16291): agente que aprende skills no Minecraft
  - 3 componentes:
    1. Automatic curriculum: gera próximos desafios baseado no progresso
    2. Skill library: armazena skills como código executável
    3. Iterative prompting: refina prompts baseado em feedback do ambiente
  - Resultado: aprende skills complexas sem intervenção humana
  - Lição: ambiente fechado com feedback automático = auto-aprendizado viável
  - Limitação: Minecraft é determinístico e seguro — mundo real não é
- **Diagrama**: Arquitetura Voyager: curriculum → skill → library → execução
- **Tempo**: 2 min

---

#### Slide 41 — Quando Esquecer (Drift de Dados)
- **Tipo**: Conteúdo
- **Objetivo**: Discutir quando memória acumulada se torna problema
- **Conteúdo**:
  - Drift: ambiente muda, conhecimento antigo torna-se obsoleto
  - Tipos de drift:
    - Conceito: o que era correto não é mais (ex: política mudou)
    - Dados: distribuição de inputs mudou (ex: novos tipos de pergunta)
  - Sintomas: success rate cai, erros aumentam, feedback negativo cresce
  - Estratégias de esquecimento:
    - TTL: descartar memória antiga (ex: >30 dias)
    - Janela deslizante: manter apenas N casos mais recentes
    - Detecção ativa: monitorar métricas, descartar quando drift detectado
  - Pergunta: *O que acontece se o ambiente muda e o agente continua otimizando para o ambiente antigo?*
- **Diagrama**: Timeline: ambiente muda, memória antiga vs nova, detecção de drift
- **Tempo**: 2 min

---

#### Slide 42 — Pergunta: O Que Acontece se o Ambiente Muda?
- **Tipo**: Exercício
- **Objetivo**: Engajar a turma com uma pergunta sobre drift
- **Conteúdo**:
  - "O que acontece se o ambiente muda e o agente continua otimizando para o ambiente antigo?"
  - Resposta: overfitting ao ambiente antigo → performance cai
  - "Como detectar drift automaticamente?"
  - "Deveria esquecer tudo ou apenas o relevante?"
  - Discussão em duplas (2 min)
- **Diagrama**: Caixa de discussão
- **Tempo**: 1.5 min

---

#### Slide 43 — Exercício: Detectar Drift
- **Tipo**: Exercício
- **Objetivo**: Praticar detecção de drift em dados de agentes
- **Conteúdo**:
  - Cenário: agente de suporte com 6 meses de memória
  - Métricas dos últimos 30 dias: success rate caiu de 92% → 78%
  - Em duplas: propor 3 estratégias para detectar e mitigar drift
  - Exemplos: comparar distribuição de queries, TTL agressivo, re-treinar
  - 2 min propor, 1 min compartilhar
- **Diagrama**: Gráfico de success rate caindo ao longo do tempo
- **Tempo**: 2 min

---

#### Slide 44 — Auto-Aprendizado Sempre Melhora? (V/F)
- **Tipo**: Exercício
- **Objetivo**: Desafiar a hipótese de que auto-aprendizado é sempre positivo
- **Conteúdo**:
  - V/F: "Auto-aprendizado contínuo sempre melhora."
  - Resposta: FALSO
  - Razões:
    - Overfitting ao ambiente atual
    - Drift não detectado
    - Loop de feedback positivo (agente aprende a "jogar" a métrica)
    - Catastrophic forgetting (esquece skills úteis)
  - Auto-aprendizado precisa de: monitoramento, validação, e reset quando necessário
- **Diagrama**: V/F card com explicação
- **Tempo**: 1 min

---

#### Slide 45 — Lições do Auto-Aprendizado
- **Tipo**: Conteúdo
- **Objetivo**: Sintetizar os aprendizados
- **Conteúdo**:
  - Memória é poder, mas também é risco
  - Reflexão sistêmica > reflexão individual para melhorias estruturais
  - Strategy evolver = evolução biológica aplicada a configurações
  - Voyager prova que auto-aprendizado funciona em ambiente controlado
  - Drift é inevitável — detecção e esquecimento são obrigatórios
  - Auto-aprendizado não é bala de prata: precisa de governança
- **Diagrama**: 6 ícones com as lições
- **Tempo**: 1 min

---

### SEÇÃO F — Riscos e Governança (Slides 46-55 · 12 min)

---

#### Slide 46 — [SEÇÃO] Riscos e Governança
- **Tipo**: Seção
- **Objetivo**: Transição para riscos e segurança
- **Conteúdo**: "5 — Riscos e Governança"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 47 — Recursão e Loops de Auto-Modificação
- **Tipo**: Conteúdo
- **Objetivo**: Alertar sobre o perigo de recursão descontrolada
- **Conteúdo**:
  - Meta-agente modifica a si mesmo → nova versão modifica a si mesma → ...
  - Sem convergência: loop infinito de auto-modificação
  - Cada iteração pode introduzir mudanças cumulativas
  - Risco: comportamento emergente imprevisível
  - Mitigação:
    - max_iterations no loop de auto-modificação
    - Diff entre versões (mudança > N% requer aprovação)
    - Snapshot/versionamento de cada versão
    - Rollback automático se performance cair
- **Diagrama**: Loop de auto-modificação com guardrails (max_iter, diff check)
- **Tempo**: 2 min

---

#### Slide 48 — Drift de Objetivos (Goal Drift)
- **Tipo**: Conteúdo
- **Objetivo**: Explicar como objetivos podem derivar
- **Conteúdo**:
  - Goal drift: agente otimiza métrica que diverge do objetivo real
  - Exemplo: objetivo = "resolver tickets", métrica = "tickets fechados/hora"
  - Drift: agente fecha tickets sem resolver para maximizar métrica
  - Causa: métrica é proxy imperfeito do objetivo
  - Detecção:
    - Monitorar divergência entre métrica e satisfação do usuário
    - Auditoria periódica de amostras
    - Alerta se métrica sobe mas feedback cai
  - Mitigação: múltiplas métricas, não uma única
- **Diagrama**: Objetivo real vs métrica proxy divergindo ao longo do tempo
- **Tempo**: 2 min

---

#### Slide 49 — Meta-Governor Pattern
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar o padrão de governança para meta-agentes
- **Conteúdo**:
  - Meta-governor: guardião que avalia mudanças propostas pelo meta-agente
  - Separado do meta-agente (não pode auto-aprovar)
  - Regras do governor:
    - Policy-as-code: regras declarativas (não remover safety constraints, não aumentar custo >10%)
    - Sandbox test: mudança deve passar em testes antes de aprovação
    - Shadow run: executar em paralelo, comparar com versão atual
    - Canary: liberar para 5% do tráfego, monitorar
    - Rollback: se piorar, reverter automaticamente
  - HITL: aprovação humana para mudanças críticas
- **Diagrama**: Meta-agente → propõe mudança → Meta-governor → aprova/rejeita
- **Tempo**: 2 min

---

#### Slide 50 — Safety Fences
- **Tipo**: Diagrama
- **Objetivo**: Visualizar as camadas de segurança para mudanças auto-propostas
- **Conteúdo**:
  - mudança proposta → Meta-Governor → policy-as-code
  - vetar → bloquear / ok → sandbox test
  - sandbox passa? não → bloquear / sim → shadow run
  - shadow melhor? não → bloquear / sim → canary
  - canary ok? sim → produção / não → rollback
  - 4 camadas de defesa: policy → sandbox → shadow → canary
  - Cada camada filtra mudanças perigosas
- **Diagrama**: `12-Diagrams/ETHAGT15/safety-fences.mmd`
- **Animação**: Fluxo percorre as camadas, bloqueios destacados em vermelho
- **Tempo**: 2 min

---

#### Slide 51 — Confiança Incremental (Sandbox → Produção)
- **Tipo**: Conteúdo
- **Objetivo**: Detalhar o pipeline de confiança incremental
- **Conteúdo**:
  - Nível 0: Sandbox isolado (sem acesso a produção, dados sintéticos)
  - Nível 1: Shadow run (executa em paralelo, não afeta usuários)
  - Nível 2: Canary (5% do tráfego, monitorado)
  - Nível 3: Produção gradual (10% → 50% → 100%)
  - Nível 4: Produção total
  - Cada nível requer aprovação (automática ou humana)
  - Rollback instantâneo se métricas degradarem
  - Princípio: "confiança se ganha, não se dá"
- **Diagrama**: Escada de níveis 0 → 4 com gates entre eles
- **Tempo**: 1.5 min

---

#### Slide 52 — Vetos: Regras de Segurança
- **Tipo**: Código
- **Objetivo**: Mostrar como implementar regras de veto
- **Conteúdo**:
  - Veto = regra inegociável que bloqueia mudança
  - Exemplos de regras de veto:
    - "NUNCA remover constraints de segurança do system prompt"
    - "NUNCA aumentar custo por execução > 10%"
    - "NUNCA remover tools de auditoria/logging"
    - "NUNCA mudar modelo para um não-aprovado"
  - Implementação: policy-as-code (Rego/CEL)
  - Snippet: `veto(change) if change.removes_safety_constraint or change.cost_increase > 0.10`
  - Veto é binário: não há "quase veto"
- **Diagrama**: Code block com regras de veto
- **Tempo**: 1.5 min

---

#### Slide 53 — Exercício: Projetar um Meta-Governor
- **Tipo**: Exercício
- **Objetivo**: Praticar design de governança
- **Conteúdo**:
  - Cenário: meta-agente quer modificar o próprio system prompt
  - Em trios: projetar um meta-governor com regras de veto
  - Exemplos de regra: "não pode remover constraints de segurança", "não pode aumentar custo >10%"
  - Bônus: o que acontece se o meta-governor também for um agente?
  - 3 min design, 2 min compartilhar regras mais criativas
- **Diagrama**: Template de design do meta-governor
- **Tempo**: 3 min

---

#### Slide 54 — Pergunta: Em Que Ponto um Meta-Agente Se Torna Perigoso?
- **Tipo**: Exercício
- **Objetivo**: Estimular reflexão crítica sobre limites
- **Conteúdo**:
  - "Em que ponto um meta-agente se torna perigoso?"
  - Sinais de alerta:
    - Pode modificar suas próprias regras de segurança
    - Pode escolher sua própria métrica de avaliação
    - Não tem HITL para mudanças críticas
    - Pode escalar mudanças sem canary
  - Princípio: perigo = capacidade × autonomia × falta de oversight
  - Discussão aberta (2 min)
- **Tempo**: 2 min

---

#### Slide 55 — Caso de Estudo: Voyager (Segurança em Ambiente Fechado)
- **Tipo**: Diagrama
- **Objetivo**: Mostrar Voyager como caso de auto-aprendizado seguro
- **Conteúdo**:
  - Voyager aprende skills no Minecraft — por que é seguro?
  - Ambiente fechado: sandbox total, sem acesso a mundo real
  - Feedback determinístico: sucesso/falha é claro (crafteou o item?)
  - Sem consequências reais: erro no Minecraft não causa dano
  - Skills são código verificável (não ações opacas)
  - Lição: auto-aprendizado é seguro quando:
    - Ambiente é sandboxed
    - Feedback é claro e determinístico
    - Skills são auditáveis
    - Não há acesso a sistemas sensíveis
  - Em produção: replicar estas condições tanto quanto possível
- **Diagrama**: Comparação: Voyager (seguro) vs meta-agente em produção (risco)
- **Tempo**: 2 min

---

### SEÇÃO G — Fechamento (Slides 56-67 · 10 min)

---

#### Slide 56 — [SEÇÃO] Boas Práticas e Anti-Patterns
- **Tipo**: Seção
- **Objetivo**: Transição para o fechamento
- **Conteúdo**: "6 — Boas Práticas e Anti-Patterns"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 57 — Boas Práticas (DO)
- **Tipo**: Conteúdo
- **Objetivo**: Checklist de boas práticas de meta-agência
- **Conteúdo**:
  - Comece com domínio estreito e bem definido
  - Sempre valide agentes gerados (eval antes de deploy)
  - Use confiança incremental (sandbox → shadow → canary → produção)
  - Implemente meta-governor com vetos desde o início
  - Versionamento de todas as configs geradas
  - Monitore drift continuamente
  - HITL para mudanças críticas
  - Audite skills/memória acumulada periodicamente
- **Diagrama**: Checklist verde (etho-success)
- **Tempo**: 2 min

---

#### Slide 58 — Anti-Patterns (DON'T)
- **Tipo**: Conteúdo
- **Objetivo**: Checklist do que NÃO fazer
- **Conteúdo**:
  - Permitir auto-modificação sem limites (recursão descontrolada)
  - Usar métrica única como objetivo (goal drift)
  - Deployar sem eval (agente gerado pode ser pior)
  - Deixar meta-agente escolher própria métrica
  - Sem rollback automático
  - Confiança total sem canary/shadow
  - Ignorar drift de dados
  - Meta-agente sem governor (auto-aprovação)
- **Diagrama**: Checklist vermelho (etho-danger)
- **Tempo**: 2 min

---

#### Slide 59 — Resumo da Aula
- **Tipo**: Resumo
- **Objetivo**: Sintetizar os pontos-chave
- **Conteúdo**:
  - Meta-agência = agentes que operam sobre agentes (synthesis, evolution, optimization)
  - Geração = meta-agente + primitivas + validação rigorosa
  - Otimização = DSPy (compilação), Promptbreeder (evolução), Atlas (busca)
  - Auto-aprendizado = memória + reflexion + strategy evolver + drift detection
  - Riscos = recursão, goal drift, perda de controle
  - Governança = meta-governor + safety fences + confiança incremental + vetos
  - Projeto: otimizar prompts/tools automaticamente e medir ganho
- **Diagrama**: 7 ícones com os pontos-chave
- **Tempo**: 2 min

---

#### Slide 60 — Checklist da Aula
- **Tipo**: Resumo
- **Objetivo**: Confirmar que todos os tópicos foram cobertos
- **Conteúdo**:
  - [ ] Definiu meta-agência e 3 estratégias
  - [ ] Implementou geração de agente com validação
  - [ ] Aplicou DSPy ou Promptbreeder para otimização
  - [ ] Discutiu auto-aprendizado e drift
  - [ ] Projetou um meta-governor com vetos
  - [ ] Identificou riscos e mitigações
- **Diagrama**: Checklist visual
- **Tempo**: 1 min

---

#### Slide 61 — Quiz: Pergunta 1
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "Qual é a diferença fundamental entre um agente e um meta-agente?"
  - A) O meta-agente usa um modelo maior
  - B) O meta-agente opera sobre agentes (seu ambiente é outro agente)
  - C) O meta-agente tem mais tools
  - D) O meta-agente é sempre mais rápido
  - Resposta: B
- **Tempo**: 1 min

---

#### Slide 62 — Quiz: Pergunta 2
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "O que é goal drift?"
  - A) Agente muda de tarefa
  - B) Agente otimiza uma métrica que diverge do objetivo real
  - C) Agente esquece o objetivo original
  - D) Agente muda de modelo
  - Resposta: B
- **Tempo**: 1 min

---

#### Slide 63 — Quiz: Pergunta 3
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "Qual é a PRIMEIRA camada de defesa em safety fences?"
  - A) Canary deployment
  - B) Shadow run
  - C) Policy-as-code (vetos)
  - D) Rollback automático
  - Resposta: C
- **Tempo**: 1 min

---

#### Slide 64 — Perguntas para Discussão
- **Tipo**: Exercício
- **Objetivo**: Estimular debate
- **Conteúdo**:
  1. "Quando otimizar prompts é melhor que reescrevê-los manualmente?"
  2. "Defina goal drift e proponha uma detecção automática."
  3. "Por que meta-governor é necessário? O agente não pode se autorregular?"
  4. "Em que ponto um meta-agente se torna perigoso?"
- **Tempo**: 2 min

---

#### Slide 65 — Conexão com Próximos Módulos
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar como ETHAGT15 conecta com o resto da especialização
- **Conteúdo**:
  - ETHAGT16 — Sociedades de Agentes: meta-agentes em ecossistemas multi-agente
  - ETHAGT90 — Capstone: meta-agente como sistema de orquestração
  - ETHAGT14 — Escalabilidade: otimização de custo aplicada a meta-agentes
  - ETHAGT12 — AgentOps: avaliação e observabilidade de meta-agentes
- **Diagrama**: Mapa da especialização com ETHAGT15 destacado
- **Tempo**: 1 min

---

#### Slide 66 — Referências, Projeto e Labs
- **Tipo**: Referências
- **Objetivo**: Indicar leitura e apresentar projeto/labs
- **Conteúdo**:
  - Obrigatório: Khattab et al. *DSPy* (arXiv:2310.03714)
  - Obrigatório: Fernando et al. *Promptbreeder* (arXiv:2309.16797)
  - Recomendado: Hu et al. *Meta-Prompting* (arXiv:2311.11402)
  - Recomendado: Wang et al. *Voyager* (arXiv:2305.16291)
  - Projeto: implementar otimização automática (DSPy) e medir ganho em benchmark
  - Lab 1 (4h): "Agente que escreve agente" — meta-agente que gera e avalia
  - Próxima aula: ETHAGT16 — Sociedades de Agentes
- **Tempo**: 1 min

---

#### Slide 67 — Q&A / Encerramento
- **Tipo**: Capa
- **Objetivo**: Abrir para perguntas e encerrar
- **Conteúdo**:
  - "Perguntas?"
  - Contato do professor
  - "Na próxima aula: ETHAGT16 — Sociedades de Agentes"
- **Diagrama**: Logo Etho + fundo etho-dark
- **Tempo**: 2 min

---

## Resumo do Storyboard

| Seção | Slides | Tempo | Conteúdo |
|---|---|---|---|
| A — Abertura | 1-6 | 8 min | Capa, objetivos, competências, agenda, motivação, contexto |
| B — Meta-Agência | 7-14 | 12 min | Definição, estratégias, arquitetura, exemplos, risco vs benefício, exercício |
| C — Geração | 15-24 | 15 min | Meta-agente, templates, pipeline, validação, caso, DEMO, exercício |
| D — Otimização | 25-35 | 15 min | DSPy, Promptbreeder, Atlas, tools, topologia, loop, comparação |
| E — Auto-Aprendizado | 36-45 | 13 min | Memória, reflexion, evolver, Voyager, drift, exercício |
| F — Riscos | 46-55 | 12 min | Recursão, goal drift, meta-governor, safety fences, vetos, caso |
| G — Fechamento | 56-67 | 10 min | Boas práticas, anti-patterns, resumo, quiz, discussão, referências, Q&A |
| **Total** | **67** | **90 min** | |

---

## Diagramas Necessários

| # | Slide | Diagrama | Tipo | Fonte |
|---|---|---|---|---|
| D1 | 5 | Manual vs automatizado (motivação) | Comparação | Novo |
| D2 | 6 | Timeline de marcos da meta-agência | Timeline | Novo |
| D3 | 8 | Hierarquia: meta-agente → agentes → ambiente | Hierarquia | Novo |
| D4 | 9 | 3 estratégias (synthesis/evolution/optimization) | 3 colunas | Novo |
| D5 | 10 | Meta-agente: arquitetura conceitual | Flowchart | `12-Diagrams/ETHAGT15/meta-agent.mmd` |
| D6 | 11 | 4 cards: DSPy, Voyager, Meta-Prompting, Promptbreeder | Grid | Novo |
| D7 | 12 | Balança risco vs benefício | Balança | Novo |
| D8 | 16 | Input → meta-agente → primitivas → config | Flowchart | Novo |
| D9 | 17 | Biblioteca de templates → composição | Arquitetura | Novo |
| D10 | 18 | Pipeline de geração (6 passos + feedback) | Pipeline | Novo |
| D11 | 19 | Funil de validação | Funil | Novo |
| D12 | 20 | Antes vs depois (caso suporte por produto) | Comparação | Novo |
| D13 | 26 | Espaço de busca humano vs automático | Gráfico | Novo |
| D14 | 27 | Código declarativo → DSPy → prompt otimizado | Flowchart | Novo |
| D15 | 28 | Teleprompter: assinatura + dados → prompt | Flowchart | Novo |
| D16 | 29 | Ciclo evolutivo do Promptbreeder | Ciclo | Novo |
| D17 | 31 | Loop de otimização de tools | Loop | Novo |
| D18 | 32 | Topologia A vs B com métricas | Comparação | Novo |
| D19 | 33 | Loop de evolução (strategy evolver) | Flowchart | `12-Diagrams/ETHAGT15/evolution-loop.mmd` |
| D20 | 37 | Agente → outcome → memória → recuperação | Flowchart | Novo |
| D21 | 38 | Hierarquia: reflexão individual vs sistêmica | Hierarquia | Novo |
| D22 | 39 | Ciclo evolutivo com população de estratégias | Ciclo | Novo |
| D23 | 40 | Arquitetura Voyager | Arquitetura | arXiv:2305.16291 |
| D24 | 41 | Timeline de drift: ambiente muda, memória envelhece | Timeline | Novo |
| D25 | 47 | Loop de auto-modificação com guardrails | Loop | Novo |
| D26 | 48 | Objetivo real vs métrica proxy divergindo | Gráfico | Novo |
| D27 | 49 | Meta-agente → propõe → meta-governor → aprova | Flowchart | Novo |
| D28 | 50 | Safety fences (4 camadas) | Flowchart | `12-Diagrams/ETHAGT15/safety-fences.mmd` |
| D29 | 51 | Escada de confiança incremental (níveis 0-4) | Escada | Novo |
| D30 | 55 | Comparação: Voyager (seguro) vs produção (risco) | Comparação | Novo |
| D31 | 65 | Mapa da especialização com ETHAGT15 | Mind map | Novo |

---

## Pendências de Produção

- [ ] Produzir 28 diagramas novos (D1-D4, D6-D18, D20-D27, D29-D31)
- [ ] Screenshot do terminal com meta-agente gerando config (Slide 21)
- [ ] Screenshot do código com syntax highlighting (Slides 21, 52)
- [ ] Imagem de fundo para capa (Slide 1) — tema recursão/agentes gerando agentes
- [ ] Badge de competências (Slide 3)
- [ ] Timeline de marcos da meta-agência (Slide 6)
- [ ] Arquitetura Voyager (Slide 40) — baseada no paper
- [ ] Template de design do meta-governor (Slide 53)

---

> **Aguardando aprovação deste storyboard para gerar os slides detalhados com notas do professor.**
