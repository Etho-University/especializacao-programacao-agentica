# ETHAGT02 — Lab 2: Tool destrutiva com HITL

> Curso: Tool Calling e Agent-Computer Interface (ACI) · Carga: 25h · Pré-req: ETHAGT02 Lab 1

## Objetivo
Construir uma tool destrutiva ("enviar email") com confirmação humana (HITL), modo dry-run, log de auditoria e validação de segurança — aplicando a matriz de risco e os princípios de tools perigosas.

## Preparação
- Ambiente: Python 3.11+, `pip install pydantic openai`, `.env` com API key
- Dados/recursos: servidor SMTP mock (ou `aiosmtplib` em modo sandbox)
- Leitura prévia: Apostila ETHAGT02, Unidade 4 (Tools perigosas e HITL) e Unidade 3 (Engenharia de tools)

## Roteiro
### Passo 1 — Modelar a matriz de risco
Classifique a tool "enviar email" na matriz irreversível × impactante e justifique por que exige HITL:

```markdown
| Tool          | Irreversível? | Impactante? | Classificação    | HITL? |
|---------------|---------------|-------------|------------------|-------|
| send_email    | Sim           | Sim         | Destrutiva       | Obrigatório |
| read_email    | Não           | Baixo       | Leitura          | Não   |
| delete_email  | Sim           | Alto        | Destrutiva       | Obrigatório |
```

**Checkpoint:** matriz documentada em `risk_matrix.md` com justificativa.

### Passo 2 — Schema Pydantic estrito
Defina o input schema com validação forte:

```python
from pydantic import BaseModel, Field, EmailStr
from enum import Enum

class Priority(str, Enum):
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"

class SendEmailInput(BaseModel):
    to: EmailStr = Field(..., description="Recipient email address")
    subject: str = Field(..., min_length=1, max_length=200)
    body: str = Field(..., min_length=1, max_length=5000)
    priority: Priority = Field(default=Priority.NORMAL)
    cc: list[EmailStr] = Field(default_factory=list, max_length=10)
    attachments: list[str] = Field(default_factory=list,
        description="Absolute file paths only, e.g. /data/report.pdf")
```

**Checkpoint:** schema rejeita `to="not-an-email"` com erro de validação.

### Passo 3 — Modo dry-run
Implemente a tool com dry-run como **comportamento padrão**:

```python
SANDBOX_MODE = True

async def send_email(params: SendEmailInput) -> dict:
    if SANDBOX_MODE:
        return {
            "status": "dry_run",
            "message": f"DRY-RUN: would send to {params.to}",
            "preview": {"to": params.to, "subject": params.subject,
                        "body_preview": params.body[:200]}
        }
    # ... envio real omitido
```

**Checkpoint:** chamada padrão retorna `status: "dry_run"` sem enviar nada.

### Passo 4 — HITL com confirmação explícita
Implemente um fluxo de confirmação humana antes da execução real:

```python
async def send_email_with_hitl(params: SendEmailInput) -> dict:
    preview = await send_email(params)  # dry-run
    print(f"\n=== CONFIRMAÇÃO NECESSÁRIA ===")
    print(f"Para: {params.to}")
    print(f"Assunto: {params.subject}")
    print(f"Prioridade: {params.priority}")
    print(f"Body (200 chars): {params.body[:200]}...")
    print(f"Deseja enviar? (yes/no): ", end="")
    confirm = input().strip().lower()
    if confirm != "yes":
        return {"status": "cancelled", "reason": "user declined"}
    # Proceder com envio real
    ...
```

**Checkpoint:** se o usuário digita algo diferente de "yes", a execução é cancelada.

### Passo 5 — Log de auditoria
Registre toda decisão em `audit_log.jsonl` com timestamp, usuário, ação, parâmetros, decisão:

```python
def log_audit(action, params, decision, actor="agent"):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "actor": actor,
        "action": action,
        "params": params.model_dump(),
        "decision": decision,
        "sandbox": SANDBOX_MODE
    }
    with open("audit_log.jsonl", "a") as f:
        f.write(json.dumps(entry, default=str) + "\n")
```

**Checkpoint:** cada chamada (dry-run, confirmada, cancelada) produz uma linha de log.

### Passo 6 — Rate limiting e quotas
Adicione proteção contra abuso — máximo de 5 emails por minuto, máximo de 50 por dia:

```python
from collections import defaultdict
from time import time
send_log = defaultdict(list)

def check_rate_limit(user_id="default") -> bool:
    now = time()
    send_log[user_id] = [t for t in send_log[user_id] if now - t < 86400]
    recent = [t for t in send_log[user_id] if now - t < 60]
    if len(recent) >= 5:
        return False
    if len(send_log[user_id]) >= 50:
        return False
    return True
```

**Checkpoint:** a 6ª chamada em 1 minuto é rejeitada com mensagem clara ao agente.

### Passo 7 — Integração com agente
Integre a tool a um agente simples que pode responder "envie um email para X sobre Y":

```python
tools = {"send_email": send_email_with_hitl, ...}
# O SYSTEM prompt deve instruir:
# "ALWAYS use dry-run first. Only send for real after user confirms."
```

**Checkpoint:** agente propõe envio, mostra preview, e só executa após confirmação.

### Passo 8 — Teste de edge cases
Teste os seguintes cenários e documente o comportamento:

1. Email inválido → deve rejeitar com erro tratado
2. Subject vazio → deve rejeitar na validação
3. Anexo com path relativo → deve rejeitar
4. Rate limit excedido → deve rejeitar com mensagem útil
5. Usuário cancela → deve logar como "cancelled"

**Checkpoint:** todos os 5 cenários documentados com comportamento esperado vs real.

## Desafios extras
- Adicione allowlist de destinatários (só domains aprovados podem receber)
- Implemente um segundo HITL para anexos (confirmar cada anexo individualmente)
- Crie um wrapper que converte qualquer tool em tool-com-HITL via decorator

## Entrega
- Repositório com `email_tool.py`, `audit_log.jsonl`, `risk_matrix.md`, `edge_cases.md`
- Demo ao vivo: agente propondo envio e HITL funcionando
- Commit no padrão `ETHAGT02: lab-2 implementar tool destrutiva com HITL`

## Rubrica
Avaliado pela rubrica em `08-Assignments/ETHAGT02/assignment-01.md` (Pilar Comportamental 20%: colaboração em labs).
