from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DisponibleTumba
from .utils import actualizar_estado_disponibilidad

@receiver(post_save, sender=DisponibleTumba)
def actualizar_disponibilidad_tumba(sender, instance, **kwargs):
    """señal para actualizar estado de la tumba"""
    tumba=instance.numberTumba
    actualizar_estado_disponibilidad(tumba)