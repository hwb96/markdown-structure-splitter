# -*- coding: utf-8 -*-
import os
from pathlib import Path

# 获取项目根目录
PROJECT_ROOT = Path(__file__).parent.parent.parent

# 数据目录配置
DATA_DIR = PROJECT_ROOT / 'data'
INPUT_DIR = DATA_DIR / 'input'
OUTPUT_DIR = DATA_DIR / 'output'

# 确保目录存在
DATA_DIR.mkdir(exist_ok=True)
INPUT_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)