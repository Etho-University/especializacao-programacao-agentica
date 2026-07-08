# Variação: Mixture-of-Experts (routing por especialista)

## Intenção
Variação de **routing** onde cada ramo é um "especialista" treinado/configurado para um domínio. Inspirado em MoE clássico (transformers) mas em nível de workflow.

## Estrutura
```
input ─► [Router LLM] ─► especialista X ─► [LLM X com tools/prompt de domínio X]
                          especialista Y ─► [LLM Y com tools/prompt de domínio Y]
```

## Quando usar
- Domínios realmente distintos (SAP, Salesforce, GCP).
- Cada especialista tem tools/prompt/modelo próprio.
- Routing é confiável.

## Quando evitar
- Especialistas se sobrepõem (router confunde).
- Volume baixo por domínio.

## Custo
1 router + 1 especialista = 2 chamadas. Geralmente barato.

## Referências
- Shazeer et al. *Outrageously Large Neural Networks: The Sparsely-Gated MoE Layer* (clássico).
- Aplicações modernas em routing LLM (GPT-4 MoE internals).
