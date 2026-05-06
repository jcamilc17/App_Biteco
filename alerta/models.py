from django.db import models

from empresa.models import Empresa
from usuario.models import Usuario

class Alerta(models.Model):
    tipo = models.CharField(max_length=100)
    severidad = models.CharField(max_length=100)
    mensaje = models.CharField(max_length=500)
    fechaCreacion = models.DateField(auto_now_add=True)
    fechaLectura = models.DateField(auto_now=True)
    estado = models.CharField(max_length=100)
    
    # Relaciones
    usuario = models.ForeignKey(Usuario, verbose_name=_("usuarioAlerta"), on_delete=models.SET_NULL)
    empresa = models.ForeignKey(Empresa, verbose_name=_("empresaAlerta"), on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.tipo}-{self.severidad}: {self.mensaje}'
    
    class Meta:
        app_label = 'alerta'