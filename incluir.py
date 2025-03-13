from carregar import carregar
from salvar import salvar
# aqui fica a def de colocar pessoas novas
def incluir():
    dados = carregar()
    dados = list(carregar())
    nome = str(input(' NOME: '))
    cpf = int(input(' CPF:'))
    data_nasc = str(input(' data de nascimento: '))
    estado_civil = str(input(' estado civil: '))
    pessoa = {"id": len(dados) + 1,'nome': nome, "cpf":cpf, 'data_de_nasc' : data_nasc, 'estado_civil': estado_civil}
    dados.append(pessoa)
    salvar(dados)

if __name__ == "__main__":
    incluir()