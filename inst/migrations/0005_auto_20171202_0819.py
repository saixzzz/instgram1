# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-02 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inst', '0004_auto_20171201_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photos',
            name='03b2554e92083b96ea1960f579cecfdcd62d4ac4',
        ),
        migrations.AddField(
            model_name='photos',
            name='2aeaa3ba8a9035c1be7f7f48d0f16186a7906424',
            field=models.ImageField(default=1, upload_to=b''),
            preserve_default=False,
        ),
    ]