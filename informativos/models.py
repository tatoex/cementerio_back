from django.db import models
from django.utils.timezone import now
from simple_history.models import HistoricalRecords
from .base import BaseInformativo
# Create your models here.
nada="N/A"
class Articulo(BaseInformativo):
    references = models.TextField(default=nada,blank=True , verbose_name='Referencias')
    external_source = models.URLField( default="https://www.google.com.ec/?hl=es",blank=True,verbose_name='Fuentes externas')
    publication_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de publicacion')
    author = models.CharField(max_length=100, verbose_name='Autor')
    is_featured = models.BooleanField(default= False, verbose_name='Noticia destacada')
    history = HistoricalRecords()
    class Meta:
        permissions = [
                ("can_view_articulo", "Can view articulo"),
                ("can_edit_articulo", "Can edit articulo"),
            ]

class Guia(BaseInformativo):
    steps =models.TextField(default=nada,blank=True , verbose_name='Pasos a seguir')
    aditional_resources = models.URLField(default="https://www.google.com.ec/?hl=es", blank=True,verbose_name='Recursos adicionales')
    history = HistoricalRecords()
    class Meta:
        permissions = [
                ("can_view_guia", "Can view guia"),
                ("can_edit_guia", "Can edit guia"),
            ]

class ServicioInfo(BaseInformativo):
    features = models.TextField( verbose_name='Caracteristicas incluidas')
    exclusions = models.TextField( default=nada, blank=True, verbose_name='Exclusiones')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, verbose_name='Precio', default=0.0)
    history = HistoricalRecords()
    class Meta:
        permissions = [
                ("can_view_servicioInfo", "Can view servicioInfo"),
                ("can_edit_servicioInfo", "Can edit servicioInfo"),
            ]
    
class SeccionArticulo(models.Model):
    subtitle = models.CharField(max_length=200, verbose_name='Subtitulo', blank=True,)
    content = models.TextField( verbose_name='contenido',  blank=True,)
    loadDate = models.DateTimeField(auto_now_add=True, blank=True, null=True,verbose_name='Creacion')
    updateDate = models.DateTimeField(auto_now=True, blank=True,null=True, verbose_name='Actualizacion')
    description = models.TextField(max_length=300, blank=True, default=nada, verbose_name='observaciones')
    article = models.ForeignKey(Articulo, related_name='seccionArticulo', on_delete=models.CASCADE)
    history = HistoricalRecords()

    class Meta:
        permissions = [
                ("can_view_deudo", "Can view deudo"),
                ("can_edit_deudo", "Can edit deudo"),
            ]