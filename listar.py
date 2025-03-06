def listar():
    print(' LISTAGEM DE PESSOAS')
    print('-' * 30)
    print('1 -- quero ver todos da lista')
    print('2 -- quero ver somente os dados de 1 pessoa da lista')
    quer = int(input(' qual opçao voce quer? [1/2]'))
    if quer == 1:
        for c,pessoa in enumerate(banco_de_dados):
            print(f' pessoa{c}:')
            print(f' Nome: {pessoa['nome']}')
            print(f' cpf: {pessoa['cpf']}')
            print(f' data de nascimento: {pessoa['data_de_nasc']}')
            print(f' estado civil {pessoa['estado_civil']}')
            print('-' * 30)
    if quer == 2:
        escolha = (' qual o numero da pessoa que voce quer ver? ')
        for c,pessoa in enumerate(banco_de_dados):
            if c == escolha:
                 print(f' pessoa{c}:')
                 print(f' Nome: {pessoa['nome']}')
                 print(f' cpf: {pessoa['cpf']}')
                 print(f' data de nascimento: {pessoa['data_de_nasc']}')
                 print(f' estado civil {pessoa['estado_civil']}')
                 print('-' * 30)

if __name__ == "__main__":
    listar()


