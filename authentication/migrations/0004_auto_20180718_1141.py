# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-18 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20180718_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joiningpoints',
            name='points',
            field=models.CharField(max_length=100),
        ),
    ]
