from .models import Parroquia

def actualizar_numero_iglesias(parroquia):
    """actualiza el numero de iglesas asociadas a una parroquia."""
    churches_number=parroquia.iglesias.count()
    parroquia.churches_number=churches_number
    parroquia.save()