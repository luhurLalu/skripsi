from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import Mahasiswa,Multimedia,Jaringan,Rpl,Tesdasar
from management.mahasiswa import helpers


# Create your views here.


class ListMahasiswaView(View):
    def get(self, request):
        template = 'mahasiswa/index.html'
        mahasiswa = Mahasiswa.objects.all()
        data = {

            'mahasiswa' : mahasiswa,
        }
        return render(request, template, data)

class ListHasilRekomendasiMahasiswa(View):
    def get(self, request):
        template = 'mahasiswa/data_rekomendasi.html'
        mahasiswa = Mahasiswa.objects.all()
        data_rekomendasi = helpers.Nilai(mahasiswa).as_matrix()
        data = {

            'data_rekomendasi': data_rekomendasi
        }
        return render(request, template, data)
    
class ListDetailMahasiswa(View):
    def get(self,request):
        mhs = Mahasiswa.objects.all()
        a=helpers.Mhsis(mhs).index.get_values()[0]
        template = 'mahasiswa/detail_mahasiswa.html'
        detail_mahasiswa = helpers.Perangkingan()[a].as_matrix()        
        data = {      

            'detail_mahasiswa' : detail_mahasiswa,
        }
        return render(request,template,data)

class ListAkademikMahasiswa(View):
    def get(self,request):
        template = 'mahasiswa/kriteria/akademik.html'        
        akademik = helpers.Akademik().as_matrix()        
        data = {            
            'akademik' : akademik
        }
        return render(request,template,data)

class ListTestMahasiswa(View):
    def get(self,request):
        template = 'mahasiswa/kriteria/tes_dasar.html'
        tesdasar = helpers.TesDasar().as_matrix()        
        data = {            
            'tesdasar' : tesdasar
        }
        return render(request,template,data)

    