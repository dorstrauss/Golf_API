from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

import pyowm
from django.http import JsonResponse

from api_app.models import User, Swing
from api_app.serializers import RegisterSerializer, SwingsSerializer

class RegistrationView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]  #the client interact with this view before he been authorizied, so we need to say specificaly that this view is for everyone
    queryset = User.objects.all()  # all the relevant data from the database that we are going to work with
    serializer_class = RegisterSerializer

class LoginView(ObtainAuthToken):

    #overriding the ObtainAuthToken class post method
    def post(self, request, *args, **kwargs):  # method that gets a post request with the user's login data

        serializer = self.serializer_class(data=request.data, context={'request': request})  # the ObtainAuthToken class built-in serializer that checks if the user exists in the database base on the username (email) and password provided in the request
        serializer.is_valid(raise_exception=True)  # if the serializer finds that the data provided in the request is not valid he raise an exception
        user = serializer.validated_data['user']  # getting the user with this username (email) and password
        username = user.username
        token = Token.objects.get(user=user)  # getting the token associated with this user
        return Response({  # if the login is successful we are returning the username and token to the frontend
            'username': username,
            'token': token.key
        })


# the view that will get username and it's token and will return a list of all the swings of the user
class GetSwingsView(APIView):
    
    #permission_classes = [permissions.IsAuthenticated]  # using the built-in IsAuthenticated class that gets the token assosiated with the user

    def get(self, request):
        swings = Swing.objects.filter(username=request.user)  # getting the user's swings from the database (the IsAuthenticated class provide the user with the assosiated token we got)
        serialized_swings = SwingsSerializer(swings, many=True)  # passing the swings queryset to the serializer, and configaring the serializer to handel a queryset of multiple objects
        return Response(serialized_swings.data)

class GetWind(APIView):

    def get(self, request, latitude, longitude):

        owm = pyowm.OWM('5b94cff5fb780b9f0680204791c9626d')  # creating a owm instance with our api key, with this instance we can get the weather data from pyowm

        # getting the wing data in the coordinates we got
        weather_manager = owm.weather_manager()
        observation = weather_manager.weather_at_coords(float(latitude), float(longitude))
        weather = observation.weather
        wind = weather.wind()
        wind_speed = wind['speed']
        wind_direction = wind['deg']

        return JsonResponse({'wind_speed':wind_speed, 'wind_direction':wind_direction})  # returning the wind data as json

