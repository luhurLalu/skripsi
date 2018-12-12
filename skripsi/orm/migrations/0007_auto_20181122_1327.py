# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-22 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0006_auto_20181122_1319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='multimedia',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='rpl',
            name='grade',
        ),
        migrations.AddField(
            model_name='multimedia',
            name='Grade',
            field=models.CharField(choices=[('A+', 'A+'), ('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C+', 'C+'), ('C', 'C'), ('D', 'D')], default='A+', max_length=2),
        ),
        migrations.AddField(
            model_name='rpl',
            name='Grade',
            field=models.CharField(choices=[('A+', 'A+'), ('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C+', 'C+'), ('C', 'C'), ('D', 'D')], default='A+', max_length=2),
        ),
    ]
