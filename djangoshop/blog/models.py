from django.db import models
from django.utils.text import slugify
from kategori_artikel.models import category

class artikel(models.Model):
    judul = models.CharField(max_length=50)
    isi = models.TextField(max_length=1000)
    tanggal = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    slug = models.SlugField(editable=False,blank=True,null=True)
    kategori = models.ForeignKey(category,on_delete=models.SET_NULL, blank=True, null=True)
    gambar = models.ImageField(upload_to='images/')

    def save(self):
        self.slug = slugify(self.judul)
        super(artikel, self).save()

    def __str__(self):
        return self.judul
