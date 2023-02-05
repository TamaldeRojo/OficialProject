from django.db import models
from django.contrib.auth.models import User

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



    
class carausel(models.Model):
    image = models.imagenField(upload_to = 'pics/%y/%m/%d/')
    title = models.CharField(max_length=150)
    sub_title = models.ChaField(max_lenght=100)

    def __Str__(self):
        return self.title