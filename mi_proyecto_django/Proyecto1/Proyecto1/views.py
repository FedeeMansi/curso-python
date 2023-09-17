from django.http import HttpResponse
from datetime import datetime


def saludo(request, nombre):
    return HttpResponse (f"Hola {nombre}! Muy buen dia!")

def dia_actual(request):
    dia = datetime.now()
    documento = f"Hoy es: {dia}"
    return HttpResponse(documento)
    
