from django.db import models

class BaseModelTumba(models.Model):
    loadDate = models.DateTimeField(auto_now_add=True, verbose_name='creacion')
    updateDate = models.DateTimeField(auto_now=True, verbose_name='actualizacion')
    decription = models.TextField(max_length=300, blank=True, null=True, verbose_name='observaciones')

    class Meta:
        abstract = True