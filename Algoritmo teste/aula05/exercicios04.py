a = float(input("digite um valor"))
b = float(input("digite um valor"))
c = float(input("digitei um valor"))
if  ((a+b)<c) or ((b+c)<a) or ((a+c)<b):
    print ("nao e um triangulo")
elif (a==b==c):
    print ("lados iguais")
elif (a==b) or (a==c) or (b==c):
    print ("um lado dierente")
else:
    print (" tres lados diferentes")



