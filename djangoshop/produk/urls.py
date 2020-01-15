from django.urls import path
from . import views
app_name = 'produk'
urlpatterns = [
    path('kategori/<slug:kategori>', views.category,name='category'),
    path('', views.index,name='index'),
    path('<int:kodebarang>', views.show,name='show'),
    
]