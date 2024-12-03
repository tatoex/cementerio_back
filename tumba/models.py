from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords
from .base import BaseModelTumba

# Clase lote
class Lote (BaseModelTumba):
    blockName = models.IntegerField(verbose_name='Lote')# Numero de lote
    typeblock=models.CharField(max_length=3, verbose_name='Tipo de Bloque')# Tipo de bloque
    numbersblock=models.IntegerField(blank=True,verbose_name='numero de tipo')# numero de bloque
    filas=models.IntegerField(verbose_name='Numero de filas')# Coordenada X
    columnas=models.IntegerField(verbose_name='Numero de columnas')# Coordenada X
    limite=models.IntegerField(verbose_name='Limite de espacio')# Coordenada X
    x = models.FloatField(verbose_name='x', blank="true")  # Coordenada X
    y = models.FloatField(verbose_name='y', blank="true")  # Coordenada Y
    width = models.FloatField(verbose_name='ancho', blank="true")  # Ancho del rectángulo
    height = models.FloatField(verbose_name='alto', blank="true")  # Alto del rectángulo
    rotation = models.FloatField(default=0, verbose_name='rotacion', blank="true")  # Rotación opcional
    text_x = models.FloatField(default=0,verbose_name='text x', blank="true")  # Posición X del texto
    text_y = models.FloatField(default=0,verbose_name='text y', blank="true")  # Posición Y del texto
    history=HistoricalRecords()
    @extend_schema_field(serializers.IntegerField)
    def ocupadas(self):
        return self.tumbaLote.filter(available=False).count()
    @extend_schema_field(serializers.IntegerField)
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
    
