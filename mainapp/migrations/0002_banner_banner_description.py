# Generated by Django 3.1 on 2021-01-16 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='banner_description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
