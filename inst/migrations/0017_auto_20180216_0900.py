# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-16 09:00
from __future__ import unicode_literals

from django.db import migrations, models
import inst.models


class Migration(migrations.Migration):

    dependencies = [
        ('inst', '0016_auto_20180216_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersettings',
            name='avatar',
            field=models.ImageField(blank=True),
        ),
    ]
