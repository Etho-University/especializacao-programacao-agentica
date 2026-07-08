# ETHAGT02 — Tool Calling e Agent-Computer Interface (ACI)

> **Apostila do curso** · Especialização em Programação Agêntica · Universidade Etho
> Fase A — Fundamentos Agênticos · Carga 25 h · Versão 1.0 · Julho 2026
> *Material de referência duradouro (nível pós-graduação lato sensu). Os slides são auxiliares.*

---

## Sumário

- **Capítulo 1** — O mecanismo do tool calling
- **Capítulo 2** — ACI como disciplina de design
- **Capítulo 3** — Engenharia de tools
- **Capítulo 4** — Tools perigosas e Human-in-the-Loop (HITL)
- **Capítulo 5** — Erros comuns e correções
- **Capítulo 6** — Avaliando tools: o workbench
- **Capítulo 7** — Casos de estudo
- **Capítulo 8** — Referências e leituras

---

## Capítulo 1 — O mecanismo do tool calling

### 1.1 Por que tools definem a utilidade de um agente

Em ETHAGT01 vimos que o **Augmented LLM** é o bloco fundamental e que as *tools* são o que transforma um LLM de *falador* em *fazedor*. Este módulo aprofunda exatamente essa componente. A tese central é simples, mas subestimada: **em sistemas agentes reais, a maior parte do valor, da complexidade e dos bugs está nas ferramentas — não no "cérebro" do modelo.** Um modelo brilhante com ferramentas mal projetadas falha; um modelo medíocre com ferramentas excelentes costuma impressionar.

Por isso, projetar ferramentas não é uma tarefa de "plumbing" delegável a um estagiário: é uma **disciplina de design** que merece o mesmo rigor que dedicamos a qualquer interface de usuário. A esta disciplina chamamos **Agent-Computer Interface (ACI)**, por analogia direta com a Human-Computer Interface (HCI). O resto da apostila desenvolve essa analogia.

### 1.2 Function calling: do prompt para JSON estruturado

Historicamente, integrar ferramentas a um LLM exigia *prompt engineering*: descrevia-se a ferramenta em linguagem natural e pedia-se ao modelo que emitisse, como texto, um comando a ser *parsado* com expressões regulares. Esse modo é frágil — o modelo pode desformatar, inventar ferramentas, mesclar argumentos, esquecer de fechar parênteses. Cada novo modelo quebrava o parser.

O **function calling** (ou *tool calling*) moderno resolve isso ao tornar a chamada de ferramenta uma primitiva de primeira classe da API. Em vez de pedir texto e parseá-lo, o desenvolvedor:

1. **Declara** as ferramentas disponíveis, cada uma com um *JSON Schema* descrevendo nome, descrição e parâmetros.
2. O modelo recebe essas declarações no contexto e, se julgar necessário, **emite uma chamada de ferramenta estruturada** — não como texto livre, mas como um objeto com `name` e `arguments`, separado do conteúdo textual.
3. O sistema executa a ferramenta e devolve o resultado numa mensagem de papel `tool`, que o modelo consome para continuar.

A vantagem é decisiva: **elimina-se o problema de parsing.** A saída é estruturada porque o modelo foi treinado (ou constrangido) a produzi-la estruturada. Veja o exemplo concreto com a OpenAI SDK:

```python
from openai import OpenAI

client = OpenAI()

tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Retorna a previsão do tempo atual para uma cidade.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "Nome da cidade, ex.: 'São Paulo'"},
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"], "default": "celsius"},
            },
            "required": ["city"],
        },
    },
}]

resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Como está o tempo em Recife?"}],
    tools=tools,
)

if resp.choices[0].message.tool_calls:
    call = resp.choices[0].message.tool_calls[0]
    print(call.function.name)        # "get_weather"
    print(call.function.arguments)   # '{"city": "Recife", "unit": "celsius"}'
```

Note que a decisão de *chamar* a ferramenta é do modelo — ele só o faz se a pergunta exigir. Esse é o coração da autonomia: **o agente decide quando age.**

### 1.3 JSON Schema como contrato

