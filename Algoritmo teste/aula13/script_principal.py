import random
from exibir_menu import exibir_menu
from valida_data import valida_data
from valida_cpf import valida_cpf

def cadastrar():
    nome = input("Digite o nome: ")
    sobrenome = input("Digite o sobrenome: ")

    while True:
        cpf = input("Digite o CPF no formato xxx.xxx.xxx-xx: ")
        if valida_cpf(cpf):
            break
        else:
            print("CPF inválido!")

    while True:
        data = input("Digite a data de nascimento no formato dd/mm/aaaa: ")
        if valida_data(data):
            break
        else:
            print("Data inválida!")

    renda_bruta = float(input("Digite a renda bruta: "))

    print("Cadastro realizado com sucesso!")
    print("Nome:", nome)
    print("Sobrenome:", sobrenome)
    print("CPF:", cpf)
    print("Data de Nascimento:", data)
    print("Renda Bruta:", renda_bruta)


def exibir_mensagem():
    mensagens = [
        "A persistência realiza o impossível",
        "Seus sonhos não precisam de plateia, eles só precisam de você",
        "A persistência é o caminho do êxito",
        "No meio da dificuldade encontra-se a oportunidade"
    ]
    mensagem = random.choice(mensagens)
    print("Mensagem Motivacional:")
    print(mensagem)


if __name__ == "__main__":
    while True:
        opcao = exibir_menu()
        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            exibir_mensagem()
        elif opcao == 3:
            print("Bye bye!")
            break