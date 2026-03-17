# utils/config_loader.py
import os
import yaml


def load_yaml(relative_path):
    """从项目根目录读取 YAML 文件。运行时请保证在项目根执行 pytest。"""
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(root, relative_path)
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
