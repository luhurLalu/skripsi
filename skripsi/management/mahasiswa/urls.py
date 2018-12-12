from django.conf.urls import url
from management.mahasiswa import views

urlpatterns = [
    url (r'^$', views.ListMahasiswaView.as_view(), name='view'),
    url (r'^data_rekomendasi$', views.ListHasilRekomendasiMahasiswa.as_view(), name='data_rekomendasi'),    
    url (r'^detail_mahasiswa', views.ListDetailMahasiswa.as_view(), name='detail_mahasiswa'),           

    url (r'^kriteria_akademik', views.ListAkademikMahasiswa.as_view(), name='kriteria_akademik'),
    url (r'^kriteria_test', views.ListTestMahasiswa.as_view(), name='kriteria_test'),
    # url(r"^detail/(?P<idmhs>\d+)/$", views.ListDetailMahasiswa.as_view(),name='detail_mahasiswa'),
]