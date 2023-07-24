from django.shortcuts import render

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
    return render(request, 'contact.html', content)
