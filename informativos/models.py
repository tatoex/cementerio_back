from django.db import models
from simple_history.models import HistoricalRecords
from .base import BaseInformativo
# Create your models here.

class Articulo(BaseInformativo):
    references = models.TextField(blank=True ,null=True, verbose_name='Referencias')
    external_source = models.URLField(null=True, blank=True,verbose_name='Fuentes externas')
    publication_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de publicacion')
    author = models.CharField(max_length=100, verbose_name='Autor')
    is_featured = models.BooleanField(default= False, verbose_name='Noticia destacada')
    history = HistoricalRecords()

class Guia(BaseInformativo):
    steps =models.TextField(blank=True ,null=True, verbose_name='Pasos a seguir')
    aditional_resources = models.URLField(null=True, blank=True,verbose_name='Recursos adicionales')
    history = HistoricalRecords()

class ServicioInfo(BaseInformativo):
    features = models.TextField( verbose_name='Caracteristicas incluidas')
    exclusions = models.TextField( null=True, blank=True, verbose_name='Exclusiones')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Precio')
    history = HistoricalRecords()
    
class SeccionArticulo(models.Model):
    subtitle = models.CharField(max_length=200, verbose_name='Subtitulo')
    content = models.TextField( verbose_name='Pasos a seguir')
    loadDate = models.DateTimeField(auto_now_add=True,blank=True, null=True,  verbose_name='Creacion')
    updateDate = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='Actualizacion')
    description = models.TextField(max_length=300, blank=True, null=True, verbose_name='observaciones')
    article = models.ForeignKey(Articulo, related_name='seccionArticulo', on_delete=models.CASCADE)
    history = HistoricalRecords()
    
    def __str__(self):
        return self.title