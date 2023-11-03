from django.apps import AppConfig


class CollectionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'collection'
    def ready(self):
        import collection.signals  # Asegúrate de que las señales se carguen cuando la aplicación esté lista