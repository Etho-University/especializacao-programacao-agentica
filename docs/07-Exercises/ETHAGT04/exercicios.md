# ETHAGT04 — Lista de Exercícios

> Curso: Reasoning & Planning. Fixação de conceitos. Use a apostila `04-Apostilas/ETHAGT04/apostila.md` como referência.

## Múltipla escolha

**1. Qual é a principal vantagem do padrão ReWOO sobre ReAct?**

a) ReWOO usa modelos maiores
b) ReWOO planeja todas as etapas primeiro e coleta evidências em paralelo, reduzindo tokens de raciocínio intermediário
c) ReWOO não usa ferramentas
d) ReWOO é mais preciso em todos os casos

**2. No padrão Reflexion, a "memória de erros" serve para:**

a) Armazenar senhas
b) Lembrar falhas anteriores e evitar repeti-las em tentativas subsequentes
c) Caching de respostas
d) Indexar documentos

**3. Em Tree of Thoughts (ToT), o que diferencia este padrão do CoT linear?**

a) ToT explora múltiplos caminhos de raciocínio em árvore, avaliando estados intermediários
b) ToT é mais rápido
c) ToT não usa LLM
d) ToT só funciona com matemática

**4. Um reasoning model nativo (ex.: o1/o3, Claude com extended thinking) difere de CoT promptado porque:**

a) É mais barato
b) O raciocínio é treinado/integrado ao modelo, não adicionado via prompt
c) Não usa tools
d) Sempre produz respostas mais curtas

## Verdadeiro ou Falso (justificado)

**1.** "Self-Discover é sempre superior a CoT." — Justifique.

**2.** "ReWOO reduz custo vs. ReAct porque não inclui o raciocínio intermediário a cada passo do loop." — Justifique.

**3.** "Em LATS (Language Agent Tree Search), o backtracking permite abandonar caminhos improdutivos." — Justifique.

**4.** "Um reasoning model nativo torna o CoT promptado desnecessário." — Justifique.

## Código curto

**1.** Escreva o pseudocódigo da estrutura de memória de um agente Reflexion (lista de reflexões de tentativas anteriores injetada no prompt).

**2.** Escreva o pseudocódigo de um Plan-and-Execute: planner gera lista de passos; executor executa cada um; coleta resultados.

**3.** Escreva o pseudocódigo de um orçamento de tokens para um agente (parar quando `total_tokens > budget`).

## Análise de trade-off

**1.** Compare ReAct vs. Plan-and-Execute para uma tarefa multi-step. Quando cada é preferível?

**2.** Compare Tree of Thoughts vs. reasoning model nativo (o1/o3). Quando o reasoning model nativo substitui ToT?

**3.** Para 3 classes de problema (matemática, código, decisão aberta), indique a estratégia de raciocínio mais adequada e justifique.

## Debug / diagnóstico

**1.** Um agente Plan-and-Execute gera um plano de 10 passos, mas o passo 3 falha e o agente não re-planeja. Proponha uma correção com re-planejamento supervisionado.

**2.** Um agente com Tree of Thoughts gera muitos ramos mas nunca seleciona um caminho ótimo — sempre escolhe o primeiro. Diagnóstico provável e correção.
