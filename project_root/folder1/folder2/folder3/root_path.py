from pathlib import Path

PROJECT_ROOT = 'project_root'
cur_path = Path(__file__)

ROOT_DIR = next(
                 p for p in cur_path.parents if p.parts[-1] == PROJECT_ROOT
               )

print(f'{cur_path=}\n{ROOT_DIR=}')