'''

Anlisis: encontrar el minimo numero de moendad para devolver segun el numero digitado po el usuario.

DATOS DE ENTRADA
cantidad:dinero a devolver

DATOS DE SALIDA
M1:numero completo de monedas de 1000, si se da el caso
M2:numero completo de monedas de 500, si se da el caso
M3:numero completo de moendad de 200, si se da el caso
m4:numero compelto de monedas 100, si se da el caso
M5: numero completo de moendas de 50, si se da el caso
cantidad: cantidad que no puede devolver en monedad, segun el caso

'''


import math
cantidad = input("ingresa tu cantidad a devolver:")


while True:
    cantidad = float(cantidad)
    if cantidad < 0:
        print("lo sentimos el programa no acepta nuemeros negativos. Verifica tu error")
        break

    if cantidad >= 1000:
        M1 = cantidad//1000
        cantidad = cantidad-(1000*M1)
        M1 = math.ceil(M1)
        print(M1)

    else:
        print(0)

    if cantidad >= 500:
        M2 = cantidad//500
        cantidad = cantidad-(500*M2)
        M2 = math.ceil(M2)
        print(M2)

    else:
        print(0)

    if cantidad >= 200:
        M3 = cantidad//200
        cantidad = cantidad-(200*M3)
        M3 = math.ceil(M3)
        print(M3)

    else:
        print(0)

    if cantidad >= 100:
        M4 = cantidad//100
        cantidad = cantidad-(100*M4)
        M4 = math.ceil(M4)
        print(M4)
    else:
        print(0)
    if cantidad >= 50:
        M5 = cantidad//50
        cantidad = cantidad-(50*M5)
        M5 = math.ceil(M5)
        print(M5)
    else:
        print(0)
    if cantidad == 0:
        print(0)
        break
    else:
        cantidad = math.ceil(cantidad)
        print(cantidad)
        break
