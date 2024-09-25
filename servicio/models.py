from .utils import BaseModelServicio
from tumba.models import Tumba
from difunto.models import Difunto

# Create your models here.
class Servicio(BaseModelServicio):
    startDate = models.DateTimeField(verbose_name='inicio')
    endDate = models.DateTimeField(null=True, blank=True, verbose_name='vecimiento')
    numberTomb = models.ForeignKey(Tumba, related_name='servicioTumba', on_delete=models.DO_NOTHING) 
    deceased = models.ForeignKey(Difunto, related_name='servicioDifunto', on_delete=models.DO_NOTHING) 
    
class Ceremonia(BaseModelServicio):
        TIPO_CEREMONIA_CHOICES[
        ('Cremacion','Cremación'),
        ('Inhumacion','Inhumación'),
        ('Exhumacion','Exhumación'),
    ]
    name = models.CharField(max_length=50, choices=TIPO_CEREMONIA_CHOICES, verbose_name='tipo')
    date = models.DateTimeField(verbose_name='fecha')
    servicios = models.ForeignKey(Servicio, related_name='ceremoniaServicio', on_delete=models.CASCADE) 
