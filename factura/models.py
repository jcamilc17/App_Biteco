from django.db import models

from datetime import date

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
    # TODO terminar las asociaciones para itemfactura ver como hacerlo un coso imbeded

    def __str__(self):
        return f'{self.numeroFactura} en {self.fecha}. Total: {self.total}{self.moneda}'
    
    class Meta:
        app_label = 'factura'
