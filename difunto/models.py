from django.db import models

# Create difunto
class Difunto(models.Model):
    names = models.CharField( max_length=200, verbose_name='nombres')
    last_names = models.CharField( max_length=200, verbose_name='apellidos')
    idNumber = models.CharField(max_length=10, unique=True, verbose_name='cedula')
    requestNumber = models.CharField(max_length=20, unique=True, verbose_name='solicitud')
    loadDate = models.mDateTimeField(auto_now_add=True, verbose_name='creacion')
    updateDate = models.mDateTimeField(auto_now=True, verbose_name='actualizacion')
    decription = models.TextField(max_length=300, blank=True, null=True, verbose_name='observaciones')
    tumba = models.ForeignKey(Tumba, related_name='difunto', on_delete=models.DO_NOTHING) 
    deudo = models.ForeignKey(Deudo, related_name='difunto', on_delete=models.DO_NOTHING) 

# Create deudo
class Deudo(models.Model):
    names = models.CharField( max_length=200, verbose_name='nombres')
    last_names = models.CharField( max_length=200, verbose_name='apellidos')
    idNumber = models.CharField(max_length=10, verbose_name='cedula')
    phoneNumber = models.CharField(max_length=15, verbose_name='telefono')
    email = models.EmailField( verbose_name='email')
    address = models.CharField(max_length=100, blank=True, null=True, verbose_name='direccion')
    loadDate = models.mDateTimeField(auto_now_add=True, verbose_name='creacion')
    updateDate = models.mDateTimeField(auto_now=True, verbose_name='actualizacion')
    decription = models.TextField(max_length=300, blank=True, null=True, verbose_name='observaciones')

