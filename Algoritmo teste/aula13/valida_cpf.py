def valida_cpf(cpf):

    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    total = 0
    multiplicador = 10
    for i in range(9):
        total += int(cpf[i]) * multiplicador
        multiplicador -= 1
    resto = total % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto

    total = 0
    multiplicador = 11
    for i in range(10):
        total += int(cpf[i]) * multiplicador
        multiplicador -= 1
    resto = total % 11
    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto

    if digito1 == int(cpf[9]) and digito2 == int(cpf[10]):
        return True
    else:
        return False

if __name__ == "__main__":
    cpf = input("Digite o CPF no formato xxx.xxx.xxx-xx: ")
    if valida_cpf(cpf):
        print("CPF válido!")
    else:
        print("CPF inválido!")
