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
    deudo = models.ForeignKey(Deudo, null=True,related_name='servicioDeudo', on_delete=models.DO_NOTHING)  

# Clase ceremonia  
class Ceremonia(BaseModelServicio):
    TIPO_CEREMONIA_CHOICES = [
        ('Cremacion','Cremación'),
        ('Inhumacion','Inhumación'),
        ('Exhumacion','Exhumación'),
        ('Mantenimiento','Mantenimiento'),
    ]
    names = models.CharField(max_length=50, verbose_name='tipo', choices= TIPO_CEREMONIA_CHOICES)
    date = models.DateTimeField(verbose_name='fecha')
    history=HistoricalRecords()
    servicios = models.ForeignKey(Servicio, related_name='ceremoniaServicio', on_delete=models.CASCADE) 
