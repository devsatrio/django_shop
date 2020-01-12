from django.shortcuts import render

def index(request):
    context = {
        'title':'Blog',
        'head':'Halaman Blog',
    }
    return render(request,'blog/index.html',context)
