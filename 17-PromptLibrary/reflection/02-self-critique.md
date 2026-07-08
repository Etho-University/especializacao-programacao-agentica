# reflection/02-self-critique.md

## objetivo
Prompt para o modelo criticar a própria saída antes de entregá-la, identificando falhas e sugerindo melhorias.

## variáveis
- `{{original_input}}` — entrada/prompt original
- `{{draft_output}}` — rascunho gerado pelo modelo
- `{{critique_focus}}` — área específica para criticar (ex.: clareza, factualidade, tom, segurança)

## template

```
Review the draft output below. Identify at least three specific issues, then produce a revised version.

Original input:
{{original_input}}

Draft output:
{{draft_output}}

Critique focus: {{critique_focus}}

For each issue:
- Location: quote or reference the problematic part
- Problem: what is wrong
- Severity: critical / major / minor
- Suggestion: how to fix

After listing issues, write:
- Revised Output: a corrected version of the full draft
- Change Log: summary of what changed and why
```

## exemplo de uso
Após gerar um e-mail profissional, o modelo critica o tom (muito informal) e reescreve para um tom mais formal.

## trade-offs
- Modelos menos capazes podem não identificar seus próprios erros (calibration gap)
- Adiciona latência de ~1 chamada extra
- Pode introduzir novos erros na revisão

## variações
- **Self-critique com rubrica**: fornecer checklist contra a qual o modelo deve verificar
- **Critique externo**: outro agente (ou instância) faz a crítica em vez do mesmo modelo
- **Multi-pass critique**: rodadas múltiplas de crítica até não haver mais issues identificadas
