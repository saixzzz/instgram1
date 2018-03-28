# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-19 13:32
from __future__ import unicode_literals

from django.db import migrations, models
import inst.models


class Migration(migrations.Migration):

    dependencies = [
        ('inst', '0017_auto_20180216_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='photo',
            field=models.ImageField(blank=True, upload_to=inst.models.get_name_and_path),
        ),
        migrations.AlterField(
            model_name='usersettings',
            name='avatar',
            field=models.ImageField(blank=True, default='Default-image.jpeg', upload_to=inst.models.get_name_and_path),
        ),
        migrations.AlterField(
            model_name='usersettings',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
