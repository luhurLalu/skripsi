from django.contrib import admin
from orm.models import Multimedia
# Register your models here.
class MultimediaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Multimedia, MultimediaAdmin)