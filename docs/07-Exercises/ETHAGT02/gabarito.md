---
password: Etho-Prof-2026
---
# ETHAGT02 — Gabarito

> Restrito a mentores. Cada resposta justificada com referência à apostila.

## Múltipla escolha

1. **b)** — Poka-yoke é um princípio de design à prova de erros (mistake-proofing): projetar descrições de tools de modo que o modelo dificilmente as use incorretamente, com exemplos e fronteiras claras (Capítulo 2 — ACI como disciplina).

2. **b)** — Tools destrutivas produzem efeitos irreversíveis (delete, deploy, transfer, email) e exigem HITL com confirmação explícita, dry-run e log de auditoria (Capítulo 4 — Tools perigosas e HITL).

3. **b)** — O JSON Schema atua como contrato entre o LLM (que gera os argumentos) e o executor (que valida e chama a função), garantindo tipos, formatos e obrigatoriedade (Capítulo 1 — O mecanismo do tool calling).

4. **b)** — Paths relativos levam o modelo a gerar caminhos que não correspondem ao filesystem real; Anthropic corrigiu isso exigindo paths absolutos (Capítulo 5 — Erros comuns e correções).

## Verdadeiro ou Falso (justificado)

1. **Falso (depende).** Muitas tools similares confundem o modelo e aumentam custo de tokens de descrição. Anthropic recomenda consolidar tools sobrepostas. Granularidade fina só é vantajosa quando as tools têm propósitos genuinamente distintos (Capítulo 5.2).

2. **Verdadeiro.** Chamadas de rede são não-determinísticas e sujeitas a timeouts; sem retry/backoff, o agente recebe erros transitórios que degradam a experiência. Todas as tools de rede devem ter timeout e política de retry (Capítulo 3.3).

3. **Verdadeiro.** Idempotência via `request_id` garante que chamadas duplicadas (por retry ou reprocessamento) não enviem dois emails, por exemplo. É essencial para tools com efeitos colaterais (Capítulo 3.2).

4. **Verdadeiro.** Propagar erros como mensagem útil (ex.: "ERROR: user 123 not found") permite que o modelo ajuste sua estratégia. Erros silenciosos levam a loops de repetição (Capítulo 5.5).

## Código curto

1. **JSON Schema com idempotência:**
```python
from pydantic import BaseModel, EmailStr
from typing import Literal

class SendEmailParams(BaseModel):
    to: EmailStr
    subject: str
    body: str
    request_id: str  # idempotência: mesmo request_id = no-op se já processado
```
Referência: Capítulo 3 (Engenharia de tools) e 3.2 (idempotência).

2. **Descrição reescrita com ACI:**
```
search(query: str, source: Literal["docs", "tickets", "kb"]) -> list[dict]
Busca documentos por palavra-chave na fonte especificada.
Use quando precisar encontrar informação em documentação, tickets ou base de conhecimento.

Parâmetros:
  query: termos de busca (mín. 3 caracteres). Ex.: "senha reset", "fatura duplicada"
  source: "docs" (documentação técnica), "tickets" (tickets de suporte), "kb" (knowledge base)

Retorna: lista de {title, url, snippet}. Lista vazia se nada encontrado.
NÃO use para buscar em código-fonte (use code_search para isso).
```
Referência: Capítulo 2 (princípios ACI) e Capítulo 5 (erros comuns).

3. **Decorator HITL:**
```python
def hitl_confirm(func):
    def wrapper(*args, **kwargs):
        print(f"[HITL] Prestes a executar: {func.__name__}({args}, {kwargs})")
        resp = input("Confirmar? (y/n): ")
        if resp.lower() != 'y':
            return "CANCELLED by human"
        return func(*args, **kwargs)
    return wrapper
```
Referência: Capítulo 4 (HITL obrigatório para ações destrutivas).

## Análise de trade-off

1. **`mode` vs. tools separadas:** Uma tool com `mode` é melhor quando as operações compartilham lógica e o custo cognitivo de escolher é baixo. Tools separadas são melhores quando uma é segura (draft) e outra é destrutiva (send) — separar facilita HITL seletivo e evita uso acidental do modo destrutivo (Capítulo 3 e 4).

2. **Schema estrito vs. frouxo:** Estrito (enums, patterns, required) reduz erros do modelo e melhora a taxa de uso correto, mas pode rejeitar entradas válidas em casos de borda. Frouxo é mais flexível mas gera chamadas inválidas. Recomenda-se estrito com fallback descritivo (Capítulo 5.4).

3. **Idempotência essencial vs. desnecessária:** Essencial em tools com side-effects (enviar email, cobrar cartão, deploy) onde duplicação causa dano. Desnecessária em tools de leitura pura (`get_user`, `search`) onde repetição é inofensiva (Capítulo 3.2).

## Debug / diagnóstico

1. **Causas prováveis:**
   - **Erro não propagado:** A tool retorna `null` sem mensagem; o modelo não entende que o usuário não existe. Correção: retornar `"ERROR: user 123 not found"` como string.
   - **Falta de instrução de tratamento:** O prompt não orienta o modelo a alterar a abordagem ao receber erro. Correção: adicionar instrução "se uma tool retornar erro, reformule ou tente alternativa".
   Referência: Capítulo 5.5 (Falta de erro tratado).

2. **Anti-patterns identificados:**
   - **Nome vago:** `do_stuff` não indica o propósito — o modelo não saberá quando usar.
   - **Sem descrição:** Não há docstring/descrição da função.
   - **Schema sem propriedades:** `{"type": "object"}` sem campos definidos não informa o modelo sobre parâmetros esperados.
   Referência: Capítulo 5 (Erros comuns e correções).
