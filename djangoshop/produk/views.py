from django.shortcuts import render
from . import models
def index(request):
    data_kategori = models.kategori.objects.all()
    data_barang = models.barang.objects.all()
    context = {
        'title':'Produk',
        'head':'Halman Produk',
        'data_kategori':data_kategori,
        'data_barang':data_barang,
    }
    return render(request,'produk/index.html',context)
