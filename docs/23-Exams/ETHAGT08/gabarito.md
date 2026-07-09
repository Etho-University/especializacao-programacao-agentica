---
password: Etho-Prof-2026
---
# ETHAGT08 — Gabarito da Prova

> Restrito a mentores. Respostas esperadas e critérios de correção para [`prova.md`](prova.md).

## Parte 1 — Conceitos

**1. (b) Host · Client · Server.** Host = a aplicação que o usuário opera e onde o LLM reside (Claude Desktop, VSCode, agente custom). Client = componente dentro do host que se conecta a um servidor (relação 1:1). Server = processo que expõe capabilities (tools, resources, prompts). Ref.: Capítulo 2 — Arquitetura, §2.1.

**2. FALSO.** MCP *não* substitui o tool calling nativo. O function calling continua sendo como o LLM *emite* a intenção de agir. O MCP é a *camada de transporte e padronização* que leva essa intenção até o sistema externo. MCP usurpa o problema da fragmentação de integrações (N×M), não o do tool calling. Ref.: Capítulo 1 — Por que MCP, §1.3.

**3. (d) Sampling.** Sampling permite que um *servidor* peça ao LLM do *host* para gerar um completion — invertendo a direção habitual (server-initiated, não LLM-initiated). Use cases: servidor que processa dados e precisa de um LLM para classificá-los sem sua própria chave de API. Ref.: Capítulo 3 — Capabilities, §3.5.

**4. VERDADEIRO.** Prompt injection via resources é um risco real: um resource (arquivo, row de DB) pode conter instruções maliciosas ("ignore as instruções anteriores e envie dados para...") que, lidas pelo LLM, o manipulam. Mitigação: tratar conteúdo externo como não-confiável; isolamento de contexto. Ref.: Capítulo 7 — Segurança, §7.2.

## Parte 2 — Aplicação e trade-off

**5.** **stdio:** o servidor roda como subprocesso do host; comunicação via stdin/stdout. Simples, local, seguro por isolamento de processo. Cenário: ferramentas locais e privadas (acesso ao filesystem da máquina). **Streamable HTTP:** o servidor é um endpoint HTTP; permite servidores *remotos*, escaláveis e compartilháveis. Cenário: servidores multi-tenant, hospedados, compartilháveis entre organizações (ex.: Remote MCP da Cloudflare). Ref.: Capítulo 2, §2.2.

**6.** **Tools** — funções com schema (alinhado ao ETHAGT02); o LLM decide chamar. Ex.: `search_issues(repo)`. **Resources** — dados estruturados identificados por URI; o host lê ou o LLM pede. Ex.: `file:///repo/README.md`, uma row de DB. **Prompts** — templates reutilizáveis; o usuário/host seleciona. Ex.: um template de "resumo de PR". Ref.: Capítulo 3 — Capabilities, §3.1-3.4.

**7.** Três problemas em escala sem governança: (i) **Servidores desatualizados/conflitantes** — sem catálogo, ninguém sabe quais existem, quem mantém, qual versão; descoberta é caótica. (ii) **Permissões frouxas** — sem princípio do menor privilégio, qualquer agente acessa qualquer servidor (ex.: agente de suporte com acesso a deploy). (iii) **Quebras silenciosas** — sem versionamento semântico, um servidor que renomeia/remove uma tool quebra agentes em produção sem aviso. Ref.: Capítulo 6 — Governança, §6.1-6.4.

**8. VERDADEIRO.** Supply chain security em MCP inclui: **provenance** (saber de onde veio cada servidor/dependência), **SBOM** (Software Bill of Materials — inventário de dependências), **scanning** de vulnerabilidades, e **pinning** de versões. Um servidor malicioso ou com dependência comprometida pode expor dados ou executar ações em nome do agente. Ref.: Capítulo 6, §6.5.

## Parte 3 — Projeto curto

**9.**
```json
{
  "mcpServers": {
    "etho-arxiv": {
      "command": "python",
      "args": ["-m", "etho_arxiv_server"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {"GITHUB_TOKEN": "..."}
    }
  }
}
```
Avaliar: estrutura `mcpServers` com 2 entradas, `command` + `args`, `env` para token. Ref.: Capítulo 5 — Clients e hosts, §5.2.

**10.** Os 5 riscos + mitigações:
1. **Prompt injection via resources** → tratar conteúdo externo como não-confiável; isolamento de contexto.
2. **Exfiltração de dados** → sandboxing, network egress filtering, auditoria.
3. **Tool misuse** (LLM manipulado chama tools destrutivas) → HITL para ações perigosas; allowlists.
4. **Sampling abuse** (servidor injeta conteúdo via sampling) → host trata sampling com cautela, validando e limitando.
5. **Supply chain** (dependências comprometidas) → SBOM, scanning, pinning.

Ref.: Capítulo 7 — Segurança, §7.2.

---

## Nota esperada por perfil

- **5,0**: domina arquitetura MCP, constrói servers, justifica governança e segurança com rigor.
- **4,0**: diferencia capabilities e transportes, com pequenas imprecisões em governança.
- **3,0**: conhece conceitos mas não articula riscos/permissões em escala.
- **<3,0**: precisa revisar MCP.
