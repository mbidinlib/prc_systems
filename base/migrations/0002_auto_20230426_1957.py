# Generated by Django 3.2 on 2023-04-27 00:57

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datasets',
            name='data',
        ),
        migrations.RemoveField(
            model_name='datasets',
            name='uploaded',
        ),
        migrations.AddField(
            model_name='datasets',
            name='file',
            field=models.FileField(null=True, upload_to=base.models.user_dir_path),
        ),
    ]
