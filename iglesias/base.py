from django.db import models

class BaseIglesia(models.Model):
    description = models.TextField(null=True, blank=True, verbose_name='Description breve')
    image=models.ImageField(upload_to='iglesias/', null=True, blank=True, verbose_name='Foto')
    loadDate = models.DateTimeField(auto_now_add=True, verbose_name='Creacion')
    updateDate = models.DateTimeField(auto_now=True, verbose_name='Actualizacion')
    

    class Meta:
        abstract=True

    def __str__(self):
        return self.name