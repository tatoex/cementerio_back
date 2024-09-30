from django.apps import AppConfig


class TumbaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tumba'

    def ready(self):
        import tumba.signals