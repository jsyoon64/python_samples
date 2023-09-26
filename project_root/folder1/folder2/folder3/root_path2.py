import sys
import os

PROJECT_ROOT = 'project_root'
cur_path = os.path.abspath(__file__)
path_list = cur_path.split(os.sep)
ROOT_DIR = cur_path

for folder in path_list[::-1]:
    if folder != PROJECT_ROOT:
        ROOT_DIR = os.path.dirname(ROOT_DIR)
    else:
        break

print(f'{cur_path=}\n{ROOT_DIR=}')
