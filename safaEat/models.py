import enum
from django.db import models

class TipoRestaurante(models.TextChoices):
    AMERICANO = "Americano"
    TURCA = "Turca"
    ITALIANO = "Italiano"
    ORIENTAL = "Oriental"

    def mostrar(self):
        return self.value


# Create your models here.
class Restaurante(models.Model):
    nombre = models.CharField(max_length=150)
    url = models.CharField(max_length=500, default="")
    ciudad = models.CharField(max_length=50)
    tipo = models.CharField(max_length=60, choices=TipoRestaurante.choices)
    capacidad = models.IntegerField()
    fecha_fundacion= models.DateField()

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    precio = models.FloatField()
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + "->" +  str(self.precio)