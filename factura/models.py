from django.db import models

from datetime import date

from empresa.models import Empresa

class Factura(models.Model):
    numeroFactura = models.CharField(max_length=100)
    fecha = models.DateField(default=date.today)
    fechaVencimiento = models.DateField()
    subtotal = models.DecimalField(decimal_places=2)
    impuestos = models.DecimalField(decimal_places=2)
    total = models.DecimalField(decimal_places=2)
    moneda = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    conceptos = models.CharField(max_length=100)
    
    # Relaciones
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name='empresa')

    def __str__(self):
        return f'{self.numeroFactura} en {self.fecha}. Total: {self.total}{self.moneda}'
    
    class Meta:
        app_label = 'factura'

class ItemFactura(models.model):
    concepto = models.CharField(max_length=100)
    cantidad = models.IntegerField(min=1)
    precioUnitario = models.DecimalField(decimal_places=2)
    subtotal = models.DecimalField(decimal_places=2, default=cantidad*precioUnitario)
    
    # Relaciones
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, verbose_name="factura")