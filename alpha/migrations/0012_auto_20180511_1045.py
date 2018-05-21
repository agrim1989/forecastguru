# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-11 05:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0008_socialaccount_fg_points_total'),
        ('alpha', '0011_auto_20180510_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bettingforecast',
            name='forecast',
        ),
        migrations.RemoveField(
            model_name='bettingforecast',
            name='users',
        ),
        migrations.RemoveField(
            model_name='betting',
            name='bet_points_against',
        ),
        migrations.RemoveField(
            model_name='betting',
            name='bet_points_for',
        ),
        migrations.RemoveField(
            model_name='betting',
            name='betting_forecast',
        ),
        migrations.AddField(
            model_name='betting',
            name='forecast',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='alpha.ForeCast'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='betting',
            name='users',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='socialaccount.SocialAccount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='forecast',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='forecast',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 11, 10, 44, 29, 357055)),
        ),
        migrations.DeleteModel(
            name='BettingForecast',
        ),
    ]
