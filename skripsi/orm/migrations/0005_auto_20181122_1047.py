# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-22 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0004_auto_20181122_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jaringan',
            name='Grade',
            field=models.CharField(choices=[(('A+',), 'A+'), (('A',), 'A'), (('B+',), 'B+'), (('B',), 'B'), (('C+',), 'C+'), (('C',), 'C'), (('D',), 'D')], default=('A+',), max_length=2),
        ),
    ]
