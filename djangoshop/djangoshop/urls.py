
from django.contrib import admin
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('produk/',include('produk.urls')),
    path('',views.index,name='index')
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)