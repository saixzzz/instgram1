# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-21 10:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inst', '0066_auto_20180426_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='current_user',
        ),
        migrations.RemoveField(
            model_name='friend',
            name='users',
        ),
        migrations.AlterModelOptions(
            name='photos',
            options={'verbose_name_plural': 'Photos'},
        ),
        migrations.AlterModelOptions(
            name='usersettings',
            options={'verbose_name_plural': 'UserSettings'},
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
    ]
