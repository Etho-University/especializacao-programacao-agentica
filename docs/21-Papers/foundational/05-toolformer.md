# Toolformer: Language Models Can Teach Themselves to Use Tools

> **Autores**: Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, Thomas Scialom  
> **Venue/Ano**: NeurIPS 2023 · arXiv:2302.04761  
> **URL**: https://arxiv.org/abs/2302.04761

## TL;DR
Toolformer ensina LLMs a usar ferramentas via self-supervision: o modelo gera chamadas de API em texto, e se a chamada reduz a perplexidade, ela é mantida no fine-tuning.

## Contribuições
- Método self-supervised para LLMs aprenderem tool use
- Sem necessidade de demonstrações humanas de tool calling
- Ferramentas: calculadora, QA, search, tradutor, calendário

## Método
Para cada ferramenta: (1) amostrar chamadas candidatas via few-shot, (2) executar a ferramenta e obter resultado, (3) verificar se incluir a chamada reduz perplexidade na predição do próximo token, (4) fine-tuning nos exemplos que passaram no filtro.

## Resultados
- Mantém performance em linguagem natural (não degrada)
- Melhora em tarefas que exigem cálculo, busca, data
- Generaliza para ferramentas não vistas durante fine-tuning

## Limitações
- Só ferramentas que retornam texto
- Decisão binária (usa ou não), sem raciocínio sobre *qual* ferramenta
- Fine-tuning caro; desatualizado vs function calling nativo de GPT-4/Claude

## Relação com a Especialização
**Fundamento de ETHAGT02** (Tool Use & ACI). Toolformer é o paper seminal de tool use; Function Calling moderno e MCP são evoluções. Conceito de ACI (Agent-Computer Interface) é resposta às limitações do Toolformer.
