
import json
from typing import Dict

path_config = 'TRABALHO2\data\configs\config.json'

def load_config(path: path_config) -> Dict:
    with open(path, 'r') as f:
        config = json.load(f)
    return config