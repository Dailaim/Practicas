Tiempo_de_uso = int(input("Tiempo de eso en minutos:"))

if Tiempo_de_uso > 1440:
    valor = Tiempo_de_uso - 100
    valor = (valor*57)+700
    valor+= 96000

elif Tiempo_de_uso > 100:

    valor = Tiempo_de_uso - 100
    valor = (valor*57)+700

else:
    valor = Tiempo_de_uso * 7
print(valor)