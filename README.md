<img width="374" alt="Golf-Analyticis logo" src="https://user-images.githubusercontent.com/97314875/209589890-03502a09-68ef-43e2-aba5-22dd545273da.png">

# Golf-Analytics backend API
The back-end API of the web application "Golf-Analytics".

## What
This is the backend API of "Golf-Analytics" which is an App that uses a sensor to improve professional golf players performance on the field.

## How
Physically the player put our sensor on his club, login to the app, swings, the app gets the swing data of the player, analyzes it, and gives back the speed, angle, approximate distance and even recommends for the best golf club type for him.

Software: I used Django to build a REST API.
I used the built-in views and serializers to create the APIs end-points.
I used Django built-in models to create & handle the application databases.
I used Tokens to form a strong users authentication. 
I used MQTT protocol combined with threads to handle the communication with the sensor.

## Why
Our mission is to develop a low-cost kit that will drastically increase players performances on the field.

## Structure
Inside the "Golf_API" directory there is a directory called "GolfAI" this is the main project directory. Inside this directory there are two importent directories, "api_app" which is the app for all the API functionality, and "GolfAI" which is the django project directory.

![image](https://user-images.githubusercontent.com/97314875/215344898-22b7b3da-0743-419d-9397-729cdda8c4c7.png)


