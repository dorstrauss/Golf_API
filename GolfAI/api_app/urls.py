import threading

from django.urls import path

from api_app.views import RegistrationView, LoginView
from api_app.sensors_communication.mqtt_subscriber import start_listening, check_messages_queue

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='user_registration'),
    path('login/', LoginView.as_view(), name='user_login')
]

# i have chosen this location to start the threads because i need them to start when the server is run for the first time, but after all the server components as being loaded
# creating a thread that listen for messages from the sensors, and sarting it
listener_thread = threading.Thread(target=start_listening)
listener_thread.start()

# creating a thread that run every 0.5 seconds and check if there are messages to handle
messages_handler_thread = threading.Thread(target=check_messages_queue)
messages_handler_thread.start()


