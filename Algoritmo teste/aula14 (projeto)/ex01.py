def cabeca_pes(cabecas, pes):

    coelhos = (pes - 2 * cabecas) / 2
    patos = cabecas - coelhos

    return coelhos, patos


cabecas = int(input("Digite o número total de cabeçass: "))
pes = int(input("Digite o número total de pés: "))

coelhos, patos = cabeca_pes(cabecas, pes)

print(f"Coelhos: {coelhos}")
print(f"Patos: {patos}")

