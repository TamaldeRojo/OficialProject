from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
import requests
import random

from .forms import createPost
from .models import posts,Carausel, OpenAI
import openai



# Create your views here.
def index(request):
    
        obj = Carausel.objects.all()
        first_obj = obj.get(id=6).img.url
        s_obj = obj.get(id=7).img.url
        t_obj = obj.get(id=7).img.url
        l_obj = obj.get(id=7).img.url
        context = {
            'obj': obj, 'f_obj': first_obj, 's_obj': s_obj, 't_obj':t_obj,'l_obj':l_obj
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
                login(request,user, backend='django.contrib.auth.backends.ModelBackend')
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

            img_query = OpenAI.objects.all()
            imgs = img_query.latest('id')
            print("segunda "+ str(imgs))

            objects_posts = posts.objects.all()
            return render(request,'pages/menu.html',{ 'post': objects_posts, 'createP': createP, 'imgs' : imgs })

        elif request.method == 'POST':
            if 'form_a_submit' in request.POST:

                form = createPost(request.POST, request.FILES)
                if form.is_valid():
                    new_post = form.save(commit=False)
                    new_post.username = request.user
                    new_post.save()

                    return redirect('menu')
                
            elif 'form_b_submit' in request.POST:
                 #---------------DALL E 2---------------------------------------------- 
                    dalle = request.POST
                    prompt = dalle['prompt']
                
                    response = requests.post('https://api.openai.com/v1/images/generations',
                                                headers={'Authorization': 'Bearer ' + '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'},
                                                json={
                                                    'model': 'image-alpha-001',
                                                    'prompt': prompt,
                                                })

                    image_url = response.json()['data'][0]['url']
                    print("Primera " +image_url)

                    openai_obj = OpenAI.objects.create(nombre=str(request.user)+'_|_'+str(random.randint(0,1000)),photo=image_url,owner=request.user)
                    openai_obj.save()

                    
                    return redirect('menu')  
                   #--------------End DALL E 2 ------------------------------------------
                
       
    else: 
        return render(request,'pages/index.html', {'lol', image_url}) 
#END MENU----------------------------------------------------------------------------
def post_detail(request,post_id):
    if request.user.is_authenticated:
        detail_posts = posts.objects.get(id=post_id)
        return render(request,'pages/post_detail.html', {'post': detail_posts})
    else: 
        return render(request,'pages/index.html') 

# END MENU VIEW ------------------------------------------------------------>
def log_out(request):
    logout(request)
    return redirect(index)

def log_in(request):
    if request.method == 'GET':
        return render(request,'account/login.html',{
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
