# Generated by Django 3.2 on 2023-04-29 04:57

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_datasets_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasets',
            name='data',
            field=models.JSONField(blank=True, default=base.models.default__dict, null=True),
        ),
    ]
