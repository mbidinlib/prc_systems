from django.db import models
from django.contrib.auth.models import User
from .file_validation import validate_file_extension

# Create your models here.


def user_dir_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    #  return 'user_{0}/{1}'.format(instance.user.id, filename)
    return 'uploads'

 
class Datasets(models.Model):
    name = models.CharField(max_length=200)
    # file = models.FileField(null=True)
    file = models.FileField(upload_to='uploads', null=True, validators=[validate_file_extension])

    def __str__(self):
        return self.name

