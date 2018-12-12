from django.contrib import admin
from orm.models import Mahasiswa
# Register your models here.
class MahasiswaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Mahasiswa, MahasiswaAdmin)