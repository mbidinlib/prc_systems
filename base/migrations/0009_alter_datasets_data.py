# Generated by Django 3.2 on 2023-04-29 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_datasets_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasets',
            name='data',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
