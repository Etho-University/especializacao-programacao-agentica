# ETHAGT02 — Exercícios

> Exercícios para aula e para casa.
> Organizados por tipo: em aula, individual, em duplas/trios, projeto.

---

## Exercícios em Aula

### E1 — Tool Bem vs Mal Descrita (Discussão em Duplas)
**Slide**: 13
**Tempo**: 2 min
**Formato**: Duplas, 1 min observar + 1 min compartilhar

**Enunciado**: Observem as duas descrições abaixo da mesma tool. Em duplas, identifiquem 3 problemas na versão "mal descrita":

**Mal descrita**:
```json
{
  "name": "search",
  "description": "Busca produtos.",
  "parameters": {
    "type": "object",
    "properties": {
      "q": {"type": "string"},
      "c": {"type": "string"}
    }
  }
}
```

**Bem descrita**:
```json
{
  "name": "search_product",
  "description": "Busca um produto pelo nome exato ou parcial no catálogo. Retorna preço, disponibilidade e SKU. Use esta tool quando o usuário perguntar sobre preço, estoque ou detalhes de um produto específico. NÃO use para listar todos os produtos — use list_products para isso.",
  "parameters": {
    "type": "object",
    "properties": {
      "query": {"type": "string", "description": "Nome do produto ou parte. Ex.: 'iPhone 15'"},
      "category": {"type": "string", "enum": ["electronics", "clothing", "food", "books"]}
    },
    "required": ["query"]
  }
}
```

**Gabarito (problemas na mal descrita)**:
1. Nome `search` é genérico — não diz o QUE busca
2. Parâmetros `q` e `c` não têm descrição nem exemplo
3. `category` aceita qualquer string (sem enum = pode errar)
4. Descrição não diz quando USAR nem quando NÃO USAR
5. `required` ausente — modelo não sabe o que é obrigatório

---

### E2 — O Que Está Faltando no send_email? (Trios)
**Slide**: 23
**Tempo**: 3 min
**Formato**: Trios, 2 min discutir + 1 min compartilhar

**Enunciado**: Analisem a tool `send_email` abaixo e listem o que está faltando do ponto de vista de ACI:

```json
{
  "name": "send_email",
  "description": "Envia um email.",
  "parameters": {
    "type": "object",
    "properties": {
      "to": {"type": "string"},
      "subject": {"type": "string"},
      "body": {"type": "string"}
    }
  }
}
```

**Gabarito** ( itens que faltam ):
- Descrição rica (o que faz, quando usar, quando NÃO usar)
- `to` precisa de formato validado (`format: email` ou pattern regex)
- Falta `cc`, `bcc` se necessário
- Falta `dry_run` ou modo de preview
- Falta `request_id` para idempotência
- `required` omitido
- Esta é uma tool DESTRUTIVA (external side-effect) → precisa de HITL
- Sem tratamento de erro definido

---

### E3 — Classificação de Tools por Tipo e HITL (Individual)
**Slide**: 36
**Tempo**: 2 min
**Formato**: Individual, votação rápida

**Enunciado**: Para cada tool abaixo, classifique: (a) tipo [leitura / escrita / destrutiva / external], (b) HITL necessário? [sim/não/opcional]

1. `get_order_status(order_id)`
2. `update_profile(user_id, data)`
3. `delete_account(user_id)`
4. `send_email(to, subject, body)`
5. `deploy_to_production(branch)`
6. `search_products(query)`
7. `create_invoice(customer_id, items)`
8. `drop_table(table_name)`

**Gabarito**:

| # | Tool | Tipo | HITL |
|---|---|---|---|
| 1 | get_order_status | Leitura | Não |
| 2 | update_profile | Escrita (reversível) | Opcional |
| 3 | delete_account | Destrutiva (irreversível) | **SIM** |
| 4 | send_email | External side-effect | **SIM** |
| 5 | deploy_to_production | External + destrutiva | **SIM** |
| 6 | search_products | Leitura | Não |
| 7 | create_invoice | Escrita (reversível) | Opcional |
| 8 | drop_table | Destrutiva (irreversível) | **SIM** |

---

### E4 — Anti-patterns em Schema DB (Trios)
**Slide**: 49
**Tempo**: 4 min
**Formato**: Trios, 3 min identificar + 1 min compartilhar

**Enunciado**: Identifiquem 3 anti-patterns no schema abaixo de uma tool que executa query SQL:

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

**Gabarito** ( anti-patterns ):
1. **Descrição vazia** ("Roda query") — não diz o que pode/não pode rodar
2. **SQL como string livre** — permite `DROP TABLE`, `DELETE FROM` → precisa de allowlist ou `mode: "read_only"`
3. **Sem separação read/write** — deveria ter `query_read` vs `query_write` com HITL na write
4. **`db` sem enum** — pode acessar qualquer banco; deve ter allowlist
5. **Sem `limit`** — query sem limite pode retornar milhões de linhas
6. **Sem timeout** — query pode travar o agente
7. **Nome genérico** `query_db` — `search_records` ou `read_table` seria mais claro

