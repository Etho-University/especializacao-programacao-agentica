"""
tools_v0.py — 5 tools mal-desenhadas para o Lab 1 (ETHAGT02)

Cada tool contém pelo menos um anti-pattern de ACI.
O objetivo é refatorá-las para tools_v1.py aplicando os princípios da Anthropic.

Anti-patterns por tool:
  1. search(q)       → nome ambíguo, parâmetro sem tipo, sem descrição
  2. get_data(...)   → 4 parâmetros sem tipo, sem default, sem enum
  3. update_record() → aceita JSON genérico, path relativo
  4. calc(e)         → eval() perigoso, aceita qualquer string
  5. send(...)       → 6 parâmetros, sem validação de email, destrutiva sem HITL
"""

import os
import json
import sqlite3
import smtplib
from email.mime.text import MIMEText


# ---------------------------------------------------------------------------
# Tool 1: search(q)
# Anti-patterns:
#   - Nome genérico "search" — não diz O QUÊ搜索
#   - Parâmetro "q" sem anotação de tipo
#   - Sem docstring / descrição
#   - Sem limites de resultados
# ---------------------------------------------------------------------------

def search(q):
    conn = sqlite3.connect("/data/kb/index.db")
    cur = conn.cursor()
    cur.execute("SELECT id, title, body FROM articles WHERE body LIKE ?", (f"%{q}%",))
    rows = cur.fetchall()
    conn.close()
    return [{"id": r[0], "title": r[1], "body": r[2]} for r in rows]


# ---------------------------------------------------------------------------
# Tool 2: get_data(type, id, fmt, opt)
# Anti-patterns:
#   - "type" shadow built-in
#   - Nenhum parâmetro tem anotação de tipo
#   - Sem valores default
#   - "type" e "fmt" são strings livres — deveriam ser enum
#   - "opt" é misterioso — ninguém sabe o que faz
# ---------------------------------------------------------------------------

def get_data(type, id, fmt, opt):
    conn = sqlite3.connect("./data/app.db")
    cur = conn.cursor()
    table = type + "s"
    cur.execute(f"SELECT * FROM {table} WHERE id = ?", (id,))
    row = cur.fetchone()
    conn.close()
    if row is None:
        return None
    if fmt == "json":
        return json.dumps({"id": row[0], "data": row[1]})
    elif fmt == "csv":
        return f"{row[0]},{row[1]}"
    elif fmt == "raw":
        return str(row)
    elif opt == "verbose":
        return f"Record {id} from {table}: {row}"
    return str(row)


# ---------------------------------------------------------------------------
# Tool 3: update_record(rec)
# Anti-patterns:
#   - Aceita um JSON genérico "rec" — sem schema definido
#   - Path relativo "./data/app.db" — quebra se CWD mudar
#   - Não retorna mensagem útil ao modelo em caso de erro
#   - Sem idempotência
# ---------------------------------------------------------------------------

def update_record(rec):
    try:
        data = json.loads(rec)
    except:
        return "error"
    conn = sqlite3.connect("./data/app.db")
    cur = conn.cursor()
    table = data.get("table", "records")
    fields = data.get("fields", {})
    record_id = data.get("id")
    set_clause = ", ".join(f"{k} = ?" for k in fields)
    values = list(fields.values()) + [record_id]
    cur.execute(f"UPDATE {table} SET {set_clause} WHERE id = ?", values)
    conn.commit()
    conn.close()
    return "ok"


# ---------------------------------------------------------------------------
# Tool 4: calc(e)
# Anti-patterns:
#   - Usa eval() — executa qualquer código Python
#   - Parâmetro "e" sem descrição
#   - Sem restrição de operadores
#   - Vulnerável a injection: calc("__import__('os').system('rm -rf /')")
# ---------------------------------------------------------------------------

def calc(e):
    result = eval(e)
    return str(result)


# ---------------------------------------------------------------------------
# Tool 5: send(msg, to, subj, cc, bcc, att)
# Anti-patterns:
#   - 6 parâmetros — excesso de complexidade
#   - Sem validação de email
#   - Destrutiva sem confirmação humana (HITL)
#   - "att" (attachment) aceita qualquer coisa
#   - "cc" e "bcc" raramente usados — poluição de interface
# ---------------------------------------------------------------------------

def send(msg, to, subj, cc=None, bcc=None, att=None):
    smtp = smtplib.SMTP("smtp.company.com", 587)
    smtp.starttls()
    smtp.login("bot@company.com", os.environ.get("SMTP_PASS", ""))

    body = MIMEText(msg)
    body["Subject"] = subj
    body["From"] = "bot@company.com"
    body["To"] = to
    if cc:
        body["Cc"] = cc

    recipients = [to]
    if cc:
        recipients.append(cc)
    if bcc:
        recipients.append(bcc)

    smtp.sendmail("bot@company.com", recipients, body.as_string())
    smtp.quit()
    return "sent"


# ---------------------------------------------------------------------------
# Registro das tools (formato simples para o lab)
# ---------------------------------------------------------------------------

TOOLS_V0 = [
    {
        "name": "search",
        "function": search,
        "parameters": {"q": {"type": "any"}},
    },
    {
        "name": "get_data",
        "function": get_data,
        "parameters": {
            "type": {"type": "any"},
            "id": {"type": "any"},
            "fmt": {"type": "any"},
            "opt": {"type": "any"},
        },
    },
    {
        "name": "update_record",
        "function": update_record,
        "parameters": {"rec": {"type": "any"}},
    },
    {
        "name": "calc",
        "function": calc,
        "parameters": {"e": {"type": "any"}},
    },
    {
        "name": "send",
        "function": send,
        "parameters": {
            "msg": {"type": "any"},
            "to": {"type": "any"},
            "subj": {"type": "any"},
            "cc": {"type": "any"},
            "bcc": {"type": "any"},
            "att": {"type": "any"},
        },
    },
]


if __name__ == "__main__":
    print("=== tools_v0.py — 5 tools ruins ===\n")
    for t in TOOLS_V0:
        print(f"  - {t['name']}({', '.join(t['parameters'].keys())})")
    print("\nExecute workbench.py para testar com test_cases.json")
