# ETHAGT08 — Roteiro da Apresentação

> Universidade Etho · Especialização em Programação Agêntica
> Fase C — Multi-Agentes, Ferramentas e Orquestração · 25 h

---

## Metadados

| Campo | Valor |
|---|---|
| Código | ETHAGT08 |
| Título | MCP — Model Context Protocol (servers, clients, hosts, governança) |
| Duração | 90 min (2 blocos de 45 min) |
| Total de slides | 70 |
| Público | Arquitetos, Engenheiros de Software, Engenheiros de IA, DevOps/SRE, Tech Leads |
| Competências | C1 (A), C2 (B), C3 (A), C5 (B), C6 (I) |
| Spec de referência | MCP Specification 2025-11-25 |
| Laboratórios | Lab 1 (4 h) — Primeiro MCP Server · Lab 2 (5 h) — Multi-server (arXiv + GitHub) |

---

## Fluxo da Aula

### BLOCO 1 — 45 min

| Seção | Slides | Tempo | Objetivo |
|---|---|---|---|
| A — Abertura | 1-6 | 8 min | Engajar, contextualizar e estabelecer objetivos |
| B — Arquitetura MCP | 7-13 | 10 min | Host-client-server, transportes, ciclo de vida |
| C — Modelo de Capabilities | 14-20 | 12 min | Tools, resources, prompts, sampling, roots |
| D — Construindo Servers | 21-30 | 15 min | FastMCP, decorators, exemplos, DEMO |
| Intervalo | — | 5 min | — |

### BLOCO 2 — 45 min

| Seção | Slides | Tempo | Objetivo |
|---|---|---|---|
| E — Clients e Hosts | 31-38 | 10 min | Claude Desktop, VSCode, OpenCode, multi-server |
| F — Governança | 39-46 | 10 min | Catálogo, versionamento, permissões, SBOM |
| G — Segurança | 47-54 | 10 min | Boundary, sandbox, injection, OAuth 2.1 |
| H — Fechamento | 55-70 | 15 min | Boas práticas, casos reais, quiz, projeto, Q&A |
| Q&A extra | — | 10 min | Perguntas abertas |

---

## Pontos de Engajamento

| Slide | Tipo | Interação |
|---|---|---|
| 5 | Mão levantada | "Quantas integrações LLM↔sistemas vocês já escreveram?" |
| 13 | Duplas (2 min) | "Qual sistema da empresa viraria MCP server primeiro?" |
| 20 | Pergunta retórica | "Sampling: quando o server precisa gerar texto?" |
| 30 | Duplas (2 min) | "O que acontece se a tool retornar erro?" |
| 38 | Discussão aberta | "Com 50 tools, como o LLM escolhe a certa?" |
| 46 | Discussão aberta | "Quem é dono dos servers — platform ou biz team?" |
| 54 | Exercício individual | "Como mitigar path traversal em server de arquivos?" |
| 59 | Exercício individual + share | "Config JSON + 3 riscos de server de DB" |
| 62-66 | Quiz individual | 5 perguntas de múltipla escolha + V/F |

---

## Materiais Necessários

- [ ] Projetor / tela de compartilhamento
- [ ] VS Code aberto com código do Lab 1 (`05-Labs/ETHAGT08/Lab1-Primeiro-MCP-Server`)
- [ ] Terminal com Python 3.11+ e `pip install mcp` instalado
- [ ] Claude Desktop (ou OpenCode) instalado e configurado
- [ ] MCP Inspector disponível (`npx @modelcontextprotocol/inspector`)
- [ ] Acesso ao repositório da especialização
- [ ] Quadro branco (para diagramas improvisados)
- [ ] Handout: storyboard impresso (opcional)
- [ ] Screenshots de plano B: MCP Inspector, trace de tool call

---

## Riscos e Planos B

| Risco | Plano B |
|---|---|
| DEMO do Slide 29 falha (host não conecta ao server) | Mostrar screenshot do trace pré-gravado |
| Claude Desktop indisponível | Usar OpenCode ou MCP Inspector como host alternativo |
| Alunos sem pré-requisito de ETHAGT02 (tool calling) | Direcionar para revisão do ETHAGT02; oferecer pair programming nos labs |
| Tempo estourado no Bloco 1 | Cortar exercício do Slide 30 (duplas), mover para homework |
| Tempo estourado no Bloco 2 | Reduzir quiz para 3 perguntas (Slides 62-64); referências como leitura |
| Spec MCP atualizada desde a preparação | Anunciar mudanças no Slide 1; referenciar modelcontextprotocol.io/specification |

---

## Avaliação da Aula

- Quiz ao final (Slides 62-66): ≥3 acertos = compreensão básica
- Exercício de config + threat model (Slide 59): discussão individual + share
- Exercício de path traversal (Slide 54): profundidade das mitigações propostas
- DEMO (Slide 29): server rodando em host real — critério prático
- Feedback informal: "Uma coisa que você aprendeu hoje sobre MCP que não sabia"

---

## Conexões com Outros Módulos

| Conexão | Módulo | Relação |
|---|---|---|
| Pré-requisito | ETHAGT02 (Tool Calling & ACI) | Tool calling nativo = fundação do MCP Tools |
| Aplica em | ETHAGT13 (Segurança & Governança) | Aprofunda threat modeling e defesa |
| Aplica em | ETHAGT90 (Capstone) | Projeto integrador usa MCP servers |
| Complementa | ETHAGT09-10 (Multi-Agent) | Servers MCP como tools de agentes |

---

> **Mantido por**: Universidade Etho · Versão 1.0 · Julho 2026
> **Spec de referência**: MCP Specification 2025-11-25 (modelcontextprotocol.io)
