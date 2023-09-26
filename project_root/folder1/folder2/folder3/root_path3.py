import sys
import os

PROJECT_ROOT = 'project_root'
ROOT_DIR = cur_path = os.path.abspath(__file__)
basename = os.path.basename(ROOT_DIR)

while basename != PROJECT_ROOT and basename !='':
    ROOT_DIR,_ = os.path.split(ROOT_DIR)
    basename = os.path.basename(ROOT_DIR)

print(f'{cur_path=}\n{ROOT_DIR=}')
