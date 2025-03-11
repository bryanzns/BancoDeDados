import json
from carregar import arquivo
def salvar(dados):
    with open(arquivo, "w", encoding="utf-8") as arquivoa:
        json.dump(dados,arquivoa, indent=4, ensure_ascii=False)
