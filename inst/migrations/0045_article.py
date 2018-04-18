# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-10 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inst', '0044_auto_20180410_1017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('body', models.TextField(max_length=2000)),
                ('author', models.CharField(max_length=30)),
            ],
        ),
    ]