from carregar import carregar
from salvar import salvar
def excluir():
    dado = carregar()
    print(' PARA REMOVER UMA PESSOA ESPECIFICA, PRIMEIRO VEJA A LISTAGEM DE TODOS PARA SABER O ID')
    escolha = int(input(' Qual pessoa voce quer remover?[id]:'))
    for  c,i in enumerate(dado):
         if i["id"] == escolha:
            del dado[c]
            print(f' dados de pessoa sendo excluida...')
            salvar(dado)
            break
    print(' concluido.')

if __name__ == "__main__":
    excluir()

