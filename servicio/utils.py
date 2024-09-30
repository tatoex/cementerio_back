from django.db import models
from tumba.models import DisponibleTumba



class BaseModelServicio(models.Model):
    loadDate = models.DateTimeField(auto_now_add=True, verbose_name='creacion')
    updateDate = models.DateTimeField(auto_now=True, verbose_name='actualizacion')
    description = models.TextField(max_length=300, blank=True, null=True, verbose_name='observaciones')


    class Meta:
        abstract = True

def sincronizar_disponibilidad_tumba(servicio):
    """Sincroniza las fechas de Disponibilidad en funcion a servicio"""
    dispobilidad=DisponibleTumba.objects.filter(numberTumba=servicio.numberTomb).first()
    if dispobilidad:
        dispobilidad.startDate = servicio.startDate
        dispobilidad.endDate = servicio.endDate
        dispobilidad.numberTumba = servicio.numberTomb
        dispobilidad.save()