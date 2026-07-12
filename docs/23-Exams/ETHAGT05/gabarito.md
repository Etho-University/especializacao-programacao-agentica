# ETHAGT05 — Gabarito da Prova

> Restrito a mentores. Respostas esperadas e critérios de correção para [`prova.md`](prova.md).

## Parte 1 — Conceitos

**1. (b) Working · Episódica · Semântica · Procedural.** As quatro camadas canônicas, com inspiração cognitiva (Tulving) tratada como categorias de engenharia, não modelos neurológicos. Ref.: Capítulo 1 — Tipos de memória, §1.3.

**2. VERDADEIRO.** Working memory = janela de contexto (tokens), efêmera. Persistent memory = armazenamento externo (banco, vector store), durável. A distinção é temporal e técnica. Ref.: Capítulo 1, §1.3 (tabela das quatro camadas).

**3. (b) Vector store + metadados.** A memória episódica registra eventos com timestamp; o recall é feito por similaridade semântica (embedding) com filtragem por metadados (usuário, sessão, período). Ref.: Capítulo 1, §1.3 e Capítulo 4 — Memória vetorial.

**4. FALSO.** Nem todo agente precisa das quatro camadas. Um chatbot de FAQ precisa só de working memory (e talvez semântica). A regra: **adicione uma camada quando houver evidência de que o agente precisa dela** — não por padrão. Cada camada adiciona complexidade, custo e vetores de falha. Ref.: Capítulo 1, §1.4.

## Parte 2 — Aplicação e trade-off

**5.** HITL pausa a execução para aguardar confirmação humana. Sem checkpointer, o estado do agente se perde na pausa (o processo termina). O checkpointer **serializa o estado** a cada passo; ao retomar (horas/dias depois), o estado é restaurado. Sem isso, HITL longo é impossível — não há como pausar e continuar. Ref.: Capítulo 2 — Checkpointer, §2.3 (Resume).

**6.** A fórmula dos Generative Agents combina três fatores num score único: **recency** (quão recente — decai exponencialmente com o tempo), **importance** (quão importante — score atribuído na gravação), **relevance** (quão relevante à situação atual — similaridade semântica). O score = `f(recency, importance, relevance)` determina quais memórias são trazidas à working memory. Ref.: Capítulo 3 — Gerenciamento de contexto, §3.4.

**7.** Três estratégias para fatos que mudam: (i) **Timestamping** — cada fato tem validade (desde/quando); (ii) **Invalidação** — um fato novo conflitante invalida o antigo (ou ambos coexistem com data); (iii) **Decaimento** — fatos não acessados há muito tempo perdem confiança. A memória estruturada como knowledge graph oferece ferramentas naturais para isso (nós com atributos temporais). Ref.: Capítulo 5 — Memória semântica, §5.3.

**8. FALSO.** Para consultas exatas por chave estruturada ("qual o CPF?"), uma base **relacional** é superior: mais barata, mais precisa, mais consistente. A memória vetorial brilha em *recall aproximado por semântica* ("eventos parecidos com isto"). Regra: vetorial para similaridade, relacional para fatos estruturados, grafos para relações. Ref.: Capítulo 4, §4.3.

## Parte 3 — Projeto curto

**9.** Espera-se sumarização em cascata:
```python
def gerenciar_contexto(mensagens, max_tokens):
    while contar_tokens(mensagens) > max_tokens:
        antigas = mensagens[:K]
        resumo = llm_summarize(antigas)
        mensagens = [{"role": "system", "content": "Resumo da conversa: " + resumo}] + mensagens[K:]
    return mensagens
```
Avaliar: loop enquanto excede limite, sumariza as K mais antigas, substitui por resumo. Ref.: Capítulo 3, §3.3.

**10.** Exemplos esperados:
- **Working:** "a conversa atual, incluindo o que o usuário acabou de pedir" (context window).
- **Episódica:** "o usuário pediu ajuda com deploy na terça passada" (vector store, recall por similaridade).
- **Semântica:** "o usuário é VIP desde 2024, prefere resposta por e-mail" (KB/Postgres, fato consolidado).
- **Procedural:** "sempre que o usuário reclamar de lentidão, verificar logs antes de sugerir soluções" (skill/reflexão aprendida).

Ref.: Capítulo 1, §1.3 e Capítulo 5, §5.4.

---

## Nota esperada por perfil

- **5,0**: domina as 4 camadas, justifica quando usar cada, implementa checkpointer e eviction.
- **4,0**: diferencia tipos de memória, com pequenas imprecisões em implementação.
- **3,0**: conhece os tipos mas não articula trade-offs de custo/privacidade.
- **<3,0**: precisa revisar arquitetura de memória.
