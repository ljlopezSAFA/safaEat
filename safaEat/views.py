from django.shortcuts import render
from .models import *
from .carga_datos import *

# Create your views here.
def cargar_pagina_inicio(request):
    cargar_datos_pagina()
    return render(request, 'inicio.html')

def listar_restaurantes(request):
    list_restaurantes = Restaurante.objects.all()
    return render(request, 'listRestaurantes.html', {'restaurantes': list_restaurantes})