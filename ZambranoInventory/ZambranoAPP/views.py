from django.shortcuts import render, redirect
from django.contrib import messages
from .models import TblMsUsuario, TblMsRoles


def bienvenido(request):
    # Obtener el usuario de la sesión
    usuario = request.session.get('usuario')
    # Si no hay usuario en la sesión, redirigir al login
    if not usuario:
        return redirect('login')
    # Pasar los valores a la plantilla
    context = {
        'usuario': usuario,
    }
    # Renderizar la plantilla con los datos de contexto
    return render(request, "bienvenido.html", context)


def users_view(request):
    usuarios = TblMsUsuario.objects.all()

    # Obtener el usuario de la sesión
    usuario = request.session.get('usuario')
    # Si no hay usuario en la sesión, redirigir al login
    if not usuario:
        return redirect('login')
    # Pasar los valores a la plantilla
    #context = {
    #   'usuario': usuario,
    #}
    # Renderizar la plantilla con los datos de contexto
    return render(request, "usuarios_view.html", {'usuarios': usuarios})

def rols_view(request):
    roles = TblMsRoles.objects.all()
    return render(request, "roles_view.html", {'roles': roles} )



def login(request):
    usuario = None
    contrasena = None
    mensaje = None
    if request.method == "POST":
        usuario = request.POST['usuario']
        contrasena = request.POST['contraseña']

    # Buscar usuario y contraseña en la base de datos
    usuarios = TblMsUsuario.objects.filter(usuario=usuario, contrasena=contrasena)

    # Si se encontró un usuario con la contraseña proporcionada
    if usuarios.exists():
        # Guardar el usuario en la sesión
        request.session['usuario'] = usuario
        # Redirigir a la página de bienvenida
        return redirect('bienvenido')
    else:
        mensaje = "Porfavor ingrese un usuario valido"

    # Pasar los valores a la plantilla
    context = {
        'usuario': usuario,
        'contrasena': contrasena,
        'mensaje': mensaje,
    }

    # Renderizar la plantilla con los datos de contexto
    return render(request, "login.html", context)


def cerrar_sesion(request):
    # Verifica si la petición es un POST
    if request.method == 'POST':
         # Obtiene el usuario almacenado en la sesión
        usuario = request.session.get('usuario')
        # Si hay un usuario en la sesión
        if usuario is not None:
             # Crea un mensaje para mostrar al usuario
            messages.success(request, f'Has cerrado sesión, ¡hasta pronto {usuario}!')
             # Elimina todos los datos de la sesión
            request.session.flush()
            # Redirige al usuario a la página de inicio de sesión
            return redirect('login')
    # Si la petición no es un POST o no hay usuario en la sesión, redirige al usuario a la página de bienvenida    
    return redirect('bienvenido')


