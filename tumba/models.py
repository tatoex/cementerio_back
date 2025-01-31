from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from .base import BaseModelTumba

# Clase lote
class Lote (BaseModelTumba):
    blockName = models.PositiveIntegerField(verbose_name='Lote',validators=[
            MinValueValidator(1),
            MaxValueValidator(12)
        ],)# Numero de lote
    typeblock=models.CharField(max_length=3, verbose_name='Tipo de Bloque')# Tipo de bloque
    numbersblock=models.PositiveIntegerField(blank=True, default=0,verbose_name='numero de tipo')# numero de bloque
    filas=models.PositiveIntegerField(verbose_name='Numero de filas')# Coordenada X
    columnas=models.PositiveIntegerField(verbose_name='Numero de columnas')# Coordenada X
    limite=models.PositiveIntegerField(verbose_name='Limite de espacio')# Coordenada X
    x = models.FloatField(default=0.1,verbose_name='x', blank="true")  # Coordenada X
    y = models.FloatField(default=0.1,verbose_name='y', blank="true")  # Coordenada Y
    rotation = models.IntegerField(default=0, verbose_name='rotacion', blank="true")  # Rotación opcional
    text_x = models.IntegerField(default=0,verbose_name='text x', blank="true")  # Posición X del texto
    text_y = models.IntegerField(default=0,verbose_name='text y', blank="true")  # Posición Y del texto
    trans_r_x = models.FloatField(default=0.0, verbose_name='Translate X', blank=True)  # Coordenada X del translate rectangulo
    trans_r_y = models.FloatField(default=0.0, verbose_name='Translate Y', blank=True)  # Coordenada Y del translate rectangulo
    trans_t_x = models.FloatField(default=0.0, verbose_name='Translate X', blank=True)  # Coordenada X del translate texto
    trans_t_y = models.FloatField(default=0.0, verbose_name='Translate Y', blank=True)  # Coordenada Y del translate texto
    history=HistoricalRecords()
    @extend_schema_field(serializers.IntegerField)
    def ocupadas(self):
        return self.tumbaLote.filter(available=False).count()
    @extend_schema_field(serializers.IntegerField)
    def disponibles(self):
        return self.tumbaLote.filter(available=True).count()
    def clean(self):
        if self.pk and self.limite < self.tumbaLote.count():
            raise ValidationError("El límite no puede ser menor que las tumbas existentes.")
        super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()  # Asegura que las validaciones se ejecuten
        super().save(*args, **kwargs)

# Clase tumba
class Tumba (BaseModelTumba):
    # Definiendo las opciones de tipo de nichos
    TIPO_NICHO_CHOICES = [
        ('T','Tumba de tierra'),
        ('E','Tumba extramuros'),
    ]
    nicheNumber = models.PositiveIntegerField( verbose_name='tumba',validators=[MaxValueValidator(99999)])
    nicheType = models.CharField(max_length=1, verbose_name='tipo', choices= TIPO_NICHO_CHOICES)
    available = models.BooleanField(default=True)
    history=HistoricalRecords()
    nameLote = models.ForeignKey(Lote, related_name='tumbaLote', on_delete=models.CASCADE) 
    def clean(self):
        if self.nicheNumber <= 0:
            raise ValidationError({'nicheNumber': 'El número de tumba debe ser mayor a 0.'})
        super().clean()
    def save(self, *args, **kwargs):
        if self.nameLote and self.nameLote.tumbaLote.count() >= self.nameLote.limite:
            raise ValidationError("No se pueden agregar más tumbas, se ha alcanzado el límite del lote.")
        super().save(*args, **kwargs)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nicheNumber', 'nameLote'], name='unique_niche_per_lote')
        ]
    