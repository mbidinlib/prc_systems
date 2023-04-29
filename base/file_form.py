from .models import Datasets
from django.forms import ModelForm

class FileForm(ModelForm):
    class Meta:
        model = Datasets
        fields = ["file", "name"]
        labels = {'file': "Select data file", "name": "Name (opt) "}
        # help_texts = {'name': "Opt",}
