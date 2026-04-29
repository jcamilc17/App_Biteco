from django.db import models

class CuentaCloud(models.Model):
    proveedor = models.CharField(max_length=100)
    accountId = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    credenciales = models.CharField(max_length=100)
    fechaIntegracion = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=100)
    # TODO terminar las relaciones

    def __str__(self):
        return f'{self.accountId}, Estado: {self.estado}'
    
    class Meta:
        app_label = 'cuentaCloud'