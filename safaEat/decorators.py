from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render
from .models import *

def user_required(view_func):
    funcion_login_required = login_required(view_func)
    def wrapper(request,*args,**kwargs):
        if not request.user.is_active:
            return redirect('login')
        return funcion_login_required(request,*args, **kwargs)
    return wrapper


def comprobar_permiso_gestor(view_func):
    def wrapper(request,*args,**kwargs):
        if not request.user.rol == Roles.PROPIETARIO_RESTAURANTE:
            request.session['tiene_permiso'] = False
            return render(request,"")
        else:
            request.session['tiene_permiso'] = True
            return render(request, "")
    return wrapper