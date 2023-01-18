from datetime import datetime
import time
import queue

import json
from paho.mqtt import client

from api_app.models import Player, Swing
from api_app.sensors_communication.point import Point

messages_queue = queue.Queue()  # the queue that the coming messages will be inserted to
messages_checking_interval = 0.5  #the interval which we check the messages queue
temporary_swings_container = {}  # declaring the dict that will hold the dictionaries position data of each swing (dictionary of dictionaries)


# function that will be activated every time the subscriber get a message from the broker
def on_message(receiver, userdata, message):
    decoded_message = json.loads(message.payload)
    messages_queue.put(decoded_message)  # adding the new message to the queue
    print("Received message: ", str(message.payload.decode("utf-8")))



# function that start listening to the POSITION topic
def start_listening():
    mqtt_broker = "mqtt.eclipseprojects.io"  # the address of our broker
    receiver = client.Client("App_receiver")  # creating the subscriber client
    receiver.connect(mqtt_broker)

    #temporary_swings_data = {}  # declaring the dict that will hold the sorted dictionaries position data of each swing
    print("Started listening")
    receiver.subscribe("POSITION", qos=0)
    receiver.on_message = on_message
    receiver.loop_forever()

# a function that runs every 0.5 seconds and check if there are messages to handle in the messages queue
def check_messages_queue():

    #print(f"Started checking queue every {messages_checking_interval} seconds")
    #print("The queue state is: ", messages_queue)
    while True:  # a loop that run forever and iterate every 0.5 seconds
        #print("Checking for messages in the queue..")
        while not messages_queue.empty():  # if the messages queue is not empty
            message = messages_queue.get()  # getting the first message of the queue (a dictionary that holds the data)
            #print("Handel message: ", message)
            handle_swing_massage(message)


        time.sleep(messages_checking_interval)


# function that gets the messages received by the subscriber validate and save them to the relevant dict
def handle_swing_massage(massage):
    #decoded_massage = massage.payload.decode("utf-8")
    sensor_id = massage["SENSOR_ID"]
    if Player.objects.filter(sensor_id=sensor_id).exists():  # if the sensor is register in the database
        swing_id = massage["SWING_ID"]
        message_time = massage["TIME"]  # getting the time of this swing
        if swing_id in temporary_swings_container.keys():  # if this swing already has a dictionary for the swing data in the swings dictionary
            container = temporary_swings_container[swing_id]  # getting the dictionary of this swing
            container[message_time] = massage  # adding the message data to the dictionary, the time as the key and the all message as the value
        else:  # if this is the first massage of this swing
            temporary_swings_container[swing_id] = {}  # creating a new dictionary that will contain all this swing messages
            container = temporary_swings_container[swing_id]  # getting the new dictionary
            container[message_time] = massage  # adding the message data to the dictionary, the time as the key and the all message as the value

        if massage['NOTE'] == 'end':  # if this is the last message of this swing we call the function that run over the messages of the swing, calculate the speed and save it to the database
            analyze_swing_data(container, sensor_id)  # analyzing and saving the swing data
            del temporary_swings_container[swing_id]  # deleting the swing data after analyzing it
    else:
        print(f"Sensor {sensor_id} is not register in the database!")


# function that gets the data of the swing, analyze the swings max speed,
# velocity and save it to the database
def analyze_swing_data(swing_data_container: {}, sensor_id: str):
    swing_max_speed = 0
    max_velocity_time = None
    previous_point = None  # flag to identify the first point in the loop
    previous_time = None
    for key in swing_data_container:  # going over the different positions and calculating the velocity in each one
        data = swing_data_container[key]
        current_point = Point(data['X'], data['Y'], data['Z'])  # creating a 3-D point that represent the current point
        if previous_point is None:  # if this is the first point
            previous_point = current_point
            previous_time = datetime.strptime(data['TIME'], "%Y-%m-%d %H:%M:%S.%f%z")
        else:  # if this not the first pont
            current_time = datetime.strptime(data['TIME'], "%Y-%m-%d %H:%M:%S.%f%z")
            time_difference = current_time - previous_time
            current_velocity, current_speed = current_point.getVelocityAndSpeed(previous_point, time_difference)  # calculating the velocity between the current point and the previous point

            if swing_max_speed < current_speed:
                swing_max_speed = current_speed
                max_speed_velocity = current_velocity
                max_velocity_time = data['TIME']
                previous_point = current_point
                previous_time = current_time
            else:
                previous_point = current_point
                previous_time = current_time

    # saving tha swing analyzed data to the database
    swing_username = Player.objects.filter(sensor_id=sensor_id).first().user

    x_velocity = max_speed_velocity['X_VELOCITY']
    y_velocity = max_speed_velocity['Y_VELOCITY']
    z_velocity = max_speed_velocity['Z_VELOCITY']

    swing = Swing(username=swing_username, time=max_velocity_time, x_velocity=x_velocity, y_velocity=y_velocity, z_velocity=z_velocity, swing_speed=swing_max_speed)
    swing.save()