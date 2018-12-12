# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-10 03:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0020_auto_20181201_1916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jaringan',
            old_name='AljabarLinear',
            new_name='JaringanKomputer',
        ),
        migrations.RenameField(
            model_name='jaringan',
            old_name='OrganisasiDanArsitekturKomputer',
            new_name='Komdat',
        ),
        migrations.RenameField(
            model_name='jaringan',
            old_name='PengantarJaringan',
            new_name='Orkom',
        ),
        migrations.RenameField(
            model_name='jaringan',
            old_name='PengantarSistemDigital',
            new_name='PrakJaringanKomputer',
        ),
        migrations.RenameField(
            model_name='jaringan',
            old_name='PraktikumJaringan',
            new_name='PrakSistemOperasi',
        ),
        migrations.RenameField(
            model_name='jaringan',
            old_name='TeoriJaringan',
            new_name='Psd',
        ),
        migrations.RenameField(
            model_name='multimedia',
            old_name='AutoringTools',
            new_name='ArtificialIntelligent',
        ),
        migrations.RenameField(
            model_name='multimedia',
            old_name='InteraksiManusiaDanKomputer',
            new_name='GrafikaKomputer',
        ),
        migrations.RenameField(
            model_name='multimedia',
            old_name='PengantarTeknologiInformasi',
            new_name='IMK',
        ),
        migrations.RenameField(
            model_name='multimedia',
            old_name='PengolahanCitra',
            new_name='PrakGrafikaKomputer',
        ),
        migrations.RenameField(
            model_name='rpl',
            old_name='GraffikaKomputer',
            new_name='Adpl',
        ),
        migrations.RenameField(
            model_name='rpl',
            old_name='LogikaInformatika',
            new_name='PTI',
        ),
        migrations.RenameField(
            model_name='rpl',
            old_name='Pemrograman4',
            new_name='Pemrograman1',
        ),
        migrations.RenameField(
            model_name='rpl',
            old_name='PraktikumGraffikaKomputer',
            new_name='Pemrograman2',
        ),
        migrations.RenameField(
            model_name='rpl',
            old_name='PraktikumPemrograman4',
            new_name='PrakAlgoritmaDanPemrograman',
        ),
        migrations.RemoveField(
            model_name='multimedia',
            name='PraktikumMultimedia',
        ),
        migrations.RemoveField(
            model_name='multimedia',
            name='TeoriMultimedia',
        ),
        migrations.AddField(
            model_name='jaringan',
            name='SistemOperasi',
            field=models.CharField(choices=[('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C+', 'C+'), ('C', 'C'), ('D', 'D')], default='D', max_length=2),
        ),
        migrations.AddField(
            model_name='rpl',
            name='PrakPemrograman1',
            field=models.CharField(choices=[('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C+', 'C+'), ('C', 'C'), ('D', 'D')], default='D', max_length=2),
        ),
        migrations.AddField(
            model_name='rpl',
            name='PrakPemrograman2',
            field=models.CharField(choices=[('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C+', 'C+'), ('C', 'C'), ('D', 'D')], default='D', max_length=2),
        ),
        migrations.AddField(
            model_name='rpl',
            name='PrakSistemBasisData',
            field=models.CharField(choices=[('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C+', 'C+'), ('C', 'C'), ('D', 'D')], default='D', max_length=2),
        ),
        migrations.AddField(
            model_name='rpl',
            name='SistemBasisData',
            field=models.CharField(choices=[('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C+', 'C+'), ('C', 'C'), ('D', 'D')], default='D', max_length=2),
        ),
        migrations.AddField(
            model_name='rpl',
            name='SistemInformasi',
            field=models.CharField(choices=[('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C+', 'C+'), ('C', 'C'), ('D', 'D')], default='D', max_length=2),
        ),
        migrations.AddField(
            model_name='rpl',
            name='StrukturData',
            field=models.CharField(choices=[('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C+', 'C+'), ('C', 'C'), ('D', 'D')], default='D', max_length=2),
        ),
    ]
