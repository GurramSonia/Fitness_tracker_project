from django.apps import AppConfig


class RegistrationAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'registration_app'
def ready(self):
    import registration_app.signals
