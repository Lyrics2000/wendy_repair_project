from django.db import models
from django.db.models.query import ModelIterable
from django.db import models
import random
import os
from django.db.models import Q
from datetime import datetime
from django.utils.timezone import now
from django.db.models.signals import pre_save
from django.shortcuts import reverse
from mainapp.utils import unique_slug_generator,category_unique_slug_generator
import uuid

# Create your models here.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance,filename):
    new_filename = random.randint(1,999992345677653234)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext = ext)
    return "products/{new_filename}/{final_filename}".format(new_filename=new_filename,final_filename = final_filename )


def upload_image_technician(instance,filename):
    new_filename = random.randint(1,999992345677653234)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext = ext)
    return "technician/{new_filename}/{final_filename}".format(new_filename=new_filename,final_filename = final_filename )


class Banner(models.Model):
    banner_picture = models.FileField(upload_to = upload_image_path ,null=True,blank=False)
    banner_description = models.CharField(max_length=200,blank =True , null= True)

    def __str__(self):
        return self.banner_description


class TechnicianDetails(models.Model):
    technician_name  = models.CharField(max_length=100)
    email = models.EmailField()
    technician_picture = models.FileField(upload_to = upload_image_technician ,null=True,blank=False)
    technician_overview = models.TextField()
    shop_location = models.CharField(max_length=150, blank=True,null=True)
    phone_number = models.CharField(max_length=150, blank=True,null=True)
    email = models.CharField(max_length=150, blank=True,null=True)
    facebook_url = models.CharField(max_length=150, blank=True,null=True)
    twitter_url = models.CharField(max_length=150, blank=True,null=True)
    youtube_url = models.CharField(max_length=150, blank=True,null=True)
    vimeo_url = models.CharField(max_length=150, blank=True,null=True)
    slug = models.SlugField(blank=True,unique=True,default=uuid.uuid4)

    def __str__(self):
        return self.technician_name

    def get_absolute_url(self):
        return reverse("mainapp:techniciandetail", kwargs={
            'slug': self.slug
        })
def product_presave_reciver(sender, instance, *args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_presave_reciver,sender = TechnicianDetails)   


class Services(models.Model):
    CHOICES = (
        ('MR', 'Mobile Repair'),
        ('CR', 'Computer Repair'),
        ('TR', 'Television Repair'),
        ('DR', 'Desktop Repair'),
        ('TBR', 'Tablet Repair'),
    )
    technician =  models.ForeignKey(TechnicianDetails,on_delete= models.CASCADE)
    technician_services = models.CharField(max_length=300, choices = CHOICES)

    def __str__(self):
        return self.technician_services
    

class Testimonies(models.Model):
    technician  = models.ForeignKey(TechnicianDetails,on_delete= models.CASCADE)
    Clients_Name = models.CharField(max_length=150)
    comment  =  models.TextField()
    date = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.Clients_Name
    
    