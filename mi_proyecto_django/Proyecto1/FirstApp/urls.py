from django.urls import path
from Proyecto1.views import dia_actual, saludo
from .views import inicio, random_pwd, guardar_credencial, mostrar_credencial

urlpatterns = [
    path('bienvenido/<nombre>', saludo),
    path('dia/', dia_actual),
    path('', inicio),
    path('create-password/', random_pwd),
    path('save-credentials/', guardar_credencial),
    path('see-credentals/', mostrar_credencial),
]
