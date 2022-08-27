'''
ANALISIS: ENCONTRAR LOS CAMBIOS DE ACEITE DEPENDIENDO DE LOS KILOMETROS RECORRIDOS

DATOS ENTRADA
kms:kilometros recorridos
DATOS DE SALIDA
cambios: cambios en el tiempo transcurrido
mensaje de error-->segun el caso

'''


import math
kms = input("ingresa los kilometros recorridos por el auto: ")


while True:
    kms = float(kms)
    if kms < 0:
        print("lo sentimos la cantidad ingresa de kilometros no puede ser negativa; verifica tu error")
        break
    cambios = kms//5678
    cambios = math.ceil(cambios)
    print(cambios)
    break
