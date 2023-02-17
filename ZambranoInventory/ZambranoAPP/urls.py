from django.urls import path
from . import views


urlpatterns = [
    path("", views.login, name='login'),
    path('bienvenido/', views.bienvenido, name='bienvenido'),
    path('cerrar', views.cerrar_sesion, name='cerrar_sesion'),
    path('user_views', views.users_view, name='user_views'),
    path('roles_views', views.rols_view, name='rols_views'),

]