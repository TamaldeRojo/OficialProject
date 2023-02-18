from django.db import models
import os
import urllib
from django.core.files import File
from django.forms import TextInput,EmailInput
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

# Create your models here.

"""
class usersInfo(models.Model):
    countries = (
        ('LATAM','LTM'),('UNITED STATES OF AMERICA', 'USA'),('CANADA','CANADA')
    )
    first_Name = models.CharField(max_length=200)
    last_Name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    country = models.CharField(max_length=60, choices=countries)
    createdDate = models.DateTimeField(auto_now_add=True) 
"""

class InfoUsers(models.Model):
    countries = (
        ('LATAM','LATAM'),('USA', 'USA'),('CANADA','CANADA')
    )
    
    first_Name = models.CharField(max_length=200)
    last_Name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    country = models.CharField(max_length=60, choices=countries)
    createdDate = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class materiales(models.Model):
    nombre = models.CharField(max_length=250)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre + ' | $' + str(self.precio)
    
    
class posts(models.Model):
    
    title = models.CharField(max_length=250)
    username = models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name='social_post_author')
    description = models.TextField()
   # materiales = models.ForeignKey(materiales,on_delete=models.CASCADE, null=True)
    created_at = models.DateField(auto_now=True)
    img = models.ImageField(upload_to='pics/%y/%m/%d/')

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title + ' | '+ str(self.username)
    
class OpenAI(models.Model):
    nombre = models.CharField(max_length=250)
    photo = models.URLField(max_length=250)
    created_at = models.DateField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='OpenAI_owner_img')

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.nombre

class imgs(models.Model):
    ruta = models.URLField()
    nombre_img = models.CharField(max_length=150)

class constructoras(models.Model):
    nombre_c = models.CharField(max_length=200)
    password_c = models.CharField(max_length=200)
    email_c = models.CharField(max_length=250)
    text_c = models.TextField(max_length=500)

class Carausel(models.Model):
    img = models.ImageField(upload_to='pics/%y/%m/%d/')
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

