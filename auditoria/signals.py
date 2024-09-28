from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from difunto.models import Difunto, Deudo
from tumba.models import Tumba, DisponibleTumba, Lote
from servicio.models import Servicio, Ceremonia
from .utils import AutitoriaManager

@receiver(post_save, sender=Difunto)
@receiver(post_save, sender=Deudo)
@receiver(post_save, sender=Lote)
@receiver(post_save, sender=Tumba)
@receiver(post_save, sender=DisponibleTumba)
@receiver(post_save, sender=Servicio)
@receiver(post_save, sender=Ceremonia)
def auditar_crear_modificar(sender, instance, created, **kwargs):
    auditor=AutitoriaManager(instance, sender.__name__)
    accion='CREAR' if created else 'MODIFICAR'
    auditor.auditar_accion(accion)

@receiver(post_delete, sender=Difunto)
@receiver(post_delete, sender=Deudo)
@receiver(post_delete, sender=Lote)
@receiver(post_delete, sender=Tumba)
@receiver(post_delete, sender=DisponibleTumba)
@receiver(post_delete, sender=Servicio)
@receiver(post_delete, sender=Ceremonia)
def auditar_crear_modificar(sender, instance, created, **kwargs):
    auditor=AutitoriaManager(instance, sender.__name__)
    auditor.auditar_accion('BORRAR')
