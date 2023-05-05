from background_task import background
from .models import *
from django.db import transaction
import subprocess


@background(schedule=1)
@transaction.atomic
def tarea():
    nuevo_restaurante = Restaurante()
    nuevo_restaurante.nombre = "Ejemplo"
    nuevo_restaurante.url = "Ejemplo"
    nuevo_restaurante.ciudad =  "Ejemplo"
    nuevo_restaurante.capacidad =  100
    nuevo_restaurante.fecha_fundacion = "2023-03-30"
    nuevo_restaurante.tipo = TipoRestaurante.AMERICANO
    nuevo_restaurante.save()
    subprocess.run(['python', 'manage.py', 'process_tasks'])


