# ETHAGT08 — Perguntas para Discussão

> Perguntas para estimular debate durante e após a aula.
> Organizadas por profundidade: rápida (1-2 min) → média (3-5 min) → profunda (10+ min).

---

## Perguntas Rápidas (1-2 min)

### Q1 — Experiência com MCP
"Quem aqui já ouviu falar do MCP? Quem já usou um server MCP em produção?"
- **Objetivo**: Calibrar o nível da turma
- **Slide**: 1
- **Ação**: Contar mãos levantadas — ajustar profundidade das explicações

### Q2 — Quantas Integrações?
"Quantas integrações diferentes vocês já fizeram para conectar LLMs a sistemas?"
- **Objetivo**: Tornar o problema N×M concreto
- **Slide**: 5
- **Resposta esperada**: Geralmente 3-5 por pessoa — mostra que o problema é real

### Q3 — Tool ou Resource?
"Para ler um arquivo de config, você usaria tool ou resource?"
- **Objetivo**: Fixar a distinção crítica
- **Slide**: 17
- **Resposta esperada**: Resource — é leitura passiva de dado. Tool é para ação.

### Q4 — Sampling na Prática
"Em qual caso de vocês um server precisaria pedir ao LLM do host para gerar texto?"
- **Objetivo**: Conectar sampling a casos reais
- **Slide**: 20
- **Resposta esperada**: Sumarização de dados locais, classificação, raciocínio sobre dados sem enviá-los ao LLM diretamente

### Q5 — Remote ou Local?
"Para um server de DB interno, vocês usariam stdio ou Streamable HTTP?"
- **Objetivo**: Praticar escolha de transporte
- **Slide**: 9
- **Resposta esperada**: stdio se o host está na mesma máquina; Streamable HTTP se o host é remoto ou múltiplos hosts compartilham o server

---

## Perguntas Médias (3-5 min)

### Q6 — Primeiro Server na Empresa
"Qual sistema da sua empresa você transformaria em MCP server primeiro? E quais dados você NÃO exporia?"
- **Objetivo**: Trazer MCP para a realidade deles
- **Slide**: 13
- **Ação**: Discussão em duplas (2 min) + share (1 min)
- **Respostas esperadas**: Servers: Salesforce, SAP, Confluence, Jira. Não expor: dados de RH sensíveis, dados de saúde (LGPD), chaves de API

### Q7 — O Que Acontece Se...?
"O que acontece se a tool retornar erro? E se o LLM chamar uma tool que não existe?"
- **Objetivo**: Pensar em error handling
- **Slide**: 30
- **Resposta esperada**: (1) O erro vira Observation — o LLM decide o que fazer. (2) O host retorna "tool not found" — o LLM corrige

### Q8 — Seleção de Tools
"Com 50 tools de 5 servers, como o LLM escolhe a certa? O que acontece quando tools têm nomes sobrepostos?"
- **Objetivo**: Pensar em escalabilidade de tools
- **Slide**: 38
- **Resposta esperada**: Descrições ricas (ACI), namespacing (`fs_read`, `gh_create_issue`), tool filtering dinâmico

### Q9 — Ownership dos Servers
"Servers de infra (filesystem, DB) — dono: platform team? Servers de domínio (Salesforce, SAP) — dono: biz team? Quem aprova a criação de um novo server?"
- **Objetivo**: Pensar em organização e governança
- **Slide**: 46
- **Ação**: Discussão aberta (2 min)
- **Resposta esperada**: Infra = platform team. Domínio = biz team dono do sistema. Aprovação: comitê de governança (platform + security + biz)

### Q10 — Path Traversal
"Se um MCP server de arquivos permite ler qualquer path, como você mitigaria?"
- **Objetivo**: Praticar mitigação de risco concreto
- **Slide**: 54
- **Ação**: 2 min individual + 1 min share
- **Respostas esperadas**: Roots (boundary), path validation (resolve + check prefix), sandbox FS, allowlist de extensões. Ideal: combinar todas

---

## Perguntas Profundas (10+ min)

### Q11 — MCP Substitui Tool Calling?
"Verdadeiro ou falso: MCP substitui o tool calling nativo do LLM. Justifique."
- **Objetivo**: Pensamento crítico sobre o papel do MCP
- **Slide**: 66 (quiz), mas pode aprofundar
- **Resposta esperada**: Falso. MCP padroniza o **protocolo** de comunicação host↔server. O modelo continua usando tool calling nativo. MCP é a camada de padronização, não substituição.
- **Contraponto**: Sem MCP, cada host reinventa o protocolo. Com MCP, há interoperabilidade.

