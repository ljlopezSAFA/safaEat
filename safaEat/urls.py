
from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', cargar_pagina_inicio),
    path('restaurantes/', listar_restaurantes, name="restaurantes"),
    path('buscar/', buscar_restaurante),
    path('restaurantes/crear', crear_restaurante, name="crear_restaurante"),
    path('restaurantes/eliminar/<int:id>', eliminar_restaurante),
    path('restaurantes/productos/<int:id>',ver_productos),
    path('restaurantes/productos/crear/<int:id>',crear_producto),
    path('restaurantes/productos/comprar/<int:id>',comprar_producto),
    path('login/', logearse, name= "login"),
    path('logout/', desloguearse , name= "logout"),
    path('register/', registrar_usuario, name= "register"),
    path('carrito/', ver_carrito, name="ver_carrito"),
    path('reservas/', ver_mis_reservas, name="reservas"),
    path('reservas/crear/', crear_reserva, name="crear_reserva"),
    path('reservas/eliminar/<int:id>', eliminar_reserva, name="eliminar_reserva"),
    path('reservas/editar/<int:id>', editar_reserva, name="editar_reserva"),
]