from import_export import resources
from . import models

class PersonResource(resources.ModelResource):
    class Meta:
        model = models.category