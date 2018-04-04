# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-03 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inst', '0041_usersettings_default_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersettings',
            name='default_avatar',
        ),
        migrations.AlterField(
            model_name='usersettings',
            name='avatar',
            field=models.ImageField(blank=True, default='Default-image.jpeg', upload_to='crop_x0.5-'),
        ),
    ]
