# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-25 04:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alpha', '0002_auto_20180524_2110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['-name'],
                'verbose_name_plural': 'Source',
            },
        ),
        migrations.AlterField(
            model_name='forecast',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alpha.Source'),
        ),
        migrations.AlterField(
            model_name='forecast',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 25, 10, 7, 33, 574416)),
        ),
    ]