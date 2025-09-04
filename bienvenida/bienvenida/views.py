from django.http import HttpResponse
from django.db import models
from django.shortcuts import render
from .models import Producto

def inicio(request):
    nombre=('Vicente Alcaíno')
    return HttpResponse(f"Hola mundo desde Django, {nombre}.")


def lista_productos(request):
 productos = Producto.objects.all()
 return render(request, 'productos/lista.html', {'productos': productos})
