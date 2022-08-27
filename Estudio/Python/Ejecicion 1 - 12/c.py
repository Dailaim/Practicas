'''
analisis: encontrar el area total del area superficial de un cilindro y su volumen

DATOS DE ENTRADA

radio: radio del ciclindro
altura: altura del cilindro

DATOS DE SALIDA
volumen: volumen del cilindro
area: area del cilindro

'''


import math

radio = input("Igresa el radio del cilindro: ")
altura = input("ingresa la altura del cilindro: ")


while True:
    radio = float(radio)
    altura = float(altura)
    if radio < 0:
        print("lo sentimos la medida del radio no puede ser negativa: verifica tu error")
        break
    if altura < 0:
        print("lo sentimos la altura del radio no puede ser negativa: verifica tu error")
        break

    volumen = (math.pi * radio**2 * altura)
    area = (2 * math.pi * radio * altura) + (2 * math.pi * radio**2)

    print(volumen)
    print(area)
    break
