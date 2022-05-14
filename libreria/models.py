from django.db import models

class pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    especie = models.CharField(max_length=30)
    nivel = models.IntegerField()
    habilidad = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


# Create your models here.
class entrenador(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre= models.TextField(max_length=150)
    pokemon = models.ForeignKey(pokemon, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.nombre, self.pokemon




