def excluir():
    print(' PARA REMOVER UMA PESSOA ESPECIFICA, PRIMEIRO VEJA A LISTAGEM DE TODOS PARA SABER A NUMERAÇAO')
    escolha = int(input(' Qual pessoa voce quer remover?'))
    for p,c in enumerate(banco_de_dados):
        if p == escolha:
            del banco_de_dados[p]
            print(f' dados de pessoa {banco_de_dados[p]} sendo excluida...')
    print(' concluido.')

if __name__ == "__main__":
    excluir()

