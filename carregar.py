import json
import os
arquivo = "arquivo.json"
def carregar():
    try:
        with open(arquivo, "r", encoding="utf-8") as arquivoa:
            return json.load(arquivoa)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


