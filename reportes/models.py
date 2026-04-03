from django.db import models

# Create your models here.
class ConsumoCloud(models.Model):
    empresa_id = models.IntegerField() # FK a Empresa, pero sin relacion directa para evitar dependencias
    empresa_nombre = models.CharField(max_length=100) 
    proveedor = models.CharField(max_length=20)  # 'AWS' o 'GCP'
    servicio = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=12, decimal_places=4) # Costo total del servicio en el mes
    mes = models.IntegerField() # 1-12
    anio = models.IntegerField() # Año del consumo
    region = models.CharField(max_length=50, null=True, blank=True) 

    def __str__(self):
        return '%s %s %s/%s' % (self.empresa_nombre, self.proveedor, self.mes, self.anio)

    class Meta:
        app_label = 'reportes'