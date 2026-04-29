from django.db import models

class RegistroAuditoria(models.Model):
    accion = models.CharField(max_length=100)
    #TODO terminar esto cuando usuario este hecho usuario = models.ForeignKey()
    fecha = models.DateField()
    ipOrigen = models.models.CharField(max_length=100)
    detalles = models.models.CharField(max_length=100)
    resultado = models.models.CharField(max_length=100)
    # TODO relaciones, ver si volver la clase embeded en empresa
    
    def __str__(self):
        return f'{self.pk}'
    
    class Meta:
        app_label = 'registroAuditoria'