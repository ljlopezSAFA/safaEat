from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class Roles(models.TextChoices):
    ADMIN = "Admin"
    PROPIETARIO_RESTAURANTE = "Propietario"
    CLIENTE = "Cliente"

    def mostrar(self):
        return self.value

class UsuarioManager(BaseUserManager):
    def create_user(self,email, password, **extra_fields):
        if not email:
            raise ValueError("El usuario debe tener un email válido")
        user = self.model(email=self.normalize_email(email),**extra_fields )
        user.set_password(password)
        user.save(using = self.db)
        return user

    def create_superuser(self,email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault("is_susperuser", True)
        return self.create_user(email,password,**extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=255, blank=False)
    rol = models.CharField(max_length=60, choices=Roles.choices, default= Roles.CLIENTE)
    password = models.CharField(max_length=255, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD= 'username'
    REQUIRED_FIELDS = ['username,email,password']

    objects = UsuarioManager()

    def __str__(self):
        return self.username, self.email


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
    url = models.CharField(max_length=500, default="")
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + "->" +  str(self.precio)


class Reserva(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete= models.CASCADE)
    restaurante = models.ForeignKey(Restaurante, on_delete= models.CASCADE)
    fecha_reserva = models.DateTimeField()
    num_personas = models.IntegerField()

    def __str__(self):
        return self.usuario.username + self.restaurante.nombre + str(self.fecha_reserva)


