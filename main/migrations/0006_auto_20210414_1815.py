# Generated by Django 3.1.7 on 2021-04-14 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210326_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='rBathroom',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='rType',
            field=models.CharField(default='Flat', max_length=100),
            preserve_default=False,
        ),
    ]
