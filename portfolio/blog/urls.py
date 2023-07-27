from django.urls import path
from .views import *

urlpatterns = [
    path('', blog, name="blog"),
    path('test/', test, name="test"),
]