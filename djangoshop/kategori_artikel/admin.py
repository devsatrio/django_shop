from django.contrib import admin
from . import models
from import_export import resources
from import_export.admin import ImportExportModelAdmin

    

class BookResource(resources.ModelResource):

    class Meta:
        model = models.category

class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource
    list_display = ['nama','slug','tanggal']
    readonly_fields = ['slug']

admin.site.register(models.category,BookAdmin)
