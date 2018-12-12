from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from app.config import setting

urlpatterns = [    
    url(r'^admin/', admin.site.urls),
    url(r'^mahasiswa/', include('management.mahasiswa.urls', namespace='mahasiswa')),
]