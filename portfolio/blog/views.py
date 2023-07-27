from django.shortcuts import render
from .models import *
# Create your views here.
def blog(request):
    content = {
        'title':'blog',
        'data' : BlogData.objects.all(),
        'category' : Category.objects.all(),
    }
    return render(request,'blog.html',content)

def test(request):
    return render(request, 'test.html')