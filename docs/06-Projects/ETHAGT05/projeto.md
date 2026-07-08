# ETHAGT05 — Projeto do Módulo: Memória de Agente Pessoal de Longo Prazo

> Curso: Memória de Agentes (working · episódica · semântica · procedural) · Pilar: Técnico 40% + Prático 10% · Equipe: individual ou dupla

## Contexto / Cenário

Uma startup de produtividade está construindo um assistente pessoal que acompanha o usuário por meses ou anos — um "segundo cérebro" que lembra preferências, projetos em andamento, contatos, decisões passadas e skills aprendidas. Hoje, o assistente perde tudo entre sessões: a cada conversa, começa do zero, o que frustra os usuários. O desafio é arquitetar um sistema de memória de 4 camadas (working, episódica, semântica, procedural) que persista entre sessões, recupere contexto relevante sem inundar a context window, e respeite privacidade (PII, direito ao esquecimento). O sistema deve sobreviver a reinícios do servidor, migrar estado entre versões de schema, e justificar quando *não* memorizar (custo vs benefício).

## Objetivo

Projetar a memória de um agente pessoal de longo prazo com as 4 camadas (working, episódica, semântica, procedural). Implementar persistência via checkpointer (Postgres), recall vetorial para memória episódica, sumarização/eviction para gerenciamento de contexto, e uma política documentada de privacidade e evicção. Justificar os trade-offs arquiteturais em um ADR de memória.

## Requisitos

### Funcionais

1. Working memory: contexto da sessão atual gerenciado na context window com eviction por relevância/idade.
2. Episódica: eventos (interações, decisões) persistidos com timestamp em Postgres + embedding para recall vetorial (Qdrant).
3. Semântica: fatos consolidados extraídos da episódica (ex.: "usuário prefere respostas concisas") com promoção episódica → semântica.
4. Procedural: skills/fluxos aprendidos (ex.: "para agendar reunião, usar tool X") armazenados e recuperáveis.
5. Agente demonstra memória útil em sessões espaçadas ( Dia 1, Dia 3, Dia 7 ) respondendo perguntas que dependem de contexto anterior.
6. Resume/checkpointer: agente interrompido pode ser retomado preservando estado completo.

### Não-funcionais

- Persistência em Postgres (checkpointer LangGraph) com schema versionado.
- Recall vetorial com metadata filtering (por sessão, usuário, janela temporal).
- Política de privacidade documentada: PII redigida, retenção configurável, direito ao esquecimento implementado (delete cascata).
- Política de eviction: combinação de relevância (score de embedding) e idade (TTL).
- Custo de memória (storage + embedding) monitorado e reportado por usuário/mês.
- Latência de recall ≤ 500 ms para base de ≤10.000 memórias.

## Entregáveis

- Código (repositório com as 4 camadas de memória + agente integrado).
- ADR de memória (camadas, stores, trade-offs de consolidação e eviction).
- Política de privacidade/eviction (documento + implementação de redação e delete).
- Demo cross-sessão: script que simula sessões em D1/D3/D7 e mostra recall correto.

## Critérios de sucesso (mensuráveis)

- Agente demonstra memória útil em sessões espaçadas: recall correto de fato/decisão em ≥80% das perguntas que dependem de contexto anterior.
- Política de privacidade e eviction documentada e implementada (PII redigida, delete funcional, TTL configurável).
- Resume via checkpointer funciona: estado preservado após restart do processo (demonstrado em ≥1 caso).
- Custo de memória reportado e justificado (quando memorizar vs descartar).
- Promoção episódica → semântica documentada com exemplo concreto (fato extraído de ≥2 episódios).

## Competências avaliadas

- C1 Programação Agêntica — nível **A** (integração de memória em agente de produção).
- C4 Agent Memory — nível **I** (arquitetura das 4 camadas, checkpointer, recall vetorial, eviction).
- C5 AgentOps & Avaliação — nível **B** (observabilidade de memória, custo, testes cross-sessão).
- C6 Agent Security — nível **B** (privacidade, PII, direito ao esquecimento).

## Referências

- Apostila: `04-Apostilas/ETHAGT05/apostila.md`
- Rubrica técnica: `08-Assignments/ETHAGT05/assignment-01.md`
