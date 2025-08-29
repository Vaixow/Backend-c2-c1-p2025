from django.http import HttpResponse
from django.db import models

def inicio(request):
    nombre=('Vicente Alcaíno')
    return HttpResponse(f"Hola mundo desde Django, {nombre}.")
