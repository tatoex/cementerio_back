from django.db import models
from .base import BaseModelDifunto
from simple_history.models import HistoricalRecords
from tumba.models import Tumba

# Clase deudo
class Deudo(BaseModelDifunto):
    TIPO_DEUDO_CHOICES = [
        ('Allegado','Familiar cercano'),
        ('Familiar','Miembro de la familia'),
        ('Conocido','Conocido del fallecido'),
    ]
    phoneNumber = models.CharField(max_length=15, verbose_name='telefono')
    email = models.EmailField( verbose_name='email')
    address = models.CharField(max_length=100, blank=True, null=True, verbose_name='direccion')
    tipo = models.CharField(max_length=50, verbose_name='tipo relacion', choices=TIPO_DEUDO_CHOICES, null=True)
    history=HistoricalRecords()

# Clase difunto
class Difunto(BaseModelDifunto):
    requestNumber = models.CharField(max_length=20, unique=True, verbose_name='solicitud')
    history = HistoricalRecords()
    tumba = models.ForeignKey(Tumba, related_name='difuntoTumba', on_delete=models.DO_NOTHING) 
    deudo = models.ForeignKey(Deudo, related_name='difuntoDeudo', on_delete=models.DO_NOTHING) 

