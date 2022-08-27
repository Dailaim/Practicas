'''
ANALISIS:Determinar un patron secuencial especifico segun el numero impar que digite el usuario.

DATOS DE ENTRADA
numero: es la cantidad impar de asteriscos que el usuario digitara.

DATOS DE SALIDA
-asteriscos y espacios que corrspondientes a la figura a obtener segun el numero dado.

VARIABLES AUXIALIARES
esp:despues de imprimir en cada linea los asteriscos correspondiente segun la variable ciclo. Significa la cantidad de espacios que debe imprmir a continuacion
contador: es la variable  que nos ayuda a contar el numero de asteriscos a imprmir en cada linea, hasta que no llegue al numero que representa el ciclo no deja de imprimir
ciclo: es el numero de asteriscos que se imprimimen en cada linea estos disminuyen de dos en dos
ci2:es el contador para imprimir los espacios necesarios, cuando es igual a la variable espacios deja de hacer esta funcion.
'''


ciclo = 1
esp = 1
contador = 1
numero = input("ingresa tu numero impar: ")

while True:
    numero = float(numero)

    if numero <= 0:
        print("lo sentimos no aceptamos numeros negativos. Verifica tu error")
        break
    if numero % 2 != 0 and numero % 2 != 1:
        print("lo sentimos el programa no acepta numeros decimales")
        break
    if numero % 2 == 0:
        print("lo sentimos el programa no acepta numeros pares")
        break

    while contador <= numero*2:
        print("+", end="")
        contador = contador+1
    ciclo = numero
    ciclo = ciclo-2
    print("")

    while ciclo >= 1:
        ci = 0
        while ci < ciclo:
            print("+", end="")
            ci = ci+1
        espacios = esp*4
        ci2 = 1

        while ci2 <= espacios:
            print(" ", end="")
            ci2 = ci2+1
        ci = 0
        while ci < ciclo:
            print("+", end="")
            ci = ci+1
        print()
        esp = esp+1
        ciclo = ciclo-2
    break
