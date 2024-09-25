from .utils import BaseModelTumba

# modelo lote
class Lote (BaseModelTumba):
    blockName = models.CharField(max_length=3, verbose_name='lote')

# modelo tumba
class Tumba (BaseModelTumba):
    TIPO_NICHO_CHOICES[
        ('T','Tumba de tierra'),
        ('E','Tumba extramuros'),
    ]
    nicheNumber = models.IntegerField(max_length=4, verbose_name='tumba')
    nicheType = models.CharField(max_length=2, choices= TIPO_NICHO_CHOICES, verbose_name='tipo')
    nameLote = models.ForeignKey(Lote, related_name='tumbaLote', on_delete=models.CASCADE) 

# modelo Disponibilidad
class DisponibleTumba (BaseModelTumba):
    startDate = models.DateTimeField(verbose_name='inicio')
    endDate = models.DateTimeField(verbose_name='vence')
    numberTumba = models.ForeignKey(Tumba, related_name='disponibleTumba', on_delete=models.DO_NOTHING) 
