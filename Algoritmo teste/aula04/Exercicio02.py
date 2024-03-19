Salario = float(input('escreva o salario inicial:'))
porcentual = float(input('escreva o porcentual de aumento:'))

A = Salario * porcentual / 100

print(f'valor de aumento: R$ {A:8.2f}')
print(f'novo salario: R$ {Salario + A:8.2f}')