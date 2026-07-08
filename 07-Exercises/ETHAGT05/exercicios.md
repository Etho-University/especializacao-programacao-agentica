# ETHAGT05 — Lista de Exercícios

> Curso: Memória de Agentes. Fixação de conceitos. Use a apostila `04-Apostilas/ETHAGT05/apostila.md` como referência.

## Múltipla escolha

**1. Qual tipo de memória armazena "como fazer" uma tarefa (skills/procedimentos)?**

a) Episódica
b) Semântica
c) Procedural
d) Working

**2. Qual é o papel de um checkpointer (ex.: Postgres) em LangGraph?**

a) Caching de embeddings
b) Persistir o estado serializável do agente, permitindo resume, replay e branching (time travel)
c) Indexar documentos
d) Enviar notificações

**3. A estratégia de "sumarização em cascata" no gerenciamento de contexto serve para:**

a) Melhorar a qualidade das respostas
b) Reduzir o tamanho da context window quando a conversa cresce, preservando informação essencial
c) Aumentar o custo
d) Substituir a memória vetorial

**4. Em entity-centric memory (estilo MemGPT), a entidade é:**

a) Um tipo de embedding
b) Uma unidade de informação centrada em entidades (pessoas, lugares, conceitos) com atributos e relações
c) Um protocolo de comunicação
d) Um tipo de checkpoint

## Verdadeiro ou Falso (justificado)

**1.** "Uma memória vetorial é sempre melhor que uma memória relacional para recall episódico." — Justifique.

**2.** "Eviction por relevância (remover itens menos relevantes da context window) é preferível a eviction por tempo." — Justifique.

**3.** "PII (Personally Identifiable Information) em memória de longo prazo requer redação e política de retenção." — Justifique.

**4.** "O custo financeiro de uma chamada LLM (por token) cresce quadraticamente com o tamanho do contexto." — Justifique.

## Código curto

**1.** Escreva o pseudocódigo de uma política de eviction que combina relevância (score de embedding) e idade (timestamp), removendo os N itens menos prioritários.

**2.** Escreva o pseudocódigo de um recall episódico: dado um query, buscar os top-k eventos por similaridade semântica com filtros de metadata (sessão, usuário).

**3.** Escreva o pseudocódigo de uma sumarização em cascata: quando o histórico excede M mensagens, sumarizar as mais antigas.

## Análise de trade-off

**1.** Compare memória vetorial vs. memória relacional para um agente de suporte ao cliente. Quando cada é melhor?

**2.** Compare working memory (context window) vs. memória persistente (checkpointer). Quando o agente só precisa da primeira?

**3.** Para um agente pessoal de longo prazo (assistente de produtividade), quais das 4 camadas de memória são necessárias e por quê?

## Debug / diagnóstico

**1.** Um agente com checkpointer é interrompido e retomado, mas perde o contexto da conversa. Liste 2 causas prováveis.

**2.** Um agente com memória vetorial recupera eventos irrelevantes (ex.: conversa de outro usuário). Diagnóstico e correção.
