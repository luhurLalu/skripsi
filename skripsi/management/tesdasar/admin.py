from django.contrib import admin
from orm.models import Tesdasar
# Register your models here.
class TesdasarAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tesdasar, TesdasarAdmin)