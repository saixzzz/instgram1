# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-22 08:54
from __future__ import unicode_literals

import autoslug.fields
import cities_light.abstract_models
import cities_light.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('name_ascii', models.CharField(blank=True, db_index=True, max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name_ascii')),
                ('geoname_id', models.IntegerField(blank=True, null=True, unique=True)),
                ('alternate_names', models.TextField(blank=True, default='', null=True)),
                ('display_name', models.CharField(max_length=200)),
                ('search_names', cities_light.abstract_models.ToSearchTextField(blank=True, db_index=True, default='', max_length=4000)),
                ('latitude', models.DecimalField(blank=True, decimal_places=5, max_digits=8, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=5, max_digits=8, null=True)),
                ('population', models.BigIntegerField(blank=True, db_index=True, null=True)),
                ('feature_code', models.CharField(blank=True, db_index=True, max_length=10, null=True)),
                ('timezone', models.CharField(blank=True, db_index=True, max_length=40, null=True, validators=[cities_light.validators.timezone_validator])),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
                'verbose_name_plural': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('name_ascii', models.CharField(blank=True, db_index=True, max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name_ascii')),
                ('geoname_id', models.IntegerField(blank=True, null=True, unique=True)),
                ('alternate_names', models.TextField(blank=True, default='', null=True)),
                ('code2', models.CharField(blank=True, max_length=2, null=True, unique=True)),
                ('code3', models.CharField(blank=True, max_length=3, null=True, unique=True)),
                ('continent', models.CharField(choices=[('OC', 'Oceania'), ('EU', 'Europe'), ('AF', 'Africa'), ('NA', 'North America'), ('AN', 'Antarctica'), ('SA', 'South America'), ('AS', 'Asia')], db_index=True, max_length=2)),
                ('tld', models.CharField(blank=True, db_index=True, max_length=5)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
                'verbose_name_plural': 'countries',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('name_ascii', models.CharField(blank=True, db_index=True, max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name_ascii')),
                ('geoname_id', models.IntegerField(blank=True, null=True, unique=True)),
                ('alternate_names', models.TextField(blank=True, default='', null=True)),
                ('display_name', models.CharField(max_length=200)),
                ('geoname_code', models.CharField(blank=True, db_index=True, max_length=50, null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.Country')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
                'verbose_name_plural': 'regions/states',
                'verbose_name': 'region/state',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.Country'),
        ),
        migrations.AddField(
            model_name='city',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='location.Region'),
        ),
        migrations.AlterUniqueTogether(
            name='region',
            unique_together=set([('country', 'name'), ('country', 'slug')]),
        ),
        migrations.AlterUniqueTogether(
            name='city',
            unique_together=set([('region', 'name'), ('region', 'slug')]),
        ),
    ]