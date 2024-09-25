from django.db import models

# modelo lote
class Lote (models.Model):
    name=models.CharField(max_length=3, verbose_name="lote")
    decription=models.TextField(max_length=300, blank=True, null=True, verbose_name="lugar")
    loadDate=models.mDateTimeField(auto_now_add=True)
    updateDate=models.mDateTimeField(auto_now=True)

class Tumba (models.Model):
    TIPO_NICHO_CHOICES[
        ('T','Tumba de tierra'),
        ('E','Tumba extramuros'),
    ]
    numero=models.IntegerField(max_length=4)
    decription=models.TextField(max_length=300, blank=True, null=True, verbose_name="pocision")
    tipo_nicho=models.CharField(max_length=2, choices= TIPO_NICHO_CHOICES)
    loadDate=models.mDateTimeField(auto_now_add=True)
    updateDate=models.mDateTimeField(auto_now=True)
    name=models.ForeignKey(Lote, on_delete=models.CASCADE) 

class DisponibleTumba (models.Model):
    startDate=models.DateTimeField()
    endDate=models.DateTimeField()
    loadDate=models.mDateTimeField(auto_now_add=True)
    updateDate=models.mDateTimeField(auto_now=True)
    decription=models.TextField(max_length=300, blank=True, null=True, verbose_name="observaciones")
