
'''
ANALISIS:un programa que reciba una frase o palabra, y ademas una letra que quiera ocultar en la misma.

VARIABLES DE ENTRADA
frase: representa la palabra o frase que el usuario ingresa
letra: representa una letra para ocultar

VARIABLES DE SALIDA
N/A
VARIABLES AUXILIARES
y=con el fin de determinar el tipo de valor que ingreso
z= con el fin el determianr la cantidad de elementos de la variabel que el usuario ingreso
frase2=almacena la frase o palabra modificada'''


frase = input("ingresa tu frase o palabra: ")
letra = input("ingresa una letra para oculpar: ")

y = letra.isalpha()
z = len(letra)

while y == True and z == 1:
    frase2 = frase.replace(letra, "*")
    print(frase2)
    break

if y == False:
    print("lo sentimos tu letra a ocultar presenta un error")

if z != 1:
    print("lo sentimos solo recibimos una letra a ocultar")
