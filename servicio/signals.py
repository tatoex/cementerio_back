from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Servicio
from .utils import sincronizar_disponibilidad_tumba

@receiver(post_save, sender=Servicio)
def actualizar_disponibilidad_tumba(sender, instance, **kwargs):
    """señal para sincrunizar fechas y numero de tumba"""
    sincronizar_disponibilidad_tumba(instance)