# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.utils.timezone import now  # Para obtener la fecha actual
# from servicio.models import Servicio
# from tumba.models import Tumba  # Asegúrate de importar correctamente

# @receiver(post_save, sender=Servicio)
# def actualizar_disponibilidad_tumba(sender, instance, **kwargs):
#     """Actualiza la disponibilidad de la tumba basada en las fechas del servicio"""
    
#     # Obtenemos la fecha actual
#     fecha_actual = now().date()  # Solo la fecha, sin la hora
    
#     # Si la tumba está asociada al servicio
#     if instance.tumba:
#         # Verificamos si la fecha actual está fuera del rango
#         if instance.startDate and instance.endDate:
#             if fecha_actual < instance.startDate or fecha_actual > instance.endDate:
#                 # Si está fuera del rango de fechas, la tumba está disponible
#                 instance.tumba.available = True
#             else:
#                 # Si está dentro del rango de fechas, la tumba no está disponible
#                 instance.tumba.available = False
#             instance.tumba.save()  # Guardar los cambios en la tumba
