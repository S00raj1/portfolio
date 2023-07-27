from django.shortcuts import render, redirect
from django.contrib import messages
from . models import *

# Create your views here.

def home(request):
    content = {
        'title' : 'Home'
    }
    return render(request, 'home.html', content)
    
def projects(request):
    content = {
        'title' : 'Projects'
    }
    return render(request, 'projects.html', content)

def services(request):
    content = {
        'title' : 'Services'
    }
    return render(request, 'services.html', content)

def contact(request):
    content = {
        'title' : 'Contact'
    }
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        msg = Contact.objects.create(name=name, email=email, message=message)
        msg.save()
        messages.success(request,'You will be contacted soon..')
        return redirect('contact')
    return render(request, 'contact.html', content)



