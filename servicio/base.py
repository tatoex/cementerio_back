from django.db import models

class BaseModelServicio(models.Model):
    loadDate = models.DateTimeField(auto_now_add=True, verbose_name='creacion')
    updateDate = models.DateTimeField(auto_now=True, verbose_name='actualizacion')
    description = models.TextField(max_length=300, blank=True, null=True, verbose_name='observaciones')


    class Meta:
        abstract = True
