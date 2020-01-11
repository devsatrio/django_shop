from django.shortcuts import render

def index(request):
    context = {
        'title':'Produk'
    }
    return render(request,'produk/index.html',context)
