from django.db import models
from django.contrib.auth.models import User
import time
import os

class Mahasiswa(models.Model):
    nim = models.CharField(max_length=100, blank=True, null=True)
    nama = models.CharField(max_length=100, blank=True, null=True)
    PRIA = 'PR'
    WANITA = 'WN'
    JK_CHOICES  = (
        (PRIA, 'Pria'),
        (WANITA, 'Wanita'),

    )
    jenis_kelamin = models.CharField(
        max_length=2,
        choices=JK_CHOICES,
        default=PRIA,
    )
    tgl_lahir = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    agama = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nama

    class Meta:
        db_table = 'mahasiswa'
        ordering = ['id']


A   = 'A'
Bb  = 'B+'
B   = 'B'
Cc  = 'C+'
C   = 'C'
D   = 'D'
grade  = (        
    (A, 'A'),
    (Bb, 'B+'),
    (B, 'B'),
    (Cc, 'C+'),
    (C, 'C'),
    (D,'D')
)         

class Multimedia(models.Model):
    mahasiswa = models.OneToOneField(Mahasiswa, on_delete=models.CASCADE, related_name='multimedias')             

    IMK = models.CharField(
        max_length=2,
        choices=grade,
        default=D,
    )   
    ArtificialIntelligent = models.CharField(
        max_length=2,
        choices=grade,
        default=D,
    )
    GrafikaKomputer = models.CharField(
        max_length=2,
        choices=grade,
        default=D,
    )    
    PrakGrafikaKomputer = models.CharField(
        max_length=2,
        choices=grade,
        default=D,
    )     
    def __str__(self):
        return self.mahasiswa.nama

    class Meta:
        db_table = 'multimedia'
        ordering = ['id']

class Jaringan(models.Model):
    mahasiswa = models.OneToOneField(Mahasiswa, on_delete=models.CASCADE, related_name='jaringans')    

    Psd = models.CharField(
        max_length=2,
        choices=grade,
        default=D,
    )
    Orkom = models.CharField(
        max_length=2,
        choices=grade,
        default=D,
    )
    SistemOperasi = models.CharField(
        max_length=2,
        choices=grade,
        default=D,
    )
    PrakSistemOperasi = models.CharField(
        max_length=2,
        choices=grade,
        default=D,
    )
    Komdat = models.CharField(
        max_length=2,
        choices=grade,
        default=D,
    )
    JaringanKomputer = models.CharField(
        max_length=2,
        choices=grade,
        default=D,
    )
    PrakJaringanKomputer = models.CharField(
        max_length=2,
        choices=grade,
        default=D,
    )                
    def __str__(self):
        return self.mahasiswa.nama

    class Meta:
        db_table = 'jaringan'
        ordering = ['id']

class Rpl(models.Model):
    mahasiswa = models.OneToOneField(Mahasiswa, on_delete=models.CASCADE, related_name='rpls')
           
    AlgoritmaDanPemrograman = models.CharField(
        max_length=2,
        choices=grade,
        default=D,
    )
    PrakAlgoritmaDanPemrograman = models.CharField(
        max_length=2,
        choices=grade,
        default=D,
    )
    PTI = models.CharField(
        max_length=2,
        choices=grade,
        default=D,
    )
    StrukturData = models.CharField(
        max_length=2,
        choices=grade,
        default=D,
    )
    SistemBasisData = models.CharField(
        max_length=2,
        choices=grade,
        default=D,
    )
    PrakSistemBasisData = models.CharField(
        max_length=2,
        choices=grade,
        default=D,
    )
    Pemrograman1 = models.CharField(
        max_length=2,
        choices=grade,
        default=D,
    )
    PrakPemrograman1 = models.CharField(
        max_length=2,
        choices=grade,
        default=D,
    )
    SistemInformasi = models.CharField(
        max_length=2,
        choices=grade,
        default=D,
    )
    Pemrograman2 = models.CharField(
        max_length=2,
        choices=grade,
        default=D,
    )
    PrakPemrograman2 = models.CharField(
        max_length=2,
        choices=grade,
        default=D,
    )
    Adpl = models.CharField(
        max_length=2,
        choices=grade,
        default=D,
    )
    
    def __str__(self):
        return self.mahasiswa.nama

    class Meta:
        db_table = 'rpl'
        ordering = ['id']



class Tesdasar(models.Model):
    mahasiswa = models.OneToOneField(Mahasiswa, on_delete=models.CASCADE, related_name='tesdasars')    
    NilaiMultimedia = models.CharField(max_length=2, blank=False, null=True)
    NilaiJaringan = models.CharField(max_length=2, blank=False, null=True)
    NilaiRPL = models.CharField(max_length=2, blank=False, null=True)

    def __str__(self):
        return self.mahasiswa.nama

    class Meta:
        db_table = 'tesdasar'
        ordering = ['id']