def primo(n):

    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def contar_primos(ate):

    contador = 0
    for num in range(ate + 1):
        if primo(num):
            contador += 1
    return contador

def somar_primos(ate):

    soma = 0
    for num in range(ate + 1):
        if primo(num):
            soma += num
    return soma


numero = int(input("Digite um número: "))
quantidade_primos = contar_primos(numero)
soma_primos = somar_primos(numero)

print(f"Existem {quantidade_primos} números primos de 0 até {numero}.")
print(f"A soma dos números primos de 0 até {numero} é {soma_primos}.")


y = soma_primos
resultado = y * 2 + 5
print(f"Resultado da expressão y * 2 + 5 onde y é a soma dos primos: {resultado}")

