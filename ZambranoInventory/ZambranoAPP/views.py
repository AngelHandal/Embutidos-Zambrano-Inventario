from django.shortcuts import render, redirect,get_object_or_404, redirect
from django.contrib import messages
from .models import TblMsUsuario, TblMsRoles, TblMsPreguntas,TblMsPreguntasUsuario,TblMsBitacora,TblMsObjetos, TblCliente, TblClienteTipo
from django.utils import timezone
from django.http import Http404,JsonResponse
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime




def bienvenido(request):
    # Obtener el usuario de la sesión
    usuario = request.session.get('usuario')
    
    # Si no hay usuario en la sesión, redirigir al login
    if not usuario:
        return redirect('login')
    


    return render(request, 'bienvenido.html', {'usuario': usuario})

def actualizar_contrasena_por_preguntas(request):
    # obtenemos el usuario que nos interesa
    usuario = request.session.get('usuario')
    usuario_obj = TblMsUsuario.objects.get(usuario=usuario)
    # obtenemos el id de mi usuario
    id_usuario = usuario_obj.id_usuario

    if request.method == 'POST':
        nueva_contra = request.POST.get('nuevacontra')
        usuario_obj.contrasena = nueva_contra
        usuario_obj.save()
        return redirect('login')

    return render(request, "actualizar_por_pregunta.html", {"usuario": usuario, "id_usuario": id_usuario})


def preguntas_seguridad_recuperar(request):
    usuario = request.session.get('usuario')
    usuario_obj = TblMsUsuario.objects.get(usuario=usuario)
    id_usuario = usuario_obj.id_usuario
    #accedemos a las respuestas de mi usuario
    #preguntas_usuario = TblMsPreguntasUsuario.objects.filter(id_usuario=id_usuario)
    preguntas_usuario = TblMsPreguntasUsuario.objects.filter(id_usuario=id_usuario).values('respuesta')

    context = {'preguntas_usuario': preguntas_usuario}
    #obtenemos todas las preguntas
    preguntas = TblMsPreguntas.objects.all()
    return render(request, 'responde_pregunta.html', {"preguntas": preguntas, "usuario": usuario, "id_usuario": id_usuario, **context})


def olvide_pass(request):
    usuario = None
    mensaje = None
    if request.method == "POST":
        usuario = request.POST['usuario']
        # Buscar usuario y contraseña en la base de datos
    usuarios = TblMsUsuario.objects.filter(usuario=usuario)

    # Si se encontró un usuario con la contraseña proporcionada
    if usuarios.exists():
        # Guardar el usuario en la sesión
        request.session['usuario'] = usuario
        # Redirigir a la página donde se mostraran las preguntas de seguridad
        return redirect('responde_pregunta')
    else:
        mensaje = "Por favor ingrese un usuario valido"
       
    return render(request, 'olvide_pass.html')


def users_view(request):
    # Obtener el usuario de la sesión
    usuario = request.session.get('usuario')
    # Si no hay usuario en la sesión, redirigir al login
    if not usuario:
        return redirect('login')
    
    usuarios = TblMsUsuario.objects.all()

    # Obtener el objeto del usuario a partir del nombre de usuario en la sesión
    usuario_obj = TblMsUsuario.objects.get(usuario=usuario)
    # Validar si existen datos en la tabla
    if TblMsBitacora.objects.count() == 0:
        nuevo_id_bitacora = 1
    else:
        # Obtener el último ID de la bitácora
        ultimo_id_bitacora = TblMsBitacora.objects.order_by("-id_bitacora").first().id_bitacora
        nuevo_id_bitacora = ultimo_id_bitacora + 1

    # Obtener la instancia del objeto asociado
    objeto = TblMsObjetos.objects.get(pk=1)
    # Crear un registro en la tabla de bitácora
    TblMsBitacora.objects.create(
        id_bitacora=nuevo_id_bitacora,
        id_usuario=usuario_obj,  # Usar la instancia del objeto del usuario
        id_objeto=objeto,  # Puedes cambiar el ID del objeto según corresponda
        fecha=datetime.now(),
        accion='Usuarios',
        descripcion='El usuario {} ha accedido a la pantalla lista de usuarios'.format(usuario),
        creado_por=usuario,
        fecha_creacion=datetime.now(),
        modificado_por=usuario,
        fecha_modificacion=datetime.now()
    )

    # Pasar los valores a la plantilla
    #context = {
    #   'usuario': usuario,
    #}
    # Renderizar la plantilla con los datos de contexto
    return render(request, "usuarios_view.html", {'usuarios': usuarios, 'usuario': usuario})


