# Se importan las bibliotecas necesarias
import random
import matplotlib.pyplot as plt
import numpy as np

# Se define la función que lance los dados
def lanzamiento(n):
    # Creamos la lista en la que se almacenarán los valores
    valores = []
    # Bucle en el que se realizará el lanzamiento de los dados n veces
    for i in range(n):
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        suma = dado1 + dado2
        valores.append(suma)
    # Se devuelve la lista con los valores
    return valores

# Se realiza el lanzamiento de los dados con una cantidad N de veces
n = int(input("Introduce la cantidad de lanzamientos: "))
resultado = lanzamiento(n)

# Se genera el histograma
plt.hist(resultado ,bins = 11, range = (2,12), density=True, color='b', ec="black", alpha=0.5, rwidth=2, align='left')

# Se añade el nombre eje x
plt.xlabel('Valores posibles')

# Se añade el nombre eje y
plt.ylabel('Probabilidad')

# Se añade el título
plt.title('Histograma del lanzamiento de dos dados regulares')

# Se muestra el histograma
plt.show()

# Se genera el histograma con la función esperada
x = np.arange(2,13)
y = 1/36 * np.ones(11)
plt.bar(x,y,width=0.5,color='r', ec="black",label='Función esperada',align='center')

# Se añade el nombre del eje x
plt.xlabel('Valores posibles')

# Se añade el nombre del eje y
plt.ylabel('Probabilidad')

# Se añade el  título
plt.title('Histograma del lanzamiento de dos dados regulares')

# Se muestra el histograma
plt.show()

'''
Conclusión: Cuando N es igual a 10 se puede decir que los resultados del experimento se ajustan al resultado esperado,
ya que a partir de esta cantidad de lanzamientos se consiguen unos resultados más cercanos a la función esperada.
'''