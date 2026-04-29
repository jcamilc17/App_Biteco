from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=320, unique=True)
    rol = models.CharField()
    telefono = models.CharField(max_length=15)
    fechaCreacion = models.DateField(auto_now_add=True)
    ultimoAcceso = models.DateField(auto_now=True)
    estado = models.CharField(max_length=100)
    # TODO relaciones

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'usuario'