def rols_view(request):
    # Obtener el usuario de la sesión
    usuario = request.session.get('usuario')
    # Si no hay usuario en la sesión, redirigir al login
    if not usuario:
        return redirect('login')
    roles = TblMsRoles.objects.all()
        # Obtener el objeto del usuario a partir del nombre de usuario en la sesión
    usuario_obj = TblMsUsuario.objects.get(usuario=usuario)
    # Obtener el último ID de la bitácora
    ultimo_id_bitacora = TblMsBitacora.objects.order_by("-id_bitacora").first().id_bitacora
    nuevo_id_bitacora = ultimo_id_bitacora + 1

    # Obtener la instancia del objeto asociado
    objeto = TblMsObjetos.objects.get(pk=1)
    # Crear un registro en la tabla de bitácora
    TblMsBitacora.objects.create(
        id_bitacora=nuevo_id_bitacora,
        id_usuario=usuario_obj,  # Usar la instancia del objeto del usuario
        id_objeto=objeto,  # Puedes cambiar el ID del objeto según corresponda
        fecha=datetime.now(),
        accion='Roles',
        descripcion='El usuario {} ha accedido a la pantalla lista de roles'.format(usuario),
        creado_por=usuario,
        fecha_creacion=datetime.now(),
        modificado_por=usuario,
        fecha_modificacion=datetime.now()
    )

    return render(request, "roles_view.html", {'roles': roles, 'usuario': usuario} )


def guardar_rol_editado(request, id):
    # Obtener el usuario de la sesión
    usuario = request.session.get('usuario')
    # Si no hay usuario en la sesión, redirigir al login
    if not usuario:
        return redirect('login')
    rol = get_object_or_404(TblMsRoles, id_rol=id)
    if request.method == 'POST':
        rol.rol = request.POST['rol']
        rol.estado = request.POST['estado']
        rol.descripcion = request.POST['descripcion']
        rol.modificado_por = usuario
        rol.fecha_modificacion = timezone.now()
        rol.save()
        return redirect('rols_views')
    else:
        return render(request, 'editar_rol.html', {'rol': rol, 'usuario': usuario})


def crear_rol(request):
    # Obtener el usuario de la sesión
    usuario = request.session.get('usuario')
    # Si no hay usuario en la sesión, redirigir al login
    if not usuario:
        return redirect('login')
    
    if request.method == 'POST':
        # obtener los datos del formulario
        rol = request.POST.get('rol')
        estado = request.POST.get('estado')
        descripcion = request.POST.get('descripcion')
        #creado_por = request.user.username
        fecha_creacion = timezone.now()
        #modificado_por = request.user.username
        fecha_modificacion = timezone.now()

        # obtener el último valor de id_rol y aumentar en 1 para asignar el nuevo id
        ultimo_rol = TblMsRoles.objects.order_by('-id_rol').first()
        nuevo_id = ultimo_rol.id_rol + 1 if ultimo_rol else 1

        # Validar si existen datos en la tabla
        if TblMsBitacora.objects.count() == 0:
            nuevo_id_bitacora = 1
        else:
            # Obtener el último ID de la bitácora
            ultimo_id_bitacora = TblMsBitacora.objects.order_by("-id_bitacora").first().id_bitacora
            nuevo_id_bitacora = ultimo_id_bitacora + 1

        # crear un objeto TblMsRoles con los datos del formulario
        nuevo_rol = TblMsRoles(
            id_rol=nuevo_id,
            rol=rol,
            estado = estado,
            descripcion=descripcion,
            creado_por=request.session.get('usuario'),
            fecha_creacion=fecha_creacion,
            modificado_por=request.session.get('usuario'),
            fecha_modificacion=fecha_modificacion
        )

        # guardar el nuevo objeto en la base de datos
        nuevo_rol.save()

                # Obtener el objeto del usuario a partir del nombre de usuario en la sesión
        usuario_obj = TblMsUsuario.objects.get(usuario=usuario)
        # Obtener el último ID de la bitácora
        ultimo_id_bitacora = TblMsBitacora.objects.order_by("-id_bitacora").first().id_bitacora
        nuevo_id_bitacora = ultimo_id_bitacora + 1

        # Obtener la instancia del objeto asociado
        objeto = TblMsObjetos.objects.get(pk=1)
        # Crear un registro en la tabla de bitácora
        TblMsBitacora.objects.create(
            id_bitacora=nuevo_id_bitacora,
            id_usuario=usuario_obj,  # Usar la instancia del objeto del usuario
            id_objeto=objeto,  # Puedes cambiar el ID del objeto según corresponda
            fecha=datetime.now(),
            accion='Roles',
            descripcion='El usuario {} ha creado un nuevo Rol'.format(usuario),
            creado_por=usuario,
            fecha_creacion=datetime.now(),
            modificado_por=usuario,
            fecha_modificacion=datetime.now()
        )

        # redirigir a la página de detalles del nuevo rol creado
        return redirect('rols_views')
    else:
        return render(request, 'crear_rol.html', {'usuario': usuario})



