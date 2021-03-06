# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-26 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0016_akademik_mahasiswa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='akademik',
            name='mahasiswa',
        ),
        migrations.RemoveField(
            model_name='jaringan',
            name='Grade',
        ),
        migrations.RemoveField(
            model_name='jaringan',
            name='nama',
        ),
        migrations.RemoveField(
            model_name='multimedia',
            name='Grade',
        ),
        migrations.RemoveField(
            model_name='multimedia',
            name='nama',
        ),
        migrations.RemoveField(
            model_name='rpl',
            name='Grade',
        ),
        migrations.RemoveField(
            model_name='rpl',
            name='nama',
        ),
        migrations.AddField(
            model_name='jaringan',
            name='AljabarLinear',
            field=models.CharField(choices=[('A+', 'A+'), ('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C+', 'C+'), ('C', 'C'), ('D', 'D')], default='D', max_length=2),
        ),
        migrations.AddField(
            model_name='jaringan',
            name='OrganisasiDanArsitekturKomputer',
            field=models.CharField(choices=[('A+', 'A+'), ('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C+', 'C+'), ('C', 'C'), ('D', 'D')], default='D', max_length=2),
        ),
        migrations.AddField(
            model_name='jaringan',
            name='PengantarJaringan',
            field=models.CharField(choices=[('A+', 'A+'), ('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C+', 'C+'), ('C', 'C'), ('D', 'D')], default='D', max_length=2),
        ),
        migrations.AddField(
            model_name='jaringan',
            name='PengantarSistemDigital',
            field=models.CharField(choices=[('A+', 'A+'), ('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C+', 'C+'), ('C', 'C'), ('D', 'D')], default='D', max_length=2),
        ),
        migrations.AddField(
            model_name='jaringan',
            name='PraktikumJaringan',
            field=models.CharField(choices=[('A+', 'A+'), ('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C+', 'C+'), ('C', 'C'), ('D', 'D')], default='D', max_length=2),
        ),
        migrations.AddField(
            model_name='jaringan',
            name='TeoriJaringan',
            field=models.CharField(choices=[('A+', 'A+'), ('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C+', 'C+'), ('C', 'C'), ('D', 'D')], default='D', max_length=2),
        ),
        migrations.AddField(
            model_name='multimedia',
            name='PengantarTeknologiInformasi',
            field=models.CharField(choices=[('A+', 'A+'), ('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C+', 'C+'), ('C', 'C'), ('D', 'D')], default='D', max_length=2),
        ),
        migrations.AddField(
            model_name='multimedia',
            name='PengolahanCitra',
            field=models.CharField(choices=[('A+', 'A+'), ('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C+', 'C+'), ('C', 'C'), ('D', 'D')], default='D', max_length=2),
        ),
        migrations.AddField(
            model_name='multimedia',
            name='PraktikumMultimedia',
            field=models.CharField(choices=[('A+', 'A+'), ('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C+', 'C+'), ('C', 'C'), ('D', 'D')], default='D', max_length=2),
        ),
        migrations.AddField(
            model_name='multimedia',
            name='Praktikum_Multimedia',
            field=models.CharField(choices=[('A+', 'A+'), ('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C+', 'C+'), ('C', 'C'), ('D', 'D')], default='D', max_length=2),
        ),
        migrations.AddField(
            model_name='multimedia',
            name='TeoriMultimedia',
            field=models.CharField(choices=[('A+', 'A+'), ('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C+', 'C+'), ('C', 'C'), ('D', 'D')], default='D', max_length=2),
        ),
        migrations.AddField(
            model_name='rpl',
            name='AlgoritmaDanPemrograman',
            field=models.CharField(choices=[('A+', 'A+'), ('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C+', 'C+'), ('C', 'C'), ('D', 'D')], default='D', max_length=2),
        ),
        migrations.AddField(
            model_name='rpl',
            name='GraffikaKomputer',
            field=models.CharField(choices=[('A+', 'A+'), ('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C+', 'C+'), ('C', 'C'), ('D', 'D')], default='D', max_length=2),
        ),
        migrations.AddField(
            model_name='rpl',
            name='LogikaInformatika',
            field=models.CharField(choices=[('A+', 'A+'), ('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C+', 'C+'), ('C', 'C'), ('D', 'D')], default='D', max_length=2),
        ),
        migrations.AddField(
            model_name='rpl',
            name='Pemrograman4',
            field=models.CharField(choices=[('A+', 'A+'), ('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C+', 'C+'), ('C', 'C'), ('D', 'D')], default='D', max_length=2),
        ),
        migrations.AddField(
            model_name='rpl',
            name='PraktikumGraffikaKomputer',
            field=models.CharField(choices=[('A+', 'A+'), ('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C+', 'C+'), ('C', 'C'), ('D', 'D')], default='D', max_length=2),
        ),
        migrations.AddField(
            model_name='rpl',
            name='PraktikumPemrograman4',
            field=models.CharField(choices=[('A+', 'A+'), ('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C+', 'C+'), ('C', 'C'), ('D', 'D')], default='D', max_length=2),
        ),
        migrations.DeleteModel(
            name='Akademik',
        ),
    ]
