print("Cálculo de Descontos")

valor = float(input("Insira o valor da compra: "))
if valor <= 1000:
    valor2 = valor*0.1
    print(f"\nO desconto para R${valor} é de R${valor2:.2f} (10%). Valor total: R${valor - valor2:.2f}")
else:
    if(valor >= 1000.01) and (valor <= 5000):
        valor2 = valor*0.2
        print(f"\nO desconto para {valor} é de {valor2:.2f} (20%). Valor total da compra: {valor - valor2:.2f}")
    else:
        if valor > 5000:
            valor2 = valor*0.3
            print(f"\nO desconto para {valor} é de {valor2:.2f} (30%). Valor total da compra: {valor - valor2:.2f}")
