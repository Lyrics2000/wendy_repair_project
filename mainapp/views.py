from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime
from .models import Banner
from .models import TechnicianDetails,Services,Testimonies
from django.views.generic import DetailView,View,ListView
from .forms import  CommentForm

# Create your views here.

def index(request):
    banners = Banner.objects.all()
    technicians =  TechnicianDetails.objects.all()

    context = {
        'banner' : banners,
        'technician' : technicians
    }
    
    return render(request,'homepage/index.html',context)


def technician_service_mobile_repair(request):
    tagname = 'MR'
    services = Services.objects.filter(technician_services__iexact = tagname)
    
    
    context = {
        'services' : services,
        'tagname' : tagname
    }
    return render(request,'technicians/index.html',context)

def technician_service_computer_repair(request):
    
    tagname = 'CR'
    services = Services.objects.filter(technician_services__iexact = tagname)
    
    
    context = {
        'services' : services,
        'tagname' : tagname
    }
    return render(request,'technicians/index.html',context)

def technician_service_desktop_remapair(request):
    tagname = 'DR'
    services = Services.objects.filter(technician_services__iexact = tagname)
    
    
    context = {
        'services' : services,
        'tagname' : tagname
    }
    return render(request,'technicians/index.html',context)

def technician_service_tablets_remapair(request):
    tagname = 'TBR'
    services = Services.objects.filter(technician_services__iexact = tagname)
    
    
    context = {
        'services' : services,
        'tagname' : tagname
    }
    return render(request,'technicians/index.html',context)

def technician_service_television_remapair(request):
    tagname = 'TR'
    services = Services.objects.filter(technician_services__iexact = tagname)
    
    
    context = {
        'services' : services,
        'tagname' : tagname
    }
    return render(request,'technicians/index.html',context)



class ItemDetail(DetailView):
    model = TechnicianDetails
    template_name = "detailedview/index.html"
    def get_context_data(self, **kwargs):
        services = Services.objects.all()
        testimonies = Testimonies.objects.all()
        form  = CommentForm()
        context = super().get_context_data(**kwargs)
        context["services"] = services
        context["testimonies"] = testimonies
        context["form"] = form
        return context

def comments(request):
    comment_id = request.POST.get("product_id")
    form = CommentForm(request.POST or None)
    if form.is_valid:
        instance = form.save(commit=False)
        technician = TechnicianDetails.objects.get(id=comment_id)
        instance.technician = technician
        instance.save()
    
    return redirect("/")
