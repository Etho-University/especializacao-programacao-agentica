# ETHAGT02 — Slides Detalhados + Notas do Professor (Parte 2: Slides 27-60)

> Universidade Etho · Especialização em Programação Agêntica
> Continuação da Parte 1.

---

## SEÇÃO D — Engenharia de Tools (Slides 27-33 · 12 min)

---

### Slide 27 — [SEÇÃO] Engenharia de Tools

**Título**: 3 — Engenharia de Tools
**Objetivo**: Transição para o bloco de engenharia de robustez.
**Conteúdo**: Número "3" grande + "Engenharia de Tools"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "3" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Já vimos o mecanismo (como tool calling funciona) e a disciplina (como projetar bem com ACI). Agora vamos à engenharia de robustez: como fazer tools que NÃO QUEBRAM. Idempotência, timeouts, tipologia, versionamento. Esta é a diferença entre uma tool que funciona em demo e uma tool que funciona em produção com 10k usuários.
➡️ TRANSIÇÃO: "Comecemos pelos schemas — a fundação."

---

### Slide 28 — Schemas Claros: Pydantic, TypedDict, Zod

**Título**: Schemas Claros — Pydantic, TypedDict, Zod
**Objetivo**: Mostrar as ferramentas modernas para definir schemas de tools.
**Conteúdo**:
- **Problema**: escrever JSON Schema à mão é verboso e propenso a erro
- **Solução**: usar bibliotecas de schema que GERAM o JSON Schema automaticamente
- **Pydantic** (Python):
```python
from pydantic import BaseModel, Field, EmailStr

class SearchProductArgs(BaseModel):
    query: str = Field(description="Nome do produto. Ex.: 'iPhone 15'")
    category: str | None = Field(
        default=None,
        description="Categoria para filtrar.",
        pattern="^(electronics|clothing|food|books)$"
    )

# Gera o JSON Schema automaticamente
schema = SearchProductArgs.model_json_schema()
```
- **TypedDict** (Python): mais leve, sem validação runtime
- **Zod** (TypeScript/JS): equivalente do Pydantic no ecossistema JS
- **Vantagens**: type-checking, validação automática, documentação viva, menos boilerplate

**Diagrama**: Code block com Pydantic + JSON Schema gerado
**Animação**: Código Pydantic → JSON Schema (transformação)
**Imagem**: Logo Pydantic + TypeScript
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Escrever JSON Schema à mão é como escrever assembly — funciona mas é propenso a erro. As bibliotecas modernas (Pydantic em Python, Zod em JS) permitem definir o schema como uma classe/tipo, e geram o JSON Schema automaticamente. Vantagens: type-checking no seu editor, validação automática no runtime, documentação que nunca fica desatualizada, e menos boilerplate. Se vocês ainda escrevem JSON Schema à mão, mudem para Pydantic ou Zod hoje. É a diferença entre digitar HTML à mão e usar um componente React.
💡 ANALOGIA: É como a diferença entre escrever SQL cru e usar um ORM. O ORM gera o SQL, valida tipos, e mantém tudo consistente. Pydantic faz o mesmo para JSON Schema.
➡️ TRANSIÇÃO: "Agora, um conceito crítico para produção: idempotência."

---

### Slide 29 — Idempotência

**Título**: Idempotência — Retentativas sem Duplicação
**Objetivo**: Explicar idempotência e como implementá-la com request_id.
**Conteúdo**:
- **Definição**: uma operação é idempotente se executá-la N vezes tem o mesmo efeito que executá-la 1 vez
- **Por que importa em tool calling**:
  - Timeout: a tool executou, mas o agente não recebeu a resposta → retenta
  - Sem idempotência: retentativa duplica o efeito (email enviado 2x, pagamento 2x)
  - Com idempotência: retentativa é detectada e ignorada
- **Implementação: `request_id`** (ou idempotency key)
  - Toda chamada inclui um UUID único
  - O servidor verifica: se `request_id` já foi processado, retorna cache
  - Se não, processa e armazena
- **Exemplo** (send_email):
```json
{
  "request_id": "550e8400-e29b-41d4-a716-446655440000",
  "to": "cliente@email.com",
  "subject": "Confirmação",
  "body": "..."
}
```
- **Quando é essencial**: writes com external side-effect (email, payment, deploy)
- **Quando é dispensável**: reads puros (search, get)

**Diagrama**: `D6` — Fluxo de sequência com request_id (retry → dedup)
**Animação**: Setas do fluxo aparecem; retry destacado
**Imagem**: Diagrama D6
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Idempotência é o conceito mais importante para tools em produção. Imagine: o agente chama `send_email`. O email é enviado. Mas a rede cai no caminho de volta — o agente não recebe a confirmação. Ele acha que falhou e retenta. Sem idempotência: o cliente recebe 2 emails. Com idempotência: a retentativa inclui o mesmo `request_id`, o servidor vê que já processou, e retorna o cache. Email enviado uma vez só. A implementação é simples: toda chamada inclui um UUID, o servidor usa como chave de deduplicação. Essencial em: email, pagamento, deploy. Dispensável em: search, get (reads puros não têm side-effect).
💡 ANALOGIA: É como o comprovante de votação. Você só pode votar uma vez porque seu título é marcado. Mesmo que tente votar de novo, o sistema detecta a duplicata. `request_id` é o título de eleitor da tool call.
❓ PERGUNTA PARA A TURMA: "Vocês têm idempotência nas tools de escrita de vocês?" (Quase ninguém tem — este é o ponto)
⚠️ ERROS COMUNS: Alunos acham que idempotência é só para APIs de pagamento. Não — toda tool com external side-effect precisa. Email duplicado é tão ruim quanto pagamento duplicado.
➡️ TRANSIÇÃO: "Idempotência previne duplicação. Mas e se a tool travar? Timeouts."

---

### Slide 30 — Timeouts, Retries, Fallbacks

**Título**: Timeouts, Retries, Fallbacks — Três Camadas de Proteção
**Objetivo**: Mostrar as três camadas de proteção para tools em produção.
**Conteúdo**:
- **Camada 1: Timeout**
  - Toda tool tem um tempo máximo de execução
  - Ex.: `search_product` → timeout de 5s; `deploy` → timeout de 300s
  - Sem timeout: tool trava → agente trava → usuário espera infinitamente
- **Camada 2: Retry (com backoff)**
  - Se a tool falhar (timeout, erro transitório), tentar de novo
  - Backoff exponencial: 1s, 2s, 4s (não bombadeie o servidor)
  - Máximo de 3 retentativas
  - Combinar com idempotência (request_id)
