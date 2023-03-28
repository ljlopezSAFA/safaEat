from django.shortcuts import render
from .models import *
from .carga_datos import *

# Create your views here.
def cargar_pagina_inicio(request):
    return render(request, 'inicio.html')

def listar_restaurantes(request):
    list_restaurantes = Restaurante.objects.all()
    return render(request, 'listRestaurantes.html', {'restaurantes': list_restaurantes})


def buscar_restaurante(request):
    lugar = request.GET.get("busqueda")
    list_restaurante = Restaurante.objects.filter(ciudad=lugar)
    return render(request, 'listRestaurantes.html', {'restaurantes': list_restaurante})


def crear_restaurante(request):

    if request.method == "GET":
        return render(request, 'crear_restaurante.html', {'tipos_restaurante': TipoRestaurante.values})
    else:
        nuevo_restaurante = Restaurante()
        nuevo_restaurante.nombre = request.POST.get("nombre")
        nuevo_restaurante.ciudad = request.POST.get("ciudad")
        nuevo_restaurante.capacidad = int(request.POST.get("capacidad"))
        nuevo_restaurante.fecha_fundacion = request.POST.get("fecha_fundacion")
        nuevo_restaurante.tipo =TipoRestaurante.values[TipoRestaurante.values.index( request.POST.get("tipo_restaurante"))]
        Restaurante.save(nuevo_restaurante)
        return render(request, "inicio.html")

