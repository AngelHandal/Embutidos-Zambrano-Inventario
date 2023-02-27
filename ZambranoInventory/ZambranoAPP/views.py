from django.shortcuts import render, redirect,get_object_or_404, redirect
from django.contrib import messages
from .models import TblMsUsuario, TblMsRoles, TblMsPreguntas,TblMsPreguntasUsuario
from django.utils import timezone
from django.http import Http404
from django.db import IntegrityError


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


def olvide_pass(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pregunta_id = request.POST.get('pregunta')
        respuesta = request.POST.get('respuesta')
        password = request.POST.get('password')

        try:
            user = TblMsUsuario.objects.get(usuario=username)
            pregunta_usuario = TblMsPreguntasUsuario.objects.get(
                id_usuario=user.id_usuario, id_pregunta_id=pregunta_id)

            if pregunta_usuario.respuesta == respuesta:
                if password:
                    user.contrasena = password
                    user.save()

                messages.success(request, 'Contraseña actualizada con éxito')
                return redirect('login')
            else:
                messages.error(request, 'La respuesta es incorrecta')
        except TblMsUsuario.DoesNotExist:
            messages.error(request, 'El usuario no existe')
        except TblMsPreguntasUsuario.DoesNotExist:
            messages.error(request, 'La pregunta seleccionada no es válida')

    preguntas = TblMsPreguntasUsuario.objects.all()
    context = {'preguntas': preguntas}
    return render(request, 'olvide_pass.html', context)


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

def guardar_rol_editado(request, id):
    rol = get_object_or_404(TblMsRoles, id_rol=id)
    if request.method == 'POST':
        rol.rol = request.POST['rol']
        rol.descripcion = request.POST['descripcion']
        rol.modificado_por = request.user.username
        rol.fecha_modificacion = timezone.now()
        rol.save()
        return redirect('rols_views')
    else:
        return render(request, 'editar_rol.html', {'rol': rol})

def crear_rol(request):
    if request.method == 'POST':
        # obtener los datos del formulario
        rol = request.POST.get('rol')
        descripcion = request.POST.get('descripcion')
        #creado_por = request.user.username
        fecha_creacion = timezone.now()
        #modificado_por = request.user.username
        fecha_modificacion = timezone.now()

        # obtener el último valor de id_rol y aumentar en 1 para asignar el nuevo id
        ultimo_rol = TblMsRoles.objects.order_by('-id_rol').first()
        nuevo_id = ultimo_rol.id_rol + 1 if ultimo_rol else 1

        # crear un objeto TblMsRoles con los datos del formulario
        nuevo_rol = TblMsRoles(
            id_rol=nuevo_id,
            rol=rol,
            descripcion=descripcion,
            creado_por=request.session.get('usuario'),
            fecha_creacion=fecha_creacion,
            modificado_por=request.session.get('usuario'),
            fecha_modificacion=fecha_modificacion
        )

        # guardar el nuevo objeto en la base de datos
        nuevo_rol.save()

        # redirigir a la página de detalles del nuevo rol creado
        return redirect('rols_views')
    else:
        return render(request, 'crear_rol.html')



def eliminar_rol(request, id):
    try:
        rol = TblMsRoles.objects.get(id_rol=id)
        rol.delete()
        return redirect('rols_views')
    except IntegrityError:
        error_msg = 'Por favor, elimina los usuarios asignados a este rol primero'
        return render(request, 'errores_rol.html', {'error_msg': error_msg})
    except TblMsRoles.DoesNotExist:
        raise Http404('Rol no existente')

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


def crear_usuario(request):
    roles = TblMsRoles.objects.all()
    preguntas = TblMsPreguntas.objects.all()

    if request.method == "POST":
        rol_id = request.POST.get("rol")
        rol = TblMsRoles.objects.get(pk=rol_id)
        ultimo_id = TblMsUsuario.objects.order_by("-id_usuario").first().id_usuario
        nuevo_id = ultimo_id + 1
        usuario = TblMsUsuario(
            id_usuario=nuevo_id,
            usuario=request.POST.get("usuario"),
            nombre_usuario=request.POST.get("nombre_usuario"),
            estado_usuario=request.POST.get("estado_usuario"),
            contrasena=request.POST.get("contrasena"),
            correo_electronico=request.POST.get("correo_electronico"),
            id_rol=rol,
            preguntas_contestadas=1,  # inicializamos la cantidad de preguntas contestadas a 0
            creado_por=request.session.get('usuario'), # utilizamos el usuario autenticado como creador y modificador
            modificado_por=request.session.get('usuario'),
            fecha_ultima_conexion=timezone.now(),
            primer_ingreso=True,
            fecha_vencimiento=request.POST.get("fecha_vencimiento"),
            fecha_creacion=timezone.now(),
            fecha_modificacion=timezone.now(),
        )
        usuario.save()

        # obtenemos las respuestas de las preguntas y las guardamos
        preguntas_usuario = []
        
        """
        nuevo_id_Pregunta_usuario = TblMsPreguntasUsuario.objects.order_by("-id_pregunta_usuario").first()
        if nuevo_id_Pregunta_usuario is not None:
            nuevo_id_Pregunta_usuario = nuevo_id_Pregunta_usuario.id_pregunta_usuario + 1
        else:
            nuevo_id_Pregunta_usuario = 1
        """
        for pregunta in preguntas:
            respuesta = request.POST.get(f"pregunta_{pregunta.id_pregunta}")
            pregunta_usuario = TblMsPreguntasUsuario(
                #id_pregunta_usuario=nuevo_id_Pregunta_usuario,
                id_pregunta=pregunta,
                id_usuario=usuario,
                respuesta=request.POST.get("respuesta"),
                creado_por=request.POST.get("nombre_usuario"),
                modificado_por=request.POST.get("nombre_usuario"),
                fecha_creacion=timezone.now(),
                fecha_modificacion=timezone.now(),
            )
            preguntas_usuario.append(pregunta_usuario)

        TblMsPreguntasUsuario.objects.bulk_create(preguntas_usuario)

        messages.success(request, "Usuario creado con éxito.")
        return redirect("bienvenido")
    return render(request, "crear_usuario.html", {"roles": roles, "preguntas": preguntas})