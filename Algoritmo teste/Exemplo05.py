from math import pow,sqrt

x1 = float(input("fale a variavel de x1:"))
x2 = float(input("fale a variavel de x2:"))
y1 = float(input("fale a variavel de y1:"))
y2 = float(input("fale a variavel de y2:"))

DX = x2 - x1
DY = y2 - y1

Dist = sqrt(pow(DX,2)+pow(DY,2))

print('o valor da distancia:', Dist)