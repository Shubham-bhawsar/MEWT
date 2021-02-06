from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login
from .models import Contacts

# Create your views here.
# Create your views here.
def index(request):
    return(HttpResponse("Hii There"))

def loginfun(request):
    if(request.method=="POST"):
        email=request.POST.get('Email')
        passw=request.POST.get('pass')
        email=email.split('@')[0]
        username = authenticate(username=email, password=passw)
        if username is not None:
            login(request,username)
            print(request.user.password)
            return redirect('/')
    # A backend authenticated the credentials
        else:
            return redirect('login')
    # No backend authenticated the credentials
        
    return render(request,"login.html")

def formfun(request):
    if(request.method=="POST"):
        email=request.POST.get('email')
        name=request.POST.get('name')
        message=request.POST.get('message')
        subject=request.POST.get('subject')
        contacts=Contacts(Email=email,Name=name,Message=message,Subject=subject)
        contacts.save()
    return render(request,'forms.html')


