from django.db import models

# Create your models here.
class Familia(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"