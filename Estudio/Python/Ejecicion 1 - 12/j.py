'''
Analisis: determinar el maximo comun divisor de dos numeros digitados

VARIABLES DE ENTRADA:
a:primer numero digitado por el usuario
b: segundos numero digitado por el usuario
VARIABLES DE SLAIDA
MCD: Representa el maximo comun divisor entre ambos numeros
Variables Auxiliares:
x:nos ayuda a determinar tipo de valro que tiene la variable que ingreso el usuario'''


import math
a = input("ingresa el primer numero: ")
b = input("ingresa el segundo numero: ")


while True:
    a = float(a)
    b = float(b)
    if a < 0:
        print("lo sentimos el programa no acepta numeros negativos. Verifica tu error")
        break
    if b < 0:
        print("lo sentimos el programa no acepta numeros negativos. Verifica tu error")
        break
    if a == 0:
        print("lo sentimos el programa no acepta numeros iguales a cero. Verifica tu error")
        break
    if b == 0:
        print("lo sentimos el programa no acepta numeros iguales a cero. Verifica tu error")
        break

    while b != 0:
        MCD = b
        b = a % b
        a = MCD
    MCD = math.ceil(MCD)
    print(MCD)
    break
