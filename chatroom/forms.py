from django.forms import ModelForm
from .models import Room

# Class that uses the ModelForm method to create a form that looks like the Rome model

class RoomForm(ModelForm):
    class Meta:
        model = Room        # creates a form after the Room model
        fields = '__all__'