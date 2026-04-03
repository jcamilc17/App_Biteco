from django.db import models

# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField(max_length=100) # Nombre de la empresa
    nit = models.CharField(max_length=20, unique=True) 
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'usuarios'