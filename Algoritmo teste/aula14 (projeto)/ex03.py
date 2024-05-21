numero_str = input("Digite um número positivo: ")

soma = 0
multiplicacao = 1


if numero_str.isdigit():

    for digito in numero_str:

        digito = int(digito)
        soma += digito
        multiplicacao *= digito


    print(f"Soma dos dígitos: {soma}")
    print(f"Multiplicação dos dígitos: {multiplicacao}")
else:
    print("Entrada inválida. Por favor, insira um número positivo.")