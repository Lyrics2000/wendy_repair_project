# Generated by Django 3.1 on 2021-01-16 15:51

from django.db import migrations, models
import mainapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_picture', models.FileField(null=True, upload_to=mainapp.models.upload_image_path)),
            ],
        ),
    ]
