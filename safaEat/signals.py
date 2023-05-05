from django.db.models.signals import post_migrate
from django.dispatch import receiver

from .task import *


@receiver(post_migrate)
def on_post_migrate(sender, **kwargs):

    # Agrega la tarea de fondo
    @background(schedule=0) # Configura la tarea para que se ejecute inmediatamente
    def run_my_task():
        tarea()

    run_my_task(repeat=0) #Agrega la tarea para que se ejecute solo una vez al arrancar la aplicación