O JSON Schema é o **contrato** entre o modelo e o seu sistema. Quanto mais preciso o contrato, menos ambiguidade o modelo tem e menos erros ele comete. Um schema fraco (`"type": "object"` sem propriedades) é uma fonte garantida de bugs; um schema rico (com `enum`, `pattern`, `format`, `description` em cada campo) guia o modelo como um bom formulário guia um usuário.

A regra prática: **trate cada propriedade do schema como um campo de formulário que precisa de rótulo e dica.** Compare:

```jsonc
// ❌ Fraco — ambíguo
{
  "name": "search",
  "parameters": {"type": "object", "properties": {"q": {"type": "string"}}}
}

// ✅ Forte — guia o modelo
{
  "name": "search_docs",
  "description": "Busca documentos na base de conhecimento interna por semântica. Use quando o usuário perguntar sobre políticas, manuais ou procedimentos da empresa.",
  "parameters": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "Termo ou pergunta em linguagem natural, ex.: 'política de reembolso'"
      },
      "top_k": {"type": "integer", "minimum": 1, "maximum": 10, "default": 5}
    },
    "required": ["query"]
  }
}
```

### 1.4 Structured outputs e constrained decoding

Um passo além do function calling é o **structured output** (ou *constrained decoding* / *response format*): em vez de *esperar* que o modelo produza JSON válido e validar depois, o sistema *força* o formato durante a própria geração, restringindo os tokens admissíveis a apenas aqueles que mantêm o JSON válido segundo o schema. Isso leva a taxa de conformidade de ~90% (com prompting) para ~100% (com restrição gramatical).

Provedores oferecem isso de formas distintas: OpenAI com `response_format: {type: "json_schema", json_schema: {...}}`, Anthropic com tool use forçado, bibliotecas como `instructor` e `outlines` com restrição no cliente. A lição: **quando você precisa de estrutura, force-a; não confie em que o modelo "vai acertar".**

### 1.5 Multi-tool calls, paralelismo e custo

Modelos modernos podem emitir **múltiplas chamadas de ferramenta em uma única resposta**, o que permite paralelismo: se a pergunta exige duas buscas independentes, o modelo emite ambas e o sistema executa-as concorrentemente. Isso reduz latência ponta-a-ponta de forma significativa.

Mas há um custo frequentemente esquecido: **cada ferramenta declarada consome tokens de contexto** — sua descrição e schema são injetados em *toda* chamada ao modelo. Com 5 ferramentas bem descritas, isso pode ser 500–1.500 tokens; com 50, vários milhares. O paper *Gorilla* (Patil et al., arXiv:2305.15334) mostra empiricamente que a performance **degrada** quando o catálogo de ferramentas cresce demais. Conclusão prática:

- Mantenha o catálogo enxuto (consolide ferramentas similares).
- Considere *retrieval de ferramentas* (selecionar dinamicamente um subconjunto relevante) quando o catálogo for grande — este é exatamente o problema que o **MCP** resolve (ETHAGT08).

> **Princípio.** O custo de uma ferramenta não é só a chamada — é a presença permanente da sua descrição no contexto. Ferramenta não usada com frequência é um imposto que você paga em *cada* token.

---

## Capítulo 2 — ACI como disciplina de design

### 2.1 A analogia ACI :: HCI

A contribuição conceitual mais importante deste módulo vem da Anthropic (*Building Effective Agents*, Appendix 2, 2024): **trate a interface entre o agente e o computador (ACI) com o mesmo cuidado que dedica à interface entre humano e computador (HCI).** A intuição é que o modelo, ao escolher e usar ferramentas, é um *usuário* do seu sistema — um usuário não-humano, mas que lê descrições, interpreta schemas e comete erros de "usabilidade" exatamente como um humano comete.

Quando um humano erra numa interface, culpar o usuário é um anti-pattern de design: a culpa é da interface. O mesmo vale para agentes. Se o modelo usa uma ferramenta errada, passa argumentos errados ou confunde duas ferramentas, a reação de um bom engenheiro de ACI não é "o modelo é burro" — é "minha interface falhou em guiá-lo".

> **Princípio (Anthropic).** *Spend the effort to make the interface [of tools] well-documented, [...] just as you would with a human-facing interface.* Quando o agente erra, melhore a *interface*, não apenas o prompt.

