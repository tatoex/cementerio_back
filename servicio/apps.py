from django.apps import AppConfig


class ServicioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'servicio'
    def ready(self):
        import servicio.signals  # Registras las señales de la app 'servicio'