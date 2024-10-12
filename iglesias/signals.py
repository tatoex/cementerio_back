from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Iglesia, Parroquia
from .utils import actualizar_numero_iglesias

@receiver(post_save, sender=Iglesia)
def actualizar_numero_iglesias_post_save(sender, instance, **kwargs):
    actualizar_numero_iglesias(instance.parroquia)
    
@receiver(post_delete, sender=Iglesia)
def actualizar_numero_iglesias_post_save(sender, instance, **kwargs):
    actualizar_numero_iglesias(instance.parroquia)
