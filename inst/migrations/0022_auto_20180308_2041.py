# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-08 20:41
from __future__ import unicode_literals

from django.db import migrations, models
import inst.models


class Migration(migrations.Migration):

    dependencies = [
        ('inst', '0021_auto_20180308_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='photo',
            field=models.ImageField(blank=True),
        ),
    ]
