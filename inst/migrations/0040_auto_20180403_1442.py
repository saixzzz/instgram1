# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-03 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inst', '0039_auto_20180403_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersettings',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='crop_x0.5-'),
        ),
    ]
