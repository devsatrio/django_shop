from django.shortcuts import render

def index(request):
    context={
        'title':'contact',
    }
    return render(request,'contact/index.html',context)
