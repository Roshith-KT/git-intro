from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
import urllib.parse
from django.http import JsonResponse
from . models import Image


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


from django.shortcuts import redirect

def whatsapp_redirect(request):
    image=Image.objects.get(id=1)
    image_data=image.image
    company_phone_number = "+918547332099"  # Replace with the company's WhatsApp phone number
    message = "Hello! Roshith I'm interested in your products."  # Replace with your desired message
    whatsapp_url = f"https://wa.me/{company_phone_number}?text={message}&image={image_data}"
    return redirect(whatsapp_url)




def whatsapp_redirect_with_image(request):
    company_phone_number = "+917338247288"  # Replace with the company's WhatsApp phone number
    message = "Check out this image:"  # Replace with your desired message
    image=Image.objects.get(id=1)
    image_data=image.image

    # Image URL to be encoded in base64
    image_url = "https://staticimg.titan.co.in/Titan/Catalog/1805QM01_1.jpg?impolicy=pqmed&imwidth=640"  # Replace with the URL of your image
    image_base64 = urllib.parse.quote(image_url)

    # Combine the message and image base64 in the URL
    whatsapp_url = f"https://wa.me/{company_phone_number}?text={message}%0a{image_data}"
    return redirect(whatsapp_url)




