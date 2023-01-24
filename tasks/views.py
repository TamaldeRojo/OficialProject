from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.db import IntegrityError


# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

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
   
def menu(request):
    return render(request,'pages/menu.html')

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
   
