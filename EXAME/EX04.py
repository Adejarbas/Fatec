nome_automovel = input("Digite o nome carro: ")
preco_fabrica = int(input("Digite o preço de fábrica: "))

print("Calculando...")

preco_impostos = int(0.45 * preco_fabrica)
preco_revendedor = int(0.28 * preco_fabrica)
preco_final = preco_fabrica + preco_impostos + preco_revendedor


print("Automóvel:", nome_automovel)
print(f"Preço de Fábrica..: R$ {preco_fabrica}")
print(f"Impostos..........: R$ {preco_impostos}")
print(f"Lucro Revendedor..: R$ {preco_revendedor}")
print(f"Preço Final.......: R$ {preco_final}")