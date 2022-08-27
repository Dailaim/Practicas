'''

ANALISIS: segun el tiempo que el usuario utilizo la bicicleta encontrar costo del uso del mismo

DATOS DE ENTRADA
minutos :timepo en minutos que el usuario uso el medio de transporte
mensaje de error-->segun el caso

DATOS DE SALIDA:
p: precio total a pagar

VARIABLES AUXILIARES
x1 almacenar los minutos restantes depsues de restar 120 de ellos
p1: precio por los primeros 100 minutos(7 pesos de cada miuto)
p1: precio po el resto de minutos(57 pesos de cada minuto)
fijo: precio dijo si hay mas de 1440 minutos'''


import math
minutos = input("escribe el numero total de minutos de uso de la bicicleta: ")


while True:
    minutos = float(minutos)
    if minutos < 0:
        print("lo sentimos el programa no acepta numeros negativos. Verifica tu error")
        break
    if minutos % 2 != 0 and minutos % 2 != 1:
        print("lo sentimos el programa no acepta numeros decimales. Verifica tu error")
        break

    if minutos < 100:
        p = minutos * 7
        p = math.ceil(p)
        print(p)

    elif minutos < 1440:
        x1 = minutos - 100
        p1 = 100*7
        p2 = x1 * 57
        p = p1+p2
        p = math.ceil(p)
        print(p)

    else:
        fijo = 96000
        x1 = minutos-100
        p1 = 100*7
        p2 = x1 * 57
        p = fijo + p1 + p2
        p = math.ceil(p)
        print(p)
    break
