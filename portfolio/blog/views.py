from django.shortcuts import render
from .models import *
# Create your views here.
def blog(request):
    content = {
        'title':'blog',
        'data' : BlogData.objects.all()
    }
    return render(request,'blog.html',content)

def test_data(request):
    return render(request, 'test.html')