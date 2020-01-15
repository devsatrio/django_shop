from django.shortcuts import render
from . import models

def index(request):
    data_kategori = models.kategori.objects.all().order_by('-id')
    data_barang = models.barang.objects.all().order_by('-id')
    context = {
        'title':'Produk',
        'head':'Semua Produk',
        'data_kategori':data_kategori,
        'data_barang':data_barang,
    }
    return render(request,'produk/index.html',context)

def show(request, kodebarang):
    data_barang = models.barang.objects.get(id=kodebarang)
    other = models.barang.objects.all().order_by('?')[0:4]
    context={
        'title':'Detail Produk',
        'head':'Detail Produk',
        'barang':data_barang,
        'other_barang':other,
    }
    return render(request,'produk/show.html',context)

def category(request, kategori):
    data_kategori = models.kategori.objects.get(slug=kategori)
    data_barang = models.barang.objects.filter(kategori__slug=kategori).order_by('-id')
    context={
        'title':'Produk',
        'head':'Detail Produk',
        'data_barang':data_barang,
        'kategori':data_kategori,
    }
    return render(request,'produk/category.html',context)
