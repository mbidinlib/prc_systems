# Generated by Django 3.2 on 2023-04-28 02:44

import base.file_validation
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_datasets_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasets',
            name='file',
            field=models.FileField(null=True, upload_to='uploads', validators=[base.file_validation.validate_file_extension]),
        ),
    ]
