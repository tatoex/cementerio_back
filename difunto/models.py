from django.db import models
from .base import BaseModelDifunto
from simple_history.models import HistoricalRecords
from django.core.exceptions import ValidationError
from tumba.models import Tumba

# Clase deudo
class Deudo(BaseModelDifunto):
    TIPO_DEUDO_CHOICES = [
        ('Allegado','Familiar cercano'),
        ('Familiar','Miembro de la familia'),
        ('Conocido','Conocido del fallecido'),
    ]
    phoneNumber = models.CharField(max_length=15, verbose_name='telefono')
    email = models.EmailField(verbose_name='email')
    address = models.CharField(default="Quito",max_length=100, blank=True, verbose_name='direccion')
    tipo = models.CharField(default="Conocido",max_length=50, verbose_name='tipo relacion', choices=TIPO_DEUDO_CHOICES)
    history=HistoricalRecords()
    def clean(self):
        # Llama al método clean del modelo base
        super().clean()
        
        # Validación para asegurar la unicidad de idNumber
        if Deudo.objects.filter(idNumber=self.idNumber).exclude(pk=self.pk).exists():
            raise ValidationError(f"El ID {self.idNumber} ya está en uso por otro deudo.")

    class Meta:
        permissions = [
            ("can_view_deudo", "Can view deudo"),
            ("can_edit_deudo", "Can edit deudo"),
        ]

# Clase difunto
class Difunto(BaseModelDifunto):
    requestNumber = models.CharField(max_length=20, unique=True, verbose_name='solicitud')
    history = HistoricalRecords()
    tumba = models.ForeignKey( Tumba, related_name='difuntoTumba',blank=True, on_delete=models.DO_NOTHING, default=6000) 
    deudo = models.ForeignKey(Deudo, related_name='difuntoDeudo',  on_delete=models.DO_NOTHING) 
    def clean(self):
        super().clean()
        if not self.tumba and not hasattr(self, 'cremacion'):  # Validación de tumbas y cremaciones
            raise ValidationError("Debe asociarse una tumba o manejar el difunto de otra forma.")
    
    class Meta:
        permissions = [
            ("can_view_difunto", "Can view difunto"),
            ("can_edit_difunto", "Can edit difunto"),
        ]
