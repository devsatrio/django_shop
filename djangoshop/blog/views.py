from django.shortcuts import render
from kategori_artikel.models import category
from . import models

def index(request):
    data_kategori = category.objects.all().order_by('-id')
    data_blog = models.artikel.objects.all().order_by('-id')
    context = {
        'title':'Blog',
        'head':'Halaman Blog',
        'data_kategori':data_kategori,
        'data_blog':data_blog,
    }
    return render(request,'blog/index.html',context)

def show(request,judul):
    data_lain = models.artikel.objects.all().order_by('?')[0:6]
    data_blog = models.artikel.objects.get(slug=judul)
    context = {
        'title':'Blog',
        'data_blog':data_blog,
        'bloglain':data_lain,
    }
    return render(request,'blog/show.html',context)

def kategori(request,kategori):
    data_blog = models.artikel.objects.filter(kategori__slug=kategori)
    data_kategori = category.objects.all().order_by('-id')
    kategori = category.objects.get(slug=kategori)
    context = {
        'title':'Blog',
        'data_blog':data_blog,
        'data_kategori':data_kategori,
        'kategori':kategori,
    }
    print(kategori)
    return render(request,'blog/kategori.html',context)