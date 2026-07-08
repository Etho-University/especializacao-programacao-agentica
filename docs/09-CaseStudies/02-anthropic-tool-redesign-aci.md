# Caso de Estudo — Anthropic: redesign de tools no coding agent

> ETHAGT02 · O caso canônico do princípio ACI.

## Contexto

Durante o desenvolvimento do coding agent de Claude para o SWE-bench (ver caso em ETHAGT01), a equipe da Anthropic observou um padrão de erro sistemático: após o agente "navegar" para fora do diretório raiz do repositório, começava a usar **paths relativos** incorretos, levando a edições no arquivo errado ou falhas de "arquivo não encontrado".

## A tentação

O instinto inicial de quase todo time seria ajustar o **system prompt**: "lembre-se sempre do diretório em que você está e use paths relativos corretos". Isso raramente resolve — o modelo continua errando porque o erro não é de "esquecimento", é estrutural.

## A solução adotada

A equipe mudou a **tool**: em vez de aceitar paths relativos (que exigem ao modelo manter estado implícito do CWD), passaram a exigir **paths absolutos sempre**. Após a mudança, Schluntz relatou que "o modelo usou a tool perfeitamente".

## Por que funcionou

A mudança aplica três princípios ACI simultaneamente:

1. **Poka-yoke**: torna o erro (path relativo ambíguo) estruturalmente impossível.
2. **Menos estado implícito**: o modelo não precisa rastrear CWD.
3. **Tokens para pensar**: paths absolutos são mais longos, mas eliminam ambiguidade.

## Lições para a Especialização

1. **Erros sistemáticos são sinais de design de tool, não de prompt.**
2. **Antes de reescrever o prompt pela 3ª vez, pergunte: posso redesenhar a tool?**
3. **Preferir restrições estruturais (schemas, formatos) a instruções verbais.**
4. **Observar com traces** — sem traces, o erro sistemático passa despercebido.

## Aplicação no Lab 1

O Lab 1 deste módulo replica exatamente essa dinâmica: tools mal desenhadas → diagnóstico → refatoração → re-medir. A meta é formar o **reflexo** de redesenhar a tool antes de culpar o prompt.

## Referências

- Anthropic. *Building Effective Agents*, Appendix 2. dez/2024.
- Albert, A. & Schluntz, E. *Building more effective AI agents* (YouTube).
