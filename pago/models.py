from django.db import models

from empresa.models import Empresa
from factura.models import Factura

class Pago(models.Model):
    fecha = models.DateField()
    monto = models.DecimalField(decimal_places=2)
    moneda = models.CharField(max_length=100)
    metodoPago = models.CharField(max_length=100)
    referencia = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    comprobante = models.CharField()
    
    # Relaciones
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, verbose_name='factura')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name='empresa')

    def __str__(self):
        return f'{self.monto}{self.moneda} en {self.fecha}. Estado: {self.estado}'
    
    class Meta:
        app_label = 'pago'