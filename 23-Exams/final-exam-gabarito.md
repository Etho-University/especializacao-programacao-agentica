# Prova Final Integradora — Gabarito Comentado (restrito a avaliadores)

> Respostas esperadas e critérios de correção para [`final-exam.md`](final-exam.md).

## Parte 1 — Fundamentos e raciocínio

**1.** Augmented LLM = LLM + retrieval + tools + memory (Anthropic). É atômico porque workflows e agentes são composições dele. Remover retrieval: agente não acessa conhecimento externo. Remover tools: não age, só fala. Remover memory: sem persistência, sem aprendizado.

**2.**
| | Latência | Custo | Robustez |
|---|---|---|---|
| ReAct | média | alto (O(N²) tokens) | média |
| Plan-and-Execute | baixa (1 planner) | médio (O(N)) | alta (replanner) |
| ReWOO | baixa (paralelo) | baixo | baixa (rígido) |

- ReAct: interativo com ambiente dinâmico.
- Plan-and-Execute: estrutura previsível.
- ReWOO: evidências independentes, alto volume.

**3.** Vale quando: (i) problema tem múltiplos caminhos possíveis com qualidade variável; (ii) há avaliador confiável para podar; (iii) orçamento permite (problema é valioso). Não vale para problemas simples ou custo-sensível.

**4.** Com reasoning model nativo: não force CoT promptado (modelo já raciocina); mais tool use (raciocínio robusto → calls confiáveis); orçamento de reasoning (calibrar esforço); latência maior esperada.

**5.** Reasoning models fazem internamente o que ToT faz externamente (explorar caminhos, avaliar). Para raciocínio "puro" sem ambiente, ToT torna-se redundante. ToT ainda vale para agentes com estado externo (LATS).

## Parte 2 — Tools, MCP e memória

**6.**
```python
def request_delete_account(user_id: str, reason: str) -> str:
    """Solicita a exclusão PERMANENTE de uma conta. AÇÃO IRRIVERSÍVEL.
    Todos os dados serão apagados após confirmação humana.
    Use apenas após confirmar identidade e motivo com o usuário."""
```
HITL obrigatório: humano aprova antes de `_delete_account_real` executar.

**7.** (i) **Poka-yoke** — violação: paths relativos. (ii) **Exemplos na descrição** — violação: "faz coisa". (iii) **Fronteiras claras entre tools similares** — violação: `search_kb` e `search_web` sem dizer quando usar qual.

**8.** **Tools** (ações com schema): quando modelo precisa executar. **Resources** (dados por URI, leitura): quando modelo precisa ler dado. **Prompts** (templates): quando quer padronizar interação. Exemplo: tool `get_order`, resource `docs://policy/X`, prompt `summarize_doc`.

**9.** Working (context window: conversa atual); Episódica (vector: "cliente perguntou X em jan/26"); Semântica (Postgres: "cliente é VIP desde 2024"); Procedural (skills: "sempre que cliente reclamar de Y, faça Z").

**10.** HITL pausa execução. Sem checkpointer, estado se perde na pausa (processo termina). Checkpointer serializa estado; ao retomar (horas/dias depois), restaurado. Sem isso, HITL longo é impossível.

## Parte 3 — Multi-agente e orquestração

**11.** Hierarchical > swarm quando: (i) >10 workers (swarm fica caótico); (ii) sub-domínios separáveis; (iii) quer isolamento entre sub-árvores; (iv) precisa de coordenação estruturada (SOPs).

**12.** Partition key determina partição; ordering é garantido **dentro** de partição. Exemplo: eventos do mesmo `user_id` devem estar ordenados (para não processar delete antes de create). Use `user_id` como key → mesma partição → ordem preservada.

**13.**
```
1. processar_pedido ✓
2. cobrar_cartao ✗ (falha)
   compensar: cancelar_pedido
3. (não chega a enviar email)
```
Se 2 passa e 3 falha: compensar 2 (estornar) e 1 (cancelar).

**14.** **Temporal**: durable execution — sobrevive a crashes com estado checkpointado; HITL via interrupt por dias; replays. **Kafka + retries**: mensagens persistem mas **lógica** de workflow não é durável — se processo cai entre steps, lógica precisa ser refeita. Temporal modela workflow como código first-class durável.

## Parte 4 — Produção e fronteira

**15.** (1) Input filter (classifica injeção); (2) Schema estrito (structured output); (3) System prompt robusto; (4) Tool allowlist; (5) HITL antes de enviar; (6) Output filter (PII); (7) Auditoria. Cada camada independente.

**16.** Benchmarks: cobertura limitada; risco de overfit; sem distribuição real de uso; sem integrações reais; contaminação. Use como sinal entre vários.

**17.** Model routing: classificador avalia complexidade; 80% fáceis → Haiku (10× mais barato); 20% difíceis → Sonnet/Opus. Economia 5-7× sem perder qualidade percebida. Combinar com cache semântico (perguntas repetidas).

**18.** **Goal drift**: sistema otimiza para métrica errada ou deriva do objetivo. Detecções: (i) métricas multi-dimensionais (se primária melhora mas secundária degrada, alerta); (ii) audit periódico alinhado com humanos ("para que estamos otimizando?").

**19.** Limitações AI Scientist: (i) originalidade fraca (recombinante); (ii) hallucinações factuais em domains não-ML; (iii) código às vezes quebrado. HITL essencial porque: qualidade científica requer julgamento humano; consequências são públicas; "automatização" cria falsa confiança.

**20.** ADR esperado:
- **Contexto**: pesquisa técnica autônoma na Etho.
- **Decisão**: Hierarchical + Orchestrator-Workers + Evaluator-Optimizer; memória multi-camada (Postgres + Qdrant + Neo4j); Temporal para durable.
- **Justificativa**: integração dos 16 módulos; pesquisa exige flexibilidade (agente) + rigor (workflow); durable para HITL.
- **Alternativas**: swarm (caótico para muitos workers); só Postgres (sem KG multi-hop); sem Temporal (sem HITL longo).
- **Consequências**: complexidade alta; custo; mas atende todos os requisitos.

---

## Nota esperada por perfil

- **5,0**: arquiteto sênior — síntese perfeita, justifica tudo, vê trade-offs.
- **4,0**: profissional sólido — aplica conceitos, raciocina bem, algumas imprecisões.
- **3,0**: profissional em formação — conhece conceitos mas não sintetiza.
- <3,0: precisa revisar módulos antes de certificar.
