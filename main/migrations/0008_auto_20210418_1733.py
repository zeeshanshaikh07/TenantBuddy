# Generated by Django 3.1.7 on 2021-04-18 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_room_rprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='rProfile',
            new_name='rPic',
        ),
    ]
