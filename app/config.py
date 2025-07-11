import yaml
import os

def load_models_config(path=None):
    if not path:
        path = os.path.join(os.path.dirname(__file__), "models.yml")
    with open(path, "r") as f:
        data = yaml.safe_load(f)
    return data["models"]