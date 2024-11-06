from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name="index"),
    path('index',index,name="index"),

    path('about',about,name="about"),
    path('services',services,name="services"),
    path('contact_us',contact_us,name="contact_us"),



    

]

