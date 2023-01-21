from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.db import IntegrityError

# Create your views here.

def index(request):

    if request.method == 'GET':
         return render(request,'index.html',{
        'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                    password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('menu')
            except IntegrityError:
                return render(request,'index.html',{
                    'form': UserCreationForm,
                    'error': 'Username already exists'
                    })
            #register user
            
        return render(request,'index.html',{
            'form': UserCreationForm,
            'error': 'Passwords dont match'
            })
   
def menu(request):
    return render(request,'menu.html')

def log_out(request):
    logout(request)
    return redirect(index)