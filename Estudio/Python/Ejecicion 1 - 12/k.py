'''
Analisis: determinar el patron secuencial segun corresponda al numero que ingreso el usuario.

DATOS DE ENTRADA:
numero: numero impar que ingresa el usuario


DATOS DE SALIDA:
El algoriitmo imprmime asteriscos en orden especifico con el fin de determinar el patron deseado

VARIABLES AUXILIARES:
ci: es una variable que actua como contador; su funcion es ir sumando hasta que iguale el valor de contador
contador: representala cnatidad de asteriscos a imprimir en cada linea, hasta que constador no sea igual al numero la persona, se imprimen el numero de asteriscos que tiene dicha variable, y despues de cicho objetivo, disminuye hasta que sea menor que 0, y simultaneamente en el proceso de disminucion de la variable imprime los asteriscos correspondientes.
'''


numero = input("ingresa tu numero impar: ")
contador = 1


while True:
    numero = float(numero)
    if numero <= 0:
        print("lo sentimos no aceptemos  numeros negativos. Verifica tu error")
        break
    if numero % 2 != 0 and numero % 2 != 1:
        print("lo sentimos el programa no acepta numeros decimales. Veridica tu error")
        break
    if numero % 2 == 0:
        print("lo sentimos el programa no acepta numeros pares. Verifica tu error")
        break

    while contador <= numero:
        print(" ")
        ci = 0
        while ci < contador:
            print("*", end="")
            ci = ci+1
        contador = contador+2

    contador = contador-4

    while contador >= 0:
        print("")
        ci = 0
        while ci < contador:
            print("*", end="")
            ci = ci+1
        contador = contador-2
    break
