from django.db import models
from simple_history.models import HistoricalRecords
from .base import BaseObituario
from difunto.models import Difunto
from servicio.models import Ceremonia

# Create your models here.
class Obituario(BaseObituario):
    obituary_detail = models.TextField(verbose_name='Detalle del difunto')
    cementery = models.CharField(max_length=200, null=True, blank=True, verbose_name='lugar de la ceremonia')
    place = models.CharField(max_length=200, null=True, blank=True, verbose_name='lugar de la ceremonia')
    history = HistoricalRecords()
    deceased = models.OneToOneField(Difunto, related_name='obituarioDifunto', on_delete=models.CASCADE)

    def __str__(self):
        return f"Obituario de {self.deceased.names} {self.deceased.last_names}"
    
class Memoria(BaseObituario):
    names = models.CharField(max_length=200, verbose_name='Nombre autor')
    relationship = models.CharField(max_length=200, null=True, blank=True, verbose_name='Relacion con el difunto')
    text = models.TextField(verbose_name='Recuerdo')
    image = models.ImageField(upload_to='memories/', null=True, blank=True, verbose_name='Imagen opcional')
    history = HistoricalRecords()
    obituary = models.ForeignKey(Obituario, related_name='memoriaObituario', on_delete=models.CASCADE)

    def __str__(self):
        return f"Recuerdo de {self.names} para {self.obituary.deceased.names} {self.obituary.deceased.last_names}"
    
class EtapasObituario(BaseObituario):
    ETAPAS_OBITUARIO_CHOICES = [
        ('Velacion','Velación'),
        ('Misa','Misa'),
        ('Recepcion','Recepción'),
        ('Entrega_cenizas','Entrega de las cenizas'),
        ('Lectura_recuerdos','Lectura de recuerdos'),
        ('Celebracion_vida','Celebración de vida'),
    ]
    stage_type = models.CharField( max_length=100, choices=ETAPAS_OBITUARIO_CHOICES, verbose_name='Etapas de las ceremonias')
    place = models.CharField(max_length=200, null=True, blank=True, verbose_name='lugar de la ceremonia')
    history = HistoricalRecords()
    obituary = models.ForeignKey(Obituario, related_name='etapasObituario', on_delete=models.CASCADE)
    ceremony = models.ForeignKey(Ceremonia, related_name='etapasCeremonia', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.stage_type} en {self.place} para {self.obituary.deceased.names} {self.obituary.deceased.last_names}"