from django.db import models

class kategori(models.Model):
    nama = models.CharField(max_length=50)
    gambar = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.nama

class barang(models.Model):
    nama = models.CharField(max_length=70)
    deskripsi = models.TextField()
    stok = models.IntegerField()
    diskon = models.IntegerField()
    harga = models.IntegerField()
    kategori = models.ForeignKey(kategori,on_delete=models.SET_NULL,
        blank=True,
        null=True,)
    gambar = models.ImageField(upload_to='images/')

    def __str__(self):
        return "%s %s %s" % (self.nama, self.stok, self.harga)
