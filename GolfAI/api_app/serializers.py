from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework.authtoken.models import Token
from rest_framework import serializers

from api_app.models import Player

class PlayerSerializer(serializers.ModelSerializer):

    height = serializers.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(250)])
    handicap = serializers.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(28)])
    sensor_id = serializers.CharField(max_length=25, required=True, validators=[UniqueValidator(queryset=Player.objects.all())])

    class Meta:
        model = Player
        exclude = ['user']  # excluding the user field because it already populated when the user instance was created


# class serializer that handel the data from user registration
class RegisterSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])  # making sure that the email that the user entered have not being used by another user
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])  # checking that the password is valid
    password2 = serializers.CharField(write_only=True, required=True)  #write_only means that the field data will ne used only when writing to the databese, it will not be showen in the serializer object because it contains sensetive information
    player = PlayerSerializer()  # we are using a nested serializer as a field

    class Meta:  # nested class that gives the serializer details
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'password2', 'player')

    # overriding the built-in validation method of the model serializer
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:  # if the 2 passwords on the form don't match
            raise serializers.ValidationError({'password': "passwords don't match!"})  # raising an error
        return attrs

    # overriding the built-in create method
    def create(self, validated_data):
        # creating a user instance with the data came from the registration
        player = validated_data.pop('player')
        user = User(username=validated_data['email'], first_name=validated_data['first_name'], last_name=validated_data['last_name'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        user.player.sensor_id = player['sensor_id']
        user.player.height = player['height']
        user.player.handicap = player['handicap']
        user.player.save()
        token = Token.objects.create(user=user)  # creating a unique token for that user to use when he is signing in
        token.save()  # saving the token to the database
        return user

