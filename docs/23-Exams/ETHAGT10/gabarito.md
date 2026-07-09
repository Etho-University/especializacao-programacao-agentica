---
password: Etho-Prof-2026
---
# ETHAGT10 — Gabarito da Prova
> Restrito a mentores.

## Parte 1 — Conceitos

**1.** **(b)** Correta. O supervisor é um roteador: recebe estado, decide qual worker chamar via tool calls e agrega resultados. — *Ref.: Cap. 2 — Supervisor e Hierarchical (§2.1).*

**2.** **Falso.** Mesh (p2p flat) escala mal em coordenação: cada agente precisa conhecer/routear para os demais (explosão O(N²) de ligações), difícil de governar. Pode ser ótimo para poucos agentes peer;Hierarchical/Swarm costumam escalar melhor em muitos workers. — *Ref.: Cap. 1 — Catálogo (§1.2); Cap. 6 — Tree, Recursive e Mesh.*

**3.** **(c)** Recursive é anti-pattern quando há recursão profunda *sem cercas* (orçamento de agentes, profundidade máxima, critério de parada, meta-governor com veto) — o sistema explode em complexidade e custo. (a) é um caso *favorável* ao recursive, não anti-pattern; (b) é falso (recursive é justificável com cercas); (d) é problema de workers/mesh, não de recursão. — *Ref.: Cap. 6 (§6.2 Recursive; §6.3 Quando recursive é anti-pattern).*

**4.** **Falso.** Hierarchical agrega complexidade; só vale quando há sub-domínios separáveis, isolamento desejado ou > ~10 workers que tornariam flat caótico. Para 2-3 workers, flat/supervisor é mais simples e geralmente melhor. — *Ref.: Cap. 2 (§2.4 Quando escalar hierarquia vs flat; §2.5 Casos de falha).*

## Parte 2 — Aplicação e trade-off

**5.** Hierarchical > swarm quando: (i) > ~10 workers (swarm fica caótico); (ii) sub-domínios nitidamente separáveis e isoláveis; (iii) necessidade de coordenação estruturada/SOPs e responsabilidade rastreável; (iv) quer-se sub-árvores independentes. — *Ref.: Cap. 2 (§2.3 Hierarchical; §2.4); Cap. 3 — Swarm e handoffs (§3.3 Limites do swarm).*

**6.** Escolha típica: **Supervisor** (ou Orchestrator-Workers) com 3 workers especialistas + um sintetizador. Rejeitar *swarm*: a coordenação por handoffs é frágil quando há 3 especialistas paralelos e um agregador; rejeitar *mesh*: 3 agentes peer não agregam valor e complicam a convergência. — *Ref.: Cap. 7 — Escolha e ADR (§7.1 Matriz); Cap. 4 — Pipeline e Orchestrator-Workers.*

**7.** Causas: (i) supervisor processa serialmente todas as decisões (gargalo de LLM); (ii) workers redundantes geram ruído/confusão de roteamento. Correções: (a) hierarquizar — sub-supervisores por domínio (paralelismo); (b) cache/roteamento de baixo custo (classificador leve) antes do supervisor caro; (c) particionar workers. — *Ref.: Cap. 2 (§2.5 Casos de falha).*

**8.** Priorizar **Swarm/Event-driven** (fluxo com handoffs e processamento paralelo): baixa latência percebida (sem serializar tudo num supervisor central) e alta flexibilidade (agentes leves com transfer). Custa mais em coordenação, aceitável dado o enunciado. — *Ref.: Cap. 7 — Escolha e ADR (§7.1 Matriz de decisão); Cap. 3 — Swarm.*

## Parte 3 — Projeto curto

**9.** ADR esperado:
- **Contexto**: atendimento multi-tenant com múltiplos domínios, isolamento por tenant, necessidade de escala.
- **Decisão**: Hierarchical — supervisor raiz roteia por tenant; sub-supervisores por domínio (suporte, vendas) com workers.
- **Justificativa**: isolamento entre tenants/domínios; escalável com sub-árvores; responsabilidade rastreável.
- **Alternativas**: Supervisor flat (gargalo acima de ~10 workers); Swarm (frágil para coordenação multi-domínio).
- **Consequências**: mais complexidade e custo; mas atende isolamento e escala. — *Ref.: Cap. 7 — Escolha e ADR (§7.2 O ADR de topologia).*

**10.** **Tree of Agents**: árvore fixa de especialistas que se ramifica para explorar/avaliar opções (ex.: LATS explorando caminhos). **Recursive**: agente que gera/invoca agentes (meta-agência, potencialmente auto-referente). Cenários: Tree = diagnóstico diferencial com múltiplos ramos; Recursive = um meta-agente que monta dinamicamente uma equipe para uma tarefa nova. — *Ref.: Cap. 6 — Tree, Recursive e Mesh (§6.1, §6.2).*

---

## Erros comuns (parcial/dedução)

- **Q1**: descrever supervisor como executor → anular; (a) e (c) revelam mal-entendido do padrão.
- **Q2**: defender "mesh sempre escalável" sem citar explosão O(N²) de ligações → até -50%.
- **Q4**: aplicar hierarchical cegamente para 2-3 workers → deduzir metade (ignora complexidade desnecessária).
- **Q5/Q7**: citar só "muitos workers" sem isolamento/domínios separáveis → até -40%.
- **Q9**: ADR sem "Alternativas" ou "Consequências" → estrutura incompleta, -40%.
- **Q10**: confundir Tree (ramificação de especialistas) com Recursive (auto-geração de agentes) → anular.

Crédito parcial: topologia certa com justificativa fraca vale até 60%; topologia defensável mas não ótima, com ADR sólido, merece nota alta.

---

## Rubrica por questão (pts)

| Q | Tipo | pts | Aceita parcial |
|---|---|---|---|
| 1 | Múltipla escolha | 10 | 0 |
| 2 | V/F justificado | 10 | 5 |
| 3 | Múltipla escolha | 10 | 0 (mas (a) também aceitável) |
| 4 | V/F justificado | 10 | 5 |
| 5 | Trade-off (≥3 critérios) | 10 | ~3 pts por critério |
| 6 | Análise (escolha + 2 rejeições) | 10 | 4 escolha + 3 por rejeição justificada |
| 7 | Debug (2 causas + 2 correções) | 10 | 2,5 por item |
| 8 | Trade-off (topologia + justif.) | 10 | 6 escolha + 4 justificativa |
| 9 | Projeto (ADR) | 10 | 2 pts por seção do ADR preenchida |
| 10 | Projeto (Tree vs Recursive) | 10 | 5 distinção + 5 cenários |

---

## Nota esperada por perfil

- **5,0**: justifica topologias com ADR coerente, mede trade-offs, identifica sinais de evolução.
- **4,0**: escolhe bem topologias com justificativa sólida, pequenas lacunas.
- **3,0**: conhece nomes das topologias mas confunde critérios de escolha.
- **<3,0**: afirma mitos (mesh sempre escalável; hierarchical sempre para >2 workers).
