'''
ANALISIS: DETERMINAR LAS SOLUCIONES DE UNA ECUACION DE SEGUNDO GRADO
DATOS DE ENTRADA
a:coeficiente de la variable de grado 2.
b: coeficiente de la variable de primer grado
c: coeficiente de termino independiente

DATOS DE SALIDA
x1: representa la primera solucion en la formula cuadratica
x2: segunda solucion en la formula cuadratica
'''


a = input("escribe el coeficiente de la variable de segundo grado: ")
b = input("escribe el coeficiente de la variable de primer grado: ")
c = input("escribe el coeficiente de termino independiente: ")

while True:
    a = float(a)
    b = float(b)
    c = float(c)
    if a == 0:
        print("lo sentimos el coeficiente que acompaña la variable de segundo grado no puede ser cero. Verifica tu error")
        break
    discriminante = (b**2)-(4*a*c)
    if discriminante < 0:
        print("lo sentimos; la solucion no la tenemos en los numeros reales.")
        break
    else:
        x1 = ((-(b) + ((b**2) - (4 * a * c))**0.5) / (2 * a))
        x2 = ((-(b) - ((b**2) - (4 * a * c))**0.5) / (2 * a))
        if x1 < x2:
            print(x1)
            print(x2)
        else:
            print(x2)
            print(x1)
    break