- **Camada 3: Fallback**
  - Se todas as retentativas falharem, o que o agente faz?
  - Retornar erro estruturado: `{"error": "servidor indisponível", "suggestion": "tente mais tarde"}`
  - Ou usar tool alternativa (ex.: cache em vez de busca ao vivo)
- **Princípio**: o agente nunca deve "travar". Sempre ter uma resposta (mesmo que seja erro tratado).

**Diagrama**: 3 camadas empilhadas (timeout → retry → fallback)
**Animação**: Camadas aparecem de baixo para cima
**Imagem**: Ícones de relógio, loop, escudo
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Em produção, tools falham. Servidor cai. Rede oscila. API retorna 500. Sem proteção, o agente trava — fica esperando infinitamente ou quebra com exceção. As três camadas: (1) Timeout — toda tool tem um tempo máximo. Se exceder, aborta. (2) Retry — se a falha for transitória (timeout, 500), tenta de novo com backoff exponencial. Máximo 3 retentativas. Sempre combinado com idempotência para não duplicar. (3) Fallback — se tudo falhar, o agente precisa de uma resposta. Nunca deixem o agente sem saída. Retornem erro estruturado: o modelo recebe `{"error": "...", "suggestion": "..."}` e decide o que fazer — informar o usuário, tentar outra tool, ou desistir graciosamente.
💡 ANALOGIA: É como dirigir em estrada longa. Timeout é o tanque de gasória (não pode ir infinitamente). Retry é o estepe (se furar, troca). Fallback é o seguro (se tudo der errado, tem quem socorra). Sem nenhum dos três, você para no meio do nada.
➡️ TRANSIÇÃO: "Agora, uma tipologia que determina o nível de proteção."

---

### Slide 31 — Tipologia: Leitura / Escrita / Destrutiva / External

**Título**: Tipologia de Tools — 4 Tipos
**Objetivo**: Classificar tools por nível de risco para determinar proteções.
**Conteúdo**:
- **Tipo 1: Leitura (read)** — segura
  - `search`, `get_order`, `view_file`
  - Sem side-effect. Sem proteção especial.
- **Tipo 2: Escrita (write)** — reversível
  - `update_profile`, `create_cart`, `add_note`
  - Side-effect, mas pode ser desfeito. Log + validação.
- **Tipo 3: Destrutiva (destructive)** — irreversível
  - `delete_account`, `drop_table`, `remove_file`
  - Side-effect irreversível. **HITL OBRIGATÓRIO.**
- **Tipo 4: External side-effect** — afeta mundo externo
  - `send_email`, `deploy`, `transfer_money`, `post_tweet`
  - Side-effect fora do sistema. **HITL + dry-run + auditoria.**
- **Princípio**: o tipo determina o nível de governança
  - Read → nenhuma
  - Write → log
  - Destructive → HITL
  - External → HITL + dry-run + log de auditoria

**Diagrama**: `D7` — 4 quadrantes com tipo, exemplo, proteção
**Animação**: Quadrantes aparecem um a um (semáforo: verde → amarelo → vermelho)
**Imagem**: Semáforo de 4 cores
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esta tipologia é a base da governança de tools. Toda tool cai em um dos 4 tipos. Leitura é segura — sem side-effect, sem proteção. Escrita é reversível — tem side-effect mas pode ser desfeito, log é suficiente. Destrutiva é irreversível — HITL obrigatório, o humano precisa aprovar antes. External afeta o mundo fora do sistema — HITL + dry-run (preview antes de enviar) + log de auditoria (quem aprovou, quando, o quê). Esta classificação determina o nível de governança. Se vocês não sabem o tipo de cada tool de vocês, não conseguem proteger adequadamente.
💡 ANALOGIA: É como classificar procedimentos médicos. Consulta (read — seguro). Receita (write — reversível, para se descobrir erro). Cirurgia (destructive — irreversível, precisa consentimento = HITL). Transplante (external — afeta outro sistema, precisa consentimento + checklist + registro).
❓ PERGUNTA PARA A TURMA: "Pensem em uma tool de vocês — qual o tipo?" (Deixar 2-3 responderem)
➡️ TRANSIÇÃO: "E quando a tool precisa mudar? Versionamento."

---

### Slide 32 — Versionamento de Tools

**Título**: Versionamento de Tools — Sem Quebrar Agentes em Produção
**Objetivo**: Mostrar como evoluir tools mantendo compatibilidade retroativa.
**Conteúdo**:
- **Problema**: a tool precisa mudar (novo parâmetro, mudança de formato), mas agentes em produção dependem da versão atual
- **Regra 1: adições não quebram**
  - Adicionar parâmetro OPCIONAL é seguro — agentes antigos continuam funcionando
  - `category` com `default: null` → ok
- **Regra 2: remoções QUEBRAM**
  - Remover parâmetro que agentes usam → quebra
  - Solução: deprecation com sobreposição (manter ambas por um ciclo)
- **Regra 3: mudança de tipo QUEBRA**
  - `query: string` → `query: object` quebra
  - Solução: criar `search_product_v2` e manter `search_product` (deprecated)
- **Ciclo de depreciação**:
  1. Lançar v2
  2. Log de uso da v1
  3. Notificar consumidores
  4. Quando uso da v1 < 5%, desligar
- **Boa prática**: semver para tools (v1.0.0 → v1.1.0 adição, v2.0.0 breaking)

**Diagrama**: Timeline de versionamento (v1 → v1.1 → v2 com deprecation overlap)
**Animação**: Timeline cresce; período de overlap destacado
**Imagem**: Ícone de branch git
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Tools não são estáticas — evoluem. Mas agentes em produção dependem da versão atual. Mudar uma tool sem cuidado quebra agentes. As regras: (1) adicionar parâmetro opcional é seguro. (2) remover parâmetro quebra — use deprecation com sobreposição. (3) mudar tipo de parâmetro quebra — crie v2 e mantenha v1 viva durante a transição. O ciclo de depreciação: lançar v2, logar uso de v1, notificar, e só desligar v1 quando o uso cair abaixo de 5%. Use semver: v1.0.0 → v1.1.0 (adição) → v2.0.0 (breaking). Sem versionamento, vocês têm agentes que funcionavam ontem e quebraram hoje sem motivo aparente.
💡 ANALOGIA: É como mudar a numeração das salas de um escritório. Você pode ADICIONAR salas sem problema. Mas se RENUMERAR as existentes, quem tem o mapa antigo se perde. Por isso prédios mantêm numeração antiga durante reformas.
➡️ TRANSIÇÃO: "Uma decisão comum: 1 tool com mode ou 2 separadas?"

