# Generated by Django 3.2 on 2023-04-29 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_datasets_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasets',
            name='data',
            field=models.JSONField(default=[{'0'}], null=True),
        ),
    ]
