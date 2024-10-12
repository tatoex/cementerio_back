from django.db import models
from simple_history.models import HistoricalRecords
from .base import BaseModelServicio
from tumba.models import Tumba
from difunto.models import Difunto, Deudo

# Clase servicio
class Servicio(BaseModelServicio):
    startDate = models.DateTimeField(verbose_name='inicio')
    endDate = models.DateTimeField(null=True, blank=True, verbose_name='vecimiento')
    history=HistoricalRecords()
    numberTomb = models.ForeignKey(Tumba, related_name='servicioTumba', on_delete=models.DO_NOTHING, null=True,blank=True) 
    deceased = models.ForeignKey(Difunto, related_name='servicioDifunto', on_delete=models.DO_NOTHING)


# Clase ceremonia  
class Ceremonia(BaseModelServicio):
    TIPO_CEREMONIA_CHOICES = [
        ('Cremacion','Cremación'),
        ('Inhumacion','Inhumación'),
        ('Exhumacion','Exhumación'),
        ('Conmemoracion','Conmemoración'),
        ('Mantenimiento','Mantenimiento'),
    ]
    names = models.CharField(max_length=50, verbose_name='tipo', choices= TIPO_CEREMONIA_CHOICES)
    date = models.DateTimeField(verbose_name='fecha')
    is_paid=models.BooleanField(default=False, verbose_name='Cancelado')
    amount_paid=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Monto')
    payment_date=models.DateTimeField(null=True, blank=True, verbose_name='Fecha de pago')
    history=HistoricalRecords()
    servicios = models.ForeignKey(Servicio, related_name='ceremoniaServicio', on_delete=models.CASCADE) 