---

### Slide 33 — 1 Tool com Mode vs 2 Separadas

**Título**: 1 Tool com Mode vs 2 Separadas
**Objetivo**: Dar um critério prático para decidir entre consolidar ou separar tools.
**Conteúdo**:
- **Dilema**: `create_user` e `update_user` — 1 tool com `action: "create"|"update"` ou 2 tools?
- **A regra dos 80%**:
  - Se >80% dos casos usam AMBAS → consolidar em 1 tool com mode
  - Se raramente se sobrepõem → separar em 2 tools
- **Fatores a favor de consolidar**:
  - Menos tokens de descrição (economia)
  - Menos confusão de escolha (modelo escolhe entre 2 em vez de 8)
  - Parâmetros compartilhados (DRY)
- **Fatores a favor de separar**:
  - Governança diferente (create é seguro, delete é destrutivo → HITL)
  - Descrição mais específica por ação
  - Schema mais simples por tool
- **Exemplo**: `create_user` + `update_user` → consolidar (ambas escrita, mesma governança)
- **Exemplo**: `get_user` + `delete_user` → separar (read vs destructive, HITL só no delete)

**Diagrama**: Árvore de decisão (consolidar vs separar)
**Animação**: Ramos aparecem com critérios
**Imagem**: Ícone de bifurcação
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esta é uma dúvida frequente. A regra dos 80% resolve a maioria dos casos. Se mais de 80% dos casos usam ambas as ações juntas (ex.: admin panel que sempre cria e atualiza), consolidar em 1 tool com `mode` economiza tokens e reduz confusão. Se raramente se sobrepõem, separar. Mas há um fator decisivo: governança. Se uma ação é segura (create) e a outra é destrutiva (delete), SEPARAR — porque o HITL deve estar só no delete. Misturar em 1 tool força a mesma governança para ambas. Regra prática: se os tipos de risco são diferentes, separar. Se são iguais, avaliar a regra dos 80%.
💡 ANALOGIA: É como decidir entre uma faca multiuso (canivete suíço) e facas separadas. O canivete é prático se você usa todas as lâminas. Mas se uma lâmina é de serra (perigosa) e outra é de descascar maçã (segura), talvez separar faça sentido — você não quer a serra na mesma gaveta que a criança alcança.
➡️ TRANSIÇÃO: "Falando em perigo, vamos à seção mais importante do Bloco 2: HITL."

---

## SEÇÃO E — Tools Perigosas e HITL (Slides 34-36 · 5 min)

---

### Slide 34 — [SEÇÃO] Tools Perigosas e HITL

**Título**: 4 — Tools Perigosas e HITL
**Objetivo**: Transição para o bloco de governança e segurança.
**Conteúdo**: Número "4" grande + "Tools Perigosas e HITL"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "4" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Até agora falamos de tools que funcionam bem. Agora vamos falar de tools que podem CAUSAR DANO. Toda tool destrutiva ou com external side-effect é uma ferramenta de poder — e poder sem governança é perigoso. HITL (Human-in-the-Loop) é a governança. Esta seção é curta mas é a mais importante do Bloco 2 do ponto de vista de segurança.
➡️ TRANSIÇÃO: "Comecemos pela matriz de risco."

---

### Slide 35 — Matriz de Risco: Irreversível × Impactante

**Título**: Matriz de Risco — Quando HITL é Obrigatório?
**Objetivo**: Apresentar a matriz 2×2 que classifica tools por risco.
**Conteúdo**:
- **Dois eixos**:
  - **Reversibilidade**: a ação pode ser desfeita? (sim/não)
  - **Impacto**: qual o dano potencial? (baixo/alto)
- **4 quadrantes**:

| | Reversível | Irreversível |
|---|---|---|
| **Alto impacto** | update_profile, create_order | delete_account, deploy, transfer_money |
| **Baixo impacto** | get_order, search | log_event (sobrescreve) |

- **Governança por quadrante**:
  - Baixo impacto + reversível → sem HITL (search, get)
  - Baixo impacto + irreversível → HITL opcional (log)
  - Alto impacto + reversível → HITL opcional (update)
  - **Alto impacto + irreversível → HITL OBRIGATÓRIO** (delete, deploy, email)
- **Princípio**: HITL é proporcional ao dano potencial, não à complexidade

**Diagrama**: `12-Diagrams/ETHAGT02/risk-matrix.mmd`
**Animação**: Quadrantes aparecem um a um (cores: verde → amarelo → vermelho)
**Imagem**: Matriz 2×2 colorida
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A matriz de risco é a ferramenta de decisão para HITL. Dois eixos: reversibilidade (pode desfazer?) e impacto (quanto dano?). O quadrante crítico é alto impacto + irreversível: delete_account, deploy, transfer_money, send_email. Neste quadrante, HITL é OBRIGATÓRIO. Não é opcional — é não-negociável. Um agente que deleta conta de usuário sem confirmação humana é um acidente esperando para acontecer. Nos outros quadrantes, HITL é opcional ou desnecessário. O critério é o dano potencial, não a complexidade técnica. Uma tool simples (`drop_table`) pode causar mais dano que uma tool complexa (`generate_report`).
💡 ANALOGIA: É como a classificação de medicamentos. Tylenol (baixo impacto, reversível) — venda livre. Antibiótico (alto impacto, reversível) — precisa receita. Quimioterapia (alto impacto, irreversível side-effects) — precisa consentimento informado + assinatura. HITL é o consentimento informado do agente.
❓ PERGUNTA PARA A TURMA: "Quantas tools de vocês estão no quadrante vermelho (alto impacto + irreversível)? E quantas têm HITL?" (Quase sempre: gap entre as duas respostas)
➡️ TRANSIÇÃO: "Como implementar HITL? Vamos ao fluxo."

---

### Slide 36 — HITL: Confirmação, Dry-run, Simulação

**Título**: HITL — 4 Níveis de Intervenção Humana
**Objetivo**: Mostrar os 4 níveis de HITL e quando usar cada.
**Conteúdo**:
- **Nível 1: Confirmação explícita** (mínimo)
  - Humano aprova antes de executar: "Confirmar envio de email para X?"
  - Para: toda tool destrutiva
- **Nível 2: Dry-run / Preview**
  - Mostrar o que SERIA feito antes de fazer: "Preview do email: [corpo]. Enviar?"
  - Para: tools onde o conteúdo importa (email, mensagem)
