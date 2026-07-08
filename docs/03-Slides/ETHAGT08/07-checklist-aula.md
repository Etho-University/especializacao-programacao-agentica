# ETHAGT08 — Checklist da Aula

> Checklist para o professor verificar antes, durante e depois da aula.

---

## Pré-Aula (24h antes)

### Preparação Técnica
- [ ] Python 3.11+ instalado com `pip install mcp` (FastMCP)
- [ ] Node.js 18+ instalado com `npx @modelcontextprotocol/inspector` testado
- [ ] VS Code aberto com código do Lab 1 (`05-Labs/ETHAGT08/Lab1-Primeiro-MCP-Server`)
- [ ] Terminal testado: server FastMCP sobe em stdio sem erro
- [ ] Claude Desktop (ou OpenCode) instalado e com config de MCP testada
- [ ] `OPENAI_API_KEY` ou `ANTHROPIC_API_KEY` configurada e testada
- [ ] MCP Inspector abrindo e listando tools do server de teste
- [ ] Screenshot do trace de tool call salvo (plano B se DEMO falhar)
- [ ] Projetor testado
- [ ] Slides exportados para PDF (plano B se apresentação falhar)

### Preparação de Conteúdo
- [ ] Revisar todas as notas do professor (70 slides)
- [ ] Ensaiar a DEMO (Slide 29) — rodar pelo menos 2x antes
- [ ] Verificar spec MCP atual (modelcontextprotocol.io/specification) — confirmar 2025-11-25 ainda vigente
- [ ] Confirmar que todos os diagramas estão legíveis
- [ ] Preparar handout (opcional): storyboard impresso

### Preparação de Logística
- [ ] Sala reservada para 90 min + 15 min de buffer
- [ ] Quadro branco disponível
- [ ] Acesso ao repositório da especialização confirmado
- [ ] Wi-Fi estável (necessário para remote servers e API do LLM)

---

## Durante a Aula

### Bloco 1 (45 min)
- [ ] **Slide 1-6 (8 min)**: Abertura — anotar experiência da turma com MCP
- [ ] **Slide 5**: Fazer a pergunta de mão levantada ("Quantas integrações LLM↔sistemas?")
- [ ] **Slide 8**: Mostrar o diagrama host-client-server — destacar que LLM vive no host
- [ ] **Slide 9**: Reforçar que HTTP+SSE está deprecated; Streamable HTTP é o atual
- [ ] **Slide 15**: Mostrar o diagrama de capabilities — destacar sampling como inversão
- [ ] **Slide 17**: Reforçar Resource ≠ Tool (dado passivo vs ação ativa)
- [ ] **Slide 19**: Destacar que sampling nunca dá acesso direto ao LLM ao server
- [ ] **Slide 22-23**: Mostrar código FastMCP ao vivo — type hints → schema
- [ ] **Slide 29 (5 min)**: DEMO AO VIVO — se API/host falhar, usar screenshot do trace
- [ ] **Slide 30**: Pergunta da demo — deixar 2 min em duplas
- [ ] Intervalo (5 min)

### Bloco 2 (45 min)
- [ ] **Slide 31-38 (10 min)**: Clients e hosts
- [ ] **Slide 33**: Mostrar config JSON real do Claude Desktop
- [ ] **Slide 38**: Discussão aberta — deixar 2 min sobre seleção de tools
- [ ] **Slide 39-46 (10 min)**: Governança
- [ ] **Slide 43**: Reforçar SBOM e provenance — supply chain é crítico
- [ ] **Slide 46**: Discussão sobre ownership — anotar quem é dono na empresa deles
- [ ] **Slide 47-54 (10 min)**: Segurança
- [ ] **Slide 50**: Destacar prompt injection via resources como vetor #1
- [ ] **Slide 51**: Mostrar fluxo OAuth 2.1 — PKCE obrigatório
- [ ] **Slide 54 (3 min)**: Exercício de path traversal — individual + share
- [ ] **Slide 56-57**: Boas práticas e anti-patterns — pedir exemplos da turma
- [ ] **Slide 58**: Casos reais (Anthropic, Block, Replit) — destacar padrão comum
- [ ] **Slide 59 (5 min)**: Exercício config + threat model — individual + share
- [ ] **Slide 60-61**: Resumo e checklist
- [ ] **Slide 62-66 (5 min)**: Quiz — individual, sem consulta
- [ ] **Slide 67-69**: Projeto, labs, próximos passos
- [ ] **Slide 70 (2 min)**: Q&A

---

## Pós-Aula

### Avaliação
- [ ] Contar resultados do quiz (≥3 acertos = compreensão básica)
- [ ] Anotar perguntas frequentes no Q&A para futuras iterações
- [ ] Pedir feedback informal: "Uma coisa que você aprendeu hoje sobre MCP"
- [ ] Verificar tempo real vs planejado por seção
- [ ] Avaliar qualidade das mitigações propostas no exercício de path traversal (Slide 54)

### Follow-up
- [ ] Enviar leitura recomendada (spec MCP + Anthropic blog) no Slack/email
- [ ] Disponibilizar slides (PDF + repositório)
- [ ] Lembrar prazo do Lab 1 (1 semana)
- [ ] Lembrar prazo do Projeto (2 semanas)
- [ ] Preparar ETHAGT13 (a próxima aula aprofunda threat modeling)

---

## Sinais de Alerta Durante a Aula

| Sinal | Ação |
|---|---|
| Alunos confundem Resource com Tool (Slide 17) | Reforçar com exemplo: "ler config" = resource; "salvar config" = tool |
| DEMO do Slide 29 falha (host não conecta) | Screenshot do trace pré-gravado; não improvisar |
| Alunos sem pré-requisito de ETHAGT02 (tool calling) | Direcionar para revisão do ETHAGT02; oferecer pair programming nos labs |
| Tempo estourado no Bloco 1 | Cortar exercício do Slide 30 (duplas), mover para homework |
| Tempo estourado no Bloco 2 | Reduzir quiz para 3 perguntas (Slides 62-64); referências como leitura |
| Nenhuma pergunta no Q&A | Fazer pergunta inversa: "Qual parte de MCP foi menos clara?" |
| Turma confunde sampling (Slide 19) | Refazer o diagrama no quadro — destacar inversão de direção |
| Spec MCP atualizada desde a preparação | Anunciar mudanças no Slide 1; referenciar modelcontextprotocol.io/specification |

---

## Validação de Objetivos (Slide 61)

Antes de encerrar, confirmar com a turma:

- [ ] **Objetivo 1** (arquitetura MCP): coberto nos Slides 7-13
- [ ] **Objetivo 2** (construir servers): coberto nos Slides 21-29 (incluindo DEMO)
- [ ] **Objetivo 3** (integrar a hosts): coberto nos Slides 31-38
- [ ] **Objetivo 4** (governança): coberto nos Slides 39-46
- [ ] **Objetivo 5** (segurança): coberto nos Slides 47-54

Se algum objetivo não foi bem absorvido, indicar leitura específica na seção de referências.

---

> **Mantido por**: Universidade Etho · Versão 1.0 · Julho 2026
> **Spec de referência**: MCP Specification 2025-11-25 (modelcontextprotocol.io)
