print('Calculo de tinta para pintura')

largura = float(input('\nInsira a largura do comomo: '))
comprimento = float(input('\nInsira o comprimento do comodo: '))
altura = 2.8
tamanho_lata = input("\nQual o tamanho da lata: \n(Litro) = 1 litro \n (Galão) = 3.6 litros \n (Lata) = 18 litros\n")
area_porta = 0.8 * 2.1
rendimento = 3

if tamanho_lata == 'Litro':
    tamanho_lata = 1
else:
    if tamanho_lata == "Galão":
        tamanho_lata = 3.6
    else:
        if tamanho_lata == "Lata":
            tamanho_lata = 18
        else:
            tamanho_lata = 1

area = (largura * altura * 2) + (comprimento * altura * 2)
area = area - area_porta

litros_necessarios = area / rendimento
qtd_latas = litros_necessarios / tamanho_lata

if(qtd_latas - int(qtd_latas)) > 0:
    qtd_latas = int(qtd_latas) + 1

print(f"Qtd latas necessárias: ")