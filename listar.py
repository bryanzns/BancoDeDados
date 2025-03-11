from carregar import carregar
def listar():
    dado = carregar()
    print(' LISTAGEM DE PESSOAS')
    print('-' * 30)
    print('1 -- quero ver todos da lista')
    print('2 -- quero ver somente os dados de 1 pessoa da lista')
    quer = int(input(' qual opçao voce quer? [1/2]'))
    if quer == 1:
        for pessoa in dado:
            print(f' id: {pessoa['id']}')
            print(f' Nome: {pessoa['nome']}')
            print(f' cpf: {pessoa['cpf']}')
            print(f' data de nascimento: {pessoa['data_de_nasc']}')
            print(f' estado civil {pessoa['estado_civil']}')
            print('-' * 30)
    if quer == 2:
        escolha = (' qual o id da pessoa que voce quer ver? ')
        for pessoa in dado:
            if pessoa["id"] == escolha:
                print(f' Nome: {pessoa['nome']}')
                print(f' cpf: {pessoa['cpf']}')
                print(f' data de nascimento: {pessoa['data_de_nasc']}')
                print(f' estado civil {pessoa['estado_civil']}')
                print('-' * 30)

if __name__ == "__main__":
    listar()


