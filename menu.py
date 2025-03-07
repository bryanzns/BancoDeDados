import incluir
import alterar
import excluir
import listar

# Menu de opções
def menu():
    while True:
        print('CADASTRO DE PESSOAS')
        print('-' * 30)
        print('1 -- incluir uma nova pessoa')
        print('2 -- alterar os dados de uma pessoa')
        print('3 -- excluir uma pessoa')
        print('4 -- listar todas ou uma parte das pessoas')
        print('5 -- sair do menu de pessoas')
        print('POR FAVOR ESCOLHA UMA OPÇÃO ENTRE 1 E 5')
        # excelente uso do try !!!
        try:
            opcao = int(input('Faça sua escolha aqui: '))
            
            if opcao == 1:
                incluir.incluir()
            elif opcao == 2:
                alterar.alterar()
            elif opcao == 3:
                excluir.excluir()
            elif opcao == 4:
                listar.listar()
            elif opcao == 5:
                break
            else:
                print('Opção inválida! Tente novamente.')
        except ValueError:
            print('Erro! Digite um número entre 1 e 5.')
    #
    # aqui estamos fora do loop. Sempre é bom colocar alguma coisa DEPOIS do fim do while. 
    # Se não tiver nada para colocar, as vezes é bom colocar um pass
    # 
    print('Programa encerrado. Obrigado por usar o software de Bryan.')

if __name__ == "__main__":
    menu()
