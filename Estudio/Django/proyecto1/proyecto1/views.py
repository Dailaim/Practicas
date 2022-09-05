from django.http import HttpResponse
import datetime
from django.template.loader import get_template
from django.shortcuts import render


def saludo(request):  # primera vista

    fecha_actual = datetime.datetime.now()
    fecha_actual = fecha_actual.strftime("%c")
    linstita = ["hola", "adios", "bona", "tagon"]

    nombre = "LEo"
    doc_externo = get_template('index.html')

    ctx = {"nombre_persona": nombre,
           "fecha_hola": fecha_actual, "lista1": linstita}

    documento = doc_externo.render(ctx)
    return HttpResponse(documento)


def damefecha(request):
    fecha_actual = datetime.datetime.now()
    fecha_actual = fecha_actual.strftime("%c")
    documento = """<html>
    <body>
    <h1>
    fecha actual %s
    <h1>
    <body>
    <html>""" % fecha_actual

    return HttpResponse(documento)


def calcularEdad(request, edad, agno):
    periodo = agno-2022
    edad_Futura = edad+periodo
    documento = """<html>
    <body>
    <h2>
    En el año %s tendras %s años
    <h2>
    <body>
    <html>""" % (agno, edad_Futura)
    return HttpResponse(documento)
