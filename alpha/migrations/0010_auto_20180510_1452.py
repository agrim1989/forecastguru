# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-10 09:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alpha', '0009_auto_20180510_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forecast',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 10, 14, 52, 57, 727513)),
        ),
    ]
