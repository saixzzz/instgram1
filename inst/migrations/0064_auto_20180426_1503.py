# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-26 15:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inst', '0063_remove_photos_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
