from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=="POST":
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')       
        if password==cpassword:
            if User.objects.filter(username=username).exists() and User.objects.filter(email=email).exists():
                messages.info(request,'USERNAME AND EMAIL TAKEN')
                return redirect('/register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'USERNAME TAKEN')
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'EMAIL TAKEN')
                return redirect('/register')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                return redirect('/login/')
                
        else:
            messages.info(request,'PASSOWRD NOT MATCHING')
            return redirect('/register/')
        
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'INVALID CREDENTIALS')
            return redirect('/login/')
    return render(request,'login.html')
        

def logout(request):
    auth.logout(request)
    return redirect('/')
    
