from django.db import models


class BaseModelDifunto(models.Model):
    names = models.CharField( max_length=200, verbose_name='nombres')
    last_names = models.CharField( max_length=200, verbose_name='apellidos')
    idNumber = models.CharField(max_length=10, verbose_name='cedula', unique=True)
    loadDate = models.DateTimeField(auto_now_add=True, verbose_name='creacion')
    updateDate = models.DateTimeField(auto_now=True, verbose_name='actualizacion')
    description = models.TextField(default="N/A",max_length=300, blank=True, verbose_name='observaciones')


    class Meta:
        abstract = True

