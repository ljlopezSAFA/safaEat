from datetime import date
from safaEat.models import *

def cargar_datos_pagina():

    new_restaurant = Restaurante()
    new_restaurant.nombre = "TGB"
    new_restaurant.ciudad = "Sevilla"
    new_restaurant.capacidad = 100
    new_restaurant.tipo = TipoRestaurante.AMERICANO.value
    new_restaurant.fecha_fundacion = date.fromisoformat('2019-12-04')

    Restaurante.save(new_restaurant)
