# aqui a ideia é "persistir" os dados no arquivo, ou seja, salvar os dados digitados entre um uso e outro do programa

import os
import json

ARQUIVO_PESSOAS = "arquivo_de_pessoas.json" # sempre que puder, salve em json pois facilita. Não é o modo mais rápido, no entanto

banco_de_dados = [] 
# primeiro, testamos se o banco existe, se tem o arquivo com os dados
if os.path.exists(ARQUIVO_PESSOAS):
    with open(ARQUIVO_PESSOAS, 'r') as arquivo_pessoas:
        banco_de_dados = json.load(arquivo_pessoas)
pass

def banco():
    return banco_de_dados

# função para salvar o banco no arquivo

def salvar_banco():
    with open(ARQUIVO_PESSOAS, "w") as arquivo_pessoas:
        json.dump(banco_de_dados, arquivo_pessoas)