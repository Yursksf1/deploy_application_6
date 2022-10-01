
from django.db import models

# Create your models here.

class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    new_file = models.CharField(max_length=100, default='', blank=True, null=True)

    def __str__(self):
        return "{}".format(self.nombre)

class Tema(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(default='', blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.nombre, self.materia)