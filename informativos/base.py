from django.db import models
from django.core.exceptions import ValidationError

def validar_tamano_imagen(image):
    max_tamano = 2 * 1024 * 1024  # Limita a 2MB
    if image.size > max_tamano:
        raise ValidationError("El tamaño máximo permitido es 2MB.")

class BaseInformativo(models.Model):
    category = models.CharField(max_length=100, verbose_name='Categoria')
    title = models.CharField(max_length=200, verbose_name='Titulo')
    description_short = models.TextField( null=True, blank=True,verbose_name='Descripcion breve')
    image = models.ImageField(upload_to='info/', null=True, blank=True, validators=[validar_tamano_imagen], verbose_name='Imagen')
    loadDate = models.DateTimeField(auto_now_add=True, verbose_name='Creacion')
    updateDate = models.DateTimeField(auto_now=True, verbose_name='Actualizacion')
    description = models.TextField(max_length=300, blank=True, null=True, verbose_name='observaciones')

    class Meta:
        abstract=True
    
    def __str__(self):
        return self.title