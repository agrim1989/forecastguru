# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-09 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0036_auto_20180809_0604'),
    ]

    operations = [
        migrations.AddField(
            model_name='authentication',
            name='points_lost_public',
            field=models.IntegerField(default=0),
        ),
    ]
