from django.db import models
from simple_history.models import HistoricalRecords
from django.utils.timezone import now
from .base import BaseModelServicio
from tumba.models import Tumba
from difunto.models import Difunto

naa="N/A"
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
    endDate = models.DateTimeField(default=now, blank=True, verbose_name='vecimiento')
    ceremony = models.CharField(max_length=50, default="Inhumacion", blank=True, verbose_name='tipo', choices= TIPO_CEREMONIA_CHOICES)
    is_paid = models.BooleanField(default=False, verbose_name='Cancelado')
    amount_paid = models.DecimalField(max_digits=10, default=1.1,decimal_places=2,  blank=True, verbose_name='Monto')
    payment_date = models.DateTimeField( blank=True, default=now, verbose_name='Fecha de pago')
    loadDate = models.DateTimeField(auto_now_add=True, verbose_name='creacion')
    updateDate = models.DateTimeField(auto_now=True, verbose_name='actualizacion')
    description = models.TextField(max_length=300, blank=True, default=naa, verbose_name='observaciones')
    numberTomb = models.ForeignKey(Tumba, related_name='servicioTumba',default=6000, on_delete=models.DO_NOTHING, blank=True) 
    deceased = models.ForeignKey(Difunto, related_name='servicioDifunto', on_delete=models.DO_NOTHING)
    history = HistoricalRecords()
    
    class Meta:
        permissions = [
                ("can_view_servicio", "Can view servicio"),
                ("can_edit_servicio", "Can edit servicio"),
            ]

