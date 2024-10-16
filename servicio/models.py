from django.db import models
from simple_history.models import HistoricalRecords
from .base import BaseModelServicio
from tumba.models import Tumba
from difunto.models import Difunto, Deudo

# Clase servicio
class Servicio(BaseModelServicio):
    TIPO_CEREMONIA_CHOICES = [
        ('Cremacion','Cremación'),
        ('Inhumacion','Inhumación'),
        ('Exhumacion','Exhumación'),
        ('Conmemoracion','Conmemoración'),
        ('Mantenimiento','Mantenimiento'),
    ]
    startDate = models.DateTimeField(verbose_name='inicio')
    endDate = models.DateTimeField(null=True, blank=True, verbose_name='vecimiento')
    ceremony = models.CharField(max_length=50, null=True, blank=True, verbose_name='tipo', choices= TIPO_CEREMONIA_CHOICES)
    is_paid=models.BooleanField(default=False, verbose_name='Cancelado')
    amount_paid=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Monto')
    payment_date=models.DateTimeField(null=True, blank=True, verbose_name='Fecha de pago')
    history=HistoricalRecords()
    numberTomb = models.ForeignKey(Tumba, related_name='servicioTumba', on_delete=models.DO_NOTHING, null=True,blank=True) 
    deceased = models.ForeignKey(Difunto, related_name='servicioDifunto', on_delete=models.DO_NOTHING)
    class Meta:
        permissions = [
                ("can_view_servicio", "Can view servicio"),
                ("can_edit_servicio", "Can edit servicio"),
            ]

