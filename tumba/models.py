from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords
from .base import BaseModelTumba

# Clase lote
class Lote (BaseModelTumba):
    blockName = models.IntegerField(verbose_name='Bloque')
    typeblock=models.CharField(max_length=3, verbose_name='Tipo de Bloque')
    numbersblock=models.IntegerField(null=True,verbose_name='numero de tipo')
    filas=models.IntegerField(verbose_name='Numero de filas')
    columnas=models.IntegerField(verbose_name='Numero de columnas')
    limite=models.IntegerField(verbose_name='Limite de espacio')
    history=HistoricalRecords()
    @property
    def ocupadas(self):
        return self.tumbaLote.filter(available=False).count()
    @property
    def disponibles(self):
        return self.tumbaLote.filter(available=True).count()

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
    
