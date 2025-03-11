from carregar import carregar 
from salvar import salvar
def alterar():
    dados = carregar()
    escolha = int(input(' qual o id da pessoa que voce que voce quer alterar o dado: '))
    for pessoa in dados:
        if pessoa["id"] == escolha:
             print(' o que voce quer alterar?')
             print('1 -- nome')
             print('2 -- cpf ')
             print('3 -- data de nascimento')
             print('4 -- estado civil')
             quer = int(input(' digite o numero da sua escolha: '))
             if quer == 1:
                troca = str(input(' digite o nome novo: '))
                pessoa['nome'] = troca
                salvar(dados)
             if quer == 2:
                troca = int(input(' digite o novo cpf: '))
                pessoa['cpf'] = troca
                salvar(dados)
             if quer == 3:
                troca = str(input(' digite a nova data de nascimento: '))
                pessoa['data_de_nasc'] = troca
                salvar(dados)
             if quer == 4:
                troca = str(input(' digite o novo estado civil (se casou agora?kkk): '))
                pessoa['estado_civil'] = troca
                salvar(dados)

if __name__ == "__main__":
    alterar()




