# Generated by Django 3.2 on 2021-04-22 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_owner_oprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='oProfile',
            field=models.ImageField(default='main', upload_to=''),
        ),
    ]
