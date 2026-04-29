from django.db import models

class registroCosto(models.Model):
    fecha = models.DateField(auto_now_add=True)
    monto = models.DecimalField(decimal_places=2)
    moneda = models.CharField(max_length=100)
    servicioCloud = models.CharField(max_length=100)
    unidadMedida = models.CharField(max_length=100)
    cantidad = models.DecimalField(decimal_places=2)
    #TODO terminar relaciones

    def __str__(self):
        return f'{self.accountId}, Estado: {self.estado}'
    
    class Meta:
        app_label = 'registroCosto'