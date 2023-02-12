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

class materiales(models.Model):
    precio = models.IntegerField(max_length=100)
    nombre = models.CharField(max_length=250)
    
class posts(models.Model):
    title = models.CharField(max_length=250)
    username = models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name='blog_posts')
    description = models.TextField()
    created_at = models.DateField(auto_now=True)
    img = models.ImageField(upload_to='pics/%y/%m/%d/')

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title + ' | '+ str(self.username)

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

