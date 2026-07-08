# planning/02-plan-decomposition.md

## objetivo
Prompt que decompõe uma tarefa complexa em sub-etapas ordenadas, com dependências explícitas.

## variáveis
- `{{task}}` — descrição da tarefa a ser decomposta
- `{{max_subtasks}}` — número máximo de sub-etapas permitido
- `{{output_format}}` — formato esperado (lista, markdown, JSON)

## template

```
Break down the following task into a sequence of subtasks.

Task: {{task}}

Requirements:
- Produce at most {{max_subtasks}} subtasks.
- Each subtask must be independently executable.
- Specify dependencies between subtasks.
- Output in the following format: {{output_format}}

For each subtask, include:
1. ID (e.g., ST-01)
2. Description
3. Dependencies (list of IDs that must be completed first)
4. Estimated effort (low / medium / high)

Order subtasks so that dependencies are always resolved before dependent tasks.
```

## exemplo de uso
`{{task}}` = "Implementar login com Google OAuth" → ST-01: configurar credenciais, ST-02: criar endpoint de callback, etc.

## trade-offs
- Pode super-decompor tarefas simples, gerando sobrecarga cognitiva
- Dependências incorretas inviabilizam o plano
- Muito útil em tarefas com muitas etapas encadeadas (e.g., pipelines de dados)

## variações
- **DAG-based**: incluir grafo de dependências visual (textual ou mermaid)
- **Milestone decomposition**: agrupar subtarefas em marcos com prazos
- **Decomposition with effort estimation**: adicionar estimativa de tempo ou pontos de história
