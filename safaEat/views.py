from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from .carga_datos import *
from .forms import  *
from django.contrib.auth.hashers import  make_password
from .decorators import  *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout,login,authenticate


# Create your views here.
@user_required
def cargar_pagina_inicio(request):
    return render(request, 'inicio.html')

def listar_restaurantes(request):
    list_restaurantes = Restaurante.objects.all()
    return render(request, 'restaurantes.html', {'restaurantes': list_restaurantes})


def buscar_restaurante(request):
    lugar = request.GET.get("busqueda")
    list_restaurante = Restaurante.objects.filter(ciudad=lugar)
    return render(request, 'restaurantes.html', {'restaurantes': list_restaurante})


@comprobar_permiso_gestor
def crear_restaurante(request):
    if request.session.get("tiene_permiso") == True:
        if request.method == "GET":
            return render(request, 'crear_restaurante.html', {'tipos_restaurante': TipoRestaurante.values})
        else:
            nuevo_restaurante = Restaurante()
            nuevo_restaurante.nombre = request.POST.get("nombre")
            nuevo_restaurante.url = request.POST.get("url")
            nuevo_restaurante.ciudad = request.POST.get("ciudad")
            nuevo_restaurante.capacidad = int(request.POST.get("capacidad"))
            nuevo_restaurante.fecha_fundacion = request.POST.get("fecha_fundacion")
            nuevo_restaurante.tipo =TipoRestaurante.values[TipoRestaurante.values.index( request.POST.get("tipo_restaurante"))]
            Restaurante.save(nuevo_restaurante)
            return render(request, "inicio.html")
    else:
        return render(request, "inicio.html")

def eliminar_restaurante(request,id):
     restaurante = Restaurante.objects.get(id=id)
     Restaurante.delete(restaurante)
     return redirect('/safaEat/restaurantes')


def registrar_usuario(request):
    form = FormularioRegistro()
    if request.method == "GET":
        return render(request,"registrar.html",{"form": form})
    #POST
    else:
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'inicio.html')
        else:
            return render(request, "registrar.html", {"form": form})


def logearse(request):
    form = AuthenticationForm()

    if request.method == "GET":
        return render(request, "login.html", {"form": form})
    elif request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)

        #Verificar que el formulario es valido
        if form.is_valid():
            #Intentar loguear
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],)

            #Si hemos encontrado el usuario
            if user is not None:
                #Nos logueamos
                login(request, user)
                return render(request, 'inicio.html')

        else:
            #pasar errores a la vista
            for error in list(form.errors.values()):
                messages.error(request, error)
            return render(request, "login.html", {"form": form})