---

## Exercícios Individuais (para casa)

### E5 — Reescreva uma Tool Vaga com ACI
**Tempo estimado**: 15 min
**Formato**: Individual, código

**Enunciado**: Reescreva a descrição da tool abaixo aplicando os 5 princípios ACI (pôr-se no lugar do modelo, descrições ricas, formato natural, poka-yoke, espaço para pensar):

```json
{
  "name": "update",
  "description": "Atualiza dados.",
  "parameters": {
    "type": "object",
    "properties": {
      "id": {"type": "string"},
      "data": {"type": "object"}
    }
  }
}
```

**Critério de avaliação**:
- Nome descritivo (ex.: `update_user_profile`) ✅
- Descrição diz o QUE faz, QUANDO usar, QUANDO NÃO usar ✅
- Parâmetros têm descrição e exemplos ✅
- Poka-yoke aplicado (enum, pattern, required) ✅
- Considera HITL se aplicável ✅

---

### E6 — JSON Schema com Idempotência
**Tempo estimado**: 15 min
**Formato**: Individual, código

**Enunciado**: Escreva um JSON Schema completo para uma tool `process_payment` que force idempotência via `request_id`. O schema deve incluir:
- Validação de formato de email
- Enum para moeda
- Validação de valor positivo
- `request_id` obrigatório (UUID)
- Descrição rica

**Exemplo de resposta**:
```json
{
  "type": "function",
  "function": {
    "name": "process_payment",
    "description": "Processa um pagamento com cartão. Usa request_id para garantir idempotência — retentativas com o mesmo request_id não duplicam o pagamento. NÃO use para reembolsos — use refund_payment para isso.",
    "parameters": {
      "type": "object",
      "properties": {
        "request_id": {
          "type": "string",
          "format": "uuid",
          "description": "Identificador único da requisição (UUID v4). Reuse em retentativas para evitar duplicação."
        },
        "customer_email": {
          "type": "string",
          "format": "email",
          "description": "Email do cliente. Ex.: 'joao@exemplo.com'"
        },
        "amount": {
          "type": "number",
          "exclusiveMinimum": 0,
          "description": "Valor a cobrar. Deve ser positivo. Ex.: 99.90"
        },
        "currency": {
          "type": "string",
          "enum": ["BRL", "USD", "EUR"],
          "description": "Moeda ISO 4217."
        }
      },
      "required": ["request_id", "customer_email", "amount", "currency"]
    }
  }
}
```

---

### E7 — 1 Tool com Mode vs 2 Separadas
**Tempo estimado**: 10 min
**Formato**: Individual, escrito

**Enunciado**: Responda justificando em 3-5 frases: Para o caso de gerenciar usuários (`create`, `update`, `delete`, `get`), você usaria 1 tool com parâmetro `action` ou 4 tools separadas? Aplique a regra dos 80%.

**Gabarito esperado**:
- 4 tools separadas é melhor na maioria dos casos
- Razão: `create`/`update`/`get` são de baixo risco, mas `delete` é destrutiva → HITL obrigatório
- Misturar em 1 tool com `action` força a mesma governança para todas
- Exceção: se >80% das chamadas são admin panel onde todas as ações co-ocorrem, 1 tool com `action` reduz a descrição total de tokens

---

## Projeto do Módulo

### P1 — Tools de Suporte ao Cliente com Workbench
**Prazo**: 2 semanas
**Formato**: Individual
**Carga**: ~10h

**Descrição**: Projetar o conjunto de tools (até 8) de um agente de suporte ao cliente. O agente deve conseguir: buscar pedidos, atualizar perfil, processar reembolso, enviar email de confirmação, e escalar para humano.

**Entrega**:
- Código com schemas, descrições e tratamento de erro
- HITL funcionando para ações destrutivas (reembolso, email)
- Workbench próprio com 20 casos de teste
- Relatório de iteração ACI (antes/depois da refatoração)

**Critério de sucesso**:
- Taxa de uso correto ≥ 85%
- HITL funcionando para reembolso e email
- Relatório documenta melhoria antes/depois

**Avaliação** (rubrica de 4 pilares):

| Pilar | Peso | Critério |
|---|---|---|
| Técnico | 40% | Schemas corretos, código funcional, workbench com 20 casos |
| Consultivo | 30% | Relatório de iteração — clareza da justificativa ACI |
| Comportamental | 20% | Revisão cruzada de schemas de um colega |
| Prático | 10% | Demo ao vivo: agente usando as tools em 3 cenários |

**Nota mínima de aprovação**: 3.0
