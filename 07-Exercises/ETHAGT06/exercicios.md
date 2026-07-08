# ETHAGT06 — Lista de Exercícios

> Curso: RAG Agêntico. Fixação de conceitos. Use a apostila `04-Apostilas/ETHAGT06/apostila.md` como referência.

## Múltipla escolha

**1. No Corrective RAG (CRAG), quais são os três caminhos após avaliar os documentos recuperados?**

a) Traduzir, resumir, expandir
b) Usar os docs / corrigir (extração) / buscar na web como fallback
c) Ignorar, reescrever, cancelar
d) Classificar, ordenar, agrupar

**2. A técnica de HyDE (Hypothetical Document Embeddings) consiste em:**

a) Gerar uma resposta hipotética e usá-la como query de busca
b) Aumentar o número de documentos recuperados
c) Reescrever a query com sinônimos
d) Fazer re-ranking dos resultados

**3. Em Adaptive RAG, o agente decide:**

a) Qual modelo usar
b) Quando recuperar (ou responder direto) e quanto recuperar
c) Qual vector DB usar
d) Se deve usar fine-tuning

**4. Qual métrica de avaliação de RAG mede se a resposta é fiel aos documentos recuperados (sem alucinação)?**

a) Context precision
b) Faithfulness
c) Answer relevance
d) Context recall

## Verdadeiro ou Falso (justificado)

**1.** "Sempre adicionar mais documentos recuperados melhora a resposta." — Justifique.

**2.** "Self-RAG usa tokens de reflexão para decidir se a recuperação é necessária." — Justifique.

**3.** "HyDE é útil quando a pergunta do usuário é muito diferente do estilo dos documentos indexados." — Justifique.

**4.** "Agentic RAG com multi-hop encadeia múltiplas recuperações para responder perguntas complexas." — Justifique.

## Código curto

**1.** Escreva o pseudocódigo de um Corrective RAG: recuperar docs → avaliar relevância → decidir caminho (usar / corrigir / web).

**2.** Escreva um prompt de re-ranking que recebe 5 documentos e uma pergunta, e retorna os 3 mais relevantes com justificativa.

**3.** Escreva o pseudocódigo de um Agentic RAG multi-hop: o agente recupera, se insuficiente, reformula a query e recupera novamente (até N vezes).

## Análise de trade-off

**1.** Compare Adaptive RAG vs. Self-RAG. Qual a diferença fundamental?

**2.** Compare chunking semântico vs. chunking por tamanho fixo. Quando cada brilha?

**3.** Compare hybrid search (BM25 + densa) vs. apenas busca densa. Quando o híbrido vale o custo extra?

## Debug / diagnóstico

**1.** Um sistema RAG responde corretamente a perguntas fáceis mas falha sistematicamente em perguntas multi-hop. Diagnóstico provável e 2 correções.

**2.** O faithfulness do seu RAG é 0.60 (abaixo de 0.85 desejado). Liste 3 hipóteses de causa e uma correção para cada.
