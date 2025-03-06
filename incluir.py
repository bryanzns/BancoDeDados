# aqui fica a def de colocar pessoas novas
def incluir():
    nome = str(input(' NOME: '))
    cpf = int(input(' CPF:'))
    data_nasc = str(input(' data de nascimento: '))
    estado_civil = str(input(' estado civil: '))
    pessoa = {'nome': nome, "cpf":cpf, 'data_de_nasc' : data_nasc, 'estado_civil': estado_civil}
    print(pessoa)
    banco_de_dados.append(pessoa)

if __name__ == "__main__":
    incluir()

