# Generated by Django 3.2 on 2023-04-28 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_datasets_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasets',
            name='file',
            field=models.FileField(null=True, upload_to='media/uploads/'),
        ),
    ]