- **Nível 3: Simulação completa**
  - Executar em ambiente isolado e mostrar resultado antes de produção
  - Para: deploy, migrações de banco
- **Nível 4: Allowlist dinâmico**
  - Humano aprova previamente quais tools/args são permitidos
  - Para: ambientes controlados (ex.: só deploy de branches aprovadas)
- **Exercício individual (2 min)**: classifique 5 tools por tipo e HITL necessário
  - `get_order_status`, `delete_account`, `send_email`, `deploy_to_production`, `search_products`

**Diagrama**: `12-Diagrams/ETHAGT02/hitl-flow.mmd`
**Animação**: Fluxo aparece: agente → runtime → humano → tool real
**Imagem**: Diagrama hitl-flow
**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: HITL não é binário (tem ou não tem) — tem 4 níveis. Confirmação explícita é o mínimo: humano clica "sim" antes de executar. Dry-run mostra o que seria feito: o agente prepara o email, o humano lê o preview, aprova, aí envia. Simulação completa executa em ambiente isolado: deploy em staging antes de produção. Allowlist é a forma mais restritiva: humano aprova previamente quais ações são permitidas (ex.: só deploy de branch `main` aprovada por 2 pessoas). O nível depende do dano potencial. Vejam o diagrama: o agente NUNCA tem acesso à tool real (`_send_email_real`). Ele chama `request_send_email`, o runtime pausa e serializa o estado, o humano vê o preview, aprova, e só então a tool real é executada — com log de auditoria. O agente nunca pode enviar email sem o humano. Esta separação é crítica.
💡 ANALOGIA: É como um cofre bancário. O gerente (agente) pede para abrir. O segurança (humano) confirma. Só depois o cofre abre. O gerente não tem a chave — o segurança tem. Sem o segurança, o cofre não abre, por mais que o gerente peça.
❓ PERGUNTA PARA A TURMA: "Vocês têm HITL em algum agente hoje? Como?" (A maioria não tem estruturado — "humano revisa depois" não é HITL)
➡️ TRANSIÇÃO: "Agora, os erros mais comuns e como avaliar."

---

## SEÇÃO F — Erros Comuns e Avaliação (Slides 37-44 · 10 min)

---

### Slide 37 — [SEÇÃO] Erros Comuns e Avaliação

**Título**: 5 — Erros Comuns e Avaliação
**Objetivo**: Transição para a seção de anti-patterns e avaliação.
**Conteúdo**: Número "5" grande + "Erros Comuns e Avaliação"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "5" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vimos como projetar bem. Agora vamos ver os 5 erros mais comuns — para vocês reconhecerem em código de vocês — e como avaliar empiricamente se as tools estão boas.
➡️ TRANSIÇÃO: "Comecemos pelos erros."

---

### Slide 38 — Os 5 Erros Mais Comuns

**Título**: Os 5 Erros Mais Comuns em Design de Tools
**Objetivo**: Visão geral dos 5 anti-patterns mais frequentes.
**Conteúdo**:
1. **Paths relativos** → exigir absolutos (poka-yoke)
2. **Muitas tools similares** → consolidar ou renomear
3. **Descrições vagas** → reescrever como docstring de júnior
4. **Schema frouxo** → apertar com enum/pattern/format
5. **Falta de erro tratado** → propagar com mensagem útil ao modelo

**Diagrama**: 5 cards com erro + correção
**Animação**: Cards aparecem um a um
**Imagem**: Ícones de erro/correção
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Estes são os 5 erros que eu vejo em 90% das code reviews de tools. Cada um tem uma correção direta. Vamos detalhar os dois primeiros nos próximos slides.
➡️ TRANSIÇÃO: "Erro 1 em detalhe."

---

### Slide 39 — Erro 1: Paths Relativos → Absolutos

**Título**: Erro 1 — Paths Relativos → Absolutos
**Objetivo**: Detalhar o caso canônico de poka-yoke com regex.
**Conteúdo**:
- **O erro**: tool aceita path relativo (`"src/main.py"`)
  - Modelo não sabe qual é o diretório atual
  - Após sair do raiz, path relativo quebra
- **A correção (poka-yoke)**: exigir path absoluto via regex
  - `pattern: "^/.+"` no schema
  - Modelo é FORÇADO a enviar `/repo/src/main.py`
- **Antes**:
```json
{"path": {"type": "string"}}
```
- **Depois**:
```json
{"path": {"type": "string", "pattern": "^/.+", "description": "Path absoluto. Ex.: '/repo/src/main.py'"}}
```
- **Resultado**: erro estruturalmente impossível

**Diagrama**: Antes/depois com regex destacado
**Animação**: Regex aparece com highlight
**Imagem**: Ícone de pasta/caminho
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Este é o erro #1 e a correção mais elegante. Path relativo é ambiguidade — o modelo não sabe de onde é relativo. A correção é um regex de uma linha: `^/.+`. A partir daí, o modelo SÓ PODE enviar path absoluto. Poka-yoke puro. O caso SWE-bench da Anthropic é exatamente isto.
➡️ TRANSIÇÃO: "Erros 2 e 3 rapidamente."

---

### Slide 40 — Erros 2 e 3: Tools Similares, Descrições Vagas

**Título**: Erros 2 e 3 — Tools Similares, Descrições Vagas
**Objetivo**: Mostrar como consolidar tools similares e reescrever descrições vagas.
**Conteúdo**:
- **Erro 2: Muitas tools similares**
  - Sintoma: `search_product`, `find_product`, `get_product`, `lookup_product` — todas fazem quase o mesmo
  - Problema: modelo não sabe qual escolher → escolhe errado ou fica paralisado
  - Solução: consolidar em UMA (`search_product`) ou renomear para deixar claro a diferença
- **Erro 3: Descrições vagas**
  - Sintoma: `"Busca dados."`, `"Processa requisição."`, `"Atualiza registro."`
  - Problema: modelo não sabe o que a tool faz, quando usar, nem que args passar
  - Solução: reescrever como docstring de júnior — o QUÊ, QUANDO, EXEMPLO
- **Antes**: `"Atualiza registro."`
- **Depois**: `"Atualiza o perfil de um cliente existente. Use quando o usuário quiser mudar nome, email ou endereço. NÃO use para criar novo cliente — use create_customer. Exemplo: update_profile(id='123', field='email', value='novo@email.com')"`

