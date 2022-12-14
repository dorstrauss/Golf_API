import json

from paho.mqtt import client
from random import uniform
from datetime import datetime
from json import dumps

mqtt_broker = "mqtt.eclipseprojects.io"  # the address of our broker
receiver = client.Client("demo_sensor")  # creating the subscriber client
receiver.connect(mqtt_broker)

i = 0
while i < 10:
    x_position = uniform(0,10)
    y_position = uniform(0, 10)
    z_position = uniform(0, 10)
    time = datetime.now()
    position_data = {"X":x_position, "Y":y_position,"Z":z_position, "TIME": str(time)}
    json_data = json.dumps(position_data, indent=4)
    receiver.publish("POSITION", json_data)
    print("published: " + str(position_data))
    i = i + 1
