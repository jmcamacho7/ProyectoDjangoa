from django.shortcuts import render,redirect
from .models import *


# Create your views here.

def cargar_inicio(request):
    return render(request, 'inicio.html')


def cargar_vista_pokemon(requests):
    lista_pokemon = pokemon.objects.all()
    return render(requests,'libros.html', {'pokemones': lista_pokemon})


def crear_pokemon(request):
    # Método para operación CRUD Crear nuevo libro
    if request.method == 'POST':
        # En caso de que no exista id quiere decir que no existe y hay que crearlo
        bicho = pokemon()
        bicho.id = request.POST.get('id')
        bicho.nombre = request.POST.get('nombre')
        bicho.especie = request.POST.get('especie')
        bicho.nivel = request.POST.get('nivel')
        bicho.habilidad = request.POST.get("habilidad")
        pokemon.save(bicho)
        return redirect('/libreria/libros')
    else:
        return render(request, 'crear_libro.html')


def editar_pokemon(request,id):
    if request.method == "GET":
        bicho = pokemon.objects.get(id=id)
        return render(request, 'editar_libro.html', {"pokemon": bicho})
    else:
        bicho = pokemon.objects.get(id=id)
        bicho.nombre = request.POST.get('nombre')
        bicho.especie = request.POST.get('especie')
        bicho.nivel = request.POST.get('nivel')
        bicho.habilidad = request.POST.get("habilidad")
        pokemon.save(bicho)
        return redirect('/libreria/libros')



def detalle_pokemon(request, id):
    if request.method == "GET":
        bicho = pokemon.objects.get(id=id)

        return render(request, 'libro_detalle.html', {"pokemon": bicho})
    else:
        bicho = pokemon.objects.get(id=id)
        bicho.id = request.POST.get('id')
        bicho.nombre = request.POST.get('nombre')
        bicho.especie = request.POST.get('especie')
        bicho.nivel = request.POST.get('nivel')
        bicho.habilidad = request.POST.get("habilidad")
        return redirect("/libreria")


def borrar_pokemon(request,id):
    bicho = pokemon.objects.get(id=id)
    if bicho is not None:
        pokemon.delete(bicho)
    return redirect('/libreria/libros')




