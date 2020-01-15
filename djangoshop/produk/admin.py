from django.contrib import admin
from django.contrib.auth.models import Group
from . import models

class ProductA(admin.ModelAdmin):
    readonly_fields = ['models.kategori.slug']
    list_display = ('models.barang.nama','models.barang.diskon','models.barang.harga')

myModels = [models.kategori, models.barang]
admin.site.register(myModels)
admin.site.unregister(Group)
admin.site.site_header = "Toko Mantab Jiwa"