### 2.2 Pôr-se no lugar do modelo

A primeira prática da ACI é a empatia: **antes de escrever uma ferramenta, imagine-se como o modelo que precisa escolhê-la apenas lendo sua descrição e schema, sem ver o código.** Pergunte-se:

- Eu saberia *quando* usar esta ferramenta em vez de outra?
- Eu saberia *o que* passar em cada parâmetro?
- Eu saberia o que *esperar* de retorno?
- Há ambiguidade com alguma ferramenta vizinha?

Se a resposta a qualquer pergunta é "não", a interface precisa melhorar. Esse exercício de empatia é a versão agêntica de um *usability test*.

### 2.3 Princípios de design de ACI

Da analogia derivam princípios concretos. Vamos enumerá-los com exemplos.

**(1) Descrições ricas, como docstring de um desenvolvedor júnior.** A descrição não é um rótulo — é a documentação completa que o modelo consulta. Deve dizer *o que* a ferramenta faz, *quando* usá-la, *quando não* usá-la, e dar exemplos.

```python
# ❌ Descrição pobre
"Consulta pedidos."

# ✅ Descrição rica
"""Consulta o status de um pedido pelo seu número.
Use quando o cliente perguntar sobre um pedido específico.
NÃO use para listar todos os pedidos (use 'list_orders').
Retorna: id, status (pending|shipped|delivered|cancelled), total, eta."""
```

**(2) Exemplos e edge cases na descrição.** Exemplos ancoram o modelo. Liste casos-limite explícitos: "para datas, use ISO 8601 (YYYY-MM-DD)"; "se o cliente não souber o número do pedido, peça o CPF e use 'find_order_by_cpf'".

**(3) Formato próximo ao natural.** Evite formatos que exijam escaping complexo, diffs ou estruturas profundamente aninhadas. O modelo lida melhor com formatos que se aproximam de como ele "pensaria" naturalmente. Por exemplo, prefira passar um texto completo a um diff; prefira paths absolutos a relativos (voltaremos a isto no Capítulo 5).

**(4) Dê espaço para pensar em tokens.** Algumas ferramentas exigem raciocínio intermediário do modelo (ex.: montar uma query SQL complexa). Se você constranger a saída a um formato rígido demais, o modelo "engasga" porque não tem tokens para raciocinar. Considere aceitar um campo de "raciocínio" livre antes da ação estruturada.

**(5) Fronteiras claras entre ferramentas.** Se duas ferramentas se sobrepõem, o modelo hesita e erra. Defina fronteiras explícitas na descrição: "use A quando X; use B quando Y". Quando a fronteira é tênue, costuma ser melhor **consolidar** em uma só ferramenta com um parâmetro `mode` (Capítulo 5).

### 2.4 O loop de iteração ACI

ACI não é uma atividade de uma passada: é um **loop iterativo** de projetar → testar → observar falhas → refinar. A versão agêntica do ciclo de design de HCI:

> **Diagrama de referência:** [`12-Diagrams/ETHAGT02/aci-iteration-loop.mmd`](../../12-Diagrams/ETHAGT02/aci-iteration-loop.mmd)

```
   projetar ferramenta (descrição + schema)
            │
            ▼
   rodar workbench (N casos de teste)
            │
            ▼
   observar falhas ──► qual ferramenta? qual parâmetro? por quê?
            │
            ▼
   refatorar interface (descrição, schema, exemplos)
            │
            └── (repetir até taxa de uso correto aceitável)
```

A iteração é dirigida por *evidência* (os traces de falha), não por achismo. Cada falha revela uma ambiguidade na interface que a próxima versão deve eliminar.

---

## Capítulo 3 — Engenharia de tools

### 3.1 Schemas claros com Pydantic

Em Python, a forma mais robusta e ergonômica de declarar schemas é o **Pydantic** (ou `TypedDict` para casos simples; `Zod` no ecossistema TypeScript). Pydantic dá validação, documentação e conversão para JSON Schema de uma só vez:

