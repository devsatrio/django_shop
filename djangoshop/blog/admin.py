from django.contrib import admin
from . import models

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']
    list_display = ['judul','isi','tanggal']
admin.site.register(models.artikel,PostAdmin)
