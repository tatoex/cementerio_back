from django.db import models
from simple_history.models import HistoricalRecords
from .base import BaseObituario
from difunto.models import Difunto
from servicio.models import Servicio
from django.core.exceptions import ValidationError
from django.utils.timezone import now

nadaa="N/A"
def validar_tamano_imagen(image):
    max_tamano = 2 * 1024 * 1024  # Limita a 2MB
    if image.size > max_tamano:
        raise ValidationError("El tamaño máximo permitido es 2MB.")

# Create your models here.
class Obituario(BaseObituario):
    obituary_detail = models.TextField(verbose_name='Detalle del obituario')
    cementery = models.CharField(max_length=200, default=nadaa,  blank=True, verbose_name='cemeterio')
    place = models.CharField(max_length=200, default=nadaa, blank=True, verbose_name='lugar de la ceremonia')
    name = models.CharField(max_length=200, default=nadaa, blank=True, verbose_name='homenajeado')
    deceased = models.OneToOneField(Difunto, related_name='obituarioDifunto', on_delete=models.CASCADE)
    image_dif = models.ImageField(upload_to='obituario/', default=nadaa,  blank=True, validators=[validar_tamano_imagen], verbose_name='Imagen opcional')
    date_dead=models.DateTimeField(blank=True, default=now, verbose_name='fecha de fallecimiento')
    date_born=models.DateTimeField(blank=True, default=now, verbose_name='fecha de nacimiento')
    history = HistoricalRecords()
    
    class Meta:
        permissions = [
                ("can_view_obituario", "Can view obituario"),
                ("can_edit_obituario", "Can edit obituario"),
            ]
    def __str__(self):
        return f"Obituario de {self.deceased.names} {self.deceased.last_names}"
    
class Memoria(BaseObituario):
    names = models.CharField(max_length=200, verbose_name='Nombre autor')
    relationship = models.CharField(max_length=200, default=nadaa, blank=True, verbose_name='Relacion con el difunto')
    text = models.TextField(verbose_name='Recuerdo')
    image = models.ImageField(upload_to='memories/', default=nadaa,  blank=True, validators=[validar_tamano_imagen], verbose_name='Imagen opcional')
    history = HistoricalRecords()
    obituary = models.ForeignKey(Obituario, related_name='memoriaObituario', on_delete=models.CASCADE)
    class Meta:
        permissions = [
                ("can_view_memoria", "Can view memoria"),
                ("can_edit_memoria", "Can edit memoria"),
            ]
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
    stage_ceremony = models.CharField( max_length=100, choices=ETAPAS_OBITUARIO_CHOICES, verbose_name='Etapas de las ceremonias')
    place = models.CharField(max_length=200, default=nadaa, blank=True, verbose_name='lugar de la ceremonia')
    history = HistoricalRecords()
    obituary = models.ForeignKey(Obituario, related_name='etapasObituario', on_delete=models.CASCADE)
    ceremony = models.ForeignKey(Servicio, related_name='etapasCeremonia', on_delete=models.CASCADE)
    class Meta:
        permissions = [
                ("can_view_etapasObituario", "Can view etapasObituario"),
                ("can_edit_etapasObituario", "Can edit etapasObituario"),
            ]
    def __str__(self):
        return f"{self.stage_ceremony} en {self.place} para {self.obituary.deceased.names} {self.obituary.deceased.last_names}"