# SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

> **Autores**: Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan  
> **Venue/Ano**: ICLR 2024 · arXiv:2310.06770  
> **URL**: https://arxiv.org/abs/2310.06770

## TL;DR
SWE-bench é um benchmark onde agentes recebem uma issue real de GitHub e devem produzir um patch que resolve a issue, validado por testes.

## Contribuições
- Benchmark realista: issues reais de Django, scikit-learn, sympy, etc.
- Avaliação automática via testes existentes
- Subconjunto *Verified* curado para resolubilidade

## Método
Cada instância = repositório + issue (+ pull request de referência). Agente recebe descrição da issue e ambiente isolado. Deve gerar um patch. Avaliação: o patch passa nos testes associados?

## Resultados
- Melhores agentes (2024): ~30% resolve rate no SWE-bench Verified
- Claude 3.5 Opus + agent: ~49% (estado da arte 2024)
- Lacuna grande para humanos (~80%+)

## Limitações
- Sobre Python (3 frameworks). Não cobre JS, Java, Go
- Só bugs com teste existente
- Super-representa bugs simples vs complexos

## Relação com a Especialização
**Benchmark principal de ETHAGT12**. SWE-bench é o benchmark mais usado para coding agents. Discussão em ETHAGT12 (como medir agentes). Caso de estudo 1 (`09-CaseStudies/01-anthropic-swe-bench-coding-agent.md`) detalha implementação.
