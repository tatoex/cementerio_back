from django.db import models
from django.utils import timezone


class BaseModelTumba(models.Model):
    loadDate = models.DateTimeField(auto_now_add=True, verbose_name='creacion')
    updateDate = models.DateTimeField(auto_now=True, verbose_name='actualizacion')
    description = models.TextField(max_length=300, blank=True, null=True, verbose_name='observaciones')
    

    class Meta:
        abstract = True

def actualizar_estado_disponibilidad(tumba):
    """Sincroniza las fechas de Disponibilidad en funcion a servicio"""
    DisponibleTumba=models.get_model('tumba','DisponibleTumba')
    disponibilidad=DisponibleTumba.objects.filter(numberTumba=tumba).first()
    if disponibilidad:
                now=timezone.now()
                if disponibilidad.startDate<=now<=disponibilidad.endDate:
                    tumba.available=True
                else:
                    tumba.available=False
                tumba.save()