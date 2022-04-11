from django.db import models

class Automovil(models.Model):
    patente = models.CharField(max_length=10, unique=True)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()
    marca = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="automoviles", null=True, blank=True)

    def __str__(self):
        return self.patente


