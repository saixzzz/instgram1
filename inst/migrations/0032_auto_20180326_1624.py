# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-26 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inst', '0031_auto_20180326_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='photo',
            field=models.ImageField(blank=True, upload_to='crop_x1'),
        ),
    ]
