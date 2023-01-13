from django.test import TestCase
from api_app.sensors_communication.point import Point
from datetime import datetime

point1 = Point(x=-0.3748147,y=-1.049886,z=-1.795301)
time1 = datetime.strptime("2022-12-19 07:13:02.16", "%Y-%m-%d %H:%M:%S.%f")

point2 = Point(x=-0.3951789,y=-1.049697,z=-1.775126)
time2 = datetime.strptime("2022-12-19 07:13:02.18", "%Y-%m-%d %H:%M:%S.%f")

time_difference = time2 - time1
print(f"time difference: {time_difference}")

velocity, speed = point2.getVelocityAndSpeed(point1,time_difference)
print(speed)




