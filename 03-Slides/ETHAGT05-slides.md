# ETHAGT05 — Memória de Agentes — Slides

> Apresentação para aula síncrona · ~50 min · 13 slides

## Estrutura da aula
- Abertura (5 min): gancho/motivação
- Teoria (25 min): conceitos principais com diagramas de referência
- Demonstração (10 min): código ao vivo ou walkthrough de lab
- Exercício (5 min): questão rápida ou discussão
- Fechamento (5 min): conexão com próximo módulo, leitura recomendada

## Slides

### Slide 1 — Título
- ETHAGT05 — Memória de Agentes (working · episódica · semântica · procedural)
- Professor, data, Universität Etho
- Pré-requisito: ETHAGT04
- ~1 min

### Slide 2 — Agenda
1. Tipos de memória
2. Checkpointer e estado persistente
3. Gerenciamento de contexto
4. Memória vetorial para recall
5. Memória semântica e grafos
6. Produção: consistência, privacidade, custo
- ~1 min

### Slide 3 — Gancho / Motivação
- Problema: agente sem memória começa do zero a cada interação — não aprende, não melhora
- Exemplo: assistente de produtividade que você pergunta "lembra do projeto X?" e ele não sabe
- A solução: memória em 4 camadas (working, episódica, semântica, procedural)
- Pergunta: *Quanto contexto você acha que um assistente pessoal precisa reter?*
- ~3 min

### Slide 4 — Tipos de Memória
- Working memory (context window): limites e estratégias (token budget, sliding window)
- Episódica: eventos passados com timestamp (o que aconteceu, quando)
- Semântica: fatos, conhecimento (o que é verdade sobre o mundo)
- Procedural: como fazer, skills aprendidas
- Inspiração cognitiva sem literalismo (não somos cérebros)
- Diagrama: `12-Diagrams/ETHAGT05/memory-layers.mmd`
- ~4 min

### Slide 5 — Checkpointer e Estado Persistente
- LangGraph checkpointer: modelo de estado serializável
- Implementações: Postgres, SQLite, Redis
- Resume, replay, branching (time travel)
- Versionamento de schema de estado
- Diagrama: `12-Diagrams/ETHAGT05/checkpointer-resume.mmd`
- Pergunta: *Time travel: debug ou problema de segurança?*
- ~4 min

### Slide 6 — Gerenciamento de Contexto
- Custo cresce quadraticamente? Visão crítica (KV cache, sliding window)
- Sumarização em cascata: sumário de sumários
- Eviction por relevância ou tempo
- Entity-centric memory (estilo MemGPT, Zep)
- ~3 min

### Slide 7 — Memória Vetorial para Recall
- Embedding de eventos/passados
- Recall por similaridade semântica
- Metadata filtering (por sessão, usuário, tempo)
- Pós-recuperação: re-ranking
- Quando memória vetorial é pior que relacional
- Pergunta: *Se o usuário pergunta "aquela reunião de terça" — embedding ou metadata?*
- ~4 min

### Slide 8 — DEMO: Checkpointer em Postgres
- Código ao vivo: agente inicia tarefa, é interrompido (kill), retoma dias depois
- Mostrar estado preservado (mensagens, contexto, steps)
- Replay de execução anterior para debug
- Referência: `05-Labs/ETHAGT05/Lab1-Checkpointer-Postgres`
- ~5 min

### Slide 9 — Memória Semântica e Grafos
- Quando promover episódica → semântica (consolidação)
- Knowledge graph como memória estruturada
- Integração com KG (profundidade em ETHAGT07)
- Exemplo: de "João perguntou sobre Python" (episódica) → "João é desenvolvedor Python" (semântica)
- ~3 min

### Slide 10 — Produção: Consistência, Privacidade, Custo
- Consistência em sistemas multi-agente (eventual, ordenação)
- PII em memória: redação, retenção, direito ao esquecimento
- Custo de memória vs benefício (quando *não* memorizar)
- Observabilidade de memória (quem acessou, quando)
- Discussão: *Direito ao esquecimento: como implementar em memória vetorial?*
- ~4 min

### Slide 11 — Exercício: Política de Eviction
- Cenário: assistente pessoal com 1 ano de interações
- Em trios: escrever política de eviction combinando relevância e idade
- Exemplo: "eventos com > 6 meses e score < 0.5 são arquivados"
- 3 min discussão, 1 min compartilhar
- ~4 min

### Slide 12 — Conexão com Próximo Módulo
- ETHAGT06 — RAG Agêntico: memória + recuperação combinados
- ETHAGT07 — Knowledge Graphs: memória semântica aprofundada
- ETHAGT14 — Escalabilidade: memória em produção multi-tenant
- Leitura: Packer et al. *MemGPT* (arXiv:2310.08560)
- ~2 min

### Slide 13 — Referências
- Packer, C. *MemGPT: Towards LLMs as Operating Systems* (arXiv:2310.08560)
- Park, J.S. *Generative Agents* (arXiv:2304.03442)
- LangGraph docs — *Persistence* e *Memory*
- Zep (long-term memory para agentes)
- ~1 min
