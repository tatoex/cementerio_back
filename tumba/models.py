from django.db import models

# modelo lote
class Lote (models.Model):
    blockName = models.CharField(max_length=3, verbose_name='lote')
    decription = models.TextField(max_length=300, blank=True, null=True, verbose_name='lugar')
    loadDate = models.DateTimeField(auto_now_add=True, verbose_name='creacion')
    updateDate = models.DateTimeField(auto_now=True, verbose_name='actualizacion')

# modelo tumba
class Tumba (models.Model):
    TIPO_NICHO_CHOICES[
        ('T','Tumba de tierra'),
        ('E','Tumba extramuros'),
    ]
    nicheNumber = models.IntegerField(max_length=4, verbose_name='tumba')
    decription = models.TextField(max_length=300, blank=True, null=True, verbose_name='pocision')
    nicheType = models.CharField(max_length=2, choices= TIPO_NICHO_CHOICES, verbose_name='tipo')
    loadDate = models.DateTimeField(auto_now_add=True, verbose_name='creacion')
    updateDate = models.DateTimeField(auto_now=True, verbose_name='actualizacion')
    nameLote = models.ForeignKey(Lote, related_name='tumbaLote', on_delete=models.CASCADE) 

# modelo Disponibilidad
class DisponibleTumba (models.Model):
    startDate = models.DateTimeField(verbose_name='inicio')
    endDate = models.DateTimeField(verbose_name='vence')
    loadDate = models.DateTimeField(auto_now_add=True, verbose_name='creacion')
    updateDate = models.DateTimeField(auto_now=True, verbose_name='actualizacion')
    decription = models.TextField(max_length=300, blank=True, null=True, verbose_name='observaciones')
    numberTumba = models.ForeignKey(Tumba, related_name='disponibleTumba', on_delete=models.DO_NOTHING) 