**Diagrama**: Antes/depois para cada erro
**Animação**: Transformação antes → depois
**Imagem**: Dois blocos comparativos
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Erro 2 é multiplicação desnecessária. Se vocês têm `search_product` e `find_product` que fazem quase o mesmo, o modelo fica confuso — qual usar? Consolidem em uma, ou deixem a diferença CRISTALINA nas descrições. Erro 3 é a descrição vaga — o anti-pattern mais comum. "Atualiza registro" é inútil para o modelo. Atualiza QÊ registro? Com quais campos? Quando usar vs criar? A regra: escrevam como se fosse para um estagiário júnior que não conhece o sistema.
➡️ TRANSIÇÃO: "Agora a parte mais importante do Bloco 2: como avaliar se as tools estão boas."

---

### Slide 41 — [SEÇÃO] Avaliando Tools

**Título**: 6 — Avaliando Tools
**Objetivo**: Transição para a subseção de avaliação empírica.
**Conteúdo**: Número "6" grande + "Avaliando Tools"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "6" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Como sabemos se uma tool está bem desenhada? Não é achismo — é medição empírica. Vamos falar de workbench: a ferramenta fundamental para iterar em tools.
➡️ TRANSIÇÃO: "O workbench."

---

### Slide 42 — Workbench: Rodar, Observar, Iterar

**Título**: Workbench — Rodar, Observar, Iterar
**Objetivo**: Apresentar o loop de avaliação empírica de tools.
**Conteúdo**:
- **Workbench** = ambiente de teste onde você roda N inputs e observa o comportamento do agente
- **O loop** (5 passos):
  1. **Design** da tool (nome, schema, descrição)
  2. **Rodar** 20+ casos de teste × 3 runs cada
  3. **Medir**: taxa de uso correto, custo, latência, erros
  4. **Diagnosticar**: erros são sistemáticos ou aleatórios?
  5. **Redesenhar** a tool (NÃO o prompt!) se houver erros sistemáticos
- **Princípio**: o workbench é onde ACI é VALIDADA, não na cabeça do desenvolvedor
- **Quantos casos**: mínimo 20; ideal 50+ para tools críticas
- **Por que 3 runs**: modelos são estocásticos — 1 run pode ser sorte. 3 runs dão variância.

**Diagrama**: `12-Diagrams/ETHAGT02/aci-iteration-loop.mmd`
**Animação**: Loop aparece e gira (design → bench → measure → diagnose → redesign)
**Imagem**: Diagrama aci-iteration-loop
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O workbench é a ferramenta mais importante desta aula para produção. É um ambiente onde vocês rodam casos de teste e observam o que o agente faz. O loop: designam a tool, rodam 20+ casos (3 runs cada para capturar variância), medem (taxa de uso correto, custo, latência), diagnosticam (erros sistemáticos vs aleatórios), e se houver sistemáticos, REDESENHAM A TOOL — não o prompt. Este é o ponto: se o erro é sistemático (acontece sempre), a causa é a tool. Se é aleatório (às vezes), pode ser o modelo. O workbench é onde a hipótese "esta tool está bem desenhada" é testada empiricamente. Sem workbench, vocês estão achando — e achismo não escala.
💡 ANALOGIA: É como um túnel de vento para aviões. Você não projeta uma asa e coloca no ar — testa no túnel de vento com N condições até validar. Workbench é o túnel de vento de tools.
➡️ TRANSIÇÃO: "O que medir no workbench?"

---

### Slide 43 — Métricas: Taxa de Uso, Custo, Latência

**Título**: Métricas — O Que Medir no Workbench
**Objetivo**: Definir as 4 métricas-chave e suas metas.
**Conteúdo**:
- **Métrica 1: Taxa de uso correto** (a mais importante)
  - % de casos onde o agente escolheu a tool certa com args certos
  - Meta: ≥85%
- **Métrica 2: Custo por chamada**
  - Tokens (in + out) × preço por 1M
  - Meta: <$0.01 por chamada (depende do caso)
- **Métrica 3: Latência**
  - p50 (mediana) e p95 (cauda)
  - Meta: p50 <3s, p95 <10s
- **Métrica 4: Taxa de erro**
  - % de chamadas que falharam (timeout, args inválidos, exceção)
  - Meta: <10%
- **Dashboard mínimo**: 4 cards com valor atual vs meta

**Diagrama**: `D11` — Dashboard mockup com 4 métricas
**Animação**: Cards aparecem um a um
**Imagem**: Dashboard com 4 KPIs
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Quatro métricas. Taxa de uso correto é a rainha — é o que define se a tool funciona. Custo por chamada é FinOps. Latência é UX (usuário desiste se demora). Taxa de erro é robustez. As metas são pontos de partida: 85% de uso correto, <$0.01, p50<3s, erro<10%. Ajustem conforme o caso. O dashboard mínimo: 4 cards com valor atual vs meta. Se a taxa de uso correto está em 60%, vocês têm trabalho de ACI pela frente. Se está em 90%, parabéns — agora otimizem custo e latência.
➡️ TRANSIÇÃO: "E como garantir que regressões não aconteçam? Testes."

---

### Slide 44 — Testes de Regressão para Tools

**Título**: Testes de Regressão para Tools
**Objetivo**: Mostrar como criar CI/CD para tools — evitar que mudanças quebrem o agente.
**Conteúdo**:
- **Problema**: você refatora uma tool para melhorar. Como saber se não quebrou algo?
- **Solução: conjunto de testes de regressão**
  - Os mesmos 20+ casos do workbench viram testes automatizados
  - A cada mudança de tool, roda os testes
  - Se taxa de uso correto cai abaixo do threshold, CI falha
- **Estrutura de um caso de teste**:
```python
def test_search_product_with_typo():
    result = run_agent("Tem ifone 15?", tools=[search_product])
    assert result["tool_called"] == "search_product"
    assert "iphone" in result["args"]["query"].lower()
    assert "preço" in result["response"].lower()
```
- **No CI/CD**: roda a cada PR que mexe em tools
- **Threshold**: se taxa de uso correto <85%, block merge

**Diagrama**: Pipeline CI/CD com gate de tool regression
**Animação**: Pipeline aparece; gate destacado
**Imagem**: Ícone de pipeline/gear
**Tempo**: 1.5 min

**Rodape**: PR = Pull Request — requisicao de pull (GitHub)

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O workbench é manual. O teste de regressão é automatizado. A ideia: os mesmos 20+ casos viram testes. A cada PR que mexe em tool, roda os testes. Se a taxa de uso correto cai abaixo de 85%, o CI bloqueia o merge. Isto é CI/CD para tools — garante que melhorias não causam regressões. Sem isto, vocês refatoram uma tool, acham que melhorou, mas quebraram 3 casos que funcionavam. E só descobrem em produção.
💡 ANALOGIA: É como testes unitários para código normal. Você não da deploy sem testes passando. O mesmo para tools: não da deploy sem workbench passando.
➡️ TRANSIÇÃO: "Vamos ao fechamento."

