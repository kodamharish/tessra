from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name="index"),
    path('index',index,name="index"),
    path('about',about,name="about"),
    path('services',services,name="services"),
    path('projects_on_going',projects_on_going,name="projects_on_going"),
    path('projects_up_coming',projects_up_coming,name="projects_up_coming"),
    path('projects_completed',projects_completed,name="projects_completed"),

    path('contact_us',contact_us,name="contact_us"),
  

]