```python
from pydantic import BaseModel, Field
from typing import Literal
from datetime import date

class CreateOrderArgs(BaseModel):
    """Argumentos para criar um pedido de venda."""
    customer_id: str = Field(..., description="UUID do cliente, ex.: 'cust_abc123'")
    items: list[str] = Field(..., min_length=1, description="Lista de SKUs")
    payment: Literal["credit", "pix", "boleto"] = Field(..., description="Meio de pagamento")
    discount_code: str | None = Field(None, pattern=r"^[A-Z0-9]{6,12}$",
                                      description="Cupom alfanumérico, se houver")
    scheduled_for: date | None = Field(None, description="Data agendada (ISO 8601)")

# JSON Schema gerado automaticamente:
print(CreateOrderArgs.model_json_schema())
```

A vantagem sobre JSON Schema escrito à mão: a fonte da verdade é o *código*, e a validação acontece automaticamente na chamada. Use Pydantic sempre que o schema tiver mais de dois campos.

### 3.2 Idempotência: por que e onde

Uma operação é **idempotente** se executá-la uma ou N vezes produz o mesmo estado final. Em agentes, a idempotência é crucial porque **execuções podem repetir** — por retry automático, por reprocessamento após crash, por um modelo teimoso que chama a mesma ferramenta duas vezes. Sem idempotência, uma cobrança pode ser feita em duplicata; um e-mail enviado duas vezes; um registro criado duas vezes.

O padrão canônico é o **idempotency key** (chave de idempotência): o chamador fornece um identificador único; o sistema registra se já processou aquela chave e, se sim, retorna o resultado anterior em vez de reexecutar.

```python
import uuid

processed: dict[str, dict] = {}

def charge_customer(customer_id: str, amount_cents: int, idempotency_key: str | None = None):
    """Cobra um cliente. Idempotente via idempotency_key."""
    key = idempotency_key or str(uuid.uuid4())
    if key in processed:
        return processed[key]
    result = payment_gateway.charge(customer_id, amount_cents, idempotency_key=key)
    processed[key] = result
    return result
```

A regra: **toda ferramenta com efeito colateral de escrita (pagamento, e-mail, criação de recurso) deve ser idempotente.** Ferramentas de leitura pura já são idempotentes por natureza.

### 3.3 Timeouts, retries e fallbacks

Ferramentas chamam sistemas externos (APIs, bancos), que falham. Três defesas são obrigatórias em produção:

- **Timeout:** toda chamada externa precisa de um tempo máximo. Um agente que fica esperando indefinidamente uma API travada não apenas falha — consome recursos e frustra o usuário.
- **Retry com backoff:** falhas transitórias (rede, 503) merecem retentativa, com *exponential backoff* e jitter para não sincronizar.
- **Fallback:** quando a ferramenta principal falha definitivamente, há uma alternativa? (ex.: cache, valor padrão, mensagem útil ao modelo).

```python
import time, random

def call_with_retry(fn, retries=3, base_delay=0.5, timeout=10):
    for attempt in range(retries):
        try:
            return _call_with_timeout(fn, timeout)
        except TransientError:
            if attempt == retries - 1:
                raise
            delay = base_delay * (2 ** attempt) + random.uniform(0, 0.1)
            time.sleep(delay)
```

### 3.4 Tipologia de ferramentas

Classificar ferramentas por *tipo de efeito* orienta as decisões de segurança:

| Tipo | Exemplo | Reversível | Idempotência necessária | HITL |
|---|---|---|---|---|
| **Leitura** | `get_order`, `search_docs` | — (não altera estado) | Já é | Não |
| **Escrita** | `create_ticket`, `update_profile` | Sim | Sim | Depende |
| **Destrutiva** | `delete_account`, `cancel_order` | Não | Sim | **Sim** |
| **External side-effect** | `send_email`, `charge_card`, `deploy` | Não | Sim | **Sim** |

A última coluna (HITL) é tão importante que tem seu próprio capítulo (Capítulo 4).

### 3.5 Versionamento de tools sem quebrar agentes

Ferramentas evoluem: novos parâmetros, mudança de comportamento, deprecação. Em produção, mudar uma ferramenta pode quebrar agentes que dependiam do comportamento antigo. Estratégias:

