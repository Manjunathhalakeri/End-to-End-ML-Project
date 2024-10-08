import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "MlProject"
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"
]

# Create folders and subfolders for all files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir = filepath.parent
    filename = filepath.name
    
    if not filedir.exists():
        filedir.mkdir(parents=True, exist_ok=True)
        logging.info(f"Creating directory: {filedir}")
    
    file_path = filedir / filename
    if not file_path.exists():
        file_path.touch()
        logging.info(f"Creating file: {file_path}")
    else:
        logging.info(f"File already exists: {file_path}")
