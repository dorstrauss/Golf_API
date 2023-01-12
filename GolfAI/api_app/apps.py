from django.apps import AppConfig
#from api_app.sensors_communication.mqtt_subscriber import start_listening
#import threading



class ApiAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api_app'
    verbose_name = "My Application"

    def ready(self):  # the app that being called when we run the server

        return
