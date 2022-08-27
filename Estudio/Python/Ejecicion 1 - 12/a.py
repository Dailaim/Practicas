'''

Enunciado
Dado el valor da los lados de un triángulos isóceles, haga un algoritmo su perimetro, su altura y su área.

VARIABLES DE ENTRADA
a=valor del lado del triangulo que se repite
b=valor del lado del triangulo que difiere a los demas

VARIABLES DE SALIDA
altura:altura del triangulo
area:area del triangulo
perimetro:perimetro del triangulo

VARIBLES AUXILIARES
N/A
'''


print("Calcularemos el perimetro, altrura y area de un triangulo ispceles")
a = input("escribe el lado de triangulo isoceles que se repite: ")
b = input("escribe el lado de triangulo que difiere a los demas: ")

while True:
    a = float(a)
    b = float(b)
    if a < 0:
        print("lo sentimos la medida del triangulo isoceles que se repiye no puede ser negativa. Verifica tu error ")
        break
    if b < 0:
        print("lo sentimos la medida del triangulo no puede ser negativa")
        break
    altura = ((a**2) - (b**2)/4)**0.5
    area = altura * (b/2)
    perimetro = (2*a) + b

    print(perimetro)
    print(altura)
    print(area)
    break
