def exibir_menu():
    while True:
        print("Menu:")
        print("1 - Cadastrar")
        print("2 - Exibir Frase")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao.isdigit():
            opcao = int(opcao)
            if 1 <= opcao <= 3:
                return opcao
            else:
                print("Opção inválida! Por favor, escolha uma opção entre 1 e 3.")
        else:
            print("Opção inválida! Por favor, digite um número entre 1 e 3.")
