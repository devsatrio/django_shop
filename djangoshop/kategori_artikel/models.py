from django.db import models

class category(models.Model):
    nama = models.CharField(max_length=50)
    tanggal = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__ (self):
        return self.nama
