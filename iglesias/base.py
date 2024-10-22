from django.db import models
from django.core.exceptions import ValidationError

def validar_tamano_imagen(image):
    max_tamano = 2 * 1024 * 1024  # Limita a 2MB
    if image.size > max_tamano:
        raise ValidationError("El tamaño máximo permitido es 2MB.")
        
class BaseIglesia(models.Model):
    image=models.ImageField(upload_to='iglesias/', null=True, blank=True, , validators=[validar_tamano_imagen], verbose_name='Foto')
    loadDate = models.DateTimeField(auto_now_add=True, verbose_name='Creacion')
    updateDate = models.DateTimeField(auto_now=True, verbose_name='Actualizacion')
    

    class Meta:
        abstract=True

    def __str__(self):
        return self.name