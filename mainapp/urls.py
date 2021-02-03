
from django.contrib import admin
from django.urls import path
from .views import (index,
technician_service_computer_repair,
technician_service_desktop_remapair,
technician_service_mobile_repair,
technician_service_tablets_remapair,
technician_service_television_remapair,ItemDetail,comments,contact_us)

app_name = 'mainapp'


urlpatterns = [
    path('',index, name = "index_page"),
    path('mobilepair/',technician_service_mobile_repair,name = "mobilerepair"),
    path('desktoprepair/',technician_service_desktop_remapair,name = "desktoprepair"),
    path('tabletrepair/',technician_service_tablets_remapair,name = "tabletrepair"),
    path('televisionrepair/',technician_service_television_remapair,name = "televisonrepair"),
    path('computerrepair/',technician_service_computer_repair, name = "computerrepair"),
    path('technician/<slug>/', ItemDetail.as_view(), name='techniciandetail'),
    path('comments/', comments, name='comments'),
    path('contact/', contact_us, name='contact'),
    
   
]