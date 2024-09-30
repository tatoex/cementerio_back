from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords
from .utils import BaseModelTumba

# Clase lote
class Lote (BaseModelTumba):
    blockName = models.IntegerField(verbose_name='bloque')
    typeblock=models.CharField(max_length=3, verbose_name='Tipo')
    numbersblock=models.IntegerField(verbose_name='numero de tipo', null=True)
    filas=models.IntegerField(verbose_name='Nuero de filas')
    columnas=models.IntegerField(verbose_name='Nuero de columnas')
    limite=models.IntegerField(verbose_name='Limite de espacio')
    history=HistoricalRecords()


# Clase tumba
class Tumba (BaseModelTumba):
    # Definiendo las opciones de tipo de nichos
    TIPO_NICHO_CHOICES = [
        ('T','Tumba de tierra'),
        ('E','Tumba extramuros'),
    ]
    nicheNumber = models.IntegerField( verbose_name='tumba')
    nicheType = models.CharField(max_length=1, verbose_name='tipo', choices= TIPO_NICHO_CHOICES)
    available = models.BooleanField(default=True)
    history=HistoricalRecords()
    nameLote = models.ForeignKey(Lote, related_name='tumbaLote', on_delete=models.CASCADE) 
    


# Clase Disponibilidad
class DisponibleTumba (BaseModelTumba):
    startDate = models.DateTimeField(verbose_name='inicio')
    endDate = models.DateTimeField(verbose_name='vence')
    history=HistoricalRecords()
    numberTumba = models.ForeignKey(Tumba, related_name='disponibleTumba', on_delete=models.DO_NOTHING) 


