from django.db import models

from empresa.models import Empresa
from usuario.models import Usuario

class RegistroAuditoria(models.Model):
    accion = models.CharField(max_length=100)
    fecha = models.DateField()
    ipOrigen = models.models.CharField(max_length=100)
    detalles = models.models.CharField(max_length=100)
    resultado = models.models.CharField(max_length=100)
    
    # Relaciones
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, verbose_name='usuario')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name='empresa')
    
    def __str__(self):
        return f'{self.pk}'
    
    class Meta:
        app_label = 'registroAuditoria'