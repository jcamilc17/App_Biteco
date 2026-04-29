from django.db import models

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    presupuestoMensual = models.models.DecimalField(decimal_places=2)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    estado = models.CharField(max_length=100)
    # TODO relaciones

    def __str__(self):
        return f'{self.nombre}, Estado: {self.estado}'
    
    class Meta:
        app_label = 'proyecto'