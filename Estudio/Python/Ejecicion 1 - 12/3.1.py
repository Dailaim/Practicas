'''
ANALISIS: un programa que determine si una letra es vocal o consonante

VARIABLES DE ENTRADA
string: letra que el usuario digitara

VARIABLES DE SALIDA
N/A

VARIABLES AUXILIARES
x: variable con el fin de determianr que tipo de dato ingreso el usurio
vocales: contiene las letras que representan vocales
consonante=contiene las letrs que representan consonntes
auxiliar= para guardar la cantidad de elementos de la variable que el usuario ingreso'''


vocales = ("a", "e", "i", "o", "u")
consonantes = ("bcdfghjklmnñpqrstvwxyz")
string = input("introduce una letra: ")
string = string.lower()
auxiliar = len(string)

x = string.isalpha()

while x == True and auxiliar == 1:
    if string in vocales:
        print("vocal")

    elif string in consonantes:
        print("consonante")
    x = 2

if x == False:
    print("lo sentimos recuerda solo recibimos una letra.")

if auxiliar != 1:
    print("lo sentimos solo recibimos un caracter")
