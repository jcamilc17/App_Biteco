from django.db import models

from proyecto.models import Proyecto
from recursoCloud.models import RecursoCloud

class registroCosto(models.Model):
    fecha = models.DateField(auto_now_add=True)
    monto = models.DecimalField(decimal_places=2)
    moneda = models.CharField(max_length=100)
    servicioCloud = models.CharField(max_length=100)
    unidadMedida = models.CharField(max_length=100)
    cantidad = models.DecimalField(decimal_places=2)
    
    # Relaciones
    recursoCloud = models.ForeignKey(RecursoCloud, on_delete=models.SET_NULL, verbose_name='recursoCloud')
    proyecto = models.ForeignKey(Proyecto, on_delete=models.SET_NULL, verbose_name='proyecto')

    def __str__(self):
        return f'{self.accountId}, Estado: {self.estado}'
    
    class Meta:
        app_label = 'registroCosto'