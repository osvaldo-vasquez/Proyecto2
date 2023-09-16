from django.http import HttpResponse
from datetime import datetime as dt
from django.template import Template, Context

def probando_template(request):

    # Abrimos el archivo html
    mi_html = open('./templates/hola.html')

    # Creamos el template haciendo uso de la clase Template
    plantilla = Template(mi_html.read())

    # Cerramos el archivo previamente abierto, ya que lo tenemos cargado en la variable plantilla
    mi_html.close()

    # Creamos un contexto, más adelante vamos a aprender a usarlo, ahora lo necesitamos aunque sea vacío para que funcione
    mi_contexto = Context()

    # Terminamos de construír el template renderizándolo con su contexto
    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendimos esto, es muy simple :)")

def diaDeHoy(request):
    dia = dt.now()

    documentoDeTexto = f"Hoy es día: <br> {dia}"

    return HttpResponse(documentoDeTexto)

def saludoPersonal(request, nombre):
    hoy = dt.now()
    return HttpResponse(f"Hola {nombre}, hoy es: {hoy}")