def eliminar_rol(request, id):
    # Obtener el usuario de la sesión
    usuario = request.session.get('usuario')
    # Si no hay usuario en la sesión, redirigir al login
    if not usuario:
        return redirect('login')
    try:
        rol = TblMsRoles.objects.get(id_rol=id)
        #rol.delete() No eliminaremos ningun rol
        rol.estado = 'Inactivo'
        rol.save()
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
    id_usuario = None  # agregar variable para id_usuario

    if request.method == "POST":
        usuario = request.POST['usuario']
        contrasena = request.POST['contraseña']

    # Buscar usuario y contraseña en la base de datos
    usuarios = TblMsUsuario.objects.filter(usuario=usuario, contrasena=contrasena)
   
    # Si se encontró un usuario con la contraseña proporcionada
    if usuarios.exists():
        # Guardar el usuario en la sesión
        request.session['usuario'] = usuario
        request.session['id_usuario'] = id_usuario

        # Obtener el objeto del usuario a partir del nombre de usuario en la sesión
        usuario_obj = TblMsUsuario.objects.get(usuario=usuario)
        
            # Validar si existen datos en la tabla
        if TblMsBitacora.objects.count() == 0:
            nuevo_id_bitacora = 1
        else:
            # Obtener el último ID de la bitácora
            ultimo_id_bitacora = TblMsBitacora.objects.order_by("-id_bitacora").first().id_bitacora
            nuevo_id_bitacora = ultimo_id_bitacora + 1

        # Obtener la instancia del objeto asociado
        objeto = TblMsObjetos.objects.get(pk=1)

        # Crear un registro en la tabla de bitácora
        TblMsBitacora.objects.create(
            id_bitacora=nuevo_id_bitacora,
            id_usuario=usuario_obj,  # Usar la instancia del objeto del usuario
            id_objeto=objeto,  # Puedes cambiar el ID del objeto según corresponda
            fecha=datetime.now(),
            accion='Login',
            descripcion='El usuario {} ha accedido al sistema'.format(usuario),
            creado_por=usuario,
            fecha_creacion=datetime.now(),
            modificado_por=usuario,
            fecha_modificacion=datetime.now()
        )

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
        # Obtener el usuario de la sesión
    usuario = request.session.get('usuario')
    # Si no hay usuario en la sesión, redirigir al login
    if not usuario:
        return redirect('login')
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

        # Obtener el objeto del usuario a partir del nombre de usuario en la sesión
        usuario_obj = TblMsUsuario.objects.get(usuario=usuario)
        # Validar si existen datos en la tabla
        if TblMsBitacora.objects.count() == 0:
            nuevo_id_bitacora = 1
        else:
            # Obtener el último ID de la bitácora
            ultimo_id_bitacora = TblMsBitacora.objects.order_by("-id_bitacora").first().id_bitacora
            nuevo_id_bitacora = ultimo_id_bitacora + 1

        # Obtener la instancia del objeto asociado
        objeto = TblMsObjetos.objects.get(pk=1)
        # Crear un registro en la tabla de bitácora
        TblMsBitacora.objects.create(
            id_bitacora=nuevo_id_bitacora,
            id_usuario=usuario_obj,  # Usar la instancia del objeto del usuario
            id_objeto=objeto,  # Puedes cambiar el ID del objeto según corresponda
            fecha=datetime.now(),
            accion='Usuarios',
            descripcion='El usuario {} ha creado un nuevo usuario'.format(usuario),
            creado_por=usuario,
            fecha_creacion=datetime.now(),
            modificado_por=usuario,
            fecha_modificacion=datetime.now()
        )

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
    return render(request, "crear_usuario.html", {"roles": roles, "preguntas": preguntas, 'usuario': usuario})


