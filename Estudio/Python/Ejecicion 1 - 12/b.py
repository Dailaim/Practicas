'''
analisis: pasar de radianes a grados cierta cantidad
DATOS DE ENTRADA
radianes:cantidad de radianes

DATOS DE SALIDA
grados: cantidad de grados
'''

import math


radianes = input("digite la cantidad de radianes para covertir a grados: ")


while True:
    radianes = float(radianes)

    if radianes > 2*math.pi or radianes < -(2*math.pi):
        print("lo sentimos la cantidad de radianes ingresados no son validos. Verifica tu error")
        break
    grados = radianes * (180/math.pi)
    grados = math.ceil(grados)
    print(grados)
    break
