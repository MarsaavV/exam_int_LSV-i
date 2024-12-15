# meseros/models.py
from django.db import models

class Mesero(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    procedencia = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.nombre
