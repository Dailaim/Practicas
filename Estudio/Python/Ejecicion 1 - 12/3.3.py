'''
ANALISIS: un porgrama que detemrine si una palabra es palindroma o no.

VARIABLES DE ENTRADA
palabra: palabra ingresada por el usuario
VARIABLES AUXILIARES
cantidad:significa el numero de un indice de un lemento que compone la palabra
auxiliar:significa el numero de un indice de un lemento que compone la palabra
x: para determinar el tipo de dato que contiene la variable que ingreso el usuairo
VIRBALES DE SALIDA
N/A'''


alfabeto = "bcdfghjklmnpqrstvwxyx"
abecedario = "aeiou"

palabra = input("ingresa una palabra: ")
cantidad = len(palabra)
cantidad = cantidad-1
auxiliar = 0


x = palabra.isalpha()

palabra = palabra.lower()

while palabra[auxiliar] == palabra[cantidad] and x == True:
    auxiliar = auxiliar+1
    cantidad = cantidad-1
    if auxiliar == cantidad or auxiliar == cantidad-1 or auxiliar-1 == cantidad:
        print("tu palabra es palindroma")
        auxiliar = 0
        cantidad = 0
        break


if auxiliar != cantidad and auxiliar != cantidad-1 and auxiliar-1 != cantidad:
    print("tu palabra no es palindroma")

if x == False:
    print("lo sentimos solo captamos letras")
