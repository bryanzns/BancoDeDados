# importar o banco de dados
from .banco import banco_de_dados, salvar_Banco
# aqui fica a def de colocar pessoas novas

def incluir():
    nome = str(input(' NOME: '))
    cpf = int(input(' CPF:'))
    data_nasc = str(input(' data de nascimento: '))
    estado_civil = str(input(' estado civil: '))
    pessoa = {'nome': nome, "cpf":cpf, 'data_de_nasc' : data_nasc, 'estado_civil': estado_civil}
    print(pessoa)
    banco_de_dados.append(pessoa)
    # agora, toda vez que modificar o banco, tem que salvar ele no arquivo
    salvar_Banco()


if __name__ == "__main__":
    incluir()

