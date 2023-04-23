# Create models using classes . These are the databases for the project
# Whenever models are created or updated, migrations need to be run.


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
    
    # Create a manay to many to many relationship
    # Blank=True allows the user to create a new room with no participants
    participants = models.ManyToManyField(User, related_name='participants', blank = True)       
    
    update = models.DateField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    # The class below orders the rooms in a descending order. Remove - to get ascending order
    # It automatically orders everythin in the room
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
    
    # The sub-class below orders the messages in a room in a descending order. Remove - to get ascending order
    class Meta:
        ordering = ['-update', '-created'] 