- **Versionamento semântico** do contrato: `search_docs` → `search_docs_v2` quando há breaking change; mantenha a antiga por um período.
- **Compatibilidade retroativa:** adicionar parâmetros opcionais é seguro; remover ou renomear é breaking.
- **Telemetria de uso:** saiba *quais* agentes usam *quais* parâmetros antes de removê-los.
- **Janela de deprecação:** anuncie, monitore o decaimento de uso, remova só quando o uso for zero.

---

## Capítulo 4 — Tools perigosas e Human-in-the-Loop (HITL)

### 4.1 A matriz de risco

Nem toda ferramenta tem o mesmo risco. A Anthropic propõe pensar em duas dimensões: **impacto** (quão grave é o resultado) e **reversibilidade** (dá pra desfazer?). Isso dá uma matriz de risco que orienta quando exigir intervenção humana.

> **Diagrama de referência:** [`12-Diagrams/ETHAGT02/risk-matrix.mmd`](../../12-Diagrams/ETHAGT02/risk-matrix.mmd)

| | Baixo impacto | Alto impacto |
|---|---|---|
| **Reversível** | `get_weather`, `search` | `create_ticket`, `update_note` |
| **Irreversível** | `post_comment` (difícil apagar) | `delete_account`, `deploy`, `transfer_money`, `send_email` |

O quadrante **irreversível + alto impacto** exige **Human-in-the-Loop (HITL)**: nenhuma execução acontece sem confirmação humana explícita. O agente *propõe* a ação; um humano *aprova*; só então executa.

### 4.2 O fluxo HITL

O HITL não é um obstáculo ao agente — é um **padrão de controle** que permite dar autonomia onde é segura e cercar onde não é. O fluxo canônico:

> **Diagrama de referência:** [`12-Diagrams/ETHAGT02/hitl-flow.mmd`](../../12-Diagrams/ETHAGT02/hitl-flow.mmd)

```
   agente decide chamar ferramenta perigosa
            │
            ▼
   sistema INTERROMPE e pede confirmação humana
            │
        ┌───┴───┐
   aprova      rejeita
        │         │
        ▼         ▼
   executa   devolve "ação rejeitada" ao modelo (ele se adapta)
```

O ponto-chave é que a *rejeição* não é um erro fatal: ela volta ao agente como uma observação ("o humano rejeitou o envio do e-mail para X"), e o modelo pode reagir — perguntar por quê, propor alternativa, etc.

### 4.3 Confirmação explícita, dry-run e simulação

Há níveis crescentes de cautela para ações perigosas:

1. **Confirmação explícita:** "Você confirma o envio de R$ 1.200,00 para conta final 4521? [s/n]". Mínimo para qualquer ação irreversível.
2. **Dry-run:** a ferramenta simula o que *faria* sem executar de verdade ("o e-mail seria enviado para 3 destinatários: ..."), e o humano aprova com base na simulação.
3. **Log de auditoria:** toda ação aprovada fica registrada (quem, quando, o quê, com qual justificativa do agente) para responsabilização.

```python
def send_email_with_hitl(to, subject, body, approver, dry_run=True):
    preview = f"PARA: {to}\nASSUNTO: {subject}\nCORPO: {body[:200]}..."
    if dry_run:
        return {"status": "dry_run", "preview": preview, "note": "Nada enviado. Aprove para executar."}
    if not confirm_with(approver, preview):
        return {"status": "rejected", "by": approver}
    audit_log.record(approver, "send_email", to=to, subject=subject)
    return smtp.send(to, subject, body)
```

### 4.4 Allowlists vs dinâmico

Para ferramentas de alto risco, uma defesa em profundidade é a **allowlist**: um conjunto *fixo e curado* de ações permitidas, validado fora do controle do agente. Mesmo que o modelo "decida" algo fora da allowlist, o sistema recusa. Contraste com o modo *dinâmico*, onde o agente pode compor ações livremente — poderoso, mas perigoso, e só apropriado em ambientes sandboxed.

---

## Capítulo 5 — Erros comuns e correções

Este capítulo cataloga os anti-patterns mais frequentes e suas correções — material de referência para revisão de código.

### 5.1 Paths relativos → absolutos

