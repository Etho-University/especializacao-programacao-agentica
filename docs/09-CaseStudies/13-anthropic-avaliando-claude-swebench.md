# Caso de Estudo — Anthropic avaliando Claude no SWE-bench

> ETHAGT12 · Processo de avaliação dirigido por dados.

## Contexto

Anthropic publicou detalhes de como avalia o coding agent de Claude no **SWE-bench Verified**. É um caso emblemático de AgentOps aplicado.

## Processo

1. **Subconjunto curado**: 500 issues com verificação humana (remover ambíguas/quebradas).
2. **Métrica principal**: % resolvido (testes automatizados passam).
3. **Métricas secundárias**: custo por issue, latência, número médio de steps.
4. **Análise de falhas por categoria**: multi-arquivo, dependências complexas, refatoração, etc.
5. **Iteração dirigida**: cada versão do agente visava categorias onde a anterior falhava.

## Resultados observados

- Cada versão de Claude (3.5 → 4 → 4.5) mostrou melhoria mensurável no benchmark.
- Melhorias direcionadas por categorias de falha, não por "tentativa e erro".
- Trade-offs explícitos: custo aumentou com capacidades.

## Lições

1. **Avaliação contínua direciona melhoria** — sem eval estruturado, "melhoria" é achismo.
2. **Análise de falhas por categoria** é mais útil que score agregado.
3. **Trade-offs explícitos** (custo × qualidade) informam decisões de produto.
4. **Verificação humana** do benchmark é essencial (dados ruidosos distorcem).

## Referências

- Anthropic *Building Effective Agents* (Appendix 1, 2024).
- Jimenez et al. *SWE-bench*. arXiv:2310.06770.
