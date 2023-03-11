from django.urls import path
from . import views


urlpatterns = [
    path("", views.login, name='login'),
    path('bienvenido/', views.bienvenido, name='bienvenido'),
    path('olvide_pass/', views.olvide_pass, name='olvide_pass'),
    path('responde_pregunta/', views.preguntas_seguridad_recuperar, name='responde_pregunta'),
    path('actualizar_por_pregunta/', views.actualizar_contrasena_por_preguntas, name='actualizar_por_pregunta'),
    path('cerrar', views.cerrar_sesion, name='cerrar_sesion'),
    #path('user_views', views.users_view, name='user_views'),
    path('roles_views', views.rols_view, name='rols_views'),
    path('roles/<int:id>/editar/', views.guardar_rol_editado, name='editar_rol'),
    path('eliminar_rol/<int:id>/', views.eliminar_rol, name='eliminar_rol'),
    path('crear_rol', views.crear_rol, name='crear_rol'),
    path('crear_usuario', views.crear_usuario, name='crear_usuarios'),
    path('editar_usuario/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('eliminar_usuario/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('preguntas/', views.preguntas, name='preguntas'),
    path('preguntas/editar/<int:id_pregunta>/', views.editar_pregunta, name='editar_pregunta'),
    path('preguntas/eliminar/<int:id>/', views.eliminar_pregunta, name='eliminar_pregunta'),
    path('preguntas/crear/', views.crear_pregunta, name='crear_pregunta'),
    path('ver_mas_usuario/<int:id>/', views.ver_mas_usuario, name='ver_mas_usuario'),
    path('bitacora/', views.ver_bitacora, name='bitacora'),
    path('bitacora/eliminar/', views.eliminar_bitacora, name='eliminar_bitacora'),
    path('clientes/', views.mostrar_clientes, name='mostrar_clientes'),
    path('ver_mas_clientes/<int:id>/', views.ver_mas_clientes, name='ver_mas_clientes'),
    path('clientes/crear/', views.crear_cliente, name='crear_clientes'),
    path('clientes/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('ver_usuarios', views.ver_usuarios, name='ver_usuarios'),


]