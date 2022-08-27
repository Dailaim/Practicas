'''

ANALISIS: DETERMIANR EL COSTO DE SERVICIO DE VIDEOJUEGOS MEDIANTE EL TIEMPO DE INICIO Y FIN DEL MISMO.

VARIBALES DE ENTRADA
tiempo: tiempo de inicio del serivicio y posteriormente tiempo de fin del servicio.

VARIABLES DE SALIDA
costo:costo total del servicio

VAIRBALES AUXILIARES
horas: representa el tiempo en horas que el usuario digito que seran convertidos a segundos, si se da este caso.
minutos: representa el tiempo en minutos que el usuario digito que sera convertidos a segundos, si se da este caso
segundos: representa el tiempo en segundos que el usuario digito, si se da este caso
total_total: representa la suma completa de segundos entre horas,minutos y segundos
TC: tiempo de inicio en segundos
TF: tiempo de fin en segundos'''


import math
tiempo = input("ingresa porfavor el tiempo de comienzo: ")


while True:
    horas = 0
    minutos = 0
    segundos = 0
    tiempo = float(tiempo)

    if tiempo % 2 != 0 and tiempo % 2 != 1:
        print("error no aceptamos numeros decimales, verifica tu error, gracias")
        break
    if tiempo < 0:
        print("lo sentimos el programa no acepta numeros negativos. Verifica tu error, gracias")
        break
    if tiempo >= 10000:
        horas = tiempo//10000
        tiempo = tiempo-(horas*10000)
        horas = horas*60*60
        if horas > 86400:
            print("error verifica la cantidad de horas en los tiempos ingresas;Gracias")
            break
    if tiempo >= 100:
        minutos = tiempo//100
        tiempo = tiempo - (minutos*100)
        minutos = minutos*60
        if minutos > 3600:
            print(
                "error verifica la cantidad de minutos ingresasdos en los tiempos digitados; gracias")
            break
    if tiempo >= 0:
        segundos = tiempo
        if segundos > 60:
            print("verifica la cantidad de segundos en los tiempos ingresdos; Gracias")
            break
    tiempo_total = horas+minutos+segundos
    if vueltas == 0:
        TC = tiempo_total
        tiempo = input("ingresa tiempo de fin: ")
    vueltas = vueltas+1
    if vueltas == 2:
        TF = tiempo_total
        costo = (TF-TC)*2
        costo = math.ceil(costo)
        if costo < 0:
            costo = -(costo)
        print(costo)
        break
