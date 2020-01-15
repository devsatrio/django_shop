from django.urls import path
from . import views
app_name='blog'
urlpatterns = [
    path('',views.index,name='index'),
    path('<slug:judul>',views.show,name='show'),
    path('kategori/<slug:kategori>',views.kategori,name='kategori'),
]