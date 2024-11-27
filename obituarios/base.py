from django.db import models

class BaseObituario(models.Model):
    date = models.DateTimeField( blank=True, verbose_name='Fecha y Hora')
    loadDate = models.DateTimeField(auto_now_add=True, verbose_name='creacion')
    updateDate = models.DateTimeField(auto_now=True, verbose_name='actualizacion')
    description = models.TextField(max_length=300, blank=True,  verbose_name='observaciones')