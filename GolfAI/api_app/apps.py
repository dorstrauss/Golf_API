from django.apps import AppConfig

class ApiAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api_app'
    verbose_name = "My Application"

    def ready(self):  # the app that being called when we run the server

        return