---

## SEÇÃO G — Fechamento (Slides 45-60 · 15 min)

---

### Slide 45 — [SEÇÃO] Boas Práticas e Fechamento

**Título**: 7 — Boas Práticas e Fechamento
**Objetivo**: Transição para o fechamento.
**Conteúdo**: Número "7" grande + "Boas Práticas e Fechamento"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "7" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vamos consolidar tudo que vimos em boas práticas (DO) e anti-patterns (DON'T). Esta é a parte que vocês devem anotar e levar para o trabalho.
➡️ TRANSIÇÃO: "Começando pelo que fazer."

---

### Slide 46 — Boas Práticas (DO)

**Título**: Boas Práticas — O Que Fazer
**Objetivo**: Checklist de boas práticas de design de tools.
**Conteúdo**:
- ✅ **Escreva descrições ricas** — o QUÊ, QUANDO, QUANDO NÃO, EXEMPLO
- ✅ **Use poka-yoke** — enum, format, pattern, required
- ✅ **Exija paths absolutos** (se aplicável) via regex
- ✅ **Use Pydantic/Zod** para gerar schemas (não escreva JSON à mão)
- ✅ **Implemente idempotência** (request_id) para tools com side-effect
- ✅ **Defina timeout** para toda tool
- ✅ **Trate erros** com mensagem estruturada útil ao modelo
- ✅ **Use HITL** para toda tool destrutiva/irreversível
- ✅ **Mantenha workbench** com 20+ casos de teste
- ✅ **Versione tools** com semver e ciclo de deprecation
- ✅ **Invista mais tempo em tools** do que no prompt principal

**Diagrama**: Checklist verde (`etho-success` #2D8659)
**Animação**: Itens aparecem um a um (on click)
**Imagem**: Ícones de check verde
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Cada item desta lista é uma lição que alguém aprendeu da forma difícil em produção. "Descrições ricas" é o princípio 2. "Poka-yoke" é o princípio 4. "Paths absolutos" é o caso SWE-bench. "Pydantic/Zod" é engenharia moderna. "Idempotência" é robustez. "Timeout" é não-travar. "Erro tratado" é resiliência. "HITL" é governança. "Workbench" é validação. "Versionamento" é evolução sem quebra. E o item mais importante: "invista mais tempo em tools do que no prompt". Se vocês só fizerem UM item desta lista, façam este.
💡 ANALOGIA: É como o checklist de pré-voo. Cada item parece óbvio, mas pilotos ainda esquecem. Checklist existe porque a memória falha.
➡️ TRANSIÇÃO: "Agora o que NÃO fazer."

---

### Slide 47 — Anti-Patterns (DON'T)

**Título**: Anti-Patterns — O Que NÃO Fazer
**Objetivo**: Checklist do que evitar em design de tools.
**Conteúdo**:
- ❌ **Descrição de 1 palavra** ("Busca.") — o modelo não sabe o que buscar
- ❌ **Schema sem `description` nos parâmetros** — args opacos
- ❌ **`string` livre onde cabe `enum`** — modelo alucina valores
- ❌ **Path relativo** em tools de arquivo — ambiguidade
- ❌ **Sem `required`** — modelo não sabe o que é obrigatório
- ❌ **Sem timeout** — tool trava, agente trava
- ❌ **Sem tratamento de erro** — exceção quebra o loop
- ❌ **Sem idempotência** em tools com side-effect — retentativa duplica
- ❌ **Sem HITL** em tools destrutivas — acidente esperando
- ❌ **Muitas tools similares** — modelo paralisa ou erra
- ❌ **Mudar tipo de parâmetro** sem versionar — quebra agentes em produção

**Diagrama**: Checklist vermelho (`etho-danger` #C0392B)
**Animação**: Itens aparecem um a um (on click)
**Imagem**: Ícones de X vermelho
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Cada anti-pattern aqui é um bug que eu já vi em produção. "Descrição de 1 palavra" é o mais comum. "Sem idempotência" causa emails duplicados. "Sem HITL" causa deletes acidentais. Cada um é evitável com as boas práticas do slide anterior.
❓ PERGUNTA PARA A TURMA: "Qual destes anti-patterns vocês têm no código de vocês hoje?" (Honestidade aqui é valiosa)
➡️ TRANSIÇÃO: "Vamos ver todos os conceitos no caso consolidado."

---

### Slide 48 — Caso Consolidado: Anthropic Tool Redesign

**Título**: Caso Consolidado — Anthropic Tool Redesign
**Objetivo**: Sintetizar todos os princípios no caso real do SWE-bench.
**Conteúdo**:
- **Contexto**: coding agent para resolver issues de GitHub (SWE-bench)
- **Problema**: paths relativos → erro sistemático
- **Os 5 princípios aplicados**:
  1. Empatia: o modelo não sabe o diretório atual → precisa de clareza
  2. Descrição rica: `view_file` descreve que precisa de path absoluto
  3. Formato natural: path como string simples, não objeto complexo
  4. **Poka-yoke**: `pattern: ^/.+` força path absoluto
  5. max_tokens generoso para reasoning antes da tool_call
- **Resultado**: erro desapareceu, acurácia subiu
- **Citação**: "We spent more time optimizing our tools than the overall prompt."
- **A lição**: ACI resolve onde prompt engineering falha

**Diagrama**: `D5` — Arquitetura do coding agent com tools destacadas
**Animação**: Fluxo aparece; tools destacadas uma a uma
**Imagem**: Diagrama de arquitetura
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Este caso consolida tudo. Os 5 princípios da Anthropic, todos aplicados. O resultado: erro que meses de prompt engineering não resolveram, resolvido com poka-yoke na tool. A citação é o resumo da aula: tempo em tools > prompt. Se vocês só lembrarem de uma frase, deve ser esta.
➡️ TRANSIÇÃO: "Último exercício antes do resumo."

---

### Slide 49 — Exercício: Anti-patterns em Schema DB

**Título**: Exercício — Anti-patterns em Schema de DB
**Objetivo**: Aplicar todos os conceitos diagnosticando anti-patterns.
**Conteúdo**:
- **Em trios (4 min)**: identifiquem 3 anti-patterns na tool abaixo:

```json
{
  "name": "query_db",
  "description": "Roda query.",
  "parameters": {
    "type": "object",
    "properties": {
      "sql": {"type": "string"},
      "db": {"type": "string"}
    }
  }
}
```

- **Perguntas-guia**:
  1. A descrição é rica?
  2. Há poka-yoke?
  3. `sql` como string livre é seguro?
  4. Falta `mode: read_only`?
  5. Falta `limit`?
  6. Falta HITL para writes?

- **3 min discutir, 1 min compartilhar**

**Diagrama**: Schema com campos marcados como "?"
**Animação**: Campos piscam
**Imagem**: Código com pontos de interrogação
**Tempo**: 4 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Deixem os trios discutirem por 3 minutos. Os anti-patterns: (1) descrição vazia ("Roda query" não diz o que pode/não pode); (2) `sql` como string livre permite DROP TABLE, DELETE → precisa de allowlist ou `mode: read_only`; (3) sem separação read/write — deveria ter `query_read` vs `query_write` com HITL; (4) `db` sem enum — pode acessar qualquer banco; (5) sem `limit` — query pode retornar milhões de linhas; (6) sem timeout — query pode travar. Cada um destes é uma vulnerabilidade ou causa de bug.
➡️ TRANSIÇÃO: "Vamos consolidar."

---

### Slide 50 — Resumo da Aula

**Título**: Resumo da Aula
**Objetivo**: Sintetizar os 8 pontos-chave da aula.
**Conteúdo**:
1. **Tool calling** = LLM decide qual tool e quais args, runtime executa
2. **JSON Schema** é o contrato — rico e restritivo é melhor
3. **ACI :: HCI** — invista no design de tools com mesmo rigor
4. **Poka-yoke** torna o erro estruturalmente impossível (caso SWE-bench)
5. **Idempotência** (request_id) previne duplicação em retentativas
6. **Matriz de risco** classifica tools — HITL obrigatório no quadrante vermelho
7. **Workbench** valida empiricamente — 20+ casos, medir, iterar
8. **Tempo em tools > prompt** — a regra de ouro da Anthropic

**Diagrama**: 8 ícones com os pontos-chave em grid 2x4
**Animação**: Ícones aparecem um a um
**Imagem**: 8 ícones minimalistas
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Se vocês só lembrarem de 8 coisas, devem ser estas. Tool calling é o mecanismo. JSON Schema é o contrato. ACI é a disciplina. Poka-yoke é a técnica. Idempotência é a robustez. Matriz de risco é a governança. Workbench é a validação. E a regra de ouro: tempo em tools > prompt. Na próxima aula (ETHAGT03) vamos aprofundar padrões de workflow.
➡️ TRANSIÇÃO: "Agora o quiz."

---

### Slide 51 — Quiz: Pergunta 1

**Título**: Quiz 1/5
**Objetivo**: Verificar compreensão de poka-yoke.
**Conteúdo**:
- **Pergunta**: O que é "poka-yoke" no contexto de ACI?
  - A) Uma técnica de prompt engineering para reduzir alucinações
  - B) Um design de tool que torna o erro impossível de cometer
  - C) Um tipo de structured output que força JSON válido
  - D) Um framework para versionamento de tools
