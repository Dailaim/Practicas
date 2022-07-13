
from cmath import pi


a = int(input("valor de a: "))

b = int(input("valor de b: "))

c = int(input("valor de c: "))

discrimiante = (b*b)-4*a*c

if discrimiante < 0:
    print("No tiene soluciones reales")

else:
    x1= (-b + (discrimiante)**0.5)/(2*a)
    x2= (-b - (discrimiante)**0.5)/(2*a)

    print(x1)
    print(x2)