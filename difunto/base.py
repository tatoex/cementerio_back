from django.db import models


class BaseModelDifunto(models.Model):
    names = models.CharField( max_length=200, verbose_name='nombres')
    last_names = models.CharField( max_length=200, verbose_name='apellidos')
    idNumber = models.CharField(max_length=10, unique=True, verbose_name='cedula')
    loadDate = models.DateTimeField(auto_now_add=True, verbose_name='creacion')
    updateDate = models.DateTimeField(auto_now=True, verbose_name='actualizacion')
    description = models.TextField(max_length=300, blank=True, null=True, verbose_name='observaciones')


    class Meta:
        abstract = True