### Q12 — Quando NÃO Usar MCP
"Em quais cenários MCP seria overengineering? Quando escrever um adapter custom é melhor?"
- **Objetivo**: Pensamento crítico sobre quando NÃO usar MCP
- **Slide**: 58 (fechamento)
- **Resposta esperada**: MCP é overengineering quando: (1) você tem 1 LLM e 1 sistema — adapter direto é mais simples; (2) a integração é tão específica que padronização não agrega; (3) latência crítica onde o overhead do protocolo é inaceitável. Use MCP quando há múltiplos LLMs ou múltiplos sistemas ou múltiplos hosts.

### Q13 — Server Malicioso no Catálogo
"Um server malicioso entra no catálogo interno. Qual o pior caso? Como você detectaria?"
- **Objetivo**: Threat modeling profundo
- **Slide**: 43, 50, 53
- **Resposta esperada**: Pior caso: backdoor para todos os hosts que usam o server. Vetores: exfiltração via sampling, prompt injection via resources, tool misuse. Detecção: auditoria central de chamadas, alertas de volume anômalo, sandbox com network egress monitorado, SBOM + scan regular.

### Q14 — Sampling em Produção
"Em produção, você habilitaria sampling em servers de terceiro? Quais as salvaguardas?"
- **Objetivo**: Decisão de segurança com trade-offs
- **Slide**: 19, 48
- **Resposta esperada**: Default: desabilitado para servers de terceiro. Se habilitar: (1) HITL obrigatório em todo sampling; (2) budget de tokens por sessão; (3) allowlist de operações; (4) log de todo sampling; (5) auditoria pós-call. Sem HITL, sampling é risco inaceitável.

### Q15 — Multi-Server vs Micro-Frontend
"MCP multi-server composition é análogo a microsserviços ou a micro-frontends? Quais as lições herdamos?"
- **Objetivo**: Conectar MCP a padrões arquiteturais conhecidos
- **Slide**: 37
- **Resposta esperada**: Mais análogo a microsserviços — servers são independentes, comunicam via host, podem ser owned por teams diferentes. Lições: (1) namespacing para evitar colisão; (2) versionamento independente; (3) circuit breaker para isolar falhas; (4) observabilidade distribuída (trace entre servers); (5) cuidado com transações distribuídas (MCP não fornece).

---

## Perguntas Bônus (para alunos avançados)

### Q16 — MCP vs Function Calling Padronizado
"Por que não simplesmente padronizar o schema de function calling entre provedores? O que MCP agrega além disso?"
- **Objetivo**: Questionar o design do MCP
- **Resposta**: Function calling padroniza o **formato** da chamada (JSON Schema da tool). MCP padroniza o **protocolo** de descoberta e comunicação — como o host descobre as tools do server, como negociam capabilities, como lidam com lifecycle, transportes, autenticação. Function calling é a ponta do iceberg; MCP é todo o resto.

### Q17 — Spec Evolution
"A spec MCP evoluiu de 2025-03-26 para 2025-11-25. O que mudou? Como você lida com breaking changes de spec?"
- **Objetivo**: Pensar em evolução de protocolo
- **Resposta**: Mudanças: HTTP+SSE deprecated, Streamable HTTP canônico, Elicitation adicionado, OAuth 2.1 formalizado. Lidar com breaking changes: negociação de versão no `initialize`, janela de deprecação, suporte a múltiplas versões no host.

### Q18 — Custom Host vs Host Pronto
"Quando vale a pena construir um host custom (agente) em vez de usar Claude Desktop/VSCode?"
- **Objetivo**: Trade-off build vs buy
- **Resposta**: Construa host custom quando: (1) precisa de controle fino do roteamento de tools; (2) integração com sistema legado específico; (3) multi-tenant com isolamento; (4) UX custom (não é chat). Use host pronto quando: (1) caso de uso é chat genérico; (2) time pequeno; (3) velocidade > controle.

### Q19 — Server com Estado
"MCP servers são stateless por padrão? Como lidar com servers que precisam de estado (ex.: sessão de DB)?"
- **Objetivo**: Pensar em arquitetura de server
- **Resposta**: MCP servers podem ter estado interno, mas o protocolo é stateless entre chamadas. Para sessão de DB: (1) abrir conexão no `initialize`, fechar no `shutdown`; (2) usar session ID do MCP; (3) para HTTP, usar `Mcp-Session-Id`. Não confie em estado entre chamadas sem ID de sessão.

### Q20 — MCP e LGPD
"Como MCP se relaciona com LGPD? Quais cuidados ao expor dados pessoais via resources?"
- **Objetivo**: Conectar a compliance
- **Resposta**: LGPD exige: (1) minimização — não exponha dados pessoais desnecessários via resource; (2) propósito — cada tool deve ter propósito claro; (3) consentimento — HITL para acessos a dados sensíveis; (4) auditoria — logs de quem acessou quais dados pessoais; (5) anonimização — servers podem anonimizar antes de retornar. MCP + LGPD = permissões granulares + auditoria + HITL.

---

> **Mantido por**: Universidade Etho · Versão 1.0 · Julho 2026
> **Spec de referência**: MCP Specification 2025-11-25 (modelcontextprotocol.io)
