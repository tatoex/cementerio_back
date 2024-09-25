from django.db import models
from tumba.models import Tumba
from difunto.models import Difunto

# Create your models here.
class Servicio(models.Model):
    startDate = models.DateTimeField(verbose_name='inicio')
    endDate = models.DateTimeField(null=True, blank=True, verbose_name='vecimiento')
    loadDate = models.DateTimeField(auto_now_add=True, verbose_name='creacion')
    updateDate = models.DateTimeField(auto_now=True, verbose_name='actualizacion')
    decription = models.TextField(max_length=300, blank=True, null=True, verbose_name='observaciones')
    numberTomb = models.ForeignKey(Tumba, related_name='servicioTumba', on_delete=models.DO_NOTHING) 
    deceased = models.ForeignKey(Difunto, related_name='servicioDifunto', on_delete=models.DO_NOTHING) 
    
class Ceremonia(models.Model):
        TIPO_CEREMONIA_CHOICES[
        ('Cremacion','Cremación'),
        ('Inhumacion','Inhumación'),
        ('Exhumacion','Exhumación'),
    ]
    name = models.CharField(max_length=50, choices=TIPO_CEREMONIA_CHOICES, verbose_name='tipo')
    date = models.DateTimeField(verbose_name='fecha')
    loadDate = models.DateTimeField(auto_now_add=True, verbose_name='creacion')
    updateDate = models.DateTimeField(auto_now=True, verbose_name='actualizacion')
    decription = models.TextField(max_length=300, blank=True, null=True, verbose_name='observaciones')
    servicios = models.ForeignKey(Servicio, related_name='ceremoniaServicio', on_delete=models.CASCADE) 
