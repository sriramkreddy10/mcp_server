# registry/registry_loader.py

import yaml  # or json
import os

_registry_cache = None

def load_registry(path="registry/model_registry.yaml"):
    global _registry_cache
    if _registry_cache:
        return _registry_cache

    with open(path, "r") as f:
        data = yaml.safe_load(f)
        _registry_cache = data
        return data
