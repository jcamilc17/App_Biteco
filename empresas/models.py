import datetime

from django.db import models
from plan_suscripcion.models import PlanSuscripcion

class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    razonSocial = models.CharField(max_length=100)
    nit = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    fechaRegistro = models.DateField(default=datetime.date.today)
    estado = models.CharField(max_length=100)
    plan_suscripcion = models.ForeignKey(PlanSuscripcion, on_delete=models.SET_NULL, default=None)

    def __str__(self):
        return f'{self.name}, {self.nit}'
    
    class Meta:
        app_label = 'empresas'
