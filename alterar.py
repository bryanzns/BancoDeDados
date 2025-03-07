from .banco import banco_de_dados, salvar_banco

def alterar():
   # é uma boa prática sempre que precisar ler algum dado do usuário validar
   # usando o try
   while True :
      # na hora de alterar é bom exibir os dados da pessoa
      for numero , pessoa in enumerate(banco_de_dados) :
         print(f"{numero}={pessoa.nome} {pessoa.CPF}")
      print() # uma linha em branco para ficar mais legal
      pass # esse pass não é necessário. estou usando-o aqui apenas para usar como exemplo.
      # a variável qual_pessoa conterá o 
      qual_pessoa = int(input(' qual o numero da pessoa que voce que voce quer alterar: '))
      # aqui é melhor escolher qual registro (número da pessoa) vai ser alterado primeiro
      #
      if qual_pessoa < 0 or qual_pessoa >= len(banco_de_dados):
         print("Favor informe um número de registro válido")
      
      pessoa_a_alterar = banco_de_dados[qual_pessoa] # pegamos os dados da pessoa, vamos mostrar para o usuário
      for numero, (campo, valor) in enumerate(pessoa_a_alterar.items())    # .items() retorna uma lista de campos e seus respectivos valores
         print( f"{numero+1}:{campo} = {valor}")
      qual_campo = int("Informe o número do campo que quer alterar")
      # aqui novamente caberia uma validação. Aí você se pergunta, melhor fazer uma função que faz isso! 
      # tente criar uma função que lê dados do console do usuário e faz a validação, retornando um valor.
      #
      # agora vamos alterar o campo
      if qual_campo == 1:
         pessoa_a_alterar.nome  = str(input(' digite o nome novo: '))
      if qual_campo == 2:
         pessoa_a_alterar.CPF = int(input(' digite o novo cpf: '))
      if qual_campo == 3:
         pessoa_a_alterar.data_de_nasc = str(input(' digite a nova data de nascimento: '))
      if qual_campo == 4:
         pessoa_a_alterar.estado_civil = str(input(' digite o novo estado civil (se casou agora?kkk): '))
      #
      # depois de alterar a pessoa, vamos colocar ela no banco de dados
      banco_de_dados[qual_pessoa] = pessoa
      # agora vamos salvar o banco no arquivo
      salvar_banco()

if __name__ == "__main__":
    alterar()