- **Resposta**: **B**
- **Justificativa**: Poka-yoke é design que torna o erro estruturalmente impossível — ex.: exigir path absoluto via regex.

**Diagrama**: 4 opções com radio buttons
**Animação**: Opções aparecem; resposta revelada após click
**Imagem**: Ícone de pergunta
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A resposta é B. Poka-yoke é prevenção de erro pelo design da tool, não pelo prompt.
➡️ TRANSIÇÃO: "Próxima."

---

### Slide 52 — Quiz: Pergunta 2

**Título**: Quiz 2/5
**Objetivo**: Verificar compreensão da analogia ACI.
**Conteúdo**:
- **Pergunta**: Qual é a analogia central da Anthropic para design de tools?
  - A) Tools são como funções de biblioteca
  - B) ACI merece tanto esforço quanto HCI
  - C) Tools são como APIs REST
  - D) Tools são como prompts
- **Resposta**: **B**
- **Justificativa**: ACI (Agent-Computer Interface) recebe o mesmo investimento que HCI (Human-Computer Interface). O "usuário" da tool é o modelo.

**Diagrama**: 4 opções com radio buttons
**Animação**: Opções aparecem; resposta revelada após click
**Imagem**: Ícone de pergunta
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A resposta é B. ACI :: HCI. O modelo é o usuário da tool.
➡️ TRANSIÇÃO: "Próxima."

---

### Slide 53 — Quiz: Pergunta 3

**Título**: Quiz 3/5
**Objetivo**: Verificar compreensão de HITL.
**Conteúdo**:
- **Pergunta**: Quando o HITL é OBRIGATÓRIO?
  - A) Para toda tool que retorna dados
  - B) Para toda tool com parâmetros
  - C) Para toda tool irreversível E de alto impacto
  - D) Para toda tool lenta
- **Resposta**: **C**
- **Justificativa**: A matriz de risco classifica por reversibilidade × impacto. HITL é obrigatório no quadrante "irreversível + alto impacto".

**Diagrama**: 4 opções com radio buttons
**Animação**: Opções aparecem; resposta revelada após click
**Imagem**: Ícone de pergunta
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A resposta é C. HITL é proporcional ao dano potencial, não à complexidade.
➡️ TRANSIÇÃO: "Próxima."

---

### Slide 54 — Quiz: Pergunta 4

**Título**: Quiz 4/5
**Objetivo**: Verificar compreensão de tratamento de erro.
**Conteúdo**:
- **Pergunta**: Qual é a forma CORRETA de tratar erro quando uma tool falha?
  - A) Propagar a exceção para o framework
  - B) Retornar o traceback cru
  - C) Capturar e retornar mensagem estruturada útil ao modelo
  - D) Abortar o agente
- **Resposta**: **C**
- **Justificativa**: Mensagem como `{"error": "...", "suggestion": "..."}` permite ao modelo decidir o que fazer.

**Diagrama**: 4 opções com radio buttons
**Animação**: Opções aparecem; resposta revelada após click
**Imagem**: Ícone de pergunta
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A resposta é C. Traceback cru confunde o modelo. Mensagem estruturada permite recuperação.
➡️ TRANSIÇÃO: "Última pergunta."

---

### Slide 55 — Quiz: Pergunta 5

**Título**: Quiz 5/5
**Objetivo**: Verificar a regra de ouro.
**Conteúdo**:
- **Pergunta**: Qual é a "regra de ouro" da Anthropic sobre onde investir tempo?
  - A) Otimize o prompt do sistema antes de tudo
  - B) Troque para um modelo maior
  - C) Passe mais tempo otimizando as tools do que o prompt
  - D) Adicione mais tools para dar opções