def ver_mas_usuario(request,id):
    # Obtener el usuario de la sesión
    usuario = request.session.get('usuario')
    # Si no hay usuario en la sesión, redirigir al login
    if not usuario:
        return redirect('login')
    
        # Obtener el objeto usuario desde la variable
    # en la sesión
    usuario = get_object_or_404(TblMsUsuario, id_usuario=id)
    

    return render(request, "ver_mas_usuario.html", {'usuario': usuario})





def editar_usuario(request, id):
    # Obtener el usuario de la sesión
    usuario = request.session.get('usuario')
    # Si no hay usuario en la sesión, redirigir al login
    if not usuario:
        return redirect('login')
    
    # Obtener el objeto usuario desde la variable
    # en la sesión
    usuario = get_object_or_404(TblMsUsuario, id_usuario=id)

    if request.method == 'POST':
        # Actualizar los datos del usuario en la base de datos
        usuario.usuario = request.POST.get('usuario')
        usuario.nombre_usuario = request.POST.get('nombre_usuario')
        usuario.estado_usuario = request.POST.get('estado_usuario')
        usuario.contrasena = request.POST.get('contrasena')
        usuario.fecha_ultima_conexion = timezone.now()
        usuario.primer_ingreso = 1
        usuario.fecha_vencimiento = request.POST.get('fecha_vencimiento')
        usuario.correo_electronico = request.POST.get('correo_electronico')
        usuario.creado_por = request.POST.get('creado_por')
        usuario.fecha_creacion = timezone.now()
        usuario.modificado_por = usuario
        usuario.fecha_modificacion = timezone.now()
        usuario.preguntas_contestadas = 1
        usuario.save()
        # Redirigir a la página de la lista de usuarios
        return redirect('bienvenido')

    return render(request, 'editar_usuario.html', {'usuario': usuario})

def eliminar_usuario(request, id):
    # Obtener el usuario de la sesión
    usuario = request.session.get('usuario')
    # Si no hay usuario en la sesión, redirigir al login
    if not usuario:
        return redirect('login')
    try:
        usuario = TblMsUsuario.objects.get(pk=id)
        usuario.estado_usuario = 'Inactivo'
        usuario.save()
        messages.success(request, 'Usuario eliminado exitosamente')
    except usuario.DoesNotExist:
        messages.error(request, 'El usuario que intentas eliminar no existe')
    return HttpResponseRedirect(reverse('user_views'))


def preguntas(request):
    # Obtener el usuario de la sesión
    usuario = request.session.get('usuario')
    # Si no hay usuario en la sesión, redirigir al login
    if not usuario:
        return redirect('login')
    preguntas = TblMsPreguntas.objects.all()
    # Obtener el objeto del usuario a partir del nombre de usuario en la sesión
    usuario_obj = TblMsUsuario.objects.get(usuario=usuario)
    # Validar si existen datos en la tabla
    if TblMsBitacora.objects.count() == 0:
        nuevo_id_bitacora = 1
    else:
        # Obtener el último ID de la bitácora
        ultimo_id_bitacora = TblMsBitacora.objects.order_by("-id_bitacora").first().id_bitacora
        nuevo_id_bitacora = ultimo_id_bitacora + 1

    # Obtener la instancia del objeto asociado
    objeto = TblMsObjetos.objects.get(pk=1)
    # Crear un registro en la tabla de bitácora
    TblMsBitacora.objects.create(
        id_bitacora=nuevo_id_bitacora,
        id_usuario=usuario_obj,  # Usar la instancia del objeto del usuario
        id_objeto=objeto,  # Puedes cambiar el ID del objeto según corresponda
        fecha=datetime.now(),
        accion='Preguntas',
        descripcion='El usuario {} ha accedido a la pantalla lista de Preguntas'.format(usuario),
        creado_por=usuario,
        fecha_creacion=datetime.now(),
        modificado_por=usuario,
        fecha_modificacion=datetime.now()
    )
    return render(request, 'preguntas_view.html', {'preguntas': preguntas, 'usuario': usuario})

