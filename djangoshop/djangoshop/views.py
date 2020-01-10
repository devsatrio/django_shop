from django.shortcuts import render

def index(request):
    context = {
        'title':'home',
        'head':'home page'
    }
    return render(request,'index.html',context)