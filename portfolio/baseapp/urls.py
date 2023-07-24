from django.urls import path
from .views import *

urlpatterns=[
    path('', home,name="home"),
    path('projects/', projects,name="projects"),
    path('services/', services,name="services"),
    path('contact/', contact,name="contact"),
]