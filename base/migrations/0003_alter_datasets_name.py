# Generated by Django 3.2 on 2023-04-27 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20230426_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasets',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