- **Resposta**: **C**
- **Justificativa**: Citação direta: "We spent more time optimizing our tools than the overall prompt."

**Diagrama**: 4 opções com radio buttons
**Animação**: Opções aparecem; resposta revelada após click
**Imagem**: Ícone de pergunta
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A resposta é C. Se vocês só lembrarem de UMA coisa, deve ser esta: tempo em tools > prompt.
➡️ TRANSIÇÃO: "Como isto conecta com o resto da especialização."

---

### Slide 56 — Conexão com Próximos Módulos

**Título**: Conexão com a Especialização
**Objetivo**: Mostrar como ETHAGT02 conecta com o restante do programa.
**Conteúdo**:
- **ETHAGT03** — Padrões de Workflow: composição de tools em workflows
- **ETHAGT04** — Reasoning & Planning: reflexion, tool use em loops de reasoning
- **ETHAGT05** — Memória: tools + memória persistente
- **ETHAGT06** — RAG Agêntico: retrieval como tool
- **ETHAGT08** — MCP: descoberta dinâmica de tools em escala
- **ETHAGT09-10** — Multi-Agentes: tools compartilhadas entre agentes
- **ETHAGT12** — AgentOps: avaliação sistemática de tools
- **ETHAGT13** — Segurança: prompt injection via tools, red team

**Diagrama**: Mapa da especialização com ETHAGT02 no centro
**Animação**: Conexões aparecem do centro para fora
**Imagem**: Mind map radial
**Tempo**: 1 min

**Rodape**: RAG = Retrieval-Augmented Generation — Geracao Aumentada por Recuperacao

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: ETHAGT02 é o aprofundamento do componente "tools" do Augmented LLM. Todo módulo seguinte expande um aspecto: composição em ETHAGT03, reasoning em ETHAGT04, memória em ETHAGT05, retrieval em ETHAGT06, escala em ETHAGT08 (MCP), multi-agente em ETHAGT09, avaliação em ETHAGT12, segurança em ETHAGT13.
➡️ TRANSIÇÃO: "O que ler antes da próxima aula."

---

### Slide 57 — Leitura Recomendada e Referências

**Título**: Leitura Recomendada
**Objetivo**: Indicar o que ler antes da próxima aula.
**Conteúdo**:
- **Obrigatório**:
  - Anthropic. *Building Effective Agents*, Appendix 2. 2024.
    - URL: anthropic.com/engineering/building-effective-agents
  - OpenAI. *Function Calling Guide*. 2024.
    - URL: platform.openai.com/docs/guides/function-calling
- **Recomendado**:
  - arXiv:2305.15334 — Gorilla (degradação com muitas tools)
  - arXiv:2307.16789 — ToolLLM (benchmark de tool use)
  - arXiv:2302.04761 — Toolformer (contexto histórico)
- **Opcional**:
  - Pydantic AI docs — padrões modernos de schema
  - Pat McGuinness — Design Patterns for Effective AI Agents (Substack)

**Diagrama**: Lista com ícones de livro
**Animação**: Itens aparecem um a um
**Imagem**: Ícones de livro/paper
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A leitura obrigatória é o Appendix 2 da Anthropic (15 min) e a doc de function calling da OpenAI. Os papers são para quem quer aprofundar. A doc do Pydantic AI é referência prática para schemas.
➡️ TRANSIÇÃO: "O projeto do módulo."

---

### Slide 58 — Projeto do Módulo

**Título**: Projeto — Tools de Suporte ao Cliente com Workbench
**Objetivo**: Apresentar o projeto que os alunos devem entregar.
**Conteúdo**:
- **Descrição**: projetar o conjunto de tools (até 8) de um agente de suporte ao cliente
  - Capacidades: buscar pedidos, atualizar perfil, processar reembolso, enviar email, escalar para humano
- **Entrega**:
  - Código com schemas, descrições e tratamento de erro
  - HITL funcionando para ações destrutivas (reembolso, email)
  - Workbench com 20 casos de teste
  - Relatório de iteração ACI (antes/depois)
- **Critério de sucesso**:
  - Taxa de uso correto ≥ 85%
  - HITL funcionando para reembolso e email
- **Prazo**: 2 semanas
- **Avaliação**: rubrica de 4 pilares (Técnico 40%, Consultivo 30%, Comportamental 20%, Prático 10%)

**Diagrama**: 4 cards representando entregáveis
**Animação**: Cards aparecem um a um
**Imagem**: Ícones de código, workbench, relatório, demo
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O projeto é a aplicação prática de tudo. A chave não é "funcionar" — é a iteração ACI documentada no relatório. Vocês devem mostrar: versão inicial (tools vagas), medição (taxa de uso correto baixa), refatoração (aplicar princípios), medição nova (taxa subiu). O relatório antes/depois é tão importante quanto o código.
➡️ TRANSIÇÃO: "Perguntas?"

---

### Slide 59 — Q&A / Encerramento

**Título**: Perguntas?
**Objetivo**: Abrir para perguntas e encerrar a aula.
**Conteúdo**:
- Q&A aberto
- **Próxima aula**: ETHAGT03 — Padrões de Workflow
  - Os 5 padrões canônicos em detalhe
  - Composição de tools em workflows
  - Quando compor vs quando usar agente
- **Feedback**: "Uma refatoração de tool que você faria amanhã no trabalho"

**Diagrama**: Ícone de Q&A
**Animação**: Fade
**Imagem**: Ícone de balão de pergunta
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Abrir para Q&A. Se não houver perguntas, fazer a pergunta inversa: "Qual princípio ACI foi menos claro?" Lembrar da leitura obrigatória (Anthropic Appendix 2) e do prazo do projeto. A próxima aula (ETHAGT03) aprofunda padrões de workflow — onde as tools de hoje se combinam em orquestrações.

---

### Slide 60 — Agradecimento

**Título**: Obrigado!
**Objetivo**: Encerrar formalmente.
**Conteúdo**:
- Universidade Etho · Especialização em Programação Agêntica
- ETHAGT02 — Tool Calling e Agent-Computer Interface (ACI)
- Próxima: ETHAGT03 — Padrões de Workflow
- Contato do professor · Repositório da especialização

**Diagrama**: Logo Etho centralizado
**Animação**: Fade out
**Imagem**: Logo Etho em fundo `etho-dark`
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Encerrar. Lembrar: tempo em tools > prompt. Poka-yoke suas tools. HITL no quadrante vermelho. Até a próxima.
