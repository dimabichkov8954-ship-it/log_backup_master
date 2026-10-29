import os

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