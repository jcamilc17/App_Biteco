from django.db import models

class PlanSuscripcion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    precioMensual = models.models.FloatField(decimal_places=2)
    maxUsuarios = models.IntegerField()
    maxProyectos = models.IntegerField()
    soportePremium = models.BooleanField()
    analisisAvanzado = models.BooleanField()
    estado = models.CharField()
    
    def __str__(self):
        return f'{self.nombre}:{self.descripcion}'
    
    class Meta:
        app_label = 'planes_suscripcion'