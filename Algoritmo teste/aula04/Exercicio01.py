idade =  int(input('escreva que ano você nasceu:'))
ano = int(input('escreva o ano atual:'))

a = ano - idade
b = a * 12
d = a * 52
c = a * 365

print('A idade dessa pessoa em anos é:', a)
print('A idade dessa pessoa em meses é:', b)
print('A idade dessa pessoa em dias é:', c)
print('A idade dessa pessoa em semanas é:', d)