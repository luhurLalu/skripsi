# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-22 14:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0012_akademik'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='akademik',
            name='mahasiswa',
        ),
    ]
