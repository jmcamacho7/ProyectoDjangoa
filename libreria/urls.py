from django.urls import path
from .views import *

urlpatterns = [
    path('inicio/', cargar_inicio),
    path('libros/', cargar_vista_pokemon),
    path('libros/crear/', crear_pokemon),
    path('libros/<int:id>',detalle_pokemon),
    path('libros/editar/<int:id>', editar_pokemon),
    path('libros/borrar/<int:id>', borrar_pokemon)
]