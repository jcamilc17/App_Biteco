from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from empresa.models import Empresa
from proyecto.models import Proyecto
from usuario.models import Usuario

# Create your models here.
class Reporte(models.Model):
    titulo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    fechaGeneracion = models.DateField(auto_now_add=True)
    periodoInicio = models.DateField()
    periodoFin = models.DateField()
    formato = models.CharField(max_length=100)
    
    # Relaciones
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, verbose_name='usuario')
    empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL, verbose_name='empresa')
    proyecto = models.ForeignKey(Proyecto, on_delete=models.SET_NULL, verbose_name='proyecto')

    def __str__(self):
        return '%s %s %s/%s' % (self.empresa_nombre, self.proveedor, self.mes, self.anio)

    class Meta:
        app_label = 'reporte'