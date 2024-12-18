from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    AREA_CHOICES = [
        ('correccion_datos', 'Corrección de Datos'),
        ('soporte', 'Soporte Técnico'),
        ('paquetes', 'Información de Paquetes'),
    ]

    area = models.CharField(max_length=50, choices=AREA_CHOICES)  # Clasificación de la solicitud
    name = models.CharField(max_length=100)                      # Nombre del deudo
    contact_number = models.CharField(max_length=15)             # Teléfono del deudo
    email = models.EmailField(blank=True)             # Correo del deudo (opcional)
    message = models.TextField()                                 # Mensaje de la solicitud
    is_attended = models.BooleanField(default=False)             # Estado de atención
    attended_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True,null=True, related_name='attended_notifications')  # Usuario que atendió la notificación (opcional)
    created_at = models.DateTimeField(auto_now_add=True)         # Fecha de creación
    attended_at = models.DateTimeField(auto_now=True, blank=True)    # Fecha de atención (opcional)

    def __str__(self):
        return f"{self.area} - {self.name} - {'Atendido' if self.is_attended else 'Pendiente'}"