# docs — Site estático (MkDocs)

A Especialização publicada como site navegável, construído com **mkdocs-material**.

## Uso

```powershell
mkdocs serve      # preview local em http://localhost:8000
mkdocs build      # gera site/ (HTML estático)
```

## Estrutura

- `index.md` — página inicial
- `sobre/` — governança, roadmap, ADRs
- `curriculo/` — grade, competências, fases, rastreabilidade
- `cursos/ETHAGT0x/index.md` — página de cada módulo com links para conteúdo
- `bibliotecas/` — arquiteturas, padrões, workflows, RAG, memória, MCP, prompts, ferramentas, glossário
- `pesquisa/` — master index, papers
- `avaliacao/` — provas modulares, capstone, certificação
- `templates/` — templates e checklists

As páginas do site são **overlays de navegação** — os links apontam para os arquivos reais no repositório (funcionam no GitHub, não no site estático).

## Build

```powershell
pip install mkdocs mkdocs-material
mkdocs build
```

Output vai para `site/` (adicionado ao `.gitignore`).
