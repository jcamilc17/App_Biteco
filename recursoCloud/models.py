from django.db import models

class RecursoCloud(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    tamano = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    fechaCreacion = models.DateField(auto_now_add=True)
    etiquetas = models.CharField(max_length=100)
    # TODO relaciones
    
    def __str__(self):
        return f'{self.nombre} creado en {self.fechaCreacion}'
    
    class Meta:
        app_label = 'recursoCloud'