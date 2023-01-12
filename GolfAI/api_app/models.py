from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import *

# This model extend the basic built-in User model, by adding additional information on the uesr like
# handicap score anf height.
class Player(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)  # connecting this model to the User model
    # (cascade means when deleting a user row in the user table
    # the match row in this table will automatically will be deleted)
    handicap = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(28)])
    height = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(250)])
    sensor_id = models.CharField(unique=True, max_length=25, default="")  #the id of the sensor of the player must be unique
    registration_date = models.DateTimeField(default=datetime.now())

    #a listener that listen to the User model, if a new user as been save, it creates a new row in the player model with the new user in the user field
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:  # if a new user created in the User model
            Player.objects.create(user=instance)  # creating a new row in player, inserting the new user instance to the user field

    def __str__(self):
        return self.user.username

class Swing(models.Model):

    username = models.ForeignKey(User, on_delete=models.CASCADE)  # username is a foreign key of the model User
    time = models.DateTimeField(default=datetime.now())
    x_velocity = models.FloatField(default=0)
    y_velocity = models.FloatField(default=0)
    z_velocity = models.FloatField(default=0)
    swing_speed = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(500)])
    #shaft = models.CharField(choices=[('STIFF','Stiff'), ('REGULAR','Regular'), ('FLEX', 'Flex')], max_length=7)
    #weight_in_grams = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5000)])
    #club_type = models.CharField(choices=[('WOOD','Wood'), ('IRON','Iron')], max_length=4)

    class Meta:
        constraints = [  # making the combination of username & time the model's primary key
            models.UniqueConstraint(
                fields=['username', 'time'], name='unique_migration_username_time'
            )
        ]
