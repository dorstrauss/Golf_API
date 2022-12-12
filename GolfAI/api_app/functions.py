from models import Swing


def save_swing_data(swing_data):

    username= swing_data['username']
    time = swing_data['time']
    swing_speed = swing_data['speed']
    shaft = swing_data['shaft']
    weight_in_grams = swing_data['weight']
    club_type = swing_data['type']

    # creating a Swing object with the data we got to the function
    swing = Swing(username=username, time=time, swing_speed=swing_speed, shaft=shaft, weight_in_grams=weight_in_grams, club_type=club_type)
    swing.save()  # saving the new row to the table in the database
