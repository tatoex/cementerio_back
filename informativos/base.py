from django.db import models

class BaseInformativo(models.Model):
    category = models.CharField(max_length=100, verbose_name='Categoria')
    title = models.CharField(max_length=200, verbose_name='Titulo')
    description = models.TextField(verbose_name='Descripcion breve')
    image = models.ImageField(upload_to='info/', null=True, blank=True, verbose_name='Imagen')
    loadDate = models.DateTimeField(auto_now_add=True, verbose_name='Creacion')
    updateDate = models.DateTimeField(auto_now=True, verbose_name='Actualizacion')
    description = models.TextField(max_length=300, blank=True, null=True, verbose_name='observaciones')

    class Meta:
        abstract=True
    
    def __str__(self):
        return self.title