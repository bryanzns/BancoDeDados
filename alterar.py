import banco
def alterar():
    escolha = int(input(' qual o numero da pessoa que voce que voce quer alterar o dado: '))
    for c,pessoa in enumerate(banco.banco()):
        if c == escolha:
             print(' o que voce quer alterar?')
             print('1 -- nome')
             print('2 -- cpf ')
             print('3 -- data de nascimento')
             print('4 -- estado civil')
             quer = int(input(' digite o numero da sua escolha: '))
             if quer == 1:
                troca = str(input(' digite o nome novo: '))
                pessoa['nome'] = troca
             if quer == 2:
                troca = int(input(' digite o novo cpf: '))
                pessoa['cpf'] = troca
             if quer == 3:
                troca = str(input(' digite a nova data de nascimento: '))
                pessoa['data_de_nasc'] = troca
             if quer == 4:
                troca = str(input(' digite o novo estado civil (se casou agora?kkk): '))
                pessoa['estado_civil'] = troca


if __name__ == "__main__":
    alterar()




