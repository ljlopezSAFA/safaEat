from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class FormularioRegistro(UserCreationForm):
    email = forms.EmailField(max_length=255, required=True,
                             help_text='Requerido. Ingrese una dirección de correo electrónico válida.')
    username = forms.CharField(max_length=255, required=True,
                               help_text='Requerido. 255 caracteres o menos. Solo letras, números y @/./+/-/_ caracteres.')
    password1 = forms.CharField(max_length=255, required=True,
                                help_text='Requerido. 255 caracteres o menos. Al menos 8 caracteres y no pueden ser todos números.')
    password2 = forms.CharField(max_length=255, required=True,
                                help_text='Requerido. Ingrese la misma contraseña que antes, para verificarla.')

    class Meta:
        model = Usuario
        fields = ('email', 'username', 'password1', 'password2')
