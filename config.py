import os
from pathlib import Path

path_log_backup_master = r"C:\Users\Роман\Desktop\git\log_backup_master"

path_gitignore = os.path.join(path_log_backup_master, ".gitignore")

with open(path_gitignore, "w", encoding="utf-8") as f:
    f.write(""" #Python cache
 __pycache__/
*.pyc

# OS files
.DS_Store
Thumbs.db

# Project local data
data/backups/""")

file_path = Path(__file__).resolve().parent
path_to_create = [
    file_path / "main.py",
    file_path / "core" / "__init__.py",
    file_path / "core" /"analyzer.py",
    file_path / "utils" / "__init__.py",
    file_path / "utils" / "decorators.py",
    file_path / "data" / "source_docs" / "sample.log"
]

for p in path_to_create:
    if p.suffix:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.touch()
    else:
        p.mkdir(parents=True, exist_ok=True)







