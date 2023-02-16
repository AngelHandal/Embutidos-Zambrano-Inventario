from django.urls import path
from . import views


urlpatterns = [
    path("", views.login, name='login'),
    path('bienvenido/', views.bienvenido, name='bienvenido'),
    path('cerrar', views.cerrar_sesion, name='cerrar_sesion'),

]