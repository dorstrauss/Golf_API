import time
from time import sleep
from paho.mqtt import client


# function that will be activated every time the subscriber get a message from the broker
def on_message(receiver, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))

# function that start listening to the POSITION topic
def start_listening():
    mqtt_broker = "mqtt.eclipseprojects.io"  # the address of our broker
    receiver = client.Client("App_receiver")  # creating the subscriber client
    receiver.connect(mqtt_broker)

    receiver.loop_start()
    receiver.subscribe("POSITION")
    receiver.on_message = on_message
    print("Started listening")
    time.sleep(30)
    receiver.loop_stop()
    print("Finished listening")
