from .models import Datasets
from django.forms import ModelForm

class FileForm(ModelForm):
    class Meta:
        model = Datasets
        fields = '__all__'
