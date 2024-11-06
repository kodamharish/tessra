from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *


# Create your views here.
def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')


def services(request):
    return render(request,'services.html')


def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        subject = request.POST.get('subject')
        description = request.POST.get('description')

        contact = Contact(
            name = name,
            email = email,
            phone_number = phone_number,
            subject = subject,
            description = description
        )
        contact.save()
        messages.success(request, 'Thank you! We’ve received your message and will get back to you soon.')

        return redirect('contact_us')



        
    else:
        return render(request,'contact_us.html')