# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-10 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inst', '0043_auto_20180404_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersettings',
            name='bio',
            field=models.TextField(blank=True),
        ),
    ]
