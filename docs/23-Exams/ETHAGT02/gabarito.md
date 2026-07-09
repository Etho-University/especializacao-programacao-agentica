---
password: Etho-Prof-2026
---
# ETHAGT02 — Gabarito da Prova

> Restrito a mentores. Respostas esperadas e critérios de correção para [`prova.md`](prova.md).

## Parte 1 — Conceitos

**1. (b) Elimina o problema de parsing, pois a saída é estruturada.** O function calling moderno emite a chamada como objeto estruturado (JSON com `name` e `arguments`), separado do conteúdo textual, eliminando o parsing frágil de regex. Ref.: Capítulo 1 — O mecanismo do tool calling, §1.2.

**2. FALSO.** Cada ferramenta declarada consome tokens de contexto permanentemente — sua descrição e schema são injetados em *toda* chamada ao modelo. Com 50 ferramentas, isso são vários milhares de tokens. Ferramenta não usada é um imposto pago a cada token. Ref.: Capítulo 1, §1.5 (Multi-tool calls, paralelismo e custo).

**3. (c) Irreversível + alto impacto.** O quadrante irreversível + alto impacto (ex.: `delete_account`, `deploy`, `transfer_money`) exige HITL obrigatório. O agente *propõe*; um humano *aprova*; só então executa. Ref.: Capítulo 4 — Tools perigosas e HITL, §4.1 (matriz de risco).

**4. FALSO.** A analogia ACI :: HCI (Anthropic) diz: se o modelo erra, a culpa é da *interface*, não do modelo. A reação correta é refatorar a interface (descrição, schema, exemplos), não trocar de LLM. Ref.: Capítulo 2 — ACI como disciplina, §2.1.

## Parte 2 — Aplicação e trade-off

**5.** Três anti-patterns: (i) **Nome genérico** `search` — não diz o que busca; (ii) **Descrição vaga** `"Consulta pedidos"` — não diz quando usar, o que retorna, nem as fronteiras; (iii) **Schema frouxo** — `"q"` sem descrição, sem `enum`, sem constraints; o modelo não sabe o formato esperado. Ref.: Capítulo 5 — Erros comuns, §5.3-5.4.

**6.** **Consolidar** em uma única tool com parâmetros opcionais:
```python
def search_orders(order_id=None, customer_id=None, date_from=None, date_to=None):
    """Busca pedidos. Forneça ao menos um critério."""
```
Regra de bolso: se duas ferramentas compartilham 80% da lógica, são uma ferramenta. Consolidar reduz confusão do modelo (hesitação sobre qual usar) e o overhead de tokens. Ref.: Capítulo 5, §5.2.

**7.** A correção canônica (caso real da Anthropic no SWE-bench) é **usar sempre paths absolutos** e forçar validação: `absolute_path` DEVE começar com `/`. Isso elimina a ambiguidade do "diretório atual". Ref.: Capítulo 5, §5.1 (Paths relativos → absolutos).

**8. FALSO.** Ferramentas de leitura pura já são idempotentes por natureza (não alteram estado). A idempotency key é obrigatória para ferramentas com **efeito colateral de escrita** (pagamento, e-mail, criação de recurso). Ref.: Capítulo 3 — Engenharia de tools, §3.2 e §3.4 (tipologia).

## Parte 3 — Projeto curto

**9.** Resposta modelo:
```python
def get_order_status(order_id: str) -> dict:
    """Consulta o status de um pedido pelo seu número.
    Use quando o cliente perguntar sobre um pedido específico.
    NÃO use para listar todos os pedidos (use 'list_orders').
    Retorna: id, status (pending|shipped|delivered|cancelled), total, eta."""
```
Avaliar: o que faz, quando usar, quando NÃO usar, o que retorna. Ref.: Capítulo 2, §2.3 (Princípios de design de ACI).

**10.** Espera-se:
```python
def charge_customer(customer_id, amount_cents, idempotency_key=None):
    key = idempotency_key or str(uuid.uuid4())
    if key in processed:
        return processed[key]
    try:
        result = gateway.charge(customer_id, amount_cents, idempotency_key=key)
        processed[key] = result
        return result
    except InsufficientFunds as e:
        return {"error": "fundos_insuficientes", "message": str(e),
                "hint": "Peça ao cliente outro meio de pagamento."}
```
Avaliar: idempotency key, captura de erro, mensagem com `hint` acionável. Ref.: Capítulo 3 §3.2 e Capítulo 5 §5.5.

---

## Nota esperada por perfil

- **5,0**: domina ACI, escreve schemas ricos, justifica HITL e idempotência com rigor.
- **4,0**: identifica anti-patterns e aplica correções, com pequenas imprecisões.
- **3,0**: conhece conceitos mas não produz schemas/descrições de qualidade consistentemente.
- **<3,0**: precisa revisar ACI e engenharia de tools.
