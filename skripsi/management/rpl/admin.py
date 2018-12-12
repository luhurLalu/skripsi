from django.contrib import admin
from orm.models import Rpl
# Register your models here.
class RplAdmin(admin.ModelAdmin):
    pass
admin.site.register(Rpl, RplAdmin)