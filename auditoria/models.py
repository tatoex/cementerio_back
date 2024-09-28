from django.db import models
from django.contrib.auth.models import User

class Auditoria(models.Model):
    ACCION_CHOICES = [
        ('CREAR','Creación'),
        ('MODIFICAR','modificación'),
        ('BORRAR','Eliminación'),
    ]
    afectado=models.CharField (max_length=210)
    objecto_id=models.IntegerField()
    accion=models.CharField(max_length=10, choice=ACCION_CHOICES)
    descripcion_cambios=models.TextField(blank=True, null=True)
    usuario=models.ForeignKey(User, verbose_name=_("auditoriaUsuario"), on_delete=models.SET_NULL)