def crear_pregunta(request):
    # Obtener el usuario de la sesión
    usuario = request.session.get('usuario')
    # Si no hay usuario en la sesión, redirigir al login
    if not usuario:
        return redirect('login')
    if request.method == 'POST':
        # Procesar los datos del formulario de creación de pregunta
        pregunta = request.POST.get('pregunta')
        estado = request.POST.get('estado')
        creado_por = usuario
        ultimo_id = TblMsPreguntas.objects.order_by("-id_pregunta").first().id_pregunta
        nueva_id = ultimo_id + 1
        nueva_pregunta = TblMsPreguntas(id_pregunta=nueva_id,pregunta=pregunta,estado=estado, creado_por=usuario, fecha_creacion=timezone.now(), modificado_por = usuario, fecha_modificacion= timezone.now() )
        nueva_pregunta.save()

        # Obtener el objeto del usuario a partir del nombre de usuario en la sesión
        usuario_obj = TblMsUsuario.objects.get(usuario=usuario)
        # Validar si existen datos en la tabla
        if TblMsBitacora.objects.count() == 0:
            nuevo_id_bitacora = 1
        else:
            # Obtener el último ID de la bitácora
            ultimo_id_bitacora = TblMsBitacora.objects.order_by("-id_bitacora").first().id_bitacora
            nuevo_id_bitacora = ultimo_id_bitacora + 1

        # Obtener la instancia del objeto asociado
        objeto = TblMsObjetos.objects.get(pk=1)
        # Crear un registro en la tabla de bitácora
        TblMsBitacora.objects.create(
            id_bitacora=nuevo_id_bitacora,
            id_usuario=usuario_obj,  # Usar la instancia del objeto del usuario
            id_objeto=objeto,  # Puedes cambiar el ID del objeto según corresponda
            fecha=datetime.now(),
            accion='Roles',
            descripcion='El usuario {} ha accedido a la pantalla lista de roles'.format(usuario),
            creado_por=usuario,
            fecha_creacion=datetime.now(),
            modificado_por=usuario,
            fecha_modificacion=datetime.now()
        )
        # Redirigir a la página de preguntas
        return redirect('preguntas')
    else:
        # Mostrar el formulario de creación de pregunta
        return render(request, 'crear_pregunta.html', {'usuario': usuario})

def editar_pregunta(request, id_pregunta):
     # Obtener el usuario de la sesión
    usuario = request.session.get('usuario')
    # Si no hay usuario en la sesión, redirigir al login
    if not usuario:
        return redirect('login')
    pregunta = TblMsPreguntas.objects.get(id_pregunta=id_pregunta)
    if request.method == 'POST':
        # procesar datos del formulario
        pregunta.pregunta = request.POST['pregunta']
        pregunta.estado = request.POST['estado']
        pregunta.modificado_por = usuario
        pregunta.fecha_modificacion = timezone.now()
        pregunta.save()
        return redirect('preguntas')
    else:
        # mostrar formulario para editar
        return render(request, 'editar_pregunta.html', {'pregunta': pregunta, 'usuario': usuario})


def eliminar_pregunta(request, id):
    # Obtener el usuario de la sesión
    usuario = request.session.get('usuario')
    # Si no hay usuario en la sesión, redirigir al login
    if not usuario:
        return redirect('login')
    
    #pregunta = get_object_or_404(TblMsPreguntas, id_pregunta=id)
    pregunta = TblMsPreguntas.objects.get(id_pregunta=id)
    #pregunta.delete()
    pregunta.estado = 'Inactivo'
    pregunta.save()

    return redirect('preguntas')


def ver_bitacora(request):
    # Obtener el usuario de la sesión
    usuario = request.session.get('usuario')
    # Si no hay usuario en la sesión, redirigir al login
    if not usuario:
        return redirect('login')
    
    movimientos = TblMsBitacora.objects.all()

    return render(request, "bitacora.html", {'movimientos':movimientos, 'usuario': usuario})


def eliminar_bitacora(request):
    #elimina todo mi historial
    TblMsBitacora.objects.all().delete()
    return redirect('bienvenido')

