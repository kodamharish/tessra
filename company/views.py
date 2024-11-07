from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from Tessra import settings
from django.core.mail import send_mail


# Create your views here.
def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')


def services(request):
    return render(request,'services.html')



def projects_on_going(request):
    return render(request,'projects/on-going.html')



def projects_up_coming(request):
    return render(request,'projects/up-coming.html')

def projects_completed(request):
    return render(request,'projects/completed.html')


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
        subject=subject
        txt='''
                Name :{}
                Email : {}
                Phone Number : {}
                Subject : {}
                Description : {}
                    '''
        message=txt.format(name,email,phone_number,subject,description)
        from_email=settings.EMAIL_HOST_USER
        to_list=[settings.EMAIL_HOST_USER]
        
        send_mail(subject, message,from_email,to_list,fail_silently=True)
        contact.save()
        messages.success(request, 'Thank you! We’ve received your message and will get back to you soon.')

        return redirect('contact_us')



        
    else:
        return render(request,'contact_us.html')