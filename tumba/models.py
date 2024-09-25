from django.db import models
from .utils import BaseModelTumba


# Clase lote
class Lote (BaseModelTumba):
    blockName = models.CharField(max_length=3, verbose_name='lote')

# Clase tumba
class Tumba (BaseModelTumba):
    # Definiendo las opciones de tipo de nichos
    TIPO_NICHO_CHOICES = [
        ('T','Tumba de tierra'),
        ('E','Tumba extramuros'),
    ]
    nicheNumber = models.IntegerField(max_length=4, verbose_name='tumba')
    nicheType = models.CharField(max_length=1, verbose_name='tipo', choices= TIPO_NICHO_CHOICES)
    nameLote = models.ForeignKey(Lote, related_name='tumbaLote', on_delete=models.CASCADE) 

# Clase Disponibilidad
class DisponibleTumba (BaseModelTumba):
    startDate = models.DateTimeField(verbose_name='inicio')
    endDate = models.DateTimeField(verbose_name='vence')
    numberTumba = models.ForeignKey(Tumba, related_name='disponibleTumba', on_delete=models.DO_NOTHING) 
