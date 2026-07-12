#!/usr/bin/env python3
"""
Sincroniza pastas numeradas (00-27) do diretorio raiz para docs/.

Usado pelo deploy.yml antes do mkdocs build para garantir que o site
sempre reflita a versao mais recente dos slides, apostilas, etc.

Uso:
    python sync_docs.py          # sincroniza tudo
    python sync_docs.py --dry-run  # mostra o que seria copiado sem copiar
"""

import os
import sys
import shutil
import hashlib
from pathlib import Path

ROOT = Path(__file__).parent
DOCS = ROOT / "docs"

# Pastas numeradas que devem ser sincronizadas
SYNC_FOLDERS = [f"{i:02d}-{name}" for i, name in enumerate([
    "Governanca", "Curriculum", "Syllabus", "Slides", "Apostilas",
    "Labs", "Projects", "Exercises", "Assignments", "CaseStudies",
    "Architecture", "AgentPatterns", "Diagrams", "Workflows", "MCP",
    "RAG", "Memory", "PromptLibrary", "Tools", "Examples",
    "Research", "Papers", "Glossary", "Exams", "Templates",
    "Checklists", "Capstone", "Certification"
], 0)]

# Excluidos de sync (nao existem no topo ou sao apenas docs)
SKIP_PATTERNS = {".git", "__pycache__", ".cache", "site"}


def file_hash(path: Path) -> str:
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def sync_folder(name: str, dry_run: bool = False) -> int:
    src = ROOT / name
    dst = DOCS / name

    if not src.is_dir():
        return 0
    if not dst.is_dir():
        print(f"  SKIP {name}: docs/{name}/ nao existe")
        return 0

    copied = 0
    for root, dirs, files in os.walk(src):
        # Pular diretorios ignorados
        dirs[:] = [d for d in dirs if d not in SKIP_PATTERNS]

        rel = Path(root).relative_to(src)
        dst_dir = dst / rel

        for fname in sorted(files):
            src_file = Path(root) / fname
            dst_file = dst_dir / fname

            # Pular se destino existe e eh identico
            if dst_file.exists() and file_hash(src_file) == file_hash(dst_file):
                continue

            if dry_run:
                action = "UPDATE" if dst_file.exists() else "NEW"
                print(f"  {action} {name}/{rel}/{fname}")
            else:
                dst_dir.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_file, dst_file)
                print(f"  COPIED {name}/{rel}/{fname}")

            copied += 1

    return copied


def main():
    dry_run = "--dry-run" in sys.argv

    if dry_run:
        print("=== DRY RUN ===\n")

    total = 0
    for folder in SYNC_FOLDERS:
        count = sync_folder(folder, dry_run)
        total += count

    print(f"\n{'(dry run) ' if dry_run else ''}Total: {total} arquivos copiados")


if __name__ == "__main__":
    main()
