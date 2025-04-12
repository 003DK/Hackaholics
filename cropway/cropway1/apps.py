from django.apps import AppConfig

class Cropway1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cropway1'

    def ready(self):
        # Import here to avoid "Apps aren't loaded yet" error
        from .models import Crop
        # Optional: do something with Crop if needed
