
from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', cargar_pagina_inicio),
    path('restaurantes/', listar_restaurantes),
    path('buscar/', buscar_restaurante),
    path('restaurantes/crear', crear_restaurante),
    path('restaurantes/eliminar/<int:id>', eliminar_restaurante),
    path('login/', logearse, name= "login"),
    path('logout/', buscar_restaurante , name= "logout"),
    path('register/', registrar_usuario, name= "register"),
]