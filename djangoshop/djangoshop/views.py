from django.shortcuts import render
from produk import models as barang
from blog import models as blogs
from kategori_artikel import models as katar
def index(request):
    Barangs = barang.barang
    KategoriBrg = barang.kategori
    Blogsnya = blogs.artikel
    Kategoriartikel = katar.category

    data_blog = Blogsnya.objects.all().select_related('kategori')
    data_kategori = KategoriBrg.objects.all().order_by('-id')[0:3]
    data_barang = Barangs.objects.all().order_by('-id')[0:8]

    context = {
        'title':'home',
        'head':'home page',
        'kategori':data_kategori,
        'barang':data_barang,
        'blog':data_blog,
    }
    return render(request,'index.html',context)