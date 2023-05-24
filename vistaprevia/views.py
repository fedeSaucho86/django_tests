from django.shortcuts import render
from django.http import HttpResponse

#def index(request):
#  return HttpResponse("Hola Mundo")

def index(request):
    params = {}
    params["nombre_sitio"] = "librosonline"
    return render(request, "vistaprevia/index.html", params)