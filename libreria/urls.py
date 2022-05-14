from django.urls import path
from .views import *

urlpatterns = [
    path('inicio/', cargar_inicio),
    path('libros/', cargar_vista_pokemon),
    path('libros/crear/', crear_pokemon, name='crear_pokemon'),
    path('libros/<int:id>',detalle_pokemon, name='detalle_pokemon'),
    path('libros/editar/<int:id>', editar_pokemon, name='editar_pokemon'),
    path('libros/borrar/<int:id>', borrar_pokemon, name='borrar_pokemon')
]