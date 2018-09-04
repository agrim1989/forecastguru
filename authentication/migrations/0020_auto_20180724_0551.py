# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-24 05:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0019_authentication_forecast_participated'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertisementPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField()),
            ],
            options={
                'ordering': ['-points'],
                'verbose_name_plural': 'Advertisement Points',
            },
        ),
        migrations.AlterField(
            model_name='authentication',
            name='last_login',
            field=models.DateField(default=datetime.date(2018, 7, 24)),
        ),
    ]
