from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField(default=00000000)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