O caso canônico da Anthropic: durante o desenvolvimento do coding agent para o SWE-bench, ferramentas de edição de arquivo usavam *paths relativos*. O agente interpretava "edite `src/app.py`" relativamente ao diretório *que ele achava* que era o atual — frequentemente errado — e escrevia no lugar errado. A correção: **use sempre paths absolutos** nas ferramentas de arquivo, eliminando a ambiguidade.

```python
# ❌ Ambíguo
def edit_file(path, content): ...

# ✅ Sem ambiguidade
def edit_file(absolute_path: str, content: str):
    """absolute_path DEVE começar com '/'. Ex.: '/repo/src/app.py'."""
```

### 5.2 Muitas ferramentas similares → consolidar

Quando há `search_orders_by_id`, `search_orders_by_date`, `search_orders_by_customer`, o modelo hesita sobre qual usar. Consolide em uma só com parâmetros opcionais:

```python
def search_orders(order_id=None, customer_id=None, date_from=None, date_to=None):
    """Busca pedidos. Forneça ao menos um critério."""
```

Regra de bolso: **se duas ferramentas compartilham 80% da lógica, são uma ferramenta.**

### 5.3 Descrições vagas → reescrever

Uma descrição como `"gerencia usuários"` não diz *nada* ao modelo. Reescreva como a documentação que você daria a um desenvolvedor júnior no primeiro dia (Capítulo 2.3).

### 5.4 Schema frouxo → apertar

Sem `enum`, `pattern`, `minimum/maximum`, o modelo inventa valores. Aperte o contrato:

```jsonc
// ❌ Frouxo
"status": {"type": "string"}

// ✅ Apertado
"status": {"type": "string", "enum": ["active", "inactive", "banned"]}
```

### 5.5 Falta de erro tratado → propagar mensagem útil

O pior erro de ferramenta é o não-tratado: uma exceção sobe, mata o agente, e o modelo nunca fica sabendo *por que*. Em vez disso, **capture o erro e devolva-o como observação útil**:

```python
def charge(args):
    try:
        return gateway.charge(args)
    except InsufficientFunds as e:
        return {"error": "fundos_insuficientes", "message": str(e),
                "hint": "Peça ao cliente outro meio de pagamento."}
```

A `hint` é o detalhe que torna o erro *acionável* pelo modelo — ele sabe o que fazer a seguir.

---

## Capítulo 6 — Avaliando tools: o workbench

### 6.1 O workbench como laboratório de ACI

Ferramentas não se avaliam por intuição — avaliam-se empiricamente. Um **workbench** é um pequeno harness que roda a ferramenta (ou o agente completo) contra um conjunto de casos de teste, mede resultados e expõe falhas. É o equivalente agêntico de testes de usabilidade.

### 6.2 Um workbench mínimo

```python
cases = [
    {"input": "qual o status do pedido 12345?", "expect_tool": "get_order", "expect_args": {"order_id": "12345"}},
    {"input": "cancele minha conta", "expect_tool": "cancel_account", "expect_hitl": True},
    {"input": "liste meus pedidos de maio", "expect_tool": "search_orders", "expect_args": {"date_from": "..."}},
]

def run_workbench(agent, cases):
    results = []
    for c in cases:
        trace = agent.run(c["input"])
        ok = (trace.tool_calls[0].name == c["expect_tool"])
        results.append({"case": c["input"], "passed": ok, "trace": trace})
    pass_rate = sum(r["passed"] for r in results) / len(results)
    return {"pass_rate": pass_rate, "details": results}
```

### 6.3 Métricas que importam

- **Taxa de uso correto:** fração de casos em que a ferramenta certa foi chamada com args corretos. A métrica principal de qualidade de ACI.
- **Custo por chamada:** tokens consumidos (incluindo descrições) × preço.
- **Latência:** ponta-a-ponta e por etapa.
- **Taxa de HITL aprovado:** quantas confirmações humanas foram aprovadas vs rejeitadas (alta rejeição indica agente propondo ações inadequadas).

### 6.4 Testes de regressão para tools

Mudou a descrição de uma ferramenta? Rode o workbench. Adicionou um parâmetro? Rode o workbench. O conjunto de casos vira um **teste de regressão** que protege contra mudanças que silenciosamente degradam o comportamento do agente. Aprofundamos avaliação sistemática em ETHAGT12 (AgentOps).

