from django.contrib import admin
from orm.models import Jaringan
# Register your models here.
class JaringanAdmin(admin.ModelAdmin):
    pass
admin.site.register(Jaringan, JaringanAdmin)
