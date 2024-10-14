from django.db import models
from simple_history.models import HistoricalRecords
from .base import BaseIglesia

class Parroquia(BaseIglesia):
    name=models.CharField(max_length=100, verbose_name='nombre')
    churches_number = models.PositiveIntegerField(default=0, verbose_name='Numero de iglesias')
    history = HistoricalRecords()
    class Meta:
        permissions = [
                ("can_view_parroquia", "Can view parroquia"),
                ("can_edit_parroquia", "Can edit parroquia"),
            ]

class Iglesia(BaseIglesia):
    name=models.CharField(max_length=100, verbose_name='nombre')
    address = models.CharField(max_length=200, null=True, blank=True, verbose_name='Direccion')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='latitud')
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='longitud')
    phone = models.CharField(max_length=15, null=True, blank=True, verbose_name='Telefono')
    email = models.EmailField(null=True, blank=True, verbose_name='Email')
    schedule = models.TextField(null=True, blank=True, verbose_name='Horario')
    priest = models.CharField(max_length=100, null=True, blank=True, verbose_name='Sacerdote')
    logo=models.ImageField(upload_to='logo/', null=True, blank=True, verbose_name='Logo')
    history = HistoricalRecords()
    parish = models.ForeignKey(Parroquia, related_name='iglesias', on_delete=models.CASCADE)
    class Meta:
        permissions = [
                ("can_view_iglesia", "Can view iglesia"),
                ("can_edit_iglesia", "Can edit iglesia"),
            ]

    
    @property
    def google_maps_url(self):
        if self.latitude and self.longitude:
            return f"https://www.google.com/maps?q={self.latitude},{self.longitude}"
        return None

class LinkRedSocial(BaseIglesia):
    PLATAFORMAS_CHOICES = [
        ('Twitter','Twitter'),
        ('Facebook','Facebook'),
        ('Instagram','Instagram'),
        ('Youtube','Youtube'),
    ]
    stage_type = models.CharField( max_length=50, choices=PLATAFORMAS_CHOICES, verbose_name='Etapas de las ceremonias')
    history = HistoricalRecords()
    class Meta:
        permissions = [
                ("can_view_linkRedSocial", "Can view linkRedSocial"),
                ("can_edit_linkRedSocial", "Can edit linkRedSocial"),
            ]