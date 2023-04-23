from django.contrib import admin

# Import all defined models and 
# Register your models here. 
# Without this, you won't see the models in the admin page

from .models import Room, Topic, Message


admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)

