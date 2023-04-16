from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


# This class creates a Room model(table head) with the various variables
class Room(models.Model):
    host=models.ForeignKey(User, on_delete=models.SET_NULL, null =True)
    topic=models.ForeignKey(Topic, on_delete=models.SET_NULL, null =True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    #participants = models.
    update = models.DateField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    # The class below orders the rooms in a descending order. Remove - to get ascending order
    class Meta:
        ordering = ['-update', '-created'] 
    
    def __str__(self):
        return self.name
    
# A class that create the message  model
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room =  models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    update = models.DateField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]