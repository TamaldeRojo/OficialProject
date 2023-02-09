from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.db import IntegrityError
from django.views.generic import ListView,DetailView, CreateView

from .forms import createPost
from .models import posts,Carausel

import time


# Create your views here.
def index(request):
    

        
        obj = Carausel.objects.all()
        first_obj = obj.get(id=4).img.url
        s_obj = obj.get(id=5).img.url
        context = {
            'obj': obj, 'f_obj': first_obj, 's_obj': s_obj
        }
        if request.user.is_authenticated:
            return render(request, 'pages/menu.html')
        else:
            return render(request, 'pages/index.html', context)
        


            
        
def reg(request):

    if request.method == 'GET':
         return render(request,'pages/reg.html',{
        'form': UserCreationForm
        })
    else:
        #print(request.POST)
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                    password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('menu')
            except IntegrityError:
                return render(request,'pages/reg.html',{
                    'form': UserCreationForm,
                    'error': 'Username already exists'
                    })
            #register user
            
        return render(request,'pages/index.html',{
            'form': UserCreationForm,
            'error': 'Passwords dont match'
            })
# MENU VIEW ------------------------------------------------------------->
def menu(request):
    if request.user.is_authenticated:
        createP = createPost()
        if request.method == 'GET':
            objects_posts = posts.objects.all()
            return render(request,'pages/menu.html',{ 'post': objects_posts, 'createP': createP })
        elif request.method == 'POST':
            form = createPost(request.POST)
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect('menu')
       
    else: 
        return render(request,'pages/index.html') 

def post_detail(request,post_id):
    if request.user.is_authenticated:
        detail_posts = posts.objects.get(id=post_id)
        return render(request,'pages/post_detail.html',{ 'post': detail_posts })
    else: 
        return render(request,'pages/index.html') 

# END MENU VIEW ------------------------------------------------------------>
def log_out(request):
    logout(request)
    return redirect(index)

def log_in(request):
    if request.method == 'GET':
        return render(request,'pages/login.html',{
                'log' : AuthenticationForm
            })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
            return render(request,'pages/login.html',{
                'log' : AuthenticationForm,
                'error' : 'Username or password is incorrect'
                    })
        else:
            login(request, user)
            return redirect('menu')

def conocenos(request):
    return render(request,'pages/conocenos.html')

def empresas(request):
    return render(request,'pages/empresas.html')

def novedades(request):
    return render(request, 'pages/novedades.html')

def perfil(request):
    return render(request, 'pages/perfil.html')

def mensajes(request):
    return render(request, 'pages/mensajes.html')

def tendencias(request):
    return render(request, 'pages/tendencias.html')
