
from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', cargar_pagina_inicio),
    path('restaurantes/', listar_restaurantes),
]