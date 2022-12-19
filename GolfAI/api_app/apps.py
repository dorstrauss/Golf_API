from django.apps import AppConfig
from .sensors_communication.mqtt_subscriber import start_listening



class ApiAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api_app'
    verbose_name = "My Application"
    def ready(self):  # the app that being called when we run the server

       start_listening()  # calling the function that start listening to the POSITION topic

