# class that represent a 3-D point
import math


class Point:

    def __init__(self, x, y, z):  # constructor
        self.x = x
        self.y = y
        self.z = z

    # function that calculate the velocity between this point and the point we got as a argument and return the velocity vector
    def getVelocityAndSpeed(self, start_point, time_difference):
        x_difference = start_point.x - self.x
        y_difference = start_point.y - self.y
        z_difference = start_point.z - self.z
        #print(f"x difference: {x_difference} y difference: {y_difference} z difference: {z_difference}")

        time_difference = time_difference.total_seconds()  # converting the time difference from dateTime object to float

        x_velocity = x_difference / time_difference
        y_velocity = y_difference / time_difference
        z_velocity = z_difference / time_difference

        velocity = {'X_VELOCITY': x_velocity, 'Y_VELOCITY': y_velocity, 'Z_VELOCITY': z_velocity}

        distance = math.sqrt(x_difference**2 + y_difference**2 + z_difference**2)  # calculating the distance between the points
        speed = distance/time_difference
        return velocity, speed


