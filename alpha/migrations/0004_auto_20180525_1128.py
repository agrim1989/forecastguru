# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-25 05:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alpha', '0003_auto_20180525_1007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='image',
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.URLField(default='http://www.projectsport.org.uk/wp-content/uploads/2015/01/multisports-large-icon.jpg'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='forecast',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 25, 11, 28, 15, 287152)),
        ),
    ]