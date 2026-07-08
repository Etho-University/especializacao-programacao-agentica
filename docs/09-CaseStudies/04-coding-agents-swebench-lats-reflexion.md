# Caso de Estudo — Coding agents no SWE-bench com padrões avançados

> ETHAGT04 · LATS, Reflexion e Plan-and-Execute em código.

## Contexto

Vários coding agents de pesquisa (SWE-agent, AutoCodeRover, Agentless, Devin) combinam padrões avançados de raciocínio para resolver issues do SWE-bench. O ReAct puro é insuficiente para issues complexas; a arquitetura típica combina padrões.

## Arquitetura típica

```
issue (texto)
   │
   ▼
[Plan-and-Execute]  ── entender issue, decomor o que investigar
   │
   ▼
[ReAct]  ── explorar código (ler arquivos, rodar testes)
   │
   ▼ falha no patch
[Reflexion]  ── reflexão verbal orienta próxima edição
   │
   ▼ (problemas difíceis)
[LATS]  ── explorar múltiplas abordagens com backtracking
   │
   ▼
patch final
```

## Resultados empíricos

Agentes que combinam padrões superam ReAct-only em ~10-20 pontos percentuais no SWE-bench Verified. A escolha da estratégia de raciocínio é **decisão arquitetural de primeira classe**, não detalhe.

## Lições

1. **Nenhuma estratégia é universal** — a combinação vence.
2. **Reflexion é particularmente útil em código** porque os testes dão sinal claro de falha.
3. **LATS é caro** — reserve para casos difíceis, não para todos.
4. **Plan-and-Execute economiza tokens** quando a estrutura do problema é previsível.

## Referências

- Yang et al. *SWE-agent*. arXiv:2405.15793.
- Zhang et al. *AutoCodeRover*. arXiv:2404.05427.
- Jimenez et al. *SWE-bench*. arXiv:2310.06770.
