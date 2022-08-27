
'''
ANALISIS: UN PROGRAMA QUE RECIBA UNA PALABRA DEL USUARIO Y LA CODIFIQUE SEGUN UN NUMERO QUE DIGITO.

VARIABLES DE ENTRADA
palabra: palabra para codificar
numero: numero que usaremos para saber que letras usuremos
VARIABLES AUXILIARES
alfabeto: representa los elementos del alfabeto
x: Se una para iniciar el ciclo y terminarlo
uxiliar: con el fin de determinar si la plabra que ingreso el usuairo e svalida
cantidad: posicion de un elemento de la lista, que se le sumara el numero que el usurio digite

VAIRABLES DE SALIDA
N/A'''


alfabeto = "abcdefghijklmnopqrstuvwxyz"
palabra = input("ingresa tu palabra a codificar: ")
numero = input("ingresa tu numero: ")
palabra = palabra.lower()
x = 0

auxiliar = palabra.isalpha()

while x == 0 and auxiliar == True:
    numero = int(numero)
    if numero % 2 != 0 and numero % 2 != 1:
        print("lo sentimos numeros decimales no estan permitidos")
        break
    if numero < 0:
        print("lo sentimos numeros negativos no son validos.")
        break

    if numero > 26:
        print("lo sentimos tu numero no es valido")
        break
    for i in palabra:
        cantidad = alfabeto.index(i)
        cantidad = cantidad+numero
        if cantidad >= 26:
            cantidad = cantidad-26
        cantidad = int(cantidad)
        print(alfabeto[cantidad], end="")
        x = 2
if auxiliar == False:
    print("solo aceptamos letras en la palabra a codificar")
