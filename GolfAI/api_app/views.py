from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import permissions
from rest_framework import generics
from .serializers import *
from rest_framework.response import Response

# Create your views here.
class RegistrationView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]  #the client interact with this view before he been authorizied, so we need to say specificaly that this view is for everyone
    queryset = User.objects.all()
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
