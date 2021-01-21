
from django.contrib import admin
from django.urls import path,include
from config.settings.development import DEBUG,STATIC_URL,STATIC_ROOT,MEDIA_ROOT,MEDIA_URL
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('mainapp.urls')),
  
]
