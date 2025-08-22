from django.http import HttpResponse

def inicio(request):
    nombre=('Vicente Alcaíno')
    return HttpResponse(f"Hola mundo desde Django, {nombre}.")