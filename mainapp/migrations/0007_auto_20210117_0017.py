# Generated by Django 3.1 on 2021-01-16 21:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20210117_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='techniciandetails',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.uuid4, unique=True),
        ),
    ]
