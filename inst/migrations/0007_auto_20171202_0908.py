# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-02 09:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inst', '0006_auto_20171202_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='photos',
            field=models.ImageField(upload_to=b'', verbose_name=b'43296f47124544b66f0a6658035d10c35fa941f9'),
        ),
    ]
