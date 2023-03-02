from django.urls import path
from . import views


urlpatterns = [
    path("", views.login, name='login'),
    path('bienvenido/', views.bienvenido, name='bienvenido'),
    path('olvide_pass/', views.olvide_pass, name='olvide_pass'),
    path('responde_pregunta/', views.preguntas_seguridad_recuperar, name='responde_pregunta'),
    path('actualizar_por_pregunta/', views.actualizar_contrasena_por_preguntas, name='actualizar_por_pregunta'),
    path('cerrar', views.cerrar_sesion, name='cerrar_sesion'),
    path('user_views', views.users_view, name='user_views'),
    path('roles_views', views.rols_view, name='rols_views'),
    path('roles/<int:id>/editar/', views.guardar_rol_editado, name='editar_rol'),
    path('eliminar_rol/<int:id>/', views.eliminar_rol, name='eliminar_rol'),
    path('crear_rol', views.crear_rol, name='crear_rol'),
    path('crear_usuario', views.crear_usuario, name='crear_usuarios'),


]