---

## Capítulo 7 — Casos de estudo

### 7.1 Redesign de ACI na Anthropic (SWE-bench)

O caso mais instrutivo de ACI é o redesign das ferramentas durante o desenvolvimento do coding agent (ETHAGT01, §7.1). A lição registrada pela Anthropic: depois de refinar as descrições e *forçar paths absolutos*, a taxa de sucesso do agente subiu significativamente — *sem mudar o modelo*. A melhoria veio inteiramente da interface.

> **Leitura.** Detalhes em [`09-CaseStudies/`](../../09-CaseStudies/). A lição arquitetural: *antes de culpar o modelo ou trocar de framework, examine a ACI.*

### 7.2 Gorilla e a degradação por escala

O paper *Gorilla* (Patil et al., arXiv:2305.15334) treina um LLM para usar mais de 1.700 APIs e mede a precisão. A lição para ACI: à medida que o catálogo cresce, a precisão cai — o modelo confunde APIs similares e a sobrecarga de tokens prejudica. Isso fundamenta a regra "mantenha o catálogo enxuto" e motiva o **MCP** (ETHAGT08), que permite descobrir ferramentas dinamicamente em vez de injetar todas no contexto.

### 7.3 Lições transversais

1. **A interface é o produto.** Em agentes, a qualidade percebida é majoritariamente função da ACI.
2. **Erros de ferramenta são erros de design.** Trate-os como feedback de usabilidade, não como "modelo burro".
3. **HITL é liberdade com segurança.** Cercar as ações perigosas libera você para dar autonomia nas demais.

---

## Capítulo 8 — Referências e leituras

### 8.1 Bibliografia fundamental

- **Anthropic.** *Building Effective Agents*, Appendix 2: "Prompt engineering your tools". 2024. 🏛 Canônica. <https://www.anthropic.com/engineering/building-effective-agents>
- **Schick, T. et al.** *Toolformer: Language Models Can Teach Themselves to Use Tools.* NeurIPS 2023. arXiv:2302.04761. 🏛 Canônica.
- **OpenAI.** *Function Calling Guide* e *Structured Outputs*. 2024.

### 8.2 Bibliografia complementar

- **Patil, S. et al.** *Gorilla: Large Language Model Connected with Massive APIs.* arXiv:2305.15334. — Degradação por escala.
- **Qin, Y. et al.** *ToolLLM: Facilitating LLMs to Master 16000+ Real-world APIs.* arXiv:2307.16789. — Benchmark de tool use (aprofundado em ETHAGT12).
- **Pydantic AI Documentation.** <https://ai.pydantic.dev/> — Padrões modernos de schema.
- **McGuinness, P.** *Design Patterns for Effective AI Agents* (Substack).

### 8.3 Recursos práticos

- **`instructor`** (jxnl) — structured outputs com Pydantic.
- **LangChain *Tool Calling* guide.**
- **Anthropic Engineering Blog** — série sobre tool use.

### 8.4 Ficha de pesquisa

Fontes completas em [`20-Research/ETHAGT02-pesquisa.md`](../../20-Research/ETHAGT02-pesquisa.md). Última consulta: Julho 2026.

---

## Síntese do módulo

Ao concluir ETHAGT02, você deve ser capaz de:

1. **Dominar** o mecanismo de tool calling (function calling, JSON Schema, structured outputs, multi-tool).
2. **Aplicar** os princípios de ACI: descrições ricas, exemplos, formato natural, fronteiras claras.
3. **Projetar** ferramentas idempotentes, com timeouts/retries/fallbacks e versionamento seguro.
4. **Classificar** ferramentas por risco e aplicar HITL onde necessário.
5. **Diagnosticar** anti-patterns e refatorar interfaces com evidência de workbench.

Próximo passo: ETHAGT03 aprofunda os padrões de *workflow* (orquestração predefinida); ETHAGT08 levará o tool use ao padrão de servidor com o **MCP**; ETHAGT13 tratará ferramentas como vetor de ataque (segurança).

---

*Mantido por: Escola de Tecnologia — Universidade Etho · Área de Inteligência Artificial · Versão 1.0 · Julho 2026*
