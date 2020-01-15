from django.db import models
from django.utils.text import slugify

class category(models.Model):
    nama = models.CharField(max_length=50)
    tanggal = models.DateTimeField(auto_now_add=True, blank=True)
    slug = models.SlugField(editable=False,blank=True,null=True)

    def save(self):
        self.slug = slugify(self.nama)
        super(category, self).save()

    def __str__ (self):
        return self.nama
