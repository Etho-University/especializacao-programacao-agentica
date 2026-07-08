# Caso de Estudo — Anthropic Coding Agent no SWE-bench

> ETHAGT01 · Aplicação real dos conceitos do curso.

## Contexto

O **SWE-bench** (Jimenez et al., arXiv:2310.06770) é um benchmark que mede a capacidade de sistemas resolverem issues reais de repositórios open source Python (Django, scikit-learn, sympy, etc.). Um subconjunto *Verified* foi curado para garantir que a issue é resolvível e verificável por testes.

A Anthropic desenvolveu um **coding agent** baseado em Claude que, dado apenas o texto da issue (típico de um PR description), produz um patch que passa nos testes. Esse caso ilustra todos os conceitos de ETHAGT01.

## Arquitetura (aproximação pública)

```
   issue (texto) ──► [Augmented LLM: Claude + tools + memória de repo]
                              │
                              ▼
                    ┌──── Agent Loop (limitado) ────┐
                    │  Thought: entender a issue      │
                    │  Action:  view_file(path)       │
                    │  Observation: conteúdo do arquivo│
                    │  Thought: localizar bug         │
                    │  Action:  edit_file(...)        │
                    │  Observation: diff aplicado     │
                    │  Action:  run_tests()           │
                    │  Observation: testes passaram   │
                    │  Thought: pronto, submeto patch │
                    └─────────────────────────────────┘
                              │
                              ▼
                       patch (diff)
```

## Conceitos de ETHAGT01 em ação

| Conceito | No coding agent |
|---|---|
| **Augmented LLM** | Claude com tools de manipulação de repo, memória do estado dos arquivos |
| **Agent loop (ReAct-like)** | Cada iteração: pensa → edita → observa (testes) → repete |
| **Ground truth per-step** | Resultado dos testes é fato real do ambiente (não alucinável) |
| **Workflow vs Agente** | É **agente autônomo** — passos não são predefinidos, dependem da issue |
| **ACI trabalhada** | Anthropic gastou **mais tempo nas tools** do que no prompt principal |
| **max_steps + sandbox** | Execução isolada em container; limite de iterações; orçamento |

## A lição ACI (central para ETHAGT02)

Em entrevista pública (Albert & Schluntz, *Building more effective AI agents*, YouTube), Schluntz relata um caso emblemático:

> Após o agente "sair" do diretório raiz, começou a usar paths relativos errados. Em vez de mexer no prompt, **mudaram a tool** para exigir **paths absolutos** — e o erro desapareceu.

Essa é a essência do princípio ACI: investir na interface da tool ( HCI :: ACI ) tantas vezes quanto na interface humano-computador. Ferramenta bem desenhada > prompt melhor.

## Resultados

Claude 3.5 Sonnet (out/2024) atingiu ~49% no SWE-bench Verified (state-of-the-art na época); Sonnet 4.5 elevou essa marca substancialmente em 2025. Mais relevante que os números absolutos: a **arquitetura** é simples nos blocos — Augmented LLM + loop + ACI + sandbox. Não há "magia".

## Lições para a Especialização

1. **Comece pelo bloco fundamental** — o coding agent não usa nada além do que ETHAGT01 ensina.
2. **ACI é onde mora a confiabilidade** — Gastar tempo em descrições e schemas de tools rende mais que mexer no prompt principal.
3. **Sandboxing + limites** são inegociáveis em agentes que agem no mundo.
4. **Observabilidade via traces** é o que permite iterar — sem traces, melhoria é adivinhação.
5. **Workflow vs Agente**: este é um caso clássico onde agente é a escolha certa — não dá para predefinir passos para uma issue arbitrária.

## Referências

- Jimenez, C. et al. *SWE-bench: Can Language Models Resolve Real-World GitHub Issues?* arXiv:2310.06770.
- Anthropic. *Building Effective Agents* (Appendix 1, "Coding Agents"). dez/2024.
- Albert, A. & Schluntz, E. *Building more effective AI agents* (YouTube).
