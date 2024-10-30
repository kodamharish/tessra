from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name="index"),
    path('index',index,name="index"),

    path('about_us',about_us,name="about_us"),
    path('services',services,name="services"),


    

]

