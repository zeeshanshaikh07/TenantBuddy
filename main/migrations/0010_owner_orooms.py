# Generated by Django 3.1.7 on 2021-04-18 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210418_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='oRooms',
            field=models.IntegerField(default=0),
        ),
    ]
